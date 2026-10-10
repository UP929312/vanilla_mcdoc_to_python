"""
Generated from symbols.json for ::java::util::memory::LastWoken
Local link to file: vanilla_mcdoc/util/memory/LastWoken.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class LastWoken(ExpirableValue):
    value: int  # The gametime tick that the villager last woke up from a bed.
