"""Vanilla's data/villager_trade/farmer/_4/ files"""
from vanilla_mcdoc.data.loot.function.LootFunction import LootFunctionSetStewEffect
from vanilla_mcdoc.data.loot.function.StewEffect import StewEffect
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

EMERALD_CAKE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=3),
    gives=ItemStackOfComponent(id='minecraft:cake'),
    max_uses=12,
    reputation_discount=0.05,
    xp=15,
)

EMERALD_SUSPICIOUS_STEW = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:suspicious_stew'),
    given_item_modifier=LootFunctionSetStewEffect(
        effects=[
            StewEffect(type='minecraft:night_vision', duration=5),
            StewEffect(type='minecraft:jump_boost', duration=8),
            StewEffect(type='minecraft:weakness', duration=7),
            StewEffect(type='minecraft:blindness', duration=6),
            StewEffect(type='minecraft:poison', duration=14),
            StewEffect(type='minecraft:saturation', duration=7),
        ],
        type='minecraft:set_stew_effect',
    ),
    max_uses=12,
    reputation_discount=0.05,
    xp=15,
)
