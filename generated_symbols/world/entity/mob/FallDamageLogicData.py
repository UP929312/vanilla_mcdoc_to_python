# Generated from symbols.json for ::java::world::entity::mob::FallDamageLogicData
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class FallDamageLogicData:
    current_explosion_impact_pos: tuple[float, float, float] | None = None  # Added mid-air after being hit by an explosion.
    current_impulse_context_reset_grace_time: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # Used by fall damage logic. Decreases by 1 every tick.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::FallDamageLogicData": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.20.3"
                            }
                        }
                    }
                ],
                "desc": "Added mid-air after being hit by an explosion.",
                "key": "current_explosion_impact_pos",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "double"
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
                "kind": "spread",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21"
                            }
                        }
                    },
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "desc": "Used by fall damage logic. Decreases by 1 every tick.",
                            "key": "current_impulse_context_reset_grace_time",
                            "type": {
                                "kind": "int",
                                "valueRange": {
                                    "kind": 0,
                                    "min": 0
                                }
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
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "desc": "Used by fall damage logic. Decreases by 1 every tick.",
                            "key": "current_impulse_context_reset_grace_time",
                            "type": {
                                "kind": "int",
                                "valueRange": {
                                    "kind": 0,
                                    "min": 0
                                }
                            },
                            "optional": True
                        }
                    ]
                }
            }
        ]
    }
}

