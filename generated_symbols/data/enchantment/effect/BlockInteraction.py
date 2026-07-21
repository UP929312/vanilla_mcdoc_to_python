# Generated from symbols.json for ::java::data::enchantment::effect::BlockInteraction
from enum import Enum


class BlockInteraction(Enum):
    NONE = "none"  # No item drops or special behavior.
    BLOCKOLDDOC = "block"  # Drops items as if a block caused the explosion; `blockExplosionDropDecay` game rule applies.
    BLOCK = "block"  # Drops items as if a block caused the explosion; `block_explosion_drop_decay` game rule applies.
    MOBOLDDOC = "mob"  # Drops items as if a mob caused the explosion; `mobExplosionDropDecay` game rule applies.
    MOB = "mob"  # Drops items as if a mob caused the explosion; `mob_explosion_drop_decay` game rule applies.
    TNTOLDDOC = "tnt"  # Drops items as if TNT caused the explosion; `tntExplosionDropDecay` game rule applies.
    TNT = "tnt"  # Drops items as if TNT caused the explosion; `tnt_explosion_drop_decay` game rule applies.
    TRIGGER = "trigger"  # Triggers redstone-activated blocks.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect::BlockInteraction": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "desc": "No item drops or special behavior.",
                "identifier": "None",
                "value": "none"
            },
            {
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "desc": "Drops items as if a block caused the explosion; `blockExplosionDropDecay` game rule applies.",
                "identifier": "BlockOldDoc",
                "value": "block"
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "desc": "Drops items as if a block caused the explosion; `block_explosion_drop_decay` game rule applies.",
                "identifier": "Block",
                "value": "block"
            },
            {
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "desc": "Drops items as if a mob caused the explosion; `mobExplosionDropDecay` game rule applies.",
                "identifier": "MobOldDoc",
                "value": "mob"
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "desc": "Drops items as if a mob caused the explosion; `mob_explosion_drop_decay` game rule applies.",
                "identifier": "Mob",
                "value": "mob"
            },
            {
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "desc": "Drops items as if TNT caused the explosion; `tntExplosionDropDecay` game rule applies.",
                "identifier": "TNTOldDoc",
                "value": "tnt"
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "desc": "Drops items as if TNT caused the explosion; `tnt_explosion_drop_decay` game rule applies.",
                "identifier": "TNT",
                "value": "tnt"
            },
            {
                "desc": "Triggers redstone-activated blocks.",
                "identifier": "Trigger",
                "value": "trigger"
            }
        ]
    }
}

