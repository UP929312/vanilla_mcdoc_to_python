"""
Generated from symbols.json for ::java::world::component::DataComponentPatch
Local link to file: vanilla_mcdoc/world/component/DataComponentPatch.py
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
    from vanilla_mcdoc.world.component.item.BlocksAttacks import BlocksAttacks
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
    from vanilla_mcdoc.world.entity.AnyEntity import AnyEntity
    from vanilla_mcdoc.world.item.ItemStackTemplate import ItemStackTemplate


class CreativeSlotLockStruct(GeneratedModel):
    pass


class GliderStruct(GeneratedModel):
    pass


class IntangibleProjectileStruct(GeneratedModel):
    pass


class MapPostProcessingStruct(GeneratedModel):
    pass


class WaxedStruct(GeneratedModel):
    pass


class DataComponentPatchValueStruct(GeneratedModel):
    pass


class DataComponentPatch(GeneratedModel):
    additional_trade_cost: int | None = Field(default=None, validation_alias='minecraft:additional_trade_cost', serialization_alias='minecraft:additional_trade_cost')
    attack_animation: SwingAnimation | None = Field(default=None, validation_alias='minecraft:attack_animation', serialization_alias='minecraft:attack_animation')
    attack_range: AttackRange | None = Field(default=None, validation_alias='minecraft:attack_range', serialization_alias='minecraft:attack_range')
    attribute_modifiers: list[AttributeModifier] | None = Field(default=None, validation_alias='minecraft:attribute_modifiers', serialization_alias='minecraft:attribute_modifiers')
    axolotl_variant: AxolotlVariant | None = Field(default=None, validation_alias='minecraft:axolotl/variant', serialization_alias='minecraft:axolotl/variant')
    banner_patterns: list[BannerPatternLayer] | None = Field(default=None, validation_alias='minecraft:banner_patterns', serialization_alias='minecraft:banner_patterns')
    base_color: DyeColor | None = Field(default=None, validation_alias='minecraft:base_color', serialization_alias='minecraft:base_color')
    bees: list[Occupant] | None = Field(default=None, validation_alias='minecraft:bees', serialization_alias='minecraft:bees')
    block_entity_data: BlockEntityData | str | None = Field(default=None, validation_alias='minecraft:block_entity_data', serialization_alias='minecraft:block_entity_data')
    block_state: dict[str, str] | None = Field(default=None, validation_alias='minecraft:block_state', serialization_alias='minecraft:block_state')
    block_transformer: Annotated[str, IdSpec(registry='block_transformer')] | None = Field(default=None, validation_alias='minecraft:block_transformer', serialization_alias='minecraft:block_transformer')
    blocks_attacks: BlocksAttacks | None = Field(default=None, validation_alias='minecraft:blocks_attacks', serialization_alias='minecraft:blocks_attacks')
    break_sound: SoundEventRef | None = Field(default=None, validation_alias='minecraft:break_sound', serialization_alias='minecraft:break_sound')
    brewing_fuel: BrewingFuel | None = Field(default=None, validation_alias='minecraft:brewing_fuel', serialization_alias='minecraft:brewing_fuel')
    bucket_entity_data: BucketEntityData | str | None = Field(default=None, validation_alias='minecraft:bucket_entity_data', serialization_alias='minecraft:bucket_entity_data')
    bundle_contents: list[ItemStackTemplate] | None = Field(default=None, validation_alias='minecraft:bundle_contents', serialization_alias='minecraft:bundle_contents')
    can_break: AdventureModePredicate | None = Field(default=None, validation_alias='minecraft:can_break', serialization_alias='minecraft:can_break')
    can_place_on: AdventureModePredicate | None = Field(default=None, validation_alias='minecraft:can_place_on', serialization_alias='minecraft:can_place_on')
    cat_collar: DyeColor | None = Field(default=None, validation_alias='minecraft:cat/collar', serialization_alias='minecraft:cat/collar')
    cat_sound_variant: Annotated[str, IdSpec(registry='cat_sound_variant')] | None = Field(default=None, validation_alias='minecraft:cat/sound_variant', serialization_alias='minecraft:cat/sound_variant')
    cat_variant: Annotated[str, IdSpec(registry='cat_variant')] | None = Field(default=None, validation_alias='minecraft:cat/variant', serialization_alias='minecraft:cat/variant')
    charged_projectiles: list[ItemStackTemplate] | None = Field(default=None, validation_alias='minecraft:charged_projectiles', serialization_alias='minecraft:charged_projectiles')
    chicken_sound_variant: Annotated[str, IdSpec(registry='chicken_sound_variant')] | None = Field(default=None, validation_alias='minecraft:chicken/sound_variant', serialization_alias='minecraft:chicken/sound_variant')
    chicken_variant: Annotated[str, IdSpec(registry='chicken_variant')] | None = Field(default=None, validation_alias='minecraft:chicken/variant', serialization_alias='minecraft:chicken/variant')
    compostable: Compostable | None = Field(default=None, validation_alias='minecraft:compostable', serialization_alias='minecraft:compostable')
    consumable: Consumable | None = Field(default=None, validation_alias='minecraft:consumable', serialization_alias='minecraft:consumable')
    container: Annotated[list[ContainerSlot], Field(max_length=256)] | None = Field(default=None, validation_alias='minecraft:container', serialization_alias='minecraft:container')
    container_loot: ContainerLoot | None = Field(default=None, validation_alias='minecraft:container_loot', serialization_alias='minecraft:container_loot')
    cooking_fuel: CookingFuel | None = Field(default=None, validation_alias='minecraft:cooking_fuel', serialization_alias='minecraft:cooking_fuel')
    cow_sound_variant: Annotated[str, IdSpec(registry='cow_sound_variant')] | None = Field(default=None, validation_alias='minecraft:cow/sound_variant', serialization_alias='minecraft:cow/sound_variant')
    cow_variant: Annotated[str, IdSpec(registry='cow_variant')] | None = Field(default=None, validation_alias='minecraft:cow/variant', serialization_alias='minecraft:cow/variant')
    creative_slot_lock: CreativeSlotLockStruct | None = Field(default=None, validation_alias='minecraft:creative_slot_lock', serialization_alias='minecraft:creative_slot_lock')
    cushion_color: DyeColor | None = Field(default=None, validation_alias='minecraft:cushion/color', serialization_alias='minecraft:cushion/color')
    custom_data: CustomData | None = Field(default=None, validation_alias='minecraft:custom_data', serialization_alias='minecraft:custom_data')
    custom_model_data: CustomModelData | None = Field(default=None, validation_alias='minecraft:custom_model_data', serialization_alias='minecraft:custom_model_data')
    custom_name: Text | None = Field(default=None, validation_alias='minecraft:custom_name', serialization_alias='minecraft:custom_name')
    damage: Annotated[int, Field(ge=0)] | None = Field(default=None, validation_alias='minecraft:damage', serialization_alias='minecraft:damage')
    damage_resistant: DamageResistant | None = Field(default=None, validation_alias='minecraft:damage_resistant', serialization_alias='minecraft:damage_resistant')
    damage_type: Annotated[str, IdSpec(registry='damage_type')] | DamageType | None = Field(default=None, validation_alias='minecraft:damage_type', serialization_alias='minecraft:damage_type')
    death_protection: DeathProtection | None = Field(default=None, validation_alias='minecraft:death_protection', serialization_alias='minecraft:death_protection')
    debug_stick_state: DebugStickState | None = Field(default=None, validation_alias='minecraft:debug_stick_state', serialization_alias='minecraft:debug_stick_state')
    dye: DyeColor | None = Field(default=None, validation_alias='minecraft:dye', serialization_alias='minecraft:dye')
    dyed_color: RGB | None = Field(default=None, validation_alias='minecraft:dyed_color', serialization_alias='minecraft:dyed_color')
    enchantable: Enchantable | None = Field(default=None, validation_alias='minecraft:enchantable', serialization_alias='minecraft:enchantable')
    enchantment_glint_override: bool | None = Field(default=None, validation_alias='minecraft:enchantment_glint_override', serialization_alias='minecraft:enchantment_glint_override')
    enchantments: EnchantmentLevels | None = Field(default=None, validation_alias='minecraft:enchantments', serialization_alias='minecraft:enchantments')
    entity_data: AnyEntity | str | None = Field(default=None, validation_alias='minecraft:entity_data', serialization_alias='minecraft:entity_data')
    equippable: Equippable | None = Field(default=None, validation_alias='minecraft:equippable', serialization_alias='minecraft:equippable')
    firework_explosion: Explosion | None = Field(default=None, validation_alias='minecraft:firework_explosion', serialization_alias='minecraft:firework_explosion')
    fireworks: Fireworks | None = Field(default=None, validation_alias='minecraft:fireworks', serialization_alias='minecraft:fireworks')
    food: Food | None = Field(default=None, validation_alias='minecraft:food', serialization_alias='minecraft:food')
    fox_variant: FoxType | None = Field(default=None, validation_alias='minecraft:fox/variant', serialization_alias='minecraft:fox/variant')
    frog_variant: Annotated[str, IdSpec(registry='frog_variant')] | None = Field(default=None, validation_alias='minecraft:frog/variant', serialization_alias='minecraft:frog/variant')
    glider: GliderStruct | None = Field(default=None, validation_alias='minecraft:glider', serialization_alias='minecraft:glider')
    horse_variant: HorseVariant | None = Field(default=None, validation_alias='minecraft:horse/variant', serialization_alias='minecraft:horse/variant')
    instrument: Annotated[str, IdSpec(registry='instrument')] | Instrument | None = Field(default=None, validation_alias='minecraft:instrument', serialization_alias='minecraft:instrument')
    intangible_projectile: IntangibleProjectileStruct | None = Field(default=None, validation_alias='minecraft:intangible_projectile', serialization_alias='minecraft:intangible_projectile')
    interact_animation: SwingAnimation | None = Field(default=None, validation_alias='minecraft:interact_animation', serialization_alias='minecraft:interact_animation')
    item_model: Annotated[str, IdSpec(registry='item_definition')] | None = Field(default=None, validation_alias='minecraft:item_model', serialization_alias='minecraft:item_model')
    item_name: Text | None = Field(default=None, validation_alias='minecraft:item_name', serialization_alias='minecraft:item_name')
    jukebox_playable: Annotated[str, IdSpec(registry='jukebox_song')] | None = Field(default=None, validation_alias='minecraft:jukebox_playable', serialization_alias='minecraft:jukebox_playable')
    kinetic_weapon: KineticWeapon | None = Field(default=None, validation_alias='minecraft:kinetic_weapon', serialization_alias='minecraft:kinetic_weapon')
    llama_variant: LlamaVariant | None = Field(default=None, validation_alias='minecraft:llama/variant', serialization_alias='minecraft:llama/variant')
    lock: ItemPredicate | None = Field(default=None, validation_alias='minecraft:lock', serialization_alias='minecraft:lock')
    lodestone_tracker: LodestoneTracker | None = Field(default=None, validation_alias='minecraft:lodestone_tracker', serialization_alias='minecraft:lodestone_tracker')
    lore: list[Text] | None = Field(default=None, validation_alias='minecraft:lore', serialization_alias='minecraft:lore')
    map_decorations: MapDecorations | None = Field(default=None, validation_alias='minecraft:map_decorations', serialization_alias='minecraft:map_decorations')
    map_id: int | None = Field(default=None, validation_alias='minecraft:map_id', serialization_alias='minecraft:map_id')
    map_post_processing: MapPostProcessingStruct | None = Field(default=None, validation_alias='minecraft:map_post_processing', serialization_alias='minecraft:map_post_processing')
    max_damage: Annotated[int, Field(ge=1)] | None = Field(default=None, validation_alias='minecraft:max_damage', serialization_alias='minecraft:max_damage')
    max_stack_size: Annotated[int, Field(ge=1, le=99)] | None = Field(default=None, validation_alias='minecraft:max_stack_size', serialization_alias='minecraft:max_stack_size')
    minimum_attack_charge: Annotated[float, Field(ge=0, le=1)] | None = Field(default=None, validation_alias='minecraft:minimum_attack_charge', serialization_alias='minecraft:minimum_attack_charge')
    mob_visibility: MobVisibility | None = Field(default=None, validation_alias='minecraft:mob_visibility', serialization_alias='minecraft:mob_visibility')
    mooshroom_variant: MooshroomType | None = Field(default=None, validation_alias='minecraft:mooshroom/variant', serialization_alias='minecraft:mooshroom/variant')
    note_block_sound: Annotated[str, IdSpec(registry='weighed_sound_event')] | None = Field(default=None, validation_alias='minecraft:note_block_sound', serialization_alias='minecraft:note_block_sound')
    ominous_bottle_amplifier: Annotated[int, Field(ge=0, le=4)] | None = Field(default=None, validation_alias='minecraft:ominous_bottle_amplifier', serialization_alias='minecraft:ominous_bottle_amplifier')
    painting_variant: Annotated[str, IdSpec(registry='painting_variant')] | None = Field(default=None, validation_alias='minecraft:painting/variant', serialization_alias='minecraft:painting/variant')
    parrot_variant: ParrotVariant | None = Field(default=None, validation_alias='minecraft:parrot/variant', serialization_alias='minecraft:parrot/variant')
    piercing_weapon: PiercingWeapon | None = Field(default=None, validation_alias='minecraft:piercing_weapon', serialization_alias='minecraft:piercing_weapon')
    pig_sound_variant: Annotated[str, IdSpec(registry='pig_sound_variant')] | None = Field(default=None, validation_alias='minecraft:pig/sound_variant', serialization_alias='minecraft:pig/sound_variant')
    pig_variant: Annotated[str, IdSpec(registry='pig_variant')] | None = Field(default=None, validation_alias='minecraft:pig/variant', serialization_alias='minecraft:pig/variant')
    pot_decorations: PotDecorations | None = Field(default=None, validation_alias='minecraft:pot_decorations', serialization_alias='minecraft:pot_decorations')
    potion_contents: PotionContents | Annotated[str, IdSpec(registry='potion')] | None = Field(default=None, validation_alias='minecraft:potion_contents', serialization_alias='minecraft:potion_contents')
    potion_duration_scale: Annotated[float, Field(ge=0)] | None = Field(default=None, validation_alias='minecraft:potion_duration_scale', serialization_alias='minecraft:potion_duration_scale')
    profile: Profile | None = Field(default=None, validation_alias='minecraft:profile', serialization_alias='minecraft:profile')
    provides_banner_patterns: Annotated[str, IdSpec(registry='banner_pattern', tags='allowed')] | list[Annotated[str, IdSpec(registry='banner_pattern')]] | None = Field(default=None, validation_alias='minecraft:provides_banner_patterns', serialization_alias='minecraft:provides_banner_patterns')
    provides_pottery_pattern: Annotated[str, IdSpec(registry='decorated_pot_pattern')] | None = Field(default=None, validation_alias='minecraft:provides_pottery_pattern', serialization_alias='minecraft:provides_pottery_pattern')
    provides_trim_material: Annotated[str, IdSpec(registry='trim_material')] | None = Field(default=None, validation_alias='minecraft:provides_trim_material', serialization_alias='minecraft:provides_trim_material')
    rabbit_variant: RabbitVariant | None = Field(default=None, validation_alias='minecraft:rabbit/variant', serialization_alias='minecraft:rabbit/variant')
    rarity: Rarity | None = Field(default=None, validation_alias='minecraft:rarity', serialization_alias='minecraft:rarity')
    recipes: list[Annotated[str, IdSpec(registry='recipe')]] | None = Field(default=None, validation_alias='minecraft:recipes', serialization_alias='minecraft:recipes')
    repair_cost: Annotated[int, Field(ge=0)] | None = Field(default=None, validation_alias='minecraft:repair_cost', serialization_alias='minecraft:repair_cost')
    repairable: Repairable | None = Field(default=None, validation_alias='minecraft:repairable', serialization_alias='minecraft:repairable')
    salmon_size: SalmonType | None = Field(default=None, validation_alias='minecraft:salmon/size', serialization_alias='minecraft:salmon/size')
    sheep_color: DyeColor | None = Field(default=None, validation_alias='minecraft:sheep/color', serialization_alias='minecraft:sheep/color')
    shulker_color: DyeColor | None = Field(default=None, validation_alias='minecraft:shulker/color', serialization_alias='minecraft:shulker/color')
    sign_text_back: SignText | None = Field(default=None, validation_alias='minecraft:sign_text_back', serialization_alias='minecraft:sign_text_back')
    sign_text_front: SignText | None = Field(default=None, validation_alias='minecraft:sign_text_front', serialization_alias='minecraft:sign_text_front')
    stored_enchantments: EnchantmentLevels | None = Field(default=None, validation_alias='minecraft:stored_enchantments', serialization_alias='minecraft:stored_enchantments')
    sulfur_cube_content: ItemStackTemplate | None = Field(default=None, validation_alias='minecraft:sulfur_cube_content', serialization_alias='minecraft:sulfur_cube_content')
    suspicious_stew_effects: list[SuspiciousStewEffect] | None = Field(default=None, validation_alias='minecraft:suspicious_stew_effects', serialization_alias='minecraft:suspicious_stew_effects')
    tool: Tool | None = Field(default=None, validation_alias='minecraft:tool', serialization_alias='minecraft:tool')
    tooltip_display: TooltipDisplay | None = Field(default=None, validation_alias='minecraft:tooltip_display', serialization_alias='minecraft:tooltip_display')
    tooltip_style: Annotated[str, IdSpec()] | None = Field(default=None, validation_alias='minecraft:tooltip_style', serialization_alias='minecraft:tooltip_style')
    trim: Trim | None = Field(default=None, validation_alias='minecraft:trim', serialization_alias='minecraft:trim')
    tropical_fish_base_color: DyeColor | None = Field(default=None, validation_alias='minecraft:tropical_fish/base_color', serialization_alias='minecraft:tropical_fish/base_color')
    tropical_fish_pattern: TropicalFishPattern | None = Field(default=None, validation_alias='minecraft:tropical_fish/pattern', serialization_alias='minecraft:tropical_fish/pattern')
    tropical_fish_pattern_color: DyeColor | None = Field(default=None, validation_alias='minecraft:tropical_fish/pattern_color', serialization_alias='minecraft:tropical_fish/pattern_color')
    unbreakable: Unbreakable | None = Field(default=None, validation_alias='minecraft:unbreakable', serialization_alias='minecraft:unbreakable')
    use_cooldown: UseCooldown | None = Field(default=None, validation_alias='minecraft:use_cooldown', serialization_alias='minecraft:use_cooldown')
    use_effects: UseEffects | None = Field(default=None, validation_alias='minecraft:use_effects', serialization_alias='minecraft:use_effects')
    use_remainder: ItemStackTemplate | None = Field(default=None, validation_alias='minecraft:use_remainder', serialization_alias='minecraft:use_remainder')
    villager_food: VillagerFood | None = Field(default=None, validation_alias='minecraft:villager_food', serialization_alias='minecraft:villager_food')
    villager_variant: Annotated[str, IdSpec(registry='villager_type')] | None = Field(default=None, validation_alias='minecraft:villager/variant', serialization_alias='minecraft:villager/variant')
    waxed: WaxedStruct | None = Field(default=None, validation_alias='minecraft:waxed', serialization_alias='minecraft:waxed')
    weapon: Weapon | None = Field(default=None, validation_alias='minecraft:weapon', serialization_alias='minecraft:weapon')
    wolf_collar: DyeColor | None = Field(default=None, validation_alias='minecraft:wolf/collar', serialization_alias='minecraft:wolf/collar')
    wolf_sound_variant: Annotated[str, IdSpec(registry='wolf_sound_variant')] | None = Field(default=None, validation_alias='minecraft:wolf/sound_variant', serialization_alias='minecraft:wolf/sound_variant')
    wolf_variant: Annotated[str, IdSpec(registry='wolf_variant')] | None = Field(default=None, validation_alias='minecraft:wolf/variant', serialization_alias='minecraft:wolf/variant')
    writable_book_content: WritableBookContent | None = Field(default=None, validation_alias='minecraft:writable_book_content', serialization_alias='minecraft:writable_book_content')
    written_book_content: WrittenBookContent | None = Field(default=None, validation_alias='minecraft:written_book_content', serialization_alias='minecraft:written_book_content')
    zombie_nautilus_variant: Annotated[str, IdSpec(registry='zombie_nautilus_variant')] | None = Field(default=None, validation_alias='minecraft:zombie_nautilus/variant', serialization_alias='minecraft:zombie_nautilus/variant')
    __pydantic_extra__: dict[Annotated[str, IdSpec(registry='data_component_type', prefix='!', exclude=('additional_trade_cost', 'creative_slot_lock', 'map_post_processing'))], DataComponentPatchValueStruct] = Field(init=False)
