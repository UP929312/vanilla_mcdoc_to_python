# Generated from symbols.json for ::java::assets::model::Model
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from generated_symbols.assets.model.CustomizableItemDisplayContext import CustomizableItemDisplayContext
    from generated_symbols.assets.model.ModelElement import ModelElement
    from generated_symbols.assets.model.TextureMaterial import TextureMaterial


@dataclass(kw_only=True)
class Model:
    parent: str | None = None
    ambientocclusion: bool | None = None
    gui_light: str | None = None
    textures: dict[str, str | TextureMaterial] | None = None
    elements: list[ModelElement] | None = None
    display: dict[CustomizableItemDisplayContext, Any] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::model::Model": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "parent",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "model"
                                }
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "ambientocclusion",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "gui_light",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "front"
                            }
                        },
                        {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "side"
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "textures",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": {
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
                                                        "value": "definition"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                ]
                            },
                            "type": {
                                "kind": "union",
                                "members": [
                                    {
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
                                                                "value": "value"
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        ]
                                    },
                                    {
                                        "kind": "reference",
                                        "path": "::java::assets::model::TextureMaterial",
                                        "attributes": [
                                            {
                                                "name": "since",
                                                "value": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "string",
                                                        "value": "26.1"
                                                    }
                                                }
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "elements",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::assets::model::ModelElement"
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "display",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": {
                                "kind": "reference",
                                "path": "::java::assets::model::CustomizableItemDisplayContext"
                            },
                            "type": {
                                "kind": "struct",
                                "fields": [
                                    {
                                        "kind": "pair",
                                        "key": "rotation",
                                        "type": {
                                            "kind": "list",
                                            "item": {
                                                "kind": "float"
                                            },
                                            "lengthRange": {
                                                "kind": 0,
                                                "min": 3,
                                                "max": 3
                                            }
                                        },
                                        "optional": True
                                    },
                                    {
                                        "kind": "pair",
                                        "key": "translation",
                                        "type": {
                                            "kind": "list",
                                            "item": {
                                                "kind": "float",
                                                "valueRange": {
                                                    "kind": 0,
                                                    "min": -80,
                                                    "max": 80
                                                }
                                            },
                                            "lengthRange": {
                                                "kind": 0,
                                                "min": 3,
                                                "max": 3
                                            }
                                        },
                                        "optional": True
                                    },
                                    {
                                        "kind": "pair",
                                        "key": "scale",
                                        "type": {
                                            "kind": "list",
                                            "item": {
                                                "kind": "float",
                                                "valueRange": {
                                                    "kind": 0,
                                                    "min": -4,
                                                    "max": 4
                                                }
                                            },
                                            "lengthRange": {
                                                "kind": 0,
                                                "min": 3,
                                                "max": 3
                                            }
                                        },
                                        "optional": True
                                    }
                                ]
                            }
                        }
                    ]
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
                                "value": "1.21.4"
                            }
                        }
                    }
                ],
                "key": "overrides",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "struct",
                        "fields": [
                            {
                                "kind": "pair",
                                "key": "predicate",
                                "type": {
                                    "kind": "struct",
                                    "fields": [
                                        {
                                            "kind": "pair",
                                            "key": {
                                                "kind": "reference",
                                                "path": "::java::assets::model::Predicates"
                                            },
                                            "type": {
                                                "kind": "float"
                                            }
                                        }
                                    ]
                                }
                            },
                            {
                                "kind": "pair",
                                "key": "model",
                                "type": {
                                    "kind": "reference",
                                    "path": "::java::assets::model::ModelRef"
                                }
                            }
                        ]
                    }
                },
                "optional": True
            }
        ]
    }
}

