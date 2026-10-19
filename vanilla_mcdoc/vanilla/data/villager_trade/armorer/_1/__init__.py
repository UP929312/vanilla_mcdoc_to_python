"""Vanilla's data/villager_trade/armorer/_1/ files"""
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

EMERALD_IRON_BOOTS = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=4),
    gives=ItemStackOfComponent(id='minecraft:iron_boots'),
    max_uses=12,
    reputation_discount=0.2,
)

EMERALD_IRON_CHESTPLATE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=9),
    gives=ItemStackOfComponent(id='minecraft:iron_chestplate'),
    max_uses=12,
    reputation_discount=0.2,
)

EMERALD_IRON_HELMET = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=5),
    gives=ItemStackOfComponent(id='minecraft:iron_helmet'),
    max_uses=12,
    reputation_discount=0.2,
)

EMERALD_IRON_LEGGINGS = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=7),
    gives=ItemStackOfComponent(id='minecraft:iron_leggings'),
    max_uses=12,
    reputation_discount=0.2,
)
