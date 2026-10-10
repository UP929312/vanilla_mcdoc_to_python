"""
Generated from symbols.json for ::java::util::memory::ItemPickupCooldownTicks
Local link to file: vanilla_mcdoc/util/memory/ItemPickupCooldownTicks.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class ItemPickupCooldownTicks(ExpirableValue):
    value: int  # Ticks before the allay goes to pick up an item again.
