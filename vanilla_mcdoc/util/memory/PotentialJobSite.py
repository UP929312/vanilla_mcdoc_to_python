"""
Generated from symbols.json for ::java::util::memory::PotentialJobSite
Local link to file: vanilla_mcdoc/util/memory/PotentialJobSite.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue

if TYPE_CHECKING:
    from vanilla_mcdoc.util.GlobalPos import GlobalPos


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
