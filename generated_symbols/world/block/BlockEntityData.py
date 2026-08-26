"""
Generated from symbols.json for ::java::world::block::BlockEntityData
Local link to file: generated_symbols/world/block/BlockEntityData.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Literal

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
from generated_symbols.world.block.creaking_heart.CreakingHeart import CreakingHeart
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
from generated_symbols.world.block.spawner.Spawner import Spawner
from generated_symbols.world.block.spawner.TrialSpawner import TrialSpawner
from generated_symbols.world.block.structure_block.StructureBlock import StructureBlock
from generated_symbols.world.block.test_block.TestBlock import TestBlock
from generated_symbols.world.block.test_instance_block.TestInstanceBlock import TestInstanceBlock
from generated_symbols.world.block.vault.Vault import Vault


@dataclass(kw_only=True)
class BlockEntityDataBanner(Banner):
    id: Literal['minecraft:banner']


@dataclass(kw_only=True)
class BlockEntityDataBarrel(Container27):
    id: Literal['minecraft:barrel']


@dataclass(kw_only=True)
class BlockEntityDataBeacon(Beacon):
    id: Literal['minecraft:beacon']


@dataclass(kw_only=True)
class BlockEntityDataBeehive(Beehive):
    id: Literal['minecraft:beehive']


@dataclass(kw_only=True)
class BlockEntityDataBlastFurnace(Furnace):
    id: Literal['minecraft:blast_furnace']


@dataclass(kw_only=True)
class BlockEntityDataBrewingStand(BrewingStand):
    id: Literal['minecraft:brewing_stand']


@dataclass(kw_only=True)
class BlockEntityDataBrushableBlock(BrushableBlock):
    id: Literal['minecraft:brushable_block']


@dataclass(kw_only=True)
class BlockEntityDataCalibratedSculkSensor(SculkSensor):
    id: Literal['minecraft:calibrated_sculk_sensor']


@dataclass(kw_only=True)
class BlockEntityDataCampfire(Campfire):
    id: Literal['minecraft:campfire']


@dataclass(kw_only=True)
class BlockEntityDataChest(Container27):
    id: Literal['minecraft:chest']


@dataclass(kw_only=True)
class BlockEntityDataChiseledBookshelf(ChiseledBookshelf):
    id: Literal['minecraft:chiseled_bookshelf']


@dataclass(kw_only=True)
class BlockEntityDataCommandBlock(CommandBlock):
    id: Literal['minecraft:command_block']


@dataclass(kw_only=True)
class BlockEntityDataComparator(Comparator):
    id: Literal['minecraft:comparator']


@dataclass(kw_only=True)
class BlockEntityDataConduit(Conduit):
    id: Literal['minecraft:conduit']


@dataclass(kw_only=True)
class BlockEntityDataCrafter(Crafter):
    id: Literal['minecraft:crafter']


@dataclass(kw_only=True)
class BlockEntityDataCreakingHeart(CreakingHeart):
    id: Literal['minecraft:creaking_heart']


@dataclass(kw_only=True)
class BlockEntityDataDecoratedPot(DecoratedPot):
    id: Literal['minecraft:decorated_pot']


@dataclass(kw_only=True)
class BlockEntityDataDispenser(Container9):
    id: Literal['minecraft:dispenser']


@dataclass(kw_only=True)
class BlockEntityDataDropper(Container9):
    id: Literal['minecraft:dropper']


@dataclass(kw_only=True)
class BlockEntityDataEnchantingTable(EnchantingTable):
    id: Literal['minecraft:enchanting_table']


@dataclass(kw_only=True)
class BlockEntityDataEndGateway(EndGateway):
    id: Literal['minecraft:end_gateway']


@dataclass(kw_only=True)
class BlockEntityDataFurnace(Furnace):
    id: Literal['minecraft:furnace']


@dataclass(kw_only=True)
class BlockEntityDataHangingSign:
    id: Literal['minecraft:hanging_sign']


@dataclass(kw_only=True)
class BlockEntityDataHopper(Hopper):
    id: Literal['minecraft:hopper']


@dataclass(kw_only=True)
class BlockEntityDataJigsaw(Jigsaw):
    id: Literal['minecraft:jigsaw']


@dataclass(kw_only=True)
class BlockEntityDataJukebox(Jukebox):
    id: Literal['minecraft:jukebox']


@dataclass(kw_only=True)
class BlockEntityDataLectern(Lectern):
    id: Literal['minecraft:lectern']


@dataclass(kw_only=True)
class BlockEntityDataMobSpawner(Spawner):
    id: Literal['minecraft:mob_spawner']


@dataclass(kw_only=True)
class BlockEntityDataMovingPiston(MovingPiston):
    id: Literal['minecraft:moving_piston']


@dataclass(kw_only=True)
class BlockEntityDataPotentSulfur(PotentSulfur):
    id: Literal['minecraft:potent_sulfur']


@dataclass(kw_only=True)
class BlockEntityDataSculkCatalyst(SculkCatalyst):
    id: Literal['minecraft:sculk_catalyst']


@dataclass(kw_only=True)
class BlockEntityDataSculkSensor(SculkSensor):
    id: Literal['minecraft:sculk_sensor']


@dataclass(kw_only=True)
class BlockEntityDataSculkShrieker(SculkShrieker):
    id: Literal['minecraft:sculk_shrieker']


@dataclass(kw_only=True)
class BlockEntityDataShelf(Shelf):
    id: Literal['minecraft:shelf']


@dataclass(kw_only=True)
class BlockEntityDataShulkerBox(Container27):
    id: Literal['minecraft:shulker_box']


@dataclass(kw_only=True)
class BlockEntityDataSign:
    id: Literal['minecraft:sign']


@dataclass(kw_only=True)
class BlockEntityDataSkull(Skull):
    id: Literal['minecraft:skull']


@dataclass(kw_only=True)
class BlockEntityDataSmoker(Furnace):
    id: Literal['minecraft:smoker']


@dataclass(kw_only=True)
class BlockEntityDataStructureBlock(StructureBlock):
    id: Literal['minecraft:structure_block']


@dataclass(kw_only=True)
class BlockEntityDataTestBlock(TestBlock):
    id: Literal['minecraft:test_block']


@dataclass(kw_only=True)
class BlockEntityDataTestInstanceBlock(TestInstanceBlock):
    id: Literal['minecraft:test_instance_block']


@dataclass(kw_only=True)
class BlockEntityDataTrappedChest(Container27):
    id: Literal['minecraft:trapped_chest']


@dataclass(kw_only=True)
class BlockEntityDataTrialSpawner(TrialSpawner):
    id: Literal['minecraft:trial_spawner']


@dataclass(kw_only=True)
class BlockEntityDataVault(Vault):
    id: Literal['minecraft:vault']


type BlockEntityData = BlockEntityDataBanner | BlockEntityDataBarrel | BlockEntityDataBeacon | BlockEntityDataBeehive | BlockEntityDataBlastFurnace | BlockEntityDataBrewingStand | BlockEntityDataBrushableBlock | BlockEntityDataCalibratedSculkSensor | BlockEntityDataCampfire | BlockEntityDataChest | BlockEntityDataChiseledBookshelf | BlockEntityDataCommandBlock | BlockEntityDataComparator | BlockEntityDataConduit | BlockEntityDataCrafter | BlockEntityDataCreakingHeart | BlockEntityDataDecoratedPot | BlockEntityDataDispenser | BlockEntityDataDropper | BlockEntityDataEnchantingTable | BlockEntityDataEndGateway | BlockEntityDataFurnace | BlockEntityDataHangingSign | BlockEntityDataHopper | BlockEntityDataJigsaw | BlockEntityDataJukebox | BlockEntityDataLectern | BlockEntityDataMobSpawner | BlockEntityDataMovingPiston | BlockEntityDataPotentSulfur | BlockEntityDataSculkCatalyst | BlockEntityDataSculkSensor | BlockEntityDataSculkShrieker | BlockEntityDataShelf | BlockEntityDataShulkerBox | BlockEntityDataSign | BlockEntityDataSkull | BlockEntityDataSmoker | BlockEntityDataStructureBlock | BlockEntityDataTestBlock | BlockEntityDataTestInstanceBlock | BlockEntityDataTrappedChest | BlockEntityDataTrialSpawner | BlockEntityDataVault


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::BlockEntityData": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "id",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "block_entity_type"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "id"
                            ]
                        }
                    ],
                    "registry": "minecraft:block_entity"
                }
            }
        ]
    }
}

