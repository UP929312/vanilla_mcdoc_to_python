"""
Generated from symbols.json for ::java::util::memory::BreezeJumpCooldown
Local link to file: vanilla_mcdoc/util/memory/BreezeJumpCooldown.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class ValueStruct(GeneratedModel):
    pass


class BreezeJumpCooldown(ExpirableValue):
    value: ValueStruct  # If present, the breeze will not long jump or slide. Set after performing a long jump.
