"""
Generated from symbols.json for ::java::util::memory::LastWorkedAtPoi
Local link to file: vanilla_mcdoc/util/memory/LastWorkedAtPoi.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class LastWorkedAtPoi(ExpirableValue):
    value: int  # The gametime tick that the villager last worked at their job site.
