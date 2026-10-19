"""Vanilla's data/villager_trade/leatherworker/_1/ files"""
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.loot.function.LootFunction import LootFunctionDiscard, LootFunctionFiltered, LootFunctionSetRandomDyes
from vanilla_mcdoc.data.number_provider.context_int.ContextIntProvider import ContextIntProviderStructAdd, ContextIntProviderStructBinomial
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

EMERALD_DYED_LEATHER_CHESTPLATE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=7),
    gives=ItemStackOfComponent(id='minecraft:leather_chestplate'),
    given_item_modifier=[
        LootFunctionSetRandomDyes(
            number_of_dyes=ContextIntProviderStructAdd(
                inputs=[1, ContextIntProviderStructBinomial(n=2, p=0.75, type='minecraft:binomial')],
                type='minecraft:add',
            ),
            type='minecraft:set_random_dyes',
        ),
        LootFunctionFiltered(
            item_filter=ItemPredicate(items='minecraft:leather_chestplate', predicates={'minecraft:dyed_color': {}}),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=12,
    reputation_discount=0.2,
)

EMERALD_DYED_LEATHER_LEGGINGS = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=3),
    gives=ItemStackOfComponent(id='minecraft:leather_leggings'),
    given_item_modifier=[
        LootFunctionSetRandomDyes(
            number_of_dyes=ContextIntProviderStructAdd(
                inputs=[1, ContextIntProviderStructBinomial(n=2, p=0.75, type='minecraft:binomial')],
                type='minecraft:add',
            ),
            type='minecraft:set_random_dyes',
        ),
        LootFunctionFiltered(
            item_filter=ItemPredicate(items='minecraft:leather_leggings', predicates={'minecraft:dyed_color': {}}),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=12,
    reputation_discount=0.2,
)

LEATHER_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:leather', count=6),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=16,
    reputation_discount=0.05,
    xp=2,
)
