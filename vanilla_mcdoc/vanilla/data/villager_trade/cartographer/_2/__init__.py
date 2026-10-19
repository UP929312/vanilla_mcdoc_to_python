"""Vanilla's data/villager_trade/cartographer/_2/ files"""
from vanilla_mcdoc.data.advancement.predicate.EntitySubPredicateMap import EntitySubPredicateMap
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.loot.EntityTarget import EntityTarget
from vanilla_mcdoc.data.loot.condition.LootCondition import LootConditionEntityProperties
from vanilla_mcdoc.data.loot.function.LootFunction import LootFunctionDiscard, LootFunctionExplorationMap, LootFunctionFiltered
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

EMERALD_AND_COMPASS_EXPLORER_JUNGLE_MAP = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=8),
    additional_wants=TradeCost(id='minecraft:compass'),
    gives=ItemStackOfComponent(id='minecraft:jungle_pyramid_map'),
    given_item_modifier=[
        LootFunctionExplorationMap(
            destination='#minecraft:on_jungle_pyramid_maps',
            decoration='minecraft:jungle_temple',
            search_radius=100,
            type='minecraft:exploration_map',
        ),
        LootFunctionFiltered(
            item_filter=ItemPredicate(predicates={'minecraft:map_id': {}}),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=12,
    reputation_discount=0.2,
    xp=5,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(
            predicates={'minecraft:villager/variant': ['minecraft:swamp', 'minecraft:savanna', 'minecraft:desert']},
        ),
        type='minecraft:entity_properties',
    ),
)

EMERALD_AND_COMPASS_EXPLORER_SWAMP_MAP = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=8),
    additional_wants=TradeCost(id='minecraft:compass'),
    gives=ItemStackOfComponent(id='minecraft:swamp_hut_map'),
    given_item_modifier=[
        LootFunctionExplorationMap(
            destination='#minecraft:on_swamp_hut_maps',
            decoration='minecraft:swamp_hut',
            search_radius=100,
            type='minecraft:exploration_map',
        ),
        LootFunctionFiltered(
            item_filter=ItemPredicate(predicates={'minecraft:map_id': {}}),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=12,
    reputation_discount=0.2,
    xp=5,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(
            predicates={'minecraft:villager/variant': ['minecraft:taiga', 'minecraft:snow', 'minecraft:jungle']},
        ),
        type='minecraft:entity_properties',
    ),
)

EMERALD_AND_COMPASS_VILLAGE_DESERT_MAP = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=8),
    additional_wants=TradeCost(id='minecraft:compass'),
    gives=ItemStackOfComponent(id='minecraft:desert_village_map'),
    given_item_modifier=[
        LootFunctionExplorationMap(
            destination='#minecraft:on_desert_village_maps',
            decoration='minecraft:village_desert',
            search_radius=100,
            type='minecraft:exploration_map',
        ),
        LootFunctionFiltered(
            item_filter=ItemPredicate(predicates={'minecraft:map_id': {}}),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=12,
    reputation_discount=0.2,
    xp=5,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': ['minecraft:savanna', 'minecraft:jungle']}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_AND_COMPASS_VILLAGE_PLAINS_MAP = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=8),
    additional_wants=TradeCost(id='minecraft:compass'),
    gives=ItemStackOfComponent(id='minecraft:plains_village_map'),
    given_item_modifier=[
        LootFunctionExplorationMap(
            destination='#minecraft:on_plains_village_maps',
            decoration='minecraft:village_plains',
            search_radius=100,
            type='minecraft:exploration_map',
        ),
        LootFunctionFiltered(
            item_filter=ItemPredicate(predicates={'minecraft:map_id': {}}),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=12,
    reputation_discount=0.2,
    xp=5,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(
            predicates={
                'minecraft:villager/variant': ['minecraft:taiga', 'minecraft:snow', 'minecraft:savanna', 'minecraft:desert'],
            },
        ),
        type='minecraft:entity_properties',
    ),
)

EMERALD_AND_COMPASS_VILLAGE_SAVANNA_MAP = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=8),
    additional_wants=TradeCost(id='minecraft:compass'),
    gives=ItemStackOfComponent(id='minecraft:savanna_village_map'),
    given_item_modifier=[
        LootFunctionExplorationMap(
            destination='#minecraft:on_savanna_village_maps',
            decoration='minecraft:village_savanna',
            search_radius=100,
            type='minecraft:exploration_map',
        ),
        LootFunctionFiltered(
            item_filter=ItemPredicate(predicates={'minecraft:map_id': {}}),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=12,
    reputation_discount=0.2,
    xp=5,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(
            predicates={'minecraft:villager/variant': ['minecraft:plains', 'minecraft:jungle', 'minecraft:desert']},
        ),
        type='minecraft:entity_properties',
    ),
)

EMERALD_AND_COMPASS_VILLAGE_SNOWY_MAP = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=8),
    additional_wants=TradeCost(id='minecraft:compass'),
    gives=ItemStackOfComponent(id='minecraft:snowy_village_map'),
    given_item_modifier=[
        LootFunctionExplorationMap(
            destination='#minecraft:on_snowy_village_maps',
            decoration='minecraft:village_snowy',
            search_radius=100,
            type='minecraft:exploration_map',
        ),
        LootFunctionFiltered(
            item_filter=ItemPredicate(predicates={'minecraft:map_id': {}}),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=12,
    reputation_discount=0.2,
    xp=5,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': ['minecraft:taiga', 'minecraft:swamp']}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_AND_COMPASS_VILLAGE_TAIGA_MAP = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=8),
    additional_wants=TradeCost(id='minecraft:compass'),
    gives=ItemStackOfComponent(id='minecraft:taiga_village_map'),
    given_item_modifier=[
        LootFunctionExplorationMap(
            destination='#minecraft:on_taiga_village_maps',
            decoration='minecraft:village_taiga',
            search_radius=100,
            type='minecraft:exploration_map',
        ),
        LootFunctionFiltered(
            item_filter=ItemPredicate(predicates={'minecraft:map_id': {}}),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=12,
    reputation_discount=0.2,
    xp=5,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(
            predicates={'minecraft:villager/variant': ['minecraft:swamp', 'minecraft:snow', 'minecraft:plains']},
        ),
        type='minecraft:entity_properties',
    ),
)

GLASS_PANE_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:glass_pane', count=11),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=12,
    reputation_discount=0.05,
    xp=10,
)
