"""
Generated from symbols.json for ::java::data::advancement::predicate::MovementPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/MovementPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds


class MovementPredicate(GeneratedModel):
    x: MinMaxBounds[float] | float | None = None
    y: MinMaxBounds[float] | float | None = None
    z: MinMaxBounds[float] | float | None = None
    speed: MinMaxBounds[float] | float | None = None
    horizontal_speed: MinMaxBounds[float] | float | None = None
    vertical_speed: MinMaxBounds[float] | float | None = None
    fall_distance: MinMaxBounds[float] | float | None = None
