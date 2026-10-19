"""Vanilla's data/datapacks/trade_rebalance/data/villager_trade/armorer/_2/ files"""
from vanilla_mcdoc.data.advancement.predicate.EntitySubPredicateMap import EntitySubPredicateMap
from vanilla_mcdoc.data.loot.EntityTarget import EntityTarget
from vanilla_mcdoc.data.loot.condition.LootCondition import LootConditionEntityProperties
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

EMERALD_CHAINMAIL_BOOTS_GROUP_2 = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=4),
    gives=ItemStackOfComponent(id='minecraft:chainmail_boots'),
    max_uses=12,
    reputation_discount=0.05,
    xp=5,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': ['minecraft:jungle', 'minecraft:swamp']}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_CHAINMAIL_CHAINMAIL_GROUP_2 = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=9),
    gives=ItemStackOfComponent(id='minecraft:chainmail_chestplate'),
    max_uses=12,
    reputation_discount=0.05,
    xp=5,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': ['minecraft:jungle', 'minecraft:swamp']}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_CHAINMAIL_HELMET_GROUP_2 = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=5),
    gives=ItemStackOfComponent(id='minecraft:chainmail_helmet'),
    max_uses=12,
    reputation_discount=0.05,
    xp=5,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': ['minecraft:jungle', 'minecraft:swamp']}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_CHAINMAIL_LEGGINGS_GROUP_2 = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=7),
    gives=ItemStackOfComponent(id='minecraft:chainmail_leggings'),
    max_uses=12,
    reputation_discount=0.05,
    xp=5,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': ['minecraft:jungle', 'minecraft:swamp']}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_IRON_BOOTS_GROUP_1 = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=4),
    gives=ItemStackOfComponent(id='minecraft:iron_boots'),
    max_uses=12,
    reputation_discount=0.05,
    xp=5,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(
            predicates={
                'minecraft:villager/variant': ['minecraft:desert', 'minecraft:plains', 'minecraft:savanna', 'minecraft:snow', 'minecraft:taiga'],
            },
        ),
        type='minecraft:entity_properties',
    ),
)

EMERALD_IRON_CHESTPLATE_GROUP_1 = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=9),
    gives=ItemStackOfComponent(id='minecraft:iron_chestplate'),
    max_uses=12,
    reputation_discount=0.05,
    xp=5,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(
            predicates={
                'minecraft:villager/variant': ['minecraft:desert', 'minecraft:plains', 'minecraft:savanna', 'minecraft:snow', 'minecraft:taiga'],
            },
        ),
        type='minecraft:entity_properties',
    ),
)

EMERALD_IRON_HELMET_GROUP_1 = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=5),
    gives=ItemStackOfComponent(id='minecraft:iron_helmet'),
    max_uses=12,
    reputation_discount=0.05,
    xp=5,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(
            predicates={
                'minecraft:villager/variant': ['minecraft:desert', 'minecraft:plains', 'minecraft:savanna', 'minecraft:snow', 'minecraft:taiga'],
            },
        ),
        type='minecraft:entity_properties',
    ),
)

EMERALD_IRON_LEGGINGS_GROUP_1 = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=7),
    gives=ItemStackOfComponent(id='minecraft:iron_leggings'),
    max_uses=12,
    reputation_discount=0.05,
    xp=5,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(
            predicates={
                'minecraft:villager/variant': ['minecraft:desert', 'minecraft:plains', 'minecraft:savanna', 'minecraft:snow', 'minecraft:taiga'],
            },
        ),
        type='minecraft:entity_properties',
    ),
)
