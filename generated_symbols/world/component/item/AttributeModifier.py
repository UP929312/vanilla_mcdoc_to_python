# Generated from symbols.json for ::java::world::component::item::AttributeModifier
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.attribute.AttributeOperation import AttributeOperation
    from generated_symbols.util.slot.EquipmentSlotGroup import EquipmentSlotGroup
    from generated_symbols.world.component.item.AttributeDisplay import AttributeDisplay


@dataclass(kw_only=True)
class AttributeModifier:
    type: str
    id: str  # Used when equipping and unequipping the item to identify which modifier to add or remove from the entity.
    amount: float  # Change in the attribute.
    operation: AttributeOperation
    slot: EquipmentSlotGroup | None = None  # Slot or slot type the item must be in for the modifier to take effect. Defaults to `any`.
    display: AttributeDisplay | None = None  # Controls how this modifier is shown in the item tooltip.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::AttributeModifier": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
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
                "key": "uuid",
                "type": {
                    "kind": "int_array",
                    "lengthRange": {
                        "kind": 0,
                        "min": 4,
                        "max": 4
                    }
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
                    }
                ],
                "desc": "Used when equipping and unequipping the item to identify which modifier to add or remove from the entity.",
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
                "key": "operation",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::attribute::AttributeOperation"
                }
            },
            {
                "kind": "pair",
                "desc": "Slot or slot type the item must be in for the modifier to take effect. Defaults to `any`.",
                "key": "slot",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::slot::EquipmentSlotGroup"
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
                                "value": "1.21.6"
                            }
                        }
                    }
                ],
                "desc": "Controls how this modifier is shown in the item tooltip.",
                "key": "display",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::item::AttributeDisplay"
                },
                "optional": True
            }
        ]
    }
}

