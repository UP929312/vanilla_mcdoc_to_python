# Generated from symbols.json for ::java::data::worldgen::attribute::ListAttribute
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Generic, TypeVar

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.attribute.modifier.ListModifier import ListModifier


E = TypeVar('E')

@dataclass(kw_only=True)
class ListAttribute(Generic[E]):
    value: list[E]
    modifier: ListModifier[E]
    attribute_track: Any


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

