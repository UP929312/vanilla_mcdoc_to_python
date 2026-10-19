"""Vanilla's data/villager_trade/cleric/_3/ files"""
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

EMERALD_GLOWSTONE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=4),
    gives=ItemStackOfComponent(id='minecraft:glowstone'),
    max_uses=12,
    reputation_discount=0.05,
    xp=10,
)

RABBIT_FOOT_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:rabbit_foot', count=2),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=12,
    reputation_discount=0.05,
    xp=20,
)
