# Generated from symbols.json for ::java::util::memory::Home
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.util.memory.ExpirableValue import ExpirableValue

if TYPE_CHECKING:
    from generated_symbols.util.GlobalPos import GlobalPos


@dataclass(kw_only=True)
class Home(ExpirableValue):
    value: GlobalPos  # Position of the villager's home.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::Home": {
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
                "desc": "Position of the villager's home.",
                "key": "value",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::GlobalPos"
                }
            }
        ]
    }
}

