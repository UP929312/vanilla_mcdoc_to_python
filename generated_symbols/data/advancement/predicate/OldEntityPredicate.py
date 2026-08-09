# Generated from symbols.json for ::java::data::advancement::predicate::OldEntityPredicate
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.DistancePredicate import DistancePredicate
    from generated_symbols.data.advancement.predicate.EntityEffectsPredicate import EntityEffectsPredicate
    from generated_symbols.data.advancement.predicate.EntityEquipmentPredicate import EntityEquipmentPredicate
    from generated_symbols.data.advancement.predicate.EntityFlagsPredicate import EntityFlagsPredicate
    from generated_symbols.data.advancement.predicate.EntityPredicate import EntityPredicate
    from generated_symbols.data.advancement.predicate.EntitySlotsPredicate import EntitySlotsPredicate
    from generated_symbols.data.advancement.predicate.EntitySubPredicate import EntitySubPredicate
    from generated_symbols.data.advancement.predicate.EntityTypePredicate import EntityTypePredicate
    from generated_symbols.data.advancement.predicate.LocationPredicate import LocationPredicate
    from generated_symbols.data.advancement.predicate.MovementPredicate import MovementPredicate
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


@dataclass(kw_only=True)
class OldEntityPredicate:
    type: EntityTypePredicate | None = None
    type_specific: EntitySubPredicate | None = None
    team: str | None = None
    nbt: str | Boat | ChestBoat | Allay | AreaEffectCloud | Armadillo | ArmorStand | Arrow | Axolotl | Bat | Bee | MobBase | BlockDisplay | Bogged | AcceleratingProjectileBase | Camel | Cat | ChestMinecart | Chicken | Fish | CommandBlockMinecart | CopperGolem | Cow | Creaking | Creeper | Cushion | Dolphin | ChestedHorse | DespawnableProjectileBase | Zombie | ThrowableItem | EndCrystal | EnderDragon | Enderman | Endermite | Spellcaster | EvokerFangs | ExperienceOrb | EyeOfEnder | FallingBlock | LargeFireball | FireWorkRocket | Fox | Frog | FurnaceMinecart | Ghast | ItemFrame | GlowSquid | Goat | HappyGhast | Hoglin | HopperMinecart | Horse | Interaction | IronGolem | Item | ItemDisplay | BlockAttachedEntity | Potion | Llama | LlamaSpit | Slime | Mannequin | Marker | Minecart | Mooshroom | Tamable | Ocelot | OminousItemSpawner | Painting | Panda | Parrot | Phantom | Pig | Piglin | PiglinBase | Pillager | Player | PolarBear | Pufferfish | Rabbit | Ravager | Salmon | Sheep | Shulker | ShulkerBullet | Skeleton | SkeletonHorse | FireballBase | Breedable | SnowGolem | SpawnerMinecart | SpectralArrow | Squid | Saddled | SulfurCube | Tadpole | TextDisplay | Tnt | TntMinecart | TraderLlama | Trident | TropicalFish | Turtle | Vex | Villager | Vindicator | WanderingTrader | Warden | RaiderBase | Wither | WitherSkull | Wolf | Zoglin | HorseBase | ZombiePigman | ZombieVillager | None = None
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
    periodic_tick: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # True every `n` ticks of an entity's lifetime.
    movement_affected_by: LocationPredicate | None = None  # Whether the block at most 0.5 blocks below the entity is present which can affect its movement.
    components: DataComponentExactPredicate | None = None  # Match exact data component values on the entity.
    predicates: DataComponentPredicate | None = None  # Test data component values on the entity.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::OldEntityPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::EntityTypePredicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "key": "type_specific",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::EntitySubPredicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "team",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "team"
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "nbt",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "nbt",
                                    "value": {
                                        "kind": "dispatcher",
                                        "parallelIndices": [
                                            {
                                                "kind": "dynamic",
                                                "accessor": [
                                                    "type"
                                                ]
                                            }
                                        ],
                                        "registry": "minecraft:entity"
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "dispatcher",
                            "parallelIndices": [
                                {
                                    "kind": "dynamic",
                                    "accessor": [
                                        "type"
                                    ]
                                }
                            ],
                            "registry": "minecraft:entity",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.20.5"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "location",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::LocationPredicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "distance",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::DistancePredicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "flags",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::EntityFlagsPredicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "equipment",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::EntityEquipmentPredicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "key": "player",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::PlayerPredicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "key": "vehicle",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::EntityPredicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.17"
                            }
                        }
                    }
                ],
                "key": "passenger",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::EntityPredicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.17"
                            }
                        }
                    }
                ],
                "key": "stepping_on",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::LocationPredicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "desc": "Entity that a mob's AI/aggro is targeting.",
                "key": "targeted_entity",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::EntityPredicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.16"
                            }
                        }
                    },
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "key": "fishing_hook",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::FishingHookPredicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.17"
                            }
                        }
                    },
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "key": "lightning_bolt",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::LightningBoltPredicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "key": "catType",
                "type": {
                    "kind": "string"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "effects",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::EntityEffectsPredicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.20.5"
                            }
                        }
                    }
                ],
                "key": "slots",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::EntitySlotsPredicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21"
                            }
                        }
                    }
                ],
                "key": "movement",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::MovementPredicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21"
                            }
                        }
                    }
                ],
                "desc": "True every `n` ticks of an entity's lifetime.",
                "key": "periodic_tick",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21"
                            }
                        }
                    }
                ],
                "desc": "Whether the block at most 0.5 blocks below the entity is present which can affect its movement.",
                "key": "movement_affected_by",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::LocationPredicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "desc": "Match exact data component values on the entity.",
                "key": "components",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::DataComponentExactPredicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "desc": "Test data component values on the entity.",
                "key": "predicates",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::DataComponentPredicate"
                },
                "optional": True
            }
        ]
    }
}

