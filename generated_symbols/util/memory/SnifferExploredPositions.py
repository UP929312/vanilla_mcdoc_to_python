"""
Generated from symbols.json for ::java::util::memory::SnifferExploredPositions
Local link to file: generated_symbols/util/memory/SnifferExploredPositions.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from generated_symbols.util.memory.ExpirableValue import ExpirableValue


class SnifferExploredPositions(ExpirableValue):
    value: Annotated[list[tuple[int, int, int]], Field(max_length=20)]  # Last 20 block positions that the sniffer has dug up. The sniffer will not dig in these positions.


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

