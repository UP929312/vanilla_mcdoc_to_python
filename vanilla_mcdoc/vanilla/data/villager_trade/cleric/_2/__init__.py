"""Vanilla's data/villager_trade/cleric/_2/ files"""
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

EMERALD_LAPIS_LAZULI = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:lapis_lazuli'),
    max_uses=12,
    reputation_discount=0.05,
    xp=5,
)

GOLD_INGOT_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:gold_ingot', count=3),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=12,
    reputation_discount=0.05,
    xp=10,
)
