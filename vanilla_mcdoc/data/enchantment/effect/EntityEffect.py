"""
Generated from symbols.json for ::java::data::enchantment::effect::EntityEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect/EntityEffect.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Discriminator, Tag

from vanilla_mcdoc.base import tag_of
from vanilla_mcdoc.data.enchantment.effect.AllOfEntityEffect import AllOfEntityEffect
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


class EntityEffectAllOf(AllOfEntityEffect):
    type: Literal['minecraft:all_of', 'all_of'] = 'minecraft:all_of'


class EntityEffectApplyExhaustion(ApplyExhaustionEntityEffect):
    type: Literal['minecraft:apply_exhaustion', 'apply_exhaustion'] = 'minecraft:apply_exhaustion'


class EntityEffectApplyImpulse(ApplyImpulseEntityEffect):
    type: Literal['minecraft:apply_impulse', 'apply_impulse'] = 'minecraft:apply_impulse'


class EntityEffectApplyMobEffect(ApplyMobEffectEntityEffect):
    type: Literal['minecraft:apply_mob_effect', 'apply_mob_effect'] = 'minecraft:apply_mob_effect'


class EntityEffectChangeItemDamage(ChangeItemDamageEffect):
    type: Literal['minecraft:change_item_damage', 'change_item_damage'] = 'minecraft:change_item_damage'


class EntityEffectDamageEntity(DamageEntityEffect):
    type: Literal['minecraft:damage_entity', 'damage_entity'] = 'minecraft:damage_entity'


class EntityEffectExplode(ExplodeEntityEffect):
    type: Literal['minecraft:explode', 'explode'] = 'minecraft:explode'


class EntityEffectIgnite(IgniteEntityEffect):
    type: Literal['minecraft:ignite', 'ignite'] = 'minecraft:ignite'


class EntityEffectPlaySound(PlaySoundEntityEffect):
    type: Literal['minecraft:play_sound', 'play_sound'] = 'minecraft:play_sound'


class EntityEffectReplaceBlock(ReplaceBlockEntityEffect):
    type: Literal['minecraft:replace_block', 'replace_block'] = 'minecraft:replace_block'


class EntityEffectReplaceDisk(ReplaceDiskEntityEffect):
    type: Literal['minecraft:replace_disk', 'replace_disk'] = 'minecraft:replace_disk'


class EntityEffectRunFunction(RunFunctionEntityEffect):
    type: Literal['minecraft:run_function', 'run_function'] = 'minecraft:run_function'


class EntityEffectSetBlockProperties(SetBlockPropertiesEntityEffect):
    type: Literal['minecraft:set_block_properties', 'set_block_properties'] = 'minecraft:set_block_properties'


class EntityEffectSpawnParticles(SpawnParticlesEntityEffect):
    type: Literal['minecraft:spawn_particles', 'spawn_particles'] = 'minecraft:spawn_particles'


class EntityEffectSummonEntity(SummonEntityEffect):
    type: Literal['minecraft:summon_entity', 'summon_entity'] = 'minecraft:summon_entity'


type EntityEffect = Annotated[
    Annotated[EntityEffectAllOf, Tag('minecraft:all_of')]
    | Annotated[EntityEffectApplyExhaustion, Tag('minecraft:apply_exhaustion')]
    | Annotated[EntityEffectApplyImpulse, Tag('minecraft:apply_impulse')]
    | Annotated[EntityEffectApplyMobEffect, Tag('minecraft:apply_mob_effect')]
    | Annotated[EntityEffectChangeItemDamage, Tag('minecraft:change_item_damage')]
    | Annotated[EntityEffectDamageEntity, Tag('minecraft:damage_entity')]
    | Annotated[EntityEffectExplode, Tag('minecraft:explode')]
    | Annotated[EntityEffectIgnite, Tag('minecraft:ignite')]
    | Annotated[EntityEffectPlaySound, Tag('minecraft:play_sound')]
    | Annotated[EntityEffectReplaceBlock, Tag('minecraft:replace_block')]
    | Annotated[EntityEffectReplaceDisk, Tag('minecraft:replace_disk')]
    | Annotated[EntityEffectRunFunction, Tag('minecraft:run_function')]
    | Annotated[EntityEffectSetBlockProperties, Tag('minecraft:set_block_properties')]
    | Annotated[EntityEffectSpawnParticles, Tag('minecraft:spawn_particles')]
    | Annotated[EntityEffectSummonEntity, Tag('minecraft:summon_entity')],
    Discriminator(tag_of('type')),
]
