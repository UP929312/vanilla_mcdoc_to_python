"""
Generated from symbols.json for ::java::data::worldgen::attribute::modifier::BooleanAttributeModifier
Local link to file: vanilla_mcdoc/data/worldgen/attribute/modifier/BooleanAttributeModifier.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.attribute.modifier.BooleanModifierType import BooleanModifierType


class BooleanAttributeModifier(GeneratedModel):
    modifier: BooleanModifierType
    argument: bool


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::attribute::modifier::BooleanAttributeModifier": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "modifier",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::attribute::modifier::BooleanModifierType"
                }
            },
            {
                "kind": "pair",
                "key": "argument",
                "type": {
                    "kind": "boolean"
                }
            }
        ]
    }
}
