"""
Generated from symbols.json for ::java::data::loot::TagPoolEntry
Local link to file: generated_symbols/data/loot/TagPoolEntry.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING

from generated_symbols.data.loot.SingletonPoolEntry import SingletonPoolEntry

if TYPE_CHECKING:
    from generated_symbols.util.registry_ref.ItemListRef import ItemListRef


@dataclass(kw_only=True)
class TagPoolEntry(SingletonPoolEntry):
    items: ItemListRef
    expand: bool | None = None  # If `true`, randomly selects an item to drop.  If `false`, drops all items.  Defaults to `false`.


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
                "kind": "spread",
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
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "desc": "If `True`, drops a random item from the tag. \\\nIf `False`, drops all items in the tag.",
                            "key": "expand",
                            "type": {
                                "kind": "boolean"
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
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
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "desc": "If `True`, randomly selects an item to drop. \\\nIf `False`, drops all items. \\\nDefaults to `False`.",
                            "key": "expand",
                            "type": {
                                "kind": "boolean"
                            },
                            "optional": True
                        }
                    ]
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

