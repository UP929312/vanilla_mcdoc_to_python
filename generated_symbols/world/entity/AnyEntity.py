"""
Generated from symbols.json for ::java::world::entity::AnyEntity
Local link to file: generated_symbols/world/entity/AnyEntity.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Literal

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


@dataclass(kw_only=True)
class AnyEntityAcaciaBoat(Boat):
    id: Literal['minecraft:acacia_boat'] = 'minecraft:acacia_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityAcaciaChestBoat(ChestBoat):
    id: Literal['minecraft:acacia_chest_boat'] = 'minecraft:acacia_chest_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityAllay(Allay):
    id: Literal['minecraft:allay'] = 'minecraft:allay'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityAreaEffectCloud(AreaEffectCloud):
    id: Literal['minecraft:area_effect_cloud'] = 'minecraft:area_effect_cloud'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityArmadillo(Armadillo):
    id: Literal['minecraft:armadillo'] = 'minecraft:armadillo'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityArmorStand(ArmorStand):
    id: Literal['minecraft:armor_stand'] = 'minecraft:armor_stand'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityArrow(Arrow):
    id: Literal['minecraft:arrow'] = 'minecraft:arrow'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityAxolotl(Axolotl):
    id: Literal['minecraft:axolotl'] = 'minecraft:axolotl'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityBambooChestRaft(ChestBoat):
    id: Literal['minecraft:bamboo_chest_raft'] = 'minecraft:bamboo_chest_raft'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityBambooRaft(Boat):
    id: Literal['minecraft:bamboo_raft'] = 'minecraft:bamboo_raft'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityBat(Bat):
    id: Literal['minecraft:bat'] = 'minecraft:bat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityBee(Bee):
    id: Literal['minecraft:bee'] = 'minecraft:bee'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityBirchBoat(Boat):
    id: Literal['minecraft:birch_boat'] = 'minecraft:birch_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityBirchChestBoat(ChestBoat):
    id: Literal['minecraft:birch_chest_boat'] = 'minecraft:birch_chest_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityBlaze(MobBase):
    id: Literal['minecraft:blaze'] = 'minecraft:blaze'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityBlockDisplay(BlockDisplay):
    id: Literal['minecraft:block_display'] = 'minecraft:block_display'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityBogged(Bogged):
    id: Literal['minecraft:bogged'] = 'minecraft:bogged'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityBreeze(MobBase):
    id: Literal['minecraft:breeze'] = 'minecraft:breeze'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityBreezeWindCharge(AcceleratingProjectileBase):
    id: Literal['minecraft:breeze_wind_charge'] = 'minecraft:breeze_wind_charge'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityCamel(Camel):
    id: Literal['minecraft:camel'] = 'minecraft:camel'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityCamelHusk(Camel):
    id: Literal['minecraft:camel_husk'] = 'minecraft:camel_husk'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityCat(Cat):
    id: Literal['minecraft:cat'] = 'minecraft:cat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityCaveSpider(MobBase):
    id: Literal['minecraft:cave_spider'] = 'minecraft:cave_spider'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityCherryBoat(Boat):
    id: Literal['minecraft:cherry_boat'] = 'minecraft:cherry_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityCherryChestBoat(ChestBoat):
    id: Literal['minecraft:cherry_chest_boat'] = 'minecraft:cherry_chest_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityChestMinecart(ChestMinecart):
    id: Literal['minecraft:chest_minecart'] = 'minecraft:chest_minecart'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityChicken(Chicken):
    id: Literal['minecraft:chicken'] = 'minecraft:chicken'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityCod(Fish):
    id: Literal['minecraft:cod'] = 'minecraft:cod'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityCommandBlockMinecart(CommandBlockMinecart):
    id: Literal['minecraft:command_block_minecart'] = 'minecraft:command_block_minecart'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityCopperGolem(CopperGolem):
    id: Literal['minecraft:copper_golem'] = 'minecraft:copper_golem'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityCow(Cow):
    id: Literal['minecraft:cow'] = 'minecraft:cow'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityCreaking(Creaking):
    id: Literal['minecraft:creaking'] = 'minecraft:creaking'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityCreeper(Creeper):
    id: Literal['minecraft:creeper'] = 'minecraft:creeper'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityCushion(Cushion):
    id: Literal['minecraft:cushion'] = 'minecraft:cushion'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityDarkOakBoat(Boat):
    id: Literal['minecraft:dark_oak_boat'] = 'minecraft:dark_oak_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityDarkOakChestBoat(ChestBoat):
    id: Literal['minecraft:dark_oak_chest_boat'] = 'minecraft:dark_oak_chest_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityDolphin(Dolphin):
    id: Literal['minecraft:dolphin'] = 'minecraft:dolphin'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityDonkey(ChestedHorse):
    id: Literal['minecraft:donkey'] = 'minecraft:donkey'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityDragonFireball(DespawnableProjectileBase):
    id: Literal['minecraft:dragon_fireball'] = 'minecraft:dragon_fireball'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityDrowned(Zombie):
    id: Literal['minecraft:drowned'] = 'minecraft:drowned'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityEgg(ThrowableItem):
    id: Literal['minecraft:egg'] = 'minecraft:egg'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityElderGuardian(MobBase):
    id: Literal['minecraft:elder_guardian'] = 'minecraft:elder_guardian'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityEndCrystal(EndCrystal):
    id: Literal['minecraft:end_crystal'] = 'minecraft:end_crystal'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityEnderDragon(EnderDragon):
    id: Literal['minecraft:ender_dragon'] = 'minecraft:ender_dragon'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityEnderPearl(ThrowableItem):
    id: Literal['minecraft:ender_pearl'] = 'minecraft:ender_pearl'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityEnderman(Enderman):
    id: Literal['minecraft:enderman'] = 'minecraft:enderman'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityEndermite(Endermite):
    id: Literal['minecraft:endermite'] = 'minecraft:endermite'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityEvoker(Spellcaster):
    id: Literal['minecraft:evoker'] = 'minecraft:evoker'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityEvokerFangs(EvokerFangs):
    id: Literal['minecraft:evoker_fangs'] = 'minecraft:evoker_fangs'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityExperienceBottle(ThrowableItem):
    id: Literal['minecraft:experience_bottle'] = 'minecraft:experience_bottle'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityExperienceOrb(ExperienceOrb):
    id: Literal['minecraft:experience_orb'] = 'minecraft:experience_orb'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityEyeOfEnder(EyeOfEnder):
    id: Literal['minecraft:eye_of_ender'] = 'minecraft:eye_of_ender'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityFallingBlock(FallingBlock):
    id: Literal['minecraft:falling_block'] = 'minecraft:falling_block'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityFireball(LargeFireball):
    id: Literal['minecraft:fireball'] = 'minecraft:fireball'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityFireworkRocket(FireWorkRocket):
    id: Literal['minecraft:firework_rocket'] = 'minecraft:firework_rocket'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityFox(Fox):
    id: Literal['minecraft:fox'] = 'minecraft:fox'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityFrog(Frog):
    id: Literal['minecraft:frog'] = 'minecraft:frog'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityFurnaceMinecart(FurnaceMinecart):
    id: Literal['minecraft:furnace_minecart'] = 'minecraft:furnace_minecart'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityGhast(Ghast):
    id: Literal['minecraft:ghast'] = 'minecraft:ghast'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityGiant(MobBase):
    id: Literal['minecraft:giant'] = 'minecraft:giant'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityGlowItemFrame(ItemFrame):
    id: Literal['minecraft:glow_item_frame'] = 'minecraft:glow_item_frame'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityGlowSquid(GlowSquid):
    id: Literal['minecraft:glow_squid'] = 'minecraft:glow_squid'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityGoat(Goat):
    id: Literal['minecraft:goat'] = 'minecraft:goat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityGuardian(MobBase):
    id: Literal['minecraft:guardian'] = 'minecraft:guardian'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityHappyGhast(HappyGhast):
    id: Literal['minecraft:happy_ghast'] = 'minecraft:happy_ghast'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityHoglin(Hoglin):
    id: Literal['minecraft:hoglin'] = 'minecraft:hoglin'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityHopperMinecart(HopperMinecart):
    id: Literal['minecraft:hopper_minecart'] = 'minecraft:hopper_minecart'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityHorse(Horse):
    id: Literal['minecraft:horse'] = 'minecraft:horse'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityHusk(Zombie):
    id: Literal['minecraft:husk'] = 'minecraft:husk'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityIllusioner(Spellcaster):
    id: Literal['minecraft:illusioner'] = 'minecraft:illusioner'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityInteraction(Interaction):
    id: Literal['minecraft:interaction'] = 'minecraft:interaction'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityIronGolem(IronGolem):
    id: Literal['minecraft:iron_golem'] = 'minecraft:iron_golem'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityItem(Item):
    id: Literal['minecraft:item'] = 'minecraft:item'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityItemDisplay(ItemDisplay):
    id: Literal['minecraft:item_display'] = 'minecraft:item_display'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityItemFrame(ItemFrame):
    id: Literal['minecraft:item_frame'] = 'minecraft:item_frame'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityJungleBoat(Boat):
    id: Literal['minecraft:jungle_boat'] = 'minecraft:jungle_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityJungleChestBoat(ChestBoat):
    id: Literal['minecraft:jungle_chest_boat'] = 'minecraft:jungle_chest_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityLeashKnot(BlockAttachedEntity):
    id: Literal['minecraft:leash_knot'] = 'minecraft:leash_knot'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityLingeringPotion(Potion):
    id: Literal['minecraft:lingering_potion'] = 'minecraft:lingering_potion'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityLlama(Llama):
    id: Literal['minecraft:llama'] = 'minecraft:llama'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityLlamaSpit(LlamaSpit):
    id: Literal['minecraft:llama_spit'] = 'minecraft:llama_spit'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityMagmaCube(Slime):
    id: Literal['minecraft:magma_cube'] = 'minecraft:magma_cube'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityMangroveBoat(Boat):
    id: Literal['minecraft:mangrove_boat'] = 'minecraft:mangrove_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityMangroveChestBoat(ChestBoat):
    id: Literal['minecraft:mangrove_chest_boat'] = 'minecraft:mangrove_chest_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityMannequin(Mannequin):
    id: Literal['minecraft:mannequin'] = 'minecraft:mannequin'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityMarker(Marker):
    id: Literal['minecraft:marker'] = 'minecraft:marker'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityMinecart(Minecart):
    id: Literal['minecraft:minecart'] = 'minecraft:minecart'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityMooshroom(Mooshroom):
    id: Literal['minecraft:mooshroom'] = 'minecraft:mooshroom'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityMule(ChestedHorse):
    id: Literal['minecraft:mule'] = 'minecraft:mule'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityNautilus(Tamable):
    id: Literal['minecraft:nautilus'] = 'minecraft:nautilus'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityOakBoat(Boat):
    id: Literal['minecraft:oak_boat'] = 'minecraft:oak_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityOakChestBoat(ChestBoat):
    id: Literal['minecraft:oak_chest_boat'] = 'minecraft:oak_chest_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityOcelot(Ocelot):
    id: Literal['minecraft:ocelot'] = 'minecraft:ocelot'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityOminousItemSpawner(OminousItemSpawner):
    id: Literal['minecraft:ominous_item_spawner'] = 'minecraft:ominous_item_spawner'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityPainting(Painting):
    id: Literal['minecraft:painting'] = 'minecraft:painting'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityPaleOakBoat(Boat):
    id: Literal['minecraft:pale_oak_boat'] = 'minecraft:pale_oak_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityPaleOakChestBoat(ChestBoat):
    id: Literal['minecraft:pale_oak_chest_boat'] = 'minecraft:pale_oak_chest_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityPanda(Panda):
    id: Literal['minecraft:panda'] = 'minecraft:panda'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityParched(MobBase):
    id: Literal['minecraft:parched'] = 'minecraft:parched'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityParrot(Parrot):
    id: Literal['minecraft:parrot'] = 'minecraft:parrot'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityPhantom(Phantom):
    id: Literal['minecraft:phantom'] = 'minecraft:phantom'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityPig(Pig):
    id: Literal['minecraft:pig'] = 'minecraft:pig'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityPiglin(Piglin):
    id: Literal['minecraft:piglin'] = 'minecraft:piglin'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityPiglinBrute(PiglinBase):
    id: Literal['minecraft:piglin_brute'] = 'minecraft:piglin_brute'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityPillager(Pillager):
    id: Literal['minecraft:pillager'] = 'minecraft:pillager'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityPlayer(Player):
    id: Literal['minecraft:player'] = 'minecraft:player'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityPolarBear(PolarBear):
    id: Literal['minecraft:polar_bear'] = 'minecraft:polar_bear'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityPoplarBoat(Boat):
    id: Literal['minecraft:poplar_boat'] = 'minecraft:poplar_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityPopolarChestBoat(ChestBoat):
    id: Literal['minecraft:popolar_chest_boat'] = 'minecraft:popolar_chest_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityPotion(Potion):
    id: Literal['minecraft:potion'] = 'minecraft:potion'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityPufferfish(Pufferfish):
    id: Literal['minecraft:pufferfish'] = 'minecraft:pufferfish'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityRabbit(Rabbit):
    id: Literal['minecraft:rabbit'] = 'minecraft:rabbit'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityRavager(Ravager):
    id: Literal['minecraft:ravager'] = 'minecraft:ravager'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntitySalmon(Salmon):
    id: Literal['minecraft:salmon'] = 'minecraft:salmon'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntitySheep(Sheep):
    id: Literal['minecraft:sheep'] = 'minecraft:sheep'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityShulker(Shulker):
    id: Literal['minecraft:shulker'] = 'minecraft:shulker'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityShulkerBullet(ShulkerBullet):
    id: Literal['minecraft:shulker_bullet'] = 'minecraft:shulker_bullet'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntitySilverfish(MobBase):
    id: Literal['minecraft:silverfish'] = 'minecraft:silverfish'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntitySkeleton(Skeleton):
    id: Literal['minecraft:skeleton'] = 'minecraft:skeleton'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntitySkeletonHorse(SkeletonHorse):
    id: Literal['minecraft:skeleton_horse'] = 'minecraft:skeleton_horse'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntitySlime(Slime):
    id: Literal['minecraft:slime'] = 'minecraft:slime'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntitySmallFireball(FireballBase):
    id: Literal['minecraft:small_fireball'] = 'minecraft:small_fireball'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntitySniffer(Breedable):
    id: Literal['minecraft:sniffer'] = 'minecraft:sniffer'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntitySnowGolem(SnowGolem):
    id: Literal['minecraft:snow_golem'] = 'minecraft:snow_golem'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntitySnowball(ThrowableItem):
    id: Literal['minecraft:snowball'] = 'minecraft:snowball'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntitySpawnerMinecart(SpawnerMinecart):
    id: Literal['minecraft:spawner_minecart'] = 'minecraft:spawner_minecart'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntitySpectralArrow(SpectralArrow):
    id: Literal['minecraft:spectral_arrow'] = 'minecraft:spectral_arrow'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntitySpider(MobBase):
    id: Literal['minecraft:spider'] = 'minecraft:spider'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntitySplashPotion(Potion):
    id: Literal['minecraft:splash_potion'] = 'minecraft:splash_potion'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntitySpruceBoat(Boat):
    id: Literal['minecraft:spruce_boat'] = 'minecraft:spruce_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntitySpruceChestBoat(ChestBoat):
    id: Literal['minecraft:spruce_chest_boat'] = 'minecraft:spruce_chest_boat'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntitySquid(Squid):
    id: Literal['minecraft:squid'] = 'minecraft:squid'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityStray(MobBase):
    id: Literal['minecraft:stray'] = 'minecraft:stray'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityStrider(Saddled):
    id: Literal['minecraft:strider'] = 'minecraft:strider'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntitySulfurCube(SulfurCube):
    id: Literal['minecraft:sulfur_cube'] = 'minecraft:sulfur_cube'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityTadpole(Tadpole):
    id: Literal['minecraft:tadpole'] = 'minecraft:tadpole'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityTextDisplay(TextDisplay):
    id: Literal['minecraft:text_display'] = 'minecraft:text_display'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityTnt(Tnt):
    id: Literal['minecraft:tnt'] = 'minecraft:tnt'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityTntMinecart(TntMinecart):
    id: Literal['minecraft:tnt_minecart'] = 'minecraft:tnt_minecart'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityTraderLlama(TraderLlama):
    id: Literal['minecraft:trader_llama'] = 'minecraft:trader_llama'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityTrident(Trident):
    id: Literal['minecraft:trident'] = 'minecraft:trident'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityTropicalFish(TropicalFish):
    id: Literal['minecraft:tropical_fish'] = 'minecraft:tropical_fish'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityTurtle(Turtle):
    id: Literal['minecraft:turtle'] = 'minecraft:turtle'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityVex(Vex):
    id: Literal['minecraft:vex'] = 'minecraft:vex'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityVillager(Villager):
    id: Literal['minecraft:villager'] = 'minecraft:villager'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityVindicator(Vindicator):
    id: Literal['minecraft:vindicator'] = 'minecraft:vindicator'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityWanderingTrader(WanderingTrader):
    id: Literal['minecraft:wandering_trader'] = 'minecraft:wandering_trader'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityWarden(Warden):
    id: Literal['minecraft:warden'] = 'minecraft:warden'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityWitch(RaiderBase):
    id: Literal['minecraft:witch'] = 'minecraft:witch'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityWither(Wither):
    id: Literal['minecraft:wither'] = 'minecraft:wither'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityWitherSkeleton(MobBase):
    id: Literal['minecraft:wither_skeleton'] = 'minecraft:wither_skeleton'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityWitherSkull(WitherSkull):
    id: Literal['minecraft:wither_skull'] = 'minecraft:wither_skull'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityWolf(Wolf):
    id: Literal['minecraft:wolf'] = 'minecraft:wolf'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityZoglin(Zoglin):
    id: Literal['minecraft:zoglin'] = 'minecraft:zoglin'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityZombie(Zombie):
    id: Literal['minecraft:zombie'] = 'minecraft:zombie'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityZombieHorse(HorseBase):
    id: Literal['minecraft:zombie_horse'] = 'minecraft:zombie_horse'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityZombieNautilus(Tamable):
    id: Literal['minecraft:zombie_nautilus'] = 'minecraft:zombie_nautilus'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityZombieVillager(ZombieVillager):
    id: Literal['minecraft:zombie_villager'] = 'minecraft:zombie_villager'  # The ID of this entity. Not present on player entities.


@dataclass(kw_only=True)
class AnyEntityZombifiedPiglin(ZombiePigman):
    id: Literal['minecraft:zombified_piglin'] = 'minecraft:zombified_piglin'  # The ID of this entity. Not present on player entities.


type AnyEntity = AnyEntityAcaciaBoat | AnyEntityAcaciaChestBoat | AnyEntityAllay | AnyEntityAreaEffectCloud | AnyEntityArmadillo | AnyEntityArmorStand | AnyEntityArrow | AnyEntityAxolotl | AnyEntityBambooChestRaft | AnyEntityBambooRaft | AnyEntityBat | AnyEntityBee | AnyEntityBirchBoat | AnyEntityBirchChestBoat | AnyEntityBlaze | AnyEntityBlockDisplay | AnyEntityBogged | AnyEntityBreeze | AnyEntityBreezeWindCharge | AnyEntityCamel | AnyEntityCamelHusk | AnyEntityCat | AnyEntityCaveSpider | AnyEntityCherryBoat | AnyEntityCherryChestBoat | AnyEntityChestMinecart | AnyEntityChicken | AnyEntityCod | AnyEntityCommandBlockMinecart | AnyEntityCopperGolem | AnyEntityCow | AnyEntityCreaking | AnyEntityCreeper | AnyEntityCushion | AnyEntityDarkOakBoat | AnyEntityDarkOakChestBoat | AnyEntityDolphin | AnyEntityDonkey | AnyEntityDragonFireball | AnyEntityDrowned | AnyEntityEgg | AnyEntityElderGuardian | AnyEntityEndCrystal | AnyEntityEnderDragon | AnyEntityEnderPearl | AnyEntityEnderman | AnyEntityEndermite | AnyEntityEvoker | AnyEntityEvokerFangs | AnyEntityExperienceBottle | AnyEntityExperienceOrb | AnyEntityEyeOfEnder | AnyEntityFallingBlock | AnyEntityFireball | AnyEntityFireworkRocket | AnyEntityFox | AnyEntityFrog | AnyEntityFurnaceMinecart | AnyEntityGhast | AnyEntityGiant | AnyEntityGlowItemFrame | AnyEntityGlowSquid | AnyEntityGoat | AnyEntityGuardian | AnyEntityHappyGhast | AnyEntityHoglin | AnyEntityHopperMinecart | AnyEntityHorse | AnyEntityHusk | AnyEntityIllusioner | AnyEntityInteraction | AnyEntityIronGolem | AnyEntityItem | AnyEntityItemDisplay | AnyEntityItemFrame | AnyEntityJungleBoat | AnyEntityJungleChestBoat | AnyEntityLeashKnot | AnyEntityLingeringPotion | AnyEntityLlama | AnyEntityLlamaSpit | AnyEntityMagmaCube | AnyEntityMangroveBoat | AnyEntityMangroveChestBoat | AnyEntityMannequin | AnyEntityMarker | AnyEntityMinecart | AnyEntityMooshroom | AnyEntityMule | AnyEntityNautilus | AnyEntityOakBoat | AnyEntityOakChestBoat | AnyEntityOcelot | AnyEntityOminousItemSpawner | AnyEntityPainting | AnyEntityPaleOakBoat | AnyEntityPaleOakChestBoat | AnyEntityPanda | AnyEntityParched | AnyEntityParrot | AnyEntityPhantom | AnyEntityPig | AnyEntityPiglin | AnyEntityPiglinBrute | AnyEntityPillager | AnyEntityPlayer | AnyEntityPolarBear | AnyEntityPoplarBoat | AnyEntityPopolarChestBoat | AnyEntityPotion | AnyEntityPufferfish | AnyEntityRabbit | AnyEntityRavager | AnyEntitySalmon | AnyEntitySheep | AnyEntityShulker | AnyEntityShulkerBullet | AnyEntitySilverfish | AnyEntitySkeleton | AnyEntitySkeletonHorse | AnyEntitySlime | AnyEntitySmallFireball | AnyEntitySniffer | AnyEntitySnowGolem | AnyEntitySnowball | AnyEntitySpawnerMinecart | AnyEntitySpectralArrow | AnyEntitySpider | AnyEntitySplashPotion | AnyEntitySpruceBoat | AnyEntitySpruceChestBoat | AnyEntitySquid | AnyEntityStray | AnyEntityStrider | AnyEntitySulfurCube | AnyEntityTadpole | AnyEntityTextDisplay | AnyEntityTnt | AnyEntityTntMinecart | AnyEntityTraderLlama | AnyEntityTrident | AnyEntityTropicalFish | AnyEntityTurtle | AnyEntityVex | AnyEntityVillager | AnyEntityVindicator | AnyEntityWanderingTrader | AnyEntityWarden | AnyEntityWitch | AnyEntityWither | AnyEntityWitherSkeleton | AnyEntityWitherSkull | AnyEntityWolf | AnyEntityZoglin | AnyEntityZombie | AnyEntityZombieHorse | AnyEntityZombieNautilus | AnyEntityZombieVillager | AnyEntityZombifiedPiglin


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::AnyEntity": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The ID of this entity. Not present on player entities.",
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
                                    "value": "entity_type"
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
                    "registry": "minecraft:entity"
                }
            }
        ]
    }
}

