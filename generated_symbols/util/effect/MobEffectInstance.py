# Generated from symbols.json for ::java::util::effect::MobEffectInstance
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class MobEffectInstance:
    id: str
    amplifier: int | Annotated[int, 'Range | `0`-`255` | both inclusive'] | None = None  # Level I having value 0. Defaults to 0.
    duration: int | Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # Duration of the effect in ticks. Infinite is represented by `-1`.
    ambient: bool | None = None  # Whether the effect appears as a HUD icon in addition to in the inventory GUI (same behavior as beacons when `true`). Defaults to `false`.
    show_particles: bool | None = None  # Defaults to `true`.
    show_icon: bool | None = None  # Whether the effect appears in the inventory GUI. Defaults to `true`
    hidden_effect: MobEffectInstance | None = None  # A lower amplifier effect of the same type.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::effect::MobEffectInstance": {
        "kind": "union",
        "members": [
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "key": "Id",
                        "type": {
                            "kind": "reference",
                            "path": "::java::util::effect::EffectId"
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "key": "Amplifier",
                        "type": {
                            "kind": "union",
                            "members": [
                                {
                                    "kind": "byte",
                                    "attributes": [
                                        {
                                            "name": "canonical"
                                        }
                                    ]
                                },
                                {
                                    "kind": "int",
                                    "valueRange": {
                                        "kind": 0,
                                        "min": 0,
                                        "max": 255
                                    }
                                }
                            ]
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "desc": "Duration of the effect in ticks. Infinite is represented by `-1`.",
                        "key": "Duration",
                        "type": {
                            "kind": "union",
                            "members": [
                                {
                                    "kind": "int",
                                    "valueRange": {
                                        "kind": 0,
                                        "min": 1
                                    }
                                },
                                {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "int",
                                        "value": -1
                                    },
                                    "attributes": [
                                        {
                                            "name": "since",
                                            "value": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "1.19.4"
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
                        "desc": "Whether particles are semi-transparent. (like with a Beacon)",
                        "key": "Ambient",
                        "type": {
                            "kind": "boolean"
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "desc": "Whether particles should be shown.",
                        "key": "ShowParticles",
                        "type": {
                            "kind": "boolean"
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "desc": "Whether the effect icon should be shown.",
                        "key": "ShowIcon",
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
                                        "value": "1.16"
                                    }
                                }
                            }
                        ],
                        "desc": "A lower amplifier effect of the same type.",
                        "key": "HiddenEffect",
                        "type": {
                            "kind": "reference",
                            "path": "::java::util::effect::MobEffectInstance"
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
                                "value": "1.20.2"
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
                        "key": "id",
                        "type": {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "mob_effect"
                                        }
                                    }
                                }
                            ]
                        }
                    },
                    {
                        "kind": "pair",
                        "desc": "Level I having value 0. Defaults to 0.",
                        "key": "amplifier",
                        "type": {
                            "kind": "union",
                            "members": [
                                {
                                    "kind": "byte",
                                    "attributes": [
                                        {
                                            "name": "canonical"
                                        }
                                    ]
                                },
                                {
                                    "kind": "int",
                                    "valueRange": {
                                        "kind": 0,
                                        "min": 0,
                                        "max": 255
                                    }
                                }
                            ]
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "desc": "Duration of the effect in ticks. Infinite is represented by `-1`.",
                        "key": "duration",
                        "type": {
                            "kind": "union",
                            "members": [
                                {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "int",
                                        "value": -1
                                    }
                                },
                                {
                                    "kind": "int",
                                    "valueRange": {
                                        "kind": 0,
                                        "min": 1
                                    }
                                }
                            ]
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "desc": "Whether the effect appears as a HUD icon in addition to in the inventory GUI (same behavior as beacons when `True`). Defaults to `False`.",
                        "key": "ambient",
                        "type": {
                            "kind": "boolean"
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "desc": "Defaults to `True`.",
                        "key": "show_particles",
                        "type": {
                            "kind": "boolean"
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "desc": "Whether the effect appears in the inventory GUI. Defaults to `True`",
                        "key": "show_icon",
                        "type": {
                            "kind": "boolean"
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "desc": "A lower amplifier effect of the same type.",
                        "key": "hidden_effect",
                        "type": {
                            "kind": "reference",
                            "path": "::java::util::effect::MobEffectInstance"
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
                                "value": "1.20.2"
                            }
                        }
                    }
                ]
            }
        ]
    }
}

