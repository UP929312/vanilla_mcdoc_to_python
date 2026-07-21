# Generated from symbols.json for ::java::world::entity::mob::ModernAttributeModifier
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.attribute.AttributeOperation import AttributeOperation


@dataclass(kw_only=True)
class ModernAttributeModifier:
    id: str  # The unique identifier of this attribute modifier.
    amount: float  # Change in the attribute.
    operation: AttributeOperation  # The operation used for this modifier.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::ModernAttributeModifier": {
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
    }
}

