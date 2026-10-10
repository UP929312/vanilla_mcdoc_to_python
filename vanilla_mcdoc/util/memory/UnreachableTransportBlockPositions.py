"""
Generated from symbols.json for ::java::util::memory::UnreachableTransportBlockPositions
Local link to file: vanilla_mcdoc/util/memory/UnreachableTransportBlockPositions.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue

if TYPE_CHECKING:
    from vanilla_mcdoc.util.GlobalPos import GlobalPos


class UnreachableTransportBlockPositions(ExpirableValue):
    value: list[GlobalPos]  # A list of container positions that the copper golem has visited and failed to interact with.
