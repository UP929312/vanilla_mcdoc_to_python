"""
Generated from symbols.json for ::java::data::worldgen::density_function::Spline
Local link to file: vanilla_mcdoc/data/worldgen/density_function/Spline.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.density_function.CubicSpline import CubicSpline


class Spline(GeneratedModel):
    spline: CubicSpline


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::density_function::Spline": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "spline",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::CubicSpline"
                }
            },
            {
                "kind": "pair",
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
                ],
                "key": "min_value",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::NoiseRange"
                }
            },
            {
                "kind": "pair",
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
                ],
                "key": "max_value",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::NoiseRange"
                }
            }
        ]
    }
}
