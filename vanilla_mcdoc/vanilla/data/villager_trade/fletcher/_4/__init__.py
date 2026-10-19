"""Vanilla's data/villager_trade/fletcher/_4/ files"""
from vanilla_mcdoc.data.advancement.predicate.EnchantmentPredicate import EnchantmentPredicate
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.loot.function.LootFunction import LootFunctionDiscard, LootFunctionEnchantWithLevels, LootFunctionFiltered
from vanilla_mcdoc.data.number_provider.context_int.ContextIntProvider import ContextIntProviderStructUniform
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

EMERALD_ENCHANTED_BOW = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=2),
    gives=ItemStackOfComponent(id='minecraft:bow'),
    given_item_modifier=[
        LootFunctionEnchantWithLevels(
            levels=ContextIntProviderStructUniform(type='minecraft:uniform', min=5, max=19),
            options='#minecraft:on_traded_equipment',
            include_additional_cost_component=True,
            type='minecraft:enchant_with_levels',
        ),
        LootFunctionFiltered(
            item_filter=ItemPredicate(items='minecraft:bow', predicates={'minecraft:enchantments': [EnchantmentPredicate()]}),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=3,
    reputation_discount=0.05,
    xp=15,
)

FEATHER_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:feather', count=24),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=16,
    reputation_discount=0.05,
    xp=30,
)
