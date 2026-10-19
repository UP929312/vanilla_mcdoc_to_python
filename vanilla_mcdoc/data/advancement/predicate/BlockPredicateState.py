"""
Generated from symbols.json for ::java::data::advancement::predicate::BlockPredicateState
Local link to file: vanilla_mcdoc/data/advancement/predicate/BlockPredicateState.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds


type BlockPredicateState = dict[str, MinMaxBounds[str] | str]
