"""
Generated from symbols.json for ::java::util::memory::AdmiringItem
Local link to file: vanilla_mcdoc/util/memory/AdmiringItem.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class AdmiringItem(ExpirableValue):
    value: bool  # Whether the piglin is currently admiring an item.
