"""Vanilla's data/villager_trade/mason/_1/ files"""
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

CLAY_BALL_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:clay_ball', count=10),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=16,
    reputation_discount=0.05,
    xp=2,
)

EMERALD_BRICK = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:brick', count=10),
    max_uses=16,
    reputation_discount=0.05,
)
