# Generated from symbols.json for ::java::data::item_modifier::ItemModifier
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.loot.LootFunction import LootFunction


type ItemModifier = LootFunction | list[ItemModifier] | str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::item_modifier::ItemModifier": {
        "kind": "union",
        "members": [
            {
                "kind": "reference",
                "path": "::java::data::loot::LootFunction"
            },
            {
                "kind": "list",
                "item": {
                    "kind": "reference",
                    "path": "::java::data::loot::LootFunction"
                },
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
                "kind": "list",
                "item": {
                    "kind": "reference",
                    "path": "::java::data::item_modifier::ItemModifier"
                },
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
                            "kind": "tree",
                            "values": {
                                "registry": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "item_modifier"
                                    }
                                },
                                "tags": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "allowed"
                                    }
                                }
                            }
                        }
                    }
                ]
            }
        ]
    }
}

