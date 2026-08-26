"""
Generated from symbols.json for ::java::data::advancement::AdvancementCriterion
Local link to file: generated_symbols/data/advancement/AdvancementCriterion.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Literal

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


@dataclass(kw_only=True)
class AdvancementCriterionAllayDropItemOnBlock(ItemUsedOnLocationTrigger):
    trigger: Literal['minecraft:allay_drop_item_on_block'] = 'minecraft:allay_drop_item_on_block'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionAnyBlockUse(AnyBlockInteractionTrigger):
    trigger: Literal['minecraft:any_block_use'] = 'minecraft:any_block_use'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionAvoidVibration(LocationTrigger):
    trigger: Literal['minecraft:avoid_vibration'] = 'minecraft:avoid_vibration'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionBeeNestDestroyed(BeeNestDestroyedTrigger):
    trigger: Literal['minecraft:bee_nest_destroyed'] = 'minecraft:bee_nest_destroyed'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionBredAnimals(BredAnimalsTrigger):
    trigger: Literal['minecraft:bred_animals'] = 'minecraft:bred_animals'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionBrewedPotion(BrewedPotionTrigger):
    trigger: Literal['minecraft:brewed_potion'] = 'minecraft:brewed_potion'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionChangedDimension(ChangeDimensionTrigger):
    trigger: Literal['minecraft:changed_dimension'] = 'minecraft:changed_dimension'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionChanneledLightning(ChanneledLightningTrigger):
    trigger: Literal['minecraft:channeled_lightning'] = 'minecraft:channeled_lightning'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionConstructBeacon(ConstructBeaconTrigger):
    trigger: Literal['minecraft:construct_beacon'] = 'minecraft:construct_beacon'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionConsumeItem(ConsumeItemTrigger):
    trigger: Literal['minecraft:consume_item'] = 'minecraft:consume_item'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionCrafterRecipeCrafted(RecipeCraftedTrigger):
    trigger: Literal['minecraft:crafter_recipe_crafted'] = 'minecraft:crafter_recipe_crafted'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionCuredZombieVillager(CuredZombieVillagerTrigger):
    trigger: Literal['minecraft:cured_zombie_villager'] = 'minecraft:cured_zombie_villager'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionDefaultBlockUse(DefaultBlockInteractionTrigger):
    trigger: Literal['minecraft:default_block_use'] = 'minecraft:default_block_use'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionEffectsChanged(EffectsChangedTrigger):
    trigger: Literal['minecraft:effects_changed'] = 'minecraft:effects_changed'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionEnchantedItem(EnchantedItemTrigger):
    trigger: Literal['minecraft:enchanted_item'] = 'minecraft:enchanted_item'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionEnterBlock(EnterBlockTrigger):
    trigger: Literal['minecraft:enter_block'] = 'minecraft:enter_block'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionEntityHurtPlayer(EntityHurtPlayerTrigger):
    trigger: Literal['minecraft:entity_hurt_player'] = 'minecraft:entity_hurt_player'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionEntityKilledPlayer(KilledTrigger):
    trigger: Literal['minecraft:entity_killed_player'] = 'minecraft:entity_killed_player'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionFallAfterExplosion(FallAfterExplosionTrigger):
    trigger: Literal['minecraft:fall_after_explosion'] = 'minecraft:fall_after_explosion'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionFallFromHeight(DistanceTrigger):
    trigger: Literal['minecraft:fall_from_height'] = 'minecraft:fall_from_height'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionFilledBucket(FilledBucketTrigger):
    trigger: Literal['minecraft:filled_bucket'] = 'minecraft:filled_bucket'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionFishingRodHooked(FishingRodHookedTrigger):
    trigger: Literal['minecraft:fishing_rod_hooked'] = 'minecraft:fishing_rod_hooked'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionHeroOfTheVillage(LocationTrigger):
    trigger: Literal['minecraft:hero_of_the_village'] = 'minecraft:hero_of_the_village'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionImpossible(ImpossibleTrigger):
    trigger: Literal['minecraft:impossible'] = 'minecraft:impossible'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionInventoryChanged(InventoryChangeTrigger):
    trigger: Literal['minecraft:inventory_changed'] = 'minecraft:inventory_changed'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionItemDurabilityChanged(ItemDurabilityTrigger):
    trigger: Literal['minecraft:item_durability_changed'] = 'minecraft:item_durability_changed'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionItemUsedOnBlock(ItemUsedOnLocationTrigger):
    trigger: Literal['minecraft:item_used_on_block'] = 'minecraft:item_used_on_block'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionKillMobNearSculkCatalyst(KilledTrigger):
    trigger: Literal['minecraft:kill_mob_near_sculk_catalyst'] = 'minecraft:kill_mob_near_sculk_catalyst'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionKilledByArrow(KilledByArrowTrigger):
    trigger: Literal['minecraft:killed_by_arrow'] = 'minecraft:killed_by_arrow'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionLevitation(LevitationTrigger):
    trigger: Literal['minecraft:levitation'] = 'minecraft:levitation'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionLightningStrike(LightningStrikeTrigger):
    trigger: Literal['minecraft:lightning_strike'] = 'minecraft:lightning_strike'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionLocation(LocationTrigger):
    trigger: Literal['minecraft:location'] = 'minecraft:location'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionNetherTravel(NetherTravelTrigger):
    trigger: Literal['minecraft:nether_travel'] = 'minecraft:nether_travel'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionPlacedBlock(PlacedBlockTrigger):
    trigger: Literal['minecraft:placed_block'] = 'minecraft:placed_block'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionPlayerGeneratesContainerLoot(LootTableTrigger):
    trigger: Literal['minecraft:player_generates_container_loot'] = 'minecraft:player_generates_container_loot'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionPlayerHurtEntity(PlayerHurtEntityTrigger):
    trigger: Literal['minecraft:player_hurt_entity'] = 'minecraft:player_hurt_entity'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionPlayerInteractedWithEntity(PlayerInteractTrigger):
    trigger: Literal['minecraft:player_interacted_with_entity'] = 'minecraft:player_interacted_with_entity'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionPlayerKilledEntity(KilledTrigger):
    trigger: Literal['minecraft:player_killed_entity'] = 'minecraft:player_killed_entity'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionPlayerShearedEquipment(PlayerInteractTrigger):
    trigger: Literal['minecraft:player_sheared_equipment'] = 'minecraft:player_sheared_equipment'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionRecipeCrafted(RecipeCraftedTrigger):
    trigger: Literal['minecraft:recipe_crafted'] = 'minecraft:recipe_crafted'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionRecipeUnlocked(RecipeUnlockedTrigger):
    trigger: Literal['minecraft:recipe_unlocked'] = 'minecraft:recipe_unlocked'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionRideEntityInLava(DistanceTrigger):
    trigger: Literal['minecraft:ride_entity_in_lava'] = 'minecraft:ride_entity_in_lava'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionShotCrossbow(ShotCrossbowTrigger):
    trigger: Literal['minecraft:shot_crossbow'] = 'minecraft:shot_crossbow'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionSleptInBed(LocationTrigger):
    trigger: Literal['minecraft:slept_in_bed'] = 'minecraft:slept_in_bed'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionSlideDownBlock(SlideDownBlockTrigger):
    trigger: Literal['minecraft:slide_down_block'] = 'minecraft:slide_down_block'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionSpearMobs(SpearMobsTrigger):
    trigger: Literal['minecraft:spear_mobs'] = 'minecraft:spear_mobs'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionStartedRiding(StartRidingTrigger):
    trigger: Literal['minecraft:started_riding'] = 'minecraft:started_riding'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionSummonedEntity(SummonedEntityTrigger):
    trigger: Literal['minecraft:summoned_entity'] = 'minecraft:summoned_entity'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionTameAnimal(TameAnimalTrigger):
    trigger: Literal['minecraft:tame_animal'] = 'minecraft:tame_animal'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionTargetHit(TargetBlockTrigger):
    trigger: Literal['minecraft:target_hit'] = 'minecraft:target_hit'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionThrownItemPickedUpByEntity(PickedUpItemTrigger):
    trigger: Literal['minecraft:thrown_item_picked_up_by_entity'] = 'minecraft:thrown_item_picked_up_by_entity'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionThrownItemPickedUpByPlayer(PickedUpItemTrigger):
    trigger: Literal['minecraft:thrown_item_picked_up_by_player'] = 'minecraft:thrown_item_picked_up_by_player'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionTick(PlayerTrigger):
    trigger: Literal['minecraft:tick'] = 'minecraft:tick'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionUsedEnderEye(UsedEnderEyeTrigger):
    trigger: Literal['minecraft:used_ender_eye'] = 'minecraft:used_ender_eye'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionUsedTotem(UsedTotemTrigger):
    trigger: Literal['minecraft:used_totem'] = 'minecraft:used_totem'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionUsingItem(UsingItemTrigger):
    trigger: Literal['minecraft:using_item'] = 'minecraft:using_item'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionVillagerTrade(TradeTrigger):
    trigger: Literal['minecraft:villager_trade'] = 'minecraft:villager_trade'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


@dataclass(kw_only=True)
class AdvancementCriterionVoluntaryExile(LocationTrigger):
    trigger: Literal['minecraft:voluntary_exile'] = 'minecraft:voluntary_exile'  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.


type AdvancementCriterion = AdvancementCriterionAllayDropItemOnBlock | AdvancementCriterionAnyBlockUse | AdvancementCriterionAvoidVibration | AdvancementCriterionBeeNestDestroyed | AdvancementCriterionBredAnimals | AdvancementCriterionBrewedPotion | AdvancementCriterionChangedDimension | AdvancementCriterionChanneledLightning | AdvancementCriterionConstructBeacon | AdvancementCriterionConsumeItem | AdvancementCriterionCrafterRecipeCrafted | AdvancementCriterionCuredZombieVillager | AdvancementCriterionDefaultBlockUse | AdvancementCriterionEffectsChanged | AdvancementCriterionEnchantedItem | AdvancementCriterionEnterBlock | AdvancementCriterionEntityHurtPlayer | AdvancementCriterionEntityKilledPlayer | AdvancementCriterionFallAfterExplosion | AdvancementCriterionFallFromHeight | AdvancementCriterionFilledBucket | AdvancementCriterionFishingRodHooked | AdvancementCriterionHeroOfTheVillage | AdvancementCriterionImpossible | AdvancementCriterionInventoryChanged | AdvancementCriterionItemDurabilityChanged | AdvancementCriterionItemUsedOnBlock | AdvancementCriterionKillMobNearSculkCatalyst | AdvancementCriterionKilledByArrow | AdvancementCriterionLevitation | AdvancementCriterionLightningStrike | AdvancementCriterionLocation | AdvancementCriterionNetherTravel | AdvancementCriterionPlacedBlock | AdvancementCriterionPlayerGeneratesContainerLoot | AdvancementCriterionPlayerHurtEntity | AdvancementCriterionPlayerInteractedWithEntity | AdvancementCriterionPlayerKilledEntity | AdvancementCriterionPlayerShearedEquipment | AdvancementCriterionRecipeCrafted | AdvancementCriterionRecipeUnlocked | AdvancementCriterionRideEntityInLava | AdvancementCriterionShotCrossbow | AdvancementCriterionSleptInBed | AdvancementCriterionSlideDownBlock | AdvancementCriterionSpearMobs | AdvancementCriterionStartedRiding | AdvancementCriterionSummonedEntity | AdvancementCriterionTameAnimal | AdvancementCriterionTargetHit | AdvancementCriterionThrownItemPickedUpByEntity | AdvancementCriterionThrownItemPickedUpByPlayer | AdvancementCriterionTick | AdvancementCriterionUsedEnderEye | AdvancementCriterionUsedTotem | AdvancementCriterionUsingItem | AdvancementCriterionVillagerTrade | AdvancementCriterionVoluntaryExile


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

