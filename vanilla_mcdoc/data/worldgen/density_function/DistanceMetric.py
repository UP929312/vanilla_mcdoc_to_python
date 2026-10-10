"""
Generated from symbols.json for ::java::data::worldgen::density_function::DistanceMetric
Local link to file: vanilla_mcdoc/data/worldgen/density_function/DistanceMetric.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class DistanceMetric(StrEnum):
    EUCLIDEAN = "euclidean"  # `sqrt(dx^2 + dy^2 + dz^2)`
    EUCLIDEANSQUARED = "euclidean_squared"  # `dx^2 + dy^2 + dz^2`
    MANHATTAN = "manhattan"  # `abs(dx) + abs(dy) + abs(dz)`
    CHEBYSHEV = "chebyshev"  # `max(abs(dx), abs(dy), abs(dz))`
