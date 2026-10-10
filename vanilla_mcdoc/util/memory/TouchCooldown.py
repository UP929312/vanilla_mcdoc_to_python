"""
Generated from symbols.json for ::java::util::memory::TouchCooldown
Local link to file: vanilla_mcdoc/util/memory/TouchCooldown.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class ValueStruct(GeneratedModel):
    pass


class TouchCooldown(ExpirableValue):
    value: ValueStruct  # If present, the warden will not react to being pushed by another mob. Set to 20 when touched.
