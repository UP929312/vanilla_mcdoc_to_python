"""
Generated from symbols.json for ::java::data::worldgen::density_function::DistanceMetric
Local link to file: generated_symbols/data/worldgen/density_function/DistanceMetric.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class DistanceMetric(StrEnum):
    EUCLIDEAN = "euclidean"  # `sqrt(dx^2 + dy^2 + dz^2)`
    EUCLIDEANSQUARED = "euclidean_squared"  # `dx^2 + dy^2 + dz^2`
    MANHATTAN = "manhattan"  # `abs(dx) + abs(dy) + abs(dz)`
    CHEBYSHEV = "chebyshev"  # `max(abs(dx), abs(dy), abs(dz))`


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::density_function::DistanceMetric": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "desc": "`sqrt(dx^2 + dy^2 + dz^2)`",
                "identifier": "Euclidean",
                "value": "euclidean"
            },
            {
                "desc": "`dx^2 + dy^2 + dz^2`",
                "identifier": "EuclideanSquared",
                "value": "euclidean_squared"
            },
            {
                "desc": "`abs(dx) + abs(dy) + abs(dz)`",
                "identifier": "Manhattan",
                "value": "manhattan"
            },
            {
                "desc": "`max(abs(dx), abs(dy), abs(dz))`",
                "identifier": "Chebyshev",
                "value": "chebyshev"
            }
        ]
    }
}

