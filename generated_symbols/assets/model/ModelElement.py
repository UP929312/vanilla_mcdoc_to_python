# Generated from symbols.json for ::java::assets::model::ModelElement
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Any

if TYPE_CHECKING:
    from generated_symbols.assets.model.ModelElementRotation import ModelElementRotation
    from generated_symbols.util.direction.Direction import Direction


@dataclass(kw_only=True)
class ModelElement:
    from_: tuple[Annotated[float, 'Range | `-16`-`32` | both inclusive'], Annotated[float, 'Range | `-16`-`32` | both inclusive'], Annotated[float, 'Range | `-16`-`32` | both inclusive']]
    to: tuple[Annotated[float, 'Range | `-16`-`32` | both inclusive'], Annotated[float, 'Range | `-16`-`32` | both inclusive'], Annotated[float, 'Range | `-16`-`32` | both inclusive']]
    faces: dict[Direction, Any]
    rotation: ModelElementRotation | None = None
    shade_direction_override: Direction | None = None
    light_emission: Annotated[int, 'Range | `0`-`15` | both inclusive'] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::model::ModelElement": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "from",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "float",
                        "valueRange": {
                            "kind": 0,
                            "min": -16,
                            "max": 32
                        }
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
                    }
                }
            },
            {
                "kind": "pair",
                "key": "to",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "float",
                        "valueRange": {
                            "kind": 0,
                            "min": -16,
                            "max": 32
                        }
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
                    }
                }
            },
            {
                "kind": "pair",
                "key": "faces",
                "type": {
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
            },
            {
                "kind": "pair",
                "key": "rotation",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::model::ModelElementRotation"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "shade",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "shade_direction_override",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::direction::Direction"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.2"
                            }
                        }
                    }
                ],
                "key": "light_emission",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 15
                    }
                },
                "optional": True
            }
        ]
    }
}

