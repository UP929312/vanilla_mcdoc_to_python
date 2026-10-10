"""
Generated from symbols.json for ::java::data::advancement::predicate::FluidPredicateState
Local link to file: vanilla_mcdoc/data/advancement/predicate/FluidPredicateState.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds


type FluidPredicateState = dict[str, MinMaxBounds[int] | int | bool | str]
