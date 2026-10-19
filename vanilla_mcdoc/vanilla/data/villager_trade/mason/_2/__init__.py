"""Vanilla's data/villager_trade/mason/_2/ files"""
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

EMERALD_CHISELED_STONE_BRICKS = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:chiseled_stone_bricks', count=4),
    max_uses=16,
    reputation_discount=0.05,
    xp=5,
)

STONE_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:stone', count=20),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=16,
    reputation_discount=0.05,
    xp=10,
)
