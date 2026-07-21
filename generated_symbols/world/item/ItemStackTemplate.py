# Generated from symbols.json for ::java::world::item::ItemStackTemplate
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.item.ItemStack import ItemStack


type ItemStackTemplate = ItemStack | str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::ItemStackTemplate": {
        "kind": "union",
        "members": [
            {
                "kind": "reference",
                "path": "::java::world::item::ItemStack",
                "attributes": [
                    {
                        "name": "canonical"
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
                                "value": "26.1"
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
                                        "value": "item"
                                    }
                                },
                                "exclude": {
                                    "kind": "tree",
                                    "values": {
                                        "0": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "air"
                                            }
                                        }
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

