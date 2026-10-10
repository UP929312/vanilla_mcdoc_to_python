"""
Generated from symbols.json for ::java::data::worldgen::attribute::ARGBColorAttribute
Local link to file: vanilla_mcdoc/data/worldgen/attribute/ARGBColorAttribute.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.data.timeline.AttributeTrackBase import AttributeTrackBase

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.attribute.modifier.BlendToGray import BlendToGray
    from vanilla_mcdoc.data.worldgen.attribute.modifier.ColorModifierType import ColorModifierType
    from vanilla_mcdoc.data.worldgen.attribute.modifier.TranslucentColorAttributeModifier import TranslucentColorAttributeModifier
    from vanilla_mcdoc.util.color.StringARGB import StringARGB
    from vanilla_mcdoc.util.color.StringRGB import StringRGB


class KeyframesStruct(GeneratedModel):
    ticks: Annotated[int, Field(ge=0)]
    value: StringARGB | StringRGB | BlendToGray | StringRGB | StringARGB


class AttributeTrackStruct(AttributeTrackBase):
    modifier: ColorModifierType | None = None
    keyframes: Annotated[list[KeyframesStruct], Field(min_length=1)]


class ARGBColorAttribute(GeneratedModel):
    value: StringARGB
    modifier: TranslucentColorAttributeModifier
    attribute_track: AttributeTrackStruct


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::attribute::ARGBColorAttribute": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "value",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::color::StringARGB"
                }
            },
            {
                "kind": "pair",
                "key": "modifier",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::attribute::modifier::TranslucentColorAttributeModifier"
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
                                                "registry": "minecraft:environment_attribute_argb_color_modifier"
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
