"""
Generated from symbols.json for ::java::data::loot::function::EnchantRandomly
Local link to file: vanilla_mcdoc/data/loot/function/EnchantRandomly.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.data.loot.function.Conditions import Conditions
from vanilla_mcdoc.minecraft_types import IdSpec


class EnchantRandomly(Conditions):
    options: Annotated[str, IdSpec(registry='enchantment', tags='allowed')] | list[Annotated[str, IdSpec(registry='enchantment')]] | None = None  # The allowed enchantments. If omitted, all enchantments applicable to the item are possible.
    only_compatible: bool | None = None  # Whether to only enchant with item-compatible enchantments. Defaults to `true`.  Note: Books are considered compatible with all Enchantments.
    include_additional_cost_component: bool | None = None  # Whether to add `additional_trade_cost` component to the enchanted item. Additional cost value is determined by the enchantment level, with the formula `2 + random(0, 5 + level * 10) + 3 * level`. Defaults to `false`.
