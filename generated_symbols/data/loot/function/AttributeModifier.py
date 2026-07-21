# Generated from symbols.json for ::java::data::loot::function::AttributeModifier
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.NumberProviderRef import NumberProviderRef
    from generated_symbols.util.attribute.AttributeOperation import AttributeOperation
    from generated_symbols.util.slot.EquipmentSlotGroup import EquipmentSlotGroup


@dataclass(kw_only=True)
class AttributeModifier:
    attribute: str  # Attribute type to modify.
    id: str  # The unique identifier of this attribute modifier.
    amount: NumberProviderRef
    operation: AttributeOperation  # The operation used for this modifier.
    slot: EquipmentSlotGroup | list[EquipmentSlotGroup]  # If a list, one of the listed slots will be chosen randomly.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::AttributeModifier": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Attribute type to modify.",
                "key": "attribute",
                "type": {
                    "kind": "string",
                    "attributes": [
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
                                "value": "1.21"
                            }
                        }
                    }
                ],
                "key": "name",
                "type": {
                    "kind": "string"
                }
            },
            {
                "kind": "spread",
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
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "id",
                            "type": {
                                "kind": "string",
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
            },
            {
                "kind": "spread",
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
                ],
                "type": {
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
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "amount",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::data::util::RandomValueBounds",
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
                            "kind": "reference",
                            "path": "::java::data::number_provider::NumberProviderRef",
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
                }
            },
            {
                "kind": "pair",
                "desc": "The operation used for this modifier.",
                "key": "operation",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "union",
                            "members": [
                                {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "addition"
                                    }
                                },
                                {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "multiply_base"
                                    }
                                },
                                {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "multiply_total"
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
                                            "value": "1.20.5"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "reference",
                            "path": "::java::util::attribute::AttributeOperation",
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
                            ]
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "If a list, one of the listed slots will be chosen randomly.",
                "key": "slot",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::util::slot::EquipmentSlotGroup"
                        },
                        {
                            "kind": "list",
                            "item": {
                                "kind": "reference",
                                "path": "::java::util::slot::EquipmentSlotGroup"
                            }
                        }
                    ]
                }
            }
        ]
    }
}

