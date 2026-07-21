# Generated from symbols.json for ::java::data::worldgen::density_function::CubicSpline
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef
    from generated_symbols.data.worldgen.density_function.SplinePoint import SplinePoint


@dataclass(kw_only=True)
class CubicSplineStruct1:
    coordinate: DensityFunctionRef
    points: list[SplinePoint]

type CubicSpline = float | CubicSplineStruct1


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::density_function::CubicSpline": {
        "kind": "union",
        "members": [
            {
                "kind": "float"
            },
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "key": "coordinate",
                        "type": {
                            "kind": "union",
                            "members": [
                                {
                                    "kind": "reference",
                                    "path": "::java::data::worldgen::density_function::TerrainCoordinate",
                                    "attributes": [
                                        {
                                            "name": "until",
                                            "value": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "1.19"
                                                }
                                            }
                                        }
                                    ]
                                },
                                {
                                    "kind": "reference",
                                    "path": "::java::data::worldgen::density_function::DensityFunctionRef",
                                    "attributes": [
                                        {
                                            "name": "since",
                                            "value": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "1.19"
                                                }
                                            }
                                        }
                                    ]
                                }
                            ]
                        }
                    },
                    {
                        "kind": "pair",
                        "key": "points",
                        "type": {
                            "kind": "list",
                            "item": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::density_function::SplinePoint"
                            }
                        }
                    }
                ]
            }
        ]
    }
}

