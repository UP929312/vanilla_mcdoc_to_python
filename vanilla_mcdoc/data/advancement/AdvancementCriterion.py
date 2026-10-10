"""
Generated from symbols.json for ::java::data::advancement::AdvancementCriterion
Local link to file: generated_symbols/data/advancement/AdvancementCriterion.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from generated_symbols.data.advancement.trigger.AnyBlockInteractionTrigger import AnyBlockInteractionTrigger
from generated_symbols.data.advancement.trigger.BeeNestDestroyedTrigger import BeeNestDestroyedTrigger
from generated_symbols.data.advancement.trigger.BredAnimalsTrigger import BredAnimalsTrigger
from generated_symbols.data.advancement.trigger.BrewedPotionTrigger import BrewedPotionTrigger
from generated_symbols.data.advancement.trigger.ChangeDimensionTrigger import ChangeDimensionTrigger
from generated_symbols.data.advancement.trigger.ChanneledLightningTrigger import ChanneledLightningTrigger
from generated_symbols.data.advancement.trigger.ConstructBeaconTrigger import ConstructBeaconTrigger
from generated_symbols.data.advancement.trigger.ConsumeItemTrigger import ConsumeItemTrigger
from generated_symbols.data.advancement.trigger.CuredZombieVillagerTrigger import CuredZombieVillagerTrigger
from generated_symbols.data.advancement.trigger.DefaultBlockInteractionTrigger import DefaultBlockInteractionTrigger
from generated_symbols.data.advancement.trigger.DistanceTrigger import DistanceTrigger
from generated_symbols.data.advancement.trigger.EffectsChangedTrigger import EffectsChangedTrigger
from generated_symbols.data.advancement.trigger.EnchantedItemTrigger import EnchantedItemTrigger
from generated_symbols.data.advancement.trigger.EnterBlockTrigger import EnterBlockTrigger
from generated_symbols.data.advancement.trigger.EntityHurtPlayerTrigger import EntityHurtPlayerTrigger
from generated_symbols.data.advancement.trigger.FallAfterExplosionTrigger import FallAfterExplosionTrigger
from generated_symbols.data.advancement.trigger.FilledBucketTrigger import FilledBucketTrigger
from generated_symbols.data.advancement.trigger.FishingRodHookedTrigger import FishingRodHookedTrigger
from generated_symbols.data.advancement.trigger.ImpossibleTrigger import ImpossibleTrigger
from generated_symbols.data.advancement.trigger.InventoryChangeTrigger import InventoryChangeTrigger
from generated_symbols.data.advancement.trigger.ItemDurabilityTrigger import ItemDurabilityTrigger
from generated_symbols.data.advancement.trigger.ItemUsedOnLocationTrigger import ItemUsedOnLocationTrigger
from generated_symbols.data.advancement.trigger.KilledByArrowTrigger import KilledByArrowTrigger
from generated_symbols.data.advancement.trigger.KilledTrigger import KilledTrigger
from generated_symbols.data.advancement.trigger.LevitationTrigger import LevitationTrigger
from generated_symbols.data.advancement.trigger.LightningStrikeTrigger import LightningStrikeTrigger
from generated_symbols.data.advancement.trigger.LocationTrigger import LocationTrigger
from generated_symbols.data.advancement.trigger.LootTableTrigger import LootTableTrigger
from generated_symbols.data.advancement.trigger.NetherTravelTrigger import NetherTravelTrigger
from generated_symbols.data.advancement.trigger.PickedUpItemTrigger import PickedUpItemTrigger
from generated_symbols.data.advancement.trigger.PlacedBlockTrigger import PlacedBlockTrigger
from generated_symbols.data.advancement.trigger.PlayerHurtEntityTrigger import PlayerHurtEntityTrigger
from generated_symbols.data.advancement.trigger.PlayerInteractTrigger import PlayerInteractTrigger
from generated_symbols.data.advancement.trigger.PlayerTrigger import PlayerTrigger
from generated_symbols.data.advancement.trigger.RecipeCraftedTrigger import RecipeCraftedTrigger
from generated_symbols.data.advancement.trigger.RecipeUnlockedTrigger import RecipeUnlockedTrigger
from generated_symbols.data.advancement.trigger.ShotCrossbowTrigger import ShotCrossbowTrigger
from generated_symbols.data.advancement.trigger.SlideDownBlockTrigger import SlideDownBlockTrigger
from generated_symbols.data.advancement.trigger.SpearMobsTrigger import SpearMobsTrigger
from generated_symbols.data.advancement.trigger.StartRidingTrigger import StartRidingTrigger
from generated_symbols.data.advancement.trigger.SummonedEntityTrigger import SummonedEntityTrigger
from generated_symbols.data.advancement.trigger.TameAnimalTrigger import TameAnimalTrigger
from generated_symbols.data.advancement.trigger.TargetBlockTrigger import TargetBlockTrigger
from generated_symbols.data.advancement.trigger.TradeTrigger import TradeTrigger
from generated_symbols.data.advancement.trigger.UsedEnderEyeTrigger import UsedEnderEyeTrigger
from generated_symbols.data.advancement.trigger.UsedTotemTrigger import UsedTotemTrigger
from generated_symbols.data.advancement.trigger.UsingItemTrigger import UsingItemTrigger


class AdvancementCriterionAllayDropItemOnBlock(ItemUsedOnLocationTrigger):
    trigger: Literal['minecraft:allay_drop_item_on_block', 'allay_drop_item_on_block'] = 'minecraft:allay_drop_item_on_block'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionAnyBlockUse(AnyBlockInteractionTrigger):
    trigger: Literal['minecraft:any_block_use', 'any_block_use'] = 'minecraft:any_block_use'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionAvoidVibration(LocationTrigger):
    trigger: Literal['minecraft:avoid_vibration', 'avoid_vibration'] = 'minecraft:avoid_vibration'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionBeeNestDestroyed(BeeNestDestroyedTrigger):
    trigger: Literal['minecraft:bee_nest_destroyed', 'bee_nest_destroyed'] = 'minecraft:bee_nest_destroyed'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionBredAnimals(BredAnimalsTrigger):
    trigger: Literal['minecraft:bred_animals', 'bred_animals'] = 'minecraft:bred_animals'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionBrewedPotion(BrewedPotionTrigger):
    trigger: Literal['minecraft:brewed_potion', 'brewed_potion'] = 'minecraft:brewed_potion'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionChangedDimension(ChangeDimensionTrigger):
    trigger: Literal['minecraft:changed_dimension', 'changed_dimension'] = 'minecraft:changed_dimension'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionChanneledLightning(ChanneledLightningTrigger):
    trigger: Literal['minecraft:channeled_lightning', 'channeled_lightning'] = 'minecraft:channeled_lightning'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionConstructBeacon(ConstructBeaconTrigger):
    trigger: Literal['minecraft:construct_beacon', 'construct_beacon'] = 'minecraft:construct_beacon'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionConsumeItem(ConsumeItemTrigger):
    trigger: Literal['minecraft:consume_item', 'consume_item'] = 'minecraft:consume_item'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionCrafterRecipeCrafted(RecipeCraftedTrigger):
    trigger: Literal['minecraft:crafter_recipe_crafted', 'crafter_recipe_crafted'] = 'minecraft:crafter_recipe_crafted'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionCuredZombieVillager(CuredZombieVillagerTrigger):
    trigger: Literal['minecraft:cured_zombie_villager', 'cured_zombie_villager'] = 'minecraft:cured_zombie_villager'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionDefaultBlockUse(DefaultBlockInteractionTrigger):
    trigger: Literal['minecraft:default_block_use', 'default_block_use'] = 'minecraft:default_block_use'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionEffectsChanged(EffectsChangedTrigger):
    trigger: Literal['minecraft:effects_changed', 'effects_changed'] = 'minecraft:effects_changed'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionEnchantedItem(EnchantedItemTrigger):
    trigger: Literal['minecraft:enchanted_item', 'enchanted_item'] = 'minecraft:enchanted_item'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionEnterBlock(EnterBlockTrigger):
    trigger: Literal['minecraft:enter_block', 'enter_block'] = 'minecraft:enter_block'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionEntityHurtPlayer(EntityHurtPlayerTrigger):
    trigger: Literal['minecraft:entity_hurt_player', 'entity_hurt_player'] = 'minecraft:entity_hurt_player'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionEntityKilledPlayer(KilledTrigger):
    trigger: Literal['minecraft:entity_killed_player', 'entity_killed_player'] = 'minecraft:entity_killed_player'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionFallAfterExplosion(FallAfterExplosionTrigger):
    trigger: Literal['minecraft:fall_after_explosion', 'fall_after_explosion'] = 'minecraft:fall_after_explosion'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionFallFromHeight(DistanceTrigger):
    trigger: Literal['minecraft:fall_from_height', 'fall_from_height'] = 'minecraft:fall_from_height'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionFilledBucket(FilledBucketTrigger):
    trigger: Literal['minecraft:filled_bucket', 'filled_bucket'] = 'minecraft:filled_bucket'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionFishingRodHooked(FishingRodHookedTrigger):
    trigger: Literal['minecraft:fishing_rod_hooked', 'fishing_rod_hooked'] = 'minecraft:fishing_rod_hooked'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionHeroOfTheVillage(LocationTrigger):
    trigger: Literal['minecraft:hero_of_the_village', 'hero_of_the_village'] = 'minecraft:hero_of_the_village'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionImpossible(ImpossibleTrigger):
    trigger: Literal['minecraft:impossible', 'impossible'] = 'minecraft:impossible'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionInventoryChanged(InventoryChangeTrigger):
    trigger: Literal['minecraft:inventory_changed', 'inventory_changed'] = 'minecraft:inventory_changed'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionItemDurabilityChanged(ItemDurabilityTrigger):
    trigger: Literal['minecraft:item_durability_changed', 'item_durability_changed'] = 'minecraft:item_durability_changed'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionItemUsedOnBlock(ItemUsedOnLocationTrigger):
    trigger: Literal['minecraft:item_used_on_block', 'item_used_on_block'] = 'minecraft:item_used_on_block'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionKillMobNearSculkCatalyst(KilledTrigger):
    trigger: Literal['minecraft:kill_mob_near_sculk_catalyst', 'kill_mob_near_sculk_catalyst'] = 'minecraft:kill_mob_near_sculk_catalyst'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionKilledByArrow(KilledByArrowTrigger):
    trigger: Literal['minecraft:killed_by_arrow', 'killed_by_arrow'] = 'minecraft:killed_by_arrow'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionLevitation(LevitationTrigger):
    trigger: Literal['minecraft:levitation', 'levitation'] = 'minecraft:levitation'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionLightningStrike(LightningStrikeTrigger):
    trigger: Literal['minecraft:lightning_strike', 'lightning_strike'] = 'minecraft:lightning_strike'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionLocation(LocationTrigger):
    trigger: Literal['minecraft:location', 'location'] = 'minecraft:location'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionNetherTravel(NetherTravelTrigger):
    trigger: Literal['minecraft:nether_travel', 'nether_travel'] = 'minecraft:nether_travel'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionPlacedBlock(PlacedBlockTrigger):
    trigger: Literal['minecraft:placed_block', 'placed_block'] = 'minecraft:placed_block'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionPlayerGeneratesContainerLoot(LootTableTrigger):
    trigger: Literal['minecraft:player_generates_container_loot', 'player_generates_container_loot'] = 'minecraft:player_generates_container_loot'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionPlayerHurtEntity(PlayerHurtEntityTrigger):
    trigger: Literal['minecraft:player_hurt_entity', 'player_hurt_entity'] = 'minecraft:player_hurt_entity'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionPlayerInteractedWithEntity(PlayerInteractTrigger):
    trigger: Literal['minecraft:player_interacted_with_entity', 'player_interacted_with_entity'] = 'minecraft:player_interacted_with_entity'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionPlayerKilledEntity(KilledTrigger):
    trigger: Literal['minecraft:player_killed_entity', 'player_killed_entity'] = 'minecraft:player_killed_entity'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionPlayerShearedEquipment(PlayerInteractTrigger):
    trigger: Literal['minecraft:player_sheared_equipment', 'player_sheared_equipment'] = 'minecraft:player_sheared_equipment'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionRecipeCrafted(RecipeCraftedTrigger):
    trigger: Literal['minecraft:recipe_crafted', 'recipe_crafted'] = 'minecraft:recipe_crafted'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionRecipeUnlocked(RecipeUnlockedTrigger):
    trigger: Literal['minecraft:recipe_unlocked', 'recipe_unlocked'] = 'minecraft:recipe_unlocked'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionRideEntityInLava(DistanceTrigger):
    trigger: Literal['minecraft:ride_entity_in_lava', 'ride_entity_in_lava'] = 'minecraft:ride_entity_in_lava'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionShotCrossbow(ShotCrossbowTrigger):
    trigger: Literal['minecraft:shot_crossbow', 'shot_crossbow'] = 'minecraft:shot_crossbow'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionSleptInBed(LocationTrigger):
    trigger: Literal['minecraft:slept_in_bed', 'slept_in_bed'] = 'minecraft:slept_in_bed'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionSlideDownBlock(SlideDownBlockTrigger):
    trigger: Literal['minecraft:slide_down_block', 'slide_down_block'] = 'minecraft:slide_down_block'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionSpearMobs(SpearMobsTrigger):
    trigger: Literal['minecraft:spear_mobs', 'spear_mobs'] = 'minecraft:spear_mobs'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionStartedRiding(StartRidingTrigger):
    trigger: Literal['minecraft:started_riding', 'started_riding'] = 'minecraft:started_riding'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionSummonedEntity(SummonedEntityTrigger):
    trigger: Literal['minecraft:summoned_entity', 'summoned_entity'] = 'minecraft:summoned_entity'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionTameAnimal(TameAnimalTrigger):
    trigger: Literal['minecraft:tame_animal', 'tame_animal'] = 'minecraft:tame_animal'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionTargetHit(TargetBlockTrigger):
    trigger: Literal['minecraft:target_hit', 'target_hit'] = 'minecraft:target_hit'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionThrownItemPickedUpByEntity(PickedUpItemTrigger):
    trigger: Literal['minecraft:thrown_item_picked_up_by_entity', 'thrown_item_picked_up_by_entity'] = 'minecraft:thrown_item_picked_up_by_entity'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionThrownItemPickedUpByPlayer(PickedUpItemTrigger):
    trigger: Literal['minecraft:thrown_item_picked_up_by_player', 'thrown_item_picked_up_by_player'] = 'minecraft:thrown_item_picked_up_by_player'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionTick(PlayerTrigger):
    trigger: Literal['minecraft:tick', 'tick'] = 'minecraft:tick'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionUsedEnderEye(UsedEnderEyeTrigger):
    trigger: Literal['minecraft:used_ender_eye', 'used_ender_eye'] = 'minecraft:used_ender_eye'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionUsedTotem(UsedTotemTrigger):
    trigger: Literal['minecraft:used_totem', 'used_totem'] = 'minecraft:used_totem'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionUsingItem(UsingItemTrigger):
    trigger: Literal['minecraft:using_item', 'using_item'] = 'minecraft:using_item'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionVillagerTrade(TradeTrigger):
    trigger: Literal['minecraft:villager_trade', 'villager_trade'] = 'minecraft:villager_trade'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


class AdvancementCriterionVoluntaryExile(LocationTrigger):
    trigger: Literal['minecraft:voluntary_exile', 'voluntary_exile'] = 'minecraft:voluntary_exile'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


type AdvancementCriterion = Annotated[
    AdvancementCriterionAllayDropItemOnBlock | AdvancementCriterionAnyBlockUse | AdvancementCriterionAvoidVibration | AdvancementCriterionBeeNestDestroyed | AdvancementCriterionBredAnimals | AdvancementCriterionBrewedPotion | AdvancementCriterionChangedDimension | AdvancementCriterionChanneledLightning | AdvancementCriterionConstructBeacon | AdvancementCriterionConsumeItem | AdvancementCriterionCrafterRecipeCrafted | AdvancementCriterionCuredZombieVillager | AdvancementCriterionDefaultBlockUse | AdvancementCriterionEffectsChanged | AdvancementCriterionEnchantedItem | AdvancementCriterionEnterBlock | AdvancementCriterionEntityHurtPlayer | AdvancementCriterionEntityKilledPlayer | AdvancementCriterionFallAfterExplosion | AdvancementCriterionFallFromHeight | AdvancementCriterionFilledBucket | AdvancementCriterionFishingRodHooked | AdvancementCriterionHeroOfTheVillage | AdvancementCriterionImpossible | AdvancementCriterionInventoryChanged | AdvancementCriterionItemDurabilityChanged | AdvancementCriterionItemUsedOnBlock | AdvancementCriterionKillMobNearSculkCatalyst | AdvancementCriterionKilledByArrow | AdvancementCriterionLevitation | AdvancementCriterionLightningStrike | AdvancementCriterionLocation | AdvancementCriterionNetherTravel | AdvancementCriterionPlacedBlock | AdvancementCriterionPlayerGeneratesContainerLoot | AdvancementCriterionPlayerHurtEntity | AdvancementCriterionPlayerInteractedWithEntity | AdvancementCriterionPlayerKilledEntity | AdvancementCriterionPlayerShearedEquipment | AdvancementCriterionRecipeCrafted | AdvancementCriterionRecipeUnlocked | AdvancementCriterionRideEntityInLava | AdvancementCriterionShotCrossbow | AdvancementCriterionSleptInBed | AdvancementCriterionSlideDownBlock | AdvancementCriterionSpearMobs | AdvancementCriterionStartedRiding | AdvancementCriterionSummonedEntity | AdvancementCriterionTameAnimal | AdvancementCriterionTargetHit | AdvancementCriterionThrownItemPickedUpByEntity | AdvancementCriterionThrownItemPickedUpByPlayer | AdvancementCriterionTick | AdvancementCriterionUsedEnderEye | AdvancementCriterionUsedTotem | AdvancementCriterionUsingItem | AdvancementCriterionVillagerTrade | AdvancementCriterionVoluntaryExile,
    Field(discriminator='trigger'),
]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::AdvancementCriterion": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.",
                "key": "trigger",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::data::advancement::Trigger",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.20.3"
                                        }
                                    }
                                },
                                {
                                    "name": "id"
                                }
                            ]
                        },
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.20.3"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "trigger_type"
                                        }
                                    }
                                }
                            ]
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
                                "trigger"
                            ]
                        }
                    ],
                    "registry": "minecraft:trigger"
                }
            }
        ]
    }
}
