# Generated from symbols.json for ::java::data::worldgen::attribute::MergeableAttribute
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Generic, TypeVar

from generated_symbols.data.timeline.AttributeTrackBase import AttributeTrackBase

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.attribute.modifier.MergeableModifier import MergeableModifier
    from generated_symbols.data.worldgen.attribute.modifier.MergeableModifierType import MergeableModifierType


T = TypeVar('T')

@dataclass(kw_only=True)
class KeyframesStruct(Generic[T]):
    ticks: Annotated[int, 'Range | Min `0` and above | inclusive']
    value: T


@dataclass(kw_only=True)
class AttributeTrackStruct(AttributeTrackBase, Generic[T]):
    keyframes: Annotated[list[KeyframesStruct[T]], 'Length = 1 (inclusive) and above']
    modifier: MergeableModifierType | None = None


@dataclass(kw_only=True)
class MergeableAttribute(Generic[T]):
    value: T
    modifier: MergeableModifier[T]
    attribute_track: AttributeTrackStruct[T]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::attribute::MergeableAttribute": {
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
                            "path": "::java::data::worldgen::attribute::modifier::MergeableModifier"
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
                                    "path": "::java::data::worldgen::attribute::modifier::MergeableModifierType"
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
                                                    "kind": "reference",
                                                    "path": "::java::data::worldgen::attribute::T"
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
        },
        "typeParams": [
            {
                "path": "::java::data::worldgen::attribute::T"
            }
        ]
    }
}

