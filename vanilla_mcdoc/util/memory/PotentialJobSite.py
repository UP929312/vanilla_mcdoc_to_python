"""
Generated from symbols.json for ::java::util::memory::PotentialJobSite
Local link to file: vanilla_mcdoc/util/memory/PotentialJobSite.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue

if TYPE_CHECKING:
    from vanilla_mcdoc.util.GlobalPos import GlobalPos


class PotentialJobSite(ExpirableValue):
    value: GlobalPos  # Position of a potential job site of the villager.
