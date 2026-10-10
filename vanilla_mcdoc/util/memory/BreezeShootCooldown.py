"""
Generated from symbols.json for ::java::util::memory::BreezeShootCooldown
Local link to file: vanilla_mcdoc/util/memory/BreezeShootCooldown.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class ValueStruct(GeneratedModel):
    pass


class BreezeShootCooldown(ExpirableValue):
    value: ValueStruct  # If present, the breeze will not shoot a wind charge. Set after shooting
