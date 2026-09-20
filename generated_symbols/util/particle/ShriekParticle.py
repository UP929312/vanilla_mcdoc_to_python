"""
Generated from symbols.json for ::java::util::particle::ShriekParticle
Local link to file: generated_symbols/util/particle/ShriekParticle.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from generated_symbols.base import GeneratedModel
from pydantic import Field


class ShriekParticle(GeneratedModel):
    delay: Annotated[int, Field(ge=0)]  # Ticks until the particle renders.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::particle::ShriekParticle": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.20.5"
                            }
                        }
                    }
                ],
                "key": "value",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.20.5"
                            }
                        }
                    }
                ],
                "desc": "Ticks until the particle renders.",
                "key": "delay",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                }
            }
        ]
    }
}

