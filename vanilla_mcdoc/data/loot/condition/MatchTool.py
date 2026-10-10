"""
Generated from symbols.json for ::java::data::loot::condition::MatchTool
Local link to file: vanilla_mcdoc/data/loot/condition/MatchTool.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate


class MatchTool(GeneratedModel):
    predicate: ItemPredicate
