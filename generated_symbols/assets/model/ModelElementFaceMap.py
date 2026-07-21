# Generated from symbols.json for ::java::assets::model::ModelElementFaceMap
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from generated_symbols.util.direction.Direction import Direction


type ModelElementFaceMap = dict[Direction, Any]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::model::ModelElementFaceMap": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
                    "kind": "reference",
                    "path": "::java::util::direction::Direction"
                },
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "texture",
                            "type": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "texture_slot",
                                        "value": {
                                            "kind": "tree",
                                            "values": {
                                                "kind": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "string",
                                                        "value": "reference"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                ]
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "uv",
                            "type": {
                                "kind": "list",
                                "item": {
                                    "kind": "float"
                                },
                                "lengthRange": {
                                    "kind": 0,
                                    "min": 4,
                                    "max": 4
                                }
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "cullface",
                            "type": {
                                "kind": "reference",
                                "path": "::java::util::direction::Direction"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "rotation",
                            "type": {
                                "kind": "union",
                                "members": [
                                    {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "int",
                                            "value": 0
                                        }
                                    },
                                    {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "int",
                                            "value": 90
                                        }
                                    },
                                    {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "int",
                                            "value": 180
                                        }
                                    },
                                    {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "int",
                                            "value": 270
                                        }
                                    }
                                ]
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "tintindex",
                            "type": {
                                "kind": "int"
                            },
                            "optional": True
                        }
                    ]
                }
            }
        ]
    }
}

