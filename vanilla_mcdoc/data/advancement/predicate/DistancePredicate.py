"""
Generated from symbols.json for ::java::data::advancement::predicate::DistancePredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/DistancePredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds


class DistancePredicate(GeneratedModel):
    x: MinMaxBounds[float] | float | None = None
    y: MinMaxBounds[float] | float | None = None
    z: MinMaxBounds[float] | float | None = None
    absolute: MinMaxBounds[float] | float | None = None
    horizontal: MinMaxBounds[float] | float | None = None
