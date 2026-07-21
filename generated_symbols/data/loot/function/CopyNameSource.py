# Generated from symbols.json for ::java::data::loot::function::CopyNameSource
from enum import Enum


class CopyNameSource(Enum):
    THIS = "this"
    KILLER = "killer"
    ATTACKINGENTITY = "attacking_entity"
    KILLERPLAYER = "killer_player"
    LASTDAMAGEPLAYER = "last_damage_player"
    BLOCKENTITY = "block_entity"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::CopyNameSource": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "identifier": "This",
                "value": "this"
            },
            {
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21"
                            }
                        }
                    }
                ],
                "identifier": "Killer",
                "value": "killer"
            },
            {
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
                    }
                ],
                "identifier": "AttackingEntity",
                "value": "attacking_entity"
            },
            {
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21"
                            }
                        }
                    }
                ],
                "identifier": "KillerPlayer",
                "value": "killer_player"
            },
            {
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
                    }
                ],
                "identifier": "LastDamagePlayer",
                "value": "last_damage_player"
            },
            {
                "identifier": "BlockEntity",
                "value": "block_entity"
            }
        ]
    }
}

