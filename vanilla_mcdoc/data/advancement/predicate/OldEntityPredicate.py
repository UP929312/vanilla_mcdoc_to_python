"""
Generated from symbols.json for ::java::data::advancement::predicate::OldEntityPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/OldEntityPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.advancement.predicate.DistancePredicate import DistancePredicate
    from vanilla_mcdoc.data.advancement.predicate.EntityEffectsPredicate import EntityEffectsPredicate
    from vanilla_mcdoc.data.advancement.predicate.EntityEquipmentPredicate import EntityEquipmentPredicate
    from vanilla_mcdoc.data.advancement.predicate.EntityFlagsPredicate import EntityFlagsPredicate
    from vanilla_mcdoc.data.advancement.predicate.EntityPredicate import EntityPredicate
    from vanilla_mcdoc.data.advancement.predicate.EntitySlotsPredicate import EntitySlotsPredicate
    from vanilla_mcdoc.data.advancement.predicate.EntitySubPredicate import EntitySubPredicate
    from vanilla_mcdoc.data.advancement.predicate.EntityTypePredicate import EntityTypePredicate
    from vanilla_mcdoc.data.advancement.predicate.LocationPredicate import LocationPredicate
    from vanilla_mcdoc.data.advancement.predicate.MovementPredicate import MovementPredicate
    from vanilla_mcdoc.world.component.DataComponentExactPredicate import DataComponentExactPredicate
    from vanilla_mcdoc.world.component.DataComponentPredicate import DataComponentPredicate
    from vanilla_mcdoc.world.entity.BlockAttachedEntity import BlockAttachedEntity
    from vanilla_mcdoc.world.entity.area_effect_cloud.AreaEffectCloud import AreaEffectCloud
    from vanilla_mcdoc.world.entity.boat.Boat import Boat
    from vanilla_mcdoc.world.entity.boat.ChestBoat import ChestBoat
    from vanilla_mcdoc.world.entity.cushion.Cushion import Cushion
    from vanilla_mcdoc.world.entity.display.BlockDisplay import BlockDisplay
    from vanilla_mcdoc.world.entity.display.ItemDisplay import ItemDisplay
    from vanilla_mcdoc.world.entity.display.TextDisplay import TextDisplay
    from vanilla_mcdoc.world.entity.end_crystal.EndCrystal import EndCrystal
    from vanilla_mcdoc.world.entity.evoker_fangs.EvokerFangs import EvokerFangs
    from vanilla_mcdoc.world.entity.experience_orb.ExperienceOrb import ExperienceOrb
    from vanilla_mcdoc.world.entity.eye_of_ender.EyeOfEnder import EyeOfEnder
    from vanilla_mcdoc.world.entity.falling_block.FallingBlock import FallingBlock
    from vanilla_mcdoc.world.entity.interaction.Interaction import Interaction
    from vanilla_mcdoc.world.entity.item.Item import Item
    from vanilla_mcdoc.world.entity.item_frame.ItemFrame import ItemFrame
    from vanilla_mcdoc.world.entity.marker.Marker import Marker
    from vanilla_mcdoc.world.entity.minecart.ChestMinecart import ChestMinecart
    from vanilla_mcdoc.world.entity.minecart.CommandBlockMinecart import CommandBlockMinecart
    from vanilla_mcdoc.world.entity.minecart.FurnaceMinecart import FurnaceMinecart
    from vanilla_mcdoc.world.entity.minecart.HopperMinecart import HopperMinecart
    from vanilla_mcdoc.world.entity.minecart.Minecart import Minecart
    from vanilla_mcdoc.world.entity.minecart.SpawnerMinecart import SpawnerMinecart
    from vanilla_mcdoc.world.entity.minecart.TntMinecart import TntMinecart
    from vanilla_mcdoc.world.entity.mob.MobBase import MobBase
    from vanilla_mcdoc.world.entity.mob.Squid import Squid
    from vanilla_mcdoc.world.entity.mob.allay.Allay import Allay
    from vanilla_mcdoc.world.entity.mob.armor_stand.ArmorStand import ArmorStand
    from vanilla_mcdoc.world.entity.mob.bat.Bat import Bat
    from vanilla_mcdoc.world.entity.mob.bogged.Bogged import Bogged
    from vanilla_mcdoc.world.entity.mob.breedable.Breedable import Breedable
    from vanilla_mcdoc.world.entity.mob.breedable.armadillo.Armadillo import Armadillo
    from vanilla_mcdoc.world.entity.mob.breedable.axolotl.Axolotl import Axolotl
    from vanilla_mcdoc.world.entity.mob.breedable.bee.Bee import Bee
    from vanilla_mcdoc.world.entity.mob.breedable.chicken.Chicken import Chicken
    from vanilla_mcdoc.world.entity.mob.breedable.cow.Cow import Cow
    from vanilla_mcdoc.world.entity.mob.breedable.fox.Fox import Fox
    from vanilla_mcdoc.world.entity.mob.breedable.frog.Frog import Frog
    from vanilla_mcdoc.world.entity.mob.breedable.goat.Goat import Goat
    from vanilla_mcdoc.world.entity.mob.breedable.hoglin.Hoglin import Hoglin
    from vanilla_mcdoc.world.entity.mob.breedable.horse.Camel import Camel
    from vanilla_mcdoc.world.entity.mob.breedable.horse.ChestedHorse import ChestedHorse
    from vanilla_mcdoc.world.entity.mob.breedable.horse.Horse import Horse
    from vanilla_mcdoc.world.entity.mob.breedable.horse.HorseBase import HorseBase
    from vanilla_mcdoc.world.entity.mob.breedable.horse.Llama import Llama
    from vanilla_mcdoc.world.entity.mob.breedable.horse.SkeletonHorse import SkeletonHorse
    from vanilla_mcdoc.world.entity.mob.breedable.horse.TraderLlama import TraderLlama
    from vanilla_mcdoc.world.entity.mob.breedable.mooshroom.Mooshroom import Mooshroom
    from vanilla_mcdoc.world.entity.mob.breedable.ocelot.Ocelot import Ocelot
    from vanilla_mcdoc.world.entity.mob.breedable.panda.Panda import Panda
    from vanilla_mcdoc.world.entity.mob.breedable.polar_bear.PolarBear import PolarBear
    from vanilla_mcdoc.world.entity.mob.breedable.rabbit.Rabbit import Rabbit
    from vanilla_mcdoc.world.entity.mob.breedable.saddled.Pig import Pig
    from vanilla_mcdoc.world.entity.mob.breedable.saddled.Saddled import Saddled
    from vanilla_mcdoc.world.entity.mob.breedable.sheep.Sheep import Sheep
    from vanilla_mcdoc.world.entity.mob.breedable.tamable.Cat import Cat
    from vanilla_mcdoc.world.entity.mob.breedable.tamable.Parrot import Parrot
    from vanilla_mcdoc.world.entity.mob.breedable.tamable.Tamable import Tamable
    from vanilla_mcdoc.world.entity.mob.breedable.tamable.Wolf import Wolf
    from vanilla_mcdoc.world.entity.mob.breedable.turtle.Turtle import Turtle
    from vanilla_mcdoc.world.entity.mob.breedable.villager.Villager import Villager
    from vanilla_mcdoc.world.entity.mob.breedable.villager.WanderingTrader import WanderingTrader
    from vanilla_mcdoc.world.entity.mob.copper_golem.CopperGolem import CopperGolem
    from vanilla_mcdoc.world.entity.mob.creaking.Creaking import Creaking
    from vanilla_mcdoc.world.entity.mob.creeper.Creeper import Creeper
    from vanilla_mcdoc.world.entity.mob.dolphin.Dolphin import Dolphin
    from vanilla_mcdoc.world.entity.mob.ender_dragon.EnderDragon import EnderDragon
    from vanilla_mcdoc.world.entity.mob.enderman.Enderman import Enderman
    from vanilla_mcdoc.world.entity.mob.endermite.Endermite import Endermite
    from vanilla_mcdoc.world.entity.mob.fish.Fish import Fish
    from vanilla_mcdoc.world.entity.mob.fish.Pufferfish import Pufferfish
    from vanilla_mcdoc.world.entity.mob.fish.Salmon import Salmon
    from vanilla_mcdoc.world.entity.mob.fish.TropicalFish import TropicalFish
    from vanilla_mcdoc.world.entity.mob.ghast.Ghast import Ghast
    from vanilla_mcdoc.world.entity.mob.glow_squid.GlowSquid import GlowSquid
    from vanilla_mcdoc.world.entity.mob.happy_ghast.HappyGhast import HappyGhast
    from vanilla_mcdoc.world.entity.mob.iron_golem.IronGolem import IronGolem
    from vanilla_mcdoc.world.entity.mob.mannequin.Mannequin import Mannequin
    from vanilla_mcdoc.world.entity.mob.phantom.Phantom import Phantom
    from vanilla_mcdoc.world.entity.mob.piglin.Piglin import Piglin
    from vanilla_mcdoc.world.entity.mob.piglin.PiglinBase import PiglinBase
    from vanilla_mcdoc.world.entity.mob.player.Player import Player
    from vanilla_mcdoc.world.entity.mob.raider.Pillager import Pillager
    from vanilla_mcdoc.world.entity.mob.raider.RaiderBase import RaiderBase
    from vanilla_mcdoc.world.entity.mob.raider.Ravager import Ravager
    from vanilla_mcdoc.world.entity.mob.raider.Spellcaster import Spellcaster
    from vanilla_mcdoc.world.entity.mob.raider.Vindicator import Vindicator
    from vanilla_mcdoc.world.entity.mob.shulker.Shulker import Shulker
    from vanilla_mcdoc.world.entity.mob.skeleton.Skeleton import Skeleton
    from vanilla_mcdoc.world.entity.mob.slime.Slime import Slime
    from vanilla_mcdoc.world.entity.mob.slime.SulfurCube import SulfurCube
    from vanilla_mcdoc.world.entity.mob.snow_golem.SnowGolem import SnowGolem
    from vanilla_mcdoc.world.entity.mob.tadpole.Tadpole import Tadpole
    from vanilla_mcdoc.world.entity.mob.vex.Vex import Vex
    from vanilla_mcdoc.world.entity.mob.warden.Warden import Warden
    from vanilla_mcdoc.world.entity.mob.wither.Wither import Wither
    from vanilla_mcdoc.world.entity.mob.zoglin.Zoglin import Zoglin
    from vanilla_mcdoc.world.entity.mob.zombie.Zombie import Zombie
    from vanilla_mcdoc.world.entity.mob.zombie.ZombieVillager import ZombieVillager
    from vanilla_mcdoc.world.entity.mob.zombified_piglin.ZombiePigman import ZombiePigman
    from vanilla_mcdoc.world.entity.ominous_item_spawner.OminousItemSpawner import OminousItemSpawner
    from vanilla_mcdoc.world.entity.painting.Painting import Painting
    from vanilla_mcdoc.world.entity.projectile.LlamaSpit import LlamaSpit
    from vanilla_mcdoc.world.entity.projectile.arrow.Arrow import Arrow
    from vanilla_mcdoc.world.entity.projectile.arrow.SpectralArrow import SpectralArrow
    from vanilla_mcdoc.world.entity.projectile.arrow.Trident import Trident
    from vanilla_mcdoc.world.entity.projectile.fireball.AcceleratingProjectileBase import AcceleratingProjectileBase
    from vanilla_mcdoc.world.entity.projectile.fireball.DespawnableProjectileBase import DespawnableProjectileBase
    from vanilla_mcdoc.world.entity.projectile.fireball.FireballBase import FireballBase
    from vanilla_mcdoc.world.entity.projectile.fireball.LargeFireball import LargeFireball
    from vanilla_mcdoc.world.entity.projectile.fireball.WitherSkull import WitherSkull
    from vanilla_mcdoc.world.entity.projectile.firework_rocket.FireWorkRocket import FireWorkRocket
    from vanilla_mcdoc.world.entity.projectile.shulker_bullet.ShulkerBullet import ShulkerBullet
    from vanilla_mcdoc.world.entity.projectile.throwable.Potion import Potion
    from vanilla_mcdoc.world.entity.projectile.throwable.ThrowableItem import ThrowableItem
    from vanilla_mcdoc.world.entity.tnt.Tnt import Tnt


class OldEntityPredicate(GeneratedModel):
    type: EntityTypePredicate | None = None
    type_specific: EntitySubPredicate | None = None
    team: str | None = None
    nbt: str | Boat | ChestBoat | Allay | AreaEffectCloud | Armadillo | ArmorStand | Arrow | Axolotl | Bat | Bee | MobBase | BlockDisplay | Bogged | AcceleratingProjectileBase | Camel | Cat | ChestMinecart | Chicken | Fish | CommandBlockMinecart | CopperGolem | Cow | Creaking | Creeper | Cushion | Dolphin | ChestedHorse | DespawnableProjectileBase | Zombie | ThrowableItem | EndCrystal | EnderDragon | Enderman | Endermite | Spellcaster | EvokerFangs | ExperienceOrb | EyeOfEnder | FallingBlock | LargeFireball | FireWorkRocket | Fox | Frog | FurnaceMinecart | Ghast | ItemFrame | GlowSquid | Goat | HappyGhast | Hoglin | HopperMinecart | Horse | Interaction | IronGolem | Item | ItemDisplay | BlockAttachedEntity | Potion | Llama | LlamaSpit | Slime | Mannequin | Marker | Minecart | Mooshroom | Tamable | Ocelot | OminousItemSpawner | Painting | Panda | Parrot | Phantom | Pig | Piglin | PiglinBase | Pillager | Player | PolarBear | Pufferfish | Rabbit | Ravager | Salmon | Sheep | Shulker | ShulkerBullet | Skeleton | SkeletonHorse | FireballBase | Breedable | SnowGolem | SpawnerMinecart | SpectralArrow | Squid | Saddled | SulfurCube | Tadpole | TextDisplay | Tnt | TntMinecart | TraderLlama | Trident | TropicalFish | Turtle | Vex | Villager | Vindicator | WanderingTrader | Warden | RaiderBase | Wither | WitherSkull | Wolf | Zoglin | HorseBase | ZombieVillager | ZombiePigman | None = None
    location: LocationPredicate | None = None
    distance: DistancePredicate | None = None
    flags: EntityFlagsPredicate | None = None
    equipment: EntityEquipmentPredicate | None = None
    vehicle: EntityPredicate | None = None
    passenger: EntityPredicate | None = None
    stepping_on: LocationPredicate | None = None
    targeted_entity: EntityPredicate | None = None  # Entity that a mob's AI/aggro is targeting.
    effects: EntityEffectsPredicate | None = None
    slots: EntitySlotsPredicate | None = None
    movement: MovementPredicate | None = None
    periodic_tick: Annotated[int, Field(ge=1)] | None = None  # True every `n` ticks of an entity's lifetime.
    movement_affected_by: LocationPredicate | None = None  # Whether the block at most 0.5 blocks below the entity is present which can affect its movement.
    components: DataComponentExactPredicate | None = None  # Match exact data component values on the entity.
    predicates: DataComponentPredicate | None = None  # Test data component values on the entity.
