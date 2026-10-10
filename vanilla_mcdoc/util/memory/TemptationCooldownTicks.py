"""
Generated from symbols.json for ::java::util::memory::TemptationCooldownTicks
Local link to file: vanilla_mcdoc/util/memory/TemptationCooldownTicks.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class TemptationCooldownTicks(ExpirableValue):
    value: int  # Ticks before the mob can be tempted again.
