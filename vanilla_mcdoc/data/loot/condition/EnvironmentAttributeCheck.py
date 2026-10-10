"""
Generated from symbols.json for ::java::data::loot::condition::EnvironmentAttributeCheck
Local link to file: vanilla_mcdoc/data/loot/condition/EnvironmentAttributeCheck.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Any

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.MoonPhase import MoonPhase
    from vanilla_mcdoc.data.worldgen.attribute.AmbientParticle import AmbientParticle
    from vanilla_mcdoc.data.worldgen.attribute.AmbientSounds import AmbientSounds
    from vanilla_mcdoc.data.worldgen.attribute.BackgroundMusic import BackgroundMusic
    from vanilla_mcdoc.data.worldgen.attribute.BedRule import BedRule
    from vanilla_mcdoc.data.worldgen.attribute.TriState import TriState
    from vanilla_mcdoc.data.worldgen.biome.NaturalMobSpawns import NaturalMobSpawns
    from vanilla_mcdoc.registry.KnownEnvironmentAttributeId import KnownEnvironmentAttributeId
    from vanilla_mcdoc.util.color.StringARGB import StringARGB
    from vanilla_mcdoc.util.color.StringRGB import StringRGB
    from vanilla_mcdoc.util.particle.Particle import Particle


class EnvironmentAttributeCheck(GeneratedModel):
    attribute: Annotated[str, IdSpec(registry='environment_attribute')] | KnownEnvironmentAttributeId
    value: Any | AmbientSounds | BackgroundMusic | bool | Annotated[float, Field(ge=0, le=1)] | Annotated[str, IdSpec(registry='activity')] | BedRule | Annotated[float, Field(ge=0, le=0.9999999)] | TriState | NaturalMobSpawns | Annotated[float, Field(ge=0, le=15)] | StringRGB | list[AmbientParticle] | StringARGB | Annotated[float, Field(ge=0)] | float | Particle | MoonPhase


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
