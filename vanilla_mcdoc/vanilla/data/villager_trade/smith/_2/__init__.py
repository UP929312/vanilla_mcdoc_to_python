"""Vanilla's data/villager_trade/smith/_2/ files"""
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

EMERALD_BELL = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=36),
    gives=ItemStackOfComponent(id='minecraft:bell'),
    max_uses=12,
    reputation_discount=0.2,
    xp=5,
)

IRON_INGOT_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:iron_ingot', count=4),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=12,
    reputation_discount=0.05,
    xp=10,
)
