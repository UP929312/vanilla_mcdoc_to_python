"""Vanilla's data/villager_trade/fletcher/_1/ files"""
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

EMERALD_ARROW = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:arrow', count=16),
    max_uses=12,
    reputation_discount=0.05,
)

GRAVEL_AND_EMERALD_FLINT = VillagerTrade(
    wants=TradeCost(id='minecraft:gravel', count=10),
    additional_wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:flint', count=10),
    max_uses=12,
    reputation_discount=0.05,
)

STICK_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:stick', count=32),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=16,
    reputation_discount=0.05,
    xp=2,
)
