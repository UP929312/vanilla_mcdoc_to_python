import importlib
import pkgutil
import uuid

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


def test_vanilla_files_are_their_models() -> None:
    """vanilla_mcdoc.vanilla has every one of vanilla's files, as the model it is. A file next to a folder of the same name
    (sheep.json and sheep/) is fine, as the constant's in capitals."""
    from vanilla_mcdoc.data.recipe.Recipe import RecipeCraftingShapeless
    from vanilla_mcdoc.vanilla.assets.lang import EN_US
    from vanilla_mcdoc.vanilla.data.loot_table.entities import SHEEP
    from vanilla_mcdoc.vanilla.data.loot_table.entities.sheep import WHITE
    from vanilla_mcdoc.vanilla.data.recipe import TNT_MINECART

    assert isinstance(TNT_MINECART, RecipeCraftingShapeless)
    assert TNT_MINECART.model_dump(mode="json", exclude_unset=True) == {
        "type": "minecraft:crafting_shapeless", "ingredients": ["minecraft:tnt", "minecraft:minecart"], "result": {"id": "minecraft:tnt_minecart"},
    }
    assert isinstance(SHEEP, LootTable) and isinstance(WHITE, LootTable)
    assert EN_US["block.minecraft.stone"] == "Stone"


def test_both_kinds_of_model_rotation() -> None:
    """The old axis and angle one (deprecated, but vanilla's models still use it), and one with an angle per axis, which
    are extra keys pydantic checks."""
    from vanilla_mcdoc.assets.model.ModelElementRotation import ModelElementRotation, ModelElementRotationStruct1, ModelElementRotationStruct2

    assert isinstance(TypeAdapter(ModelElementRotation).validate_python({"origin": [8, 8, 8], "axis": "y", "angle": 45, "rescale": True}), ModelElementRotationStruct1)
    per_axis: object = TypeAdapter(ModelElementRotation).validate_python({"origin": [8, 8, 8], "x": 22.5})
    assert isinstance(per_axis, ModelElementRotationStruct2) and per_axis.model_dump()["x"] == 22.5
    with raises(ValidationError):
        TypeAdapter(ModelElementRotation).validate_python({"origin": [8, 8, 8], "w": 45})  # Not an axis


def test_items_keep_their_custom_nbt() -> None:
    from vanilla_mcdoc.world.item.ItemBase import ItemBase

    item = ItemBase.model_validate({"Damage": 3, "MyPack": {"level": 2}})
    assert item.model_extra == {"MyPack": {"level": 2}}


def test_uuids_become_minecrafts_four_ints() -> None:
    from vanilla_mcdoc.minecraft_types import uuid_to_int_array

    assert uuid_to_int_array(uuid.UUID("f81d4fae-7dec-11d0-a765-00a0c91e6bf6")) == (-132296786, 2112623056, -1486552928, -920753162)
