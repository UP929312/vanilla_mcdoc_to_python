"""
Generated from symbols.json for ::java::util::memory::GazeCooldownTicks
Local link to file: vanilla_mcdoc/util/memory/GazeCooldownTicks.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class GazeCooldownTicks(ExpirableValue):
    value: int  # Ticks before the armadillo or camel can randomly look around again.
