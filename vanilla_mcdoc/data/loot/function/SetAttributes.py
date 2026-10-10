"""
Generated from symbols.json for ::java::data::loot::function::SetAttributes
Local link to file: vanilla_mcdoc/data/loot/function/SetAttributes.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from vanilla_mcdoc.data.loot.function.AttributeModifier import AttributeModifier


class SetAttributes(Conditions):
    modifiers: list[AttributeModifier]  # List of attribute modifiers to apply to this item.
    replace: bool | None = None  # Whether to replace existing attributes (otherwise append to existing). Defaults to `true`.
