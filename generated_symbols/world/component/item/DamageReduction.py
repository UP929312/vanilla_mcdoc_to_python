# Generated from symbols.json for ::java::world::component::item::DamageReduction
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class DamageReduction:
    base: float  # Constant amount of damage to be blocked.
    factor: float  # Fraction of the dealt damage that should be blocked.
    type: str | list[str] | None = None  # An optional damage type to filter this reduction by. If not specified, any damage type is accepted for this reduction.
    horizontal_blocking_angle: Annotated[float, 'Range | Min `0` and above | inclusive'] | None = None  # Maximum angle between facing direction and incoming attack direction for the blocking to be effective


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::DamageReduction": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "An optional damage type to filter this reduction by.\nIf not specified, any damage type is accepted for this reduction.",
                "key": "type",
                "type": {
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
                                                    "value": "damage_type"
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
                                                "value": "damage_type"
                                            }
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Constant amount of damage to be blocked.",
                "key": "base",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "pair",
                "desc": "Fraction of the dealt damage that should be blocked.",
                "key": "factor",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "pair",
                "desc": "Maximum angle between facing direction and incoming attack direction for the blocking to be effective",
                "key": "horizontal_blocking_angle",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 2,
                        "min": 0
                    }
                },
                "optional": True
            }
        ]
    }
}

