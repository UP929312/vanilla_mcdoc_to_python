"""
Generated from symbols.json for ::java::data::enchantment::effect::EntityEffect
Local link to file: generated_symbols/data/enchantment/effect/EntityEffect.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Literal

from generated_symbols.data.enchantment.effect.AllOfEntityEffect import AllOfEntityEffect
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
class EntityEffectAllOf(AllOfEntityEffect):
    type: Literal['minecraft:all_of']


@dataclass(kw_only=True)
class EntityEffectApplyExhaustion(ApplyExhaustionEntityEffect):
    type: Literal['minecraft:apply_exhaustion']


@dataclass(kw_only=True)
class EntityEffectApplyImpulse(ApplyImpulseEntityEffect):
    type: Literal['minecraft:apply_impulse']


@dataclass(kw_only=True)
class EntityEffectApplyMobEffect(ApplyMobEffectEntityEffect):
    type: Literal['minecraft:apply_mob_effect']


@dataclass(kw_only=True)
class EntityEffectChangeItemDamage(ChangeItemDamageEffect):
    type: Literal['minecraft:change_item_damage']


@dataclass(kw_only=True)
class EntityEffectDamageEntity(DamageEntityEffect):
    type: Literal['minecraft:damage_entity']


@dataclass(kw_only=True)
class EntityEffectExplode(ExplodeEntityEffect):
    type: Literal['minecraft:explode']


@dataclass(kw_only=True)
class EntityEffectIgnite(IgniteEntityEffect):
    type: Literal['minecraft:ignite']


@dataclass(kw_only=True)
class EntityEffectPlaySound(PlaySoundEntityEffect):
    type: Literal['minecraft:play_sound']


@dataclass(kw_only=True)
class EntityEffectReplaceBlock(ReplaceBlockEntityEffect):
    type: Literal['minecraft:replace_block']


@dataclass(kw_only=True)
class EntityEffectReplaceDisk(ReplaceDiskEntityEffect):
    type: Literal['minecraft:replace_disk']


@dataclass(kw_only=True)
class EntityEffectRunFunction(RunFunctionEntityEffect):
    type: Literal['minecraft:run_function']


@dataclass(kw_only=True)
class EntityEffectSetBlockProperties(SetBlockPropertiesEntityEffect):
    type: Literal['minecraft:set_block_properties']


@dataclass(kw_only=True)
class EntityEffectSpawnParticles(SpawnParticlesEntityEffect):
    type: Literal['minecraft:spawn_particles']


@dataclass(kw_only=True)
class EntityEffectSummonEntity(SummonEntityEffect):
    type: Literal['minecraft:summon_entity']


type EntityEffect = EntityEffectAllOf | EntityEffectApplyExhaustion | EntityEffectApplyImpulse | EntityEffectApplyMobEffect | EntityEffectChangeItemDamage | EntityEffectDamageEntity | EntityEffectExplode | EntityEffectIgnite | EntityEffectPlaySound | EntityEffectReplaceBlock | EntityEffectReplaceDisk | EntityEffectRunFunction | EntityEffectSetBlockProperties | EntityEffectSpawnParticles | EntityEffectSummonEntity


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect::EntityEffect": {
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
                                    "value": "enchantment_entity_effect_type"
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
                    "registry": "minecraft:entity_effect"
                }
            }
        ]
    }
}

