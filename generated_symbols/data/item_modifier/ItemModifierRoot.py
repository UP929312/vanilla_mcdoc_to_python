"""
Generated from symbols.json for ::java::data::item_modifier::ItemModifierRoot
Local link to file: generated_symbols/data/item_modifier/ItemModifierRoot.py
"""
# ~~~ CODE ~~~
from generated_symbols.data.loot.LootFunction import LootFunction


type ItemModifierRoot = LootFunction


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::item_modifier::ItemModifierRoot": {
        "kind": "union",
        "members": [
            {
                "kind": "reference",
                "path": "::java::data::item_modifier::ItemModifier",
                "attributes": [
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
            },
            {
                "kind": "reference",
                "path": "::java::data::loot::LootFunction",
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
                    }
                ]
            }
        ]
    }
}

