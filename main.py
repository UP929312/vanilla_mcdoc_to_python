from code_generation import SCHEMA_GRAPH, make_init_files, make_python_file_of_model
from minecraft_registry import make_registry_id_files, make_root_resource_registry_file
from utils import SYMBOLS_MAP
from tests.assertions import run_assertions

SYMBOLS_MAP_NO_ANONYMOUS = {key: value for key, value in SYMBOLS_MAP["mcdoc"].items() if "anonymous" not in key}  # TODO: Figure what is going on here?

make_registry_id_files(SCHEMA_GRAPH)

for resource_type, resource_data in SYMBOLS_MAP_NO_ANONYMOUS.items():
    make_python_file_of_model(resource_type, resource_data)

make_root_resource_registry_file(SYMBOLS_MAP_NO_ANONYMOUS)
make_init_files(SYMBOLS_MAP_NO_ANONYMOUS)  # Adds the nice top level imports

run_assertions()

# mypy . --strict --exclude generated_symbols
# coverage run --branch main.py
# coverage html 
# start microsoft-edge:htmlcov\index.html
# python3 -m pytest

# TODO:
# Put all the descriptions in the struct/dataclass docstring, not just the comments (so hovering works nicer?)
# When going from dataclass -> JSON file, recursively remove None/null so they don't end up in the JSON file.
# CONVERT DATACLASSES INTO PYDANTIC MODELS

# https://github.com/sandstone-mc/sandstone/blob/828171c5fc1f5903e7ae1c508fe638d6481ab8e9/src/arguments/generated/world/item/compass.ts#L6
# https://github.com/OguzhanUmutlu/flare/blob/84b5121a21827eefcfca846ac6859512187e7f84/flare/generated/item.py#L166


HANDY_LINKS = [
    "",
    r"generated_symbols\data\advancement\predicate\FoodPredicate.py",  # MinMaxBounds[T]
    r"generated_symbols\data\worldgen\attribute\GlobalEnvironmentAttributeMap.py",  # ConcreteSchema (Base, not struct)
    r"generated_symbols\data\worldgen\DecorationStep.py",  # Enum
    r"generated_symbols\util\FlatWeightedList.py",  # Template with types
    r"generated_symbols\data\structure\BlockPalette.py",  # Union of two structs.
    r"generated_symbols\worldentity\mob\WaypointIcon.py",  # Decorated string, i.e. "string["id"=Literal["waypoint_style"]]
    r"generated_symbols\world\block\crafter\Crafter.py",  # disabled_slots is both lengthRange and valueRange
    r"generated_symbols\world\item\ItemStackTemplate.py",  # Has a ReferenceSchema with a canonical attribute???
    r"generated_symbols\util\InclusiveRange.py",  # Is complicated, should have Struct | list
    r"generated_symbols\world\entity\mob\player\Player.py",  # Lots, but most importly, empty fields
    r"generated_symbols\world\entity\mob\MobBase.py",  # Sub-field owns own Struct
    r"generated_symbols\data\advancement\predicate\BlockPredicate.py",  # Last arg (predicates) https://misode.github.io/predicate/?share=AEftpNxfkQ

    r"generated_symbols\world\component\DataComponentPredicate.py",  # Overly simplified -> dict[str, Any], the Any is a Dispatcher
    r"generated_symbols\assets\credits\Credits.py",  # Needs to make it's own Structs (list does)
    r"generated_symbols\data\advancement\predicate\BlockPredicate.py",  # str | Dispatcher (resolves to Any)
    r"generated_symbols\data\advancement\Advancement.py",  # Super weird attributes.
    r"generated_symbols\data\advancement\predicate\BlockPredicateState.py",  # Complicated Key (for now we do Annotated, need to smarten this up.)
]

# Would be nice to have a wrapper type for the registry references
# ResourceLocation[WolfVariant] for example

# print(f"Handy links:\n{'\n- '.join(HANDY_LINKS)}")
