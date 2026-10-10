"""
Generated from symbols.json for ::java::data::loot::CompositePoolEntry
Local link to file: vanilla_mcdoc/data/loot/CompositePoolEntry.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.data.loot.LootPoolEntryBase import LootPoolEntryBase

if TYPE_CHECKING:
    from vanilla_mcdoc.data.loot.LootPoolEntry import LootPoolEntry


class CompositePoolEntry(LootPoolEntryBase):
    children: Annotated[list[LootPoolEntry], Field(min_length=1)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::CompositePoolEntry": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "children",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::loot::LootPoolEntry"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 1
                    }
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::LootPoolEntryBase"
                }
            }
        ]
    }
}
