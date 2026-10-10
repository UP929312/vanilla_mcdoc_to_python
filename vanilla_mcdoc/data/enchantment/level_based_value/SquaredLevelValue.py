"""
Generated from symbols.json for ::java::data::enchantment::level_based_value::SquaredLevelValue
Local link to file: vanilla_mcdoc/data/enchantment/level_based_value/SquaredLevelValue.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class SquaredLevelValue(GeneratedModel):
    added: float  # Added to the result so that the result becomes `square(level) + added`.
