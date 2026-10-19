"""
Generated from symbols.json for ::java::data::enchantment::effect::LocationBasedEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect/LocationBasedEffect.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Discriminator, Tag

from vanilla_mcdoc.base import GeneratedModel, tag_of
from vanilla_mcdoc.data.enchantment.effect.AllOfLocationBasedEffect import AllOfLocationBasedEffect
from vanilla_mcdoc.data.enchantment.effect.ApplyExhaustionEntityEffect import ApplyExhaustionEntityEffect
from vanilla_mcdoc.data.enchantment.effect.ApplyImpulseEntityEffect import ApplyImpulseEntityEffect
from vanilla_mcdoc.data.enchantment.effect.ApplyMobEffectEntityEffect import ApplyMobEffectEntityEffect
from vanilla_mcdoc.data.enchantment.effect.ChangeItemDamageEffect import ChangeItemDamageEffect
from vanilla_mcdoc.data.enchantment.effect.DamageEntityEffect import DamageEntityEffect
from vanilla_mcdoc.data.enchantment.effect.ExplodeEntityEffect import ExplodeEntityEffect
from vanilla_mcdoc.data.enchantment.effect.IgniteEntityEffect import IgniteEntityEffect
from vanilla_mcdoc.data.enchantment.effect.PlaySoundEntityEffect import PlaySoundEntityEffect
from vanilla_mcdoc.data.enchantment.effect.ReplaceBlockEntityEffect import ReplaceBlockEntityEffect
from vanilla_mcdoc.data.enchantment.effect.ReplaceDiskEntityEffect import ReplaceDiskEntityEffect
from vanilla_mcdoc.data.enchantment.effect.RunFunctionEntityEffect import RunFunctionEntityEffect
from vanilla_mcdoc.data.enchantment.effect.SetBlockPropertiesEntityEffect import SetBlockPropertiesEntityEffect
from vanilla_mcdoc.data.enchantment.effect.SpawnParticlesEntityEffect import SpawnParticlesEntityEffect
from vanilla_mcdoc.data.enchantment.effect.SummonEntityEffect import SummonEntityEffect


class LocationBasedEffectAllOf(AllOfLocationBasedEffect):
    type: Literal['minecraft:all_of', 'all_of'] = 'minecraft:all_of'


class LocationBasedEffectApplyExhaustion(ApplyExhaustionEntityEffect):
    type: Literal['minecraft:apply_exhaustion', 'apply_exhaustion'] = 'minecraft:apply_exhaustion'


class LocationBasedEffectApplyImpulse(ApplyImpulseEntityEffect):
    type: Literal['minecraft:apply_impulse', 'apply_impulse'] = 'minecraft:apply_impulse'


class LocationBasedEffectApplyMobEffect(ApplyMobEffectEntityEffect):
    type: Literal['minecraft:apply_mob_effect', 'apply_mob_effect'] = 'minecraft:apply_mob_effect'


class LocationBasedEffectChangeItemDamage(ChangeItemDamageEffect):
    type: Literal['minecraft:change_item_damage', 'change_item_damage'] = 'minecraft:change_item_damage'


class LocationBasedEffectDamageEntity(DamageEntityEffect):
    type: Literal['minecraft:damage_entity', 'damage_entity'] = 'minecraft:damage_entity'


class LocationBasedEffectExplode(ExplodeEntityEffect):
    type: Literal['minecraft:explode', 'explode'] = 'minecraft:explode'


class LocationBasedEffectIgnite(IgniteEntityEffect):
    type: Literal['minecraft:ignite', 'ignite'] = 'minecraft:ignite'


class LocationBasedEffectPlaySound(PlaySoundEntityEffect):
    type: Literal['minecraft:play_sound', 'play_sound'] = 'minecraft:play_sound'


class LocationBasedEffectReplaceBlock(ReplaceBlockEntityEffect):
    type: Literal['minecraft:replace_block', 'replace_block'] = 'minecraft:replace_block'


class LocationBasedEffectReplaceDisk(ReplaceDiskEntityEffect):
    type: Literal['minecraft:replace_disk', 'replace_disk'] = 'minecraft:replace_disk'


class LocationBasedEffectRunFunction(RunFunctionEntityEffect):
    type: Literal['minecraft:run_function', 'run_function'] = 'minecraft:run_function'


class LocationBasedEffectSetBlockProperties(SetBlockPropertiesEntityEffect):
    type: Literal['minecraft:set_block_properties', 'set_block_properties'] = 'minecraft:set_block_properties'


class LocationBasedEffectSpawnParticles(SpawnParticlesEntityEffect):
    type: Literal['minecraft:spawn_particles', 'spawn_particles'] = 'minecraft:spawn_particles'


class LocationBasedEffectSummonEntity(SummonEntityEffect):
    type: Literal['minecraft:summon_entity', 'summon_entity'] = 'minecraft:summon_entity'


class LocationBasedEffectAttribute(GeneratedModel):
    type: Literal['minecraft:attribute', 'attribute'] = 'minecraft:attribute'


type LocationBasedEffect = Annotated[
    Annotated[LocationBasedEffectAllOf, Tag('minecraft:all_of')]
    | Annotated[LocationBasedEffectApplyExhaustion, Tag('minecraft:apply_exhaustion')]
    | Annotated[LocationBasedEffectApplyImpulse, Tag('minecraft:apply_impulse')]
    | Annotated[LocationBasedEffectApplyMobEffect, Tag('minecraft:apply_mob_effect')]
    | Annotated[LocationBasedEffectChangeItemDamage, Tag('minecraft:change_item_damage')]
    | Annotated[LocationBasedEffectDamageEntity, Tag('minecraft:damage_entity')]
    | Annotated[LocationBasedEffectExplode, Tag('minecraft:explode')]
    | Annotated[LocationBasedEffectIgnite, Tag('minecraft:ignite')]
    | Annotated[LocationBasedEffectPlaySound, Tag('minecraft:play_sound')]
    | Annotated[LocationBasedEffectReplaceBlock, Tag('minecraft:replace_block')]
    | Annotated[LocationBasedEffectReplaceDisk, Tag('minecraft:replace_disk')]
    | Annotated[LocationBasedEffectRunFunction, Tag('minecraft:run_function')]
    | Annotated[LocationBasedEffectSetBlockProperties, Tag('minecraft:set_block_properties')]
    | Annotated[LocationBasedEffectSpawnParticles, Tag('minecraft:spawn_particles')]
    | Annotated[LocationBasedEffectSummonEntity, Tag('minecraft:summon_entity')]
    | Annotated[LocationBasedEffectAttribute, Tag('minecraft:attribute')],
    Discriminator(tag_of('type')),
]
