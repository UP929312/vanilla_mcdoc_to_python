# Generated from symbols.json for ::java::data::worldgen::attribute::AmbientParticle
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.util.particle.Particle import Particle


@dataclass(kw_only=True)
class AmbientParticle:
    particle: Particle
    probability: Annotated[float, 'Range | `0`-`1` | both inclusive']


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

