"""Vanilla's data/villager_trade/farmer/_1/ files"""
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

BEETROOT_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:beetroot', count=15),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=16,
    reputation_discount=0.05,
    xp=2,
)

CARROT_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:carrot', count=22),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=16,
    reputation_discount=0.05,
    xp=2,
)

EMERALD_BREAD = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:bread', count=6),
    max_uses=16,
    reputation_discount=0.05,
)

POTATO_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:potato', count=26),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=16,
    reputation_discount=0.05,
    xp=2,
)

WHEAT_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:wheat', count=20),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=16,
    reputation_discount=0.05,
    xp=2,
)
