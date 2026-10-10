"""
Generated from symbols.json for ::java::util::memory::IsPregnant
Local link to file: vanilla_mcdoc/util/memory/IsPregnant.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class ValueStruct(GeneratedModel):
    pass


class IsPregnant(ExpirableValue):
    value: ValueStruct  # Whether the frog is pregnant.
