"""Vanilla's data/villager_trade/farmer/_5/ files"""
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

EMERALD_GLISTENING_MELON_SLICE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=4),
    gives=ItemStackOfComponent(id='minecraft:glistering_melon_slice', count=3),
    max_uses=12,
    reputation_discount=0.05,
    xp=30,
)

EMERALD_GOLDEN_CARROT = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=3),
    gives=ItemStackOfComponent(id='minecraft:golden_carrot', count=3),
    max_uses=12,
    reputation_discount=0.05,
    xp=30,
)
