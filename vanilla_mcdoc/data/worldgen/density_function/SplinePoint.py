"""
Generated from symbols.json for ::java::data::worldgen::density_function::SplinePoint
Local link to file: vanilla_mcdoc/data/worldgen/density_function/SplinePoint.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.density_function.CubicSpline import CubicSpline


class SplinePoint(GeneratedModel):
    location: float
    derivative: float
    value: CubicSpline


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::density_function::SplinePoint": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "location",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "pair",
                "key": "derivative",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "pair",
                "key": "value",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::CubicSpline"
                }
            }
        ]
    }
}
