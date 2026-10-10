"""
Generated from symbols.json for ::java::world::entity::mob::ModernAttributeModifier
Local link to file: vanilla_mcdoc/world/entity/mob/ModernAttributeModifier.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.util.attribute.AttributeOperation import AttributeOperation


class ModernAttributeModifier(GeneratedModel):
    id: Annotated[str, IdSpec(registry='attribute_modifier')]  # The unique identifier of this attribute modifier.
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
