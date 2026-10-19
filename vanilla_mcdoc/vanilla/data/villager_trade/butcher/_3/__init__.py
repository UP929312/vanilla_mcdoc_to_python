"""Vanilla's data/villager_trade/butcher/_3/ files"""
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

BEEF_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:beef', count=10),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=16,
    reputation_discount=0.05,
    xp=20,
)

MUTTON_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:mutton', count=7),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=16,
    reputation_discount=0.05,
    xp=20,
)
