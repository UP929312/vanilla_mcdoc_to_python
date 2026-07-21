# Generated from symbols.json for ::java::data::worldgen::processor_list::AppendLoot
from dataclasses import dataclass


@dataclass(kw_only=True)
class AppendLoot:
    loot_table: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::processor_list::AppendLoot": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "loot_table",
                "type": {
                    "kind": "string",
                    "attributes": [
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
            }
        ]
    }
}

