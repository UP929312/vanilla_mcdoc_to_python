"""
Generated from symbols.json for ::java::util::memory::VisitedBlockPositions
Local link to file: vanilla_mcdoc/util/memory/VisitedBlockPositions.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue

if TYPE_CHECKING:
    from vanilla_mcdoc.util.GlobalPos import GlobalPos


class VisitedBlockPositions(ExpirableValue):
    value: list[GlobalPos]  # A list of container positions that the copper golem has visited, whether successful or not.
