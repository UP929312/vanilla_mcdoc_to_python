# Generated from symbols.json for ::java::data::worldgen::attribute::BooleanAttribute
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.attribute.modifier.BooleanAttributeModifier import BooleanAttributeModifier


@dataclass(kw_only=True)
class BooleanAttribute:
    value: bool
    modifier: BooleanAttributeModifier
    attribute_track: Any


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
                                }
                            }
                        }
                    ]
                }
            }
        ]
    }
}

