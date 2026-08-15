"""
Generated from symbols.json for ::java::assets::item_definition::ItemModel
Local link to file: generated_symbols/assets/item_definition/ItemModel.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from generated_symbols.assets.item_definition.CrossbowChargeType import CrossbowChargeType
from generated_symbols.assets.item_definition.SelectCases import SelectCases
from generated_symbols.assets.model.ItemDisplayContext import ItemDisplayContext
from generated_symbols.data.advancement.predicate.ItemPredicate import ItemPredicate
from generated_symbols.data.damage_type.DamageType import DamageType
from generated_symbols.data.util.SoundEventRef import SoundEventRef
from generated_symbols.data.variants.instrument.Instrument import Instrument
from generated_symbols.util.avatar.HumanoidArm import HumanoidArm
from generated_symbols.util.avatar.Profile import Profile
from generated_symbols.util.color.DyeColor import DyeColor
from generated_symbols.util.color.RGB import RGB
from generated_symbols.util.text.Text import Text
from generated_symbols.world.block.BlockEntityData import BlockEntityData
from generated_symbols.world.block.banner.BannerPatternLayer import BannerPatternLayer
from generated_symbols.world.component.CustomData import CustomData
from generated_symbols.world.component.block.ContainerLoot import ContainerLoot
from generated_symbols.world.component.block.ContainerSlot import ContainerSlot
from generated_symbols.world.component.block.Occupant import Occupant
from generated_symbols.world.component.block.PotDecorations import PotDecorations
from generated_symbols.world.component.block.SignText import SignText
from generated_symbols.world.component.entity.AxolotlVariant import AxolotlVariant
from generated_symbols.world.component.entity.FoxType import FoxType
from generated_symbols.world.component.entity.HorseVariant import HorseVariant
from generated_symbols.world.component.entity.LlamaVariant import LlamaVariant
from generated_symbols.world.component.entity.MooshroomType import MooshroomType
from generated_symbols.world.component.entity.ParrotVariant import ParrotVariant
from generated_symbols.world.component.entity.RabbitVariant import RabbitVariant
from generated_symbols.world.component.entity.SalmonType import SalmonType
from generated_symbols.world.component.entity.TropicalFishPattern import TropicalFishPattern
from generated_symbols.world.component.item.AdventureModePredicate import AdventureModePredicate
from generated_symbols.world.component.item.AttackRange import AttackRange
from generated_symbols.world.component.item.AttributeModifier import AttributeModifier
from generated_symbols.world.component.item.BlockTransformer import BlockTransformer
from generated_symbols.world.component.item.BrewingFuel import BrewingFuel
from generated_symbols.world.component.item.BucketEntityData import BucketEntityData
from generated_symbols.world.component.item.Compostable import Compostable
from generated_symbols.world.component.item.Consumable import Consumable
from generated_symbols.world.component.item.CookingFuel import CookingFuel
from generated_symbols.world.component.item.CustomModelData import CustomModelData
from generated_symbols.world.component.item.DamageResistant import DamageResistant
from generated_symbols.world.component.item.DeathProtection import DeathProtection
from generated_symbols.world.component.item.DebugStickState import DebugStickState
from generated_symbols.world.component.item.Enchantable import Enchantable
from generated_symbols.world.component.item.EnchantmentLevels import EnchantmentLevels
from generated_symbols.world.component.item.Equippable import Equippable
from generated_symbols.world.component.item.Explosion import Explosion
from generated_symbols.world.component.item.Fireworks import Fireworks
from generated_symbols.world.component.item.Food import Food
from generated_symbols.world.component.item.KineticWeapon import KineticWeapon
from generated_symbols.world.component.item.LodestoneTracker import LodestoneTracker
from generated_symbols.world.component.item.MapDecorations import MapDecorations
from generated_symbols.world.component.item.MobVisibility import MobVisibility
from generated_symbols.world.component.item.PiercingWeapon import PiercingWeapon
from generated_symbols.world.component.item.PotionContents import PotionContents
from generated_symbols.world.component.item.Rarity import Rarity
from generated_symbols.world.component.item.Repairable import Repairable
from generated_symbols.world.component.item.SuspiciousStewEffect import SuspiciousStewEffect
from generated_symbols.world.component.item.SwingAnimation import SwingAnimation
from generated_symbols.world.component.item.Tool import Tool
from generated_symbols.world.component.item.TooltipDisplay import TooltipDisplay
from generated_symbols.world.component.item.Trim import Trim
from generated_symbols.world.component.item.Unbreakable import Unbreakable
from generated_symbols.world.component.item.UseCooldown import UseCooldown
from generated_symbols.world.component.item.UseEffects import UseEffects
from generated_symbols.world.component.item.VillagerFood import VillagerFood
from generated_symbols.world.component.item.Weapon import Weapon
from generated_symbols.world.component.item.WritableBookContent import WritableBookContent
from generated_symbols.world.component.item.WrittenBookContent import WrittenBookContent
from generated_symbols.world.component.item.blocks_attacks import blocks_attacks
from generated_symbols.world.entity.AnyEntity import AnyEntity
from generated_symbols.world.item.ItemStackTemplate import ItemStackTemplate
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.BannerAttachment import BannerAttachment
    from generated_symbols.assets.item_definition.BedPart import BedPart
    from generated_symbols.assets.item_definition.ChestType import ChestType
    from generated_symbols.assets.item_definition.CompassTarget import CompassTarget
    from generated_symbols.assets.item_definition.ConditionalPropertyType import ConditionalPropertyType
    from generated_symbols.assets.item_definition.CopperGolemStatuePose import CopperGolemStatuePose
    from generated_symbols.assets.item_definition.EndCubeEffectType import EndCubeEffectType
    from generated_symbols.assets.item_definition.HangingSignAttachment import HangingSignAttachment
    from generated_symbols.assets.item_definition.HeadType import HeadType
    from generated_symbols.assets.item_definition.ModelTint import ModelTint
    from generated_symbols.assets.item_definition.NumericPropertyType import NumericPropertyType
    from generated_symbols.assets.item_definition.SelectPropertyType import SelectPropertyType
    from generated_symbols.assets.item_definition.SpecialModelType import SpecialModelType
    from generated_symbols.assets.item_definition.StandingSignAttachment import StandingSignAttachment
    from generated_symbols.assets.item_definition.TimeSource import TimeSource
    from generated_symbols.assets.item_definition.WoodType import WoodType
    from generated_symbols.assets.model.ModelRef import ModelRef
    from generated_symbols.data.advancement.predicate.EnchantmentPredicate import EnchantmentPredicate
    from generated_symbols.util.text.Keybind import Keybind
    from generated_symbols.world.component.predicate.AttributeModifiersPredicate import AttributeModifiersPredicate
    from generated_symbols.world.component.predicate.BundleContentsPredicate import BundleContentsPredicate
    from generated_symbols.world.component.predicate.ContainerPredicate import ContainerPredicate
    from generated_symbols.world.component.predicate.FireworkExplosionPredicate import FireworkExplosionPredicate
    from generated_symbols.world.component.predicate.FireworksPredicate import FireworksPredicate
    from generated_symbols.world.component.predicate.ItemDamagePredicate import ItemDamagePredicate
    from generated_symbols.world.component.predicate.JukeboxPlayablePredicate import JukeboxPlayablePredicate
    from generated_symbols.world.component.predicate.PotionsPredicate import PotionsPredicate
    from generated_symbols.world.component.predicate.TrimPredicate import TrimPredicate
    from generated_symbols.world.component.predicate.WritableBookPredicate import WritableBookPredicate
    from generated_symbols.world.component.predicate.WrittenBookPredicate import WrittenBookPredicate
    from generated_symbols.world.entity.display.Transformation import Transformation


@dataclass(kw_only=True)
class EntriesStruct:
    threshold: float
    model: ItemModel


type DataComponentStructBlockStateBlockItemStatesNone = dict[str, str]


@dataclass(kw_only=True)
class DataComponentStructCreativeSlotLock:
    pass


@dataclass(kw_only=True)
class ModelStructUnknown:
    type: SpecialModelType


@dataclass(kw_only=True)
class ModelStructBanner:
    type: Literal['minecraft:banner']
    color: DyeColor
    attachment: BannerAttachment | None = None  # Defaults to `ground`.


@dataclass(kw_only=True)
class ModelStructBed:
    type: Literal['minecraft:bed']
    texture: Annotated[str, IdSpec(registry='texture', path='entity/bed/')]
    part: BedPart


@dataclass(kw_only=True)
class ModelStructBook:
    type: Literal['minecraft:book']
    open_angle: float  # Angle in degrees between book cover and book centerline.  `0.0` for closed, `90.0` for open flat.
    page1: float  # The position of the first page inside the book.  `0.0` for leftmost, `1.0` for rightmost.
    page2: float  # The position of the second page inside the book.  `0.0` for leftmost, `1.0` for rightmost.


@dataclass(kw_only=True)
class ModelStructChest:
    type: Literal['minecraft:chest']
    texture: Annotated[str, IdSpec(registry='texture', path='entity/chest/')]
    openness: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None  # Defaults to `0`.
    chest_type: ChestType | None = None  # Defaults to `single`.


@dataclass(kw_only=True)
class ModelStructCopperGolemStatue:
    type: Literal['minecraft:copper_golem_statue']
    pose: CopperGolemStatuePose
    texture: str


@dataclass(kw_only=True)
class ModelStructEndCube:
    type: Literal['minecraft:end_cube']
    effect: EndCubeEffectType


@dataclass(kw_only=True)
class ModelStructHangingSign:
    type: Literal['minecraft:hanging_sign']
    wood_type: WoodType
    texture: Annotated[str, IdSpec(registry='texture', path='entity/signs/hanging/')] | None = None
    attachment: HangingSignAttachment | None = None  # Defaults to `ceiling_middle`.


@dataclass(kw_only=True)
class ModelStructHead:
    type: Literal['minecraft:head']
    kind: HeadType
    texture: Annotated[str, IdSpec(registry='texture', path='entity/')] | None = None  # Texture to use instead of the texture from `kind`.
    animation: float | None = None  # Controls the animation time for piglin and dragon heads. Defaults to `0`.


@dataclass(kw_only=True)
class ModelStructShulkerBox:
    type: Literal['minecraft:shulker_box']
    texture: Annotated[str, IdSpec(registry='texture', path='entity/shulker/')]
    openness: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None


@dataclass(kw_only=True)
class ModelStructStandingSign:
    type: Literal['minecraft:standing_sign']
    wood_type: WoodType
    texture: Annotated[str, IdSpec(registry='texture', path='entity/signs/')] | None = None
    attachement: StandingSignAttachment | None = None  # There is an extra "e" in the field name. See MC-307498.  Defaults to `ground`.


type ModelStruct = ModelStructUnknown | ModelStructBanner | ModelStructBed | ModelStructBook | ModelStructChest | ModelStructCopperGolemStatue | ModelStructEndCube | ModelStructHangingSign | ModelStructHead | ModelStructShulkerBox | ModelStructStandingSign

@dataclass(kw_only=True)
class ItemModelBundleSelectedItem:
    type: Literal['minecraft:bundle/selected_item']


@dataclass(kw_only=True)
class ItemModelComposite:
    type: Literal['minecraft:composite']
    models: list[ItemModel]
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ItemModelConditionUnknown:
    type: Literal['minecraft:condition']
    property: ConditionalPropertyType
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ItemModelConditionComponent:
    type: Literal['minecraft:condition']
    property: Literal['minecraft:component']
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    predicate: Annotated[str, IdSpec(registry='data_component_predicate_type')]  # The component predicate to check.
    value: None | AttributeModifiersPredicate | BundleContentsPredicate | ContainerPredicate | CustomData | ItemDamagePredicate | list[EnchantmentPredicate] | FireworkExplosionPredicate | FireworksPredicate | JukeboxPlayablePredicate | PotionsPredicate | TrimPredicate | Annotated[str, IdSpec(registry='villager_type', tags='allowed')] | list[Annotated[str, IdSpec(registry='villager_type')]] | WritableBookPredicate | WrittenBookPredicate  # The predicate-specific value.


@dataclass(kw_only=True)
class ItemModelConditionCustomModelData:
    type: Literal['minecraft:condition']
    property: Literal['minecraft:custom_model_data']
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    index: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The index of the `flags` list in the `custom_model_data` component. Defaults to 0.


@dataclass(kw_only=True)
class ItemModelConditionHasComponent:
    type: Literal['minecraft:condition']
    property: Literal['minecraft:has_component']
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    component: Annotated[str, IdSpec(registry='data_component_type')]
    ignore_default: bool | None = None  # Whether the default components should be handled as "no component". Defaults to false.


@dataclass(kw_only=True)
class ItemModelConditionKeybindDown:
    type: Literal['minecraft:condition']
    property: Literal['minecraft:keybind_down']
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    keybind: Keybind  # The keybind ID to check for.


@dataclass(kw_only=True)
class ItemModelConditionViewEntity:
    type: Literal['minecraft:condition']
    property: Literal['minecraft:view_entity']
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None


type ItemModelCondition = ItemModelConditionUnknown | ItemModelConditionComponent | ItemModelConditionCustomModelData | ItemModelConditionHasComponent | ItemModelConditionKeybindDown | ItemModelConditionViewEntity

@dataclass(kw_only=True)
class ItemModelModel:
    type: Literal['minecraft:model']
    model: ModelRef
    tints: list[ModelTint] | None = None
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ItemModelRangeDispatchUnknown:
    type: Literal['minecraft:range_dispatch']
    property: NumericPropertyType
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ItemModelRangeDispatchCompass:
    type: Literal['minecraft:range_dispatch']
    property: Literal['minecraft:compass']
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None
    target: CompassTarget
    wobble: bool | None = None  # Whether to oscillate for some time around target before settling. Defaults to true.


@dataclass(kw_only=True)
class ItemModelRangeDispatchCount:
    type: Literal['minecraft:range_dispatch']
    property: Literal['minecraft:count']
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None
    normalize: bool | None = None  # If false, returns count clamped to `0..max_stack_size`. If true, returns count divided by the `max_stack_size` component, clamped to `0..1`. Defaults to true.


@dataclass(kw_only=True)
class ItemModelRangeDispatchCustomModelData:
    type: Literal['minecraft:range_dispatch']
    property: Literal['minecraft:custom_model_data']
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None
    index: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The index of the `floats` list in the `custom_model_data` component. Defaults to 0.


@dataclass(kw_only=True)
class ItemModelRangeDispatchDamage:
    type: Literal['minecraft:range_dispatch']
    property: Literal['minecraft:damage']
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None
    normalize: bool | None = None  # If false, returns value of damage, clamped to `0..max_damage`. If true, returns value of damage divided by the `max_damage` component, clamped to `0..1`. Defaults to true.


@dataclass(kw_only=True)
class ItemModelRangeDispatchTime:
    type: Literal['minecraft:range_dispatch']
    property: Literal['minecraft:time']
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None
    source: TimeSource
    wobble: bool | None = None  # Whether to oscillate for some time around target before settling. Defaults to true.


@dataclass(kw_only=True)
class ItemModelRangeDispatchUseCycle:
    type: Literal['minecraft:range_dispatch']
    property: Literal['minecraft:use_cycle']
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None
    period: float | None = None  # returns remaining item use ticks modulo `period`. Defaults to 1.


@dataclass(kw_only=True)
class ItemModelRangeDispatchUseDuration:
    type: Literal['minecraft:range_dispatch']
    property: Literal['minecraft:use_duration']
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None
    remaining: bool | None = None  # If true, returns remaining item use ticks. If false, returns item use ticks so far. Defaults to false.


type ItemModelRangeDispatch = ItemModelRangeDispatchUnknown | ItemModelRangeDispatchCompass | ItemModelRangeDispatchCount | ItemModelRangeDispatchCustomModelData | ItemModelRangeDispatchDamage | ItemModelRangeDispatchTime | ItemModelRangeDispatchUseCycle | ItemModelRangeDispatchUseDuration

@dataclass(kw_only=True)
class ItemModelSelectUnknown(SelectCases[str]):
    type: Literal['minecraft:select']
    property: SelectPropertyType
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ItemModelSelectBlockState(SelectCases[str]):
    type: Literal['minecraft:select']
    property: Literal['minecraft:block_state']
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None
    block_state_property: str


@dataclass(kw_only=True)
class ItemModelSelectChargeType(SelectCases[CrossbowChargeType]):
    type: Literal['minecraft:select']
    property: Literal['minecraft:charge_type']
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ItemModelSelectComponent(SelectCases[int | SwingAnimation | AttackRange | list[AttributeModifier] | AxolotlVariant | list[BannerPatternLayer] | DyeColor | list[Occupant] | BlockEntityData | str | DataComponentStructBlockStateBlockItemStatesNone | Annotated[list[BlockTransformer], 'Length = 1-200 (both inclusive)'] | blocks_attacks | SoundEventRef | BrewingFuel | BucketEntityData | str | list[ItemStackTemplate] | AdventureModePredicate | Annotated[str, IdSpec(registry='cat_sound_variant')] | Annotated[str, IdSpec(registry='cat_variant')] | Annotated[str, IdSpec(registry='chicken_sound_variant')] | Annotated[str, IdSpec(registry='chicken_variant')] | Compostable | Consumable | Annotated[list[ContainerSlot], 'Length = up to 256 (inclusive)'] | ContainerLoot | CookingFuel | Annotated[str, IdSpec(registry='cow_sound_variant')] | Annotated[str, IdSpec(registry='cow_variant')] | DataComponentStructCreativeSlotLock | CustomData | CustomModelData | Text | Annotated[int, 'Range | Min `0` and above | inclusive'] | DamageResistant | Annotated[str, IdSpec(registry='damage_type')] | DamageType | DeathProtection | DebugStickState | RGB | Enchantable | bool | EnchantmentLevels | AnyEntity | str | Equippable | Explosion | Fireworks | Food | FoxType | Annotated[str, IdSpec(registry='frog_variant')] | HorseVariant | Annotated[str, IdSpec(registry='instrument')] | Instrument | Annotated[str, IdSpec(registry='item_definition')] | Annotated[str, IdSpec(registry='jukebox_song')] | KineticWeapon | LlamaVariant | ItemPredicate | LodestoneTracker | list[Text] | MapDecorations | Annotated[int, 'Range | Min `1` and above | inclusive'] | Annotated[int, 'Range | `1`-`99` | both inclusive'] | Annotated[float, 'Range | `0`-`1` | both inclusive'] | MobVisibility | MooshroomType | Annotated[str, IdSpec(registry='weighed_sound_event')] | Annotated[int, 'Range | `0`-`4` | both inclusive'] | Annotated[str, IdSpec(registry='painting_variant')] | ParrotVariant | PiercingWeapon | Annotated[str, IdSpec(registry='pig_sound_variant')] | Annotated[str, IdSpec(registry='pig_variant')] | PotDecorations | PotionContents | Annotated[str, IdSpec(registry='potion')] | Annotated[float, 'Range | Min `0` and above | inclusive'] | Profile | Annotated[str, IdSpec(registry='banner_pattern', tags='allowed')] | list[Annotated[str, IdSpec(registry='banner_pattern')]] | Annotated[str, IdSpec(registry='decorated_pot_pattern')] | Annotated[str, IdSpec(registry='trim_material')] | RabbitVariant | Rarity | list[Annotated[str, IdSpec(registry='recipe')]] | Repairable | SalmonType | SignText | ItemStackTemplate | list[SuspiciousStewEffect] | Tool | TooltipDisplay | Annotated[str, IdSpec()] | Trim | TropicalFishPattern | Unbreakable | UseCooldown | UseEffects | VillagerFood | Annotated[str, IdSpec(registry='villager_type')] | Weapon | Annotated[str, IdSpec(registry='wolf_sound_variant')] | Annotated[str, IdSpec(registry='wolf_variant')] | WritableBookContent | WrittenBookContent | Annotated[str, IdSpec(registry='zombie_nautilus_variant')]]):
    type: Literal['minecraft:select']
    property: Literal['minecraft:component']
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None
    component: Annotated[str, IdSpec(registry='data_component_type')]  # The component type to check the values of. If the selected value comes from a registry that the client doesn't have access to, the entry will be silently ignored.


@dataclass(kw_only=True)
class ItemModelSelectContextDimension(SelectCases[Annotated[str, IdSpec(registry='dimension')]]):
    type: Literal['minecraft:select']
    property: Literal['minecraft:context_dimension']
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ItemModelSelectContextEntityType(SelectCases[Annotated[str, IdSpec(registry='entity_type')]]):
    type: Literal['minecraft:select']
    property: Literal['minecraft:context_entity_type']
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ItemModelSelectCustomModelData(SelectCases[str]):
    type: Literal['minecraft:select']
    property: Literal['minecraft:custom_model_data']
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None
    index: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The index of the `strings` list in the `custom_model_data` component. Defaults to 0.


@dataclass(kw_only=True)
class ItemModelSelectDisplayContext(SelectCases[ItemDisplayContext]):
    type: Literal['minecraft:select']
    property: Literal['minecraft:display_context']
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ItemModelSelectLocalTime(SelectCases[str]):
    type: Literal['minecraft:select']
    property: Literal['minecraft:local_time']
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None
    pattern: str  # Format to use for time formatting. Examples: `yyyy-MM-dd`, `HH:mm:ss`.
    locale: str | None = None  # Defaults to the root locale. Examples: `en_US`, `cs_AU@numbers=thai;calendar=japanese`.
    time_zone: str | None = None  # Defaults to the timezone set on the client. Examples: `Europe/Stockholm`, `GMT+0:45`.


@dataclass(kw_only=True)
class ItemModelSelectMainHand(SelectCases[HumanoidArm]):
    type: Literal['minecraft:select']
    property: Literal['minecraft:main_hand']
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class ItemModelSelectTrimMaterial(SelectCases[Annotated[str, IdSpec(registry='trim_material')]]):
    type: Literal['minecraft:select']
    property: Literal['minecraft:trim_material']
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


type ItemModelSelect = ItemModelSelectUnknown | ItemModelSelectBlockState | ItemModelSelectChargeType | ItemModelSelectComponent | ItemModelSelectContextDimension | ItemModelSelectContextEntityType | ItemModelSelectCustomModelData | ItemModelSelectDisplayContext | ItemModelSelectLocalTime | ItemModelSelectMainHand | ItemModelSelectTrimMaterial

@dataclass(kw_only=True)
class ItemModelSpecial:
    type: Literal['minecraft:special']
    model: ModelStruct  # Renders a special hardcoded model.
    base: ModelRef  # Base model, providing transformations, particle texture and GUI light.
    transformation: Transformation | None = None


type ItemModel = ItemModelBundleSelectedItem | ItemModelComposite | ItemModelCondition | ItemModelModel | ItemModelRangeDispatch | ItemModelSelect | ItemModelSpecial


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::ItemModel": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::item_definition::ItemModeltype",
                    "attributes": [
                        {
                            "name": "id"
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:item_model"
                }
            }
        ]
    }
}

