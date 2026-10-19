"""Vanilla's data/villager_trade/mason/_5/ files"""
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

EMERALD_QUARTZ_BLOCK = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:quartz_block'),
    max_uses=12,
    reputation_discount=0.05,
    xp=30,
)

EMERALD_QUARTZ_PILLAR = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:quartz_pillar'),
    max_uses=12,
    reputation_discount=0.05,
    xp=30,
)
