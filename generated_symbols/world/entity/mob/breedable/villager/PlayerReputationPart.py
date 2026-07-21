# Generated from symbols.json for ::java::world::entity::mob::breedable::villager::PlayerReputationPart
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from generated_symbols.world.entity.mob.breedable.villager.ReputationPart import ReputationPart


@dataclass(kw_only=True)
class PlayerReputationPart:
    Type: ReputationPart | None = None
    Value: Any | None = None
    Target: tuple[int, int, int, int] | None = None  # UUID of the player that caused the gossip-worthy event(s) related to this reputation part.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::villager::PlayerReputationPart": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "Type",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::breedable::villager::ReputationPart"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "Value",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "Type"
                            ]
                        }
                    ],
                    "registry": "minecraft:reputation_part_value"
                },
                "optional": True
            },
            {
                "kind": "spread",
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
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "desc": "Upper bits of the UUID of the player that caused the gossip-worthy event(s) related to this reputation part.",
                            "key": "TargetMost",
                            "type": {
                                "kind": "long"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "desc": "Lower bits of the UUID of the player that caused the gossip-worthy event(s) related to this reputation part.",
                            "key": "TargetLeast",
                            "type": {
                                "kind": "long"
                            },
                            "optional": True
                        }
                    ]
                }
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
                "desc": "UUID of the player that caused the gossip-worthy event(s) related to this reputation part.",
                "key": "Target",
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

