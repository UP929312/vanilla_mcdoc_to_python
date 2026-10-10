"""
Generated from symbols.json for ::java::util::memory::AdmiringDisable
Local link to file: vanilla_mcdoc/util/memory/AdmiringDisable.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class AdmiringDisable(ExpirableValue):
    value: bool  # Whether the piglin cannot admire an item. Set when converting, when attacked, or when admiring an item.
