"""
Generated from symbols.json for ::java::world::block::BlockEntityData
Local link to file: vanilla_mcdoc/world/block/BlockEntityData.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Discriminator, Tag

from vanilla_mcdoc.base import GeneratedModel, tag_of
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


class BlockEntityDataBell(GeneratedModel):
    id: Literal['minecraft:bell', 'bell'] = 'minecraft:bell'


class BlockEntityDataCopperGolemStatue(GeneratedModel):
    id: Literal['minecraft:copper_golem_statue', 'copper_golem_statue'] = 'minecraft:copper_golem_statue'


class BlockEntityDataDaylightDetector(GeneratedModel):
    id: Literal['minecraft:daylight_detector', 'daylight_detector'] = 'minecraft:daylight_detector'


class BlockEntityDataEndPortal(GeneratedModel):
    id: Literal['minecraft:end_portal', 'end_portal'] = 'minecraft:end_portal'


class BlockEntityDataEnderChest(GeneratedModel):
    id: Literal['minecraft:ender_chest', 'ender_chest'] = 'minecraft:ender_chest'


class BlockEntityDataPiston(GeneratedModel):
    id: Literal['minecraft:piston', 'piston'] = 'minecraft:piston'


type BlockEntityData = Annotated[
    Annotated[BlockEntityDataBanner, Tag('minecraft:banner')]
    | Annotated[BlockEntityDataBarrel, Tag('minecraft:barrel')]
    | Annotated[BlockEntityDataBeacon, Tag('minecraft:beacon')]
    | Annotated[BlockEntityDataBeehive, Tag('minecraft:beehive')]
    | Annotated[BlockEntityDataBlastFurnace, Tag('minecraft:blast_furnace')]
    | Annotated[BlockEntityDataBrewingStand, Tag('minecraft:brewing_stand')]
    | Annotated[BlockEntityDataBrushableBlock, Tag('minecraft:brushable_block')]
    | Annotated[BlockEntityDataCalibratedSculkSensor, Tag('minecraft:calibrated_sculk_sensor')]
    | Annotated[BlockEntityDataCampfire, Tag('minecraft:campfire')]
    | Annotated[BlockEntityDataChest, Tag('minecraft:chest')]
    | Annotated[BlockEntityDataChiseledBookshelf, Tag('minecraft:chiseled_bookshelf')]
    | Annotated[BlockEntityDataCommandBlock, Tag('minecraft:command_block')]
    | Annotated[BlockEntityDataComparator, Tag('minecraft:comparator')]
    | Annotated[BlockEntityDataConduit, Tag('minecraft:conduit')]
    | Annotated[BlockEntityDataCrafter, Tag('minecraft:crafter')]
    | Annotated[BlockEntityDataCreakingHeart, Tag('minecraft:creaking_heart')]
    | Annotated[BlockEntityDataDecoratedPot, Tag('minecraft:decorated_pot')]
    | Annotated[BlockEntityDataDispenser, Tag('minecraft:dispenser')]
    | Annotated[BlockEntityDataDropper, Tag('minecraft:dropper')]
    | Annotated[BlockEntityDataEnchantingTable, Tag('minecraft:enchanting_table')]
    | Annotated[BlockEntityDataEndGateway, Tag('minecraft:end_gateway')]
    | Annotated[BlockEntityDataFurnace, Tag('minecraft:furnace')]
    | Annotated[BlockEntityDataHangingSign, Tag('minecraft:hanging_sign')]
    | Annotated[BlockEntityDataHopper, Tag('minecraft:hopper')]
    | Annotated[BlockEntityDataJigsaw, Tag('minecraft:jigsaw')]
    | Annotated[BlockEntityDataJukebox, Tag('minecraft:jukebox')]
    | Annotated[BlockEntityDataLectern, Tag('minecraft:lectern')]
    | Annotated[BlockEntityDataMobSpawner, Tag('minecraft:mob_spawner')]
    | Annotated[BlockEntityDataMovingPiston, Tag('minecraft:moving_piston')]
    | Annotated[BlockEntityDataPotentSulfur, Tag('minecraft:potent_sulfur')]
    | Annotated[BlockEntityDataSculkCatalyst, Tag('minecraft:sculk_catalyst')]
    | Annotated[BlockEntityDataSculkSensor, Tag('minecraft:sculk_sensor')]
    | Annotated[BlockEntityDataSculkShrieker, Tag('minecraft:sculk_shrieker')]
    | Annotated[BlockEntityDataShelf, Tag('minecraft:shelf')]
    | Annotated[BlockEntityDataShulkerBox, Tag('minecraft:shulker_box')]
    | Annotated[BlockEntityDataSign, Tag('minecraft:sign')]
    | Annotated[BlockEntityDataSkull, Tag('minecraft:skull')]
    | Annotated[BlockEntityDataSmoker, Tag('minecraft:smoker')]
    | Annotated[BlockEntityDataStructureBlock, Tag('minecraft:structure_block')]
    | Annotated[BlockEntityDataTestBlock, Tag('minecraft:test_block')]
    | Annotated[BlockEntityDataTestInstanceBlock, Tag('minecraft:test_instance_block')]
    | Annotated[BlockEntityDataTrappedChest, Tag('minecraft:trapped_chest')]
    | Annotated[BlockEntityDataTrialSpawner, Tag('minecraft:trial_spawner')]
    | Annotated[BlockEntityDataVault, Tag('minecraft:vault')]
    | Annotated[BlockEntityDataBell, Tag('minecraft:bell')]
    | Annotated[BlockEntityDataCopperGolemStatue, Tag('minecraft:copper_golem_statue')]
    | Annotated[BlockEntityDataDaylightDetector, Tag('minecraft:daylight_detector')]
    | Annotated[BlockEntityDataEndPortal, Tag('minecraft:end_portal')]
    | Annotated[BlockEntityDataEnderChest, Tag('minecraft:ender_chest')]
    | Annotated[BlockEntityDataPiston, Tag('minecraft:piston')],
    Discriminator(tag_of('id')),
]
