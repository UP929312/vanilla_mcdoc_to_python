"""
Generated from symbols.json for ::java::util::memory::SonicBoomSoundDelay
Local link to file: vanilla_mcdoc/util/memory/SonicBoomSoundDelay.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class ValueStruct(GeneratedModel):
    pass


class SonicBoomSoundDelay(ExpirableValue):
    value: ValueStruct  # If present, will delay the warden's sonic boom animation.
