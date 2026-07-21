# Generated from symbols.json for ::java::data::loot::TagPoolEntry
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.loot.SingletonPoolEntry import SingletonPoolEntry

if TYPE_CHECKING:
    from generated_symbols.util.registry_ref.ItemListRef import ItemListRef


@dataclass(kw_only=True)
class TagPoolEntry(SingletonPoolEntry):
    items: ItemListRef
    expand: bool  # If `true`, drops a random item from the tag.  If `false`, drops all items in the tag.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::TagPoolEntry": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
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
                ],
                "key": "name",
                "type": {
                    "kind": "string",
                    "attributes": [
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
                                    "tags": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "implicit"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
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
                ],
                "key": "items",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::registry_ref::ItemListRef"
                }
            },
            {
                "kind": "pair",
                "desc": "If `True`, drops a random item from the tag. \\\nIf `False`, drops all items in the tag.",
                "key": "expand",
                "type": {
                    "kind": "boolean"
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

