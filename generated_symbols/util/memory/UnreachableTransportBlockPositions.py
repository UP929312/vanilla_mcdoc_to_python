# Generated from symbols.json for ::java::util::memory::UnreachableTransportBlockPositions
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.util.memory.ExpirableValue import ExpirableValue

if TYPE_CHECKING:
    from generated_symbols.util.GlobalPos import GlobalPos


@dataclass(kw_only=True)
class UnreachableTransportBlockPositions(ExpirableValue):
    value: list[GlobalPos]  # A list of container positions that the copper golem has visited and failed to interact with.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::UnreachableTransportBlockPositions": {
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
                "desc": "A list of container positions that the copper golem has visited and failed to interact with.",
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

