
ASSERTIONS = {
    # FoodPredicate, references MinMaxBounds[int], a Generic of type.
    r"generated_symbols\data\advancement\predicate\FoodPredicate.py": """# Generated from symbols.json for ::java::data::advancement::predicate::FoodPredicate
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds


@dataclass(kw_only=True)
class FoodPredicate:
    level: MinMaxBounds[int] | int | None = None
    saturation: MinMaxBounds[float] | float | None = None
""",

    # GlobalEnvironmentAttributeMap, is a type of types with literal keys in the dictionary.
    r"generated_symbols\data\worldgen\attribute\GlobalEnvironmentAttributeMap.py": """# Generated from symbols.json for ::java::data::worldgen::attribute::GlobalEnvironmentAttributeMap
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.attribute.EnvironmentAttributeMap import EnvironmentAttributeMap


GlobalEnvironmentAttributeMap = EnvironmentAttributeMap[str]

""",

    # DecorationStep, an Enum
    r"generated_symbols\data\worldgen\DecorationStep.py": """# Generated from symbols.json for ::java::data::worldgen::DecorationStep
from enum import Enum


class DecorationStep(Enum):
    RAWGENERATION = "raw_generation"
    LAKES = "lakes"
    LOCALMODIFICATIONS = "local_modifications"
    UNDERGROUNDSTRUCTURES = "underground_structures"
    SURFACESTRUCTURES = "surface_structures"
    STRONGHOLDS = "strongholds"
    UNDERGROUNDORES = "underground_ores"
    UNDERGROUNDDECORATION = "underground_decoration"
    FLUIDSPRINGS = "fluid_springs"
    VEGETALDECORATION = "vegetal_decoration"
    TOPLAYERMODIFICATION = "top_layer_modification"
""",

    # DyeColorInt, an alias with the same name, needs to be suffixed or weirdness happens.
    r"generated_symbols\util\DyeColorInt.py": """# Generated from symbols.json for ::java::util::DyeColorInt
from generated_symbols.util.color.DyeColorInt import DyeColorInt as DyeColorInt_alias


type DyeColorInt = DyeColorInt_alias
""",

    # FlatWeightedList, a type with type, equating to another type with type.
    r"generated_symbols\util\FlatWeightedList.py": """# Generated from symbols.json for ::java::util::FlatWeightedList
from typing import TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    from generated_symbols.util.FlatWeightedEntry import FlatWeightedEntry


T = TypeVar('T')

type FlatWeightedList[T] = list[FlatWeightedEntry[T]]
""",

    # SkullOwner, IntArray of length 4 -> tuple[int, int, int, int]
    r"generated_symbols\world\item\head\SkullOwner.py": """# Generated from symbols.json for ::java::world::item::head::SkullOwner
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.item.head.Properties import Properties


@dataclass(kw_only=True)
class SkullOwner:
    Id: tuple[int, int, int, int] | None = None  # Optional.
    Name: str | None = None  # Name of the owner, if missing appears as a steve head.
    Properties: Properties | None = None
""",

    # This has the weird `...::tag::E` thing, ensure it's working properly.
    r"generated_symbols\data\tag\ExplicitTagEntry.py": """# Generated from symbols.json for ::java::data::tag::ExplicitTagEntry
from dataclasses import dataclass
from typing import Generic, TypeVar


E = TypeVar('E')

@dataclass(kw_only=True)
class ExplicitTagEntry(Generic[E]):
    id: E
    required: bool | None = None""",

    # This has an override of it's parent (inherited), but because it's the same type, we're fine.
    r"generated_symbols\world\entity\mob\creaking\Creaking.py": """# Generated from symbols.json for ::java::world::entity::mob::creaking::Creaking
from dataclasses import dataclass
from generated_symbols.world.entity.mob.MobBase import MobBase


@dataclass(kw_only=True)
class Creaking(MobBase):
    home_pos: tuple[int, int, int] | None = None  # The creaking heart block that this is linked to.
""",

    # IntArray -> tuple[int, int, int]
    r"generated_symbols\world\block\test_instance_block\ErrorMarker.py": """# Generated from symbols.json for ::java::world::block::test_instance_block::ErrorMarker
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.text.Text import Text


@dataclass(kw_only=True)
class ErrorMarker:
    pos: tuple[int, int, int]
    text: Text
""",

    # Text's definition is cyclical - It can be str | <other> | list[<self>]
    r"generated_symbols\util\text\Text.py": """# Generated from symbols.json for ::java::util::text::Text
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.util.text.TextObject import TextObject


type Text = str | TextObject | Annotated[list[Text], 'Length = 1 (inclusive) and above']
""",

    # Has a union attr, so makes its own Struct.
    r"generated_symbols\data\worldgen\HeightProvider.py": """# Generated from symbols.json for ::java::data::worldgen::HeightProvider
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.VerticalAnchor import VerticalAnchor


@dataclass(kw_only=True)
class HeightProviderStruct1:
    type: str

type HeightProvider = HeightProviderStruct1 | VerticalAnchor
""",

    # Nothing in particular, just a nice, nested object with lots going on
    r"generated_symbols\data\advancement\AdvancementDisplay.py": """# Generated from symbols.json for ::java::data::advancement::AdvancementDisplay
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.advancement.AdvancementFrame import AdvancementFrame
    from generated_symbols.util.text.Text import Text
    from generated_symbols.world.item.ItemStackTemplate import ItemStackTemplate


@dataclass(kw_only=True)
class AdvancementDisplay:
    icon: ItemStackTemplate
    title: Text
    description: Text
    background: str | None = None  # Used for the advancement tab (root advancement only).
    frame: AdvancementFrame | None = None  # Controls the advancement tile frame. Defaults to `task`.
    show_toast: bool | None = None  # Whether to show the toast pop up after completing this advancement. Defaults to `true`.
    announce_to_chat: bool | None = None  # Whether to announce in the chat when this advancement has been completed. Defaults to `true`.
    hidden: bool | None = None  # Whether or not to hide this advancement and all its children from the advancement screen, until this advancement have been completed. Has no effect on root advancements themselves, but still affects all their children. Defaults to `false`.
""",

    # Shows one of the pairs owning their own struct, not currently implemented.
#     r"generated_symbols\world\entity\mob\MobBase.py": """# Generated from symbols.json for ::java::world::entity::mob::MobBase
# from dataclasses import dataclass
# from typing import TYPE_CHECKING
# from generated_symbols.world.entity.mob.LivingEntity import LivingEntity

# if TYPE_CHECKING:
#     from generated_symbols.world.entity.mob.DropChances import DropChances
#     from generated_symbols.world.entity.mob.EntityEquipment import EntityEquipment


# @dataclass(kw_only=True):
# class MobBaseleash:
#     UUID: tuple[int, int, int, int] | None = None

# @dataclass(kw_only=True)
# class MobBase(LivingEntity):
#     equipment: EntityEquipment | None = None  # The equipment items of the mob, such as armor or weapons.
#     drop_chances: DropChances | None = None  # Chances of the mob dropping an equipment slot on death.
#     DeathLootTable: str | None = None  # Loot table that is dropped when the mob dies.
#     DeathLootTableSeed: int | None = None  # Seed for generating the death loot table.
#     CanPickUpLoot: bool | None = None  # Whether it can pick up loot.
#     PersistenceRequired: bool | None = None  # Whether it should not despawn naturally.
#     LeftHanded: bool | None = None  # Whether it is left handed.
#     NoAI: bool | None = None  # Whether it should have an AI.
#     leash: tuple[int, int, int] | MobBaseleash | None = None  # What the leash is attached to.
#     home_radius: int | None = None  # Defaults to -1, which represents "no home".
#     home_pos: tuple[int, int, int] | None = None  # This field will be discarded if `home_radius` is less than 0.
# """,

    r"generated_symbols\world\entity\mob\AttributeModifier.py": """# Generated from symbols.json for ::java::world::entity::mob::AttributeModifier
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.attribute.AttributeOperation import AttributeOperation


@dataclass(kw_only=True)
class AttributeModifier:
    id: str  # The unique identifier of this attribute modifier.
    amount: float  # Change in the attribute.
    operation: AttributeOperation  # The operation used for this modifier.
""",

    # Collapses it's deprecated child - nice.
    r"generated_symbols\assets\model\ModelElementRotation.py": """# Generated from symbols.json for ::java::assets::model::ModelElementRotation
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.model.Axis import Axis


type ModelElementRotation = dict[Axis, float]
""",

}

def run_assertions() -> None:
    for path, content in ASSERTIONS.items():
        with open(path, "r", encoding="utf-8") as file:
            file_contents = file.read().split("\n# ~~~")[0].strip().strip("\n")
            assert file_contents == content.strip().strip("\n"), f"{path} was different!"


if __name__ == "__main__":
    run_assertions()