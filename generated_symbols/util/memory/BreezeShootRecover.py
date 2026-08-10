"""
Generated from symbols.json for ::java::util::memory::BreezeShootRecover
Local link to file: generated_symbols/util/memory/BreezeShootRecover.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass

from generated_symbols.util.memory.ExpirableValue import ExpirableValue


@dataclass(kw_only=True)
class ValueStruct:
    pass


@dataclass(kw_only=True)
class BreezeShootRecover(ExpirableValue):
    value: ValueStruct  # If present, the breeze will not shoot a wind charge.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::BreezeShootRecover": {
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
                "desc": "If present, the breeze will not shoot a wind charge.",
                "key": "value",
                "type": {
                    "kind": "struct",
                    "fields": []
                }
            }
        ]
    }
}

