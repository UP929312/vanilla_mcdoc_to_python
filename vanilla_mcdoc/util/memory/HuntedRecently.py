"""
Generated from symbols.json for ::java::util::memory::HuntedRecently
Local link to file: vanilla_mcdoc/util/memory/HuntedRecently.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class HuntedRecently(ExpirableValue):
    value: bool  # Whether the piglin just hunted recently. Set after hunting or spawning in a bastion remnant.
