"""
Generated from symbols.json for ::java::assets::shader::post::UniformValue
Local link to file: generated_symbols/assets/shader/post/UniformValue.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.assets.shader.post.UniformValueType import UniformValueType


class UniformValue(GeneratedModel):
    name: str | None = None  # Unused by the game, but good to set in practice.
    type: UniformValueType
    value: float | int | tuple[int, int, int] | tuple[float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float] | tuple[float, float] | tuple[float, float, float] | tuple[float, float, float, float]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::shader::post::UniformValue": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.6"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "name",
                            "type": {
                                "kind": "string"
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.6"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "desc": "Unused by the game, but good to set in practice.",
                            "key": "name",
                            "type": {
                                "kind": "string"
                            },
                            "optional": True
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::shader::post::UniformValueType"
                }
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
                                "value": "1.21.6"
                            }
                        }
                    }
                ],
                "key": "values",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "float"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 4
                    }
                }
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
                                "value": "1.21.6"
                            }
                        }
                    }
                ],
                "key": "value",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:uniform_value"
                }
            }
        ]
    }
}
