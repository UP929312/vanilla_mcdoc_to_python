"""
Generated from symbols.json for ::java::util::particle::GeyserBaseParticle
Local link to file: generated_symbols/util/particle/GeyserBaseParticle.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from generated_symbols.base import GeneratedModel
from pydantic import Field


class GeyserBaseParticle(GeneratedModel):
    water_blocks: Annotated[int, Field(ge=1)]  # Scales the particle size and its burst impulse.
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

