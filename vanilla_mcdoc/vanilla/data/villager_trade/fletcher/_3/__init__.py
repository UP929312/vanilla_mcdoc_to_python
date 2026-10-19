"""Vanilla's data/villager_trade/fletcher/_3/ files"""
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

EMERALD_CROSSBOW = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=3),
    gives=ItemStackOfComponent(id='minecraft:crossbow'),
    max_uses=12,
    reputation_discount=0.05,
    xp=10,
)

STRING_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:string', count=14),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=16,
    reputation_discount=0.05,
    xp=20,
)
