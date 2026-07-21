# Generated from symbols.json for ::java::data::predicate::Predicate
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.loot.LootCondition import LootCondition


type Predicate = LootCondition


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::predicate::Predicate": {
        "kind": "union",
        "members": [
            {
                "kind": "reference",
                "path": "::java::data::loot::LootCondition"
            },
            {
                "kind": "list",
                "item": {
                    "kind": "reference",
                    "path": "::java::data::loot::LootCondition"
                },
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.16"
                            }
                        }
                    },
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ]
            }
        ]
    }
}

