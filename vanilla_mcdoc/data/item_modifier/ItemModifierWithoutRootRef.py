"""
Generated from symbols.json for ::java::data::item_modifier::ItemModifierWithoutRootRef
Local link to file: vanilla_mcdoc/data/item_modifier/ItemModifierWithoutRootRef.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vanilla_mcdoc.data.loot.LootFunction import LootFunction


type ItemModifierWithoutRootRef = LootFunction | list[ItemModifierWithoutRootRef]
