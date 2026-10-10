"""
Generated from symbols.json for ::java::util::memory::HasHuntingCooldown
Local link to file: vanilla_mcdoc/util/memory/HasHuntingCooldown.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class HasHuntingCooldown(ExpirableValue):
    value: bool  # Whether the axolotl is in a hunting cooldown.
