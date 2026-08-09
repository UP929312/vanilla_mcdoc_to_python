# Generated from symbols.json for ::java::data::advancement::predicate::BlockPredicate
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.BlockPredicateState import BlockPredicateState
    from generated_symbols.world.block.BlockEntity import BlockEntity
    from generated_symbols.world.block.banner.Banner import Banner
    from generated_symbols.world.block.beacon.Beacon import Beacon
    from generated_symbols.world.block.beehive.Beehive import Beehive
    from generated_symbols.world.block.brewing_stand.BrewingStand import BrewingStand
    from generated_symbols.world.block.brushable_block.BrushableBlock import BrushableBlock
    from generated_symbols.world.block.campfire.Campfire import Campfire
    from generated_symbols.world.block.chiseled_bookshelf.ChiseledBookshelf import ChiseledBookshelf
    from generated_symbols.world.block.command_block.CommandBlock import CommandBlock
    from generated_symbols.world.block.comparator.Comparator import Comparator
    from generated_symbols.world.block.conduit.Conduit import Conduit
    from generated_symbols.world.block.container.Container27 import Container27
    from generated_symbols.world.block.container.Container9 import Container9
    from generated_symbols.world.block.container.Hopper import Hopper
    from generated_symbols.world.block.container.Shelf import Shelf
    from generated_symbols.world.block.crafter.Crafter import Crafter
    from generated_symbols.world.block.decorated_pot.DecoratedPot import DecoratedPot
    from generated_symbols.world.block.enchanting_table.EnchantingTable import EnchantingTable
    from generated_symbols.world.block.end_gateway.EndGateway import EndGateway
    from generated_symbols.world.block.furnace.Furnace import Furnace
    from generated_symbols.world.block.head.Skull import Skull
    from generated_symbols.world.block.jigsaw.Jigsaw import Jigsaw
    from generated_symbols.world.block.jukebox.Jukebox import Jukebox
    from generated_symbols.world.block.lectern.Lectern import Lectern
    from generated_symbols.world.block.moving_piston.MovingPiston import MovingPiston
    from generated_symbols.world.block.potent_sulfur.PotentSulfur import PotentSulfur
    from generated_symbols.world.block.sculk_catalyst.SculkCatalyst import SculkCatalyst
    from generated_symbols.world.block.sculk_sensor.SculkSensor import SculkSensor
    from generated_symbols.world.block.sculk_shrieker.SculkShrieker import SculkShrieker
    from generated_symbols.world.block.sign.Sign import Sign
    from generated_symbols.world.block.spawner.Spawner import Spawner
    from generated_symbols.world.block.spawner.TrialSpawner import TrialSpawner
    from generated_symbols.world.block.structure_block.StructureBlock import StructureBlock
    from generated_symbols.world.block.test_block.TestBlock import TestBlock
    from generated_symbols.world.block.test_instance_block.TestInstanceBlock import TestInstanceBlock
    from generated_symbols.world.block.vault.Vault import Vault
    from generated_symbols.world.component.DataComponentExactPredicate import DataComponentExactPredicate
    from generated_symbols.world.component.DataComponentPredicate import DataComponentPredicate


@dataclass(kw_only=True)
class BlockStructUnknown:
    pass


@dataclass(kw_only=True)
class NbtStructBlockUnknown:
    pass


@dataclass(kw_only=True)
class BlockPredicate:
    blocks: Annotated[str, IdSpec(registry='block', tags='allowed')] | list[Annotated[str, IdSpec(registry='block')]] | None = None
    state: BlockPredicateState | None = None
    nbt: str | NbtStructBlockUnknown | Sign | Shelf | Container27 | Beacon | BlockEntity | Beehive | Banner | Furnace | BrewingStand | SculkSensor | Campfire | CommandBlock | ChiseledBookshelf | Comparator | Conduit | Crafter | Skull | DecoratedPot | Container9 | EnchantingTable | EndGateway | Hopper | Jigsaw | Jukebox | Lectern | MovingPiston | PotentSulfur | SculkCatalyst | SculkShrieker | Spawner | StructureBlock | BrushableBlock | TestBlock | TestInstanceBlock | TrialSpawner | Vault | None = None
    components: DataComponentExactPredicate | None = None  # Match exact data component values on the block entity.
    predicates: DataComponentPredicate | None = None  # Test data component values on the block entity.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::BlockPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.17"
                            }
                        }
                    }
                ],
                "key": "block",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "block"
                                }
                            }
                        }
                    ]
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
                                "value": "1.17"
                            }
                        }
                    }
                ],
                "key": "blocks",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
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
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "tree",
                                        "values": {
                                            "registry": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "block"
                                                }
                                            },
                                            "tags": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "allowed"
                                                }
                                            }
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "list",
                            "item": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "id",
                                        "value": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "block"
                                            }
                                        }
                                    }
                                ]
                            }
                        }
                    ]
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
                "key": "tag",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "tree",
                                "values": {
                                    "registry": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "block"
                                        }
                                    },
                                    "tags": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "implicit"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "state",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::BlockPredicateState"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "nbt",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "nbt",
                                    "value": {
                                        "kind": "dispatcher",
                                        "parallelIndices": [
                                            {
                                                "kind": "dynamic",
                                                "accessor": [
                                                    "blocks"
                                                ]
                                            }
                                        ],
                                        "registry": "minecraft:block"
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "dispatcher",
                            "parallelIndices": [
                                {
                                    "kind": "dynamic",
                                    "accessor": [
                                        "blocks"
                                    ]
                                }
                            ],
                            "registry": "minecraft:block",
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
                            ]
                        }
                    ]
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
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "desc": "Match exact data component values on the block entity.",
                "key": "components",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::DataComponentExactPredicate"
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
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "desc": "Test data component values on the block entity.",
                "key": "predicates",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::DataComponentPredicate"
                },
                "optional": True
            }
        ]
    }
}

