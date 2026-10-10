"""
Generated from symbols.json for ::java::data::loot::condition::Inverted
Local link to file: vanilla_mcdoc/data/loot/condition/Inverted.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.predicate.PredicateRef import PredicateRef


class Inverted(GeneratedModel):
    term: PredicateRef
