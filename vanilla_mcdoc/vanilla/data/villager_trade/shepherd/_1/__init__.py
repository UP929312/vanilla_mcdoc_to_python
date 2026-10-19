"""Vanilla's data/villager_trade/shepherd/_1/ files"""
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

BLACK_WOOL_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:black_wool', count=18),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=16,
    reputation_discount=0.05,
    xp=2,
)

BROWN_WOOL_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:brown_wool', count=18),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=16,
    reputation_discount=0.05,
    xp=2,
)

EMERALD_SHEARS = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=2),
    gives=ItemStackOfComponent(id='minecraft:shears'),
    max_uses=12,
    reputation_discount=0.05,
)

GRAY_WOOL_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:gray_wool', count=18),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=16,
    reputation_discount=0.05,
    xp=2,
)

WHITE_WOOL_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:white_wool', count=18),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=16,
    reputation_discount=0.05,
    xp=2,
)
