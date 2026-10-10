"""
Generated from symbols.json for ::java::data::enchantment::EnchantmentCost
Local link to file: vanilla_mcdoc/data/enchantment/EnchantmentCost.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class EnchantmentCost(GeneratedModel):
    base: int  # Base cost at level 1.
    per_level_above_first: int  # Cost increase per level above 1.
