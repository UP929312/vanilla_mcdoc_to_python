
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
from typing import TYPE_CHECKING, Annotated

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.attribute.EnvironmentAttributeMap import EnvironmentAttributeMap


GlobalEnvironmentAttributeMap = EnvironmentAttributeMap[Annotated[str, IdSpec(registry='environment_attribute')]]

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

    # Inline pair structs are materialized as sibling dataclasses instead of degrading to Any.
    r"generated_symbols\world\item\shield\Shield.py": """# Generated from symbols.json for ::java::world::item::shield::Shield
from dataclasses import dataclass
from typing import TYPE_CHECKING

from generated_symbols.world.item.ItemBase import ItemBase

if TYPE_CHECKING:
    from generated_symbols.util.color.DyeColorInt import DyeColorInt
    from generated_symbols.world.block.banner.BannerPatternLayer import BannerPatternLayer


@dataclass(kw_only=True)
class BlockEntityTagStruct:
    Base: DyeColorInt | None = None  # Base color.
    Patterns: list[BannerPatternLayer] | None = None


@dataclass(kw_only=True)
class Shield(ItemBase):
    BlockEntityTag: BlockEntityTagStruct | None = None  # Banner Data.
""",

    # Lowercase pair keys are converted to PascalCase when naming nested structs.
    r"generated_symbols\assets\equipment\TrimOverride.py": """# Generated from symbols.json for ::java::assets::equipment::TrimOverride
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.assets.atlas.PaletteRef import PaletteRef


@dataclass(kw_only=True)
class WhenStruct:
    pattern: Annotated[str, IdSpec(registry='trim_pattern')] | None = None
    material: Annotated[str, IdSpec(registry='trim_material')] | None = None


@dataclass(kw_only=True)
class TrimOverride:
    when: WhenStruct
    texture: Annotated[str, IdSpec()] | None = None  # When present, overrides the base texture provided by trim pattern.  The texture is located under `trims/entity/<layer>/`.
    palette: PaletteRef | None = None  # When present, overrides the palette texture provided by trim material.
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

    # Dispatcher spread branches retain their correlated discriminator and fields.
    r"generated_symbols\data\worldgen\HeightProvider.py": """# Generated from symbols.json for ::java::data::worldgen::HeightProvider
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from generated_symbols.data.worldgen.UniformHeightProvider import UniformHeightProvider

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.VerticalAnchor import VerticalAnchor
    from generated_symbols.util.NonEmptyWeightedList import NonEmptyWeightedList


@dataclass(kw_only=True)
class HeightProviderStructBiasedToBottom(UniformHeightProvider):
    type: Literal['minecraft:biased_to_bottom']
    inner: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None


@dataclass(kw_only=True)
class HeightProviderStructConstant:
    type: Literal['minecraft:constant']
    value: VerticalAnchor


@dataclass(kw_only=True)
class HeightProviderStructTrapezoid(UniformHeightProvider):
    type: Literal['minecraft:trapezoid']
    plateau: int | None = None


@dataclass(kw_only=True)
class HeightProviderStructUniform:
    type: Literal['minecraft:uniform']
    min_inclusive: VerticalAnchor
    max_inclusive: VerticalAnchor


@dataclass(kw_only=True)
class HeightProviderStructVeryBiasedToBottom(UniformHeightProvider):
    type: Literal['minecraft:very_biased_to_bottom']
    inner: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None


@dataclass(kw_only=True)
class HeightProviderStructWeightedList:
    type: Literal['minecraft:weighted_list']
    distribution: NonEmptyWeightedList[HeightProvider]


type HeightProviderStruct = HeightProviderStructBiasedToBottom | HeightProviderStructConstant | HeightProviderStructTrapezoid | HeightProviderStructUniform | HeightProviderStructVeryBiasedToBottom | HeightProviderStructWeightedList

type HeightProvider = HeightProviderStruct | VerticalAnchor
""",

    # Nothing in particular, just a nice, nested object with lots going on
    r"generated_symbols\data\advancement\AdvancementDisplay.py": """# Generated from symbols.json for ::java::data::advancement::AdvancementDisplay
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.advancement.AdvancementFrame import AdvancementFrame
    from generated_symbols.util.text.Text import Text
    from generated_symbols.world.item.ItemStackTemplate import ItemStackTemplate


@dataclass(kw_only=True)
class AdvancementDisplay:
    icon: ItemStackTemplate
    title: Text
    description: Text
    background: Annotated[str, IdSpec(registry='texture')] | None = None  # Used for the advancement tab (root advancement only).
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
from typing import TYPE_CHECKING, Annotated

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.util.attribute.AttributeOperation import AttributeOperation


@dataclass(kw_only=True)
class AttributeModifier:
    id: Annotated[str, IdSpec(registry='attribute_modifier')]  # The unique identifier of this attribute modifier.
    amount: float  # Change in the attribute.
    operation: AttributeOperation  # The operation used for this modifier.
""",

    # Collapses it's deprecated child - nice.
    r"generated_symbols\assets\model\ModelElementRotation.py": """# Generated from symbols.json for ::java::assets::model::ModelElementRotation
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.direction.Axis import Axis


type ModelElementRotation = dict[Axis, float]
""",

    # Make sure that if there's only 1 struct, don't number it.
    r"generated_symbols\util\avatar\Profile.py": """# Generated from symbols.json for ::java::util::avatar::Profile
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.util.avatar.PlayerModelType import PlayerModelType
    from generated_symbols.util.avatar.ProfileProperty import ProfileProperty
    from generated_symbols.util.avatar.ProfilePropertyMap import ProfilePropertyMap


@dataclass(kw_only=True)
class ProfileStruct:
    name: str | None = None  # Username of a player profile. If `id` doesn't exist, this field is used to fetch the current skin of the profile.
    id: tuple[int, int, int, int] | None = None  # UUID of the player profile. If `name` doesn't exist, this field is used to fetch the current skin of the profile.
    properties: Annotated[list[ProfileProperty], 'Length = 0-16 (both inclusive)'] | ProfilePropertyMap | None = None  # Resolved textures hosted on the minecraft CDN.
    texture: Annotated[str, IdSpec(registry='texture')] | None = None  # Skin texture override.
    cape: Annotated[str, IdSpec(registry='texture')] | None = None  # Cape texture override.
    elytra: Annotated[str, IdSpec(registry='texture')] | None = None  # Elytra texture override. If this texture is not present either as override or in player profile, the cape texture is used. If the cape texture is also not present, the default elytra texture is used.
    model: PlayerModelType | None = None  # Model type override.


type Profile = ProfileStruct | str
""",

    # Nested structs generated inside templates must retain their type arguments at use sites.
    r"generated_symbols\data\worldgen\attribute\MergeableAttribute.py": """# Generated from symbols.json for ::java::data::worldgen::attribute::MergeableAttribute
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Generic, TypeVar

from generated_symbols.data.timeline.AttributeTrackBase import AttributeTrackBase

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.attribute.modifier.MergeableModifier import MergeableModifier
    from generated_symbols.data.worldgen.attribute.modifier.MergeableModifierType import MergeableModifierType


T = TypeVar('T')

@dataclass(kw_only=True)
class KeyframesStruct(Generic[T]):
    ticks: Annotated[int, 'Range | Min `0` and above | inclusive']
    value: T


@dataclass(kw_only=True)
class AttributeTrackStruct(AttributeTrackBase, Generic[T]):
    keyframes: Annotated[list[KeyframesStruct[T]], 'Length = 1 (inclusive) and above']
    modifier: MergeableModifierType | None = None


@dataclass(kw_only=True)
class MergeableAttribute(Generic[T]):
    value: T
    modifier: MergeableModifier[T]
    attribute_track: AttributeTrackStruct[T]
""",

    # Structs nested in lists are materialized recursively before the list alias.
    r"generated_symbols\assets\credits\Credits.py": """# Generated from symbols.json for ::java::assets::credits::Credits
from dataclasses import dataclass
from typing import Annotated, Literal


@dataclass(kw_only=True)
class TitlesStruct:
    title: str
    names: list[str]  # Employees with the title.


@dataclass(kw_only=True)
class DisciplinesStruct:
    discipline: Annotated[str, 'Length = 1 (inclusive) and above'] | Literal[""]
    titles: list[TitlesStruct]


@dataclass(kw_only=True)
class CreditsStruct:
    section: str  # Company segment.
    disciplines: list[DisciplinesStruct]


type Credits = list[CreditsStruct]
""",

    # Union members that are lists of structs need a named item class.
    r"generated_symbols\assets\block_state_definition\ModelVariant.py": """# Generated from symbols.json for ::java::assets::block_state_definition::ModelVariant
from dataclasses import dataclass
from typing import Annotated

from generated_symbols.assets.block_state_definition.ModelVariantBase import ModelVariantBase


@dataclass(kw_only=True)
class ModelVariantStruct(ModelVariantBase):
    weight: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None


type ModelVariant = ModelVariantBase | list[ModelVariantStruct]
""",

    # Top-level dataclasses emitted by unions retain two blank lines between declarations.
    r"generated_symbols\assets\block_state_definition\BlockStateDefinition.py": """# Generated from symbols.json for ::java::assets::block_state_definition::BlockStateDefinition
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.block_state_definition.ModelVariant import ModelVariant
    from generated_symbols.assets.block_state_definition.MultiPartCondition import MultiPartCondition


@dataclass(kw_only=True)
class MultipartStruct:
    apply: ModelVariant
    when: MultiPartCondition | None = None  # One condition or an array where at least one condition must apply.


@dataclass(kw_only=True)
class BlockStateDefinitionStruct1:
    variants: dict[str, ModelVariant]


@dataclass(kw_only=True)
class BlockStateDefinitionStruct2:
    multipart: list[MultipartStruct]


type BlockStateDefinition = BlockStateDefinitionStruct1 | BlockStateDefinitionStruct2
""",

    # Pair unions materialize nested structs in source order instead of emitting their keys as types.
    r"generated_symbols\data\worldgen\structure\TrickyTrialsStructureConfig.py": """# Generated from symbols.json for ::java::data::worldgen::structure::TrickyTrialsStructureConfig
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.structure.LiquidSettings import LiquidSettings


@dataclass(kw_only=True)
class DimensionPaddingStruct:
    bottom: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None
    top: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None


@dataclass(kw_only=True)
class TrickyTrialsStructureConfig:
    dimension_padding: Annotated[int, 'Range | Min `0` and above | inclusive'] | DimensionPaddingStruct | None = None
    liquid_settings: LiquidSettings | None = None
""",

    # Mapping values that are structs become named dataclasses rather than unions of their field keys.
    r"generated_symbols\assets\model\ModelElementFaceMap.py": """# Generated from symbols.json for ::java::assets::model::ModelElementFaceMap
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from generated_symbols.util.direction.Direction import Direction


@dataclass(kw_only=True)
class ModelElementFaceMapValueStruct:
    texture: str
    uv: tuple[float, float, float, float] | None = None
    cullface: Direction | None = None
    rotation: Literal[0] | Literal[90] | Literal[180] | Literal[270] | None = None
    tintindex: int | None = None


type ModelElementFaceMap = dict[Direction, ModelElementFaceMapValueStruct]
""",

# Disabled because it's a lot of code for a single object which will probably never be used.
#     # An empty struct should allow {}
#     r"generated_symbols\world\entity\mob\breedable\horse\ChestedHorse.py": """# Generated from symbols.json for ::java::world::entity::mob::breedable::horse::ChestedHorse
# from dataclasses import dataclass
# from typing import TYPE_CHECKING, Annotated, Never

# from generated_symbols.world.entity.mob.breedable.horse.HorseBase import HorseBase

# if TYPE_CHECKING:
#     from generated_symbols.util.slot.SlottedItem import SlottedItem


# @dataclass(kw_only=True)
# class ChestedHorse(HorseBase):
#     ChestedHorse: bool | None = None  # Whether it has a chest.
#     Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`14` | both inclusive']] | dict[Never, Never]], 'Length = 0-15 (both inclusive)'] | None = None  # Slots from 0 to 14.
# """,

}

def run_assertions() -> None:
    for path, content in ASSERTIONS.items():
        with open(path, "r", encoding="utf-8") as file:
            file_contents = file.read().split("\n# ~~~")[0].strip().strip("\n")
            assert file_contents == content.strip().strip("\n"), f"{path} was different!"


if __name__ == "__main__":
    run_assertions()