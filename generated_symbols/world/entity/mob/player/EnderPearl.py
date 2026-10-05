"""
Generated from symbols.json for ::java::world::entity::mob::player::EnderPearl
Local link to file: generated_symbols/world/entity/mob/player/EnderPearl.py
"""
# ~~~ CODE ~~~
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
from pydantic import Field


class EnderPearlAcaciaBoat(Boat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:acacia_boat'] = 'minecraft:acacia_boat'  # The ID of this entity. Not present on player entities.


class EnderPearlAcaciaChestBoat(ChestBoat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:acacia_chest_boat'] = 'minecraft:acacia_chest_boat'  # The ID of this entity. Not present on player entities.


class EnderPearlAllay(Allay):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:allay'] = 'minecraft:allay'  # The ID of this entity. Not present on player entities.


class EnderPearlAreaEffectCloud(AreaEffectCloud):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:area_effect_cloud'] = 'minecraft:area_effect_cloud'  # The ID of this entity. Not present on player entities.


class EnderPearlArmadillo(Armadillo):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:armadillo'] = 'minecraft:armadillo'  # The ID of this entity. Not present on player entities.


class EnderPearlArmorStand(ArmorStand):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:armor_stand'] = 'minecraft:armor_stand'  # The ID of this entity. Not present on player entities.


class EnderPearlArrow(Arrow):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:arrow'] = 'minecraft:arrow'  # The ID of this entity. Not present on player entities.


class EnderPearlAxolotl(Axolotl):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:axolotl'] = 'minecraft:axolotl'  # The ID of this entity. Not present on player entities.


class EnderPearlBambooChestRaft(ChestBoat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:bamboo_chest_raft'] = 'minecraft:bamboo_chest_raft'  # The ID of this entity. Not present on player entities.


class EnderPearlBambooRaft(Boat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:bamboo_raft'] = 'minecraft:bamboo_raft'  # The ID of this entity. Not present on player entities.


class EnderPearlBat(Bat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:bat'] = 'minecraft:bat'  # The ID of this entity. Not present on player entities.


class EnderPearlBee(Bee):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:bee'] = 'minecraft:bee'  # The ID of this entity. Not present on player entities.


class EnderPearlBirchBoat(Boat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:birch_boat'] = 'minecraft:birch_boat'  # The ID of this entity. Not present on player entities.


class EnderPearlBirchChestBoat(ChestBoat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:birch_chest_boat'] = 'minecraft:birch_chest_boat'  # The ID of this entity. Not present on player entities.


class EnderPearlBlaze(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:blaze'] = 'minecraft:blaze'  # The ID of this entity. Not present on player entities.


class EnderPearlBlockDisplay(BlockDisplay):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:block_display'] = 'minecraft:block_display'  # The ID of this entity. Not present on player entities.


class EnderPearlBogged(Bogged):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:bogged'] = 'minecraft:bogged'  # The ID of this entity. Not present on player entities.


class EnderPearlBreeze(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:breeze'] = 'minecraft:breeze'  # The ID of this entity. Not present on player entities.


class EnderPearlBreezeWindCharge(AcceleratingProjectileBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:breeze_wind_charge'] = 'minecraft:breeze_wind_charge'  # The ID of this entity. Not present on player entities.


class EnderPearlCamel(Camel):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:camel'] = 'minecraft:camel'  # The ID of this entity. Not present on player entities.


class EnderPearlCamelHusk(Camel):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:camel_husk'] = 'minecraft:camel_husk'  # The ID of this entity. Not present on player entities.


class EnderPearlCat(Cat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:cat'] = 'minecraft:cat'  # The ID of this entity. Not present on player entities.


class EnderPearlCaveSpider(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:cave_spider'] = 'minecraft:cave_spider'  # The ID of this entity. Not present on player entities.


class EnderPearlCherryBoat(Boat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:cherry_boat'] = 'minecraft:cherry_boat'  # The ID of this entity. Not present on player entities.


class EnderPearlCherryChestBoat(ChestBoat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:cherry_chest_boat'] = 'minecraft:cherry_chest_boat'  # The ID of this entity. Not present on player entities.


class EnderPearlChestMinecart(ChestMinecart):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:chest_minecart'] = 'minecraft:chest_minecart'  # The ID of this entity. Not present on player entities.


class EnderPearlChicken(Chicken):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:chicken'] = 'minecraft:chicken'  # The ID of this entity. Not present on player entities.


class EnderPearlCod(Fish):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:cod'] = 'minecraft:cod'  # The ID of this entity. Not present on player entities.


class EnderPearlCommandBlockMinecart(CommandBlockMinecart):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:command_block_minecart'] = 'minecraft:command_block_minecart'  # The ID of this entity. Not present on player entities.


class EnderPearlCopperGolem(CopperGolem):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:copper_golem'] = 'minecraft:copper_golem'  # The ID of this entity. Not present on player entities.


class EnderPearlCow(Cow):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:cow'] = 'minecraft:cow'  # The ID of this entity. Not present on player entities.


class EnderPearlCreaking(Creaking):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:creaking'] = 'minecraft:creaking'  # The ID of this entity. Not present on player entities.


class EnderPearlCreeper(Creeper):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:creeper'] = 'minecraft:creeper'  # The ID of this entity. Not present on player entities.


class EnderPearlCushion(Cushion):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:cushion'] = 'minecraft:cushion'  # The ID of this entity. Not present on player entities.


class EnderPearlDarkOakBoat(Boat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:dark_oak_boat'] = 'minecraft:dark_oak_boat'  # The ID of this entity. Not present on player entities.


class EnderPearlDarkOakChestBoat(ChestBoat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:dark_oak_chest_boat'] = 'minecraft:dark_oak_chest_boat'  # The ID of this entity. Not present on player entities.


class EnderPearlDolphin(Dolphin):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:dolphin'] = 'minecraft:dolphin'  # The ID of this entity. Not present on player entities.


class EnderPearlDonkey(ChestedHorse):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:donkey'] = 'minecraft:donkey'  # The ID of this entity. Not present on player entities.


class EnderPearlDragonFireball(DespawnableProjectileBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:dragon_fireball'] = 'minecraft:dragon_fireball'  # The ID of this entity. Not present on player entities.


class EnderPearlDrowned(Zombie):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:drowned'] = 'minecraft:drowned'  # The ID of this entity. Not present on player entities.


class EnderPearlEgg(ThrowableItem):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:egg'] = 'minecraft:egg'  # The ID of this entity. Not present on player entities.


class EnderPearlElderGuardian(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:elder_guardian'] = 'minecraft:elder_guardian'  # The ID of this entity. Not present on player entities.


class EnderPearlEndCrystal(EndCrystal):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:end_crystal'] = 'minecraft:end_crystal'  # The ID of this entity. Not present on player entities.


class EnderPearlEnderDragon(EnderDragon):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:ender_dragon'] = 'minecraft:ender_dragon'  # The ID of this entity. Not present on player entities.


class EnderPearlEnderPearl(ThrowableItem):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:ender_pearl'] = 'minecraft:ender_pearl'  # The ID of this entity. Not present on player entities.


class EnderPearlEnderman(Enderman):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:enderman'] = 'minecraft:enderman'  # The ID of this entity. Not present on player entities.


class EnderPearlEndermite(Endermite):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:endermite'] = 'minecraft:endermite'  # The ID of this entity. Not present on player entities.


class EnderPearlEvoker(Spellcaster):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:evoker'] = 'minecraft:evoker'  # The ID of this entity. Not present on player entities.


class EnderPearlEvokerFangs(EvokerFangs):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:evoker_fangs'] = 'minecraft:evoker_fangs'  # The ID of this entity. Not present on player entities.


class EnderPearlExperienceBottle(ThrowableItem):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:experience_bottle'] = 'minecraft:experience_bottle'  # The ID of this entity. Not present on player entities.


class EnderPearlExperienceOrb(ExperienceOrb):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:experience_orb'] = 'minecraft:experience_orb'  # The ID of this entity. Not present on player entities.


class EnderPearlEyeOfEnder(EyeOfEnder):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:eye_of_ender'] = 'minecraft:eye_of_ender'  # The ID of this entity. Not present on player entities.


class EnderPearlFallingBlock(FallingBlock):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:falling_block'] = 'minecraft:falling_block'  # The ID of this entity. Not present on player entities.


class EnderPearlFireball(LargeFireball):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:fireball'] = 'minecraft:fireball'  # The ID of this entity. Not present on player entities.


class EnderPearlFireworkRocket(FireWorkRocket):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:firework_rocket'] = 'minecraft:firework_rocket'  # The ID of this entity. Not present on player entities.


class EnderPearlFox(Fox):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:fox'] = 'minecraft:fox'  # The ID of this entity. Not present on player entities.


class EnderPearlFrog(Frog):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:frog'] = 'minecraft:frog'  # The ID of this entity. Not present on player entities.


class EnderPearlFurnaceMinecart(FurnaceMinecart):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:furnace_minecart'] = 'minecraft:furnace_minecart'  # The ID of this entity. Not present on player entities.


class EnderPearlGhast(Ghast):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:ghast'] = 'minecraft:ghast'  # The ID of this entity. Not present on player entities.


class EnderPearlGiant(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:giant'] = 'minecraft:giant'  # The ID of this entity. Not present on player entities.


class EnderPearlGlowItemFrame(ItemFrame):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:glow_item_frame'] = 'minecraft:glow_item_frame'  # The ID of this entity. Not present on player entities.


class EnderPearlGlowSquid(GlowSquid):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:glow_squid'] = 'minecraft:glow_squid'  # The ID of this entity. Not present on player entities.


class EnderPearlGoat(Goat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:goat'] = 'minecraft:goat'  # The ID of this entity. Not present on player entities.


class EnderPearlGuardian(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:guardian'] = 'minecraft:guardian'  # The ID of this entity. Not present on player entities.


class EnderPearlHappyGhast(HappyGhast):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:happy_ghast'] = 'minecraft:happy_ghast'  # The ID of this entity. Not present on player entities.


class EnderPearlHoglin(Hoglin):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:hoglin'] = 'minecraft:hoglin'  # The ID of this entity. Not present on player entities.


class EnderPearlHopperMinecart(HopperMinecart):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:hopper_minecart'] = 'minecraft:hopper_minecart'  # The ID of this entity. Not present on player entities.


class EnderPearlHorse(Horse):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:horse'] = 'minecraft:horse'  # The ID of this entity. Not present on player entities.


class EnderPearlHusk(Zombie):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:husk'] = 'minecraft:husk'  # The ID of this entity. Not present on player entities.


class EnderPearlIllusioner(Spellcaster):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:illusioner'] = 'minecraft:illusioner'  # The ID of this entity. Not present on player entities.


class EnderPearlInteraction(Interaction):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:interaction'] = 'minecraft:interaction'  # The ID of this entity. Not present on player entities.


class EnderPearlIronGolem(IronGolem):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:iron_golem'] = 'minecraft:iron_golem'  # The ID of this entity. Not present on player entities.


class EnderPearlItem(Item):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:item'] = 'minecraft:item'  # The ID of this entity. Not present on player entities.


class EnderPearlItemDisplay(ItemDisplay):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:item_display'] = 'minecraft:item_display'  # The ID of this entity. Not present on player entities.


class EnderPearlItemFrame(ItemFrame):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:item_frame'] = 'minecraft:item_frame'  # The ID of this entity. Not present on player entities.


class EnderPearlJungleBoat(Boat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:jungle_boat'] = 'minecraft:jungle_boat'  # The ID of this entity. Not present on player entities.


class EnderPearlJungleChestBoat(ChestBoat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:jungle_chest_boat'] = 'minecraft:jungle_chest_boat'  # The ID of this entity. Not present on player entities.


class EnderPearlLeashKnot(BlockAttachedEntity):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:leash_knot'] = 'minecraft:leash_knot'  # The ID of this entity. Not present on player entities.


class EnderPearlLingeringPotion(Potion):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:lingering_potion'] = 'minecraft:lingering_potion'  # The ID of this entity. Not present on player entities.


class EnderPearlLlama(Llama):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:llama'] = 'minecraft:llama'  # The ID of this entity. Not present on player entities.


class EnderPearlLlamaSpit(LlamaSpit):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:llama_spit'] = 'minecraft:llama_spit'  # The ID of this entity. Not present on player entities.


class EnderPearlMagmaCube(Slime):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:magma_cube'] = 'minecraft:magma_cube'  # The ID of this entity. Not present on player entities.


class EnderPearlMangroveBoat(Boat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:mangrove_boat'] = 'minecraft:mangrove_boat'  # The ID of this entity. Not present on player entities.


class EnderPearlMangroveChestBoat(ChestBoat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:mangrove_chest_boat'] = 'minecraft:mangrove_chest_boat'  # The ID of this entity. Not present on player entities.


class EnderPearlMannequin(Mannequin):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:mannequin'] = 'minecraft:mannequin'  # The ID of this entity. Not present on player entities.


class EnderPearlMarker(Marker):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:marker'] = 'minecraft:marker'  # The ID of this entity. Not present on player entities.


class EnderPearlMinecart(Minecart):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:minecart'] = 'minecraft:minecart'  # The ID of this entity. Not present on player entities.


class EnderPearlMooshroom(Mooshroom):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:mooshroom'] = 'minecraft:mooshroom'  # The ID of this entity. Not present on player entities.


class EnderPearlMule(ChestedHorse):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:mule'] = 'minecraft:mule'  # The ID of this entity. Not present on player entities.


class EnderPearlNautilus(Tamable):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:nautilus'] = 'minecraft:nautilus'  # The ID of this entity. Not present on player entities.


class EnderPearlOakBoat(Boat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:oak_boat'] = 'minecraft:oak_boat'  # The ID of this entity. Not present on player entities.


class EnderPearlOakChestBoat(ChestBoat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:oak_chest_boat'] = 'minecraft:oak_chest_boat'  # The ID of this entity. Not present on player entities.


class EnderPearlOcelot(Ocelot):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:ocelot'] = 'minecraft:ocelot'  # The ID of this entity. Not present on player entities.


class EnderPearlOminousItemSpawner(OminousItemSpawner):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:ominous_item_spawner'] = 'minecraft:ominous_item_spawner'  # The ID of this entity. Not present on player entities.


class EnderPearlPainting(Painting):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:painting'] = 'minecraft:painting'  # The ID of this entity. Not present on player entities.


class EnderPearlPaleOakBoat(Boat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:pale_oak_boat'] = 'minecraft:pale_oak_boat'  # The ID of this entity. Not present on player entities.


class EnderPearlPaleOakChestBoat(ChestBoat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:pale_oak_chest_boat'] = 'minecraft:pale_oak_chest_boat'  # The ID of this entity. Not present on player entities.


class EnderPearlPanda(Panda):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:panda'] = 'minecraft:panda'  # The ID of this entity. Not present on player entities.


class EnderPearlParched(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:parched'] = 'minecraft:parched'  # The ID of this entity. Not present on player entities.


class EnderPearlParrot(Parrot):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:parrot'] = 'minecraft:parrot'  # The ID of this entity. Not present on player entities.


class EnderPearlPhantom(Phantom):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:phantom'] = 'minecraft:phantom'  # The ID of this entity. Not present on player entities.


class EnderPearlPig(Pig):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:pig'] = 'minecraft:pig'  # The ID of this entity. Not present on player entities.


class EnderPearlPiglin(Piglin):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:piglin'] = 'minecraft:piglin'  # The ID of this entity. Not present on player entities.


class EnderPearlPiglinBrute(PiglinBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:piglin_brute'] = 'minecraft:piglin_brute'  # The ID of this entity. Not present on player entities.


class EnderPearlPillager(Pillager):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:pillager'] = 'minecraft:pillager'  # The ID of this entity. Not present on player entities.


class EnderPearlPlayer(Player):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:player'] = 'minecraft:player'  # The ID of this entity. Not present on player entities.


class EnderPearlPolarBear(PolarBear):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:polar_bear'] = 'minecraft:polar_bear'  # The ID of this entity. Not present on player entities.


class EnderPearlPoplarBoat(Boat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:poplar_boat'] = 'minecraft:poplar_boat'  # The ID of this entity. Not present on player entities.


class EnderPearlPopolarChestBoat(ChestBoat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:popolar_chest_boat'] = 'minecraft:popolar_chest_boat'  # The ID of this entity. Not present on player entities.


class EnderPearlPotion(Potion):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:potion'] = 'minecraft:potion'  # The ID of this entity. Not present on player entities.


class EnderPearlPufferfish(Pufferfish):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:pufferfish'] = 'minecraft:pufferfish'  # The ID of this entity. Not present on player entities.


class EnderPearlRabbit(Rabbit):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:rabbit'] = 'minecraft:rabbit'  # The ID of this entity. Not present on player entities.


class EnderPearlRavager(Ravager):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:ravager'] = 'minecraft:ravager'  # The ID of this entity. Not present on player entities.


class EnderPearlSalmon(Salmon):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:salmon'] = 'minecraft:salmon'  # The ID of this entity. Not present on player entities.


class EnderPearlSheep(Sheep):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:sheep'] = 'minecraft:sheep'  # The ID of this entity. Not present on player entities.


class EnderPearlShulker(Shulker):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:shulker'] = 'minecraft:shulker'  # The ID of this entity. Not present on player entities.


class EnderPearlShulkerBullet(ShulkerBullet):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:shulker_bullet'] = 'minecraft:shulker_bullet'  # The ID of this entity. Not present on player entities.


class EnderPearlSilverfish(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:silverfish'] = 'minecraft:silverfish'  # The ID of this entity. Not present on player entities.


class EnderPearlSkeleton(Skeleton):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:skeleton'] = 'minecraft:skeleton'  # The ID of this entity. Not present on player entities.


class EnderPearlSkeletonHorse(SkeletonHorse):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:skeleton_horse'] = 'minecraft:skeleton_horse'  # The ID of this entity. Not present on player entities.


class EnderPearlSlime(Slime):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:slime'] = 'minecraft:slime'  # The ID of this entity. Not present on player entities.


class EnderPearlSmallFireball(FireballBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:small_fireball'] = 'minecraft:small_fireball'  # The ID of this entity. Not present on player entities.


class EnderPearlSniffer(Breedable):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:sniffer'] = 'minecraft:sniffer'  # The ID of this entity. Not present on player entities.


class EnderPearlSnowGolem(SnowGolem):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:snow_golem'] = 'minecraft:snow_golem'  # The ID of this entity. Not present on player entities.


class EnderPearlSnowball(ThrowableItem):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:snowball'] = 'minecraft:snowball'  # The ID of this entity. Not present on player entities.


class EnderPearlSpawnerMinecart(SpawnerMinecart):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:spawner_minecart'] = 'minecraft:spawner_minecart'  # The ID of this entity. Not present on player entities.


class EnderPearlSpectralArrow(SpectralArrow):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:spectral_arrow'] = 'minecraft:spectral_arrow'  # The ID of this entity. Not present on player entities.


class EnderPearlSpider(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:spider'] = 'minecraft:spider'  # The ID of this entity. Not present on player entities.


class EnderPearlSplashPotion(Potion):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:splash_potion'] = 'minecraft:splash_potion'  # The ID of this entity. Not present on player entities.


class EnderPearlSpruceBoat(Boat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:spruce_boat'] = 'minecraft:spruce_boat'  # The ID of this entity. Not present on player entities.


class EnderPearlSpruceChestBoat(ChestBoat):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:spruce_chest_boat'] = 'minecraft:spruce_chest_boat'  # The ID of this entity. Not present on player entities.


class EnderPearlSquid(Squid):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:squid'] = 'minecraft:squid'  # The ID of this entity. Not present on player entities.


class EnderPearlStray(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:stray'] = 'minecraft:stray'  # The ID of this entity. Not present on player entities.


class EnderPearlStrider(Saddled):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:strider'] = 'minecraft:strider'  # The ID of this entity. Not present on player entities.


class EnderPearlSulfurCube(SulfurCube):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:sulfur_cube'] = 'minecraft:sulfur_cube'  # The ID of this entity. Not present on player entities.


class EnderPearlTadpole(Tadpole):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:tadpole'] = 'minecraft:tadpole'  # The ID of this entity. Not present on player entities.


class EnderPearlTextDisplay(TextDisplay):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:text_display'] = 'minecraft:text_display'  # The ID of this entity. Not present on player entities.


class EnderPearlTnt(Tnt):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:tnt'] = 'minecraft:tnt'  # The ID of this entity. Not present on player entities.


class EnderPearlTntMinecart(TntMinecart):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:tnt_minecart'] = 'minecraft:tnt_minecart'  # The ID of this entity. Not present on player entities.


class EnderPearlTraderLlama(TraderLlama):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:trader_llama'] = 'minecraft:trader_llama'  # The ID of this entity. Not present on player entities.


class EnderPearlTrident(Trident):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:trident'] = 'minecraft:trident'  # The ID of this entity. Not present on player entities.


class EnderPearlTropicalFish(TropicalFish):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:tropical_fish'] = 'minecraft:tropical_fish'  # The ID of this entity. Not present on player entities.


class EnderPearlTurtle(Turtle):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:turtle'] = 'minecraft:turtle'  # The ID of this entity. Not present on player entities.


class EnderPearlVex(Vex):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:vex'] = 'minecraft:vex'  # The ID of this entity. Not present on player entities.


class EnderPearlVillager(Villager):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:villager'] = 'minecraft:villager'  # The ID of this entity. Not present on player entities.


class EnderPearlVindicator(Vindicator):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:vindicator'] = 'minecraft:vindicator'  # The ID of this entity. Not present on player entities.


class EnderPearlWanderingTrader(WanderingTrader):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:wandering_trader'] = 'minecraft:wandering_trader'  # The ID of this entity. Not present on player entities.


class EnderPearlWarden(Warden):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:warden'] = 'minecraft:warden'  # The ID of this entity. Not present on player entities.


class EnderPearlWitch(RaiderBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:witch'] = 'minecraft:witch'  # The ID of this entity. Not present on player entities.


class EnderPearlWither(Wither):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:wither'] = 'minecraft:wither'  # The ID of this entity. Not present on player entities.


class EnderPearlWitherSkeleton(MobBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:wither_skeleton'] = 'minecraft:wither_skeleton'  # The ID of this entity. Not present on player entities.


class EnderPearlWitherSkull(WitherSkull):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:wither_skull'] = 'minecraft:wither_skull'  # The ID of this entity. Not present on player entities.


class EnderPearlWolf(Wolf):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:wolf'] = 'minecraft:wolf'  # The ID of this entity. Not present on player entities.


class EnderPearlZoglin(Zoglin):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:zoglin'] = 'minecraft:zoglin'  # The ID of this entity. Not present on player entities.


class EnderPearlZombie(Zombie):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:zombie'] = 'minecraft:zombie'  # The ID of this entity. Not present on player entities.


class EnderPearlZombieHorse(HorseBase):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:zombie_horse'] = 'minecraft:zombie_horse'  # The ID of this entity. Not present on player entities.


class EnderPearlZombieNautilus(Tamable):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:zombie_nautilus'] = 'minecraft:zombie_nautilus'  # The ID of this entity. Not present on player entities.


class EnderPearlZombieVillager(ZombieVillager):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:zombie_villager'] = 'minecraft:zombie_villager'  # The ID of this entity. Not present on player entities.


class EnderPearlZombifiedPiglin(ZombiePigman):
    ender_pearl_dimension: Annotated[str, IdSpec(registry='dimension')]
    id: Literal['minecraft:zombified_piglin'] = 'minecraft:zombified_piglin'  # The ID of this entity. Not present on player entities.


type EnderPearl = Annotated[
    EnderPearlAcaciaBoat | EnderPearlAcaciaChestBoat | EnderPearlAllay | EnderPearlAreaEffectCloud | EnderPearlArmadillo | EnderPearlArmorStand | EnderPearlArrow | EnderPearlAxolotl | EnderPearlBambooChestRaft | EnderPearlBambooRaft | EnderPearlBat | EnderPearlBee | EnderPearlBirchBoat | EnderPearlBirchChestBoat | EnderPearlBlaze | EnderPearlBlockDisplay | EnderPearlBogged | EnderPearlBreeze | EnderPearlBreezeWindCharge | EnderPearlCamel | EnderPearlCamelHusk | EnderPearlCat | EnderPearlCaveSpider | EnderPearlCherryBoat | EnderPearlCherryChestBoat | EnderPearlChestMinecart | EnderPearlChicken | EnderPearlCod | EnderPearlCommandBlockMinecart | EnderPearlCopperGolem | EnderPearlCow | EnderPearlCreaking | EnderPearlCreeper | EnderPearlCushion | EnderPearlDarkOakBoat | EnderPearlDarkOakChestBoat | EnderPearlDolphin | EnderPearlDonkey | EnderPearlDragonFireball | EnderPearlDrowned | EnderPearlEgg | EnderPearlElderGuardian | EnderPearlEndCrystal | EnderPearlEnderDragon | EnderPearlEnderPearl | EnderPearlEnderman | EnderPearlEndermite | EnderPearlEvoker | EnderPearlEvokerFangs | EnderPearlExperienceBottle | EnderPearlExperienceOrb | EnderPearlEyeOfEnder | EnderPearlFallingBlock | EnderPearlFireball | EnderPearlFireworkRocket | EnderPearlFox | EnderPearlFrog | EnderPearlFurnaceMinecart | EnderPearlGhast | EnderPearlGiant | EnderPearlGlowItemFrame | EnderPearlGlowSquid | EnderPearlGoat | EnderPearlGuardian | EnderPearlHappyGhast | EnderPearlHoglin | EnderPearlHopperMinecart | EnderPearlHorse | EnderPearlHusk | EnderPearlIllusioner | EnderPearlInteraction | EnderPearlIronGolem | EnderPearlItem | EnderPearlItemDisplay | EnderPearlItemFrame | EnderPearlJungleBoat | EnderPearlJungleChestBoat | EnderPearlLeashKnot | EnderPearlLingeringPotion | EnderPearlLlama | EnderPearlLlamaSpit | EnderPearlMagmaCube | EnderPearlMangroveBoat | EnderPearlMangroveChestBoat | EnderPearlMannequin | EnderPearlMarker | EnderPearlMinecart | EnderPearlMooshroom | EnderPearlMule | EnderPearlNautilus | EnderPearlOakBoat | EnderPearlOakChestBoat | EnderPearlOcelot | EnderPearlOminousItemSpawner | EnderPearlPainting | EnderPearlPaleOakBoat | EnderPearlPaleOakChestBoat | EnderPearlPanda | EnderPearlParched | EnderPearlParrot | EnderPearlPhantom | EnderPearlPig | EnderPearlPiglin | EnderPearlPiglinBrute | EnderPearlPillager | EnderPearlPlayer | EnderPearlPolarBear | EnderPearlPoplarBoat | EnderPearlPopolarChestBoat | EnderPearlPotion | EnderPearlPufferfish | EnderPearlRabbit | EnderPearlRavager | EnderPearlSalmon | EnderPearlSheep | EnderPearlShulker | EnderPearlShulkerBullet | EnderPearlSilverfish | EnderPearlSkeleton | EnderPearlSkeletonHorse | EnderPearlSlime | EnderPearlSmallFireball | EnderPearlSniffer | EnderPearlSnowGolem | EnderPearlSnowball | EnderPearlSpawnerMinecart | EnderPearlSpectralArrow | EnderPearlSpider | EnderPearlSplashPotion | EnderPearlSpruceBoat | EnderPearlSpruceChestBoat | EnderPearlSquid | EnderPearlStray | EnderPearlStrider | EnderPearlSulfurCube | EnderPearlTadpole | EnderPearlTextDisplay | EnderPearlTnt | EnderPearlTntMinecart | EnderPearlTraderLlama | EnderPearlTrident | EnderPearlTropicalFish | EnderPearlTurtle | EnderPearlVex | EnderPearlVillager | EnderPearlVindicator | EnderPearlWanderingTrader | EnderPearlWarden | EnderPearlWitch | EnderPearlWither | EnderPearlWitherSkeleton | EnderPearlWitherSkull | EnderPearlWolf | EnderPearlZoglin | EnderPearlZombie | EnderPearlZombieHorse | EnderPearlZombieNautilus | EnderPearlZombieVillager | EnderPearlZombifiedPiglin,
    Field(discriminator='id'),
]


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

