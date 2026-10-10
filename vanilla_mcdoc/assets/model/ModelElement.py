"""
Generated from symbols.json for ::java::assets::model::ModelElement
Local link to file: vanilla_mcdoc/assets/model/ModelElement.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.model.ModelElementRotation import ModelElementRotation
    from vanilla_mcdoc.util.direction.Direction import Direction


class FacesStructValueStruct(GeneratedModel):
    texture: str
    uv: tuple[float, float, float, float] | None = None
    cullface: Direction | None = None
    rotation: Literal[0] | Literal[90] | Literal[180] | Literal[270] | None = None
    tintindex: int | None = None


class ModelElement(GeneratedModel):
    from_: tuple[Annotated[float, Field(ge=-16, le=32)], Annotated[float, Field(ge=-16, le=32)], Annotated[float, Field(ge=-16, le=32)]] = Field(alias='from')
    to: tuple[Annotated[float, Field(ge=-16, le=32)], Annotated[float, Field(ge=-16, le=32)], Annotated[float, Field(ge=-16, le=32)]]
    faces: dict[Direction, FacesStructValueStruct]
    rotation: ModelElementRotation | None = None
    shade_direction_override: Direction | None = None
    light_emission: Annotated[int, Field(ge=0, le=15)] | None = None


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
