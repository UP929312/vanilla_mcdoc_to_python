"""
Generated from symbols.json for ::java::data::enchantment::effect::ExplosionParticleInfo
Local link to file: generated_symbols/data/enchantment/effect/ExplosionParticleInfo.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from generated_symbols.base import GeneratedModel
from pydantic import Field

if TYPE_CHECKING:
    from generated_symbols.util.particle.Particle import Particle


class ExplosionParticleInfo(GeneratedModel):
    weight: Annotated[int, Field(ge=1)]
    particle: Particle
    scaling: float | None = None  # Defaults to 1.0. Scaling of the distance between the center of the explosion and the block
    speed: float | None = None  # Defaults to 1.0. Scaling of the speed of the particle


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect::ExplosionParticleInfo": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "weight",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                }
            },
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
                "desc": "Defaults to 1.0. Scaling of the distance between the center of the explosion and the block",
                "key": "scaling",
                "type": {
                    "kind": "float"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Defaults to 1.0. Scaling of the speed of the particle",
                "key": "speed",
                "type": {
                    "kind": "float"
                },
                "optional": True
            }
        ]
    }
}

