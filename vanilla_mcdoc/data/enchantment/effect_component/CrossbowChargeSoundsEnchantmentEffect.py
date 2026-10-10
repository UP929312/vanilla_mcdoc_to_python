"""
Generated from symbols.json for ::java::data::enchantment::effect_component::CrossbowChargeSoundsEnchantmentEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect_component/CrossbowChargeSoundsEnchantmentEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.SoundEventRef import SoundEventRef


class CrossbowChargeSoundsEnchantmentEffect(GeneratedModel):
    start: SoundEventRef | None = None  # Start of charging.
    mid: SoundEventRef | None = None  # Middle of charging.
    end: SoundEventRef | None = None  # End of charging.
