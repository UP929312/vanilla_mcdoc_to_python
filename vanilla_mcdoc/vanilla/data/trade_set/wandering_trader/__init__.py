"""Vanilla's data/trade_set/wandering_trader/ files"""
from vanilla_mcdoc.data.trade_set.TradeSet import TradeSet

BUYING = TradeSet(
    trades='#minecraft:wandering_trader/buying',
    amount=2,
    random_sequence='minecraft:trade_set/wandering_trader/buying',
)

COMMON = TradeSet(
    trades='#minecraft:wandering_trader/common',
    amount=5,
    random_sequence='minecraft:trade_set/wandering_trader/common',
)

UNCOMMON = TradeSet(
    trades='#minecraft:wandering_trader/uncommon',
    amount=2,
    random_sequence='minecraft:trade_set/wandering_trader/uncommon',
)
