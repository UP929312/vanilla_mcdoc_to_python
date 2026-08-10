"""
Generated from symbols.json for ::java::util::memory::BreezeLeavingWater
Local link to file: generated_symbols/util/memory/BreezeLeavingWater.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass

from generated_symbols.util.memory.ExpirableValue import ExpirableValue


@dataclass(kw_only=True)
class ValueStruct:
    pass


@dataclass(kw_only=True)
class BreezeLeavingWater(ExpirableValue):
    value: ValueStruct  # If present, the breeze is in water.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::BreezeLeavingWater": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::memory::ExpirableValue"
                }
            },
            {
                "kind": "pair",
                "desc": "If present, the breeze is in water.",
                "key": "value",
                "type": {
                    "kind": "struct",
                    "fields": []
                }
            }
        ]
    }
}

