"""Vanilla's data/villager_trade/farmer/_3/ files"""
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

EMERALD_COOKIE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=3),
    gives=ItemStackOfComponent(id='minecraft:cookie', count=18),
    max_uses=12,
    reputation_discount=0.05,
    xp=10,
)

MELON_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:melon', count=4),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=12,
    reputation_discount=0.05,
    xp=20,
)
