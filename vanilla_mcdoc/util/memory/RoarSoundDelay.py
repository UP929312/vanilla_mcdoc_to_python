"""
Generated from symbols.json for ::java::util::memory::RoarSoundDelay
Local link to file: vanilla_mcdoc/util/memory/RoarSoundDelay.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class ValueStruct(GeneratedModel):
    pass


class RoarSoundDelay(ExpirableValue):
    value: ValueStruct  # If present, the warden doesn't roar.
