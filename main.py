import argparse

from code_generation import generate_package
from tests.assertions import run_assertions
from utils import LATEST_VERSION, SETTINGS, version_problem

parser = argparse.ArgumentParser(description="Generates the vanilla_mcdoc package from symbols.json")
parser.add_argument("--version", default=LATEST_VERSION, help="The Minecraft version to generate for, e.g. 26.1.2 (default: %(default)s)")
parser.add_argument("--no-model-dump", action="store_true", help="Leave out the raw symbols.json data at the bottom of each file (for publishing)")
parser.add_argument("--no-snapshot-tests", action="store_true", help="Don't compare against tests/assertions (CI, where symbols.json may have moved on)")
arguments = parser.parse_args()

if problem := version_problem(arguments.version):  # e.g. registries.json being for another version
    parser.error(problem)
SETTINGS.minecraft_version = arguments.version
SETTINGS.include_model_dump = not arguments.no_model_dump

generate_package()

if SETTINGS.minecraft_version == LATEST_VERSION and not arguments.no_snapshot_tests:  # The snapshots are of the latest version
    run_assertions()

# mypy . --strict --exclude vanilla_mcdoc
# coverage run --branch main.py
# coverage html
# ruff check
# flake8 --ignore=E501,W503,W391,E221
# start microsoft-edge:htmlcov\index.html
# python3 -m pytest

# TODO:
# Put all the descriptions in the struct/dataclass docstring, not just the comments (so hovering works nicer?)
# Safeguards need to also include the value range, currently that is lost (5-10 is lost and now becomes -2147483648 to 2147483647).

# https://github.com/sandstone-mc/sandstone/blob/828171c5fc1f5903e7ae1c508fe638d6481ab8e9/src/arguments/generated/world/item/compass.ts#L6
# https://github.com/OguzhanUmutlu/flare/blob/84b5121a21827eefcfca846ac6859512187e7f84/flare/generated/item.py#L166


_HANDY_LINKS = [
    r"vanilla_mcdoc\data\advancement\predicate\FoodPredicate.py",  # MinMaxBounds[T]
    r"vanilla_mcdoc\data\worldgen\attribute\GlobalEnvironmentAttributeMap.py",  # ConcreteSchema (Base, not struct)
    r"vanilla_mcdoc\data\worldgen\DecorationStep.py",  # Enum
    r"vanilla_mcdoc\util\FlatWeightedList.py",  # Template with types
    r"vanilla_mcdoc\data\structure\BlockPalette.py",  # Union of two structs.
    r"vanilla_mcdoc\worldentity\mob\WaypointIcon.py",  # Decorated string, i.e. "string["id"=Literal["waypoint_style"]]
    r"vanilla_mcdoc\world\block\crafter\Crafter.py",  # disabled_slots is both lengthRange and valueRange
    r"vanilla_mcdoc\world\item\ItemStackTemplate.py",  # Has a ReferenceSchema with a canonical attribute???
    r"vanilla_mcdoc\util\InclusiveRange.py",  # Is complicated, should have Struct | list
    r"vanilla_mcdoc\world\entity\mob\player\Player.py",  # Lots, but most importly, empty fields
    r"vanilla_mcdoc\world\entity\mob\MobBase.py",  # Sub-field owns own Struct
    r"vanilla_mcdoc\data\advancement\predicate\BlockPredicate.py",  # Last arg (predicates) https://misode.github.io/predicate/?share=AEftpNxfkQ

    r"vanilla_mcdoc\world\component\DataComponentPredicate.py",  # Overly simplified -> dict[str, Any], the Any is a Dispatcher
    r"vanilla_mcdoc\assets\credits\Credits.py",  # Needs to make it's own Structs (list does)
    r"vanilla_mcdoc\data\advancement\predicate\BlockPredicate.py",  # str | Dispatcher (resolves to Any)
    r"vanilla_mcdoc\data\advancement\Advancement.py",  # Super weird attributes.
    r"vanilla_mcdoc\data\advancement\predicate\BlockPredicateState.py",  # Complicated Key (for now we do Annotated, need to smarten this up.)
]
