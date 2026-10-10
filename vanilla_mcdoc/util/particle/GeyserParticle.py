"""
Generated from symbols.json for ::java::util::particle::GeyserParticle
Local link to file: vanilla_mcdoc/util/particle/GeyserParticle.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class GeyserParticle(GeneratedModel):
    water_blocks: Annotated[int, Field(ge=1)]  # Scales the particle size and its burst impulse.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::particle::GeyserParticle": {
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
            }
        ]
    }
}
