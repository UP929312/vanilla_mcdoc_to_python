import zipfile
from pathlib import Path

from pytest import MonkeyPatch, raises

import utils
from typed_models import Attribute, LiteralSchema, StringSchema
from utils import LATEST_VERSION, REGISTRIES_VERSION, VERSION_IDS, is_valid_with_attributes, minecraft_to_python_version, version_problem, zip_version


def version_attribute(name: str, version: str) -> Attribute:
    return Attribute(name=name, value=LiteralSchema(kind="literal", value=StringSchema(kind="string", value=version)))


def test_minecraft_versions_become_python_versions_that_sort_the_same() -> None:
    assert minecraft_to_python_version("26.3") == "26.3.0"
    assert minecraft_to_python_version("26.1.2") == "26.1.2"
    assert minecraft_to_python_version("26.4-snapshot-3") == "26.4.0a3"
    assert minecraft_to_python_version("26.4-pre-1") == "26.4.0b1"
    assert minecraft_to_python_version("26.4-rc-1") == "26.4.0rc1"
    assert minecraft_to_python_version("1.21.5-pre1") == "1.21.5b1"  # Old style pre-releases work too
    with raises(ValueError):
        minecraft_to_python_version("25w14a")  # Old style snapshots don't say which release they're for


def test_since_and_until_are_checked_against_the_given_version() -> None:
    added_in_1_21_5 = [version_attribute("since", "1.21.5")]
    removed_in_1_21_5 = [version_attribute("until", "1.21.5")]
    assert is_valid_with_attributes(added_in_1_21_5, current_version="1.21.5")
    assert not is_valid_with_attributes(added_in_1_21_5, current_version="1.21.4")
    assert is_valid_with_attributes(removed_in_1_21_5, current_version="1.21.4")
    assert not is_valid_with_attributes(removed_in_1_21_5, current_version="1.21.5")  # until is exclusive


def test_deprecated_things_are_still_valid() -> None:
    """The game still takes them (Spyglass just warns), e.g. vanilla's models still use the old axis and angle rotations."""
    assert is_valid_with_attributes([version_attribute("deprecated", "1.21.11")], current_version=LATEST_VERSION)
    assert is_valid_with_attributes([Attribute(name="deprecated")], current_version=LATEST_VERSION)  # With no version


def zip_for(path: Path, minecraft_version: str) -> Path:
    """A zip like fetch.py downloads, of mcmeta's files for that version."""
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr(f"mcmeta-{minecraft_version}-data-json/pack.mcmeta", "{}")
    return path


def test_zip_version_is_from_its_folder(tmp_path: Path) -> None:
    assert zip_version(zip_for(tmp_path / "data-json.zip", "26.4-snapshot-3")) == "26.4-snapshot-3"
    assert zip_version(tmp_path / "missing.zip") is None


def test_versions_that_cant_be_generated_say_why(tmp_path: Path, monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(utils, "VANILLA_ZIPS", [zip_for(tmp_path / "data-json.zip", REGISTRIES_VERSION)])
    assert version_problem(REGISTRIES_VERSION) is None
    assert version_problem("nope") == "Unknown Minecraft version 'nope', see versions.json"
    assert "can't" in str(version_problem("21w43a")).lower()  # Old style snapshots can't be package versions
    other_version = next(version for version in VERSION_IDS if version != REGISTRIES_VERSION and "w" not in version)
    assert version_problem(other_version) == f"registries.json is for {REGISTRIES_VERSION}, run `python .github/scripts/fetch.py version {other_version}` first"
    monkeypatch.setattr(utils, "VANILLA_ZIPS", [zip_for(tmp_path / "old.zip", other_version)])
    assert version_problem(REGISTRIES_VERSION) == f"mcmeta/ doesn't have vanilla's files for {REGISTRIES_VERSION}, run `python .github/scripts/fetch.py vanilla` first"
