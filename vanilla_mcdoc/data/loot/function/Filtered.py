"""
Generated from symbols.json for ::java::data::loot::function::Filtered
Local link to file: vanilla_mcdoc/data/loot/function/Filtered.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
    from vanilla_mcdoc.data.item_modifier.ItemModifier import ItemModifier


class Filtered(Conditions):
    item_filter: ItemPredicate  # Item predicate to select items to modify.
    on_pass: ItemModifier | None = None  # Loot function to apply to the item when `item_filter` passes.
    on_fail: ItemModifier | None = None  # Loot function to apply to the item when `item_filter` fails.
