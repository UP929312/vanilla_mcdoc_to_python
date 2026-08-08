# Generated from symbols.json for ::java::data::worldgen::attribute::RGBColorAttribute
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Any

from generated_symbols.data.timeline.AttributeTrackBase import AttributeTrackBase

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.attribute.modifier.ColorAttributeModifier import ColorAttributeModifier
    from generated_symbols.data.worldgen.attribute.modifier.ColorModifierType import ColorModifierType
    from generated_symbols.util.color.StringRGB import StringRGB


@dataclass(kw_only=True)
class AttributeTrackStruct(AttributeTrackBase):
    keyframes: Annotated[list[Any], 'Length = 1 (inclusive) and above']
    modifier: ColorModifierType | None = None


@dataclass(kw_only=True)
class RGBColorAttribute:
    value: StringRGB
    modifier: ColorAttributeModifier
    attribute_track: AttributeTrackStruct


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::attribute::RGBColorAttribute": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "value",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::color::StringRGB"
                }
            },
            {
                "kind": "pair",
                "key": "modifier",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::attribute::modifier::ColorAttributeModifier"
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
                                "path": "::java::data::worldgen::attribute::modifier::ColorModifierType"
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
                                                "registry": "minecraft:environment_attribute_color_modifier"
                                            }
                                        }
                                    ]
                                },
                                "lengthRange": {
                                    "kind": 0,
                                    "min": 1
                                }
                            }
                        }
                    ]
                }
            }
        ]
    }
}

