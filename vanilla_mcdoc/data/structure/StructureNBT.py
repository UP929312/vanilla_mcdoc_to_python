"""
Generated from symbols.json for ::java::data::structure::StructureNBT
Local link to file: vanilla_mcdoc/data/structure/StructureNBT.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.block_state.BlockState import BlockState
    from vanilla_mcdoc.world.block.BlockEntity import BlockEntity
    from vanilla_mcdoc.world.block.banner.Banner import Banner
    from vanilla_mcdoc.world.block.beacon.Beacon import Beacon
    from vanilla_mcdoc.world.block.beehive.Beehive import Beehive
    from vanilla_mcdoc.world.block.brewing_stand.BrewingStand import BrewingStand
    from vanilla_mcdoc.world.block.brushable_block.BrushableBlock import BrushableBlock
    from vanilla_mcdoc.world.block.campfire.Campfire import Campfire
    from vanilla_mcdoc.world.block.chiseled_bookshelf.ChiseledBookshelf import ChiseledBookshelf
    from vanilla_mcdoc.world.block.command_block.CommandBlock import CommandBlock
    from vanilla_mcdoc.world.block.comparator.Comparator import Comparator
    from vanilla_mcdoc.world.block.conduit.Conduit import Conduit
    from vanilla_mcdoc.world.block.container.Container27 import Container27
    from vanilla_mcdoc.world.block.container.Container9 import Container9
    from vanilla_mcdoc.world.block.container.Hopper import Hopper
    from vanilla_mcdoc.world.block.container.Shelf import Shelf
    from vanilla_mcdoc.world.block.crafter.Crafter import Crafter
    from vanilla_mcdoc.world.block.decorated_pot.DecoratedPot import DecoratedPot
    from vanilla_mcdoc.world.block.enchanting_table.EnchantingTable import EnchantingTable
    from vanilla_mcdoc.world.block.end_gateway.EndGateway import EndGateway
    from vanilla_mcdoc.world.block.furnace.Furnace import Furnace
    from vanilla_mcdoc.world.block.head.Skull import Skull
    from vanilla_mcdoc.world.block.jigsaw.Jigsaw import Jigsaw
    from vanilla_mcdoc.world.block.jukebox.Jukebox import Jukebox
    from vanilla_mcdoc.world.block.lectern.Lectern import Lectern
    from vanilla_mcdoc.world.block.moving_piston.MovingPiston import MovingPiston
    from vanilla_mcdoc.world.block.potent_sulfur.PotentSulfur import PotentSulfur
    from vanilla_mcdoc.world.block.sculk_catalyst.SculkCatalyst import SculkCatalyst
    from vanilla_mcdoc.world.block.sculk_sensor.SculkSensor import SculkSensor
    from vanilla_mcdoc.world.block.sculk_shrieker.SculkShrieker import SculkShrieker
    from vanilla_mcdoc.world.block.sign.Sign import Sign
    from vanilla_mcdoc.world.block.spawner.Spawner import Spawner
    from vanilla_mcdoc.world.block.spawner.TrialSpawner import TrialSpawner
    from vanilla_mcdoc.world.block.structure_block.StructureBlock import StructureBlock
    from vanilla_mcdoc.world.block.test_block.TestBlock import TestBlock
    from vanilla_mcdoc.world.block.test_instance_block.TestInstanceBlock import TestInstanceBlock
    from vanilla_mcdoc.world.block.vault.Vault import Vault
    from vanilla_mcdoc.world.entity.AnyEntity import AnyEntity


class NbtStructBlockUnknown(GeneratedModel):
    pass


class BlocksStruct(GeneratedModel):
    state: Annotated[int, Field(ge=0)]
    pos: tuple[Annotated[int, Field(ge=0)], Annotated[int, Field(ge=0)], Annotated[int, Field(ge=0)]]
    nbt: NbtStructBlockUnknown | Sign | Shelf | Container27 | Beacon | Beehive | BlockEntity | Banner | Furnace | BrewingStand | SculkSensor | Campfire | CommandBlock | ChiseledBookshelf | Comparator | Conduit | Crafter | Skull | DecoratedPot | Container9 | EnchantingTable | EndGateway | Hopper | Jigsaw | Jukebox | Lectern | MovingPiston | PotentSulfur | SculkCatalyst | SculkShrieker | Spawner | StructureBlock | BrushableBlock | TestBlock | TestInstanceBlock | TrialSpawner | Vault | None = None


class EntitiesStruct(GeneratedModel):
    pos: tuple[Annotated[float, Field(ge=0)], Annotated[float, Field(ge=0)], Annotated[float, Field(ge=0)]]
    blockPos: tuple[Annotated[int, Field(ge=0)], Annotated[int, Field(ge=0)], Annotated[int, Field(ge=0)]]
    nbt: AnyEntity


class StructureNBTStruct1(GeneratedModel):
    DataVersion: Annotated[int, Field(ge=0)]  # [Data version](https://minecraft.wiki/w/Data_version).
    size: tuple[Annotated[int, Field(ge=0)], Annotated[int, Field(ge=0)], Annotated[int, Field(ge=0)]]
    blocks: list[BlocksStruct]
    entities: list[EntitiesStruct]
    palette: list[BlockState]


class StructureNBTStruct2(GeneratedModel):
    DataVersion: Annotated[int, Field(ge=0)]  # [Data version](https://minecraft.wiki/w/Data_version).
    size: tuple[Annotated[int, Field(ge=0)], Annotated[int, Field(ge=0)], Annotated[int, Field(ge=0)]]
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
