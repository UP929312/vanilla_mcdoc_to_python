"""
Generated from symbols.json for ::java::util::memory::IsTempted
Local link to file: vanilla_mcdoc/util/memory/IsTempted.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class IsTempted(ExpirableValue):
    value: bool  # Whether the mob is currently tempted by a player.
