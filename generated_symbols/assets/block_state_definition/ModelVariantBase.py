# Generated from symbols.json for ::java::assets::block_state_definition::ModelVariantBase
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from generated_symbols.assets.model.ModelRef import ModelRef


@dataclass(kw_only=True)
class ModelVariantBase:
    model: ModelRef
    x: Literal[0] | Literal[90] | Literal[180] | Literal[270] | None = None
    y: Literal[0] | Literal[90] | Literal[180] | Literal[270] | None = None
    z: Literal[0] | Literal[90] | Literal[180] | Literal[270] | None = None
    uvlock: bool | None = None  # If set to `true`, the textures are not rotated with the block.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::block_state_definition::ModelVariantBase": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "model",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::model::ModelRef"
                }
            },
            {
                "kind": "pair",
                "key": "x",
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
                "key": "y",
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
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "key": "z",
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
                "desc": "If set to `True`, the textures are not rotated with the block.",
                "key": "uvlock",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

