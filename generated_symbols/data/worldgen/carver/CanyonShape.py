# Generated from symbols.json for ::java::data::worldgen::carver::CanyonShape
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.FloatProvider import FloatProvider


@dataclass(kw_only=True)
class CanyonShape:
    distance_factor: FloatProvider[float] | float
    thickness: FloatProvider[float] | float
    width_smoothness: Annotated[int, 'Range | Min `0` and above | inclusive']
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

