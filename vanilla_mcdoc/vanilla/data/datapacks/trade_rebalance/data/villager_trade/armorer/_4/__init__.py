"""Vanilla's data/datapacks/trade_rebalance/data/villager_trade/armorer/_4/ files"""
from vanilla_mcdoc.data.advancement.predicate.EnchantmentPredicate import EnchantmentPredicate
from vanilla_mcdoc.data.advancement.predicate.EntitySubPredicateMap import EntitySubPredicateMap
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.loot.EntityTarget import EntityTarget
from vanilla_mcdoc.data.loot.condition.LootCondition import LootConditionEntityProperties
from vanilla_mcdoc.data.loot.function.LootFunction import LootFunctionDiscard, LootFunctionFiltered, LootFunctionSetEnchantments
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

EMERALD_AND_DIAMOND_BOOTS_DIAMOND_LEGGINGS_TAIGA = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=4),
    additional_wants=TradeCost(id='minecraft:diamond_boots'),
    gives=ItemStackOfComponent(id='minecraft:diamond_leggings'),
    max_uses=3,
    reputation_discount=0.05,
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:taiga'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_AND_DIAMOND_CHESTPLATE_DIAMOND_HELMET_TAIGA = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=2),
    additional_wants=TradeCost(id='minecraft:diamond_chestplate'),
    gives=ItemStackOfComponent(id='minecraft:diamond_helmet'),
    max_uses=3,
    reputation_discount=0.05,
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:taiga'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_AND_DIAMOND_HELMET_DIAMOND_BOOTS_TAIGA = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=4),
    additional_wants=TradeCost(id='minecraft:diamond_helmet'),
    gives=ItemStackOfComponent(id='minecraft:diamond_boots'),
    max_uses=3,
    reputation_discount=0.05,
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:taiga'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_AND_DIAMOND_LEGGINGS_DIAMOND_CHESTPLATE_TAIGA = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=4),
    additional_wants=TradeCost(id='minecraft:diamond_leggings'),
    gives=ItemStackOfComponent(id='minecraft:diamond_chestplate'),
    max_uses=3,
    reputation_discount=0.05,
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:taiga'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_ENCHANTED_CHAINMAIL_BOOTS_JUNGLE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=8),
    gives=ItemStackOfComponent(id='minecraft:chainmail_boots'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:unbreaking': 1}, type='minecraft:set_enchantments'),
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
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:jungle'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_ENCHANTED_CHAINMAIL_BOOTS_SWAMP = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=8),
    gives=ItemStackOfComponent(id='minecraft:chainmail_boots'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:mending': 1}, type='minecraft:set_enchantments'),
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
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:swamp'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_ENCHANTED_CHAINMAIL_CHESTPLATE_JUNGLE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=13),
    gives=ItemStackOfComponent(id='minecraft:chainmail_chestplate'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:unbreaking': 1}, type='minecraft:set_enchantments'),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:chainmail_chestplate',
                predicates={'minecraft:enchantments': [EnchantmentPredicate(levels=1)]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=3,
    reputation_discount=0.05,
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:jungle'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_ENCHANTED_CHAINMAIL_CHESTPLATE_SWAMP = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=13),
    gives=ItemStackOfComponent(id='minecraft:chainmail_chestplate'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:mending': 1}, type='minecraft:set_enchantments'),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:chainmail_chestplate',
                predicates={'minecraft:enchantments': [EnchantmentPredicate(levels=1)]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=3,
    reputation_discount=0.05,
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:swamp'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_ENCHANTED_CHAINMAIL_HELMET_JUNGLE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=9),
    gives=ItemStackOfComponent(id='minecraft:chainmail_helmet'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:unbreaking': 1}, type='minecraft:set_enchantments'),
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
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:jungle'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_ENCHANTED_CHAINMAIL_HELMET_SWAMP = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=9),
    gives=ItemStackOfComponent(id='minecraft:chainmail_helmet'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:mending': 1}, type='minecraft:set_enchantments'),
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
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:swamp'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_ENCHANTED_CHAINMAIL_LEGGINGS_JUNGLE = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=11),
    gives=ItemStackOfComponent(id='minecraft:chainmail_leggings'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:unbreaking': 1}, type='minecraft:set_enchantments'),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:chainmail_leggings',
                predicates={'minecraft:enchantments': [EnchantmentPredicate(levels=1)]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=3,
    reputation_discount=0.05,
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:jungle'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_ENCHANTED_CHAINMAIL_LEGGINGS_SWAMP = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=11),
    gives=ItemStackOfComponent(id='minecraft:chainmail_leggings'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:mending': 1}, type='minecraft:set_enchantments'),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:chainmail_leggings',
                predicates={'minecraft:enchantments': [EnchantmentPredicate(levels=1)]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=3,
    reputation_discount=0.05,
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:swamp'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_ENCHANTED_IRON_BOOTS_DESERT = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=8),
    gives=ItemStackOfComponent(id='minecraft:iron_boots'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:thorns': 1}, type='minecraft:set_enchantments'),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:iron_boots',
                predicates={'minecraft:enchantments': [EnchantmentPredicate(levels=1)]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=3,
    reputation_discount=0.05,
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:desert'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_ENCHANTED_IRON_BOOTS_PLAINS = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=8),
    gives=ItemStackOfComponent(id='minecraft:iron_boots'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:protection': 1}, type='minecraft:set_enchantments'),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:iron_boots',
                predicates={'minecraft:enchantments': [EnchantmentPredicate(levels=1)]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=3,
    reputation_discount=0.05,
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:plains'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_ENCHANTED_IRON_BOOTS_SAVANNA = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=2),
    gives=ItemStackOfComponent(id='minecraft:iron_boots'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:binding_curse': 1}, type='minecraft:set_enchantments'),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:iron_boots',
                predicates={'minecraft:enchantments': [EnchantmentPredicate(levels=1)]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=3,
    reputation_discount=0.05,
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:savanna'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_ENCHANTED_IRON_BOOTS_SNOW = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=8),
    gives=ItemStackOfComponent(id='minecraft:iron_boots'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:frost_walker': 1}, type='minecraft:set_enchantments'),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:iron_boots',
                predicates={'minecraft:enchantments': [EnchantmentPredicate(levels=1)]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=3,
    reputation_discount=0.05,
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:snow'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_ENCHANTED_IRON_CHESTPLATE_DESERT = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=13),
    gives=ItemStackOfComponent(id='minecraft:iron_chestplate'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:thorns': 1}, type='minecraft:set_enchantments'),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:iron_chestplate',
                predicates={'minecraft:enchantments': [EnchantmentPredicate(levels=1)]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=3,
    reputation_discount=0.05,
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:desert'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_ENCHANTED_IRON_CHESTPLATE_PLAINS = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=13),
    gives=ItemStackOfComponent(id='minecraft:iron_chestplate'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:protection': 1}, type='minecraft:set_enchantments'),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:iron_chestplate',
                predicates={'minecraft:enchantments': [EnchantmentPredicate(levels=1)]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=3,
    reputation_discount=0.05,
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:plains'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_ENCHANTED_IRON_CHESTPLATE_SAVANNA = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=7),
    gives=ItemStackOfComponent(id='minecraft:iron_chestplate'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:binding_curse': 1}, type='minecraft:set_enchantments'),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:iron_chestplate',
                predicates={'minecraft:enchantments': [EnchantmentPredicate(levels=1)]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=3,
    reputation_discount=0.05,
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:savanna'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_ENCHANTED_IRON_HELMET_DESERT = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=9),
    gives=ItemStackOfComponent(id='minecraft:iron_helmet'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:thorns': 1}, type='minecraft:set_enchantments'),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:iron_helmet',
                predicates={'minecraft:enchantments': [EnchantmentPredicate(levels=1)]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=3,
    reputation_discount=0.05,
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:desert'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_ENCHANTED_IRON_HELMET_PLAINS = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=9),
    gives=ItemStackOfComponent(id='minecraft:iron_helmet'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:protection': 1}, type='minecraft:set_enchantments'),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:iron_helmet',
                predicates={'minecraft:enchantments': [EnchantmentPredicate(levels=1)]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=3,
    reputation_discount=0.05,
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:plains'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_ENCHANTED_IRON_HELMET_SAVANNA = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=3),
    gives=ItemStackOfComponent(id='minecraft:iron_helmet'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:binding_curse': 1}, type='minecraft:set_enchantments'),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:iron_helmet',
                predicates={'minecraft:enchantments': [EnchantmentPredicate(levels=1)]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=3,
    reputation_discount=0.05,
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:savanna'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_ENCHANTED_IRON_HELMET_SNOW = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=9),
    gives=ItemStackOfComponent(id='minecraft:iron_helmet'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:aqua_affinity': 1}, type='minecraft:set_enchantments'),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:iron_helmet',
                predicates={'minecraft:enchantments': [EnchantmentPredicate(levels=1)]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=3,
    reputation_discount=0.05,
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:snow'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_ENCHANTED_IRON_LEGGINGS_DESERT = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=11),
    gives=ItemStackOfComponent(id='minecraft:iron_leggings'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:thorns': 1}, type='minecraft:set_enchantments'),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:iron_leggings',
                predicates={'minecraft:enchantments': [EnchantmentPredicate(levels=1)]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=3,
    reputation_discount=0.05,
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:desert'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_ENCHANTED_IRON_LEGGINGS_PLAINS = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=11),
    gives=ItemStackOfComponent(id='minecraft:iron_leggings'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:protection': 1}, type='minecraft:set_enchantments'),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:iron_leggings',
                predicates={'minecraft:enchantments': [EnchantmentPredicate(levels=1)]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=3,
    reputation_discount=0.05,
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:plains'}),
        type='minecraft:entity_properties',
    ),
)

EMERALD_ENCHANTED_IRON_LEGGINGS_SAVANNA = VillagerTrade(
    wants=TradeCost(id='minecraft:emerald', count=5),
    gives=ItemStackOfComponent(id='minecraft:iron_leggings'),
    given_item_modifier=[
        LootFunctionSetEnchantments(enchantments={'minecraft:binding_curse': 1}, type='minecraft:set_enchantments'),
        LootFunctionFiltered(
            item_filter=ItemPredicate(
                items='minecraft:iron_leggings',
                predicates={'minecraft:enchantments': [EnchantmentPredicate(levels=1)]},
            ),
            on_fail=LootFunctionDiscard(type='minecraft:discard'),
            type='minecraft:filtered',
        ),
    ],
    max_uses=3,
    reputation_discount=0.05,
    xp=15,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(predicates={'minecraft:villager/variant': 'minecraft:savanna'}),
        type='minecraft:entity_properties',
    ),
)
