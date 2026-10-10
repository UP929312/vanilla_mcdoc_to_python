"""
Generated from symbols.json for ::java::data::enchantment::effect::IgniteEntityEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect/IgniteEntityEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.LevelBasedValue import LevelBasedValue


class IgniteEntityEffect(GeneratedModel):
    duration: LevelBasedValue  # Seconds the fire should last.
