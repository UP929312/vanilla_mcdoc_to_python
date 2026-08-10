"""
Generated from symbols.json for ::java::data::worldgen::density_function::DistanceToPoint
Local link to file: generated_symbols/data/worldgen/density_function/DistanceToPoint.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.density_function.DistanceMetric import DistanceMetric


@dataclass(kw_only=True)
class DistanceToPoint:
    point: tuple[int, int, int]
    metric: DistanceMetric


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::density_function::DistanceToPoint": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "point",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "int"
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
                "key": "metric",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DistanceMetric"
                }
            }
        ]
    }
}

