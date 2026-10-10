"""
Generated from symbols.json for ::java::data::loot::condition::AnyOf
Local link to file: vanilla_mcdoc/data/loot/condition/AnyOf.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.predicate.PredicateListRef import PredicateListRef


class AnyOf(GeneratedModel):
    terms: PredicateListRef  # Passes when any of these conditions pass.
