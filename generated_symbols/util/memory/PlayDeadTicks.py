# Generated from symbols.json for ::java::util::memory::PlayDeadTicks
from dataclasses import dataclass
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


@dataclass(kw_only=True)
class PlayDeadTicks(ExpirableValue):
    value: int  # Ticks until the axolotl stops playing dead.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::PlayDeadTicks": {
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
                "desc": "Ticks until the axolotl stops playing dead.",
                "key": "value",
                "type": {
                    "kind": "int"
                }
            }
        ]
    }
}

