"""Vanilla's data/villager_trade/fletcher/_5/ files"""
from vanilla_mcdoc.data.advancement.predicate.EnchantmentPredicate import EnchantmentPredicate
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.loot.function.LootFunction import LootFunctionDiscard, LootFunctionEnchantWithLevels, LootFunctionFiltered, LootFunctionSetRandomPotion
from vanilla_mcdoc.data.number_provider.context_int.ContextIntProvider import ContextIntProviderStructUniform
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

ARROW_AND_EMERALD_TIPPED_ARROW = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=2),
    additional_wants=TradeCost(id='minecraft:arrow', count=5),
    gives=ItemStackOfComponent(id='minecraft:tipped_arrow', count=5),
    given_item_modifier=LootFunctionSetRandomPotion(options='#minecraft:tradeable', type='minecraft:set_random_potion'),
    max_uses=12,
    reputation_discount=0.05,
    xp=30,
)

EMERALD_ENCHANTED_CROSSBOW = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=3),
    gives=ItemStackOfComponent(id='minecraft:crossbow'),
    given_item_modifier=[
        LootFunctionEnchantWithLevels(
            levels=ContextIntProviderStructUniform(type='minecraft:uniform', min=5, max=19),
            options='#minecraft:on_traded_equipment',
            include_additional_cost_component=True,
            type='minecraft:enchant_with_levels',
        ),
        LootFunctionFiltered(
            item_filter=ItemPredicate(items='minecraft:crossbow', predicates={'minecraft:enchantments': [EnchantmentPredicate()]}),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=3,
    reputation_discount=0.05,
    xp=15,
)

TRIPWIRE_HOOK_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:tripwire_hook', count=8),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=12,
    reputation_discount=0.05,
    xp=30,
)
