"""Vanilla's data/villager_trade/toolsmith/_3/ files"""
from vanilla_mcdoc.data.advancement.predicate.EnchantmentPredicate import EnchantmentPredicate
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.loot.function.LootFunction import LootFunctionDiscard, LootFunctionEnchantWithLevels, LootFunctionFiltered
from vanilla_mcdoc.data.number_provider.context_int.ContextIntProvider import ContextIntProviderStructUniform
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

EMERALD_DIAMOND_HOE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=4),
    gives=ItemStackOfComponent(id='minecraft:diamond_hoe'),
    max_uses=3,
    reputation_discount=0.2,
    xp=10,
)

EMERALD_ENCHANTED_IRON_AXE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald'),
    gives=ItemStackOfComponent(id='minecraft:iron_axe'),
    given_item_modifier=[
        LootFunctionEnchantWithLevels(
            levels=ContextIntProviderStructUniform(type='minecraft:uniform', min=5, max=19),
            options='#minecraft:on_traded_equipment',
            include_additional_cost_component=True,
            type='minecraft:enchant_with_levels',
        ),
        LootFunctionFiltered(
            item_filter=ItemPredicate(items='minecraft:iron_axe', predicates={'minecraft:enchantments': [EnchantmentPredicate()]}),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=3,
    reputation_discount=0.2,
    xp=10,
)

EMERALD_ENCHANTED_IRON_PICKAXE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=3),
    gives=ItemStackOfComponent(id='minecraft:iron_pickaxe'),
    given_item_modifier=[
        LootFunctionEnchantWithLevels(
            levels=ContextIntProviderStructUniform(type='minecraft:uniform', min=5, max=19),
            options='#minecraft:on_traded_equipment',
            include_additional_cost_component=True,
            type='minecraft:enchant_with_levels',
        ),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:iron_pickaxe',
                predicates={'minecraft:enchantments': [EnchantmentPredicate()]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=3,
    reputation_discount=0.2,
    xp=10,
)

EMERALD_ENCHANTED_IRON_SHOVEL = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=2),
    gives=ItemStackOfComponent(id='minecraft:iron_shovel'),
    given_item_modifier=[
        LootFunctionEnchantWithLevels(
            levels=ContextIntProviderStructUniform(type='minecraft:uniform', min=5, max=19),
            options='#minecraft:on_traded_equipment',
            include_additional_cost_component=True,
            type='minecraft:enchant_with_levels',
        ),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:iron_shovel',
                predicates={'minecraft:enchantments': [EnchantmentPredicate()]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=3,
    reputation_discount=0.2,
    xp=10,
)

FLINT_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:flint', count=30),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=12,
    reputation_discount=0.05,
    xp=20,
)
