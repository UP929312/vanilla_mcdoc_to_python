"""Vanilla's data/datapacks/trade_rebalance/data/villager_trade/armorer/_5/ files"""
from vanilla_mcdoc.data.advancement.predicate.EnchantmentPredicate import EnchantmentPredicate
from vanilla_mcdoc.data.advancement.predicate.EntitySubPredicateMap import EntitySubPredicateMap
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.loot.EntityTarget import EntityTarget
from vanilla_mcdoc.data.loot.condition.LootCondition import LootConditionEntityProperties
from vanilla_mcdoc.data.loot.function.LootFunction import LootFunctionDiscard, LootFunctionFiltered, LootFunctionSetEnchantments
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

DIAMOND_BLOCK_EMERALD_TAIGA = VillagerTrade(
    wants=TradeCost(id='minecraft:diamond_block'),
    gives=ItemStackOfComponent(id='minecraft:emerald', count=42),
    max_uses=12,
    reputation_discount=0.05,
    xp=30,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:taiga'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_AND_DIAMOND_DIAMOND_BOOTS_PLAINS = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=12),
    additional_wants=TradeCost(id='minecraft:diamond', count=2),
    gives=ItemStackOfComponent(id='minecraft:diamond_boots'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:protection': 1}, type='minecraft:set_enchantments'),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:diamond_boots',
                predicates={'minecraft:enchantments': [EnchantmentPredicate(levels=1)]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=3,
    reputation_discount=0.05,
    xp=30,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:plains'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_AND_DIAMOND_DIAMOND_BOOTS_SNOW = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=12),
    additional_wants=TradeCost(id='minecraft:diamond', count=2),
    gives=ItemStackOfComponent(id='minecraft:diamond_boots'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:frost_walker': 1}, type='minecraft:set_enchantments'),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:diamond_boots',
                predicates={'minecraft:enchantments': [EnchantmentPredicate(levels=1)]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=3,
    reputation_discount=0.05,
    xp=30,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:snow'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_AND_DIAMOND_DIAMOND_CHESTPLATE_DESERT = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=16),
    additional_wants=TradeCost(id='minecraft:diamond', count=4),
    gives=ItemStackOfComponent(id='minecraft:diamond_chestplate'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:thorns': 1}, type='minecraft:set_enchantments'),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:diamond_chestplate',
                predicates={'minecraft:enchantments': [EnchantmentPredicate(levels=1)]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=3,
    reputation_discount=0.05,
    xp=30,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:desert'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_AND_DIAMOND_DIAMOND_CHESTPLATE_SAVANNA = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=8),
    additional_wants=TradeCost(id='minecraft:diamond', count=3),
    gives=ItemStackOfComponent(id='minecraft:diamond_chestplate'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:binding_curse': 1}, type='minecraft:set_enchantments'),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:diamond_chestplate',
                predicates={'minecraft:enchantments': [EnchantmentPredicate(levels=1)]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=3,
    reputation_discount=0.05,
    xp=30,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:savanna'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_AND_DIAMOND_DIAMOND_CHESTPLATE_TAIGA = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=18),
    additional_wants=TradeCost(id='minecraft:diamond', count=4),
    gives=ItemStackOfComponent(id='minecraft:diamond_chestplate'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:blast_protection': 1}, type='minecraft:set_enchantments'),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:diamond_chestplate',
                predicates={'minecraft:enchantments': [EnchantmentPredicate(levels=1)]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=3,
    reputation_discount=0.05,
    xp=30,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:taiga'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_AND_DIAMOND_DIAMOND_HELMET_SAVANNA = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=6),
    additional_wants=TradeCost(id='minecraft:diamond', count=2),
    gives=ItemStackOfComponent(id='minecraft:diamond_helmet'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:binding_curse': 1}, type='minecraft:set_enchantments'),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:diamond_helmet',
                predicates={'minecraft:enchantments': [EnchantmentPredicate(levels=1)]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=3,
    reputation_discount=0.05,
    xp=30,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:savanna'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_AND_DIAMOND_DIAMOND_HELMET_SNOW = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=12),
    additional_wants=TradeCost(id='minecraft:diamond', count=3),
    gives=ItemStackOfComponent(id='minecraft:diamond_helmet'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:aqua_affinity': 1}, type='minecraft:set_enchantments'),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:diamond_helmet',
                predicates={'minecraft:enchantments': [EnchantmentPredicate(levels=1)]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=3,
    reputation_discount=0.05,
    xp=30,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:snow'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_AND_DIAMOND_DIAMOND_LEGGINGS_DESERT = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=16),
    additional_wants=TradeCost(id='minecraft:diamond', count=3),
    gives=ItemStackOfComponent(id='minecraft:diamond_leggings'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:thorns': 1}, type='minecraft:set_enchantments'),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:diamond_leggings',
                predicates={'minecraft:enchantments': [EnchantmentPredicate(levels=1)]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=3,
    reputation_discount=0.05,
    xp=30,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:desert'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_AND_DIAMOND_DIAMOND_LEGGINGS_PLAINS = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=16),
    additional_wants=TradeCost(id='minecraft:diamond', count=3),
    gives=ItemStackOfComponent(id='minecraft:diamond_leggings'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:protection': 1}, type='minecraft:set_enchantments'),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:diamond_leggings',
                predicates={'minecraft:enchantments': [EnchantmentPredicate(levels=1)]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=3,
    reputation_discount=0.05,
    xp=30,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:plains'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_AND_DIAMOND_DIAMOND_LEGGINGS_TAIGA = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=18),
    additional_wants=TradeCost(id='minecraft:diamond', count=3),
    gives=ItemStackOfComponent(id='minecraft:diamond_leggings'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:blast_protection': 1}, type='minecraft:set_enchantments'),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:diamond_leggings',
                predicates={'minecraft:enchantments': [EnchantmentPredicate(levels=1)]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=3,
    reputation_discount=0.05,
    xp=30,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:taiga'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_CHAINMAIL_BOOTS_JUNGLE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=8),
    gives=ItemStackOfComponent(id='minecraft:chainmail_boots'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:feather_falling': 1}, type='minecraft:set_enchantments'),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:chainmail_boots',
                predicates={'minecraft:enchantments': [EnchantmentPredicate(levels=1)]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=3,
    reputation_discount=0.05,
    xp=30,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:jungle'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_CHAINMAIL_BOOTS_SWAMP = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=8),
    gives=ItemStackOfComponent(id='minecraft:chainmail_boots'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:depth_strider': 1}, type='minecraft:set_enchantments'),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:chainmail_boots',
                predicates={'minecraft:enchantments': [EnchantmentPredicate(levels=1)]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=3,
    reputation_discount=0.05,
    xp=30,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:swamp'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_CHAINMAIL_HELMET_JUNGLE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=9),
    gives=ItemStackOfComponent(id='minecraft:chainmail_helmet'),
    given_item_modifier=[
        LootFunctionSetEnchantments(
            enchantments={'minecraft:projectile_protection': 1},
            type='minecraft:set_enchantments',
        ),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:chainmail_helmet',
                predicates={'minecraft:enchantments': [EnchantmentPredicate(levels=1)]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=3,
    reputation_discount=0.05,
    xp=30,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:jungle'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_CHAINMAIL_HELMET_SWAMP = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=9),
    gives=ItemStackOfComponent(id='minecraft:chainmail_helmet'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:respiration': 1}, type='minecraft:set_enchantments'),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:chainmail_helmet',
                predicates={'minecraft:enchantments': [EnchantmentPredicate(levels=1)]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=3,
    reputation_discount=0.05,
    xp=30,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:swamp'}),
        type='minecraft:entity_properties',
    ),
)

IRON_BLOCK_EMERALD_NON_TAIGA = VillagerTrade(
    wants=TradeCost(id='minecraft:iron_block'),
    gives=ItemStackOfComponent(id='minecraft:emerald', count=4),
    max_uses=12,
    reputation_discount=0.05,
    xp=30,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(
            predicates={
                'minecraft:villager/variant': [
                    'minecraft:desert',
                    'minecraft:jungle',
                    'minecraft:plains',
                    'minecraft:savanna',
                    'minecraft:snow',
                    'minecraft:swamp',
                ],
            },
        ),
        type='minecraft:entity_properties',
    ),
)
