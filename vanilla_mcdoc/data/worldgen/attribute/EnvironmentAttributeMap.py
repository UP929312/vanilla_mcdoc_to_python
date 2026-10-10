"""
Generated from symbols.json for ::java::data::worldgen::attribute::EnvironmentAttributeMap
Local link to file: vanilla_mcdoc/data/worldgen/attribute/EnvironmentAttributeMap.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Any, TypeVar

from pydantic import Field

from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.MoonPhase import MoonPhase
    from vanilla_mcdoc.data.worldgen.attribute.AmbientParticle import AmbientParticle
    from vanilla_mcdoc.data.worldgen.attribute.AmbientSounds import AmbientSounds
    from vanilla_mcdoc.data.worldgen.attribute.BackgroundMusic import BackgroundMusic
    from vanilla_mcdoc.data.worldgen.attribute.BedRule import BedRule
    from vanilla_mcdoc.data.worldgen.attribute.TriState import TriState
    from vanilla_mcdoc.data.worldgen.attribute.modifier.BooleanAttributeModifier import BooleanAttributeModifier
    from vanilla_mcdoc.data.worldgen.attribute.modifier.ColorAttributeModifier import ColorAttributeModifier
    from vanilla_mcdoc.data.worldgen.attribute.modifier.FloatAttributeModifier import FloatAttributeModifier
    from vanilla_mcdoc.data.worldgen.attribute.modifier.ListModifier import ListModifier
    from vanilla_mcdoc.data.worldgen.attribute.modifier.MergeableModifier import MergeableModifier
    from vanilla_mcdoc.data.worldgen.attribute.modifier.OverrideModifier import OverrideModifier
    from vanilla_mcdoc.data.worldgen.attribute.modifier.TranslucentColorAttributeModifier import TranslucentColorAttributeModifier
    from vanilla_mcdoc.data.worldgen.biome.NaturalMobSpawns import NaturalMobSpawns
    from vanilla_mcdoc.util.color.StringARGB import StringARGB
    from vanilla_mcdoc.util.color.StringRGB import StringRGB
    from vanilla_mcdoc.util.particle.Particle import Particle


K = TypeVar('K')


type EnvironmentAttributeMap[K] = dict[K, Any | AmbientSounds | BackgroundMusic | bool | Annotated[float, Field(ge=0, le=1)] | Annotated[str, IdSpec(registry='activity')] | BedRule | Annotated[float, Field(ge=0, le=0.9999999)] | TriState | NaturalMobSpawns | Annotated[float, Field(ge=0, le=15)] | StringRGB | list[AmbientParticle] | StringARGB | Annotated[float, Field(ge=0)] | float | Particle | MoonPhase | OverrideModifier[Any] | OverrideModifier[AmbientSounds] | OverrideModifier[BackgroundMusic] | BooleanAttributeModifier | FloatAttributeModifier[Annotated[float, Field(ge=0, le=1)]] | Annotated[float, Field(ge=0, le=1)] | OverrideModifier[Annotated[str, IdSpec(registry='activity')]] | OverrideModifier[BedRule] | FloatAttributeModifier[Annotated[float, Field(ge=0, le=0.9999999)]] | Annotated[float, Field(ge=0, le=0.9999999)] | OverrideModifier[TriState] | MergeableModifier[NaturalMobSpawns] | FloatAttributeModifier[Annotated[float, Field(ge=0, le=15)]] | Annotated[float, Field(ge=0, le=15)] | ColorAttributeModifier | ListModifier[AmbientParticle] | TranslucentColorAttributeModifier | FloatAttributeModifier[Annotated[float, Field(ge=0)]] | Annotated[float, Field(ge=0)] | FloatAttributeModifier[float] | float | OverrideModifier[Particle] | OverrideModifier[MoonPhase]]


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
