"""
Generated from symbols.json for ::java::util::memory::LikedNoteblockCooldownTicks
Local link to file: vanilla_mcdoc/util/memory/LikedNoteblockCooldownTicks.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class LikedNoteblockCooldownTicks(ExpirableValue):
    value: int  # Ticks before the allay stops putting items at the liked note block.
