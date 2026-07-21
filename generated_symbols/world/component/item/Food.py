# Generated from symbols.json for ::java::world::component::item::Food
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class Food:
    nutrition: Annotated[int, 'Range | Min `0` and above | inclusive']  # Food points/haunches restored when eaten (capped to 20.0).
    saturation: float  # Exact value added to the player's saturation level, capped at whatever the [new] food points value is.
    can_always_eat: bool | None = None  # Whether the item can be eaten when the player's food points/haunches are full. Defaults to `false`


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::Food": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Food points/haunches restored when eaten (capped to 20.0).",
                "key": "nutrition",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                }
            },
            {
                "kind": "pair",
                "desc": "Exact value added to the player's saturation level, capped at whatever the [new] food points value is.",
                "key": "saturation",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "pair",
                "desc": "Whether the item can be eaten when the player's food points/haunches are full. Defaults to `False`",
                "key": "can_always_eat",
                "type": {
                    "kind": "boolean"
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
                                "value": "1.21.2"
                            }
                        }
                    }
                ],
                "desc": "Seconds it takes to eat the item. Defaults to `1.6`",
                "key": "eat_seconds",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
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
                                "value": "1.21.2"
                            }
                        }
                    }
                ],
                "desc": "Applied when eaten.",
                "key": "effects",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::world::component::item::FoodEffect"
                    }
                },
                "optional": True
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
                                "value": "1.21"
                            }
                        }
                    },
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
                ],
                "desc": "Works similarly to a milk bucket.",
                "key": "using_converts_to",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::SingleItem"
                },
                "optional": True
            }
        ]
    }
}

