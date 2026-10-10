"""
Generated from symbols.json for ::java::data::predicate::PredicateListRef
Local link to file: vanilla_mcdoc/data/predicate/PredicateListRef.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.loot.LootCondition import LootCondition


type PredicateListRef = LootCondition | Annotated[str, IdSpec(registry='predicate', tags='allowed')] | list[Annotated[str, IdSpec(registry='predicate')] | LootCondition]
