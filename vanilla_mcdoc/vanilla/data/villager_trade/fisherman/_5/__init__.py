"""Vanilla's data/villager_trade/fisherman/_5/ files"""
from vanilla_mcdoc.data.advancement.predicate.EntitySubPredicateMap import EntitySubPredicateMap
from vanilla_mcdoc.data.loot.EntityTarget import EntityTarget
from vanilla_mcdoc.data.loot.condition.LootCondition import LootConditionEntityProperties
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

ACACIA_BOAT_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:acacia_boat'),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=12,
    reputation_discount=0.05,
    xp=30,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:savanna'}),
        type='minecraft:entity_properties',
    ),
)

DARK_OAK_BOAT_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:dark_oak_boat'),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=12,
    reputation_discount=0.05,
    xp=30,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:swamp'}),
        type='minecraft:entity_properties',
    ),
)

JUNGLE_BOAT_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:jungle_boat'),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=12,
    reputation_discount=0.05,
    xp=30,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': ['minecraft:desert', 'minecraft:jungle']}),
        type='minecraft:entity_properties',
    ),
)

OAK_BOAT_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:oak_boat'),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=12,
    reputation_discount=0.05,
    xp=30,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:plains'}),
        type='minecraft:entity_properties',
    ),
)

PUFFERFISH_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:pufferfish', count=4),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=12,
    reputation_discount=0.05,
    xp=30,
)

SPRUCE_BOAT_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:spruce_boat'),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=12,
    reputation_discount=0.05,
    xp=30,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': ['minecraft:taiga', 'minecraft:snow']}),
        type='minecraft:entity_properties',
    ),
)
