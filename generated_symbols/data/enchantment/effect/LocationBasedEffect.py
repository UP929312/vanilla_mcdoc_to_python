"""
Generated from symbols.json for ::java::data::enchantment::effect::LocationBasedEffect
Local link to file: generated_symbols/data/enchantment/effect/LocationBasedEffect.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from generated_symbols.data.enchantment.effect.AllOfLocationBasedEffect import AllOfLocationBasedEffect
from generated_symbols.data.enchantment.effect.ApplyExhaustionEntityEffect import ApplyExhaustionEntityEffect
from generated_symbols.data.enchantment.effect.ApplyImpulseEntityEffect import ApplyImpulseEntityEffect
from generated_symbols.data.enchantment.effect.ApplyMobEffectEntityEffect import ApplyMobEffectEntityEffect
from generated_symbols.data.enchantment.effect.ChangeItemDamageEffect import ChangeItemDamageEffect
from generated_symbols.data.enchantment.effect.DamageEntityEffect import DamageEntityEffect
from generated_symbols.data.enchantment.effect.ExplodeEntityEffect import ExplodeEntityEffect
from generated_symbols.data.enchantment.effect.IgniteEntityEffect import IgniteEntityEffect
from generated_symbols.data.enchantment.effect.PlaySoundEntityEffect import PlaySoundEntityEffect
from generated_symbols.data.enchantment.effect.ReplaceBlockEntityEffect import ReplaceBlockEntityEffect
from generated_symbols.data.enchantment.effect.ReplaceDiskEntityEffect import ReplaceDiskEntityEffect
from generated_symbols.data.enchantment.effect.RunFunctionEntityEffect import RunFunctionEntityEffect
from generated_symbols.data.enchantment.effect.SetBlockPropertiesEntityEffect import SetBlockPropertiesEntityEffect
from generated_symbols.data.enchantment.effect.SpawnParticlesEntityEffect import SpawnParticlesEntityEffect
from generated_symbols.data.enchantment.effect.SummonEntityEffect import SummonEntityEffect


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


type LocationBasedEffect = Annotated[
    LocationBasedEffectAllOf | LocationBasedEffectApplyExhaustion | LocationBasedEffectApplyImpulse | LocationBasedEffectApplyMobEffect | LocationBasedEffectChangeItemDamage | LocationBasedEffectDamageEntity | LocationBasedEffectExplode | LocationBasedEffectIgnite | LocationBasedEffectPlaySound | LocationBasedEffectReplaceBlock | LocationBasedEffectReplaceDisk | LocationBasedEffectRunFunction | LocationBasedEffectSetBlockProperties | LocationBasedEffectSpawnParticles | LocationBasedEffectSummonEntity,
    Field(discriminator='type'),
]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect::LocationBasedEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "enchantment_location_based_effect_type"
                                }
                            }
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
                    "registry": "minecraft:location_based_effect"
                }
            }
        ]
    }
}

