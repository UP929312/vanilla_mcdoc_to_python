"""
Generated from symbols.json for ::java::util::memory::Home
Local link to file: vanilla_mcdoc/util/memory/Home.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue

if TYPE_CHECKING:
    from vanilla_mcdoc.util.GlobalPos import GlobalPos


class Home(ExpirableValue):
    value: GlobalPos  # Position of the villager's home.
