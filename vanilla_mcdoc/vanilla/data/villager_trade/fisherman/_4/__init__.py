"""Vanilla's data/villager_trade/fisherman/_4/ files"""
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

TROPICAL_FISH_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:tropical_fish', count=6),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=12,
    reputation_discount=0.05,
    xp=30,
)
