# Generated from symbols.json for ::java::data::loot::LootTableRef
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.loot.LootTable import LootTable


type LootTableRef = LootTable | str


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

