# Generated from symbols.json for ::java::world::item::AttributeModifier
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.attribute.LegacyOperation import LegacyOperation
    from generated_symbols.util.slot.EquipmentSlotGroup import EquipmentSlotGroup


@dataclass(kw_only=True)
class AttributeModifier:
    AttributeName: str | None = None
    Name: str | None = None  # Identifying name of the modifier, has no real effect.
    Slot: EquipmentSlotGroup | None = None  # Slot that the modifier is active in.
    Operation: LegacyOperation | None = None
    Amount: float | None = None  # Change in the attribute.
    UUID: tuple[int, int, int, int] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::AttributeModifier": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "AttributeName",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "union",
                            "members": [
                                {
                                    "kind": "reference",
                                    "path": "::java::util::attribute::AttributeName"
                                },
                                {
                                    "kind": "string"
                                }
                            ],
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.16"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.16"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "attribute"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Identifying name of the modifier, has no real effect.",
                "key": "Name",
                "type": {
                    "kind": "string"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Slot that the modifier is active in.",
                "key": "Slot",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::slot::EquipmentSlotGroup"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "Operation",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::attribute::LegacyOperation"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Change in the attribute.",
                "key": "Amount",
                "type": {
                    "kind": "double"
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
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "desc": "Upper bits of the modifier's UUID.",
                "key": "UUIDMost",
                "type": {
                    "kind": "long"
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
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "desc": "Lower bits of the modifier's UUID.",
                "key": "UUIDLeast",
                "type": {
                    "kind": "long"
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
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "key": "UUID",
                "type": {
                    "kind": "int_array",
                    "lengthRange": {
                        "kind": 0,
                        "min": 4,
                        "max": 4
                    },
                    "attributes": [
                        {
                            "name": "uuid"
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

