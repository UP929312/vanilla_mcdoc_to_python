"""
Generated from symbols.json for ::java::data::enchantment::effect::MultiplyEffectValue
Local link to file: vanilla_mcdoc/data/enchantment/effect/MultiplyEffectValue.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.LevelBasedValue import LevelBasedValue


class MultiplyEffectValue(GeneratedModel):
    factor: LevelBasedValue  # Level-Based Value determining the factor to multiply in
