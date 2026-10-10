"""
Generated from symbols.json for ::java::util::memory::PlayDeadTicks
Local link to file: vanilla_mcdoc/util/memory/PlayDeadTicks.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class PlayDeadTicks(ExpirableValue):
    value: int  # Ticks until the axolotl stops playing dead.
