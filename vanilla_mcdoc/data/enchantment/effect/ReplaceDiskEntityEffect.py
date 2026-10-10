"""
Generated from symbols.json for ::java::data::enchantment::effect::ReplaceDiskEntityEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect/ReplaceDiskEntityEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.data.enchantment.effect.ReplaceBlockEntityEffect import ReplaceBlockEntityEffect

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.LevelBasedValue import LevelBasedValue


class ReplaceDiskEntityEffect(ReplaceBlockEntityEffect):
    offset: tuple[int, int, int] | None = None  # Relative coordinates to offset the center of the cylinder by. Defaults to `[0, 0, 0]`.
    radius: LevelBasedValue
    height: LevelBasedValue
