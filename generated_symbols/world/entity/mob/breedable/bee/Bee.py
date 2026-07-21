# Generated from symbols.json for ::java::world::entity::mob::breedable::bee::Bee
from dataclasses import dataclass
from generated_symbols.world.entity.mob.NeutralMob import NeutralMob
from generated_symbols.world.entity.mob.breedable.Breedable import Breedable


@dataclass(kw_only=True)
class Bee(Breedable, NeutralMob):
    hive_pos: tuple[int, int, int] | None = None
    flower_pos: tuple[int, int, int] | None = None  # Position of the flower the bee is circling
    HasNectar: bool | None = None  # Whether the bee has nectar.
    HasStung: bool | None = None  # Whether the bee has stung an entity.
    TicksSincePollination: int | None = None  # Ticks since the bee has pollinated a crop.
    CannotEnterHiveTicks: int | None = None  # Ticks until the bee can enter its hive.
    CropsGrownSincePollination: int | None = None  # Crops grown since the bee has gathered nectar.
    Anger: int | None = None  # Ticks the bee will be angry for.
    HurtBy: tuple[int, int, int, int] | None = None  # Player that has attacked the bee.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::bee::Bee": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::breedable::Breedable"
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
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::NeutralMob"
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
                                "value": "1.20.5"
                            }
                        }
                    }
                ],
                "key": "HivePos",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::breedable::bee::HivePos"
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
                "key": "hive_pos",
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
                "desc": "Position of the flower the bee is circling",
                "key": "FlowerPos",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::breedable::bee::FlowerPos"
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
                "desc": "Position of the flower the bee is circling",
                "key": "flower_pos",
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
                "desc": "Whether the bee has nectar.",
                "key": "HasNectar",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the bee has stung an entity.",
                "key": "HasStung",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Ticks since the bee has pollinated a crop.",
                "key": "TicksSincePollination",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Ticks until the bee can enter its hive.",
                "key": "CannotEnterHiveTicks",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Crops grown since the bee has gathered nectar.",
                "key": "CropsGrownSincePollination",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Ticks the bee will be angry for.",
                "key": "Anger",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Player that has attacked the bee.",
                "key": "HurtBy",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
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
                                },
                                {
                                    "name": "uuid"
                                }
                            ]
                        },
                        {
                            "kind": "int_array",
                            "lengthRange": {
                                "kind": 0,
                                "min": 4,
                                "max": 4
                            },
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
                                },
                                {
                                    "name": "uuid"
                                }
                            ]
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

