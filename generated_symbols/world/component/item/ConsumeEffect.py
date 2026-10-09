"""
Generated from symbols.json for ::java::world::component::item::ConsumeEffect
Local link to file: generated_symbols/world/component/item/ConsumeEffect.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from generated_symbols.base import GeneratedModel
from generated_symbols.world.component.item.ApplyEffectsConsumeEffect import ApplyEffectsConsumeEffect
from generated_symbols.world.component.item.PlaySoundConsumeEffect import PlaySoundConsumeEffect
from generated_symbols.world.component.item.RemoveEffectsConsumeEffect import RemoveEffectsConsumeEffect
from generated_symbols.world.component.item.TeleportRandomlyConsumeEffect import TeleportRandomlyConsumeEffect
from pydantic import Field


class ConsumeEffectApplyEffects(ApplyEffectsConsumeEffect):
    type: Literal['minecraft:apply_effects', 'apply_effects'] = 'minecraft:apply_effects'


class ConsumeEffectClearAllEffects(GeneratedModel):
    type: Literal['minecraft:clear_all_effects', 'clear_all_effects'] = 'minecraft:clear_all_effects'


class ConsumeEffectPlaySound(PlaySoundConsumeEffect):
    type: Literal['minecraft:play_sound', 'play_sound'] = 'minecraft:play_sound'


class ConsumeEffectRemoveEffects(RemoveEffectsConsumeEffect):
    type: Literal['minecraft:remove_effects', 'remove_effects'] = 'minecraft:remove_effects'


class ConsumeEffectTeleportRandomly(TeleportRandomlyConsumeEffect):
    type: Literal['minecraft:teleport_randomly', 'teleport_randomly'] = 'minecraft:teleport_randomly'


type ConsumeEffect = Annotated[
    ConsumeEffectApplyEffects | ConsumeEffectClearAllEffects | ConsumeEffectPlaySound | ConsumeEffectRemoveEffects | ConsumeEffectTeleportRandomly,
    Field(discriminator='type'),
]


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

