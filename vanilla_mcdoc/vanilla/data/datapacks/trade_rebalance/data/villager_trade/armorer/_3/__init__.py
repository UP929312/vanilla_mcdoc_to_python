"""Vanilla's data/datapacks/trade_rebalance/data/villager_trade/armorer/_3/ files"""
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

EMERALD_BELL = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=36),
    gives=ItemStackOfComponent(id='minecraft:bell'),
    max_uses=12,
    reputation_discount=0.2,
    xp=10,
)
