# Generated from symbols.json for ::java::data::worldgen::attribute::FloatAttribute
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Generic, TypeVar

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.attribute.modifier.FloatAttributeModifier import FloatAttributeModifier


T = TypeVar('T')

@dataclass(kw_only=True)
class FloatAttribute(Generic[T]):
    value: T
    modifier: FloatAttributeModifier[T]
    attribute_track: Any


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::attribute::FloatAttribute": {
        "kind": "template",
        "child": {
            "kind": "struct",
            "fields": [
                {
                    "kind": "pair",
                    "key": "value",
                    "type": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::attribute::T"
                    }
                },
                {
                    "kind": "pair",
                    "key": "modifier",
                    "type": {
                        "kind": "concrete",
                        "child": {
                            "kind": "reference",
                            "path": "::java::data::worldgen::attribute::modifier::FloatAttributeModifier"
                        },
                        "typeArgs": [
                            {
                                "kind": "reference",
                                "path": "::java::data::worldgen::attribute::T"
                            }
                        ]
                    }
                },
                {
                    "kind": "pair",
                    "key": "attribute_track",
                    "type": {
                        "kind": "struct",
                        "fields": [
                            {
                                "kind": "spread",
                                "type": {
                                    "kind": "reference",
                                    "path": "::java::data::timeline::AttributeTrackBase"
                                }
                            },
                            {
                                "kind": "pair",
                                "key": "modifier",
                                "type": {
                                    "kind": "reference",
                                    "path": "::java::data::worldgen::attribute::modifier::FloatModifierType"
                                },
                                "optional": True
                            },
                            {
                                "kind": "pair",
                                "key": "keyframes",
                                "type": {
                                    "kind": "list",
                                    "item": {
                                        "kind": "struct",
                                        "fields": [
                                            {
                                                "kind": "pair",
                                                "key": "ticks",
                                                "type": {
                                                    "kind": "int",
                                                    "valueRange": {
                                                        "kind": 0,
                                                        "min": 0
                                                    }
                                                }
                                            },
                                            {
                                                "kind": "pair",
                                                "key": "value",
                                                "type": {
                                                    "kind": "concrete",
                                                    "child": {
                                                        "kind": "dispatcher",
                                                        "parallelIndices": [
                                                            {
                                                                "kind": "dynamic",
                                                                "accessor": [
                                                                    {
                                                                        "keyword": "parent"
                                                                    },
                                                                    {
                                                                        "keyword": "parent"
                                                                    },
                                                                    "modifier"
                                                                ]
                                                            }
                                                        ],
                                                        "registry": "minecraft:environment_attribute_float_modifier"
                                                    },
                                                    "typeArgs": [
                                                        {
                                                            "kind": "reference",
                                                            "path": "::java::data::worldgen::attribute::T"
                                                        }
                                                    ]
                                                }
                                            }
                                        ]
                                    }
                                }
                            }
                        ]
                    }
                }
            ]
        },
        "typeParams": [
            {
                "path": "::java::data::worldgen::attribute::T"
            }
        ]
    }
}

