# Generated from symbols.json for ::java::util::registry_ref::ItemListRef
from typing import Annotated

from runtime_metadata import IdSpec


type ItemListRef = Annotated[str, IdSpec(registry='item', tags='allowed')] | list[Annotated[str, IdSpec(registry='item')]]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::registry_ref::ItemListRef": {
        "kind": "union",
        "members": [
            {
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
                                        "value": "allowed"
                                    }
                                }
                            }
                        }
                    }
                ]
            },
            {
                "kind": "list",
                "item": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "item"
                                }
                            }
                        }
                    ]
                }
            }
        ]
    }
}

