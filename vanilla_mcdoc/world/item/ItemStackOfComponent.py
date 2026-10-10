"""
Generated from symbols.json for ::java::world::item::ItemStackOfComponent
Local link to file: vanilla_mcdoc/world/item/ItemStackOfComponent.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Generic, TypeVar

from pydantic import Field

from vanilla_mcdoc.world.item.SingleItemOfComponent import SingleItemOfComponent


T = TypeVar('T')


class ItemStackOfComponent(SingleItemOfComponent[T], Generic[T]):
    count: Annotated[int, Field(ge=1, le=99)] | None = None  # Number of items in the stack. Defaults to `1`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::ItemStackOfComponent": {
        "kind": "template",
        "child": {
            "kind": "struct",
            "fields": [
                {
                    "kind": "spread",
                    "type": {
                        "kind": "concrete",
                        "child": {
                            "kind": "reference",
                            "path": "::java::world::item::SingleItemOfComponent"
                        },
                        "typeArgs": [
                            {
                                "kind": "reference",
                                "path": "::java::world::item::T"
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
                                    "value": "1.20.5"
                                }
                            }
                        }
                    ],
                    "desc": "Number of items in the stack.\nDefaults to `1`.",
                    "key": "count",
                    "type": {
                        "kind": "int",
                        "valueRange": {
                            "kind": 0,
                            "min": 1,
                            "max": 99
                        }
                    },
                    "optional": True
                },
                {
                    "kind": "pair",
                    "attributes": [
                        {
                            "name": "until",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "1.20.5"
                                }
                            }
                        }
                    ],
                    "desc": "Number of items in the stack.",
                    "key": "Count",
                    "type": {
                        "kind": "byte"
                    },
                    "optional": True
                }
            ]
        },
        "typeParams": [
            {
                "path": "::java::world::item::T"
            }
        ]
    }
}
