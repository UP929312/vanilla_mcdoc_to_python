"""
Generated from symbols.json for ::java::util::memory::VibrationCooldown
Local link to file: vanilla_mcdoc/util/memory/VibrationCooldown.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class ValueStruct(GeneratedModel):
    pass


class VibrationCooldown(ExpirableValue):
    value: ValueStruct  # If present, the warden will not react to vibrations. Set to 40 when receiving a vibration.
