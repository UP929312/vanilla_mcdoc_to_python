# Generated from symbols.json for ::java::util::memory::BreezeJumpTarget
from dataclasses import dataclass
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


@dataclass(kw_only=True)
class BreezeJumpTarget(ExpirableValue):
    value: tuple[int, int, int]  # The block position that the breeze is jumping towards.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::BreezeJumpTarget": {
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
                "desc": "The block position that the breeze is jumping towards.",
                "key": "value",
                "type": {
                    "kind": "int_array",
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
                    }
                }
            }
        ]
    }
}

