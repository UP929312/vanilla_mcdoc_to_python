"""
Generated from symbols.json for ::java::util::memory::Home
Local link to file: vanilla_mcdoc/util/memory/Home.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue

if TYPE_CHECKING:
    from vanilla_mcdoc.util.GlobalPos import GlobalPos


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
