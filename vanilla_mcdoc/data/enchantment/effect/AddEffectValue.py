"""
Generated from symbols.json for ::java::data::enchantment::effect::AddEffectValue
Local link to file: vanilla_mcdoc/data/enchantment/effect/AddEffectValue.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.LevelBasedValue import LevelBasedValue


class AddEffectValue(GeneratedModel):
    value: LevelBasedValue
