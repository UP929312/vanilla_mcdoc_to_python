"""
Generated from symbols.json for ::java::data::loot::condition::AllOf
Local link to file: vanilla_mcdoc/data/loot/condition/AllOf.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.predicate.PredicateListRef import PredicateListRef


class AllOf(GeneratedModel):
    terms: PredicateListRef  # Passes when all of these conditions pass.
