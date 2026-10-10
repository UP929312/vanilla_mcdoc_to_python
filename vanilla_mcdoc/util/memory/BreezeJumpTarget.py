"""
Generated from symbols.json for ::java::util::memory::BreezeJumpTarget
Local link to file: vanilla_mcdoc/util/memory/BreezeJumpTarget.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class BreezeJumpTarget(ExpirableValue):
    value: tuple[int, int, int]  # The block position that the breeze is jumping towards.
