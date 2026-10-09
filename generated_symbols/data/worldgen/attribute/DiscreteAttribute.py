"""
Generated from symbols.json for ::java::data::worldgen::attribute::DiscreteAttribute
Local link to file: generated_symbols/data/worldgen/attribute/DiscreteAttribute.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Generic, Literal, TypeVar

from generated_symbols.base import GeneratedModel
from generated_symbols.data.timeline.AttributeTrackBase import AttributeTrackBase
from pydantic import Field

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.attribute.modifier.OverrideModifier import OverrideModifier


T = TypeVar('T')

class KeyframesStruct(GeneratedModel, Generic[T]):
    ticks: Annotated[int, Field(ge=0)]
    value: T


class AttributeTrackStruct(AttributeTrackBase, Generic[T]):
    modifier: Literal['override'] | None = 'override'
    keyframes: Annotated[list[KeyframesStruct[T]], Field(min_length=1)]


class DiscreteAttribute(GeneratedModel, Generic[T]):
    value: T
    modifier: OverrideModifier[T]
    attribute_track: AttributeTrackStruct[T]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::attribute::DiscreteAttribute": {
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
                            "path": "::java::data::worldgen::attribute::modifier::OverrideModifier"
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
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "override"
                                    }
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

