"""
Generated from symbols.json for ::java::data::structure::StructureNBT
Local link to file: generated_symbols/data/structure/StructureNBT.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.util.block_state.BlockState import BlockState
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
    from generated_symbols.world.entity.AnyEntity import AnyEntity


@dataclass(kw_only=True)
class NbtStructBlockUnknown:
    pass


@dataclass(kw_only=True)
class BlocksStruct:
    state: Annotated[int, 'Range | Min `0` and above | inclusive']
    pos: tuple[Annotated[int, 'Range | Min `0` and above | inclusive'], Annotated[int, 'Range | Min `0` and above | inclusive'], Annotated[int, 'Range | Min `0` and above | inclusive']]
    nbt: NbtStructBlockUnknown | Sign | Shelf | Container27 | Beacon | BlockEntity | Beehive | Banner | Furnace | BrewingStand | SculkSensor | Campfire | CommandBlock | ChiseledBookshelf | Comparator | Conduit | Crafter | Skull | DecoratedPot | Container9 | EnchantingTable | EndGateway | Hopper | Jigsaw | Jukebox | Lectern | MovingPiston | PotentSulfur | SculkCatalyst | SculkShrieker | Spawner | StructureBlock | BrushableBlock | TestBlock | TestInstanceBlock | TrialSpawner | Vault | None = None


@dataclass(kw_only=True)
class EntitiesStruct:
    pos: tuple[Annotated[float, 'Range | Min `0` and above | inclusive'], Annotated[float, 'Range | Min `0` and above | inclusive'], Annotated[float, 'Range | Min `0` and above | inclusive']]
    blockPos: tuple[Annotated[int, 'Range | Min `0` and above | inclusive'], Annotated[int, 'Range | Min `0` and above | inclusive'], Annotated[int, 'Range | Min `0` and above | inclusive']]
    nbt: AnyEntity


@dataclass(kw_only=True)
class StructureNBTStruct1:
    DataVersion: Annotated[int, 'Range | Min `0` and above | inclusive']  # [Data version](https://minecraft.wiki/w/Data_version).
    size: tuple[Annotated[int, 'Range | Min `0` and above | inclusive'], Annotated[int, 'Range | Min `0` and above | inclusive'], Annotated[int, 'Range | Min `0` and above | inclusive']]
    blocks: list[BlocksStruct]
    entities: list[EntitiesStruct]
    palette: list[BlockState]


@dataclass(kw_only=True)
class StructureNBTStruct2:
    DataVersion: Annotated[int, 'Range | Min `0` and above | inclusive']  # [Data version](https://minecraft.wiki/w/Data_version).
    size: tuple[Annotated[int, 'Range | Min `0` and above | inclusive'], Annotated[int, 'Range | Min `0` and above | inclusive'], Annotated[int, 'Range | Min `0` and above | inclusive']]
    blocks: list[BlocksStruct]
    entities: list[EntitiesStruct]
    palettes: list[list[BlockState]]  # Sets of different block states used in the structure, a random palette gets selected based on coordinates.


type StructureNBT = StructureNBTStruct1 | StructureNBTStruct2


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::structure::StructureNBT": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "[Data version](https://minecraft.wiki/w/Data_version).",
                "key": "DataVersion",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                }
            },
            {
                "kind": "pair",
                "key": "size",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "int",
                        "valueRange": {
                            "kind": 0,
                            "min": 0
                        }
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
                    }
                }
            },
            {
                "kind": "pair",
                "key": "blocks",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "struct",
                        "fields": [
                            {
                                "kind": "pair",
                                "key": "state",
                                "type": {
                                    "kind": "int",
                                    "valueRange": {
                                        "kind": 0,
                                        "min": 0
                                    }
                                }
                            },
                            {
                                "kind": "pair",
                                "key": "pos",
                                "type": {
                                    "kind": "list",
                                    "item": {
                                        "kind": "int",
                                        "valueRange": {
                                            "kind": 0,
                                            "min": 0
                                        }
                                    },
                                    "lengthRange": {
                                        "kind": 0,
                                        "min": 3,
                                        "max": 3
                                    }
                                }
                            },
                            {
                                "kind": "pair",
                                "key": "nbt",
                                "type": {
                                    "kind": "dispatcher",
                                    "parallelIndices": [
                                        {
                                            "kind": "static",
                                            "value": "%fallback"
                                        }
                                    ],
                                    "registry": "minecraft:block"
                                },
                                "optional": True
                            }
                        ]
                    }
                }
            },
            {
                "kind": "pair",
                "key": "entities",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "struct",
                        "fields": [
                            {
                                "kind": "pair",
                                "key": "pos",
                                "type": {
                                    "kind": "list",
                                    "item": {
                                        "kind": "double",
                                        "valueRange": {
                                            "kind": 0,
                                            "min": 0
                                        }
                                    },
                                    "lengthRange": {
                                        "kind": 0,
                                        "min": 3,
                                        "max": 3
                                    }
                                }
                            },
                            {
                                "kind": "pair",
                                "key": "blockPos",
                                "type": {
                                    "kind": "list",
                                    "item": {
                                        "kind": "int",
                                        "valueRange": {
                                            "kind": 0,
                                            "min": 0
                                        }
                                    },
                                    "lengthRange": {
                                        "kind": 0,
                                        "min": 3,
                                        "max": 3
                                    }
                                }
                            },
                            {
                                "kind": "pair",
                                "key": "nbt",
                                "type": {
                                    "kind": "reference",
                                    "path": "::java::world::entity::AnyEntity"
                                }
                            }
                        ]
                    }
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::structure::BlockPalette"
                }
            }
        ]
    }
}

