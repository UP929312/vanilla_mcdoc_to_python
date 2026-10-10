"""
Generated from symbols.json for ::java::util::memory::JobSite
Local link to file: vanilla_mcdoc/util/memory/JobSite.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue

if TYPE_CHECKING:
    from vanilla_mcdoc.util.GlobalPos import GlobalPos


class JobSite(ExpirableValue):
    value: GlobalPos  # Position of the villager's job site.
