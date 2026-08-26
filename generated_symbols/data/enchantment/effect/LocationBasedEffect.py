"""
Generated from symbols.json for ::java::data::enchantment::effect::LocationBasedEffect
Local link to file: generated_symbols/data/enchantment/effect/LocationBasedEffect.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Literal

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


@dataclass(kw_only=True)
class LocationBasedEffectAllOf(AllOfLocationBasedEffect):
    type: Literal['minecraft:all_of']


@dataclass(kw_only=True)
class LocationBasedEffectApplyExhaustion(ApplyExhaustionEntityEffect):
    type: Literal['minecraft:apply_exhaustion']


@dataclass(kw_only=True)
class LocationBasedEffectApplyImpulse(ApplyImpulseEntityEffect):
    type: Literal['minecraft:apply_impulse']


@dataclass(kw_only=True)
class LocationBasedEffectApplyMobEffect(ApplyMobEffectEntityEffect):
    type: Literal['minecraft:apply_mob_effect']


@dataclass(kw_only=True)
class LocationBasedEffectChangeItemDamage(ChangeItemDamageEffect):
    type: Literal['minecraft:change_item_damage']


@dataclass(kw_only=True)
class LocationBasedEffectDamageEntity(DamageEntityEffect):
    type: Literal['minecraft:damage_entity']


@dataclass(kw_only=True)
class LocationBasedEffectExplode(ExplodeEntityEffect):
    type: Literal['minecraft:explode']


@dataclass(kw_only=True)
class LocationBasedEffectIgnite(IgniteEntityEffect):
    type: Literal['minecraft:ignite']


@dataclass(kw_only=True)
class LocationBasedEffectPlaySound(PlaySoundEntityEffect):
    type: Literal['minecraft:play_sound']


@dataclass(kw_only=True)
class LocationBasedEffectReplaceBlock(ReplaceBlockEntityEffect):
    type: Literal['minecraft:replace_block']


@dataclass(kw_only=True)
class LocationBasedEffectReplaceDisk(ReplaceDiskEntityEffect):
    type: Literal['minecraft:replace_disk']


@dataclass(kw_only=True)
class LocationBasedEffectRunFunction(RunFunctionEntityEffect):
    type: Literal['minecraft:run_function']


@dataclass(kw_only=True)
class LocationBasedEffectSetBlockProperties(SetBlockPropertiesEntityEffect):
    type: Literal['minecraft:set_block_properties']


@dataclass(kw_only=True)
class LocationBasedEffectSpawnParticles(SpawnParticlesEntityEffect):
    type: Literal['minecraft:spawn_particles']


@dataclass(kw_only=True)
class LocationBasedEffectSummonEntity(SummonEntityEffect):
    type: Literal['minecraft:summon_entity']


type LocationBasedEffect = LocationBasedEffectAllOf | LocationBasedEffectApplyExhaustion | LocationBasedEffectApplyImpulse | LocationBasedEffectApplyMobEffect | LocationBasedEffectChangeItemDamage | LocationBasedEffectDamageEntity | LocationBasedEffectExplode | LocationBasedEffectIgnite | LocationBasedEffectPlaySound | LocationBasedEffectReplaceBlock | LocationBasedEffectReplaceDisk | LocationBasedEffectRunFunction | LocationBasedEffectSetBlockProperties | LocationBasedEffectSpawnParticles | LocationBasedEffectSummonEntity


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

