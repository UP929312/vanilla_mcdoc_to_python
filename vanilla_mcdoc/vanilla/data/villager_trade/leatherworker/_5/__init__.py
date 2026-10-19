"""Vanilla's data/villager_trade/leatherworker/_5/ files"""
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.loot.function.LootFunction import LootFunctionDiscard, LootFunctionFiltered, LootFunctionSetRandomDyes
from vanilla_mcdoc.data.number_provider.context_int.ContextIntProvider import ContextIntProviderStructAdd, ContextIntProviderStructBinomial
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

EMERALD_DYED_LEATHER_HELMET = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=5),
    gives=ItemStackOfComponent(id='minecraft:leather_helmet'),
    given_item_modifier=[
        LootFunctionSetRandomDyes(
            number_of_dyes=ContextIntProviderStructAdd(
                inputs=[1, ContextIntProviderStructBinomial(n=2, p=0.75, type='minecraft:binomial')],
                type='minecraft:add',
            ),
            type='minecraft:set_random_dyes',
        ),
        LootFunctionFiltered(
            item_filter=ItemPredicate(items='minecraft:leather_helmet', predicates={'minecraft:dyed_color': {}}),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=12,
    reputation_discount=0.2,
    xp=5,
)

EMERALD_SADDLE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=6),
    gives=ItemStackOfComponent(id='minecraft:saddle'),
    max_uses=12,
    reputation_discount=0.2,
    xp=30,
)
