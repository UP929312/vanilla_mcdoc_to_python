"""
Generated from symbols.json for ::java::data::advancement::predicate::BlockPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/BlockPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.advancement.predicate.BlockPredicateState import BlockPredicateState
    from vanilla_mcdoc.registry.KnownBlockId import KnownBlockId
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
    from vanilla_mcdoc.world.component.DataComponentExactPredicate import DataComponentExactPredicate
    from vanilla_mcdoc.world.component.DataComponentPredicate import DataComponentPredicate


class NbtStructBlockUnknown(GeneratedModel):
    pass


class BlockPredicate(GeneratedModel):
    blocks: Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId | list[Annotated[str, IdSpec(registry='block')] | KnownBlockId] | None = None
    state: BlockPredicateState | None = None
    nbt: str | NbtStructBlockUnknown | Sign | Shelf | Container27 | Beacon | Beehive | BlockEntity | Banner | Furnace | BrewingStand | SculkSensor | Campfire | CommandBlock | ChiseledBookshelf | Comparator | Conduit | Crafter | Skull | DecoratedPot | Container9 | EnchantingTable | EndGateway | Hopper | Jigsaw | Jukebox | Lectern | MovingPiston | PotentSulfur | SculkCatalyst | SculkShrieker | Spawner | StructureBlock | BrushableBlock | TestBlock | TestInstanceBlock | TrialSpawner | Vault | None = None
    components: DataComponentExactPredicate | None = None  # Match exact data component values on the block entity.
    predicates: DataComponentPredicate | None = None  # Test data component values on the block entity.
