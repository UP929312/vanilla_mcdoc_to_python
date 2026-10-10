"""
Generated from symbols.json for ::java::util::memory::SonicBoomCooldown
Local link to file: vanilla_mcdoc/util/memory/SonicBoomCooldown.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class ValueStruct(GeneratedModel):
    pass


class SonicBoomCooldown(ExpirableValue):
    value: ValueStruct  # If present, the warden will not use the sonic boom attack.
