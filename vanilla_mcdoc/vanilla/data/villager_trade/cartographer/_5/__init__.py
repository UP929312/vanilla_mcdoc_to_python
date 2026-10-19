"""Vanilla's data/villager_trade/cartographer/_5/ files"""
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.loot.function.LootFunction import LootFunctionDiscard, LootFunctionExplorationMap, LootFunctionFiltered
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

EMERALD_AND_COMPASS_WOODLAND_MANSION_MAP = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=14),
    additional_wants=TradeCost(id='minecraft:compass'),
    gives=ItemStackOfComponent(id='minecraft:woodland_mansion_map'),
    given_item_modifier=[
        LootFunctionExplorationMap(
            destination='#minecraft:on_woodland_mansion_maps',
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
    xp=30,
)

EMERALD_GLOBE_BANNER_PATTERN = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=8),
    gives=ItemStackOfComponent(id='minecraft:globe_banner_pattern'),
    max_uses=12,
    reputation_discount=0.05,
    xp=30,
)
