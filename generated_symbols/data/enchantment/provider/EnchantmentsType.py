# Generated from symbols.json for ::java::data::enchantment::provider::EnchantmentsType
from typing import Annotated


type EnchantmentsType = str | Annotated[list[str], 'Length = 1 (inclusive) and above']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::provider::EnchantmentsType": {
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
                                        "value": "enchantment"
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
                                    "value": "enchantment"
                                }
                            }
                        }
                    ]
                },
                "lengthRange": {
                    "kind": 0,
                    "min": 1
                }
            }
        ]
    }
}

