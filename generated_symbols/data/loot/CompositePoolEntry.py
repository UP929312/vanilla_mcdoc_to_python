# Generated from symbols.json for ::java::data::loot::CompositePoolEntry
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated
from generated_symbols.data.loot.LootPoolEntryBase import LootPoolEntryBase

if TYPE_CHECKING:
    from generated_symbols.data.loot.LootPoolEntry import LootPoolEntry


@dataclass(kw_only=True)
class CompositePoolEntry(LootPoolEntryBase):
    children: Annotated[list[LootPoolEntry], 'Length = 1 (inclusive) and above']


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

