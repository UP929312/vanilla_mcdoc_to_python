"""
Generated from symbols.json for ::java::data::worldgen::biome::BiomeParticle
Local link to file: vanilla_mcdoc/data/worldgen/biome/BiomeParticle.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.particle.Particle import Particle


class BiomeParticle(GeneratedModel):
    options: Particle
    probability: Annotated[float, Field(ge=0, le=1)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::biome::BiomeParticle": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "options",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::particle::Particle"
                }
            },
            {
                "kind": "pair",
                "key": "probability",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                }
            }
        ]
    }
}
