# Generated from symbols.json for ::java::world::item::Enchantment
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class Enchantment:
    id: str | None = None  # Which enchantment is being described.
    lvl: Annotated[int, 'Range | `0`-`255` | both inclusive'] | None = None  # Which level the enchantment is.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::Enchantment": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Which enchantment is being described.",
                "key": "id",
                "type": {
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
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Which level the enchantment is.",
                "key": "lvl",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "union",
                            "members": [
                                {
                                    "kind": "short",
                                    "valueRange": {
                                        "kind": 0,
                                        "min": 1
                                    }
                                },
                                {
                                    "kind": "int",
                                    "valueRange": {
                                        "kind": 0,
                                        "min": 1
                                    }
                                }
                            ],
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.17"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "short",
                            "valueRange": {
                                "kind": 0,
                                "min": 0,
                                "max": 255
                            },
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.17"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

