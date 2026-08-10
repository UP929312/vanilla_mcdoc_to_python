"""
Generated from symbols.json for ::java::util::registry_ref::BlockListRef
Local link to file: generated_symbols/util/registry_ref/BlockListRef.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from runtime_metadata import IdSpec


type BlockListRef = Annotated[str, IdSpec(registry='block', tags='allowed')] | list[Annotated[str, IdSpec(registry='block')]]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::registry_ref::BlockListRef": {
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
                                        "value": "block"
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
                                    "value": "block"
                                }
                            }
                        }
                    ]
                }
            }
        ]
    }
}

