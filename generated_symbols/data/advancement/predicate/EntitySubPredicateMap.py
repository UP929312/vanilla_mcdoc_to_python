"""
Generated from symbols.json for ::java::data::advancement::predicate::EntitySubPredicateMap
Local link to file: generated_symbols/data/advancement/predicate/EntitySubPredicateMap.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.AxolotlPredicate import AxolotlPredicate
    from generated_symbols.data.advancement.predicate.BoatPredicate import BoatPredicate
    from generated_symbols.data.advancement.predicate.CatPredicate import CatPredicate
    from generated_symbols.data.advancement.predicate.DistancePredicate import DistancePredicate
    from generated_symbols.data.advancement.predicate.EntityEffectsPredicate import EntityEffectsPredicate
    from generated_symbols.data.advancement.predicate.EntityEquipmentPredicate import EntityEquipmentPredicate
    from generated_symbols.data.advancement.predicate.EntityFlagsPredicate import EntityFlagsPredicate
    from generated_symbols.data.advancement.predicate.EntityPredicate import EntityPredicate
    from generated_symbols.data.advancement.predicate.EntitySlotsPredicate import EntitySlotsPredicate
    from generated_symbols.data.advancement.predicate.EntityTagPredicate import EntityTagPredicate
    from generated_symbols.data.advancement.predicate.EntityTypePredicate import EntityTypePredicate
    from generated_symbols.data.advancement.predicate.FishingHookPredicate import FishingHookPredicate
    from generated_symbols.data.advancement.predicate.FoxPredicate import FoxPredicate
    from generated_symbols.data.advancement.predicate.FrogPredicate import FrogPredicate
    from generated_symbols.data.advancement.predicate.HorsePredicate import HorsePredicate
    from generated_symbols.data.advancement.predicate.LightningBoltPredicate import LightningBoltPredicate
    from generated_symbols.data.advancement.predicate.LlamaPredicate import LlamaPredicate
    from generated_symbols.data.advancement.predicate.LocationPredicate import LocationPredicate
    from generated_symbols.data.advancement.predicate.MooshroomPredicate import MooshroomPredicate
    from generated_symbols.data.advancement.predicate.MovementPredicate import MovementPredicate
    from generated_symbols.data.advancement.predicate.PaintingPredicate import PaintingPredicate
    from generated_symbols.data.advancement.predicate.ParrotPredicate import ParrotPredicate
    from generated_symbols.data.advancement.predicate.PlayerPredicate import PlayerPredicate
    from generated_symbols.data.advancement.predicate.RabbitPredicate import RabbitPredicate
    from generated_symbols.data.advancement.predicate.RaiderPredicate import RaiderPredicate
    from generated_symbols.data.advancement.predicate.SalmonPredicate import SalmonPredicate
    from generated_symbols.data.advancement.predicate.SheepPredicate import SheepPredicate
    from generated_symbols.data.advancement.predicate.SlimePredicate import SlimePredicate
    from generated_symbols.data.advancement.predicate.TropicalFishPredicate import TropicalFishPredicate
    from generated_symbols.data.advancement.predicate.VillagerPredicate import VillagerPredicate
    from generated_symbols.data.advancement.predicate.WolfPredicate import WolfPredicate
    from generated_symbols.world.component.DataComponentExactPredicate import DataComponentExactPredicate
    from generated_symbols.world.component.DataComponentPredicate import DataComponentPredicate
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


type EntitySubPredicateMap = dict[Annotated[str, IdSpec(registry='entity_sub_predicate_type')], AxolotlPredicate | BoatPredicate | CatPredicate | DataComponentExactPredicate | DistancePredicate | EntityEffectsPredicate | EntityTagPredicate | EntityTypePredicate | EntityEquipmentPredicate | FishingHookPredicate | EntityFlagsPredicate | FoxPredicate | FrogPredicate | HorsePredicate | LightningBoltPredicate | LlamaPredicate | LocationPredicate | MooshroomPredicate | MovementPredicate | str | Boat | ChestBoat | Allay | AreaEffectCloud | Armadillo | ArmorStand | Arrow | Axolotl | Bat | Bee | MobBase | BlockDisplay | Bogged | AcceleratingProjectileBase | Camel | Cat | ChestMinecart | Chicken | Fish | CommandBlockMinecart | CopperGolem | Cow | Creaking | Creeper | Cushion | Dolphin | ChestedHorse | DespawnableProjectileBase | Zombie | ThrowableItem | EndCrystal | EnderDragon | Enderman | Endermite | Spellcaster | EvokerFangs | ExperienceOrb | EyeOfEnder | FallingBlock | LargeFireball | FireWorkRocket | Fox | Frog | FurnaceMinecart | Ghast | ItemFrame | GlowSquid | Goat | HappyGhast | Hoglin | HopperMinecart | Horse | Interaction | IronGolem | Item | ItemDisplay | BlockAttachedEntity | Potion | Llama | LlamaSpit | Slime | Mannequin | Marker | Minecart | Mooshroom | Tamable | Ocelot | OminousItemSpawner | Painting | Panda | Parrot | Phantom | Pig | Piglin | PiglinBase | Pillager | Player | PolarBear | Pufferfish | Rabbit | Ravager | Salmon | Sheep | Shulker | ShulkerBullet | Skeleton | SkeletonHorse | FireballBase | Breedable | SnowGolem | SpawnerMinecart | SpectralArrow | Squid | Saddled | SulfurCube | Tadpole | TextDisplay | Tnt | TntMinecart | TraderLlama | Trident | TropicalFish | Turtle | Vex | Villager | Vindicator | WanderingTrader | Warden | RaiderBase | Wither | WitherSkull | Wolf | Zoglin | HorseBase | ZombiePigman | ZombieVillager | PaintingPredicate | ParrotPredicate | EntityPredicate | Annotated[int, 'Range | `1` and above | inclusive'] | PlayerPredicate | DataComponentPredicate | RabbitPredicate | RaiderPredicate | SalmonPredicate | SheepPredicate | SlimePredicate | EntitySlotsPredicate | str | TropicalFishPredicate | VillagerPredicate | WolfPredicate]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::EntitySubPredicateMap": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "entity_sub_predicate_type"
                                }
                            }
                        }
                    ]
                },
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                {
                                    "keyword": "key"
                                }
                            ]
                        }
                    ],
                    "registry": "minecraft:entity_sub_predicate"
                }
            }
        ]
    }
}

