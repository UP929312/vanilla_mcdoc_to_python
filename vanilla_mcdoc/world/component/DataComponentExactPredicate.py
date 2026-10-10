"""
Generated from symbols.json for ::java::world::component::DataComponentExactPredicate
Local link to file: vanilla_mcdoc/world/component/DataComponentExactPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
    from vanilla_mcdoc.data.damage_type.DamageType import DamageType
    from vanilla_mcdoc.data.util.SoundEventRef import SoundEventRef
    from vanilla_mcdoc.data.variants.instrument.Instrument import Instrument
    from vanilla_mcdoc.util.avatar.Profile import Profile
    from vanilla_mcdoc.util.color.DyeColor import DyeColor
    from vanilla_mcdoc.util.color.RGB import RGB
    from vanilla_mcdoc.util.text.Text import Text
    from vanilla_mcdoc.world.block.BlockEntityData import BlockEntityData
    from vanilla_mcdoc.world.block.banner.BannerPatternLayer import BannerPatternLayer
    from vanilla_mcdoc.world.component.CustomData import CustomData
    from vanilla_mcdoc.world.component.PersistentDataComponent import PersistentDataComponent
    from vanilla_mcdoc.world.component.block.ContainerLoot import ContainerLoot
    from vanilla_mcdoc.world.component.block.ContainerSlot import ContainerSlot
    from vanilla_mcdoc.world.component.block.Occupant import Occupant
    from vanilla_mcdoc.world.component.block.PotDecorations import PotDecorations
    from vanilla_mcdoc.world.component.block.SignText import SignText
    from vanilla_mcdoc.world.component.entity.AxolotlVariant import AxolotlVariant
    from vanilla_mcdoc.world.component.entity.FoxType import FoxType
    from vanilla_mcdoc.world.component.entity.HorseVariant import HorseVariant
    from vanilla_mcdoc.world.component.entity.LlamaVariant import LlamaVariant
    from vanilla_mcdoc.world.component.entity.MooshroomType import MooshroomType
    from vanilla_mcdoc.world.component.entity.ParrotVariant import ParrotVariant
    from vanilla_mcdoc.world.component.entity.RabbitVariant import RabbitVariant
    from vanilla_mcdoc.world.component.entity.SalmonType import SalmonType
    from vanilla_mcdoc.world.component.entity.TropicalFishPattern import TropicalFishPattern
    from vanilla_mcdoc.world.component.item.AdventureModePredicate import AdventureModePredicate
    from vanilla_mcdoc.world.component.item.AttackRange import AttackRange
    from vanilla_mcdoc.world.component.item.AttributeModifier import AttributeModifier
    from vanilla_mcdoc.world.component.item.BrewingFuel import BrewingFuel
    from vanilla_mcdoc.world.component.item.BucketEntityData import BucketEntityData
    from vanilla_mcdoc.world.component.item.Compostable import Compostable
    from vanilla_mcdoc.world.component.item.Consumable import Consumable
    from vanilla_mcdoc.world.component.item.CookingFuel import CookingFuel
    from vanilla_mcdoc.world.component.item.CustomModelData import CustomModelData
    from vanilla_mcdoc.world.component.item.DamageResistant import DamageResistant
    from vanilla_mcdoc.world.component.item.DeathProtection import DeathProtection
    from vanilla_mcdoc.world.component.item.DebugStickState import DebugStickState
    from vanilla_mcdoc.world.component.item.Enchantable import Enchantable
    from vanilla_mcdoc.world.component.item.EnchantmentLevels import EnchantmentLevels
    from vanilla_mcdoc.world.component.item.Equippable import Equippable
    from vanilla_mcdoc.world.component.item.Explosion import Explosion
    from vanilla_mcdoc.world.component.item.Fireworks import Fireworks
    from vanilla_mcdoc.world.component.item.Food import Food
    from vanilla_mcdoc.world.component.item.KineticWeapon import KineticWeapon
    from vanilla_mcdoc.world.component.item.LodestoneTracker import LodestoneTracker
    from vanilla_mcdoc.world.component.item.MapDecorations import MapDecorations
    from vanilla_mcdoc.world.component.item.MobVisibility import MobVisibility
    from vanilla_mcdoc.world.component.item.PiercingWeapon import PiercingWeapon
    from vanilla_mcdoc.world.component.item.PotionContents import PotionContents
    from vanilla_mcdoc.world.component.item.Rarity import Rarity
    from vanilla_mcdoc.world.component.item.Repairable import Repairable
    from vanilla_mcdoc.world.component.item.SuspiciousStewEffect import SuspiciousStewEffect
    from vanilla_mcdoc.world.component.item.SwingAnimation import SwingAnimation
    from vanilla_mcdoc.world.component.item.Tool import Tool
    from vanilla_mcdoc.world.component.item.TooltipDisplay import TooltipDisplay
    from vanilla_mcdoc.world.component.item.Trim import Trim
    from vanilla_mcdoc.world.component.item.Unbreakable import Unbreakable
    from vanilla_mcdoc.world.component.item.UseCooldown import UseCooldown
    from vanilla_mcdoc.world.component.item.UseEffects import UseEffects
    from vanilla_mcdoc.world.component.item.VillagerFood import VillagerFood
    from vanilla_mcdoc.world.component.item.Weapon import Weapon
    from vanilla_mcdoc.world.component.item.WritableBookContent import WritableBookContent
    from vanilla_mcdoc.world.component.item.WrittenBookContent import WrittenBookContent
    from vanilla_mcdoc.world.component.item.blocks_attacks import blocks_attacks
    from vanilla_mcdoc.world.entity.AnyEntity import AnyEntity
    from vanilla_mcdoc.world.item.ItemStackTemplate import ItemStackTemplate


class DataComponentExactPredicateValueStructDataComponentCreativeSlotLock(GeneratedModel):
    pass


class DataComponentExactPredicateValueStructDataComponentWaxed(GeneratedModel):
    pass


type DataComponentExactPredicate = dict[PersistentDataComponent, int | SwingAnimation | AttackRange | list[AttributeModifier] | AxolotlVariant | list[BannerPatternLayer] | DyeColor | list[Occupant] | BlockEntityData | str | dict[str, str] | Annotated[str, IdSpec(registry='block_transformer')] | blocks_attacks | SoundEventRef | BrewingFuel | BucketEntityData | str | list[ItemStackTemplate] | AdventureModePredicate | Annotated[str, IdSpec(registry='cat_sound_variant')] | Annotated[str, IdSpec(registry='cat_variant')] | Annotated[str, IdSpec(registry='chicken_sound_variant')] | Annotated[str, IdSpec(registry='chicken_variant')] | Compostable | Consumable | Annotated[list[ContainerSlot], Field(max_length=256)] | ContainerLoot | CookingFuel | Annotated[str, IdSpec(registry='cow_sound_variant')] | Annotated[str, IdSpec(registry='cow_variant')] | DataComponentExactPredicateValueStructDataComponentCreativeSlotLock | CustomData | CustomModelData | Text | Annotated[int, Field(ge=0)] | DamageResistant | Annotated[str, IdSpec(registry='damage_type')] | DamageType | DeathProtection | DebugStickState | RGB | Enchantable | bool | EnchantmentLevels | AnyEntity | str | Equippable | Explosion | Fireworks | Food | FoxType | Annotated[str, IdSpec(registry='frog_variant')] | HorseVariant | Annotated[str, IdSpec(registry='instrument')] | Instrument | Annotated[str, IdSpec(registry='item_definition')] | Annotated[str, IdSpec(registry='jukebox_song')] | KineticWeapon | LlamaVariant | ItemPredicate | LodestoneTracker | list[Text] | MapDecorations | Annotated[int, Field(ge=1)] | Annotated[int, Field(ge=1, le=99)] | Annotated[float, Field(ge=0, le=1)] | MobVisibility | MooshroomType | Annotated[str, IdSpec(registry='weighed_sound_event')] | Annotated[int, Field(ge=0, le=4)] | Annotated[str, IdSpec(registry='painting_variant')] | ParrotVariant | PiercingWeapon | Annotated[str, IdSpec(registry='pig_sound_variant')] | Annotated[str, IdSpec(registry='pig_variant')] | PotDecorations | PotionContents | Annotated[str, IdSpec(registry='potion')] | Annotated[float, Field(ge=0)] | Profile | Annotated[str, IdSpec(registry='banner_pattern', tags='allowed')] | list[Annotated[str, IdSpec(registry='banner_pattern')]] | Annotated[str, IdSpec(registry='decorated_pot_pattern')] | Annotated[str, IdSpec(registry='trim_material')] | RabbitVariant | Rarity | list[Annotated[str, IdSpec(registry='recipe')]] | Repairable | SalmonType | SignText | ItemStackTemplate | list[SuspiciousStewEffect] | Tool | TooltipDisplay | Annotated[str, IdSpec()] | Trim | TropicalFishPattern | Unbreakable | UseCooldown | UseEffects | VillagerFood | Annotated[str, IdSpec(registry='villager_type')] | DataComponentExactPredicateValueStructDataComponentWaxed | Weapon | Annotated[str, IdSpec(registry='wolf_sound_variant')] | Annotated[str, IdSpec(registry='wolf_variant')] | WritableBookContent | WrittenBookContent | Annotated[str, IdSpec(registry='zombie_nautilus_variant')]]
