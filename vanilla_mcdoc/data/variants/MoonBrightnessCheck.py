"""
Generated from symbols.json for ::java::data::variants::MoonBrightnessCheck
Local link to file: vanilla_mcdoc/data/variants/MoonBrightnessCheck.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds


class MoonBrightnessCheck(GeneratedModel):
    range: MinMaxBounds[float] | float  # Checks if the current moon brightness is within a certain range.
