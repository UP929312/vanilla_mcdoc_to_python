"""Vanilla's data/villager_trade/armorer/_2/ files"""
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

EMERALD_CHAINMAIL_BOOTS = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:chainmail_boots'),
    max_uses=12,
    reputation_discount=0.2,
    xp=5,
)

EMERALD_CHAINMAIL_LEGGINGS = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=3),
    gives=ItemStackOfComponent(id='minecraft:chainmail_leggings'),
    max_uses=12,
    reputation_discount=0.2,
    xp=5,
)
