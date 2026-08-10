"""
Generated from symbols.json for ::java::data::recipe::IngredientValue
Local link to file: generated_symbols/data/recipe/IngredientValue.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from runtime_metadata import IdSpec


@dataclass(kw_only=True)
class IngredientValueStruct1:
    item: Annotated[str, IdSpec(registry='item')]


@dataclass(kw_only=True)
class IngredientValueStruct2:
    tag: Annotated[str, IdSpec(registry='item', tags='implicit')]


type IngredientValue = IngredientValueStruct1 | IngredientValueStruct2


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::recipe::IngredientValue": {
        "kind": "union",
        "members": [
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "key": "item",
                        "type": {
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
            },
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "key": "tag",
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
                    }
                ]
            }
        ],
        "attributes": [
            {
                "name": "until",
                "value": {
                    "kind": "literal",
                    "value": {
                        "kind": "string",
                        "value": "1.21.2"
                    }
                }
            }
        ]
    }
}

