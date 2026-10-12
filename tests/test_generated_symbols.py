import importlib
import pkgutil

from pydantic import BaseModel, TypeAdapter, ValidationError
from pytest import raises

import vanilla_mcdoc
from vanilla_mcdoc.data.dialog.Dialog import Dialog
from vanilla_mcdoc.data.loot.LootContextParamSets import LootContextParamSets
from vanilla_mcdoc.data.loot.LootPoolEntry import LootPoolEntry, LootPoolEntryAlternatives, LootPoolEntryItem
from vanilla_mcdoc.data.loot.LootTable import LootTable
from vanilla_mcdoc.data.number_provider.FloatNumberProvider import FloatNumberProvider
from vanilla_mcdoc.data.recipe.Smelting import Smelting
from vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate


def test_every_generated_module_imports() -> None:
    """Catches generated code that can't even be defined, e.g. a field that shadows its own type (`BlockState: BlockState`)."""
    failures: dict[str, str] = {}
    for module_info in pkgutil.walk_packages(vanilla_mcdoc.__path__, "vanilla_mcdoc."):
        try:
            importlib.import_module(module_info.name)
        except Exception as error:  # noqa: BLE001  # pylint: disable=broad-exception-caught  # Any error, so they're all reported
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


def test_discriminated_unions_pick_by_tag() -> None:
    """Unions of models with a "type" (or similar) are picked between by it, here with the "minecraft:" left out. This
    one is recursive (entries can have child entries), where pydantic loses the tags if it has to find them itself."""
    entry: BaseModel = TypeAdapter(LootPoolEntry).validate_python({"type": "minecraft:alternatives", "children": [{"type": "item", "name": "minecraft:stone"}]})
    assert isinstance(entry, LootPoolEntryAlternatives)
    assert isinstance(entry.children[0], LootPoolEntryItem)
    with raises(ValidationError, match="does not match any of the expected tags"):
        TypeAdapter(LootPoolEntry).validate_python({"type": "minecraft:not_an_entry"})


def test_enums_of_ids_can_have_their_namespace() -> None:
    """e.g. a loot table's type, which vanilla writes with "minecraft:", but whose enum values don't have it."""
    table = LootTable.model_validate({"type": "minecraft:archaeology"})
    assert table.type == LootContextParamSets.ARCHAEOLOGY
    assert table.model_dump(mode="json", exclude_none=True) == {"type": "minecraft:archaeology"}


def test_unions_only_accept_their_own_types() -> None:
    """minecraft:score is a loot table number provider, not a context float one. vanilla-mcdoc's `%none: union {}` (for
    when there's no type, which isn't allowed) used to become a member that accepted any type."""
    with raises(ValidationError, match=r"Input tag 'minecraft:score' found using tag\(\) does not match any of the expected tags"):
        TypeAdapter(FloatNumberProvider).validate_python({"type": "minecraft:score", "target": "this", "score": "a"})


def test_json_schemas_refer_to_other_models() -> None:
    """Models use each other's validators (see base.py), which pydantic can't write a JSON schema for itself. So each one
    is written once in $defs and referred to, even ones that use themselves (all_of's predicates are block predicates)."""
    schema = TypeAdapter(BlockPredicate).json_schema()
    assert schema["$defs"]["BlockPredicateAllOf"]["properties"]["predicates"]["items"] == {"$ref": "#/$defs/BlockPredicate"}
    assert {"$ref": "#/$defs/BlockPredicateAllOf"} in schema["$defs"]["BlockPredicate"]["oneOf"]
