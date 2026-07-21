# Generated from symbols.json for ::java::world::entity::mob::dolphin::Dolphin
from dataclasses import dataclass
from generated_symbols.world.entity.mob.AgeableMob import AgeableMob
from generated_symbols.world.entity.mob.MobBase import MobBase


@dataclass(kw_only=True)
class Dolphin(MobBase, AgeableMob):
    GotFish: bool | None = None  # Whether it has gotten fish from a player.
    Moistness: int | None = None  # Moistness level of the dolphin. Set to 2400 when the dolphin is in water or rain, otherwise decreases by 1 every tick. The dolphin takes damage when level is at 0 or below.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::dolphin::Dolphin": {
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
                "kind": "spread",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.2"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::AgeableMob"
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
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "desc": "X coordinate of the treasure it leads to.",
                "key": "TreasurePosX",
                "type": {
                    "kind": "int"
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
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "desc": "Y coordinate of the treasure it leads to.",
                "key": "TreasurePosY",
                "type": {
                    "kind": "int"
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
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "desc": "Z coordinate of the treasure it leads to.",
                "key": "TreasurePosZ",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether it has gotten fish from a player.",
                "key": "GotFish",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Moistness level of the dolphin.\nSet to 2400 when the dolphin is in water or rain, otherwise decreases by 1 every tick.\nThe dolphin takes damage when level is at 0 or below.",
                "key": "Moistness",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}

