# Generated from symbols.json for ::java::util::memory::PotentialJobSite
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.util.memory.ExpirableValue import ExpirableValue

if TYPE_CHECKING:
    from generated_symbols.util.GlobalPos import GlobalPos


@dataclass(kw_only=True)
class PotentialJobSite(ExpirableValue):
    value: GlobalPos  # Position of a potential job site of the villager.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::PotentialJobSite": {
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
                "desc": "Position of a potential job site of the villager.",
                "key": "value",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::GlobalPos"
                }
            }
        ]
    }
}

