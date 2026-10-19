"""Vanilla's data/advancement/adventure/ files"""
from vanilla_mcdoc.data.advancement.Advancement import Advancement
from vanilla_mcdoc.data.advancement.AdvancementCriterion import AdvancementCriterionAvoidVibration, AdvancementCriterionChanneledLightning, AdvancementCriterionCrafterRecipeCrafted, AdvancementCriterionEntityKilledPlayer, AdvancementCriterionFallAfterExplosion, AdvancementCriterionFallFromHeight, AdvancementCriterionHeroOfTheVillage, AdvancementCriterionInventoryChanged, AdvancementCriterionItemUsedOnBlock, AdvancementCriterionKillMobNearSculkCatalyst, AdvancementCriterionKilledByArrow, AdvancementCriterionLightningStrike, AdvancementCriterionLocation, AdvancementCriterionPlacedBlock, AdvancementCriterionPlayerGeneratesContainerLoot, AdvancementCriterionPlayerHurtEntity, AdvancementCriterionPlayerInteractedWithEntity, AdvancementCriterionPlayerKilledEntity, AdvancementCriterionRecipeCrafted, AdvancementCriterionShotCrossbow, AdvancementCriterionSleptInBed, AdvancementCriterionSlideDownBlock, AdvancementCriterionSpearMobs, AdvancementCriterionSummonedEntity, AdvancementCriterionTargetHit, AdvancementCriterionUsedTotem, AdvancementCriterionUsingItem, AdvancementCriterionVillagerTrade
from vanilla_mcdoc.data.advancement.AdvancementDisplay import AdvancementDisplay
from vanilla_mcdoc.data.advancement.AdvancementFrame import AdvancementFrame
from vanilla_mcdoc.data.advancement.AdvancementRewards import AdvancementRewards
from vanilla_mcdoc.data.advancement.RootAdvancementDisplay import RootAdvancementDisplay
from vanilla_mcdoc.data.advancement.predicate.BlockPredicate import BlockPredicate
from vanilla_mcdoc.data.advancement.predicate.DamagePredicate import DamagePredicate
from vanilla_mcdoc.data.advancement.predicate.DamageSourcePredicate import DamageSourcePredicate
from vanilla_mcdoc.data.advancement.predicate.DamageTagPredicate import DamageTagPredicate
from vanilla_mcdoc.data.advancement.predicate.DistancePredicate import DistancePredicate
from vanilla_mcdoc.data.advancement.predicate.EntitySubPredicateMap import EntitySubPredicateMap
from vanilla_mcdoc.data.advancement.predicate.EquipmentPredicateSlot import EquipmentPredicateSlot
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.advancement.predicate.LightningBoltPredicate import LightningBoltPredicate
from vanilla_mcdoc.data.advancement.predicate.LocationPredicate import LocationPredicate, PositionStruct
from vanilla_mcdoc.data.advancement.predicate.PlayerPredicate import PlayerPredicate
from vanilla_mcdoc.data.advancement.trigger.ChanneledLightningTrigger import ChanneledLightningTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.DistanceTrigger import DistanceTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.FallAfterExplosionTrigger import FallAfterExplosionTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.InventoryChangeTrigger import InventoryChangeTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.ItemUesdOnLocationConditions import ItemUesdOnLocationConditions
from vanilla_mcdoc.data.advancement.trigger.KilledByArrowTrigger import KilledByArrowTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.KilledTrigger import KilledTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.LightningStrikeTrigger import LightningStrikeTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.LootTableTrigger import LootTableTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions
from vanilla_mcdoc.data.advancement.trigger.PlayerHurtEntityTrigger import PlayerHurtEntityTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.PlayerInteractTrigger import PlayerInteractTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.RecipeCraftedTrigger import RecipeCraftedTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.ShotCrossbowTrigger import ShotCrossbowTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.SlideDownBlockTrigger import SlideDownBlockTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.SpearMobsTrigger import SpearMobsTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.SummonedEntityTrigger import SummonedEntityTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.TargetBlockTrigger import TargetBlockTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.TradeTrigger import TradeTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.UsedTotemTrigger import UsedTotemTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.UsingItemTrigger import UsingItemTriggerTypeArg
from vanilla_mcdoc.data.loot.EntityTarget import EntityTarget
from vanilla_mcdoc.data.loot.condition.LootCondition import LootConditionAllOf, LootConditionAnyOf, LootConditionEntityProperties, LootConditionLocationCheck, LootConditionMatchBlock, LootConditionMatchTool
from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds
from vanilla_mcdoc.util.color.DyeColor import DyeColor
from vanilla_mcdoc.util.text.TextObject import TextObjectStruct2
from vanilla_mcdoc.world.block.banner.BannerPatternLayer import BannerPatternLayer
from vanilla_mcdoc.world.component.DataComponentExactPredicate import DataComponentExactPredicate
from vanilla_mcdoc.world.component.DataComponentPatch import DataComponentPatch
from vanilla_mcdoc.world.component.block.PotDecorations import PotDecorations
from vanilla_mcdoc.world.component.item.Rarity import Rarity
from vanilla_mcdoc.world.component.item.TooltipDisplay import TooltipDisplay
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

ADVENTURING_TIME = Advancement(
    parent='minecraft:adventure/sleep_in_bed',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:diamond_boots'),
        title=TextObjectStruct2(translate='advancements.adventure.adventuring_time.title'),
        description=TextObjectStruct2(translate='advancements.adventure.adventuring_time.description'),
        frame=AdvancementFrame.CHALLENGE,
    ),
    criteria={
        'minecraft:badlands': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:badlands')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:bamboo_jungle': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:bamboo_jungle')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:beach': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:beach')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:birch_forest': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:birch_forest')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:cherry_grove': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:cherry_grove')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:cold_ocean': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:cold_ocean')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:dappled_forest': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:dappled_forest')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:dark_forest': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:dark_forest')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:deep_cold_ocean': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:deep_cold_ocean')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:deep_dark': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:deep_dark')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:deep_frozen_ocean': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:deep_frozen_ocean')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:deep_lukewarm_ocean': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:deep_lukewarm_ocean')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:deep_ocean': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:deep_ocean')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:desert': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:desert')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:dripstone_caves': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:dripstone_caves')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:eroded_badlands': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:eroded_badlands')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:flower_forest': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:flower_forest')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:forest': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:forest')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:frozen_ocean': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:frozen_ocean')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:frozen_peaks': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:frozen_peaks')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:frozen_river': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:frozen_river')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:grove': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:grove')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:ice_caves': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:ice_caves')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:ice_spikes': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:ice_spikes')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:jagged_peaks': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:jagged_peaks')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:jungle': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:jungle')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:lukewarm_ocean': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:lukewarm_ocean')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:lush_caves': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:lush_caves')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:mangrove_swamp': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:mangrove_swamp')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:meadow': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:meadow')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:mushroom_fields': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:mushroom_fields')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:ocean': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:ocean')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:old_growth_birch_forest': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:old_growth_birch_forest')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:old_growth_pine_taiga': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:old_growth_pine_taiga')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:old_growth_spruce_taiga': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:old_growth_spruce_taiga')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:pale_garden': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:pale_garden')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:plains': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:plains')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:river': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:river')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:savanna': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:savanna')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:savanna_plateau': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:savanna_plateau')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:snowy_beach': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:snowy_beach')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:snowy_plains': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:snowy_plains')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:snowy_slopes': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:snowy_slopes')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:snowy_taiga': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:snowy_taiga')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:sparse_jungle': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:sparse_jungle')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:stony_peaks': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:stony_peaks')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:stony_shore': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:stony_shore')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:sulfur_caves': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:sulfur_caves')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:sunflower_plains': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:sunflower_plains')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:swamp': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:swamp')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:taiga': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:taiga')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:warm_ocean': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:warm_ocean')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:windswept_forest': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:windswept_forest')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:windswept_gravelly_hills': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:windswept_gravelly_hills')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:windswept_hills': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:windswept_hills')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:windswept_savanna': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:windswept_savanna')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
        'minecraft:wooded_badlands': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(biomes='minecraft:wooded_badlands')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
    },
    requirements=[
        ['minecraft:mushroom_fields'],
        ['minecraft:deep_frozen_ocean'],
        ['minecraft:frozen_ocean'],
        ['minecraft:deep_cold_ocean'],
        ['minecraft:cold_ocean'],
        ['minecraft:deep_ocean'],
        ['minecraft:ocean'],
        ['minecraft:deep_lukewarm_ocean'],
        ['minecraft:lukewarm_ocean'],
        ['minecraft:warm_ocean'],
        ['minecraft:stony_shore'],
        ['minecraft:swamp'],
        ['minecraft:mangrove_swamp'],
        ['minecraft:snowy_slopes'],
        ['minecraft:snowy_plains'],
        ['minecraft:snowy_beach'],
        ['minecraft:windswept_gravelly_hills'],
        ['minecraft:grove'],
        ['minecraft:windswept_hills'],
        ['minecraft:snowy_taiga'],
        ['minecraft:windswept_forest'],
        ['minecraft:taiga'],
        ['minecraft:plains'],
        ['minecraft:meadow'],
        ['minecraft:beach'],
        ['minecraft:forest'],
        ['minecraft:old_growth_spruce_taiga'],
        ['minecraft:flower_forest'],
        ['minecraft:birch_forest'],
        ['minecraft:dark_forest'],
        ['minecraft:pale_garden'],
        ['minecraft:savanna_plateau'],
        ['minecraft:savanna'],
        ['minecraft:jungle'],
        ['minecraft:badlands'],
        ['minecraft:desert'],
        ['minecraft:wooded_badlands'],
        ['minecraft:jagged_peaks'],
        ['minecraft:stony_peaks'],
        ['minecraft:frozen_river'],
        ['minecraft:river'],
        ['minecraft:ice_spikes'],
        ['minecraft:dappled_forest'],
        ['minecraft:old_growth_pine_taiga'],
        ['minecraft:sunflower_plains'],
        ['minecraft:old_growth_birch_forest'],
        ['minecraft:sparse_jungle'],
        ['minecraft:bamboo_jungle'],
        ['minecraft:eroded_badlands'],
        ['minecraft:windswept_savanna'],
        ['minecraft:cherry_grove'],
        ['minecraft:frozen_peaks'],
        ['minecraft:dripstone_caves'],
        ['minecraft:lush_caves'],
        ['minecraft:sulfur_caves'],
        ['minecraft:deep_dark'],
        ['minecraft:ice_caves'],
    ],
    rewards=AdvancementRewards(experience=500),
    sends_telemetry_event=True,
)

ARBALISTIC = Advancement(
    parent='minecraft:adventure/ol_betsy',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:crossbow'),
        title=TextObjectStruct2(translate='advancements.adventure.arbalistic.title'),
        description=TextObjectStruct2(translate='advancements.adventure.arbalistic.description'),
        frame=AdvancementFrame.CHALLENGE,
        hidden=True,
    ),
    criteria={
        'arbalistic': AdvancementCriterionKilledByArrow(
            conditions=KilledByArrowTriggerTypeArg(
                unique_entity_types=5,
                fired_from_weapon=ItemPredicate(items='minecraft:crossbow'),
            ),
            trigger='minecraft:killed_by_arrow',
        ),
    },
    requirements=[['arbalistic']],
    rewards=AdvancementRewards(experience=85),
    sends_telemetry_event=True,
)

AVOID_VIBRATION = Advancement(
    parent='minecraft:adventure/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:sculk_sensor'),
        title=TextObjectStruct2(translate='advancements.adventure.avoid_vibration.title'),
        description=TextObjectStruct2(translate='advancements.adventure.avoid_vibration.description'),
    ),
    criteria={'avoid_vibration': AdvancementCriterionAvoidVibration(trigger='minecraft:avoid_vibration')},
    requirements=[['avoid_vibration']],
    sends_telemetry_event=True,
)

BLOWBACK = Advancement(
    parent='minecraft:adventure/minecraft_trials_edition',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:wind_charge'),
        title=TextObjectStruct2(translate='advancements.adventure.blowback.title'),
        description=TextObjectStruct2(translate='advancements.adventure.blowback.description'),
        frame=AdvancementFrame.CHALLENGE,
    ),
    criteria={
        'blowback': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:breeze'),
                    type='minecraft:entity_properties',
                ),
                killing_blow=DamageSourcePredicate(
                    tags=[DamageTagPredicate(id='#minecraft:is_projectile', expected=True)],
                    direct_entity=EntitySubPredicateMap(entity_type='minecraft:breeze_wind_charge'),
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
    },
    requirements=[['blowback']],
    rewards=AdvancementRewards(experience=40),
    sends_telemetry_event=True,
)

BRUSH_ARMADILLO = Advancement(
    parent='minecraft:adventure/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:armadillo_scute'),
        title=TextObjectStruct2(translate='advancements.adventure.brush_armadillo.title'),
        description=TextObjectStruct2(translate='advancements.adventure.brush_armadillo.description'),
    ),
    criteria={
        'brush_armadillo': AdvancementCriterionPlayerInteractedWithEntity(
            conditions=PlayerInteractTriggerTypeArg(
                item=ItemPredicate(items='minecraft:brush'),
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:armadillo'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_interacted_with_entity',
        ),
    },
    requirements=[['brush_armadillo']],
    sends_telemetry_event=True,
)

BULLSEYE = Advancement(
    parent='minecraft:adventure/shoot_arrow',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:target'),
        title=TextObjectStruct2(translate='advancements.adventure.bullseye.title'),
        description=TextObjectStruct2(translate='advancements.adventure.bullseye.description'),
        frame=AdvancementFrame.CHALLENGE,
    ),
    criteria={
        'bullseye': AdvancementCriterionTargetHit(
            conditions=TargetBlockTriggerTypeArg(
                projectile=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(distance=DistancePredicate(horizontal=MinMaxBounds(min=30.0))),
                    type='minecraft:entity_properties',
                ),
                signal_strength=15,
            ),
            trigger='minecraft:target_hit',
        ),
    },
    requirements=[['bullseye']],
    rewards=AdvancementRewards(experience=50),
    sends_telemetry_event=True,
)

CRAFTERS_CRAFTING_CRAFTERS = Advancement(
    parent='minecraft:adventure/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:crafter'),
        title=TextObjectStruct2(translate='advancements.adventure.crafters_crafting_crafters.title'),
        description=TextObjectStruct2(translate='advancements.adventure.crafters_crafting_crafters.description'),
    ),
    criteria={
        'crafter_crafted_crafter': AdvancementCriterionCrafterRecipeCrafted(
            conditions=RecipeCraftedTriggerTypeArg(recipes='minecraft:crafter'),
            trigger='minecraft:crafter_recipe_crafted',
        ),
    },
    requirements=[['crafter_crafted_crafter']],
    sends_telemetry_event=True,
)

CRAFT_DECORATED_POT_USING_ONLY_SHERDS = Advancement(
    parent='minecraft:adventure/salvage_sherd',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(
            id='minecraft:decorated_pot',
            components=DataComponentPatch(
                pot_decorations=PotDecorations(
                    left=ItemStackOfComponent(id='minecraft:heart_pottery_sherd'),
                    front=ItemStackOfComponent(id='minecraft:explorer_pottery_sherd'),
                ),
            ),
        ),
        title=TextObjectStruct2(translate='advancements.adventure.craft_decorated_pot_using_only_sherds.title'),
        description=TextObjectStruct2(translate='advancements.adventure.craft_decorated_pot_using_only_sherds.description'),
    ),
    criteria={
        'pot_crafted_using_only_sherds': AdvancementCriterionRecipeCrafted(
            conditions=RecipeCraftedTriggerTypeArg(
                recipes='minecraft:decorated_pot',
                ingredients=[
                    ItemPredicate(items='#minecraft:decorated_pot_sherds'),
                    ItemPredicate(items='#minecraft:decorated_pot_sherds'),
                    ItemPredicate(items='#minecraft:decorated_pot_sherds'),
                    ItemPredicate(items='#minecraft:decorated_pot_sherds'),
                ],
            ),
            trigger='minecraft:recipe_crafted',
        ),
    },
    requirements=[['pot_crafted_using_only_sherds']],
    sends_telemetry_event=True,
)

FALL_FROM_WORLD_HEIGHT = Advancement(
    parent='minecraft:adventure/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:water_bucket'),
        title=TextObjectStruct2(translate='advancements.adventure.fall_from_world_height.title'),
        description=TextObjectStruct2(translate='advancements.adventure.fall_from_world_height.description'),
    ),
    criteria={
        'fall_from_world_height': AdvancementCriterionFallFromHeight(
            conditions=DistanceTriggerTypeArg(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(
                        location=LocationPredicate(position=PositionStruct(y=MinMaxBounds(max=-59.0))),
                    ),
                    type='minecraft:entity_properties',
                ),
                start_position=LocationPredicate(position=PositionStruct(y=MinMaxBounds(min=319.0))),
                distance=DistancePredicate(y=MinMaxBounds(min=379.0)),
            ),
            trigger='minecraft:fall_from_height',
        ),
    },
    requirements=[['fall_from_world_height']],
    sends_telemetry_event=True,
)

HEART_TRANSPLANTER = Advancement(
    parent='minecraft:adventure/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:creaking_heart'),
        title=TextObjectStruct2(translate='advancements.adventure.heart_transplanter.title'),
        description=TextObjectStruct2(translate='advancements.adventure.heart_transplanter.description'),
    ),
    criteria={
        'place_creaking_heart_awake': AdvancementCriterionPlacedBlock(
            conditions=ItemUesdOnLocationConditions(
                location=LootConditionMatchBlock(
                    blocks='minecraft:creaking_heart',
                    state={'creaking_heart_state': 'awake'},
                    type='minecraft:match_block',
                ),
            ),
            trigger='minecraft:placed_block',
        ),
        'place_creaking_heart_dormant': AdvancementCriterionPlacedBlock(
            conditions=ItemUesdOnLocationConditions(
                location=LootConditionMatchBlock(
                    blocks='minecraft:creaking_heart',
                    state={'creaking_heart_state': 'dormant'},
                    type='minecraft:match_block',
                ),
            ),
            trigger='minecraft:placed_block',
        ),
        'place_pale_oak_log': AdvancementCriterionPlacedBlock(
            conditions=ItemUesdOnLocationConditions(
                location=LootConditionAnyOf(
                    terms=[
                        LootConditionAllOf(
                            terms=[
                                LootConditionLocationCheck(
                                    predicate=LocationPredicate(
                                        block=BlockPredicate(blocks='#minecraft:pale_oak_logs', state={'axis': 'y'}),
                                    ),
                                    type='minecraft:location_check',
                                ),
                                LootConditionLocationCheck(
                                    offsetY=-1,
                                    predicate=LocationPredicate(
                                        block=BlockPredicate(blocks='minecraft:creaking_heart', state={'axis': 'y'}),
                                    ),
                                    type='minecraft:location_check',
                                ),
                                LootConditionLocationCheck(
                                    offsetY=-2,
                                    predicate=LocationPredicate(
                                        block=BlockPredicate(blocks='#minecraft:pale_oak_logs', state={'axis': 'y'}),
                                    ),
                                    type='minecraft:location_check',
                                ),
                            ],
                            type='minecraft:all_of',
                        ),
                        LootConditionAllOf(
                            terms=[
                                LootConditionLocationCheck(
                                    predicate=LocationPredicate(
                                        block=BlockPredicate(blocks='#minecraft:pale_oak_logs', state={'axis': 'y'}),
                                    ),
                                    type='minecraft:location_check',
                                ),
                                LootConditionLocationCheck(
                                    offsetY=1,
                                    predicate=LocationPredicate(
                                        block=BlockPredicate(blocks='minecraft:creaking_heart', state={'axis': 'y'}),
                                    ),
                                    type='minecraft:location_check',
                                ),
                                LootConditionLocationCheck(
                                    offsetY=2,
                                    predicate=LocationPredicate(
                                        block=BlockPredicate(blocks='#minecraft:pale_oak_logs', state={'axis': 'y'}),
                                    ),
                                    type='minecraft:location_check',
                                ),
                            ],
                            type='minecraft:all_of',
                        ),
                        LootConditionAllOf(
                            terms=[
                                LootConditionLocationCheck(
                                    predicate=LocationPredicate(
                                        block=BlockPredicate(blocks='#minecraft:pale_oak_logs', state={'axis': 'z'}),
                                    ),
                                    type='minecraft:location_check',
                                ),
                                LootConditionLocationCheck(
                                    offsetZ=-1,
                                    predicate=LocationPredicate(
                                        block=BlockPredicate(blocks='minecraft:creaking_heart', state={'axis': 'z'}),
                                    ),
                                    type='minecraft:location_check',
                                ),
                                LootConditionLocationCheck(
                                    offsetZ=-2,
                                    predicate=LocationPredicate(
                                        block=BlockPredicate(blocks='#minecraft:pale_oak_logs', state={'axis': 'z'}),
                                    ),
                                    type='minecraft:location_check',
                                ),
                            ],
                            type='minecraft:all_of',
                        ),
                        LootConditionAllOf(
                            terms=[
                                LootConditionLocationCheck(
                                    predicate=LocationPredicate(
                                        block=BlockPredicate(blocks='#minecraft:pale_oak_logs', state={'axis': 'z'}),
                                    ),
                                    type='minecraft:location_check',
                                ),
                                LootConditionLocationCheck(
                                    offsetZ=1,
                                    predicate=LocationPredicate(
                                        block=BlockPredicate(blocks='minecraft:creaking_heart', state={'axis': 'z'}),
                                    ),
                                    type='minecraft:location_check',
                                ),
                                LootConditionLocationCheck(
                                    offsetZ=2,
                                    predicate=LocationPredicate(
                                        block=BlockPredicate(blocks='#minecraft:pale_oak_logs', state={'axis': 'z'}),
                                    ),
                                    type='minecraft:location_check',
                                ),
                            ],
                            type='minecraft:all_of',
                        ),
                        LootConditionAllOf(
                            terms=[
                                LootConditionLocationCheck(
                                    predicate=LocationPredicate(
                                        block=BlockPredicate(blocks='#minecraft:pale_oak_logs', state={'axis': 'x'}),
                                    ),
                                    type='minecraft:location_check',
                                ),
                                LootConditionLocationCheck(
                                    offsetX=-1,
                                    predicate=LocationPredicate(
                                        block=BlockPredicate(blocks='minecraft:creaking_heart', state={'axis': 'x'}),
                                    ),
                                    type='minecraft:location_check',
                                ),
                                LootConditionLocationCheck(
                                    offsetX=-2,
                                    predicate=LocationPredicate(
                                        block=BlockPredicate(blocks='#minecraft:pale_oak_logs', state={'axis': 'x'}),
                                    ),
                                    type='minecraft:location_check',
                                ),
                            ],
                            type='minecraft:all_of',
                        ),
                        LootConditionAllOf(
                            terms=[
                                LootConditionLocationCheck(
                                    predicate=LocationPredicate(
                                        block=BlockPredicate(blocks='#minecraft:pale_oak_logs', state={'axis': 'x'}),
                                    ),
                                    type='minecraft:location_check',
                                ),
                                LootConditionLocationCheck(
                                    offsetX=1,
                                    predicate=LocationPredicate(
                                        block=BlockPredicate(blocks='minecraft:creaking_heart', state={'axis': 'x'}),
                                    ),
                                    type='minecraft:location_check',
                                ),
                                LootConditionLocationCheck(
                                    offsetX=2,
                                    predicate=LocationPredicate(
                                        block=BlockPredicate(blocks='#minecraft:pale_oak_logs', state={'axis': 'x'}),
                                    ),
                                    type='minecraft:location_check',
                                ),
                            ],
                            type='minecraft:all_of',
                        ),
                    ],
                    type='minecraft:any_of',
                ),
            ),
            trigger='minecraft:placed_block',
        ),
    },
    requirements=[['place_creaking_heart_dormant', 'place_creaking_heart_awake', 'place_pale_oak_log']],
    sends_telemetry_event=True,
)

HERO_OF_THE_VILLAGE = Advancement(
    parent='minecraft:adventure/voluntary_exile',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(
            id='minecraft:white_banner',
            components=DataComponentPatch(
                banner_patterns=[
                    BannerPatternLayer(color=DyeColor.CYAN, pattern='minecraft:rhombus'),
                    BannerPatternLayer(color=DyeColor.LIGHTGRAY, pattern='minecraft:stripe_bottom'),
                    BannerPatternLayer(color=DyeColor.GRAY, pattern='minecraft:stripe_center'),
                    BannerPatternLayer(color=DyeColor.LIGHTGRAY, pattern='minecraft:border'),
                    BannerPatternLayer(color=DyeColor.BLACK, pattern='minecraft:stripe_middle'),
                    BannerPatternLayer(color=DyeColor.LIGHTGRAY, pattern='minecraft:half_horizontal'),
                    BannerPatternLayer(color=DyeColor.LIGHTGRAY, pattern='minecraft:circle'),
                    BannerPatternLayer(color=DyeColor.BLACK, pattern='minecraft:border'),
                ],
                item_name=TextObjectStruct2(translate='block.minecraft.ominous_banner'),
                rarity=Rarity.UNCOMMON,
                tooltip_display=TooltipDisplay(hidden_components=['minecraft:banner_patterns']),
            ),
        ),
        title=TextObjectStruct2(translate='advancements.adventure.hero_of_the_village.title'),
        description=TextObjectStruct2(translate='advancements.adventure.hero_of_the_village.description'),
        frame=AdvancementFrame.CHALLENGE,
        hidden=True,
    ),
    criteria={'hero_of_the_village': AdvancementCriterionHeroOfTheVillage(trigger='minecraft:hero_of_the_village')},
    requirements=[['hero_of_the_village']],
    rewards=AdvancementRewards(experience=100),
    sends_telemetry_event=True,
)

HONEY_BLOCK_SLIDE = Advancement(
    parent='minecraft:adventure/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:honey_block'),
        title=TextObjectStruct2(translate='advancements.adventure.honey_block_slide.title'),
        description=TextObjectStruct2(translate='advancements.adventure.honey_block_slide.description'),
    ),
    criteria={
        'honey_block_slide': AdvancementCriterionSlideDownBlock(
            conditions=SlideDownBlockTriggerTypeArg(blocks='minecraft:honey_block'),
            trigger='minecraft:slide_down_block',
        ),
    },
    requirements=[['honey_block_slide']],
    sends_telemetry_event=True,
)

KILL_ALL_MOBS = Advancement(
    parent='minecraft:adventure/kill_a_mob',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:diamond_sword'),
        title=TextObjectStruct2(translate='advancements.adventure.kill_all_mobs.title'),
        description=TextObjectStruct2(translate='advancements.adventure.kill_all_mobs.description'),
        frame=AdvancementFrame.CHALLENGE,
    ),
    criteria={
        'minecraft:blaze': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:blaze'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:bogged': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:bogged'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:breeze': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:breeze'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:camel_husk': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:camel_husk'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:cave_spider': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:cave_spider'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:creaking': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:creaking'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:creeper': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:creeper'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:drowned': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:drowned'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:elder_guardian': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:elder_guardian'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:ender_dragon': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:ender_dragon'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:enderman': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:enderman'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:endermite': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:endermite'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:evoker': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:evoker'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:frostbite': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:frostbite'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:ghast': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:ghast'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:guardian': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:guardian'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:hoglin': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:hoglin'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:husk': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:husk'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:magma_cube': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:magma_cube'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:parched': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:parched'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:phantom': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:phantom'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:piglin': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:piglin'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:piglin_brute': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:piglin_brute'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:pillager': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:pillager'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:ravager': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:ravager'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:shulker': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:shulker'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:silverfish': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:silverfish'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:skeleton': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:skeleton'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:slime': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:slime'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:spider': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:spider'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:stray': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:stray'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:vex': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:vex'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:vindicator': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:vindicator'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:witch': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:witch'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:wither': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:wither'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:wither_skeleton': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:wither_skeleton'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:zoglin': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:zoglin'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:zombie': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:zombie'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:zombie_horse': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:zombie_horse'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:zombie_nautilus': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:zombie_nautilus'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:zombie_villager': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:zombie_villager'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:zombified_piglin': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:zombified_piglin'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
    },
    requirements=[
        ['minecraft:blaze'],
        ['minecraft:bogged'],
        ['minecraft:breeze'],
        ['minecraft:camel_husk'],
        ['minecraft:cave_spider'],
        ['minecraft:creaking'],
        ['minecraft:creeper'],
        ['minecraft:drowned'],
        ['minecraft:elder_guardian'],
        ['minecraft:ender_dragon'],
        ['minecraft:enderman'],
        ['minecraft:endermite'],
        ['minecraft:evoker'],
        ['minecraft:frostbite'],
        ['minecraft:ghast'],
        ['minecraft:guardian'],
        ['minecraft:hoglin'],
        ['minecraft:husk'],
        ['minecraft:magma_cube'],
        ['minecraft:parched'],
        ['minecraft:phantom'],
        ['minecraft:piglin'],
        ['minecraft:piglin_brute'],
        ['minecraft:pillager'],
        ['minecraft:ravager'],
        ['minecraft:shulker'],
        ['minecraft:silverfish'],
        ['minecraft:skeleton'],
        ['minecraft:slime'],
        ['minecraft:spider'],
        ['minecraft:stray'],
        ['minecraft:vex'],
        ['minecraft:vindicator'],
        ['minecraft:witch'],
        ['minecraft:wither_skeleton'],
        ['minecraft:wither'],
        ['minecraft:zoglin'],
        ['minecraft:zombie_villager'],
        ['minecraft:zombie'],
        ['minecraft:zombie_horse'],
        ['minecraft:zombified_piglin'],
        ['minecraft:zombie_nautilus'],
    ],
    rewards=AdvancementRewards(experience=100),
    sends_telemetry_event=True,
)

KILL_A_MOB = Advancement(
    parent='minecraft:adventure/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:iron_sword'),
        title=TextObjectStruct2(translate='advancements.adventure.kill_a_mob.title'),
        description=TextObjectStruct2(translate='advancements.adventure.kill_a_mob.description'),
    ),
    criteria={
        'minecraft:blaze': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:blaze'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:bogged': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:bogged'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:breeze': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:breeze'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:camel_husk': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:camel_husk'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:cave_spider': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:cave_spider'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:creaking': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:creaking'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:creeper': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:creeper'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:drowned': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:drowned'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:elder_guardian': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:elder_guardian'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:ender_dragon': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:ender_dragon'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:enderman': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:enderman'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:endermite': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:endermite'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:evoker': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:evoker'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:frostbite': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:frostbite'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:ghast': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:ghast'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:guardian': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:guardian'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:hoglin': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:hoglin'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:husk': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:husk'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:magma_cube': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:magma_cube'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:parched': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:parched'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:phantom': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:phantom'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:piglin': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:piglin'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:piglin_brute': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:piglin_brute'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:pillager': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:pillager'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:ravager': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:ravager'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:shulker': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:shulker'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:silverfish': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:silverfish'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:skeleton': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:skeleton'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:slime': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:slime'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:spider': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:spider'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:stray': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:stray'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:vex': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:vex'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:vindicator': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:vindicator'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:witch': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:witch'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:wither': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:wither'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:wither_skeleton': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:wither_skeleton'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:zoglin': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:zoglin'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:zombie': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:zombie'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:zombie_horse': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:zombie_horse'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:zombie_nautilus': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:zombie_nautilus'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:zombie_villager': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:zombie_villager'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
        'minecraft:zombified_piglin': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:zombified_piglin'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
    },
    requirements=[
        [
            'minecraft:blaze',
            'minecraft:bogged',
            'minecraft:breeze',
            'minecraft:camel_husk',
            'minecraft:cave_spider',
            'minecraft:creaking',
            'minecraft:creeper',
            'minecraft:drowned',
            'minecraft:elder_guardian',
            'minecraft:ender_dragon',
            'minecraft:enderman',
            'minecraft:endermite',
            'minecraft:evoker',
            'minecraft:frostbite',
            'minecraft:ghast',
            'minecraft:guardian',
            'minecraft:hoglin',
            'minecraft:husk',
            'minecraft:magma_cube',
            'minecraft:parched',
            'minecraft:phantom',
            'minecraft:piglin',
            'minecraft:piglin_brute',
            'minecraft:pillager',
            'minecraft:ravager',
            'minecraft:shulker',
            'minecraft:silverfish',
            'minecraft:skeleton',
            'minecraft:slime',
            'minecraft:spider',
            'minecraft:stray',
            'minecraft:vex',
            'minecraft:vindicator',
            'minecraft:witch',
            'minecraft:wither_skeleton',
            'minecraft:wither',
            'minecraft:zoglin',
            'minecraft:zombie_villager',
            'minecraft:zombie',
            'minecraft:zombie_horse',
            'minecraft:zombified_piglin',
            'minecraft:zombie_nautilus',
        ],
    ],
    sends_telemetry_event=True,
)

KILL_MOB_NEAR_SCULK_CATALYST = Advancement(
    parent='minecraft:adventure/kill_a_mob',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:sculk_catalyst'),
        title=TextObjectStruct2(translate='advancements.adventure.kill_mob_near_sculk_catalyst.title'),
        description=TextObjectStruct2(translate='advancements.adventure.kill_mob_near_sculk_catalyst.description'),
        frame=AdvancementFrame.CHALLENGE,
    ),
    criteria={
        'kill_mob_near_sculk_catalyst': AdvancementCriterionKillMobNearSculkCatalyst(trigger='minecraft:kill_mob_near_sculk_catalyst'),
    },
    requirements=[['kill_mob_near_sculk_catalyst']],
    sends_telemetry_event=True,
)

LIGHTEN_UP = Advancement(
    parent='minecraft:adventure/minecraft_trials_edition',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:copper_bulb'),
        title=TextObjectStruct2(translate='advancements.adventure.lighten_up.title'),
        description=TextObjectStruct2(translate='advancements.adventure.lighten_up.description'),
    ),
    criteria={
        'lighten_up': AdvancementCriterionItemUsedOnBlock(
            conditions=ItemUesdOnLocationConditions(
                location=LootConditionAllOf(
                    terms=[
                        LootConditionLocationCheck(
                            predicate=LocationPredicate(
                                block=BlockPredicate(
                                    blocks=[
                                        'minecraft:exposed_copper_bulb',
                                        'minecraft:weathered_copper_bulb',
                                        'minecraft:oxidized_copper_bulb',
                                        'minecraft:waxed_exposed_copper_bulb',
                                        'minecraft:waxed_weathered_copper_bulb',
                                        'minecraft:waxed_oxidized_copper_bulb',
                                    ],
                                    state={'lit': 'true'},
                                ),
                            ),
                            type='minecraft:location_check',
                        ),
                        LootConditionMatchTool(
                            predicate=ItemPredicate(
                                items=[
                                    'minecraft:wooden_axe',
                                    'minecraft:golden_axe',
                                    'minecraft:stone_axe',
                                    'minecraft:copper_axe',
                                    'minecraft:iron_axe',
                                    'minecraft:diamond_axe',
                                    'minecraft:netherite_axe',
                                ],
                            ),
                            type='minecraft:match_tool',
                        ),
                    ],
                    type='minecraft:all_of',
                ),
            ),
            trigger='minecraft:item_used_on_block',
        ),
    },
    requirements=[['lighten_up']],
    sends_telemetry_event=True,
)

LIGHTNING_ROD_WITH_VILLAGER_NO_FIRE = Advancement(
    parent='minecraft:adventure/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:lightning_rod'),
        title=TextObjectStruct2(translate='advancements.adventure.lightning_rod_with_villager_no_fire.title'),
        description=TextObjectStruct2(translate='advancements.adventure.lightning_rod_with_villager_no_fire.description'),
    ),
    criteria={
        'lightning_rod_with_villager_no_fire': AdvancementCriterionLightningStrike(
            conditions=LightningStrikeTriggerTypeArg(
                lightning=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(
                        distance=DistancePredicate(absolute=MinMaxBounds(max=30.0)),
                        type_specific_lightning=LightningBoltPredicate(blocks_set_on_fire=0),
                    ),
                    type='minecraft:entity_properties',
                ),
                bystander=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:villager'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:lightning_strike',
        ),
    },
    requirements=[['lightning_rod_with_villager_no_fire']],
    sends_telemetry_event=True,
)

MINECRAFT_TRIALS_EDITION = Advancement(
    parent='minecraft:adventure/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:chiseled_tuff'),
        title=TextObjectStruct2(translate='advancements.adventure.minecraft_trials_edition.title'),
        description=TextObjectStruct2(translate='advancements.adventure.minecraft_trials_edition.description'),
    ),
    criteria={
        'minecraft_trials_edition': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(location=LocationPredicate(structures='minecraft:trial_chambers')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
    },
    requirements=[['minecraft_trials_edition']],
    sends_telemetry_event=True,
)

OL_BETSY = Advancement(
    parent='minecraft:adventure/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:crossbow'),
        title=TextObjectStruct2(translate='advancements.adventure.ol_betsy.title'),
        description=TextObjectStruct2(translate='advancements.adventure.ol_betsy.description'),
    ),
    criteria={
        'shot_crossbow': AdvancementCriterionShotCrossbow(
            conditions=ShotCrossbowTriggerTypeArg(item=ItemPredicate(items='minecraft:crossbow')),
            trigger='minecraft:shot_crossbow',
        ),
    },
    requirements=[['shot_crossbow']],
    sends_telemetry_event=True,
)

OVEROVERKILL = Advancement(
    parent='minecraft:adventure/minecraft_trials_edition',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:mace'),
        title=TextObjectStruct2(translate='advancements.adventure.overoverkill.title'),
        description=TextObjectStruct2(translate='advancements.adventure.overoverkill.description'),
        frame=AdvancementFrame.CHALLENGE,
    ),
    criteria={
        'overoverkill': AdvancementCriterionPlayerHurtEntity(
            conditions=PlayerHurtEntityTriggerTypeArg(
                damage=DamagePredicate(
                    dealt=MinMaxBounds(min=100.0),
                    type=DamageSourcePredicate(
                        tags=[DamageTagPredicate(id='#minecraft:mace_smash', expected=True)],
                        direct_entity=EntitySubPredicateMap(
                            entity_type='minecraft:player',
                            equipment={EquipmentPredicateSlot.MAINHAND: ItemPredicate(items='minecraft:mace')},
                        ),
                    ),
                ),
            ),
            trigger='minecraft:player_hurt_entity',
        ),
    },
    requirements=[['overoverkill']],
    rewards=AdvancementRewards(experience=50),
    sends_telemetry_event=True,
)

PLAY_JUKEBOX_IN_MEADOWS = Advancement(
    parent='minecraft:adventure/sleep_in_bed',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:jukebox'),
        title=TextObjectStruct2(translate='advancements.adventure.play_jukebox_in_meadows.title'),
        description=TextObjectStruct2(translate='advancements.adventure.play_jukebox_in_meadows.description'),
    ),
    criteria={
        'play_jukebox_in_meadows': AdvancementCriterionItemUsedOnBlock(
            conditions=ItemUesdOnLocationConditions(
                location=LootConditionAllOf(
                    terms=[
                        LootConditionLocationCheck(
                            predicate=LocationPredicate(
                                biomes='minecraft:meadow',
                                block=BlockPredicate(blocks='minecraft:jukebox'),
                            ),
                            type='minecraft:location_check',
                        ),
                        LootConditionMatchTool(
                            predicate=ItemPredicate(predicates={'minecraft:jukebox_playable': {}}),
                            type='minecraft:match_tool',
                        ),
                    ],
                    type='minecraft:all_of',
                ),
            ),
            trigger='minecraft:item_used_on_block',
        ),
    },
    requirements=[['play_jukebox_in_meadows']],
    sends_telemetry_event=True,
)

READ_POWER_OF_CHISELED_BOOKSHELF = Advancement(
    parent='minecraft:adventure/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:chiseled_bookshelf'),
        title=TextObjectStruct2(translate='advancements.adventure.read_power_from_chiseled_bookshelf.title'),
        description=TextObjectStruct2(translate='advancements.adventure.read_power_from_chiseled_bookshelf.description'),
    ),
    criteria={
        'chiseled_bookshelf': AdvancementCriterionPlacedBlock(
            conditions=ItemUesdOnLocationConditions(
                location=LootConditionAllOf(
                    terms=[
                        LootConditionMatchBlock(blocks='minecraft:chiseled_bookshelf', type='minecraft:match_block'),
                        LootConditionAnyOf(
                            terms=[
                                LootConditionLocationCheck(
                                    offsetZ=1,
                                    predicate=LocationPredicate(
                                        block=BlockPredicate(blocks='minecraft:comparator', state={'facing': 'north'}),
                                    ),
                                    type='minecraft:location_check',
                                ),
                                LootConditionLocationCheck(
                                    offsetZ=-1,
                                    predicate=LocationPredicate(
                                        block=BlockPredicate(blocks='minecraft:comparator', state={'facing': 'south'}),
                                    ),
                                    type='minecraft:location_check',
                                ),
                                LootConditionLocationCheck(
                                    offsetX=1,
                                    predicate=LocationPredicate(
                                        block=BlockPredicate(blocks='minecraft:comparator', state={'facing': 'west'}),
                                    ),
                                    type='minecraft:location_check',
                                ),
                                LootConditionLocationCheck(
                                    offsetX=-1,
                                    predicate=LocationPredicate(
                                        block=BlockPredicate(blocks='minecraft:comparator', state={'facing': 'east'}),
                                    ),
                                    type='minecraft:location_check',
                                ),
                            ],
                            type='minecraft:any_of',
                        ),
                    ],
                    type='minecraft:all_of',
                ),
            ),
            trigger='minecraft:placed_block',
        ),
        'comparator': AdvancementCriterionPlacedBlock(
            conditions=ItemUesdOnLocationConditions(
                location=LootConditionAnyOf(
                    terms=[
                        LootConditionAllOf(
                            terms=[
                                LootConditionMatchBlock(
                                    blocks='minecraft:comparator',
                                    state={'facing': 'north'},
                                    type='minecraft:match_block',
                                ),
                                LootConditionLocationCheck(
                                    offsetZ=-1,
                                    predicate=LocationPredicate(block=BlockPredicate(blocks='minecraft:chiseled_bookshelf')),
                                    type='minecraft:location_check',
                                ),
                            ],
                            type='minecraft:all_of',
                        ),
                        LootConditionAllOf(
                            terms=[
                                LootConditionMatchBlock(
                                    blocks='minecraft:comparator',
                                    state={'facing': 'south'},
                                    type='minecraft:match_block',
                                ),
                                LootConditionLocationCheck(
                                    offsetZ=1,
                                    predicate=LocationPredicate(block=BlockPredicate(blocks='minecraft:chiseled_bookshelf')),
                                    type='minecraft:location_check',
                                ),
                            ],
                            type='minecraft:all_of',
                        ),
                        LootConditionAllOf(
                            terms=[
                                LootConditionMatchBlock(
                                    blocks='minecraft:comparator',
                                    state={'facing': 'west'},
                                    type='minecraft:match_block',
                                ),
                                LootConditionLocationCheck(
                                    offsetX=-1,
                                    predicate=LocationPredicate(block=BlockPredicate(blocks='minecraft:chiseled_bookshelf')),
                                    type='minecraft:location_check',
                                ),
                            ],
                            type='minecraft:all_of',
                        ),
                        LootConditionAllOf(
                            terms=[
                                LootConditionMatchBlock(
                                    blocks='minecraft:comparator',
                                    state={'facing': 'east'},
                                    type='minecraft:match_block',
                                ),
                                LootConditionLocationCheck(
                                    offsetX=1,
                                    predicate=LocationPredicate(block=BlockPredicate(blocks='minecraft:chiseled_bookshelf')),
                                    type='minecraft:location_check',
                                ),
                            ],
                            type='minecraft:all_of',
                        ),
                    ],
                    type='minecraft:any_of',
                ),
            ),
            trigger='minecraft:placed_block',
        ),
    },
    requirements=[['chiseled_bookshelf', 'comparator']],
    sends_telemetry_event=True,
)

REVAULTING = Advancement(
    parent='minecraft:adventure/under_lock_and_key',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:ominous_trial_key'),
        title=TextObjectStruct2(translate='advancements.adventure.revaulting.title'),
        description=TextObjectStruct2(translate='advancements.adventure.revaulting.description'),
        frame=AdvancementFrame.GOAL,
    ),
    criteria={
        'revaulting': AdvancementCriterionItemUsedOnBlock(
            conditions=ItemUesdOnLocationConditions(
                location=LootConditionAllOf(
                    terms=[
                        LootConditionLocationCheck(
                            predicate=LocationPredicate(block=BlockPredicate(blocks='minecraft:vault', state={'ominous': 'true'})),
                            type='minecraft:location_check',
                        ),
                        LootConditionMatchTool(
                            predicate=ItemPredicate(items='minecraft:ominous_trial_key'),
                            type='minecraft:match_tool',
                        ),
                    ],
                    type='minecraft:all_of',
                ),
            ),
            trigger='minecraft:item_used_on_block',
        ),
    },
    requirements=[['revaulting']],
    sends_telemetry_event=True,
)

ROOT = Advancement(
    display=RootAdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:buried_treasure_map'),
        title=TextObjectStruct2(translate='advancements.adventure.root.title'),
        description=TextObjectStruct2(translate='advancements.adventure.root.description'),
        show_toast=False,
        announce_to_chat=False,
        background='minecraft:gui/advancements/backgrounds/adventure',
    ),
    criteria={
        'killed_by_something': AdvancementCriterionEntityKilledPlayer(trigger='minecraft:entity_killed_player'),
        'killed_something': AdvancementCriterionPlayerKilledEntity(trigger='minecraft:player_killed_entity'),
    },
    requirements=[['killed_something', 'killed_by_something']],
    sends_telemetry_event=True,
)

SALVAGE_SHERD = Advancement(
    parent='minecraft:adventure/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:brush'),
        title=TextObjectStruct2(translate='advancements.adventure.salvage_sherd.title'),
        description=TextObjectStruct2(translate='advancements.adventure.salvage_sherd.description'),
    ),
    criteria={
        'desert_pyramid': AdvancementCriterionPlayerGeneratesContainerLoot(
            conditions=LootTableTriggerTypeArg(loot_tables='minecraft:archaeology/desert_pyramid'),
            trigger='minecraft:player_generates_container_loot',
        ),
        'desert_well': AdvancementCriterionPlayerGeneratesContainerLoot(
            conditions=LootTableTriggerTypeArg(loot_tables='minecraft:archaeology/desert_well'),
            trigger='minecraft:player_generates_container_loot',
        ),
        'has_sherd': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:decorated_pot_sherds')]),
            trigger='minecraft:inventory_changed',
        ),
        'ocean_ruin_cold': AdvancementCriterionPlayerGeneratesContainerLoot(
            conditions=LootTableTriggerTypeArg(loot_tables='minecraft:archaeology/ocean_ruin_cold'),
            trigger='minecraft:player_generates_container_loot',
        ),
        'ocean_ruin_warm': AdvancementCriterionPlayerGeneratesContainerLoot(
            conditions=LootTableTriggerTypeArg(loot_tables='minecraft:archaeology/ocean_ruin_warm'),
            trigger='minecraft:player_generates_container_loot',
        ),
        'trail_ruins_common': AdvancementCriterionPlayerGeneratesContainerLoot(
            conditions=LootTableTriggerTypeArg(loot_tables='minecraft:archaeology/trail_ruins_common'),
            trigger='minecraft:player_generates_container_loot',
        ),
        'trail_ruins_rare': AdvancementCriterionPlayerGeneratesContainerLoot(
            conditions=LootTableTriggerTypeArg(loot_tables='minecraft:archaeology/trail_ruins_rare'),
            trigger='minecraft:player_generates_container_loot',
        ),
    },
    requirements=[
        [
            'desert_pyramid',
            'desert_well',
            'ocean_ruin_cold',
            'ocean_ruin_warm',
            'trail_ruins_rare',
            'trail_ruins_common',
        ],
        ['has_sherd'],
    ],
    sends_telemetry_event=True,
)

SHOOT_ARROW = Advancement(
    parent='minecraft:adventure/kill_a_mob',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:bow'),
        title=TextObjectStruct2(translate='advancements.adventure.shoot_arrow.title'),
        description=TextObjectStruct2(translate='advancements.adventure.shoot_arrow.description'),
    ),
    criteria={
        'shot_arrow': AdvancementCriterionPlayerHurtEntity(
            conditions=PlayerHurtEntityTriggerTypeArg(
                damage=DamagePredicate(
                    type=DamageSourcePredicate(
                        tags=[DamageTagPredicate(id='#minecraft:is_projectile', expected=True)],
                        direct_entity=EntitySubPredicateMap(entity_type='#minecraft:arrows'),
                    ),
                ),
            ),
            trigger='minecraft:player_hurt_entity',
        ),
    },
    requirements=[['shot_arrow']],
    sends_telemetry_event=True,
)

SLEEP_IN_BED = Advancement(
    parent='minecraft:adventure/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:red_bed'),
        title=TextObjectStruct2(translate='advancements.adventure.sleep_in_bed.title'),
        description=TextObjectStruct2(translate='advancements.adventure.sleep_in_bed.description'),
    ),
    criteria={'slept_in_bed': AdvancementCriterionSleptInBed(trigger='minecraft:slept_in_bed')},
    requirements=[['slept_in_bed']],
    sends_telemetry_event=True,
)

SNIPER_DUEL = Advancement(
    parent='minecraft:adventure/shoot_arrow',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:arrow'),
        title=TextObjectStruct2(translate='advancements.adventure.sniper_duel.title'),
        description=TextObjectStruct2(translate='advancements.adventure.sniper_duel.description'),
        frame=AdvancementFrame.CHALLENGE,
    ),
    criteria={
        'killed_skeleton': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(
                        distance=DistancePredicate(horizontal=MinMaxBounds(min=50.0)),
                        entity_type='minecraft:skeleton',
                    ),
                    type='minecraft:entity_properties',
                ),
                killing_blow=DamageSourcePredicate(tags=[DamageTagPredicate(id='#minecraft:is_projectile', expected=True)]),
            ),
            trigger='minecraft:player_killed_entity',
        ),
    },
    requirements=[['killed_skeleton']],
    rewards=AdvancementRewards(experience=50),
    sends_telemetry_event=True,
)

SPEAR_MANY_MOBS = Advancement(
    parent='minecraft:adventure/kill_a_mob',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:iron_spear'),
        title=TextObjectStruct2(translate='advancements.adventure.spear_many_mobs.title'),
        description=TextObjectStruct2(translate='advancements.adventure.spear_many_mobs.description'),
        frame=AdvancementFrame.GOAL,
    ),
    criteria={
        'spear_many_mobs': AdvancementCriterionSpearMobs(conditions=SpearMobsTriggerTypeArg(count=5), trigger='minecraft:spear_mobs'),
    },
    requirements=[['spear_many_mobs']],
    sends_telemetry_event=True,
)

SPYGLASS_AT_DRAGON = Advancement(
    parent='minecraft:adventure/spyglass_at_ghast',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:spyglass'),
        title=TextObjectStruct2(translate='advancements.adventure.spyglass_at_dragon.title'),
        description=TextObjectStruct2(translate='advancements.adventure.spyglass_at_dragon.description'),
    ),
    criteria={
        'spyglass_at_dragon': AdvancementCriterionUsingItem(
            conditions=UsingItemTriggerTypeArg(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(
                        type_specific_player=PlayerPredicate(looking_at=EntitySubPredicateMap(entity_type='minecraft:ender_dragon')),
                    ),
                    type='minecraft:entity_properties',
                ),
                item=ItemPredicate(items='minecraft:spyglass'),
            ),
            trigger='minecraft:using_item',
        ),
    },
    requirements=[['spyglass_at_dragon']],
    sends_telemetry_event=True,
)

SPYGLASS_AT_GHAST = Advancement(
    parent='minecraft:adventure/spyglass_at_parrot',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:spyglass'),
        title=TextObjectStruct2(translate='advancements.adventure.spyglass_at_ghast.title'),
        description=TextObjectStruct2(translate='advancements.adventure.spyglass_at_ghast.description'),
    ),
    criteria={
        'spyglass_at_ghast': AdvancementCriterionUsingItem(
            conditions=UsingItemTriggerTypeArg(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(
                        type_specific_player=PlayerPredicate(looking_at=EntitySubPredicateMap(entity_type='minecraft:ghast')),
                    ),
                    type='minecraft:entity_properties',
                ),
                item=ItemPredicate(items='minecraft:spyglass'),
            ),
            trigger='minecraft:using_item',
        ),
    },
    requirements=[['spyglass_at_ghast']],
    sends_telemetry_event=True,
)

SPYGLASS_AT_PARROT = Advancement(
    parent='minecraft:adventure/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:spyglass'),
        title=TextObjectStruct2(translate='advancements.adventure.spyglass_at_parrot.title'),
        description=TextObjectStruct2(translate='advancements.adventure.spyglass_at_parrot.description'),
    ),
    criteria={
        'spyglass_at_parrot': AdvancementCriterionUsingItem(
            conditions=UsingItemTriggerTypeArg(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(
                        type_specific_player=PlayerPredicate(looking_at=EntitySubPredicateMap(entity_type='minecraft:parrot')),
                    ),
                    type='minecraft:entity_properties',
                ),
                item=ItemPredicate(items='minecraft:spyglass'),
            ),
            trigger='minecraft:using_item',
        ),
    },
    requirements=[['spyglass_at_parrot']],
    sends_telemetry_event=True,
)

SUMMON_IRON_GOLEM = Advancement(
    parent='minecraft:adventure/trade',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:carved_pumpkin'),
        title=TextObjectStruct2(translate='advancements.adventure.summon_iron_golem.title'),
        description=TextObjectStruct2(translate='advancements.adventure.summon_iron_golem.description'),
        frame=AdvancementFrame.GOAL,
    ),
    criteria={
        'summoned_golem': AdvancementCriterionSummonedEntity(
            conditions=SummonedEntityTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:iron_golem'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:summoned_entity',
        ),
    },
    requirements=[['summoned_golem']],
    sends_telemetry_event=True,
)

THROW_TRIDENT = Advancement(
    parent='minecraft:adventure/kill_a_mob',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:trident'),
        title=TextObjectStruct2(translate='advancements.adventure.throw_trident.title'),
        description=TextObjectStruct2(translate='advancements.adventure.throw_trident.description'),
    ),
    criteria={
        'shot_trident': AdvancementCriterionPlayerHurtEntity(
            conditions=PlayerHurtEntityTriggerTypeArg(
                damage=DamagePredicate(
                    type=DamageSourcePredicate(
                        tags=[DamageTagPredicate(id='#minecraft:is_projectile', expected=True)],
                        direct_entity=EntitySubPredicateMap(entity_type='minecraft:trident'),
                    ),
                ),
            ),
            trigger='minecraft:player_hurt_entity',
        ),
    },
    requirements=[['shot_trident']],
    sends_telemetry_event=True,
)

TOTEM_OF_UNDYING = Advancement(
    parent='minecraft:adventure/kill_a_mob',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:totem_of_undying'),
        title=TextObjectStruct2(translate='advancements.adventure.totem_of_undying.title'),
        description=TextObjectStruct2(translate='advancements.adventure.totem_of_undying.description'),
        frame=AdvancementFrame.GOAL,
    ),
    criteria={
        'used_totem': AdvancementCriterionUsedTotem(
            conditions=UsedTotemTriggerTypeArg(item=ItemPredicate(items='minecraft:totem_of_undying')),
            trigger='minecraft:used_totem',
        ),
    },
    requirements=[['used_totem']],
    sends_telemetry_event=True,
)

TRADE = Advancement(
    parent='minecraft:adventure/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:emerald'),
        title=TextObjectStruct2(translate='advancements.adventure.trade.title'),
        description=TextObjectStruct2(translate='advancements.adventure.trade.description'),
    ),
    criteria={'traded': AdvancementCriterionVillagerTrade(trigger='minecraft:villager_trade')},
    requirements=[['traded']],
    sends_telemetry_event=True,
)

TRADE_AT_WORLD_HEIGHT = Advancement(
    parent='minecraft:adventure/trade',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:emerald'),
        title=TextObjectStruct2(translate='advancements.adventure.trade_at_world_height.title'),
        description=TextObjectStruct2(translate='advancements.adventure.trade_at_world_height.description'),
    ),
    criteria={
        'trade_at_world_height': AdvancementCriterionVillagerTrade(
            conditions=TradeTriggerTypeArg(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(
                        location=LocationPredicate(position=PositionStruct(y=MinMaxBounds(min=319.0))),
                    ),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:villager_trade',
        ),
    },
    requirements=[['trade_at_world_height']],
    sends_telemetry_event=True,
)

TRIM_WITH_ALL_EXCLUSIVE_ARMOR_PATTERNS = Advancement(
    parent='minecraft:adventure/trim_with_any_armor_pattern',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:silence_armor_trim_smithing_template'),
        title=TextObjectStruct2(translate='advancements.adventure.trim_with_all_exclusive_armor_patterns.title'),
        description=TextObjectStruct2(translate='advancements.adventure.trim_with_all_exclusive_armor_patterns.description'),
        frame=AdvancementFrame.CHALLENGE,
    ),
    criteria={
        'armor_trimmed_minecraft:rib_armor_trim_smithing_template_smithing_trim': AdvancementCriterionRecipeCrafted(
            conditions=RecipeCraftedTriggerTypeArg(recipes='minecraft:rib_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_crafted',
        ),
        'armor_trimmed_minecraft:silence_armor_trim_smithing_template_smithing_trim': AdvancementCriterionRecipeCrafted(
            conditions=RecipeCraftedTriggerTypeArg(recipes='minecraft:silence_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_crafted',
        ),
        'armor_trimmed_minecraft:snout_armor_trim_smithing_template_smithing_trim': AdvancementCriterionRecipeCrafted(
            conditions=RecipeCraftedTriggerTypeArg(recipes='minecraft:snout_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_crafted',
        ),
        'armor_trimmed_minecraft:spire_armor_trim_smithing_template_smithing_trim': AdvancementCriterionRecipeCrafted(
            conditions=RecipeCraftedTriggerTypeArg(recipes='minecraft:spire_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_crafted',
        ),
        'armor_trimmed_minecraft:tide_armor_trim_smithing_template_smithing_trim': AdvancementCriterionRecipeCrafted(
            conditions=RecipeCraftedTriggerTypeArg(recipes='minecraft:tide_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_crafted',
        ),
        'armor_trimmed_minecraft:vex_armor_trim_smithing_template_smithing_trim': AdvancementCriterionRecipeCrafted(
            conditions=RecipeCraftedTriggerTypeArg(recipes='minecraft:vex_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_crafted',
        ),
        'armor_trimmed_minecraft:ward_armor_trim_smithing_template_smithing_trim': AdvancementCriterionRecipeCrafted(
            conditions=RecipeCraftedTriggerTypeArg(recipes='minecraft:ward_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_crafted',
        ),
        'armor_trimmed_minecraft:wayfinder_armor_trim_smithing_template_smithing_trim': AdvancementCriterionRecipeCrafted(
            conditions=RecipeCraftedTriggerTypeArg(recipes='minecraft:wayfinder_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_crafted',
        ),
    },
    requirements=[
        ['armor_trimmed_minecraft:rib_armor_trim_smithing_template_smithing_trim'],
        ['armor_trimmed_minecraft:silence_armor_trim_smithing_template_smithing_trim'],
        ['armor_trimmed_minecraft:snout_armor_trim_smithing_template_smithing_trim'],
        ['armor_trimmed_minecraft:spire_armor_trim_smithing_template_smithing_trim'],
        ['armor_trimmed_minecraft:tide_armor_trim_smithing_template_smithing_trim'],
        ['armor_trimmed_minecraft:vex_armor_trim_smithing_template_smithing_trim'],
        ['armor_trimmed_minecraft:ward_armor_trim_smithing_template_smithing_trim'],
        ['armor_trimmed_minecraft:wayfinder_armor_trim_smithing_template_smithing_trim'],
    ],
    rewards=AdvancementRewards(experience=150),
    sends_telemetry_event=True,
)

TRIM_WITH_ANY_ARMOR_PATTERN = Advancement(
    parent='minecraft:adventure/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:dune_armor_trim_smithing_template'),
        title=TextObjectStruct2(translate='advancements.adventure.trim_with_any_armor_pattern.title'),
        description=TextObjectStruct2(translate='advancements.adventure.trim_with_any_armor_pattern.description'),
    ),
    criteria={
        'armor_trimmed_minecraft:bolt_armor_trim_smithing_template_smithing_trim': AdvancementCriterionRecipeCrafted(
            conditions=RecipeCraftedTriggerTypeArg(recipes='minecraft:bolt_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_crafted',
        ),
        'armor_trimmed_minecraft:coast_armor_trim_smithing_template_smithing_trim': AdvancementCriterionRecipeCrafted(
            conditions=RecipeCraftedTriggerTypeArg(recipes='minecraft:coast_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_crafted',
        ),
        'armor_trimmed_minecraft:dune_armor_trim_smithing_template_smithing_trim': AdvancementCriterionRecipeCrafted(
            conditions=RecipeCraftedTriggerTypeArg(recipes='minecraft:dune_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_crafted',
        ),
        'armor_trimmed_minecraft:eye_armor_trim_smithing_template_smithing_trim': AdvancementCriterionRecipeCrafted(
            conditions=RecipeCraftedTriggerTypeArg(recipes='minecraft:eye_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_crafted',
        ),
        'armor_trimmed_minecraft:flow_armor_trim_smithing_template_smithing_trim': AdvancementCriterionRecipeCrafted(
            conditions=RecipeCraftedTriggerTypeArg(recipes='minecraft:flow_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_crafted',
        ),
        'armor_trimmed_minecraft:host_armor_trim_smithing_template_smithing_trim': AdvancementCriterionRecipeCrafted(
            conditions=RecipeCraftedTriggerTypeArg(recipes='minecraft:host_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_crafted',
        ),
        'armor_trimmed_minecraft:raiser_armor_trim_smithing_template_smithing_trim': AdvancementCriterionRecipeCrafted(
            conditions=RecipeCraftedTriggerTypeArg(recipes='minecraft:raiser_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_crafted',
        ),
        'armor_trimmed_minecraft:rib_armor_trim_smithing_template_smithing_trim': AdvancementCriterionRecipeCrafted(
            conditions=RecipeCraftedTriggerTypeArg(recipes='minecraft:rib_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_crafted',
        ),
        'armor_trimmed_minecraft:sentry_armor_trim_smithing_template_smithing_trim': AdvancementCriterionRecipeCrafted(
            conditions=RecipeCraftedTriggerTypeArg(recipes='minecraft:sentry_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_crafted',
        ),
        'armor_trimmed_minecraft:shaper_armor_trim_smithing_template_smithing_trim': AdvancementCriterionRecipeCrafted(
            conditions=RecipeCraftedTriggerTypeArg(recipes='minecraft:shaper_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_crafted',
        ),
        'armor_trimmed_minecraft:silence_armor_trim_smithing_template_smithing_trim': AdvancementCriterionRecipeCrafted(
            conditions=RecipeCraftedTriggerTypeArg(recipes='minecraft:silence_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_crafted',
        ),
        'armor_trimmed_minecraft:snout_armor_trim_smithing_template_smithing_trim': AdvancementCriterionRecipeCrafted(
            conditions=RecipeCraftedTriggerTypeArg(recipes='minecraft:snout_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_crafted',
        ),
        'armor_trimmed_minecraft:spire_armor_trim_smithing_template_smithing_trim': AdvancementCriterionRecipeCrafted(
            conditions=RecipeCraftedTriggerTypeArg(recipes='minecraft:spire_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_crafted',
        ),
        'armor_trimmed_minecraft:tide_armor_trim_smithing_template_smithing_trim': AdvancementCriterionRecipeCrafted(
            conditions=RecipeCraftedTriggerTypeArg(recipes='minecraft:tide_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_crafted',
        ),
        'armor_trimmed_minecraft:vex_armor_trim_smithing_template_smithing_trim': AdvancementCriterionRecipeCrafted(
            conditions=RecipeCraftedTriggerTypeArg(recipes='minecraft:vex_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_crafted',
        ),
        'armor_trimmed_minecraft:ward_armor_trim_smithing_template_smithing_trim': AdvancementCriterionRecipeCrafted(
            conditions=RecipeCraftedTriggerTypeArg(recipes='minecraft:ward_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_crafted',
        ),
        'armor_trimmed_minecraft:wayfinder_armor_trim_smithing_template_smithing_trim': AdvancementCriterionRecipeCrafted(
            conditions=RecipeCraftedTriggerTypeArg(recipes='minecraft:wayfinder_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_crafted',
        ),
        'armor_trimmed_minecraft:wild_armor_trim_smithing_template_smithing_trim': AdvancementCriterionRecipeCrafted(
            conditions=RecipeCraftedTriggerTypeArg(recipes='minecraft:wild_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_crafted',
        ),
    },
    requirements=[
        [
            'armor_trimmed_minecraft:bolt_armor_trim_smithing_template_smithing_trim',
            'armor_trimmed_minecraft:coast_armor_trim_smithing_template_smithing_trim',
            'armor_trimmed_minecraft:dune_armor_trim_smithing_template_smithing_trim',
            'armor_trimmed_minecraft:eye_armor_trim_smithing_template_smithing_trim',
            'armor_trimmed_minecraft:flow_armor_trim_smithing_template_smithing_trim',
            'armor_trimmed_minecraft:host_armor_trim_smithing_template_smithing_trim',
            'armor_trimmed_minecraft:raiser_armor_trim_smithing_template_smithing_trim',
            'armor_trimmed_minecraft:rib_armor_trim_smithing_template_smithing_trim',
            'armor_trimmed_minecraft:sentry_armor_trim_smithing_template_smithing_trim',
            'armor_trimmed_minecraft:shaper_armor_trim_smithing_template_smithing_trim',
            'armor_trimmed_minecraft:silence_armor_trim_smithing_template_smithing_trim',
            'armor_trimmed_minecraft:snout_armor_trim_smithing_template_smithing_trim',
            'armor_trimmed_minecraft:spire_armor_trim_smithing_template_smithing_trim',
            'armor_trimmed_minecraft:tide_armor_trim_smithing_template_smithing_trim',
            'armor_trimmed_minecraft:vex_armor_trim_smithing_template_smithing_trim',
            'armor_trimmed_minecraft:ward_armor_trim_smithing_template_smithing_trim',
            'armor_trimmed_minecraft:wayfinder_armor_trim_smithing_template_smithing_trim',
            'armor_trimmed_minecraft:wild_armor_trim_smithing_template_smithing_trim',
        ],
    ],
    sends_telemetry_event=True,
)

TWO_BIRDS_ONE_ARROW = Advancement(
    parent='minecraft:adventure/ol_betsy',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:crossbow'),
        title=TextObjectStruct2(translate='advancements.adventure.two_birds_one_arrow.title'),
        description=TextObjectStruct2(translate='advancements.adventure.two_birds_one_arrow.description'),
        frame=AdvancementFrame.CHALLENGE,
    ),
    criteria={
        'two_birds': AdvancementCriterionKilledByArrow(
            conditions=KilledByArrowTriggerTypeArg(
                fired_from_weapon=ItemPredicate(items='minecraft:crossbow'),
                victims=[
                    LootConditionEntityProperties(
                        entity=EntityTarget.THIS,
                        predicate=EntitySubPredicateMap(entity_type='minecraft:phantom'),
                        type='minecraft:entity_properties',
                    ),
                    LootConditionEntityProperties(
                        entity=EntityTarget.THIS,
                        predicate=EntitySubPredicateMap(entity_type='minecraft:phantom'),
                        type='minecraft:entity_properties',
                    ),
                ],
            ),
            trigger='minecraft:killed_by_arrow',
        ),
    },
    requirements=[['two_birds']],
    rewards=AdvancementRewards(experience=65),
    sends_telemetry_event=True,
)

UNDER_LOCK_AND_KEY = Advancement(
    parent='minecraft:adventure/minecraft_trials_edition',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:trial_key'),
        title=TextObjectStruct2(translate='advancements.adventure.under_lock_and_key.title'),
        description=TextObjectStruct2(translate='advancements.adventure.under_lock_and_key.description'),
    ),
    criteria={
        'under_lock_and_key': AdvancementCriterionItemUsedOnBlock(
            conditions=ItemUesdOnLocationConditions(
                location=LootConditionAllOf(
                    terms=[
                        LootConditionLocationCheck(
                            predicate=LocationPredicate(
                                block=BlockPredicate(blocks='minecraft:vault', state={'ominous': 'false'}),
                            ),
                            type='minecraft:location_check',
                        ),
                        LootConditionMatchTool(
                            predicate=ItemPredicate(items='minecraft:trial_key'),
                            type='minecraft:match_tool',
                        ),
                    ],
                    type='minecraft:all_of',
                ),
            ),
            trigger='minecraft:item_used_on_block',
        ),
    },
    requirements=[['under_lock_and_key']],
    sends_telemetry_event=True,
)

USE_LODESTONE = Advancement(
    parent='minecraft:adventure/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:lodestone'),
        title=TextObjectStruct2(translate='advancements.adventure.use_lodestone.title'),
        description=TextObjectStruct2(translate='advancements.adventure.use_lodestone.description'),
    ),
    criteria={
        'use_lodestone': AdvancementCriterionItemUsedOnBlock(
            conditions=ItemUesdOnLocationConditions(
                location=LootConditionAllOf(
                    terms=[
                        LootConditionLocationCheck(
                            predicate=LocationPredicate(block=BlockPredicate(blocks='minecraft:lodestone')),
                            type='minecraft:location_check',
                        ),
                        LootConditionMatchTool(
                            predicate=ItemPredicate(items='minecraft:compass'),
                            type='minecraft:match_tool',
                        ),
                    ],
                    type='minecraft:all_of',
                ),
            ),
            trigger='minecraft:item_used_on_block',
        ),
    },
    requirements=[['use_lodestone']],
    sends_telemetry_event=True,
)

VERY_VERY_FRIGHTENING = Advancement(
    parent='minecraft:adventure/throw_trident',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:trident'),
        title=TextObjectStruct2(translate='advancements.adventure.very_very_frightening.title'),
        description=TextObjectStruct2(translate='advancements.adventure.very_very_frightening.description'),
    ),
    criteria={
        'struck_villager': AdvancementCriterionChanneledLightning(
            conditions=ChanneledLightningTriggerTypeArg(
                victims=[
                    LootConditionEntityProperties(
                        entity=EntityTarget.THIS,
                        predicate=EntitySubPredicateMap(entity_type='minecraft:villager'),
                        type='minecraft:entity_properties',
                    ),
                ],
            ),
            trigger='minecraft:channeled_lightning',
        ),
    },
    requirements=[['struck_villager']],
    sends_telemetry_event=True,
)

VOLUNTARY_EXILE = Advancement(
    parent='minecraft:adventure/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(
            id='minecraft:white_banner',
            components=DataComponentPatch(
                banner_patterns=[
                    BannerPatternLayer(color=DyeColor.CYAN, pattern='minecraft:rhombus'),
                    BannerPatternLayer(color=DyeColor.LIGHTGRAY, pattern='minecraft:stripe_bottom'),
                    BannerPatternLayer(color=DyeColor.GRAY, pattern='minecraft:stripe_center'),
                    BannerPatternLayer(color=DyeColor.LIGHTGRAY, pattern='minecraft:border'),
                    BannerPatternLayer(color=DyeColor.BLACK, pattern='minecraft:stripe_middle'),
                    BannerPatternLayer(color=DyeColor.LIGHTGRAY, pattern='minecraft:half_horizontal'),
                    BannerPatternLayer(color=DyeColor.LIGHTGRAY, pattern='minecraft:circle'),
                    BannerPatternLayer(color=DyeColor.BLACK, pattern='minecraft:border'),
                ],
                item_name=TextObjectStruct2(translate='block.minecraft.ominous_banner'),
                rarity=Rarity.UNCOMMON,
                tooltip_display=TooltipDisplay(hidden_components=['minecraft:banner_patterns']),
            ),
        ),
        title=TextObjectStruct2(translate='advancements.adventure.voluntary_exile.title'),
        description=TextObjectStruct2(translate='advancements.adventure.voluntary_exile.description'),
        hidden=True,
    ),
    criteria={
        'voluntary_exile': AdvancementCriterionPlayerKilledEntity(
            conditions=KilledTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(
                        entity_type='#minecraft:raiders',
                        equipment={
                            EquipmentPredicateSlot.HEAD: ItemPredicate(
                                items='minecraft:white_banner',
                                components=DataComponentExactPredicate(
                                    banner_patterns=[
                                        BannerPatternLayer(color=DyeColor.CYAN, pattern='minecraft:rhombus'),
                                        BannerPatternLayer(color=DyeColor.LIGHTGRAY, pattern='minecraft:stripe_bottom'),
                                        BannerPatternLayer(color=DyeColor.GRAY, pattern='minecraft:stripe_center'),
                                        BannerPatternLayer(color=DyeColor.LIGHTGRAY, pattern='minecraft:border'),
                                        BannerPatternLayer(color=DyeColor.BLACK, pattern='minecraft:stripe_middle'),
                                        BannerPatternLayer(
                                            color=DyeColor.LIGHTGRAY,
                                            pattern='minecraft:half_horizontal',
                                        ),
                                        BannerPatternLayer(color=DyeColor.LIGHTGRAY, pattern='minecraft:circle'),
                                        BannerPatternLayer(color=DyeColor.BLACK, pattern='minecraft:border'),
                                    ],
                                    item_name=TextObjectStruct2(translate='block.minecraft.ominous_banner'),
                                ),
                            ),
                        },
                    ),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_killed_entity',
        ),
    },
    requirements=[['voluntary_exile']],
    sends_telemetry_event=True,
)

WALK_ON_POWDER_SNOW_WITH_LEATHER_BOOTS = Advancement(
    parent='minecraft:adventure/sleep_in_bed',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:leather_boots'),
        title=TextObjectStruct2(translate='advancements.adventure.walk_on_powder_snow_with_leather_boots.title'),
        description=TextObjectStruct2(translate='advancements.adventure.walk_on_powder_snow_with_leather_boots.description'),
    ),
    criteria={
        'walk_on_powder_snow_with_leather_boots': AdvancementCriterionLocation(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(
                        equipment={EquipmentPredicateSlot.FEET: ItemPredicate(items='minecraft:leather_boots')},
                        stepping_on=LocationPredicate(block=BlockPredicate(blocks='minecraft:powder_snow')),
                    ),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:location',
        ),
    },
    requirements=[['walk_on_powder_snow_with_leather_boots']],
    sends_telemetry_event=True,
)

WHOS_THE_PILLAGER_NOW = Advancement(
    parent='minecraft:adventure/ol_betsy',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:crossbow'),
        title=TextObjectStruct2(translate='advancements.adventure.whos_the_pillager_now.title'),
        description=TextObjectStruct2(translate='advancements.adventure.whos_the_pillager_now.description'),
    ),
    criteria={
        'kill_pillager': AdvancementCriterionKilledByArrow(
            conditions=KilledByArrowTriggerTypeArg(
                fired_from_weapon=ItemPredicate(items='minecraft:crossbow'),
                victims=[
                    LootConditionEntityProperties(
                        entity=EntityTarget.THIS,
                        predicate=EntitySubPredicateMap(entity_type='minecraft:pillager'),
                        type='minecraft:entity_properties',
                    ),
                ],
            ),
            trigger='minecraft:killed_by_arrow',
        ),
    },
    requirements=[['kill_pillager']],
    sends_telemetry_event=True,
)

WHO_NEEDS_ROCKETS = Advancement(
    parent='minecraft:adventure/minecraft_trials_edition',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:wind_charge'),
        title=TextObjectStruct2(translate='advancements.adventure.who_needs_rockets.title'),
        description=TextObjectStruct2(translate='advancements.adventure.who_needs_rockets.description'),
    ),
    criteria={
        'who_needs_rockets': AdvancementCriterionFallAfterExplosion(
            conditions=FallAfterExplosionTriggerTypeArg(
                distance=DistancePredicate(y=MinMaxBounds(min=7.0)),
                cause=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:wind_charge'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:fall_after_explosion',
        ),
    },
    requirements=[['who_needs_rockets']],
    sends_telemetry_event=True,
)
