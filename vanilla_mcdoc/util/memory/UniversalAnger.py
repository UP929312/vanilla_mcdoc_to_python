"""
Generated from symbols.json for ::java::util::memory::UniversalAnger
Local link to file: vanilla_mcdoc/util/memory/UniversalAnger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class UniversalAnger(ExpirableValue):
    value: bool  # Whether the piglin is being universally angered. Only used when the `universalAnger` gamerule is enabled.
