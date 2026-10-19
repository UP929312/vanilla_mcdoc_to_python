"""Vanilla's data/villager_trade/toolsmith/_1/ files"""
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

EMERALD_STONE_AXE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:stone_axe'),
    max_uses=12,
    reputation_discount=0.2,
)

EMERALD_STONE_HOE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:stone_hoe'),
    max_uses=12,
    reputation_discount=0.2,
)

EMERALD_STONE_PICKAXE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:stone_pickaxe'),
    max_uses=12,
    reputation_discount=0.2,
)

EMERALD_STONE_SHOVEL = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:stone_shovel'),
    max_uses=12,
    reputation_discount=0.2,
)
