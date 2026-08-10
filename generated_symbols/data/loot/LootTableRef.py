"""
Generated from symbols.json for ::java::data::loot::LootTableRef
Local link to file: generated_symbols/data/loot/LootTableRef.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.loot.LootTable import LootTable


type LootTableRef = LootTable | Annotated[str, IdSpec(registry='loot_table')]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::LootTableRef": {
        "kind": "union",
        "members": [
            {
                "kind": "reference",
                "path": "::java::data::loot::LootTable"
            },
            {
                "kind": "string",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    },
                    {
                        "name": "id",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "loot_table"
                            }
                        }
                    }
                ]
            }
        ]
    }
}

