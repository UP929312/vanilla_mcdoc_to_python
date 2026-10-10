"""
Generated from symbols.json for ::java::util::memory::SnifferExploredPositions
Local link to file: vanilla_mcdoc/util/memory/SnifferExploredPositions.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class SnifferExploredPositions(ExpirableValue):
    value: Annotated[list[tuple[int, int, int]], Field(max_length=20)]  # Last 20 block positions that the sniffer has dug up. The sniffer will not dig in these positions.
