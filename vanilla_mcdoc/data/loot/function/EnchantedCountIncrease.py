"""
Generated from symbols.json for ::java::data::loot::function::EnchantedCountIncrease
Local link to file: vanilla_mcdoc/data/loot/function/EnchantedCountIncrease.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.data.loot.function.Conditions import Conditions
from vanilla_mcdoc.data.loot.function.EnchantedCountBase import EnchantedCountBase
from vanilla_mcdoc.minecraft_types import IdSpec


class EnchantedCountIncrease(Conditions, EnchantedCountBase):
    enchantment: Annotated[str, IdSpec(registry='enchantment')]  # Enchantment that increases yields.
