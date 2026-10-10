"""
Generated from symbols.json for ::java::util::memory::BreezeJumpInhaling
Local link to file: vanilla_mcdoc/util/memory/BreezeJumpInhaling.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class ValueStruct(GeneratedModel):
    pass


class BreezeJumpInhaling(ExpirableValue):
    value: ValueStruct  # If present, the breeze will not long jump or shoot a wind charge when stuck.
