"""
Generated from symbols.json for ::java::util::memory::VisitedBlockPositions
Local link to file: vanilla_mcdoc/util/memory/VisitedBlockPositions.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue

if TYPE_CHECKING:
    from vanilla_mcdoc.util.GlobalPos import GlobalPos


class VisitedBlockPositions(ExpirableValue):
    value: list[GlobalPos]  # A list of container positions that the copper golem has visited, whether successful or not.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::VisitedBlockPositions": {
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
                "desc": "A list of container positions that the copper golem has visited, whether successful or not.",
                "key": "value",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::util::GlobalPos"
                    }
                }
            }
        ]
    }
}
