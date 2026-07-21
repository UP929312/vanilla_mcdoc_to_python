# Generated from symbols.json for ::java::util::memory::JobSite
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.util.memory.ExpirableValue import ExpirableValue

if TYPE_CHECKING:
    from generated_symbols.util.GlobalPos import GlobalPos


@dataclass(kw_only=True)
class JobSite(ExpirableValue):
    value: GlobalPos  # Position of the villager's job site.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::JobSite": {
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
                "desc": "Position of the villager's job site.",
                "key": "value",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::GlobalPos"
                }
            }
        ]
    }
}

