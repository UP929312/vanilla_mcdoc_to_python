# Generated from symbols.json for ::java::world::item::ItemStackOfComponent
from dataclasses import dataclass
from typing import Annotated, Generic, TypeVar
from generated_symbols.world.item.SingleItemOfComponent import SingleItemOfComponent


T = TypeVar('T')

@dataclass(kw_only=True)
class ItemStackOfComponent(SingleItemOfComponent[T], Generic[T]):
    count: Annotated[int, 'Range | `1`-`99` | both inclusive'] | None = None  # Number of items in the stack. Defaults to `1`.


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

