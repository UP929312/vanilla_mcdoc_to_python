"""
Generated from symbols.json for ::java::world::entity::mob::zombie::Zombie
Local link to file: generated_symbols/world/entity/mob/zombie/Zombie.py
"""
# ~~~ CODE ~~~
from generated_symbols.world.entity.mob.MobBase import MobBase


class Zombie(MobBase):
    IsBaby: bool | None = None  # Whether it is a baby.
    CanBreakDoors: bool | None = None  # Whether it can break doors.
    DrownedConversionTime: int | None = None  # Ticks until it converts.
    InWaterTime: int | None = None  # Ticks it has been in the water.
    FrostbiteConversionTime: int | None = None  # Ticks until it converts.
    FreezingTime: int | None = None  # Ticks it has been in the powdered snow.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::zombie::Zombie": {
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
                "desc": "Whether it is a baby.",
                "key": "IsBaby",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether it can break doors.",
                "key": "CanBreakDoors",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Ticks until it converts.",
                "key": "DrownedConversionTime",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Ticks it has been in the water.",
                "key": "InWaterTime",
                "type": {
                    "kind": "int"
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
                                "value": "26.4"
                            }
                        }
                    }
                ],
                "desc": "Ticks until it converts.",
                "key": "FrostbiteConversionTime",
                "type": {
                    "kind": "int"
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
                                "value": "26.4"
                            }
                        }
                    }
                ],
                "desc": "Ticks it has been in the powdered snow.",
                "key": "FreezingTime",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}

