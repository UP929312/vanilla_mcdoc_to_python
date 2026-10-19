"""Vanilla's data/villager_trade/cleric/_4/ files"""
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

EMERALD_ENDER_PEARL = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=5),
    gives=ItemStackOfComponent(id='minecraft:ender_pearl'),
    max_uses=12,
    reputation_discount=0.05,
    xp=15,
)

GLASS_BOTTLE_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:glass_bottle', count=9),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=12,
    reputation_discount=0.05,
    xp=30,
)

TURTLE_SCUTE_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:turtle_scute', count=4),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=12,
    reputation_discount=0.05,
    xp=30,
)
