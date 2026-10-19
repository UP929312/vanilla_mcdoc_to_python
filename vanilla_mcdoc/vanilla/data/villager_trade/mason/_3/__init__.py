"""Vanilla's data/villager_trade/mason/_3/ files"""
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

ANDESITE_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:andesite', count=16),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=16,
    reputation_discount=0.05,
    xp=20,
)

DIORITE_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:diorite', count=16),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=16,
    reputation_discount=0.05,
    xp=20,
)

EMERALD_DRIPSTONE_BLOCK = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:dripstone_block', count=4),
    max_uses=16,
    reputation_discount=0.05,
    xp=10,
)

EMERALD_POLISHED_ANDESITE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:polished_andesite', count=4),
    max_uses=16,
    reputation_discount=0.05,
    xp=10,
)

EMERALD_POLISHED_DIORITE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:polished_diorite', count=4),
    max_uses=16,
    reputation_discount=0.05,
    xp=10,
)

EMERALD_POLISHED_GRANITE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:polished_granite', count=4),
    max_uses=16,
    reputation_discount=0.05,
    xp=10,
)

GRANITE_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:granite', count=16),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=16,
    reputation_discount=0.05,
    xp=20,
)
