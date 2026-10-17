import json
import zipfile
from pathlib import Path

from pydantic import TypeAdapter
from pytest import MonkeyPatch

import vanilla_files
from vanilla_files import constant_name, python_code, python_name
from vanilla_mcdoc.assets.model.ModelElementRotation import ModelElementRotation
from vanilla_mcdoc.data.recipe.Recipe import Recipe

TNT_MINECART = {"type": "minecraft:crafting_shapeless", "ingredients": ["minecraft:tnt", "minecraft:minecart"], "result": {"id": "minecraft:tnt_minecart"}}


def test_names_are_python_names() -> None:
    assert (constant_name("tnt_minecart"), constant_name("11")) == ("TNT_MINECART", "_11")  # 11 is a jukebox song
    assert (python_name("entities"), python_name("1"), python_name("import")) == ("entities", "_1", "import_")  # Folders


def test_models_become_the_python_that_makes_them() -> None:
    imports: dict[tuple[str, str], str] = {}
    code = python_code(TypeAdapter(Recipe).validate_python(TNT_MINECART), imports)
    assert code == (
        "RecipeCraftingShapeless(\n"
        "    ingredients=['minecraft:tnt', 'minecraft:minecart'],\n"
        "    result=ItemStackOfComponent(id='minecraft:tnt_minecart'),\n"
        "    type='minecraft:crafting_shapeless',\n"
        ")"
    )
    assert imports == {
        ("vanilla_mcdoc.data.recipe.Recipe", "RecipeCraftingShapeless"): "RecipeCraftingShapeless",
        ("vanilla_mcdoc.world.item.ItemStackOfComponent", "ItemStackOfComponent"): "ItemStackOfComponent",
    }


def test_extra_keys_and_enums_become_python_too() -> None:
    imports: dict[tuple[str, str], str] = {}
    rotation: object = TypeAdapter(ModelElementRotation).validate_python({"origin": [8, 8, 8], "axis": "y", "angle": 45})
    assert python_code(rotation, imports) == "ModelElementRotationStruct1(origin=(8.0, 8.0, 8.0), axis=Axis.Y, angle=45.0)"
    rotation = TypeAdapter(ModelElementRotation).validate_python({"origin": [8, 8, 8], "y": 45})
    assert python_code(rotation, imports) == "ModelElementRotationStruct2(origin=(8.0, 8.0, 8.0), **dict[str, Any]({'y': 45.0}))"
    assert ("typing", "Any") in imports


def fake_vanilla_files(tmp_path: Path, monkeypatch: MonkeyPatch, files: dict[str, object]) -> None:
    """Make vanilla_files read zips like fetch.py downloads, with these files in them."""
    data, assets = tmp_path / "data-json.zip", tmp_path / "assets-json.zip"
    for path, pack in [(data, "data"), (assets, "assets")]:
        with zipfile.ZipFile(path, "w") as archive:
            for name, contents in files.items():
                if name.startswith((f"{pack}/", "pack.mcmeta")):
                    archive.writestr(f"mcmeta-26.4-{pack}-json/{name}", json.dumps(contents))
    monkeypatch.setattr(vanilla_files, "VANILLA_ZIPS", [data, assets])


def test_vanilla_files_are_put_where_they_are_in_the_pack(tmp_path: Path, monkeypatch: MonkeyPatch) -> None:
    fake_vanilla_files(tmp_path, monkeypatch, {
        "data/minecraft/recipe/tnt_minecart.json": TNT_MINECART,
        "data/minecraft/tags/item/11.json": {"values": []},
        "data/minecraft/datapacks/trade_rebalance/data/minecraft/tags/item/rocks.json": {"values": ["minecraft:stone"]},
        "data/minecraft/not_a_resource/thing.json": {},  # No type, so left out
        "assets/minecraft/lang/en_us.json": {"block.minecraft.stone": "Stone"},
        "assets/minecraft/lang/fr_fr.json": {"block.minecraft.stone": "Pierre"},  # Only English
        "assets/realms/lang/en_us.json": {"mco.title": "Minecraft Realms"},  # Not the minecraft namespace, so it keeps its folder
        "pack.mcmeta": {},
    })
    files = vanilla_files.vanilla_files()
    assert sorted(files) == [
        ("assets", "lang", "en_us"),
        ("assets", "realms", "lang", "en_us"),
        ("data", "datapacks", "trade_rebalance", "data", "tags", "item", "rocks"),
        ("data", "recipe", "tnt_minecart"),
        ("data", "tags", "item", "11"),
    ]
    modules = vanilla_files.package_files(files)
    recipes = modules[vanilla_files.VANILLA_DIRECTORY / "data" / "recipe" / "__init__.py"]
    assert "from vanilla_mcdoc.data.recipe.Recipe import RecipeCraftingShapeless" in recipes
    assert "\nTNT_MINECART = RecipeCraftingShapeless(\n" in recipes
    assert "_11 = Tag(values=[])" in modules[vanilla_files.VANILLA_DIRECTORY / "data" / "tags" / "item" / "__init__.py"]
    assert "EN_US = {'block.minecraft.stone': 'Stone'}" in modules[vanilla_files.VANILLA_DIRECTORY / "assets" / "lang" / "__init__.py"]
    assert vanilla_files.VANILLA_DIRECTORY / "__init__.py" in modules  # Every folder is a package, even with only folders in it


def test_folders_from_another_version_are_removed(tmp_path: Path, monkeypatch: MonkeyPatch) -> None:
    fake_vanilla_files(tmp_path, monkeypatch, {"data/minecraft/tags/item/rocks.json": {"values": []}})
    monkeypatch.setattr(vanilla_files, "VANILLA_DIRECTORY", tmp_path / "vanilla")
    stale = tmp_path / "vanilla" / "data" / "worldgen" / "configured_carver" / "__init__.py"  # Renamed to worldgen/carver in 26.3
    stale.parent.mkdir(parents=True)
    stale.write_text("", encoding="utf-8")
    vanilla_files.make_vanilla_package()
    assert not stale.parent.exists()
    assert (tmp_path / "vanilla" / "data" / "tags" / "item" / "__init__.py").exists()
