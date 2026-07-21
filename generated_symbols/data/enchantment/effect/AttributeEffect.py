# Generated from symbols.json for ::java::data::enchantment::effect::AttributeEffect
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.LevelBasedValue import LevelBasedValue
    from generated_symbols.util.attribute.AttributeOperation import AttributeOperation


@dataclass(kw_only=True)
class AttributeEffect:
    attribute: str
    id: str  # Used when equipping and unequipping the item to identify which modifier to add or remove from the entity.  Postfixed with the slot name when the enchanted item is equipped.
    amount: LevelBasedValue  # Change in the attribute.
    operation: AttributeOperation  # The attribute operation to use.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect::AttributeEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
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
                "desc": "Used when equipping and unequipping the item to identify which modifier to add or remove from the entity.\n\nPostfixed with the slot name when the enchanted item is equipped.",
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
                    "kind": "reference",
                    "path": "::java::data::enchantment::LevelBasedValue"
                }
            },
            {
                "kind": "pair",
                "desc": "The attribute operation to use.",
                "key": "operation",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::attribute::AttributeOperation"
                }
            }
        ]
    }
}

