"""
Generated from symbols.json for ::java::data::loot::condition::ValueCheck
Local link to file: vanilla_mcdoc/data/loot/condition/ValueCheck.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.loot.IntRange import IntRange
    from vanilla_mcdoc.data.number_provider.LegacyNumberProvider import LegacyNumberProvider


class ValueCheck(GeneratedModel):
    value: LegacyNumberProvider  # Clamps to an integer.
    range: IntRange  # Passes when `value` is within this range.
