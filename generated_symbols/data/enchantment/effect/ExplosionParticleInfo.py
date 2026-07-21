# Generated from symbols.json for ::java::data::enchantment::effect::ExplosionParticleInfo
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.util.particle.Particle import Particle


@dataclass(kw_only=True)
class ExplosionParticleInfo:
    weight: Annotated[int, 'Range | Min `1` and above | inclusive']
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

