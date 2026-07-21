# Generated from symbols.json for ::java::util::effect::OldMobEffect
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.util.effect.EffectId import EffectId
    from generated_symbols.util.effect.MobEffectInstance import MobEffectInstance


@dataclass(kw_only=True)
class OldMobEffect:
    Id: EffectId | None = None
    Amplifier: int | Annotated[int, 'Range | `0`-`255` | both inclusive'] | None = None
    Duration: Annotated[int, 'Range | Min `1` and above | inclusive'] | int | None = None  # Duration of the effect in ticks. Infinite is represented by `-1`.
    Ambient: bool | None = None  # Whether particles are semi-transparent. (like with a Beacon)
    ShowParticles: bool | None = None  # Whether particles should be shown.
    ShowIcon: bool | None = None  # Whether the effect icon should be shown.
    HiddenEffect: MobEffectInstance | None = None  # A lower amplifier effect of the same type.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::effect::OldMobEffect": {
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
    }
}

