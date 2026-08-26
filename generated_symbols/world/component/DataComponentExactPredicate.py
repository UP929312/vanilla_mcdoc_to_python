"""
Generated from symbols.json for ::java::world::component::DataComponentExactPredicate
Local link to file: generated_symbols/world/component/DataComponentExactPredicate.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.ItemPredicate import ItemPredicate
    from generated_symbols.data.damage_type.DamageType import DamageType
    from generated_symbols.data.util.SoundEventRef import SoundEventRef
    from generated_symbols.data.variants.instrument.Instrument import Instrument
    from generated_symbols.util.avatar.Profile import Profile
    from generated_symbols.util.color.DyeColor import DyeColor
    from generated_symbols.util.color.RGB import RGB
    from generated_symbols.util.text.Text import Text
    from generated_symbols.world.block.BlockEntityData import BlockEntityData
    from generated_symbols.world.block.banner.BannerPatternLayer import BannerPatternLayer
    from generated_symbols.world.component.CustomData import CustomData
    from generated_symbols.world.component.PersistentDataComponent import PersistentDataComponent
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


type DataComponentExactPredicateValueStructDataComponentBlockStateBlockItemStatesNone = dict[str, str]


@dataclass(kw_only=True)
class DataComponentExactPredicateValueStructDataComponentCreativeSlotLock:
    pass


@dataclass(kw_only=True)
class DataComponentExactPredicateValueStructDataComponentFireResistant:
    pass


@dataclass(kw_only=True)
class DataComponentExactPredicateValueStructDataComponentHideAdditionalTooltip:
    pass


@dataclass(kw_only=True)
class DataComponentExactPredicateValueStructDataComponentWaxed:
    pass


type DataComponentExactPredicate = dict[PersistentDataComponent, int | SwingAnimation | AttackRange | list[AttributeModifier] | AxolotlVariant | list[BannerPatternLayer] | DyeColor | list[Occupant] | BlockEntityData | str | DataComponentExactPredicateValueStructDataComponentBlockStateBlockItemStatesNone | Annotated[str, IdSpec(registry='block_transformer')] | blocks_attacks | SoundEventRef | BrewingFuel | BucketEntityData | str | list[ItemStackTemplate] | AdventureModePredicate | Annotated[str, IdSpec(registry='cat_sound_variant')] | Annotated[str, IdSpec(registry='cat_variant')] | Annotated[str, IdSpec(registry='chicken_sound_variant')] | Annotated[str, IdSpec(registry='chicken_variant')] | Compostable | Consumable | Annotated[list[ContainerSlot], 'Length = up to 256 (inclusive)'] | ContainerLoot | CookingFuel | Annotated[str, IdSpec(registry='cow_sound_variant')] | Annotated[str, IdSpec(registry='cow_variant')] | DataComponentExactPredicateValueStructDataComponentCreativeSlotLock | CustomData | CustomModelData | Text | Annotated[int, 'Range | Min `0` and above | inclusive'] | DamageResistant | Annotated[str, IdSpec(registry='damage_type')] | DamageType | DeathProtection | DebugStickState | RGB | Enchantable | bool | EnchantmentLevels | AnyEntity | str | Equippable | DataComponentExactPredicateValueStructDataComponentFireResistant | Explosion | Fireworks | Food | FoxType | Annotated[str, IdSpec(registry='frog_variant')] | DataComponentExactPredicateValueStructDataComponentHideAdditionalTooltip | HorseVariant | Annotated[str, IdSpec(registry='instrument')] | Instrument | Annotated[str, IdSpec(registry='item_definition')] | Annotated[str, IdSpec(registry='jukebox_song')] | KineticWeapon | LlamaVariant | ItemPredicate | LodestoneTracker | list[Text] | MapDecorations | Annotated[int, 'Range | Min `1` and above | inclusive'] | Annotated[int, 'Range | `1`-`99` | both inclusive'] | Annotated[float, 'Range | `0`-`1` | both inclusive'] | MobVisibility | MooshroomType | Annotated[str, IdSpec(registry='weighed_sound_event')] | Annotated[int, 'Range | `0`-`4` | both inclusive'] | Annotated[str, IdSpec(registry='painting_variant')] | ParrotVariant | PiercingWeapon | Annotated[str, IdSpec(registry='pig_sound_variant')] | Annotated[str, IdSpec(registry='pig_variant')] | PotDecorations | PotionContents | Annotated[str, IdSpec(registry='potion')] | Annotated[float, 'Range | Min `0` and above | inclusive'] | Profile | Annotated[str, IdSpec(registry='banner_pattern', tags='allowed')] | list[Annotated[str, IdSpec(registry='banner_pattern')]] | Annotated[str, IdSpec(registry='decorated_pot_pattern')] | Annotated[str, IdSpec(registry='trim_material')] | RabbitVariant | Rarity | list[Annotated[str, IdSpec(registry='recipe')]] | Repairable | SalmonType | SignText | ItemStackTemplate | list[SuspiciousStewEffect] | Tool | TooltipDisplay | Annotated[str, IdSpec()] | Trim | TropicalFishPattern | Unbreakable | UseCooldown | UseEffects | VillagerFood | Annotated[str, IdSpec(registry='villager_type')] | DataComponentExactPredicateValueStructDataComponentWaxed | Weapon | Annotated[str, IdSpec(registry='wolf_sound_variant')] | Annotated[str, IdSpec(registry='wolf_variant')] | WritableBookContent | WrittenBookContent | Annotated[str, IdSpec(registry='zombie_nautilus_variant')]]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::DataComponentExactPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
                    "kind": "reference",
                    "path": "::java::world::component::PersistentDataComponent"
                },
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                {
                                    "keyword": "key"
                                }
                            ]
                        }
                    ],
                    "registry": "minecraft:data_component"
                }
            }
        ]
    }
}

