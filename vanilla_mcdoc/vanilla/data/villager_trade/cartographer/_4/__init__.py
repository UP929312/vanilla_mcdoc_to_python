"""Vanilla's data/villager_trade/cartographer/_4/ files"""
from vanilla_mcdoc.data.advancement.predicate.EntitySubPredicateMap import EntitySubPredicateMap
from vanilla_mcdoc.data.loot.EntityTarget import EntityTarget
from vanilla_mcdoc.data.loot.condition.LootCondition import LootConditionEntityProperties
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

EMERALD_BLACK_BANNER = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=2),
    gives=ItemStackOfComponent(id='minecraft:black_banner'),
    max_uses=12,
    reputation_discount=0.05,
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:swamp'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_BLUE_BANNER = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=2),
    gives=ItemStackOfComponent(id='minecraft:blue_banner'),
    max_uses=12,
    reputation_discount=0.05,
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': ['minecraft:snow', 'minecraft:taiga']}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_BROWN_BANNER = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=2),
    gives=ItemStackOfComponent(id='minecraft:brown_banner'),
    max_uses=12,
    reputation_discount=0.05,
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': ['minecraft:plains', 'minecraft:jungle']}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_CYAN_BANNER = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=2),
    gives=ItemStackOfComponent(id='minecraft:cyan_banner'),
    max_uses=12,
    reputation_discount=0.05,
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': ['minecraft:desert', 'minecraft:snow']}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_GRAY_BANNER = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=2),
    gives=ItemStackOfComponent(id='minecraft:gray_banner'),
    max_uses=12,
    reputation_discount=0.05,
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:desert'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_GREEN_BANNER = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=2),
    gives=ItemStackOfComponent(id='minecraft:green_banner'),
    max_uses=12,
    reputation_discount=0.05,
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(
            predicates={'minecraft:villager/variant': ['minecraft:desert', 'minecraft:savanna', 'minecraft:jungle']},
        ),
        type='minecraft:entity_properties',
    ),
)

EMERALD_ITEM_FRAME = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=7),
    gives=ItemStackOfComponent(id='minecraft:item_frame'),
    max_uses=12,
    reputation_discount=0.05,
    xp=15,
)

EMERALD_LIGHT_BLUE_BANNER = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=2),
    gives=ItemStackOfComponent(id='minecraft:light_blue_banner'),
    max_uses=12,
    reputation_discount=0.05,
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': ['minecraft:snow', 'minecraft:swamp']}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_LIME_BANNER = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=2),
    gives=ItemStackOfComponent(id='minecraft:lime_banner'),
    max_uses=12,
    reputation_discount=0.05,
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': ['minecraft:desert', 'minecraft:taiga']}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_MAGENTA_BANNER = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=2),
    gives=ItemStackOfComponent(id='minecraft:magenta_banner'),
    max_uses=12,
    reputation_discount=0.05,
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:savanna'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_ORANGE_BANNER = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=2),
    gives=ItemStackOfComponent(id='minecraft:orange_banner'),
    max_uses=12,
    reputation_discount=0.05,
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': ['minecraft:savanna', 'minecraft:desert']}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_PINK_BANNER = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=2),
    gives=ItemStackOfComponent(id='minecraft:pink_banner'),
    max_uses=12,
    reputation_discount=0.05,
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': ['minecraft:taiga', 'minecraft:plains']}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_PURPLE_BANNER = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=2),
    gives=ItemStackOfComponent(id='minecraft:purple_banner'),
    max_uses=12,
    reputation_discount=0.05,
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': ['minecraft:taiga', 'minecraft:swamp']}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_RED_BANNER = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=2),
    gives=ItemStackOfComponent(id='minecraft:red_banner'),
    max_uses=12,
    reputation_discount=0.05,
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': ['minecraft:snow', 'minecraft:savanna']}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_WHITE_BANNER = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=2),
    gives=ItemStackOfComponent(id='minecraft:white_banner'),
    max_uses=12,
    reputation_discount=0.05,
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': ['minecraft:snow', 'minecraft:plains']}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_YELLOW_BANNER = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=2),
    gives=ItemStackOfComponent(id='minecraft:yellow_banner'),
    max_uses=12,
    reputation_discount=0.05,
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': ['minecraft:plains', 'minecraft:jungle']}),
        type='minecraft:entity_properties',
    ),
)
