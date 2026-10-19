"""Vanilla's data/villager_trade/cartographer/_3/ files"""
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.loot.function.LootFunction import LootFunctionDiscard, LootFunctionExplorationMap, LootFunctionFiltered
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

COMPASS_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:compass'),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=12,
    reputation_discount=0.05,
    xp=20,
)

EMERALD_AND_COMPASS_BURIED_TRIAL_CHAMBERS_MAP = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=12),
    additional_wants=TradeCost(id='minecraft:compass'),
    gives=ItemStackOfComponent(id='minecraft:buried_trial_chambers_map'),
    given_item_modifier=[
        LootFunctionExplorationMap(
            destination='#minecraft:on_buried_trial_chambers_maps',
            decoration='minecraft:trial_chambers',
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
    xp=10,
)

EMERALD_AND_COMPASS_OCEAN_MONUMENT_MAP = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=13),
    additional_wants=TradeCost(id='minecraft:compass'),
    gives=ItemStackOfComponent(id='minecraft:ocean_monument_map'),
    given_item_modifier=[
        LootFunctionExplorationMap(
            destination='#minecraft:on_ocean_monument_maps',
            decoration='minecraft:monument',
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
    xp=10,
)
