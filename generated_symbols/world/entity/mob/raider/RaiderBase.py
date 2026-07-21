# Generated from symbols.json for ::java::world::entity::mob::raider::RaiderBase
from dataclasses import dataclass
from typing import Annotated
from generated_symbols.world.entity.mob.MobBase import MobBase


@dataclass(kw_only=True)
class RaiderBase(MobBase):
    Patrolling: bool | None = None  # Whether the raider is patrolling.
    PatrolLeader: bool | None = None  # Whether the raider is leading the patrol.
    patrol_target: tuple[int, int, int] | None = None  # Where the raider is heading towards.
    CanJoinRaid: bool | None = None  # Whether the raider can join raids and count towards the progress bar.
    RaidId: int | None = None  # Id of the raid that the raider is in.
    Wave: Annotated[int, 'Range | `0`-`8` | both inclusive'] | None = None  # Wave that the raider is in.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::raider::RaiderBase": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::MobBase"
                }
            },
            {
                "kind": "pair",
                "desc": "Whether the raider is patrolling.",
                "key": "Patrolling",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the raider is leading the patrol.",
                "key": "PatrolLeader",
                "type": {
                    "kind": "boolean"
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
                                "value": "1.20.5"
                            }
                        }
                    }
                ],
                "desc": "Where the raider is heading towards.",
                "key": "PatrolTarget",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::raider::PatrolTarget"
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
                                "value": "1.20.5"
                            }
                        }
                    }
                ],
                "desc": "Where the raider is heading towards.",
                "key": "patrol_target",
                "type": {
                    "kind": "int_array",
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
                "desc": "Whether the raider can join raids and count towards the progress bar.",
                "key": "CanJoinRaid",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Id of the raid that the raider is in.",
                "key": "RaidId",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Wave that the raider is in.",
                "key": "Wave",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 8
                    }
                },
                "optional": True
            }
        ]
    }
}

