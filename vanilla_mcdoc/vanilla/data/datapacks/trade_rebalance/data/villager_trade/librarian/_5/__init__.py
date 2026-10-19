"""Vanilla's data/datapacks/trade_rebalance/data/villager_trade/librarian/_5/ files"""
from vanilla_mcdoc.data.advancement.predicate.EnchantmentPredicate import EnchantmentPredicate
from vanilla_mcdoc.data.advancement.predicate.EntitySubPredicateMap import EntitySubPredicateMap
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.loot.EntityTarget import EntityTarget
from vanilla_mcdoc.data.loot.condition.LootCondition import LootConditionEntityProperties
from vanilla_mcdoc.data.loot.function.LootFunction import LootFunctionDiscard, LootFunctionEnchantRandomly, LootFunctionFiltered, LootFunctionSetEnchantments
from vanilla_mcdoc.data.number_provider.context_int.ContextIntProvider import ContextIntProviderStructAdd, ContextIntProviderStructUniform
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

EMERALD_AND_BOOK_DESERT_ENCHANTED_BOOK = VillagerTrade(
    wants=TradeCost(
        id='minecraft:emerald',
        count=ContextIntProviderStructAdd(
            inputs=[11, ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=35)],
            type='minecraft:add',
        ),
    ),
    additional_wants=TradeCost(id='minecraft:book'),
    gives=ItemStackOfComponent(id='minecraft:enchanted_book'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:efficiency': 3}, type='minecraft:set_enchantments'),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:enchanted_book',
                predicates={'minecraft:stored_enchantments': [EnchantmentPredicate(levels=3)]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=12,
    reputation_discount=0.2,
    xp=30,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:desert'}),
        type='minecraft:entity_properties',
    ),
    double_trade_price_enchantments='#minecraft:double_trade_price',
)

EMERALD_AND_BOOK_JUNGLE_ENCHANTED_BOOK = VillagerTrade(
    wants=TradeCost(
        id='minecraft:emerald',
        count=ContextIntProviderStructAdd(
            inputs=[8, ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=25)],
            type='minecraft:add',
        ),
    ),
    additional_wants=TradeCost(id='minecraft:book'),
    gives=ItemStackOfComponent(id='minecraft:enchanted_book'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:unbreaking': 2}, type='minecraft:set_enchantments'),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:enchanted_book',
                predicates={'minecraft:stored_enchantments': [EnchantmentPredicate(levels=2)]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=12,
    reputation_discount=0.2,
    xp=30,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:jungle'}),
        type='minecraft:entity_properties',
    ),
    double_trade_price_enchantments='#minecraft:double_trade_price',
)

EMERALD_AND_BOOK_PLAINS_ENCHANTED_BOOK = VillagerTrade(
    wants=TradeCost(
        id='minecraft:emerald',
        count=ContextIntProviderStructAdd(
            inputs=[11, ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=35)],
            type='minecraft:add',
        ),
    ),
    additional_wants=TradeCost(id='minecraft:book'),
    gives=ItemStackOfComponent(id='minecraft:enchanted_book'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:protection': 3}, type='minecraft:set_enchantments'),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:enchanted_book',
                predicates={'minecraft:stored_enchantments': [EnchantmentPredicate(levels=3)]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=12,
    reputation_discount=0.2,
    xp=30,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:plains'}),
        type='minecraft:entity_properties',
    ),
    double_trade_price_enchantments='#minecraft:double_trade_price',
)

EMERALD_AND_BOOK_SAVANNA_ENCHANTED_BOOK = VillagerTrade(
    wants=TradeCost(
        id='minecraft:emerald',
        count=ContextIntProviderStructAdd(
            inputs=[11, ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=35)],
            type='minecraft:add',
        ),
    ),
    additional_wants=TradeCost(id='minecraft:book'),
    gives=ItemStackOfComponent(id='minecraft:enchanted_book'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:sharpness': 3}, type='minecraft:set_enchantments'),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:enchanted_book',
                predicates={'minecraft:stored_enchantments': [EnchantmentPredicate(levels=3)]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=12,
    reputation_discount=0.2,
    xp=30,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:savanna'}),
        type='minecraft:entity_properties',
    ),
    double_trade_price_enchantments='#minecraft:double_trade_price',
)

EMERALD_AND_BOOK_SNOW_ENCHANTED_BOOK = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=0),
    additional_wants=TradeCost(id='minecraft:book'),
    gives=ItemStackOfComponent(id='minecraft:enchanted_book'),
    given_item_modifier=[
        LootFunctionEnchantRandomly(
            options='minecraft:silk_touch',
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
    xp=30,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:snow'}),
        type='minecraft:entity_properties',
    ),
    double_trade_price_enchantments='#minecraft:double_trade_price',
)

EMERALD_AND_BOOK_SWAMP_ENCHANTED_BOOK = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=0),
    additional_wants=TradeCost(id='minecraft:book'),
    gives=ItemStackOfComponent(id='minecraft:enchanted_book'),
    given_item_modifier=[
        LootFunctionEnchantRandomly(
            options='minecraft:mending',
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
    xp=30,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:swamp'}),
        type='minecraft:entity_properties',
    ),
    double_trade_price_enchantments='#minecraft:double_trade_price',
)

EMERALD_AND_BOOK_TAIGA_ENCHANTED_BOOK = VillagerTrade(
    wants=TradeCost(
        id='minecraft:emerald',
        count=ContextIntProviderStructAdd(
            inputs=[8, ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=25)],
            type='minecraft:add',
        ),
    ),
    additional_wants=TradeCost(id='minecraft:book'),
    gives=ItemStackOfComponent(id='minecraft:enchanted_book'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:fortune': 2}, type='minecraft:set_enchantments'),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:enchanted_book',
                predicates={'minecraft:stored_enchantments': [EnchantmentPredicate(levels=2)]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=12,
    reputation_discount=0.2,
    xp=30,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:taiga'}),
        type='minecraft:entity_properties',
    ),
    double_trade_price_enchantments='#minecraft:double_trade_price',
)
