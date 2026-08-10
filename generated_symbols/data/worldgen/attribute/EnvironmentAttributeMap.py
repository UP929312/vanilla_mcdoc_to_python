"""
Generated from symbols.json for ::java::data::worldgen::attribute::EnvironmentAttributeMap
Local link to file: generated_symbols/data/worldgen/attribute/EnvironmentAttributeMap.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Any, TypeVar

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.util.MoonPhase import MoonPhase
    from generated_symbols.data.worldgen.attribute.AmbientParticle import AmbientParticle
    from generated_symbols.data.worldgen.attribute.AmbientSounds import AmbientSounds
    from generated_symbols.data.worldgen.attribute.BackgroundMusic import BackgroundMusic
    from generated_symbols.data.worldgen.attribute.BedRule import BedRule
    from generated_symbols.data.worldgen.attribute.TriState import TriState
    from generated_symbols.data.worldgen.attribute.modifier.BooleanAttributeModifier import BooleanAttributeModifier
    from generated_symbols.data.worldgen.attribute.modifier.ColorAttributeModifier import ColorAttributeModifier
    from generated_symbols.data.worldgen.attribute.modifier.FloatAttributeModifier import FloatAttributeModifier
    from generated_symbols.data.worldgen.attribute.modifier.ListModifier import ListModifier
    from generated_symbols.data.worldgen.attribute.modifier.MergeableModifier import MergeableModifier
    from generated_symbols.data.worldgen.attribute.modifier.OverrideModifier import OverrideModifier
    from generated_symbols.data.worldgen.attribute.modifier.TranslucentColorAttributeModifier import TranslucentColorAttributeModifier
    from generated_symbols.data.worldgen.biome.NaturalMobSpawns import NaturalMobSpawns
    from generated_symbols.util.color.StringARGB import StringARGB
    from generated_symbols.util.color.StringRGB import StringRGB
    from generated_symbols.util.particle.Particle import Particle


K = TypeVar('K')

type EnvironmentAttributeMap[K] = dict[K, Any | AmbientSounds | BackgroundMusic | bool | Annotated[float, 'Range | `0`-`1` | both inclusive'] | Annotated[str, IdSpec(registry='activity')] | BedRule | Annotated[float, 'Range | `0`-`0.9999999` | both inclusive'] | TriState | NaturalMobSpawns | Annotated[float, 'Range | `0`-`15` | both inclusive'] | StringRGB | list[AmbientParticle] | StringARGB | Annotated[float, 'Range | Min `0` and above | inclusive'] | float | Particle | MoonPhase | OverrideModifier[Any] | OverrideModifier[AmbientSounds] | OverrideModifier[BackgroundMusic] | BooleanAttributeModifier | FloatAttributeModifier[Annotated[float, 'Range | `0`-`1` | both inclusive']] | Annotated[float, 'Range | `0`-`1` | both inclusive'] | OverrideModifier[Annotated[str, IdSpec(registry='activity')]] | OverrideModifier[BedRule] | FloatAttributeModifier[Annotated[float, 'Range | `0`-`0.9999999` | both inclusive']] | Annotated[float, 'Range | `0`-`0.9999999` | both inclusive'] | OverrideModifier[TriState] | MergeableModifier[NaturalMobSpawns] | FloatAttributeModifier[Annotated[float, 'Range | `0`-`15` | both inclusive']] | Annotated[float, 'Range | `0`-`15` | both inclusive'] | ColorAttributeModifier | ListModifier[AmbientParticle] | TranslucentColorAttributeModifier | FloatAttributeModifier[Annotated[float, 'Range | Min `0` and above | inclusive']] | Annotated[float, 'Range | Min `0` and above | inclusive'] | FloatAttributeModifier[float] | float | OverrideModifier[Particle] | OverrideModifier[MoonPhase]]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::attribute::EnvironmentAttributeMap": {
        "kind": "template",
        "child": {
            "kind": "struct",
            "fields": [
                {
                    "kind": "pair",
                    "key": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::attribute::K"
                    },
                    "type": {
                        "kind": "union",
                        "members": [
                            {
                                "kind": "indexed",
                                "child": {
                                    "kind": "dispatcher",
                                    "parallelIndices": [
                                        {
                                            "kind": "dynamic",
                                            "accessor": [
                                                {
                                                    "keyword": "key"
                                                }
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
                            },
                            {
                                "kind": "indexed",
                                "child": {
                                    "kind": "dispatcher",
                                    "parallelIndices": [
                                        {
                                            "kind": "dynamic",
                                            "accessor": [
                                                {
                                                    "keyword": "key"
                                                }
                                            ]
                                        }
                                    ],
                                    "registry": "minecraft:environment_attribute"
                                },
                                "parallelIndices": [
                                    {
                                        "kind": "static",
                                        "value": "modifier"
                                    }
                                ]
                            }
                        ]
                    }
                }
            ]
        },
        "typeParams": [
            {
                "path": "::java::data::worldgen::attribute::K"
            }
        ]
    }
}

