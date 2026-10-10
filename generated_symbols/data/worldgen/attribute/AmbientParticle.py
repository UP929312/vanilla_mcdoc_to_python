"""
Generated from symbols.json for ::java::data::worldgen::attribute::AmbientParticle
Local link to file: generated_symbols/data/worldgen/attribute/AmbientParticle.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.util.particle.Particle import Particle


class AmbientParticle(GeneratedModel):
    particle: Particle
    probability: Annotated[float, Field(ge=0, le=1)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::attribute::AmbientParticle": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "particle",
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
