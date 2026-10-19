"""Vanilla's data/villager_trade/farmer/_2/ files"""
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

EMERALD_APPLE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:apple', count=4),
    max_uses=16,
    reputation_discount=0.05,
    xp=5,
)

EMERALD_PUMPKIN_PIE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:pumpkin_pie', count=4),
    max_uses=12,
    reputation_discount=0.05,
    xp=5,
)

PUMPKIN_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:pumpkin', count=6),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=12,
    reputation_discount=0.05,
    xp=10,
)
