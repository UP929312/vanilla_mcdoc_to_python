# Generated from symbols.json for ::java::data::worldgen::attribute::modifier::BooleanAttributeModifier
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.attribute.modifier.BooleanModifierType import BooleanModifierType


@dataclass(kw_only=True)
class BooleanAttributeModifier:
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

