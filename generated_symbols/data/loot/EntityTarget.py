# Generated from symbols.json for ::java::data::loot::EntityTarget
from enum import Enum


class EntityTarget(Enum):
    THIS = "this"
    KILLER = "killer"
    ATTACKER = "attacker"
    DIRECTKILLER = "direct_killer"
    DIRECTATTACKER = "direct_attacker"
    KILLERPLAYER = "killer_player"
    ATTACKINGPLAYER = "attacking_player"
    TARGETENTITY = "target_entity"
    INTERACTINGENTITY = "interacting_entity"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::EntityTarget": {
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
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.9"
                            }
                        }
                    }
                ],
                "identifier": "TargetEntity",
                "value": "target_entity"
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.9"
                            }
                        }
                    }
                ],
                "identifier": "InteractingEntity",
                "value": "interacting_entity"
            }
        ]
    }
}

