"""Vanilla's data/villager_trade/cleric/_5/ files"""
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

EMERALD_EXPERIENCE_BOTTLE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=3),
    gives=ItemStackOfComponent(id='minecraft:experience_bottle'),
    max_uses=12,
    reputation_discount=0.05,
    xp=30,
)

NETHER_WART_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:nether_wart', count=22),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=12,
    reputation_discount=0.05,
    xp=30,
)
