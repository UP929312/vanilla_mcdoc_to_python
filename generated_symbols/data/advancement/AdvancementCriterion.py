"""
Generated from symbols.json for ::java::data::advancement::AdvancementCriterion
Local link to file: generated_symbols/data/advancement/AdvancementCriterion.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from generated_symbols.data.advancement.trigger.AllayDropItemOnBlock import AllayDropItemOnBlock
    from generated_symbols.data.advancement.trigger.AnyBlockUse import AnyBlockUse
    from generated_symbols.data.advancement.trigger.BeeNestDestroyed import BeeNestDestroyed
    from generated_symbols.data.advancement.trigger.BredAnimals import BredAnimals
    from generated_symbols.data.advancement.trigger.BrewedPotion import BrewedPotion
    from generated_symbols.data.advancement.trigger.ChangedDimension import ChangedDimension
    from generated_symbols.data.advancement.trigger.ChanneledLightning import ChanneledLightning
    from generated_symbols.data.advancement.trigger.ConstructBeacon import ConstructBeacon
    from generated_symbols.data.advancement.trigger.ConsumeItem import ConsumeItem
    from generated_symbols.data.advancement.trigger.CuredZombieVillager import CuredZombieVillager
    from generated_symbols.data.advancement.trigger.DefaultBlockUse import DefaultBlockUse
    from generated_symbols.data.advancement.trigger.EffectsChanged import EffectsChanged
    from generated_symbols.data.advancement.trigger.EnchantedItem import EnchantedItem
    from generated_symbols.data.advancement.trigger.EnterBlock import EnterBlock
    from generated_symbols.data.advancement.trigger.EntityHurtPlayer import EntityHurtPlayer
    from generated_symbols.data.advancement.trigger.EntityKilledPlayer import EntityKilledPlayer
    from generated_symbols.data.advancement.trigger.FallAfterExplosion import FallAfterExplosion
    from generated_symbols.data.advancement.trigger.FallFromHeight import FallFromHeight
    from generated_symbols.data.advancement.trigger.FilledBucket import FilledBucket
    from generated_symbols.data.advancement.trigger.FishingRodHooked import FishingRodHooked
    from generated_symbols.data.advancement.trigger.InventoryChanged import InventoryChanged
    from generated_symbols.data.advancement.trigger.ItemDurabilityChanged import ItemDurabilityChanged
    from generated_symbols.data.advancement.trigger.ItemUsedOnBlock import ItemUsedOnBlock
    from generated_symbols.data.advancement.trigger.KillMobNearSculkCatalyst import KillMobNearSculkCatalyst
    from generated_symbols.data.advancement.trigger.KilledByArrow import KilledByArrow
    from generated_symbols.data.advancement.trigger.KilledByCrossbow import KilledByCrossbow
    from generated_symbols.data.advancement.trigger.Levitation import Levitation
    from generated_symbols.data.advancement.trigger.LightningStrike import LightningStrike
    from generated_symbols.data.advancement.trigger.NetherTravel import NetherTravel
    from generated_symbols.data.advancement.trigger.PlacedBlock import PlacedBlock
    from generated_symbols.data.advancement.trigger.PlayerGeneratesContainerLoot import PlayerGeneratesContainerLoot
    from generated_symbols.data.advancement.trigger.PlayerHurtEntity import PlayerHurtEntity
    from generated_symbols.data.advancement.trigger.PlayerInteract import PlayerInteract
    from generated_symbols.data.advancement.trigger.PlayerKilledEntity import PlayerKilledEntity
    from generated_symbols.data.advancement.trigger.PlayerTrigger import PlayerTrigger
    from generated_symbols.data.advancement.trigger.RecipeCrafted import RecipeCrafted
    from generated_symbols.data.advancement.trigger.RecipeUnlocked import RecipeUnlocked
    from generated_symbols.data.advancement.trigger.RideEntityInLava import RideEntityInLava
    from generated_symbols.data.advancement.trigger.SafelyHarvestHoney import SafelyHarvestHoney
    from generated_symbols.data.advancement.trigger.ShotCrossbow import ShotCrossbow
    from generated_symbols.data.advancement.trigger.SlideDownBlock import SlideDownBlock
    from generated_symbols.data.advancement.trigger.SpearMobs import SpearMobs
    from generated_symbols.data.advancement.trigger.SummonedEntity import SummonedEntity
    from generated_symbols.data.advancement.trigger.TameAnimal import TameAnimal
    from generated_symbols.data.advancement.trigger.TargetHit import TargetHit
    from generated_symbols.data.advancement.trigger.ThrownItemPickedUpByEntity import ThrownItemPickedUpByEntity
    from generated_symbols.data.advancement.trigger.ThrownItemPickedUpByPlayer import ThrownItemPickedUpByPlayer
    from generated_symbols.data.advancement.trigger.TriggerBase import TriggerBase
    from generated_symbols.data.advancement.trigger.UsedEnderEye import UsedEnderEye
    from generated_symbols.data.advancement.trigger.UsedTotem import UsedTotem
    from generated_symbols.data.advancement.trigger.UsingItem import UsingItem
    from generated_symbols.data.advancement.trigger.VillagerTrade import VillagerTrade


@dataclass(kw_only=True)
class AdvancementCriterionAllayDropItemOnBlock:
    trigger: Literal['minecraft:allay_drop_item_on_block']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: AllayDropItemOnBlock | None = None


@dataclass(kw_only=True)
class AdvancementCriterionAnyBlockUse:
    trigger: Literal['minecraft:any_block_use']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: AnyBlockUse | None = None


@dataclass(kw_only=True)
class AdvancementCriterionAvoidVibration:
    trigger: Literal['minecraft:avoid_vibration']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: PlayerTrigger | None = None


@dataclass(kw_only=True)
class AdvancementCriterionBeeNestDestroyed:
    trigger: Literal['minecraft:bee_nest_destroyed']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: BeeNestDestroyed | None = None


@dataclass(kw_only=True)
class AdvancementCriterionBredAnimals:
    trigger: Literal['minecraft:bred_animals']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: BredAnimals | None = None


@dataclass(kw_only=True)
class AdvancementCriterionBrewedPotion:
    trigger: Literal['minecraft:brewed_potion']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: BrewedPotion | None = None


@dataclass(kw_only=True)
class AdvancementCriterionChangedDimension:
    trigger: Literal['minecraft:changed_dimension']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ChangedDimension | None = None


@dataclass(kw_only=True)
class AdvancementCriterionChanneledLightning:
    trigger: Literal['minecraft:channeled_lightning']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ChanneledLightning | None = None


@dataclass(kw_only=True)
class AdvancementCriterionConstructBeacon:
    trigger: Literal['minecraft:construct_beacon']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConstructBeacon | None = None


@dataclass(kw_only=True)
class AdvancementCriterionConsumeItem:
    trigger: Literal['minecraft:consume_item']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ConsumeItem | None = None


@dataclass(kw_only=True)
class AdvancementCriterionCrafterRecipeCrafted:
    trigger: Literal['minecraft:crafter_recipe_crafted']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: RecipeCrafted


@dataclass(kw_only=True)
class AdvancementCriterionCuredZombieVillager:
    trigger: Literal['minecraft:cured_zombie_villager']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: CuredZombieVillager | None = None


@dataclass(kw_only=True)
class AdvancementCriterionDefaultBlockUse:
    trigger: Literal['minecraft:default_block_use']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: DefaultBlockUse | None = None


@dataclass(kw_only=True)
class AdvancementCriterionEffectsChanged:
    trigger: Literal['minecraft:effects_changed']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: EffectsChanged | None = None


@dataclass(kw_only=True)
class AdvancementCriterionEnchantedItem:
    trigger: Literal['minecraft:enchanted_item']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: EnchantedItem | None = None


@dataclass(kw_only=True)
class AdvancementCriterionEnterBlock:
    trigger: Literal['minecraft:enter_block']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: EnterBlock | None = None


@dataclass(kw_only=True)
class AdvancementCriterionEntityHurtPlayer:
    trigger: Literal['minecraft:entity_hurt_player']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: EntityHurtPlayer | None = None


@dataclass(kw_only=True)
class AdvancementCriterionEntityKilledPlayer:
    trigger: Literal['minecraft:entity_killed_player']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: EntityKilledPlayer | None = None


@dataclass(kw_only=True)
class AdvancementCriterionFallAfterExplosion:
    trigger: Literal['minecraft:fall_after_explosion']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: FallAfterExplosion | None = None


@dataclass(kw_only=True)
class AdvancementCriterionFallFromHeight:
    trigger: Literal['minecraft:fall_from_height']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: FallFromHeight | None = None


@dataclass(kw_only=True)
class AdvancementCriterionFilledBucket:
    trigger: Literal['minecraft:filled_bucket']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: FilledBucket | None = None


@dataclass(kw_only=True)
class AdvancementCriterionFishingRodHooked:
    trigger: Literal['minecraft:fishing_rod_hooked']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: FishingRodHooked | None = None


@dataclass(kw_only=True)
class AdvancementCriterionHeroOfTheVillage:
    trigger: Literal['minecraft:hero_of_the_village']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: PlayerTrigger | None = None


@dataclass(kw_only=True)
class AdvancementCriterionImpossible:
    trigger: Literal['minecraft:impossible']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: TriggerBase | None = None


@dataclass(kw_only=True)
class AdvancementCriterionInventoryChanged:
    trigger: Literal['minecraft:inventory_changed']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: InventoryChanged | None = None


@dataclass(kw_only=True)
class AdvancementCriterionItemDurabilityChanged:
    trigger: Literal['minecraft:item_durability_changed']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ItemDurabilityChanged | None = None


@dataclass(kw_only=True)
class AdvancementCriterionItemUsedOnBlock:
    trigger: Literal['minecraft:item_used_on_block']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ItemUsedOnBlock | None = None


@dataclass(kw_only=True)
class AdvancementCriterionKillMobNearSculkCatalyst:
    trigger: Literal['minecraft:kill_mob_near_sculk_catalyst']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: KillMobNearSculkCatalyst | None = None


@dataclass(kw_only=True)
class AdvancementCriterionKilledByArrow:
    trigger: Literal['minecraft:killed_by_arrow']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: KilledByArrow | None = None


@dataclass(kw_only=True)
class AdvancementCriterionKilledByCrossbow:
    trigger: Literal['minecraft:killed_by_crossbow']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: KilledByCrossbow | None = None


@dataclass(kw_only=True)
class AdvancementCriterionLevitation:
    trigger: Literal['minecraft:levitation']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: Levitation | None = None


@dataclass(kw_only=True)
class AdvancementCriterionLightningStrike:
    trigger: Literal['minecraft:lightning_strike']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: LightningStrike | None = None


@dataclass(kw_only=True)
class AdvancementCriterionLocation:
    trigger: Literal['minecraft:location']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: PlayerTrigger | None = None


@dataclass(kw_only=True)
class AdvancementCriterionNetherTravel:
    trigger: Literal['minecraft:nether_travel']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: NetherTravel | None = None


@dataclass(kw_only=True)
class AdvancementCriterionPlacedBlock:
    trigger: Literal['minecraft:placed_block']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: PlacedBlock | None = None


@dataclass(kw_only=True)
class AdvancementCriterionPlayerGeneratesContainerLoot:
    trigger: Literal['minecraft:player_generates_container_loot']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: PlayerGeneratesContainerLoot


@dataclass(kw_only=True)
class AdvancementCriterionPlayerHurtEntity:
    trigger: Literal['minecraft:player_hurt_entity']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: PlayerHurtEntity | None = None


@dataclass(kw_only=True)
class AdvancementCriterionPlayerInteractedWithEntity:
    trigger: Literal['minecraft:player_interacted_with_entity']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: PlayerInteract | None = None


@dataclass(kw_only=True)
class AdvancementCriterionPlayerKilledEntity:
    trigger: Literal['minecraft:player_killed_entity']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: PlayerKilledEntity | None = None


@dataclass(kw_only=True)
class AdvancementCriterionPlayerShearedEquipment:
    trigger: Literal['minecraft:player_sheared_equipment']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: PlayerInteract | None = None


@dataclass(kw_only=True)
class AdvancementCriterionRecipeCrafted:
    trigger: Literal['minecraft:recipe_crafted']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: RecipeCrafted


@dataclass(kw_only=True)
class AdvancementCriterionRecipeUnlocked:
    trigger: Literal['minecraft:recipe_unlocked']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: RecipeUnlocked


@dataclass(kw_only=True)
class AdvancementCriterionRideEntityInLava:
    trigger: Literal['minecraft:ride_entity_in_lava']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: RideEntityInLava | None = None


@dataclass(kw_only=True)
class AdvancementCriterionSafelyHarvestHoney:
    trigger: Literal['minecraft:safely_harvest_honey']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: SafelyHarvestHoney | None = None


@dataclass(kw_only=True)
class AdvancementCriterionShotCrossbow:
    trigger: Literal['minecraft:shot_crossbow']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ShotCrossbow | None = None


@dataclass(kw_only=True)
class AdvancementCriterionSleptInBed:
    trigger: Literal['minecraft:slept_in_bed']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: PlayerTrigger | None = None


@dataclass(kw_only=True)
class AdvancementCriterionSlideDownBlock:
    trigger: Literal['minecraft:slide_down_block']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: SlideDownBlock | None = None


@dataclass(kw_only=True)
class AdvancementCriterionSpearMobs:
    trigger: Literal['minecraft:spear_mobs']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: SpearMobs | None = None


@dataclass(kw_only=True)
class AdvancementCriterionStartedRiding:
    trigger: Literal['minecraft:started_riding']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: TriggerBase | None = None


@dataclass(kw_only=True)
class AdvancementCriterionSummonedEntity:
    trigger: Literal['minecraft:summoned_entity']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: SummonedEntity | None = None


@dataclass(kw_only=True)
class AdvancementCriterionTameAnimal:
    trigger: Literal['minecraft:tame_animal']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: TameAnimal | None = None


@dataclass(kw_only=True)
class AdvancementCriterionTargetHit:
    trigger: Literal['minecraft:target_hit']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: TargetHit | None = None


@dataclass(kw_only=True)
class AdvancementCriterionThrownItemPickedUpByEntity:
    trigger: Literal['minecraft:thrown_item_picked_up_by_entity']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ThrownItemPickedUpByEntity | None = None


@dataclass(kw_only=True)
class AdvancementCriterionThrownItemPickedUpByPlayer:
    trigger: Literal['minecraft:thrown_item_picked_up_by_player']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: ThrownItemPickedUpByPlayer | None = None


@dataclass(kw_only=True)
class AdvancementCriterionTick:
    trigger: Literal['minecraft:tick']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: TriggerBase | None = None


@dataclass(kw_only=True)
class AdvancementCriterionUsedEnderEye:
    trigger: Literal['minecraft:used_ender_eye']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: UsedEnderEye | None = None


@dataclass(kw_only=True)
class AdvancementCriterionUsedTotem:
    trigger: Literal['minecraft:used_totem']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: UsedTotem | None = None


@dataclass(kw_only=True)
class AdvancementCriterionUsingItem:
    trigger: Literal['minecraft:using_item']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: UsingItem | None = None


@dataclass(kw_only=True)
class AdvancementCriterionVillagerTrade:
    trigger: Literal['minecraft:villager_trade']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: VillagerTrade | None = None


@dataclass(kw_only=True)
class AdvancementCriterionVoluntaryExile:
    trigger: Literal['minecraft:voluntary_exile']  # Many triggers can occur multiple times, however, the reward will only be provided multiple times if the advancement is first revoked, which is often done within the function reward.
    conditions: PlayerTrigger | None = None


type AdvancementCriterion = AdvancementCriterionAllayDropItemOnBlock | AdvancementCriterionAnyBlockUse | AdvancementCriterionAvoidVibration | AdvancementCriterionBeeNestDestroyed | AdvancementCriterionBredAnimals | AdvancementCriterionBrewedPotion | AdvancementCriterionChangedDimension | AdvancementCriterionChanneledLightning | AdvancementCriterionConstructBeacon | AdvancementCriterionConsumeItem | AdvancementCriterionCrafterRecipeCrafted | AdvancementCriterionCuredZombieVillager | AdvancementCriterionDefaultBlockUse | AdvancementCriterionEffectsChanged | AdvancementCriterionEnchantedItem | AdvancementCriterionEnterBlock | AdvancementCriterionEntityHurtPlayer | AdvancementCriterionEntityKilledPlayer | AdvancementCriterionFallAfterExplosion | AdvancementCriterionFallFromHeight | AdvancementCriterionFilledBucket | AdvancementCriterionFishingRodHooked | AdvancementCriterionHeroOfTheVillage | AdvancementCriterionImpossible | AdvancementCriterionInventoryChanged | AdvancementCriterionItemDurabilityChanged | AdvancementCriterionItemUsedOnBlock | AdvancementCriterionKillMobNearSculkCatalyst | AdvancementCriterionKilledByArrow | AdvancementCriterionKilledByCrossbow | AdvancementCriterionLevitation | AdvancementCriterionLightningStrike | AdvancementCriterionLocation | AdvancementCriterionNetherTravel | AdvancementCriterionPlacedBlock | AdvancementCriterionPlayerGeneratesContainerLoot | AdvancementCriterionPlayerHurtEntity | AdvancementCriterionPlayerInteractedWithEntity | AdvancementCriterionPlayerKilledEntity | AdvancementCriterionPlayerShearedEquipment | AdvancementCriterionRecipeCrafted | AdvancementCriterionRecipeUnlocked | AdvancementCriterionRideEntityInLava | AdvancementCriterionSafelyHarvestHoney | AdvancementCriterionShotCrossbow | AdvancementCriterionSleptInBed | AdvancementCriterionSlideDownBlock | AdvancementCriterionSpearMobs | AdvancementCriterionStartedRiding | AdvancementCriterionSummonedEntity | AdvancementCriterionTameAnimal | AdvancementCriterionTargetHit | AdvancementCriterionThrownItemPickedUpByEntity | AdvancementCriterionThrownItemPickedUpByPlayer | AdvancementCriterionTick | AdvancementCriterionUsedEnderEye | AdvancementCriterionUsedTotem | AdvancementCriterionUsingItem | AdvancementCriterionVillagerTrade | AdvancementCriterionVoluntaryExile


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

