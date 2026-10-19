"""Vanilla's data/villager_trade/librarian/_1/ files"""
from vanilla_mcdoc.data.advancement.predicate.EnchantmentPredicate import EnchantmentPredicate
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.loot.function.LootFunction import LootFunctionDiscard, LootFunctionEnchantRandomly, LootFunctionFiltered
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

EMERALD_AND_BOOK_ENCHANTED_BOOK = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=0),
    additional_wants=TradeCost(id='minecraft:book'),
    gives=ItemStackOfComponent(id='minecraft:enchanted_book'),
    given_item_modifier=[
        LootFunctionEnchantRandomly(
            options='#minecraft:tradeable',
            only_compatible=False,
            include_additional_cost_component=True,
            type='minecraft:enchant_randomly',
        ),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:enchanted_book',
                predicates={'minecraft:stored_enchantments': [EnchantmentPredicate()]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=12,
    reputation_discount=0.2,
    double_trade_price_enchantments='#minecraft:double_trade_price',
)

EMERALD_BOOKSHELF = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=9),
    gives=ItemStackOfComponent(id='minecraft:bookshelf'),
    max_uses=12,
    reputation_discount=0.05,
)

PAPER_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:paper', count=24),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=16,
    reputation_discount=0.05,
    xp=2,
)
