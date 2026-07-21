# Generated from symbols.json for ::java::assets::model::ModelElementRotation
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.model.Axis import Axis


type ModelElementRotation = dict[Axis, float]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::model::ModelElementRotation": {
        "kind": "union",
        "members": [
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "spread",
                        "type": {
                            "kind": "reference",
                            "path": "::java::assets::model::ModelElementRotationBase"
                        }
                    },
                    {
                        "kind": "pair",
                        "key": "axis",
                        "type": {
                            "kind": "reference",
                            "path": "::java::assets::model::Axis"
                        }
                    },
                    {
                        "kind": "pair",
                        "key": "angle",
                        "type": {
                            "kind": "union",
                            "members": [
                                {
                                    "kind": "union",
                                    "members": [
                                        {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "double",
                                                "value": -45
                                            }
                                        },
                                        {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "double",
                                                "value": -22.5
                                            }
                                        },
                                        {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "double",
                                                "value": 0
                                            }
                                        },
                                        {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "double",
                                                "value": 22.5
                                            }
                                        },
                                        {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "double",
                                                "value": 45
                                            }
                                        }
                                    ],
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
                                    ]
                                },
                                {
                                    "kind": "float",
                                    "valueRange": {
                                        "kind": 0,
                                        "min": -45,
                                        "max": 45
                                    },
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
                                        },
                                        {
                                            "name": "until",
                                            "value": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "1.21.11"
                                                }
                                            }
                                        }
                                    ]
                                },
                                {
                                    "kind": "float",
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
                                    ]
                                }
                            ]
                        }
                    }
                ],
                "attributes": [
                    {
                        "name": "deprecated",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.11"
                            }
                        }
                    }
                ]
            },
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "spread",
                        "type": {
                            "kind": "reference",
                            "path": "::java::assets::model::ModelElementRotationBase"
                        }
                    },
                    {
                        "kind": "pair",
                        "key": {
                            "kind": "reference",
                            "path": "::java::assets::model::Axis"
                        },
                        "type": {
                            "kind": "float"
                        },
                        "optional": True
                    }
                ],
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
                ]
            }
        ]
    }
}

