"""
Generated from symbols.json for ::java::data::worldgen::attribute::ListAttribute
Local link to file: generated_symbols/data/worldgen/attribute/ListAttribute.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Generic, TypeVar

from pydantic import Field

from generated_symbols.base import GeneratedModel
from generated_symbols.data.timeline.AttributeTrackBase import AttributeTrackBase

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.attribute.modifier.ListModifier import ListModifier
    from generated_symbols.data.worldgen.attribute.modifier.ListModifierType import ListModifierType


E = TypeVar('E')

class KeyframesStruct(GeneratedModel, Generic[E]):
    ticks: Annotated[int, Field(ge=0)]
    value: list[E]


class AttributeTrackStruct(AttributeTrackBase, Generic[E]):
    modifier: ListModifierType | None = None
    keyframes: Annotated[list[KeyframesStruct[E]], Field(min_length=1)]


class ListAttribute(GeneratedModel, Generic[E]):
    value: list[E]
    modifier: ListModifier[E]
    attribute_track: AttributeTrackStruct[E]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::attribute::ListAttribute": {
        "kind": "template",
        "child": {
            "kind": "struct",
            "fields": [
                {
                    "kind": "pair",
                    "key": "value",
                    "type": {
                        "kind": "list",
                        "item": {
                            "kind": "reference",
                            "path": "::java::data::worldgen::attribute::E"
                        }
                    }
                },
                {
                    "kind": "pair",
                    "key": "modifier",
                    "type": {
                        "kind": "concrete",
                        "child": {
                            "kind": "reference",
                            "path": "::java::data::worldgen::attribute::modifier::ListModifier"
                        },
                        "typeArgs": [
                            {
                                "kind": "reference",
                                "path": "::java::data::worldgen::attribute::E"
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
                                    "path": "::java::data::worldgen::attribute::modifier::ListModifierType"
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
                                                    "kind": "list",
                                                    "item": {
                                                        "kind": "reference",
                                                        "path": "::java::data::worldgen::attribute::E"
                                                    }
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
                "path": "::java::data::worldgen::attribute::E"
            }
        ]
    }
}

