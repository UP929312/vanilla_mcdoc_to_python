"""Vanilla's data/villager_trade/butcher/_1/ files"""
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

CHICKEN_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:chicken', count=14),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=16,
    reputation_discount=0.05,
    xp=2,
)

EMERALD_RABBIT_STEW = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:rabbit_stew'),
    max_uses=12,
    reputation_discount=0.05,
)

PORKCHOP_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:porkchop', count=7),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=16,
    reputation_discount=0.05,
    xp=2,
)

RABBIT_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:rabbit', count=4),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=16,
    reputation_discount=0.05,
    xp=2,
)
