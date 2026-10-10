"""
Generated from symbols.json for ::java::data::loot::function::Conditions
Local link to file: vanilla_mcdoc/data/loot/function/Conditions.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.predicate.PredicateRef import PredicateRef


class Conditions(GeneratedModel):
    condition: PredicateRef | None = None
