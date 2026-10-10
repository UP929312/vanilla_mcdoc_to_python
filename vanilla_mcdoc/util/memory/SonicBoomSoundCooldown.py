"""
Generated from symbols.json for ::java::util::memory::SonicBoomSoundCooldown
Local link to file: vanilla_mcdoc/util/memory/SonicBoomSoundCooldown.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class ValueStruct(GeneratedModel):
    pass


class SonicBoomSoundCooldown(ExpirableValue):
    value: ValueStruct  # If present, the warden's sonic boom animation will not spawn particles and play sounds.
