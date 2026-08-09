# Generated from symbols.json for ::java::assets::item_definition::Select
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from generated_symbols.assets.item_definition.SelectCases import SelectCases
from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.CrossbowChargeType import CrossbowChargeType
    from generated_symbols.assets.item_definition.ItemModel import ItemModel
    from generated_symbols.assets.item_definition.SelectPropertyType import SelectPropertyType
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
    from generated_symbols.world.entity.display.Transformation import Transformation
    from generated_symbols.world.item.ItemStackTemplate import ItemStackTemplate


type DataComponentStructBlockStateBlockItemStatesNone = dict[str, str]


@dataclass(kw_only=True)
class DataComponentStructCreativeSlotLock:
    pass


@dataclass(kw_only=True)
class SelectUnknown(SelectCases[str]):
    property: SelectPropertyType
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class SelectBlockState(SelectCases[str]):
    property: Literal['minecraft:block_state']
    block_state_property: str
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class SelectChargeType(SelectCases[CrossbowChargeType]):
    property: Literal['minecraft:charge_type']
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class SelectComponent(SelectCases[int | SwingAnimation | AttackRange | list[AttributeModifier] | AxolotlVariant | list[BannerPatternLayer] | DyeColor | list[Occupant] | BlockEntityData | str | DataComponentStructBlockStateBlockItemStatesNone | Annotated[list[BlockTransformer], 'Length = 1-200 (both inclusive)'] | blocks_attacks | SoundEventRef | BrewingFuel | BucketEntityData | str | list[ItemStackTemplate] | AdventureModePredicate | Annotated[str, IdSpec(registry='cat_sound_variant')] | Annotated[str, IdSpec(registry='cat_variant')] | Annotated[str, IdSpec(registry='chicken_sound_variant')] | Annotated[str, IdSpec(registry='chicken_variant')] | Compostable | Consumable | Annotated[list[ContainerSlot], 'Length = up to 256 (inclusive)'] | ContainerLoot | CookingFuel | Annotated[str, IdSpec(registry='cow_sound_variant')] | Annotated[str, IdSpec(registry='cow_variant')] | DataComponentStructCreativeSlotLock | CustomData | CustomModelData | Text | Annotated[int, 'Range | Min `0` and above | inclusive'] | DamageResistant | Annotated[str, IdSpec(registry='damage_type')] | DamageType | DeathProtection | DebugStickState | RGB | Enchantable | bool | EnchantmentLevels | AnyEntity | str | Equippable | Explosion | Fireworks | Food | FoxType | Annotated[str, IdSpec(registry='frog_variant')] | HorseVariant | Annotated[str, IdSpec(registry='instrument')] | Instrument | Annotated[str, IdSpec(registry='item_definition')] | Annotated[str, IdSpec(registry='jukebox_song')] | KineticWeapon | LlamaVariant | ItemPredicate | LodestoneTracker | list[Text] | MapDecorations | Annotated[int, 'Range | Min `1` and above | inclusive'] | Annotated[int, 'Range | `1`-`99` | both inclusive'] | Annotated[float, 'Range | `0`-`1` | both inclusive'] | MobVisibility | MooshroomType | Annotated[str, IdSpec(registry='weighed_sound_event')] | Annotated[int, 'Range | `0`-`4` | both inclusive'] | Annotated[str, IdSpec(registry='painting_variant')] | ParrotVariant | PiercingWeapon | Annotated[str, IdSpec(registry='pig_sound_variant')] | Annotated[str, IdSpec(registry='pig_variant')] | PotDecorations | PotionContents | Annotated[str, IdSpec(registry='potion')] | Annotated[float, 'Range | Min `0` and above | inclusive'] | Profile | Annotated[str, IdSpec(registry='banner_pattern', tags='allowed')] | list[Annotated[str, IdSpec(registry='banner_pattern')]] | Annotated[str, IdSpec(registry='decorated_pot_pattern')] | Annotated[str, IdSpec(registry='trim_material')] | RabbitVariant | Rarity | list[Annotated[str, IdSpec(registry='recipe')]] | Repairable | SalmonType | SignText | ItemStackTemplate | list[SuspiciousStewEffect] | Tool | TooltipDisplay | Annotated[str, IdSpec()] | Trim | TropicalFishPattern | Unbreakable | UseCooldown | UseEffects | VillagerFood | Annotated[str, IdSpec(registry='villager_type')] | Weapon | Annotated[str, IdSpec(registry='wolf_sound_variant')] | Annotated[str, IdSpec(registry='wolf_variant')] | WritableBookContent | WrittenBookContent | Annotated[str, IdSpec(registry='zombie_nautilus_variant')]]):
    property: Literal['minecraft:component']
    component: Annotated[str, IdSpec(registry='data_component_type')]  # The component type to check the values of. If the selected value comes from a registry that the client doesn't have access to, the entry will be silently ignored.
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class SelectContextDimension(SelectCases[Annotated[str, IdSpec(registry='dimension')]]):
    property: Literal['minecraft:context_dimension']
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class SelectContextEntityType(SelectCases[Annotated[str, IdSpec(registry='entity_type')]]):
    property: Literal['minecraft:context_entity_type']
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class SelectCustomModelData(SelectCases[str]):
    property: Literal['minecraft:custom_model_data']
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None
    index: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The index of the `strings` list in the `custom_model_data` component. Defaults to 0.


@dataclass(kw_only=True)
class SelectDisplayContext(SelectCases[ItemDisplayContext]):
    property: Literal['minecraft:display_context']
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class SelectLocalTime(SelectCases[str]):
    property: Literal['minecraft:local_time']
    pattern: str  # Format to use for time formatting. Examples: `yyyy-MM-dd`, `HH:mm:ss`.
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None
    locale: str | None = None  # Defaults to the root locale. Examples: `en_US`, `cs_AU@numbers=thai;calendar=japanese`.
    time_zone: str | None = None  # Defaults to the timezone set on the client. Examples: `Europe/Stockholm`, `GMT+0:45`.


@dataclass(kw_only=True)
class SelectMainHand(SelectCases[HumanoidArm]):
    property: Literal['minecraft:main_hand']
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


@dataclass(kw_only=True)
class SelectTrimMaterial(SelectCases[Annotated[str, IdSpec(registry='trim_material')]]):
    property: Literal['minecraft:trim_material']
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


type Select = SelectUnknown | SelectBlockState | SelectChargeType | SelectComponent | SelectContextDimension | SelectContextEntityType | SelectCustomModelData | SelectDisplayContext | SelectLocalTime | SelectMainHand | SelectTrimMaterial


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::Select": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "property",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::item_definition::SelectPropertyType",
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
                                "property"
                            ]
                        }
                    ],
                    "registry": "minecraft:select_item_property"
                }
            },
            {
                "kind": "pair",
                "desc": "Item model to render if none of the cases matched the value.",
                "key": "fallback",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::item_definition::ItemModel"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.1"
                            }
                        }
                    }
                ],
                "key": "transformation",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::display::Transformation"
                },
                "optional": True
            }
        ]
    }
}

