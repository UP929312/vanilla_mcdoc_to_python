"""Vanilla's data/villager_trade/fisherman/_1/ files"""
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

COAL_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:coal', count=10),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=16,
    reputation_discount=0.05,
    xp=2,
)

EMERALD_COD_BUCKET = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=3),
    gives=ItemStackOfComponent(id='minecraft:cod_bucket'),
    max_uses=16,
    reputation_discount=0.05,
)

RAW_COD_AND_EMERALD_COOKED_COD = VillagerTrade(
    wants=TradeCost(id='minecraft:cod', count=6),
    additional_wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:cooked_cod', count=6),
    max_uses=16,
    reputation_discount=0.05,
)

STRING_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:string', count=20),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=16,
    reputation_discount=0.05,
    xp=2,
)
