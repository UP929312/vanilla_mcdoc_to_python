"""Vanilla's data/villager_trade/cartographer/_1/ files"""
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

EMERALD_MAP = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=7),
    gives=ItemStackOfComponent(id='minecraft:map'),
    max_uses=12,
    reputation_discount=0.05,
)

PAPER_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:paper', count=24),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=12,
    reputation_discount=0.05,
    xp=2,
)
