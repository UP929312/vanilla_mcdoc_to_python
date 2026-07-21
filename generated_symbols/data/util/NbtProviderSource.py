# Generated from symbols.json for ::java::data::util::NbtProviderSource
from enum import Enum


class NbtProviderSource(Enum):
    THIS = "this"
    KILLER = "killer"
    ATTACKER = "attacker"
    DIRECTKILLER = "direct_killer"
    DIRECTATTACKER = "direct_attacker"
    KILLERPLAYER = "killer_player"
    ATTACKINGPLAYER = "attacking_player"
    BLOCKENTITY = "block_entity"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::util::NbtProviderSource": {
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
                "identifier": "Attacker",
                "value": "attacker"
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
                "identifier": "DirectKiller",
                "value": "direct_killer"
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
                "identifier": "DirectAttacker",
                "value": "direct_attacker"
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
                "identifier": "AttackingPlayer",
                "value": "attacking_player"
            },
            {
                "identifier": "BlockEntity",
                "value": "block_entity"
            }
        ]
    }
}

