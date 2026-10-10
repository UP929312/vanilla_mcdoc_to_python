"""
Generated from symbols.json for ::java::data::number_provider::context_float::EnchantmentLevelProvider
Local link to file: vanilla_mcdoc/data/number_provider/context_float/EnchantmentLevelProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.LevelBasedValue import LevelBasedValue


class EnchantmentLevelProvider(GeneratedModel):
    amount: LevelBasedValue
