"""
Generated from symbols.json for ::java::world::component::item::ConsumeEffect
Local link to file: generated_symbols/world/component/item/ConsumeEffect.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.util.SoundEventRef import SoundEventRef
    from generated_symbols.util.effect.MobEffectInstance import MobEffectInstance


@dataclass(kw_only=True)
class ConsumeEffectApplyEffects:
    type: Literal['minecraft:apply_effects']
    effects: list[MobEffectInstance]
    probability: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None  # Chance the effects will be applied once consumed.


@dataclass(kw_only=True)
class ConsumeEffectClearAllEffects:
    type: Literal['minecraft:clear_all_effects']


@dataclass(kw_only=True)
class ConsumeEffectPlaySound:
    type: Literal['minecraft:play_sound']
    sound: SoundEventRef


@dataclass(kw_only=True)
class ConsumeEffectRemoveEffects:
    type: Literal['minecraft:remove_effects']
    effects: Annotated[str, IdSpec(registry='mob_effect', tags='allowed')] | list[Annotated[str, IdSpec(registry='mob_effect')]]


@dataclass(kw_only=True)
class ConsumeEffectTeleportRandomly:
    type: Literal['minecraft:teleport_randomly']
    diameter: Annotated[float, 'Range | Min `1` and above | inclusive'] | None = None  # Defaults to 16.
    directional_particles: bool | None = None  # Whether to show a particle trail into the direction of teleportation.  Defaults to `true`.


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

