"""
Generated from symbols.json for ::java::data::loot::function::SetEnchantments
Local link to file: vanilla_mcdoc/data/loot/function/SetEnchantments.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.data.loot.function.Conditions import Conditions
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.number_provider.IntNumberProviderRef import IntNumberProviderRef


class SetEnchantments(Conditions):
    enchantments: dict[Annotated[str, IdSpec(registry='enchantment')], IntNumberProviderRef]  # A map of enchantments to levels. Setting an enchantment to `0` removes it from the item.
    add: bool | None = None  # Whether to add to the level of each enchantment. Defaults to `false`.
