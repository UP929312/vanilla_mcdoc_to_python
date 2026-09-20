"""
Generated from symbols.json for ::java::data::loot::DynamicPoolEntry
Local link to file: generated_symbols/data/loot/DynamicPoolEntry.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.data.loot.SingletonPoolEntry import SingletonPoolEntry

if TYPE_CHECKING:
    from generated_symbols.data.loot.DynamicDrops import DynamicDrops


class DynamicPoolEntry(SingletonPoolEntry):
    name: DynamicDrops


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::DynamicPoolEntry": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "name",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::DynamicDrops",
                    "attributes": [
                        {
                            "name": "id"
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::SingletonPoolEntry"
                }
            }
        ]
    }
}

