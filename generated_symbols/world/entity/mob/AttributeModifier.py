# Generated from symbols.json for ::java::world::entity::mob::AttributeModifier
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.attribute.AttributeOperation import AttributeOperation


@dataclass(kw_only=True)
class AttributeModifier:
    id: str  # The unique identifier of this attribute modifier.
    amount: float  # Change in the attribute.
    operation: AttributeOperation  # The operation used for this modifier.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::AttributeModifier": {
        "kind": "union",
        "members": [
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "desc": "The unique identifier of this attribute modifier.",
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
                                            "value": "attribute_modifier"
                                        }
                                    }
                                }
                            ]
                        }
                    },
                    {
                        "kind": "pair",
                        "desc": "Change in the attribute.",
                        "key": "amount",
                        "type": {
                            "kind": "double"
                        }
                    },
                    {
                        "kind": "pair",
                        "desc": "The operation used for this modifier.",
                        "key": "operation",
                        "type": {
                            "kind": "reference",
                            "path": "::java::util::attribute::AttributeOperation"
                        }
                    }
                ],
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
                    }
                ]
            },
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "desc": "Has no real effect.",
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
                ],
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21"
                            }
                        }
                    }
                ]
            }
        ]
    }
}

