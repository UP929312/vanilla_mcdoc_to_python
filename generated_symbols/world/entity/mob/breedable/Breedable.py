# Generated from symbols.json for ::java::world::entity::mob::breedable::Breedable
from dataclasses import dataclass
from typing import Annotated
from generated_symbols.world.entity.mob.AgeableMob import AgeableMob
from generated_symbols.world.entity.mob.MobBase import MobBase


@dataclass(kw_only=True)
class Breedable(MobBase, AgeableMob):
    InLove: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # Ticks until it stops searching for a mate.
    LoveCause: tuple[int, int, int, int] | None = None  # Player that caused this mob to breed.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::Breedable": {
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
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::AgeableMob"
                }
            },
            {
                "kind": "pair",
                "desc": "Ticks until it stops searching for a mate.",
                "key": "InLove",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
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
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "desc": "Lower bits of the UUID of the player that caused this mob to breed.",
                "key": "LoveCauseLeast",
                "type": {
                    "kind": "long"
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
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "desc": "Upper bits of the UUID of the player that caused this mob to breed.",
                "key": "LoveCauseMost",
                "type": {
                    "kind": "long"
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
                "desc": "Player that caused this mob to breed.",
                "key": "LoveCause",
                "type": {
                    "kind": "int_array",
                    "lengthRange": {
                        "kind": 0,
                        "min": 4,
                        "max": 4
                    },
                    "attributes": [
                        {
                            "name": "uuid"
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

