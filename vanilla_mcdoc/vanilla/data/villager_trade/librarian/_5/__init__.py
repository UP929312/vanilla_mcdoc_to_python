"""Vanilla's data/villager_trade/librarian/_5/ files"""
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

EMERALD_RED_CANDLE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=3),
    gives=ItemStackOfComponent(id='minecraft:red_candle'),
    max_uses=12,
    reputation_discount=0.05,
    xp=30,
)

EMERALD_YELLOW_CANDLE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=3),
    gives=ItemStackOfComponent(id='minecraft:yellow_candle'),
    max_uses=12,
    reputation_discount=0.05,
    xp=30,
)
