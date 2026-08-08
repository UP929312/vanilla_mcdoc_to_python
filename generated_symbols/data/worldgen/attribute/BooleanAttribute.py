# Generated from symbols.json for ::java::data::worldgen::attribute::BooleanAttribute
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

from generated_symbols.data.timeline.AttributeTrackBase import AttributeTrackBase

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.attribute.modifier.BooleanAttributeModifier import BooleanAttributeModifier
    from generated_symbols.data.worldgen.attribute.modifier.BooleanModifierType import BooleanModifierType


@dataclass(kw_only=True)
class KeyframesStruct:
    ticks: Annotated[int, 'Range | Min `0` and above | inclusive']
    value: bool


@dataclass(kw_only=True)
class AttributeTrackStruct(AttributeTrackBase):
    keyframes: Annotated[list[KeyframesStruct], 'Length = 1 (inclusive) and above']
    modifier: BooleanModifierType | None = None


@dataclass(kw_only=True)
class BooleanAttribute:
    value: bool
    modifier: BooleanAttributeModifier
    attribute_track: AttributeTrackStruct


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::attribute::BooleanAttribute": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "value",
                "type": {
                    "kind": "boolean"
                }
            },
            {
                "kind": "pair",
                "key": "modifier",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::attribute::modifier::BooleanAttributeModifier"
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
                                "path": "::java::data::worldgen::attribute::modifier::BooleanModifierType"
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
                                                "kind": "boolean"
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

