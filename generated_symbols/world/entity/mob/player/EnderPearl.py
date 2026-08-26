"""
Generated from symbols.json for ::java::world::entity::mob::player::EnderPearl
Local link to file: generated_symbols/world/entity/mob/player/EnderPearl.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated, Literal

from generated_symbols.world.entity.BlockAttachedEntity import BlockAttachedEntity
from generated_symbols.world.entity.area_effect_cloud.AreaEffectCloud import AreaEffectCloud
from generated_symbols.world.entity.boat.Boat import Boat
from generated_symbols.world.entity.boat.ChestBoat import ChestBoat
from generated_symbols.world.entity.cushion.Cushion import Cushion
from generated_symbols.world.entity.display.BlockDisplay import BlockDisplay
from generated_symbols.world.entity.display.ItemDisplay import ItemDisplay
from generated_symbols.world.entity.display.TextDisplay import TextDisplay
from generated_symbols.world.entity.end_crystal.EndCrystal import EndCrystal
from generated_symbols.world.entity.evoker_fangs.EvokerFangs import EvokerFangs
from generated_symbols.world.entity.experience_orb.ExperienceOrb import ExperienceOrb
from generated_symbols.world.entity.eye_of_ender.EyeOfEnder import EyeOfEnder
from generated_symbols.world.entity.falling_block.FallingBlock import FallingBlock
from generated_symbols.world.entity.interaction.Interaction import Interaction
from generated_symbols.world.entity.item.Item import Item
from generated_symbols.world.entity.item_frame.ItemFrame import ItemFrame
from generated_symbols.world.entity.marker.Marker import Marker
from generated_symbols.world.entity.minecart.ChestMinecart import ChestMinecart
from generated_symbols.world.entity.minecart.CommandBlockMinecart import CommandBlockMinecart
from generated_symbols.world.entity.minecart.FurnaceMinecart import FurnaceMinecart
from generated_symbols.world.entity.minecart.HopperMinecart import HopperMinecart
from generated_symbols.world.entity.minecart.Minecart import Minecart
from generated_symbols.world.entity.minecart.SpawnerMinecart import SpawnerMinecart
from generated_symbols.world.entity.minecart.TntMinecart import TntMinecart
from generated_symbols.world.entity.mob.MobBase import MobBase
from generated_symbols.world.entity.mob.Squid import Squid
from generated_symbols.world.entity.mob.allay.Allay import Allay
from generated_symbols.world.entity.mob.armor_stand.ArmorStand import ArmorStand
from generated_symbols.world.entity.mob.bat.Bat import Bat
from generated_symbols.world.entity.mob.bogged.Bogged import Bogged
from generated_symbols.world.entity.mob.breedable.Breedable import Breedable
from generated_symbols.world.entity.mob.breedable.armadillo.Armadillo import Armadillo
from generated_symbols.world.entity.mob.breedable.axolotl.Axolotl import Axolotl
from generated_symbols.world.entity.mob.breedable.bee.Bee import Bee
from generated_symbols.world.entity.mob.breedable.chicken.Chicken import Chicken
from generated_symbols.world.entity.mob.breedable.cow.Cow import Cow
from generated_symbols.world.entity.mob.breedable.fox.Fox import Fox
from generated_symbols.world.entity.mob.breedable.frog.Frog import Frog
from generated_symbols.world.entity.mob.breedable.goat.Goat import Goat
from generated_symbols.world.entity.mob.breedable.hoglin.Hoglin import Hoglin
from generated_symbols.world.entity.mob.breedable.horse.Camel import Camel
from generated_symbols.world.entity.mob.breedable.horse.ChestedHorse import ChestedHorse
from generated_symbols.world.entity.mob.breedable.horse.Horse import Horse
from generated_symbols.world.entity.mob.breedable.horse.HorseBase import HorseBase
from generated_symbols.world.entity.mob.breedable.horse.Llama import Llama
from generated_symbols.world.entity.mob.breedable.horse.SkeletonHorse import SkeletonHorse
from generated_symbols.world.entity.mob.breedable.horse.TraderLlama import TraderLlama
from generated_symbols.world.entity.mob.breedable.mooshroom.Mooshroom import Mooshroom
from generated_symbols.world.entity.mob.breedable.ocelot.Ocelot import Ocelot
from generated_symbols.world.entity.mob.breedable.panda.Panda import Panda
from generated_symbols.world.entity.mob.breedable.polar_bear.PolarBear import PolarBear
from generated_symbols.world.entity.mob.breedable.rabbit.Rabbit import Rabbit
from generated_symbols.world.entity.mob.breedable.saddled.Pig import Pig
from generated_symbols.world.entity.mob.breedable.saddled.Saddled import Saddled
from generated_symbols.world.entity.mob.breedable.sheep.Sheep import Sheep
from generated_symbols.world.entity.mob.breedable.tamable.Cat import Cat
from generated_symbols.world.entity.mob.breedable.tamable.Parrot import Parrot
from generated_symbols.world.entity.mob.breedable.tamable.Tamable import Tamable
from generated_symbols.world.entity.mob.breedable.tamable.Wolf import Wolf
from generated_symbols.world.entity.mob.breedable.turtle.Turtle import Turtle
from generated_symbols.world.entity.mob.breedable.villager.Villager import Villager
from generated_symbols.world.entity.mob.breedable.villager.WanderingTrader import WanderingTrader
from generated_symbols.world.entity.mob.copper_golem.CopperGolem import CopperGolem
from generated_symbols.world.entity.mob.creaking.Creaking import Creaking
from generated_symbols.world.entity.mob.creeper.Creeper import Creeper
from generated_symbols.world.entity.mob.dolphin.Dolphin import Dolphin
from generated_symbols.world.entity.mob.ender_dragon.EnderDragon import EnderDragon
from generated_symbols.world.entity.mob.enderman.Enderman import Enderman
from generated_symbols.world.entity.mob.endermite.Endermite import Endermite
from generated_symbols.world.entity.mob.fish.Fish import Fish
from generated_symbols.world.entity.mob.fish.Pufferfish import Pufferfish
from generated_symbols.world.entity.mob.fish.Salmon import Salmon
from generated_symbols.world.entity.mob.fish.TropicalFish import TropicalFish
from generated_symbols.world.entity.mob.ghast.Ghast import Ghast
from generated_symbols.world.entity.mob.glow_squid.GlowSquid import GlowSquid
from generated_symbols.world.entity.mob.happy_ghast.HappyGhast import HappyGhast
from generated_symbols.world.entity.mob.iron_golem.IronGolem import IronGolem
from generated_symbols.world.entity.mob.mannequin.Mannequin import Mannequin
from generated_symbols.world.entity.mob.phantom.Phantom import Phantom
from generated_symbols.world.entity.mob.piglin.Piglin import Piglin
from generated_symbols.world.entity.mob.piglin.PiglinBase import PiglinBase
from generated_symbols.world.entity.mob.player.Player import Player
from generated_symbols.world.entity.mob.raider.Pillager import Pillager
from generated_symbols.world.entity.mob.raider.RaiderBase import RaiderBase
from generated_symbols.world.entity.mob.raider.Ravager import Ravager
from generated_symbols.world.entity.mob.raider.Spellcaster import Spellcaster
from generated_symbols.world.entity.mob.raider.Vindicator import Vindicator
from generated_symbols.world.entity.mob.shulker.Shulker import Shulker
from generated_symbols.world.entity.mob.skeleton.Skeleton import Skeleton
from generated_symbols.world.entity.mob.slime.Slime import Slime
from generated_symbols.world.entity.mob.slime.SulfurCube import SulfurCube
from generated_symbols.world.entity.mob.snow_golem.SnowGolem import SnowGolem
from generated_symbols.world.entity.mob.tadpole.Tadpole import Tadpole
from generated_symbols.world.entity.mob.vex.Vex import Vex
from generated_symbols.world.entity.mob.warden.Warden import Warden
from generated_symbols.world.entity.mob.wither.Wither import Wither
from generated_symbols.world.entity.mob.zoglin.Zoglin import Zoglin
from generated_symbols.world.entity.mob.zombie.Zombie import Zombie
from generated_symbols.world.entity.mob.zombie.ZombieVillager import ZombieVillager
from generated_symbols.world.entity.mob.zombified_piglin.ZombiePigman import ZombiePigman
from generated_symbols.world.entity.ominous_item_spawner.OminousItemSpawner import OminousItemSpawner
from generated_symbols.world.entity.painting.Painting import Painting
from generated_symbols.world.entity.projectile.LlamaSpit import LlamaSpit
from generated_symbols.world.entity.projectile.arrow.Arrow import Arrow
from generated_symbols.world.entity.projectile.arrow.SpectralArrow import SpectralArrow
from generated_symbols.world.entity.projectile.arrow.Trident import Trident
from generated_symbols.world.entity.projectile.fireball.AcceleratingProjectileBase import AcceleratingProjectileBase
from generated_symbols.world.entity.projectile.fireball.DespawnableProjectileBase import DespawnableProjectileBase
from generated_symbols.world.entity.projectile.fireball.FireballBase import FireballBase
from generated_symbols.world.entity.projectile.fireball.LargeFireball import LargeFireball
from generated_symbols.world.entity.projectile.fireball.WitherSkull import WitherSkull
from generated_symbols.world.entity.projectile.firework_rocket.FireWorkRocket import FireWorkRocket
from generated_symbols.world.entity.projectile.shulker_bullet.ShulkerBullet import ShulkerBullet
from generated_symbols.world.entity.projectile.throwable.Potion import Potion
from generated_symbols.world.entity.projectile.throwable.ThrowableItem import ThrowableItem
from generated_symbols.world.entity.tnt.Tnt import Tnt
from minecraft_registry import IdSpec


@dataclass(kw_only=True)
class EnderPearlAcaciaBoat(Boat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:acacia_boat'] = 'minecraft:acacia_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlAcaciaChestBoat(ChestBoat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:acacia_chest_boat'] = 'minecraft:acacia_chest_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlAllay(Allay):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:allay'] = 'minecraft:allay'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlAreaEffectCloud(AreaEffectCloud):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:area_effect_cloud'] = 'minecraft:area_effect_cloud'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlArmadillo(Armadillo):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:armadillo'] = 'minecraft:armadillo'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlArmorStand(ArmorStand):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:armor_stand'] = 'minecraft:armor_stand'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlArrow(Arrow):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:arrow'] = 'minecraft:arrow'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlAxolotl(Axolotl):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:axolotl'] = 'minecraft:axolotl'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlBambooChestRaft(ChestBoat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:bamboo_chest_raft'] = 'minecraft:bamboo_chest_raft'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlBambooRaft(Boat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:bamboo_raft'] = 'minecraft:bamboo_raft'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlBat(Bat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:bat'] = 'minecraft:bat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlBee(Bee):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:bee'] = 'minecraft:bee'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlBirchBoat(Boat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:birch_boat'] = 'minecraft:birch_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlBirchChestBoat(ChestBoat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:birch_chest_boat'] = 'minecraft:birch_chest_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlBlaze(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:blaze'] = 'minecraft:blaze'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlBlockDisplay(BlockDisplay):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:block_display'] = 'minecraft:block_display'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlBogged(Bogged):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:bogged'] = 'minecraft:bogged'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlBreeze(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:breeze'] = 'minecraft:breeze'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlBreezeWindCharge(AcceleratingProjectileBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:breeze_wind_charge'] = 'minecraft:breeze_wind_charge'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlCamel(Camel):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:camel'] = 'minecraft:camel'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlCamelHusk(Camel):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:camel_husk'] = 'minecraft:camel_husk'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlCat(Cat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:cat'] = 'minecraft:cat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlCaveSpider(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:cave_spider'] = 'minecraft:cave_spider'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlCherryBoat(Boat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:cherry_boat'] = 'minecraft:cherry_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlCherryChestBoat(ChestBoat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:cherry_chest_boat'] = 'minecraft:cherry_chest_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlChestMinecart(ChestMinecart):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:chest_minecart'] = 'minecraft:chest_minecart'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlChicken(Chicken):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:chicken'] = 'minecraft:chicken'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlCod(Fish):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:cod'] = 'minecraft:cod'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlCommandBlockMinecart(CommandBlockMinecart):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:command_block_minecart'] = 'minecraft:command_block_minecart'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlCopperGolem(CopperGolem):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:copper_golem'] = 'minecraft:copper_golem'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlCow(Cow):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:cow'] = 'minecraft:cow'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlCreaking(Creaking):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:creaking'] = 'minecraft:creaking'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlCreeper(Creeper):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:creeper'] = 'minecraft:creeper'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlCushion(Cushion):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:cushion'] = 'minecraft:cushion'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlDarkOakBoat(Boat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:dark_oak_boat'] = 'minecraft:dark_oak_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlDarkOakChestBoat(ChestBoat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:dark_oak_chest_boat'] = 'minecraft:dark_oak_chest_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlDolphin(Dolphin):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:dolphin'] = 'minecraft:dolphin'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlDonkey(ChestedHorse):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:donkey'] = 'minecraft:donkey'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlDragonFireball(DespawnableProjectileBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:dragon_fireball'] = 'minecraft:dragon_fireball'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlDrowned(Zombie):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:drowned'] = 'minecraft:drowned'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlEgg(ThrowableItem):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:egg'] = 'minecraft:egg'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlElderGuardian(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:elder_guardian'] = 'minecraft:elder_guardian'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlEndCrystal(EndCrystal):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:end_crystal'] = 'minecraft:end_crystal'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlEnderDragon(EnderDragon):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:ender_dragon'] = 'minecraft:ender_dragon'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlEnderPearl(ThrowableItem):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:ender_pearl'] = 'minecraft:ender_pearl'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlEnderman(Enderman):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:enderman'] = 'minecraft:enderman'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlEndermite(Endermite):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:endermite'] = 'minecraft:endermite'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlEvoker(Spellcaster):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:evoker'] = 'minecraft:evoker'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlEvokerFangs(EvokerFangs):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:evoker_fangs'] = 'minecraft:evoker_fangs'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlExperienceBottle(ThrowableItem):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:experience_bottle'] = 'minecraft:experience_bottle'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlExperienceOrb(ExperienceOrb):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:experience_orb'] = 'minecraft:experience_orb'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlEyeOfEnder(EyeOfEnder):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:eye_of_ender'] = 'minecraft:eye_of_ender'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlFallingBlock(FallingBlock):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:falling_block'] = 'minecraft:falling_block'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlFireball(LargeFireball):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:fireball'] = 'minecraft:fireball'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlFireworkRocket(FireWorkRocket):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:firework_rocket'] = 'minecraft:firework_rocket'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlFox(Fox):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:fox'] = 'minecraft:fox'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlFrog(Frog):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:frog'] = 'minecraft:frog'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlFurnaceMinecart(FurnaceMinecart):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:furnace_minecart'] = 'minecraft:furnace_minecart'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlGhast(Ghast):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:ghast'] = 'minecraft:ghast'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlGiant(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:giant'] = 'minecraft:giant'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlGlowItemFrame(ItemFrame):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:glow_item_frame'] = 'minecraft:glow_item_frame'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlGlowSquid(GlowSquid):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:glow_squid'] = 'minecraft:glow_squid'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlGoat(Goat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:goat'] = 'minecraft:goat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlGuardian(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:guardian'] = 'minecraft:guardian'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlHappyGhast(HappyGhast):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:happy_ghast'] = 'minecraft:happy_ghast'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlHoglin(Hoglin):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:hoglin'] = 'minecraft:hoglin'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlHopperMinecart(HopperMinecart):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:hopper_minecart'] = 'minecraft:hopper_minecart'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlHorse(Horse):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:horse'] = 'minecraft:horse'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlHusk(Zombie):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:husk'] = 'minecraft:husk'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlIllusioner(Spellcaster):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:illusioner'] = 'minecraft:illusioner'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlInteraction(Interaction):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:interaction'] = 'minecraft:interaction'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlIronGolem(IronGolem):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:iron_golem'] = 'minecraft:iron_golem'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlItem(Item):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:item'] = 'minecraft:item'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlItemDisplay(ItemDisplay):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:item_display'] = 'minecraft:item_display'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlItemFrame(ItemFrame):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:item_frame'] = 'minecraft:item_frame'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlJungleBoat(Boat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:jungle_boat'] = 'minecraft:jungle_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlJungleChestBoat(ChestBoat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:jungle_chest_boat'] = 'minecraft:jungle_chest_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlLeashKnot(BlockAttachedEntity):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:leash_knot'] = 'minecraft:leash_knot'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlLingeringPotion(Potion):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:lingering_potion'] = 'minecraft:lingering_potion'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlLlama(Llama):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:llama'] = 'minecraft:llama'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlLlamaSpit(LlamaSpit):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:llama_spit'] = 'minecraft:llama_spit'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlMagmaCube(Slime):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:magma_cube'] = 'minecraft:magma_cube'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlMangroveBoat(Boat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:mangrove_boat'] = 'minecraft:mangrove_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlMangroveChestBoat(ChestBoat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:mangrove_chest_boat'] = 'minecraft:mangrove_chest_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlMannequin(Mannequin):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:mannequin'] = 'minecraft:mannequin'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlMarker(Marker):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:marker'] = 'minecraft:marker'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlMinecart(Minecart):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:minecart'] = 'minecraft:minecart'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlMooshroom(Mooshroom):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:mooshroom'] = 'minecraft:mooshroom'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlMule(ChestedHorse):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:mule'] = 'minecraft:mule'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlNautilus(Tamable):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:nautilus'] = 'minecraft:nautilus'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlOakBoat(Boat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:oak_boat'] = 'minecraft:oak_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlOakChestBoat(ChestBoat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:oak_chest_boat'] = 'minecraft:oak_chest_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlOcelot(Ocelot):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:ocelot'] = 'minecraft:ocelot'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlOminousItemSpawner(OminousItemSpawner):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:ominous_item_spawner'] = 'minecraft:ominous_item_spawner'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlPainting(Painting):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:painting'] = 'minecraft:painting'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlPaleOakBoat(Boat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:pale_oak_boat'] = 'minecraft:pale_oak_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlPaleOakChestBoat(ChestBoat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:pale_oak_chest_boat'] = 'minecraft:pale_oak_chest_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlPanda(Panda):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:panda'] = 'minecraft:panda'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlParched(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:parched'] = 'minecraft:parched'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlParrot(Parrot):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:parrot'] = 'minecraft:parrot'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlPhantom(Phantom):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:phantom'] = 'minecraft:phantom'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlPig(Pig):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:pig'] = 'minecraft:pig'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlPiglin(Piglin):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:piglin'] = 'minecraft:piglin'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlPiglinBrute(PiglinBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:piglin_brute'] = 'minecraft:piglin_brute'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlPillager(Pillager):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:pillager'] = 'minecraft:pillager'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlPlayer(Player):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:player'] = 'minecraft:player'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlPolarBear(PolarBear):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:polar_bear'] = 'minecraft:polar_bear'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlPoplarBoat(Boat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:poplar_boat'] = 'minecraft:poplar_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlPopolarChestBoat(ChestBoat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:popolar_chest_boat'] = 'minecraft:popolar_chest_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlPotion(Potion):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:potion'] = 'minecraft:potion'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlPufferfish(Pufferfish):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:pufferfish'] = 'minecraft:pufferfish'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlRabbit(Rabbit):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:rabbit'] = 'minecraft:rabbit'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlRavager(Ravager):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:ravager'] = 'minecraft:ravager'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlSalmon(Salmon):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:salmon'] = 'minecraft:salmon'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlSheep(Sheep):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:sheep'] = 'minecraft:sheep'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlShulker(Shulker):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:shulker'] = 'minecraft:shulker'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlShulkerBullet(ShulkerBullet):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:shulker_bullet'] = 'minecraft:shulker_bullet'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlSilverfish(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:silverfish'] = 'minecraft:silverfish'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlSkeleton(Skeleton):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:skeleton'] = 'minecraft:skeleton'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlSkeletonHorse(SkeletonHorse):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:skeleton_horse'] = 'minecraft:skeleton_horse'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlSlime(Slime):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:slime'] = 'minecraft:slime'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlSmallFireball(FireballBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:small_fireball'] = 'minecraft:small_fireball'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlSniffer(Breedable):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:sniffer'] = 'minecraft:sniffer'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlSnowGolem(SnowGolem):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:snow_golem'] = 'minecraft:snow_golem'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlSnowball(ThrowableItem):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:snowball'] = 'minecraft:snowball'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlSpawnerMinecart(SpawnerMinecart):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:spawner_minecart'] = 'minecraft:spawner_minecart'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlSpectralArrow(SpectralArrow):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:spectral_arrow'] = 'minecraft:spectral_arrow'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlSpider(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:spider'] = 'minecraft:spider'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlSplashPotion(Potion):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:splash_potion'] = 'minecraft:splash_potion'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlSpruceBoat(Boat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:spruce_boat'] = 'minecraft:spruce_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlSpruceChestBoat(ChestBoat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:spruce_chest_boat'] = 'minecraft:spruce_chest_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlSquid(Squid):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:squid'] = 'minecraft:squid'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlStray(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:stray'] = 'minecraft:stray'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlStrider(Saddled):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:strider'] = 'minecraft:strider'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlSulfurCube(SulfurCube):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:sulfur_cube'] = 'minecraft:sulfur_cube'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlTadpole(Tadpole):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:tadpole'] = 'minecraft:tadpole'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlTextDisplay(TextDisplay):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:text_display'] = 'minecraft:text_display'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlTnt(Tnt):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:tnt'] = 'minecraft:tnt'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlTntMinecart(TntMinecart):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:tnt_minecart'] = 'minecraft:tnt_minecart'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlTraderLlama(TraderLlama):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:trader_llama'] = 'minecraft:trader_llama'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlTrident(Trident):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:trident'] = 'minecraft:trident'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlTropicalFish(TropicalFish):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:tropical_fish'] = 'minecraft:tropical_fish'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlTurtle(Turtle):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:turtle'] = 'minecraft:turtle'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlVex(Vex):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:vex'] = 'minecraft:vex'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlVillager(Villager):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:villager'] = 'minecraft:villager'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlVindicator(Vindicator):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:vindicator'] = 'minecraft:vindicator'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlWanderingTrader(WanderingTrader):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:wandering_trader'] = 'minecraft:wandering_trader'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlWarden(Warden):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:warden'] = 'minecraft:warden'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlWitch(RaiderBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:witch'] = 'minecraft:witch'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlWither(Wither):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:wither'] = 'minecraft:wither'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlWitherSkeleton(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:wither_skeleton'] = 'minecraft:wither_skeleton'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlWitherSkull(WitherSkull):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:wither_skull'] = 'minecraft:wither_skull'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlWolf(Wolf):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:wolf'] = 'minecraft:wolf'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlZoglin(Zoglin):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:zoglin'] = 'minecraft:zoglin'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlZombie(Zombie):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:zombie'] = 'minecraft:zombie'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlZombieHorse(HorseBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:zombie_horse'] = 'minecraft:zombie_horse'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlZombieNautilus(Tamable):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:zombie_nautilus'] = 'minecraft:zombie_nautilus'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlZombieVillager(ZombieVillager):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:zombie_villager'] = 'minecraft:zombie_villager'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class EnderPearlZombifiedPiglin(ZombiePigman):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:zombified_piglin'] = 'minecraft:zombified_piglin'  # The ID of this entity. Not present on player entities.


type EnderPearl = EnderPearlAcaciaBoat | EnderPearlAcaciaChestBoat | EnderPearlAllay | EnderPearlAreaEffectCloud | EnderPearlArmadillo | EnderPearlArmorStand | EnderPearlArrow | EnderPearlAxolotl | EnderPearlBambooChestRaft | EnderPearlBambooRaft | EnderPearlBat | EnderPearlBee | EnderPearlBirchBoat | EnderPearlBirchChestBoat | EnderPearlBlaze | EnderPearlBlockDisplay | EnderPearlBogged | EnderPearlBreeze | EnderPearlBreezeWindCharge | EnderPearlCamel | EnderPearlCamelHusk | EnderPearlCat | EnderPearlCaveSpider | EnderPearlCherryBoat | EnderPearlCherryChestBoat | EnderPearlChestMinecart | EnderPearlChicken | EnderPearlCod | EnderPearlCommandBlockMinecart | EnderPearlCopperGolem | EnderPearlCow | EnderPearlCreaking | EnderPearlCreeper | EnderPearlCushion | EnderPearlDarkOakBoat | EnderPearlDarkOakChestBoat | EnderPearlDolphin | EnderPearlDonkey | EnderPearlDragonFireball | EnderPearlDrowned | EnderPearlEgg | EnderPearlElderGuardian | EnderPearlEndCrystal | EnderPearlEnderDragon | EnderPearlEnderPearl | EnderPearlEnderman | EnderPearlEndermite | EnderPearlEvoker | EnderPearlEvokerFangs | EnderPearlExperienceBottle | EnderPearlExperienceOrb | EnderPearlEyeOfEnder | EnderPearlFallingBlock | EnderPearlFireball | EnderPearlFireworkRocket | EnderPearlFox | EnderPearlFrog | EnderPearlFurnaceMinecart | EnderPearlGhast | EnderPearlGiant | EnderPearlGlowItemFrame | EnderPearlGlowSquid | EnderPearlGoat | EnderPearlGuardian | EnderPearlHappyGhast | EnderPearlHoglin | EnderPearlHopperMinecart | EnderPearlHorse | EnderPearlHusk | EnderPearlIllusioner | EnderPearlInteraction | EnderPearlIronGolem | EnderPearlItem | EnderPearlItemDisplay | EnderPearlItemFrame | EnderPearlJungleBoat | EnderPearlJungleChestBoat | EnderPearlLeashKnot | EnderPearlLingeringPotion | EnderPearlLlama | EnderPearlLlamaSpit | EnderPearlMagmaCube | EnderPearlMangroveBoat | EnderPearlMangroveChestBoat | EnderPearlMannequin | EnderPearlMarker | EnderPearlMinecart | EnderPearlMooshroom | EnderPearlMule | EnderPearlNautilus | EnderPearlOakBoat | EnderPearlOakChestBoat | EnderPearlOcelot | EnderPearlOminousItemSpawner | EnderPearlPainting | EnderPearlPaleOakBoat | EnderPearlPaleOakChestBoat | EnderPearlPanda | EnderPearlParched | EnderPearlParrot | EnderPearlPhantom | EnderPearlPig | EnderPearlPiglin | EnderPearlPiglinBrute | EnderPearlPillager | EnderPearlPlayer | EnderPearlPolarBear | EnderPearlPoplarBoat | EnderPearlPopolarChestBoat | EnderPearlPotion | EnderPearlPufferfish | EnderPearlRabbit | EnderPearlRavager | EnderPearlSalmon | EnderPearlSheep | EnderPearlShulker | EnderPearlShulkerBullet | EnderPearlSilverfish | EnderPearlSkeleton | EnderPearlSkeletonHorse | EnderPearlSlime | EnderPearlSmallFireball | EnderPearlSniffer | EnderPearlSnowGolem | EnderPearlSnowball | EnderPearlSpawnerMinecart | EnderPearlSpectralArrow | EnderPearlSpider | EnderPearlSplashPotion | EnderPearlSpruceBoat | EnderPearlSpruceChestBoat | EnderPearlSquid | EnderPearlStray | EnderPearlStrider | EnderPearlSulfurCube | EnderPearlTadpole | EnderPearlTextDisplay | EnderPearlTnt | EnderPearlTntMinecart | EnderPearlTraderLlama | EnderPearlTrident | EnderPearlTropicalFish | EnderPearlTurtle | EnderPearlVex | EnderPearlVillager | EnderPearlVindicator | EnderPearlWanderingTrader | EnderPearlWarden | EnderPearlWitch | EnderPearlWither | EnderPearlWitherSkeleton | EnderPearlWitherSkull | EnderPearlWolf | EnderPearlZoglin | EnderPearlZombie | EnderPearlZombieHorse | EnderPearlZombieNautilus | EnderPearlZombieVillager | EnderPearlZombifiedPiglin


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::player::EnderPearl": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "ender_pearl_dimension",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "dimension"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::AnyEntity"
                }
            }
        ]
    }
}

