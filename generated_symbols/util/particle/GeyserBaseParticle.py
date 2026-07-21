# Generated from symbols.json for ::java::util::particle::GeyserBaseParticle
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class GeyserBaseParticle:
    water_blocks: Annotated[int, 'Range | Min `1` and above | inclusive']  # Scales the particle size and its burst impulse.
    burst_impulse_base: float  # Scales the initial burst impulse


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::particle::GeyserBaseParticle": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Scales the particle size and its burst impulse.",
                "key": "water_blocks",
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
                "desc": "Scales the initial burst impulse",
                "key": "burst_impulse_base",
                "type": {
                    "kind": "float"
                }
            }
        ]
    }
}

