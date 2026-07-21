# Generated from symbols.json for ::java::data::advancement::Trigger
from enum import Enum


class Trigger(Enum):
    ALLAYDROPITEMONBLOCK = "allay_drop_item_on_block"
    AVOIDVIBRATION = "avoid_vibration"
    BEENESTDESTROYED = "bee_nest_destroyed"
    BREDANIMALS = "bred_animals"
    BREWEDPOTION = "brewed_potion"
    CHANGEDDIMENSION = "changed_dimension"
    CHANNELEDLIGHTNING = "channeled_lightning"
    CONSTRUCTBEACON = "construct_beacon"
    CONSUMEITEM = "consume_item"
    CUREDZOMBIEVILLAGER = "cured_zombie_villager"
    EFFECTSCHANGED = "effects_changed"
    ENCHANTEDITEM = "enchanted_item"
    ENTERBLOCK = "enter_block"
    ENTITYHURTPLAYER = "entity_hurt_player"
    ENTITYKILLEDPLAYER = "entity_killed_player"
    FALLFROMHEIGHT = "fall_from_height"
    FILLEDBUCKET = "filled_bucket"
    FISHINGRODHOOKED = "fishing_rod_hooked"
    HEROOFTHEVILLAGE = "hero_of_the_village"
    IMPOSSIBLE = "impossible"
    INVENTORYCHANGED = "inventory_changed"
    ITEMDURABILITYCHANGED = "item_durability_changed"
    ITEMUSEDONBLOCK = "item_used_on_block"
    KILLMOBNEARSCULKCATALYST = "kill_mob_near_sculk_catalyst"
    KILLEDBYCROSSBOW = "killed_by_crossbow"
    LEVITATION = "levitation"
    LIGHTNINGSTRIKE = "lightning_strike"
    LOCATION = "location"
    NETHERTRAVEL = "nether_travel"
    PLACEDBLOCK = "placed_block"
    PLAYERGENERATESCONTAINERLOOT = "player_generates_container_loot"
    PLAYERHURTENTITY = "player_hurt_entity"
    PLAYERINTERACTEDWITHENTITY = "player_interacted_with_entity"
    PLAYERKILLEDENTITY = "player_killed_entity"
    RECIPECRAFTED = "recipe_crafted"
    RECIPEUNLOCKED = "recipe_unlocked"
    RIDEENTITYINLAVA = "ride_entity_in_lava"
    SHOTCROSSBOW = "shot_crossbow"
    SAFELYHARVESTHONEY = "safely_harvest_honey"
    SLEPTINBED = "slept_in_bed"
    SLIDEDOWNBLOCK = "slide_down_block"
    STARTEDRIDING = "started_riding"
    SUMMONEDENTITY = "summoned_entity"
    TAMEANIMAL = "tame_animal"
    TARGETHIT = "target_hit"
    THROWNITEMPICKEDUPBYENTITY = "thrown_item_picked_up_by_entity"
    THROWNITEMPICKEDUPBYPLAYER = "thrown_item_picked_up_by_player"
    TICK = "tick"
    USEDENDEREYE = "used_ender_eye"
    USEDTOTEM = "used_totem"
    USINGITEM = "using_item"
    VILLAGERTRADE = "villager_trade"
    VOLUNTARYEXILE = "voluntary_exile"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::Trigger": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
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
                "identifier": "AllayDropItemOnBlock",
                "value": "allay_drop_item_on_block"
            },
            {
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
                "identifier": "AvoidVibration",
                "value": "avoid_vibration"
            },
            {
                "identifier": "BeeNestDestroyed",
                "value": "bee_nest_destroyed"
            },
            {
                "identifier": "BredAnimals",
                "value": "bred_animals"
            },
            {
                "identifier": "BrewedPotion",
                "value": "brewed_potion"
            },
            {
                "identifier": "ChangedDimension",
                "value": "changed_dimension"
            },
            {
                "identifier": "ChanneledLightning",
                "value": "channeled_lightning"
            },
            {
                "identifier": "ConstructBeacon",
                "value": "construct_beacon"
            },
            {
                "identifier": "ConsumeItem",
                "value": "consume_item"
            },
            {
                "identifier": "CuredZombieVillager",
                "value": "cured_zombie_villager"
            },
            {
                "identifier": "EffectsChanged",
                "value": "effects_changed"
            },
            {
                "identifier": "EnchantedItem",
                "value": "enchanted_item"
            },
            {
                "identifier": "EnterBlock",
                "value": "enter_block"
            },
            {
                "identifier": "EntityHurtPlayer",
                "value": "entity_hurt_player"
            },
            {
                "identifier": "EntityKilledPlayer",
                "value": "entity_killed_player"
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.18"
                            }
                        }
                    }
                ],
                "identifier": "FallFromHeight",
                "value": "fall_from_height"
            },
            {
                "identifier": "FilledBucket",
                "value": "filled_bucket"
            },
            {
                "identifier": "FishingRodHooked",
                "value": "fishing_rod_hooked"
            },
            {
                "identifier": "HeroOfTheVillage",
                "value": "hero_of_the_village"
            },
            {
                "identifier": "Impossible",
                "value": "impossible"
            },
            {
                "identifier": "InventoryChanged",
                "value": "inventory_changed"
            },
            {
                "identifier": "ItemDurabilityChanged",
                "value": "item_durability_changed"
            },
            {
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
                "identifier": "ItemUsedOnBlock",
                "value": "item_used_on_block"
            },
            {
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
                "identifier": "KillMobNearSculkCatalyst",
                "value": "kill_mob_near_sculk_catalyst"
            },
            {
                "identifier": "KilledByCrossbow",
                "value": "killed_by_crossbow"
            },
            {
                "identifier": "Levitation",
                "value": "levitation"
            },
            {
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
                "identifier": "LightningStrike",
                "value": "lightning_strike"
            },
            {
                "identifier": "Location",
                "value": "location"
            },
            {
                "identifier": "NetherTravel",
                "value": "nether_travel"
            },
            {
                "identifier": "PlacedBlock",
                "value": "placed_block"
            },
            {
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
                "identifier": "PlayerGeneratesContainerLoot",
                "value": "player_generates_container_loot"
            },
            {
                "identifier": "PlayerHurtEntity",
                "value": "player_hurt_entity"
            },
            {
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
                "identifier": "PlayerInteractedWithEntity",
                "value": "player_interacted_with_entity"
            },
            {
                "identifier": "PlayerKilledEntity",
                "value": "player_killed_entity"
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.20"
                            }
                        }
                    }
                ],
                "identifier": "RecipeCrafted",
                "value": "recipe_crafted"
            },
            {
                "identifier": "RecipeUnlocked",
                "value": "recipe_unlocked"
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.18"
                            }
                        }
                    }
                ],
                "identifier": "RideEntityInLava",
                "value": "ride_entity_in_lava"
            },
            {
                "identifier": "ShotCrossbow",
                "value": "shot_crossbow"
            },
            {
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "identifier": "SafelyHarvestHoney",
                "value": "safely_harvest_honey"
            },
            {
                "identifier": "SleptInBed",
                "value": "slept_in_bed"
            },
            {
                "identifier": "SlideDownBlock",
                "value": "slide_down_block"
            },
            {
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
                "identifier": "StartedRiding",
                "value": "started_riding"
            },
            {
                "identifier": "SummonedEntity",
                "value": "summoned_entity"
            },
            {
                "identifier": "TameAnimal",
                "value": "tame_animal"
            },
            {
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
                "identifier": "TargetHit",
                "value": "target_hit"
            },
            {
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
                "identifier": "ThrownItemPickedUpByEntity",
                "value": "thrown_item_picked_up_by_entity"
            },
            {
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
                "identifier": "ThrownItemPickedUpByPlayer",
                "value": "thrown_item_picked_up_by_player"
            },
            {
                "identifier": "Tick",
                "value": "tick"
            },
            {
                "identifier": "UsedEnderEye",
                "value": "used_ender_eye"
            },
            {
                "identifier": "UsedTotem",
                "value": "used_totem"
            },
            {
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
                "identifier": "UsingItem",
                "value": "using_item"
            },
            {
                "identifier": "VillagerTrade",
                "value": "villager_trade"
            },
            {
                "identifier": "VoluntaryExile",
                "value": "voluntary_exile"
            }
        ]
    }
}

