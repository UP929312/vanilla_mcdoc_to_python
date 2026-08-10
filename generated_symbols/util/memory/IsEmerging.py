"""
Generated from symbols.json for ::java::util::memory::IsEmerging
Local link to file: generated_symbols/util/memory/IsEmerging.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass

from generated_symbols.util.memory.ExpirableValue import ExpirableValue


@dataclass(kw_only=True)
class ValueStruct:
    pass


@dataclass(kw_only=True)
class IsEmerging(ExpirableValue):
    value: ValueStruct  # Whether the warden is currently emerging from the ground.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::IsEmerging": {
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
                "desc": "Whether the warden is currently emerging from the ground.",
                "key": "value",
                "type": {
                    "kind": "struct",
                    "fields": []
                }
            }
        ]
    }
}

