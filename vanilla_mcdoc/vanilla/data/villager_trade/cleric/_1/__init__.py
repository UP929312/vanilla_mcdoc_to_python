"""Vanilla's data/villager_trade/cleric/_1/ files"""
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

EMERALD_REDSTONE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:redstone', count=2),
    max_uses=12,
    reputation_discount=0.05,
)

ROTTEN_FLESH_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:rotten_flesh', count=32),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=16,
    reputation_discount=0.05,
    xp=2,
)
