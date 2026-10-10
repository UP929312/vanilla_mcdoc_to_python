"""
Generated from symbols.json for ::java::util::memory::MeetingPoint
Local link to file: vanilla_mcdoc/util/memory/MeetingPoint.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue

if TYPE_CHECKING:
    from vanilla_mcdoc.util.GlobalPos import GlobalPos


class MeetingPoint(ExpirableValue):
    value: GlobalPos  # Position of the villager's meeting point.
