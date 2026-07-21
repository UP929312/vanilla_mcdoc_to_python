# Generated from symbols.json for ::java::world::entity::mob::breedable::villager::WanderingTrader
from dataclasses import dataclass
from generated_symbols.world.entity.mob.MobBase import MobBase
from generated_symbols.world.entity.mob.breedable.villager.VillagerBase import VillagerBase


@dataclass(kw_only=True)
class WanderingTrader(MobBase, VillagerBase):
    DespawnDelay: int | None = None  # Ticks until it despawns.
    wander_target: tuple[int, int, int] | None = None  # Where it is heading to.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::villager::WanderingTrader": {
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
                    "path": "::java::world::entity::mob::breedable::villager::VillagerBase"
                }
            },
            {
                "kind": "pair",
                "desc": "Ticks until it despawns.",
                "key": "DespawnDelay",
                "type": {
                    "kind": "int"
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
                "desc": "Where it is heading to.",
                "key": "WanderTarget",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::breedable::villager::WanderTarget"
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
                "desc": "Where it is heading to.",
                "key": "wander_target",
                "type": {
                    "kind": "int_array",
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
                    }
                },
                "optional": True
            }
        ]
    }
}

