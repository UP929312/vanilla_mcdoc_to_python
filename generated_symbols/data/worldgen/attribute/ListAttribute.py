"""
Generated from symbols.json for ::java::data::worldgen::attribute::ListAttribute
Local link to file: generated_symbols/data/worldgen/attribute/ListAttribute.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Generic, TypeVar

from generated_symbols.data.timeline.AttributeTrackBase import AttributeTrackBase

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.attribute.modifier.ListModifier import ListModifier
    from generated_symbols.data.worldgen.attribute.modifier.ListModifierType import ListModifierType


E = TypeVar('E')

@dataclass(kw_only=True)
class KeyframesStruct(Generic[E]):
    ticks: Annotated[int, 'Range | Min `0` and above | inclusive']
    value: list[E]


@dataclass(kw_only=True)
class AttributeTrackStruct(AttributeTrackBase, Generic[E]):
    keyframes: Annotated[list[KeyframesStruct[E]], 'Length = 1 (inclusive) and above']
    modifier: ListModifierType | None = None


@dataclass(kw_only=True)
class ListAttribute(Generic[E]):
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

