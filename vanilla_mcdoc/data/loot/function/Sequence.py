"""
Generated from symbols.json for ::java::data::loot::function::Sequence
Local link to file: vanilla_mcdoc/data/loot/function/Sequence.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from vanilla_mcdoc.data.item_modifier.ItemModifier import ItemModifier


class Sequence(Conditions):
    functions: ItemModifier  # List of functions to apply to this item.
