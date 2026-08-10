"""
Generated from symbols.json for ::java::data::loot::condition::EnvironmentAttributeCheck
Local link to file: generated_symbols/data/loot/condition/EnvironmentAttributeCheck.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Any

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.util.MoonPhase import MoonPhase
    from generated_symbols.data.worldgen.attribute.AmbientParticle import AmbientParticle
    from generated_symbols.data.worldgen.attribute.AmbientSounds import AmbientSounds
    from generated_symbols.data.worldgen.attribute.BackgroundMusic import BackgroundMusic
    from generated_symbols.data.worldgen.attribute.BedRule import BedRule
    from generated_symbols.data.worldgen.attribute.TriState import TriState
    from generated_symbols.data.worldgen.biome.NaturalMobSpawns import NaturalMobSpawns
    from generated_symbols.util.color.StringARGB import StringARGB
    from generated_symbols.util.color.StringRGB import StringRGB
    from generated_symbols.util.particle.Particle import Particle


@dataclass(kw_only=True)
class EnvironmentAttributeCheck:
    attribute: Annotated[str, IdSpec(registry='environment_attribute')]
    value: Any | AmbientSounds | BackgroundMusic | bool | Annotated[float, 'Range | `0`-`1` | both inclusive'] | Annotated[str, IdSpec(registry='activity')] | BedRule | Annotated[float, 'Range | `0`-`0.9999999` | both inclusive'] | TriState | NaturalMobSpawns | Annotated[float, 'Range | `0`-`15` | both inclusive'] | StringRGB | list[AmbientParticle] | StringARGB | Annotated[float, 'Range | Min `0` and above | inclusive'] | float | Particle | MoonPhase


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::condition::EnvironmentAttributeCheck": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "attribute",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "environment_attribute"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "value",
                "type": {
                    "kind": "indexed",
                    "child": {
                        "kind": "dispatcher",
                        "parallelIndices": [
                            {
                                "kind": "dynamic",
                                "accessor": [
                                    "attribute"
                                ]
                            }
                        ],
                        "registry": "minecraft:environment_attribute"
                    },
                    "parallelIndices": [
                        {
                            "kind": "static",
                            "value": "value"
                        }
                    ]
                }
            }
        ]
    }
}

