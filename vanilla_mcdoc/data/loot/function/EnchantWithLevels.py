"""
Generated from symbols.json for ::java::data::loot::function::EnchantWithLevels
Local link to file: vanilla_mcdoc/data/loot/function/EnchantWithLevels.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.data.loot.function.Conditions import Conditions
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.number_provider.IntNumberProviderRef import IntNumberProviderRef


class EnchantWithLevels(Conditions):
    levels: IntNumberProviderRef  # The levels to enchant this item with.
    options: Annotated[str, IdSpec(registry='enchantment', tags='allowed')] | list[Annotated[str, IdSpec(registry='enchantment')]] | None = None  # The allowed enchantments. If omitted, all enchantments applicable to the item are possible.
    include_additional_cost_component: bool | None = None  # Whether to add `additional_trade_cost` component to the enchanted item. Additional cost value is equal to the level cost determined by `levels`. Defaults to `false`.
