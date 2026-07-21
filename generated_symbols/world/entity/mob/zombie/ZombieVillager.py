# Generated from symbols.json for ::java::world::entity::mob::zombie::ZombieVillager
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.entity.mob.zombie.Zombie import Zombie

if TYPE_CHECKING:
    from generated_symbols.world.entity.mob.breedable.villager.Offers import Offers
    from generated_symbols.world.entity.mob.breedable.villager.PlayerReputationPart import PlayerReputationPart
    from generated_symbols.world.entity.mob.breedable.villager.VillagerData import VillagerData


@dataclass(kw_only=True)
class ZombieVillager(Zombie):
    VillagerData: VillagerData | None = None  # Villager's skin data
    Gossips: list[PlayerReputationPart] | None = None  # Villager's gossips
    Offers: Offers | None = None  # Villager's offers
    ConversionTime: int | None = None  # Ticks until the it is converted.
    ConversionPlayer: tuple[int, int, int, int] | None = None  # Player who triggered the conversion.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::zombie::ZombieVillager": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::zombie::Zombie"
                }
            },
            {
                "kind": "pair",
                "desc": "Villager's skin data",
                "key": "VillagerData",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::breedable::villager::VillagerData"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Villager's gossips",
                "key": "Gossips",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::world::entity::mob::breedable::villager::PlayerReputationPart"
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Villager's offers",
                "key": "Offers",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::breedable::villager::Offers"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Ticks until the it is converted.",
                "key": "ConversionTime",
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
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "desc": "Lower bits of the player's uuid who triggered the conversion.",
                "key": "ConversionPlayerLeast",
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
                "desc": "Upper bits of the player's uuid who triggered the conversion.",
                "key": "ConversionPlayerMost",
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
                "desc": "Player who triggered the conversion.",
                "key": "ConversionPlayer",
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

