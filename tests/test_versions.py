from pytest import raises

from typed_models import Attribute, LiteralSchema, StringSchema
from utils import is_valid_with_attributes, minecraft_to_python_version


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
