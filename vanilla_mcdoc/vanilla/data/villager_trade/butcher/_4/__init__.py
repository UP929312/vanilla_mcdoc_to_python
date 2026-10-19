"""Vanilla's data/villager_trade/butcher/_4/ files"""
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

DRIED_KELP_BLOCK_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:dried_kelp_block', count=10),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=12,
    reputation_discount=0.05,
    xp=30,
)
