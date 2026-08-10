"""
Generated from symbols.json for ::java::world::component::predicate::AttributeModifiersPredicateEntry
Local link to file: generated_symbols/world/component/predicate/AttributeModifiersPredicateEntry.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds
    from generated_symbols.util.attribute.AttributeOperation import AttributeOperation
    from generated_symbols.util.slot.EquipmentSlotGroup import EquipmentSlotGroup


@dataclass(kw_only=True)
class AttributeModifiersPredicateEntry:
    attribute: Annotated[str, IdSpec(registry='attribute', tags='allowed')] | list[Annotated[str, IdSpec(registry='attribute')]] | None = None
    id: Annotated[str, IdSpec(registry='attribute_modifier')] | None = None
    amount: MinMaxBounds[float] | float | None = None
    operation: AttributeOperation | None = None
    slot: EquipmentSlotGroup | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::predicate::AttributeModifiersPredicateEntry": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "attribute",
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
                                                    "value": "attribute"
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
                                                "value": "attribute"
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
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "amount",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::util::MinMaxBounds"
                    },
                    "typeArgs": [
                        {
                            "kind": "double"
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "operation",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::attribute::AttributeOperation"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "slot",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::slot::EquipmentSlotGroup"
                },
                "optional": True
            }
        ]
    }
}

