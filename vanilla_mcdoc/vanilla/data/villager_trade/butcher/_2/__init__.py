"""Vanilla's data/villager_trade/butcher/_2/ files"""
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

COAL_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:coal', count=15),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=16,
    reputation_discount=0.05,
    xp=2,
)

EMERALD_COOKED_CHICKEN = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:cooked_chicken', count=8),
    max_uses=16,
    reputation_discount=0.05,
    xp=5,
)

EMERALD_COOKED_PORKCHOP = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:cooked_porkchop', count=5),
    max_uses=16,
    reputation_discount=0.05,
    xp=5,
)
