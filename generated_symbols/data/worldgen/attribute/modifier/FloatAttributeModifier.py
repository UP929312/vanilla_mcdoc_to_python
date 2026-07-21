# Generated from symbols.json for ::java::data::worldgen::attribute::modifier::FloatAttributeModifier
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Generic, TypeVar

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.attribute.modifier.FloatModifierType import FloatModifierType


T = TypeVar('T')

@dataclass(kw_only=True)
class FloatAttributeModifier(Generic[T]):
    modifier: FloatModifierType
    argument: Any[T]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::attribute::modifier::FloatAttributeModifier": {
        "kind": "template",
        "child": {
            "kind": "struct",
            "fields": [
                {
                    "kind": "pair",
                    "key": "modifier",
                    "type": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::attribute::modifier::FloatModifierType"
                    }
                },
                {
                    "kind": "pair",
                    "key": "argument",
                    "type": {
                        "kind": "concrete",
                        "child": {
                            "kind": "dispatcher",
                            "parallelIndices": [
                                {
                                    "kind": "dynamic",
                                    "accessor": [
                                        "modifier"
                                    ]
                                }
                            ],
                            "registry": "minecraft:environment_attribute_float_modifier"
                        },
                        "typeArgs": [
                            {
                                "kind": "reference",
                                "path": "::java::data::worldgen::attribute::modifier::T"
                            }
                        ]
                    }
                }
            ]
        },
        "typeParams": [
            {
                "path": "::java::data::worldgen::attribute::modifier::T"
            }
        ]
    }
}

