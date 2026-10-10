"""
Generated from symbols.json for ::java::data::enchantment::effect::ApplyImpulseEntityEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect/ApplyImpulseEntityEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.LevelBasedValue import LevelBasedValue


class ApplyImpulseEntityEffect(GeneratedModel):
    direction: tuple[float, float, float]  # Impulse direction in local coordinates (the same used by `tp @s ^ ^ ^`).  `[left, upward, forward]`
    coordinate_scale: tuple[float, float, float]  # The multipler to apply to the computed impulse direction.  `[x, y, z]`
    magnitude: LevelBasedValue  # The scale of the impulse.
