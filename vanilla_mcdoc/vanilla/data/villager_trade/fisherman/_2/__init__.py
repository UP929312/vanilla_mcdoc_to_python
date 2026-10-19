"""Vanilla's data/villager_trade/fisherman/_2/ files"""
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

COD_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:cod', count=15),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=16,
    reputation_discount=0.05,
    xp=10,
)

EMERALD_CAMPFIRE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=2),
    gives=ItemStackOfComponent(id='minecraft:campfire'),
    max_uses=12,
    reputation_discount=0.05,
    xp=5,
)

SALMON_AND_EMERALD_COOKED_SALMON = VillagerTrade(
    wants=TradeCost(id='minecraft:salmon', count=6),
    additional_wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:cooked_salmon', count=6),
    max_uses=16,
    reputation_discount=0.05,
    xp=5,
)
