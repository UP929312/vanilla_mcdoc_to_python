"""
Generated from symbols.json for ::java::util::particle::OldDustParticle
Local link to file: generated_symbols/util/particle/OldDustParticle.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from generated_symbols.base import GeneratedModel
from pydantic import Field


class OldDustParticle(GeneratedModel):
    r: float
    g: float
    b: float
    scale: Annotated[float, Field(ge=0.01, le=4)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::particle::OldDustParticle": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "r",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "pair",
                "key": "g",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "pair",
                "key": "b",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "pair",
                "key": "scale",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0.01,
                        "max": 4
                    }
                }
            }
        ]
    }
}

