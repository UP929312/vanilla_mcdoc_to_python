"""
Generated from symbols.json for ::java::data::enchantment::level_based_value::ClampedLevelValue
Local link to file: vanilla_mcdoc/data/enchantment/level_based_value/ClampedLevelValue.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.level_based_value.LevelBasedValue import LevelBasedValue


class ClampedLevelValue(GeneratedModel):
    value: LevelBasedValue
    min: float
    max: float
