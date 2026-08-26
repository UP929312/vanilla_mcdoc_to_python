"""
Generated from symbols.json for ::java::world::component::item::ConsumeEffect
Local link to file: generated_symbols/world/component/item/ConsumeEffect.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Literal

from generated_symbols.world.component.item.ApplyEffectsConsumeEffect import ApplyEffectsConsumeEffect
from generated_symbols.world.component.item.PlaySoundConsumeEffect import PlaySoundConsumeEffect
from generated_symbols.world.component.item.RemoveEffectsConsumeEffect import RemoveEffectsConsumeEffect
from generated_symbols.world.component.item.TeleportRandomlyConsumeEffect import TeleportRandomlyConsumeEffect


@dataclass(kw_only=True)
class ConsumeEffectApplyEffects(ApplyEffectsConsumeEffect):
    type: Literal['minecraft:apply_effects'] = 'minecraft:apply_effects'


@dataclass(kw_only=True)
class ConsumeEffectClearAllEffects:
    type: Literal['minecraft:clear_all_effects'] = 'minecraft:clear_all_effects'


@dataclass(kw_only=True)
class ConsumeEffectPlaySound(PlaySoundConsumeEffect):
    type: Literal['minecraft:play_sound'] = 'minecraft:play_sound'


@dataclass(kw_only=True)
class ConsumeEffectRemoveEffects(RemoveEffectsConsumeEffect):
    type: Literal['minecraft:remove_effects'] = 'minecraft:remove_effects'


@dataclass(kw_only=True)
class ConsumeEffectTeleportRandomly(TeleportRandomlyConsumeEffect):
    type: Literal['minecraft:teleport_randomly'] = 'minecraft:teleport_randomly'


type ConsumeEffect = ConsumeEffectApplyEffects | ConsumeEffectClearAllEffects | ConsumeEffectPlaySound | ConsumeEffectRemoveEffects | ConsumeEffectTeleportRandomly


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::ConsumeEffect": {
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
                                    "value": "consume_effect_type"
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
                    "registry": "minecraft:consume_effect"
                }
            }
        ]
    }
}

