"""
Generated from symbols.json for ::java::data::advancement::predicate::FoodPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/FoodPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds


class FoodPredicate(GeneratedModel):
    level: MinMaxBounds[int] | int | None = None
    saturation: MinMaxBounds[float] | float | None = None
