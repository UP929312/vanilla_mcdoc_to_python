import importlib
import pkgutil

from pydantic import BaseModel, TypeAdapter, ValidationError
from pytest import raises

import vanilla_mcdoc
from vanilla_mcdoc.data.dialog.Dialog import Dialog
from vanilla_mcdoc.data.recipe.Smelting import Smelting


def test_every_generated_module_imports() -> None:
    """Catches generated code that can't even be defined, e.g. a field that shadows its own type (`BlockState: BlockState`)."""
    failures: dict[str, str] = {}
    for module_info in pkgutil.walk_packages(vanilla_mcdoc.__path__, "vanilla_mcdoc."):
        try:
            importlib.import_module(module_info.name)
        except Exception as error:  # pylint: disable=broad-exception-caught
            failures[module_info.name] = f"{type(error).__name__}: {error}"
    assert not failures, "\n".join(f"{name}: {error}" for name, error in failures.items())


def test_models_can_be_used() -> None:
    """Their annotations use names only imported under TYPE_CHECKING, which base.py makes available on first use."""
    recipe = Smelting(ingredient="minecraft:iron_ore", result="minecraft:iron_ingot", cookingtime=200)
    assert recipe.model_dump(exclude_none=True)["result"] == "minecraft:iron_ingot"
    validated = Smelting.model_validate({"type": "minecraft:smelting", "ingredient": "minecraft:iron_ore", "result": {"id": "minecraft:iron_ingot"}, "cookingtime": 200})
    assert validated.model_dump(exclude_none=True)["result"] == {"id": "minecraft:iron_ingot"}  # model_validate doesn't go through __init__
    with raises(ValidationError):
        Smelting.model_validate({"type": "minecraft:smelting", "ingredient": "minecraft:iron_ore", "result": {"id": 5}, "cookingtime": 200})


def test_unions_of_models_can_be_used() -> None:
    """Unions aren't classes, so they're validated with a TypeAdapter (which builds the models without model_rebuild).
    Each Dialog type splits again by after_action, so this also checks it isn't a (broken) discriminated union."""
    dialog: BaseModel = TypeAdapter(Dialog).validate_python({"type": "minecraft:notice", "title": "Hello", "after_action": "none", "pause": False})
    assert dialog.model_dump(exclude_none=True) == {"type": "minecraft:notice", "title": "Hello", "after_action": "none", "pause": False}
