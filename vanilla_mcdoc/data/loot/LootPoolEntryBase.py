"""
Generated from symbols.json for ::java::data::loot::LootPoolEntryBase
Local link to file: vanilla_mcdoc/data/loot/LootPoolEntryBase.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.item_modifier.ItemModifier import ItemModifier
    from vanilla_mcdoc.data.predicate.PredicateRef import PredicateRef


class LootPoolEntryBase(GeneratedModel):
    modifier: ItemModifier | None = None
    condition: PredicateRef | None = None
