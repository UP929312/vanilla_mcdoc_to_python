"""Vanilla's data/villager_trade/armorer/_3/ files"""
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

DIAMOND_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:diamond'),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=12,
    reputation_discount=0.05,
    xp=20,
)

EMERALD_CHAINMAIL_CHESTPLATE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=4),
    gives=ItemStackOfComponent(id='minecraft:chainmail_chestplate'),
    max_uses=12,
    reputation_discount=0.2,
    xp=10,
)

EMERALD_CHAINMAIL_HELMET = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:chainmail_helmet'),
    max_uses=12,
    reputation_discount=0.2,
    xp=10,
)

EMERALD_SHIELD = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=5),
    gives=ItemStackOfComponent(id='minecraft:shield'),
    max_uses=12,
    reputation_discount=0.2,
    xp=10,
)

LAVA_BUCKET_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:lava_bucket'),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=12,
    reputation_discount=0.05,
    xp=20,
)
