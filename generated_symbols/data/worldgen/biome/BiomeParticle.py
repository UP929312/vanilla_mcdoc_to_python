"""
Generated from symbols.json for ::java::data::worldgen::biome::BiomeParticle
Local link to file: generated_symbols/data/worldgen/biome/BiomeParticle.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from generated_symbols.base import GeneratedModel
from pydantic import Field

if TYPE_CHECKING:
    from generated_symbols.util.particle.Particle import Particle


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

