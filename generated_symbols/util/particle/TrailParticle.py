"""
Generated from symbols.json for ::java::util::particle::TrailParticle
Local link to file: generated_symbols/util/particle/TrailParticle.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from generated_symbols.base import GeneratedModel
from pydantic import Field

if TYPE_CHECKING:
    from generated_symbols.util.color.RGB import RGB


class TrailParticle(GeneratedModel):
    target: tuple[float, float, float]
    color: RGB
    duration: Annotated[int, Field(ge=1)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::particle::TrailParticle": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "target",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "double"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
                    }
                }
            },
            {
                "kind": "pair",
                "key": "color",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::color::RGB"
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
                                "value": "1.21.4"
                            }
                        }
                    }
                ],
                "key": "duration",
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

