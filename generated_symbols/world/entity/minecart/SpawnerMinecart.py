# Generated from symbols.json for ::java::world::entity::minecart::SpawnerMinecart
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.entity.minecart.Minecart import Minecart

if TYPE_CHECKING:
    from generated_symbols.world.block.spawner.SpawnPotential import SpawnPotential
    from generated_symbols.world.block.spawner.SpawnerEntry import SpawnerEntry


@dataclass(kw_only=True)
class SpawnerMinecart(Minecart):
    SpawnCount: int  # Number of entities that will be placed.
    SpawnPotentials: list[SpawnPotential] | None = None  # List of potential entities to place next.
    SpawnData: SpawnerEntry | None = None  # Data for the next mob to place. Will be overwritten by `SpawnPotentials`.
    SpawnRange: int | None = None  # Range that the spawned entities will be placed in.
    Delay: int | None = None  # Ticks until the next spawn.
    MinSpawnDelay: int | None = None  # Minimum random delay for the next spawn.
    MaxSpawnDelay: int | None = None  # Maximum random delay for the next spawn.
    MaxNearbyEntities: int | None = None  # Maximum number of entities nearby.
    RequiredPlayerRange: int | None = None  # Radius in blocks that a player has to be within to spawn entities.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::minecart::SpawnerMinecart": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::minecart::Minecart"
                }
            },
            {
                "kind": "pair",
                "desc": "List of potential entities to place next.",
                "key": "SpawnPotentials",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::world::block::spawner::SpawnPotential"
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Data for the next mob to place.\nWill be overwritten by `SpawnPotentials`.",
                "key": "SpawnData",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::world::entity::AnyEntity",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.18"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "reference",
                            "path": "::java::world::block::spawner::SpawnerEntry",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.18"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Number of entities that will be placed.",
                "key": "SpawnCount",
                "type": {
                    "kind": "short"
                }
            },
            {
                "kind": "pair",
                "desc": "Range that the spawned entities will be placed in.",
                "key": "SpawnRange",
                "type": {
                    "kind": "short"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Ticks until the next spawn.",
                "key": "Delay",
                "type": {
                    "kind": "short"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Minimum random delay for the next spawn.",
                "key": "MinSpawnDelay",
                "type": {
                    "kind": "short"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Maximum random delay for the next spawn.",
                "key": "MaxSpawnDelay",
                "type": {
                    "kind": "short"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Maximum number of entities nearby.",
                "key": "MaxNearbyEntities",
                "type": {
                    "kind": "short"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Radius in blocks that a player has to be within to spawn entities.",
                "key": "RequiredPlayerRange",
                "type": {
                    "kind": "short"
                },
                "optional": True
            }
        ]
    }
}

