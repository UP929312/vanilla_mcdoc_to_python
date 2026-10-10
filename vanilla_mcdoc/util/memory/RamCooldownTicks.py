"""
Generated from symbols.json for ::java::util::memory::RamCooldownTicks
Local link to file: vanilla_mcdoc/util/memory/RamCooldownTicks.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class RamCooldownTicks(ExpirableValue):
    value: int  # Ticks before the goat can ram again.
