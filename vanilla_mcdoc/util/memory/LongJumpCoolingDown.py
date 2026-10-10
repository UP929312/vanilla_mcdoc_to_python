"""
Generated from symbols.json for ::java::util::memory::LongJumpCoolingDown
Local link to file: vanilla_mcdoc/util/memory/LongJumpCoolingDown.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class LongJumpCoolingDown(ExpirableValue):
    value: int  # Ticks before the goat can long jump again.
