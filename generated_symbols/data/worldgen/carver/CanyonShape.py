"""
Generated from symbols.json for ::java::data::worldgen::carver::CanyonShape
Local link to file: generated_symbols/data/worldgen/carver/CanyonShape.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.FloatProvider import FloatProvider


class CanyonShape(GeneratedModel):
    distance_factor: FloatProvider[float] | float
    thickness: FloatProvider[float] | float
    width_smoothness: Annotated[int, Field(ge=0)]
    horizontal_radius_factor: FloatProvider[float] | float
    vertical_radius_default_factor: float
    vertical_radius_center_factor: float
    y_scale: FloatProvider[float] | float


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::carver::CanyonShape": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "distance_factor",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::FloatProvider"
                    },
                    "typeArgs": [
                        {
                            "kind": "float"
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "thickness",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::FloatProvider"
                    },
                    "typeArgs": [
                        {
                            "kind": "float"
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "width_smoothness",
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
                "key": "horizontal_radius_factor",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::FloatProvider"
                    },
                    "typeArgs": [
                        {
                            "kind": "float"
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "vertical_radius_default_factor",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "pair",
                "key": "vertical_radius_center_factor",
                "type": {
                    "kind": "float"
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
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "y_scale",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::FloatProvider"
                    },
                    "typeArgs": [
                        {
                            "kind": "float"
                        }
                    ]
                }
            }
        ]
    }
}
