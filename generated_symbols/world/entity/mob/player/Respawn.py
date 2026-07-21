# Generated from symbols.json for ::java::world::entity::mob::player::Respawn
from dataclasses import dataclass


@dataclass(kw_only=True)
class Respawn:
    pos: tuple[int, int, int]  # The block coordinates of the player's respawn point
    yaw: float  # The Y-rotation of the player's respawn point
    pitch: float  # The X-rotation of the player's respawn point
    forced: bool | None = None  # Whether the player must spawn at the respawn point.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::player::Respawn": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The block coordinates of the player's respawn point",
                "key": "pos",
                "type": {
                    "kind": "int_array",
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
                    }
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
                                "value": "1.21.9"
                            }
                        }
                    }
                ],
                "desc": "The Y-rotation of the player's respawn point",
                "key": "angle",
                "type": {
                    "kind": "float"
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
                                "value": "1.21.9"
                            }
                        }
                    }
                ],
                "desc": "The Y-rotation of the player's respawn point",
                "key": "yaw",
                "type": {
                    "kind": "float"
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
                                "value": "1.21.9"
                            }
                        }
                    }
                ],
                "desc": "The X-rotation of the player's respawn point",
                "key": "pitch",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "struct",
                            "fields": [
                                {
                                    "kind": "pair",
                                    "desc": "Dimension of the player's respawn point. Defaults to overworld.",
                                    "key": "dimension",
                                    "type": {
                                        "kind": "string",
                                        "attributes": [
                                            {
                                                "name": "id",
                                                "value": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "string",
                                                        "value": "dimension"
                                                    }
                                                }
                                            }
                                        ]
                                    },
                                    "optional": True
                                }
                            ],
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21.9"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "struct",
                            "fields": [
                                {
                                    "kind": "pair",
                                    "desc": "Dimension of the player's respawn point. Defaults to overworl.",
                                    "key": "dimension",
                                    "type": {
                                        "kind": "string",
                                        "attributes": [
                                            {
                                                "name": "id",
                                                "value": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "string",
                                                        "value": "dimension"
                                                    }
                                                }
                                            }
                                        ]
                                    }
                                }
                            ],
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21.9"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "Whether the player must spawn at the respawn point.",
                "key": "forced",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

