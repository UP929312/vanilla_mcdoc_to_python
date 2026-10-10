"""
Generated from symbols.json for ::java::data::worldgen::carver::CarverConfigBase
Local link to file: generated_symbols/data/worldgen/carver/CarverConfigBase.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.HeightProvider import HeightProvider


class CarverConfigBase(GeneratedModel):
    probability: Annotated[float, Field(ge=0, le=1)]
    y: HeightProvider


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::carver::CarverConfigBase": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "probability",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
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
                                "value": "1.19"
                            }
                        }
                    },
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
                "key": "replaceable",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "list",
                            "item": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "id",
                                        "value": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "block"
                                            }
                                        }
                                    }
                                ]
                            }
                        },
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "tree",
                                        "values": {
                                            "registry": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "block"
                                                }
                                            },
                                            "tags": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "allowed"
                                                }
                                            }
                                        }
                                    }
                                }
                            ]
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
                                "value": "1.17"
                            }
                        }
                    }
                ],
                "key": "y",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::HeightProvider"
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
                                "value": "1.17"
                            }
                        }
                    },
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
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "yScale",
                            "type": {
                                "kind": "concrete",
                                "child": {
                                    "kind": "reference",
                                    "path": "::java::data::worldgen::FloatProvider"
                                },
                                "typeArgs": [
                                    {
                                        "kind": "float"
                                    }
                                ]
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "lava_level",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::VerticalAnchor"
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
                                            "value": "1.18"
                                        }
                                    }
                                }
                            ],
                            "key": "aquifers_enabled",
                            "type": {
                                "kind": "boolean"
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "debug_settings",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::carver::CarverDebugSettings"
                            },
                            "optional": True
                        }
                    ]
                }
            }
        ]
    }
}
