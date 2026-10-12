import io
import json
import zipfile

from pytest import CaptureFixture, MonkeyPatch, raises

import validate

SMELTING = {"type": "minecraft:smelting", "ingredient": "minecraft:cobblestone", "result": {"id": "minecraft:stone"}, "cookingtime": 200}


def fake_vanilla_data(monkeypatch: MonkeyPatch, files: dict[str, object]) -> None:
    """Make validate.download answer like mcmeta's <version>-data-json zip would, with these files in it."""
    archive = io.BytesIO()
    with zipfile.ZipFile(archive, "w") as zip_file:
        for path, contents in files.items():
            zip_file.writestr(f"mcmeta-data-json/{path}", json.dumps(contents))
    monkeypatch.setattr(validate, "download", lambda url: archive.getvalue())


def test_validate_passes_if_only_known_invalid_files_are(monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]) -> None:
    monkeypatch.setattr(validate, "KNOWN_INVALID", {"data/minecraft/recipe/broken.json": "No ingredient"})
    fake_vanilla_data(monkeypatch, {
        "data/minecraft/recipe/stone.json": SMELTING,
        "data/minecraft/recipe/broken.json": {"type": "minecraft:smelting"},
        "data/minecraft/tags/block/rocks.json": {"values": ["minecraft:stone"]},
        "data/minecraft/datapacks/trade_rebalance/data/minecraft/loot_table/empty.json": {},  # A built-in pack's
        "pack.mcmeta": {},  # Not a data pack file
    })
    validate.validate()
    assert "3 of 4 files are valid, and 1 of the rest are known not to be" in capsys.readouterr().err


def test_validate_fails_for_invalid_files_and_known_invalid_ones_that_are_valid(monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]) -> None:
    monkeypatch.setattr(validate, "KNOWN_INVALID", {"data/minecraft/recipe/stone.json": "Used to be invalid"})
    fake_vanilla_data(monkeypatch, {
        "data/minecraft/recipe/stone.json": SMELTING,
        "data/minecraft/recipe/broken.json": {**SMELTING, "cookingtime": "soon"},
        "data/minecraft/not_a_resource/thing.json": {},
    })
    with raises(SystemExit):
        validate.validate()
    errors = capsys.readouterr().err
    assert "data/minecraft/recipe/broken.json: minecraft:smelting.cookingtime: Input should be a valid integer" in errors
    assert "data/minecraft/not_a_resource/thing.json: vanilla-mcdoc doesn't have this resource type" in errors
    assert "data/minecraft/recipe/stone.json is valid now (or gone), so take it off KNOWN_INVALID" in errors
