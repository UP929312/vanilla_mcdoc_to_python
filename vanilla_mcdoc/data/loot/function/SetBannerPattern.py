"""
Generated from symbols.json for ::java::data::loot::function::SetBannerPattern
Local link to file: vanilla_mcdoc/data/loot/function/SetBannerPattern.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from vanilla_mcdoc.data.loot.function.BannerPatternLayer import BannerPatternLayer


class SetBannerPattern(Conditions):
    patterns: list[BannerPatternLayer]  # List of banner pattern layers.
    append: bool  # Whether to add to the banner pattern list.
