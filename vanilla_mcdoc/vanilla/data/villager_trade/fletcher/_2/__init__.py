"""Vanilla's data/villager_trade/fletcher/_2/ files"""
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

EMERALD_BOW = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=2),
    gives=ItemStackOfComponent(id='minecraft:bow'),
    max_uses=12,
    reputation_discount=0.05,
    xp=5,
)

FLINT_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:flint', count=26),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=12,
    reputation_discount=0.05,
    xp=10,
)
