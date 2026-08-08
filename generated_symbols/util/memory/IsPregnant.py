# Generated from symbols.json for ::java::util::memory::IsPregnant
from dataclasses import dataclass

from generated_symbols.util.memory.ExpirableValue import ExpirableValue


@dataclass(kw_only=True)
class ValueStruct:
    pass


@dataclass(kw_only=True)
class IsPregnant(ExpirableValue):
    value: ValueStruct  # Whether the frog is pregnant.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::IsPregnant": {
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
                "desc": "Whether the frog is pregnant.",
                "key": "value",
                "type": {
                    "kind": "struct",
                    "fields": []
                }
            }
        ]
    }
}

