"""
Generated from symbols.json for ::java::data::loot::LootPool
Local link to file: vanilla_mcdoc/data/loot/LootPool.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.item_modifier.ItemModifier import ItemModifier
    from vanilla_mcdoc.data.loot.LootPoolEntry import LootPoolEntry
    from vanilla_mcdoc.data.number_provider.FloatNumberProviderRef import FloatNumberProviderRef
    from vanilla_mcdoc.data.number_provider.IntNumberProviderRef import IntNumberProviderRef
    from vanilla_mcdoc.data.predicate.PredicateRef import PredicateRef


class LootPool(GeneratedModel):
    rolls: IntNumberProviderRef
    bonus_rolls: FloatNumberProviderRef | None = None
    entries: list[LootPoolEntry]
    modifier: ItemModifier | None = None
    condition: PredicateRef | None = None
