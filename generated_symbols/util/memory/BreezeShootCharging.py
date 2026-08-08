# Generated from symbols.json for ::java::util::memory::BreezeShootCharging
from dataclasses import dataclass

from generated_symbols.util.memory.ExpirableValue import ExpirableValue


@dataclass(kw_only=True)
class ValueStruct:
    pass


@dataclass(kw_only=True)
class BreezeShootCharging(ExpirableValue):
    value: ValueStruct  # If present, the breeze will not shoot a wind charge. Set when starting to shoot.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::BreezeShootCharging": {
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
                "desc": "If present, the breeze will not shoot a wind charge. Set when starting to shoot.",
                "key": "value",
                "type": {
                    "kind": "struct",
                    "fields": []
                }
            }
        ]
    }
}

