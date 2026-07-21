# Generated from symbols.json for ::java::util::memory::SnifferExploredPositions
from dataclasses import dataclass
from typing import Annotated
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


@dataclass(kw_only=True)
class SnifferExploredPositions(ExpirableValue):
    value: Annotated[list[tuple[int, int, int]], 'Length = up to 20 (inclusive)']  # Last 20 block positions that the sniffer has dug up. The sniffer will not dig in these positions.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::SnifferExploredPositions": {
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
                "desc": "Last 20 block positions that the sniffer has dug up. The sniffer will not dig in these positions.",
                "key": "value",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "int_array",
                        "lengthRange": {
                            "kind": 0,
                            "min": 3,
                            "max": 3
                        }
                    },
                    "lengthRange": {
                        "kind": 0,
                        "max": 20
                    }
                }
            }
        ]
    }
}

