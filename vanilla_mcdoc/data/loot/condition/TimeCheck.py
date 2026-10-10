"""
Generated from symbols.json for ::java::data::loot::condition::TimeCheck
Local link to file: vanilla_mcdoc/data/loot/condition/TimeCheck.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.loot.IntRange import IntRange


class TimeCheck(GeneratedModel):
    clock: Annotated[str, IdSpec(registry='world_clock')]  # The world clock to check.
    value: IntRange  # Check the current game tick.
    period: int | None = None  # Game tick supplied to `value` check gets modulo-divided by this. For example, if set to 24000, `value` operates on a time period of days.
