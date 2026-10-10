"""
Generated from symbols.json for ::java::util::memory::LastSlept
Local link to file: vanilla_mcdoc/util/memory/LastSlept.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class LastSlept(ExpirableValue):
    value: int  # The gametime tick that the villager last slept in a bed.
