# Generated from symbols.json for ::java::world::entity::mob::zombified_piglin::ZombiePigman
from dataclasses import dataclass
from generated_symbols.world.entity.mob.MobBase import MobBase
from generated_symbols.world.entity.mob.NeutralMob import NeutralMob


@dataclass(kw_only=True)
class ZombiePigman(MobBase, NeutralMob):
    IsBaby: bool | None = None  # Whether it is a baby.
    HurtBy: str | None = None  # Last player to hit a zombie pigman in this zombie pigman's detection range.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::zombified_piglin::ZombiePigman": {
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
                "desc": "Whether it is a baby.",
                "key": "IsBaby",
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
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "desc": "Ticks that it will be angry for.",
                "key": "Anger",
                "type": {
                    "kind": "short"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Last player to hit a zombie pigman in this zombie pigman's detection range.",
                "key": "HurtBy",
                "type": {
                    "kind": "string",
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

