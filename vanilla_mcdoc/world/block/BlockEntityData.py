"""
Generated from symbols.json for ::java::world::block::BlockEntityData
Local link to file: vanilla_mcdoc/world/block/BlockEntityData.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
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
from vanilla_mcdoc.world.block.creaking_heart.CreakingHeart import CreakingHeart
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
from vanilla_mcdoc.world.block.spawner.Spawner import Spawner
from vanilla_mcdoc.world.block.spawner.TrialSpawner import TrialSpawner
from vanilla_mcdoc.world.block.structure_block.StructureBlock import StructureBlock
from vanilla_mcdoc.world.block.test_block.TestBlock import TestBlock
from vanilla_mcdoc.world.block.test_instance_block.TestInstanceBlock import TestInstanceBlock
from vanilla_mcdoc.world.block.vault.Vault import Vault


class BlockEntityDataBanner(Banner):
    id: Literal['minecraft:banner', 'banner'] = 'minecraft:banner'


class BlockEntityDataBarrel(Container27):
    id: Literal['minecraft:barrel', 'barrel'] = 'minecraft:barrel'


class BlockEntityDataBeacon(Beacon):
    id: Literal['minecraft:beacon', 'beacon'] = 'minecraft:beacon'


class BlockEntityDataBeehive(Beehive):
    id: Literal['minecraft:beehive', 'beehive'] = 'minecraft:beehive'


class BlockEntityDataBlastFurnace(Furnace):
    id: Literal['minecraft:blast_furnace', 'blast_furnace'] = 'minecraft:blast_furnace'


class BlockEntityDataBrewingStand(BrewingStand):
    id: Literal['minecraft:brewing_stand', 'brewing_stand'] = 'minecraft:brewing_stand'


class BlockEntityDataBrushableBlock(BrushableBlock):
    id: Literal['minecraft:brushable_block', 'brushable_block'] = 'minecraft:brushable_block'


class BlockEntityDataCalibratedSculkSensor(SculkSensor):
    id: Literal['minecraft:calibrated_sculk_sensor', 'calibrated_sculk_sensor'] = 'minecraft:calibrated_sculk_sensor'


class BlockEntityDataCampfire(Campfire):
    id: Literal['minecraft:campfire', 'campfire'] = 'minecraft:campfire'


class BlockEntityDataChest(Container27):
    id: Literal['minecraft:chest', 'chest'] = 'minecraft:chest'


class BlockEntityDataChiseledBookshelf(ChiseledBookshelf):
    id: Literal['minecraft:chiseled_bookshelf', 'chiseled_bookshelf'] = 'minecraft:chiseled_bookshelf'


class BlockEntityDataCommandBlock(CommandBlock):
    id: Literal['minecraft:command_block', 'command_block'] = 'minecraft:command_block'


class BlockEntityDataComparator(Comparator):
    id: Literal['minecraft:comparator', 'comparator'] = 'minecraft:comparator'


class BlockEntityDataConduit(Conduit):
    id: Literal['minecraft:conduit', 'conduit'] = 'minecraft:conduit'


class BlockEntityDataCrafter(Crafter):
    id: Literal['minecraft:crafter', 'crafter'] = 'minecraft:crafter'


class BlockEntityDataCreakingHeart(CreakingHeart):
    id: Literal['minecraft:creaking_heart', 'creaking_heart'] = 'minecraft:creaking_heart'


class BlockEntityDataDecoratedPot(DecoratedPot):
    id: Literal['minecraft:decorated_pot', 'decorated_pot'] = 'minecraft:decorated_pot'


class BlockEntityDataDispenser(Container9):
    id: Literal['minecraft:dispenser', 'dispenser'] = 'minecraft:dispenser'


class BlockEntityDataDropper(Container9):
    id: Literal['minecraft:dropper', 'dropper'] = 'minecraft:dropper'


class BlockEntityDataEnchantingTable(EnchantingTable):
    id: Literal['minecraft:enchanting_table', 'enchanting_table'] = 'minecraft:enchanting_table'


class BlockEntityDataEndGateway(EndGateway):
    id: Literal['minecraft:end_gateway', 'end_gateway'] = 'minecraft:end_gateway'


class BlockEntityDataFurnace(Furnace):
    id: Literal['minecraft:furnace', 'furnace'] = 'minecraft:furnace'


class BlockEntityDataHangingSign(GeneratedModel):
    id: Literal['minecraft:hanging_sign', 'hanging_sign'] = 'minecraft:hanging_sign'


class BlockEntityDataHopper(Hopper):
    id: Literal['minecraft:hopper', 'hopper'] = 'minecraft:hopper'


class BlockEntityDataJigsaw(Jigsaw):
    id: Literal['minecraft:jigsaw', 'jigsaw'] = 'minecraft:jigsaw'


class BlockEntityDataJukebox(Jukebox):
    id: Literal['minecraft:jukebox', 'jukebox'] = 'minecraft:jukebox'


class BlockEntityDataLectern(Lectern):
    id: Literal['minecraft:lectern', 'lectern'] = 'minecraft:lectern'


class BlockEntityDataMobSpawner(Spawner):
    id: Literal['minecraft:mob_spawner', 'mob_spawner'] = 'minecraft:mob_spawner'


class BlockEntityDataMovingPiston(MovingPiston):
    id: Literal['minecraft:moving_piston', 'moving_piston'] = 'minecraft:moving_piston'


class BlockEntityDataPotentSulfur(PotentSulfur):
    id: Literal['minecraft:potent_sulfur', 'potent_sulfur'] = 'minecraft:potent_sulfur'


class BlockEntityDataSculkCatalyst(SculkCatalyst):
    id: Literal['minecraft:sculk_catalyst', 'sculk_catalyst'] = 'minecraft:sculk_catalyst'


class BlockEntityDataSculkSensor(SculkSensor):
    id: Literal['minecraft:sculk_sensor', 'sculk_sensor'] = 'minecraft:sculk_sensor'


class BlockEntityDataSculkShrieker(SculkShrieker):
    id: Literal['minecraft:sculk_shrieker', 'sculk_shrieker'] = 'minecraft:sculk_shrieker'


class BlockEntityDataShelf(Shelf):
    id: Literal['minecraft:shelf', 'shelf'] = 'minecraft:shelf'


class BlockEntityDataShulkerBox(Container27):
    id: Literal['minecraft:shulker_box', 'shulker_box'] = 'minecraft:shulker_box'


class BlockEntityDataSign(GeneratedModel):
    id: Literal['minecraft:sign', 'sign'] = 'minecraft:sign'


class BlockEntityDataSkull(Skull):
    id: Literal['minecraft:skull', 'skull'] = 'minecraft:skull'


class BlockEntityDataSmoker(Furnace):
    id: Literal['minecraft:smoker', 'smoker'] = 'minecraft:smoker'


class BlockEntityDataStructureBlock(StructureBlock):
    id: Literal['minecraft:structure_block', 'structure_block'] = 'minecraft:structure_block'


class BlockEntityDataTestBlock(TestBlock):
    id: Literal['minecraft:test_block', 'test_block'] = 'minecraft:test_block'


class BlockEntityDataTestInstanceBlock(TestInstanceBlock):
    id: Literal['minecraft:test_instance_block', 'test_instance_block'] = 'minecraft:test_instance_block'


class BlockEntityDataTrappedChest(Container27):
    id: Literal['minecraft:trapped_chest', 'trapped_chest'] = 'minecraft:trapped_chest'


class BlockEntityDataTrialSpawner(TrialSpawner):
    id: Literal['minecraft:trial_spawner', 'trial_spawner'] = 'minecraft:trial_spawner'


class BlockEntityDataVault(Vault):
    id: Literal['minecraft:vault', 'vault'] = 'minecraft:vault'


type BlockEntityData = Annotated[
    BlockEntityDataBanner | BlockEntityDataBarrel | BlockEntityDataBeacon | BlockEntityDataBeehive | BlockEntityDataBlastFurnace | BlockEntityDataBrewingStand | BlockEntityDataBrushableBlock | BlockEntityDataCalibratedSculkSensor | BlockEntityDataCampfire | BlockEntityDataChest | BlockEntityDataChiseledBookshelf | BlockEntityDataCommandBlock | BlockEntityDataComparator | BlockEntityDataConduit | BlockEntityDataCrafter | BlockEntityDataCreakingHeart | BlockEntityDataDecoratedPot | BlockEntityDataDispenser | BlockEntityDataDropper | BlockEntityDataEnchantingTable | BlockEntityDataEndGateway | BlockEntityDataFurnace | BlockEntityDataHangingSign | BlockEntityDataHopper | BlockEntityDataJigsaw | BlockEntityDataJukebox | BlockEntityDataLectern | BlockEntityDataMobSpawner | BlockEntityDataMovingPiston | BlockEntityDataPotentSulfur | BlockEntityDataSculkCatalyst | BlockEntityDataSculkSensor | BlockEntityDataSculkShrieker | BlockEntityDataShelf | BlockEntityDataShulkerBox | BlockEntityDataSign | BlockEntityDataSkull | BlockEntityDataSmoker | BlockEntityDataStructureBlock | BlockEntityDataTestBlock | BlockEntityDataTestInstanceBlock | BlockEntityDataTrappedChest | BlockEntityDataTrialSpawner | BlockEntityDataVault,
    Field(discriminator='id'),
]


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
