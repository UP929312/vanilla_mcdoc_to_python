# Generated from symbols.json for ::java::data::worldgen::biome::BiomeParticle
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.util.particle.Particle import Particle


@dataclass(kw_only=True)
class BiomeParticle:
    options: Particle
    probability: Annotated[float, 'Range | `0`-`1` | both inclusive']


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

