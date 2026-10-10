"""
Generated from symbols.json for ::java::util::memory::MeetingPoint
Local link to file: vanilla_mcdoc/util/memory/MeetingPoint.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue

if TYPE_CHECKING:
    from vanilla_mcdoc.util.GlobalPos import GlobalPos


class MeetingPoint(ExpirableValue):
    value: GlobalPos  # Position of the villager's meeting point.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::MeetingPoint": {
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
                "desc": "Position of the villager's meeting point.",
                "key": "value",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::GlobalPos"
                }
            }
        ]
    }
}
