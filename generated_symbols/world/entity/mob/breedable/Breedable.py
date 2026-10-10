"""
Generated from symbols.json for ::java::world::entity::mob::breedable::Breedable
Local link to file: generated_symbols/world/entity/mob/breedable/Breedable.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from generated_symbols.minecraft_types import MinecraftUUID
from generated_symbols.world.entity.mob.AgeableMob import AgeableMob
from generated_symbols.world.entity.mob.MobBase import MobBase


class Breedable(AgeableMob, MobBase):
    InLove: Annotated[int, Field(ge=0)] | None = None  # Ticks until it stops searching for a mate.
    LoveCause: MinecraftUUID | None = None  # Player that caused this mob to breed.


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

