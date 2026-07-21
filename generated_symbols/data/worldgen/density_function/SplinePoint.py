# Generated from symbols.json for ::java::data::worldgen::density_function::SplinePoint
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.density_function.CubicSpline import CubicSpline


@dataclass(kw_only=True)
class SplinePoint:
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

