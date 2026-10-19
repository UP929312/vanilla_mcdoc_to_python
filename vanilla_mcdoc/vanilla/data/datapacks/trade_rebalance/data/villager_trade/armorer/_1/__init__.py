"""Vanilla's data/datapacks/trade_rebalance/data/villager_trade/armorer/_1/ files"""
from vanilla_mcdoc.data.advancement.predicate.EntitySubPredicateMap import EntitySubPredicateMap
from vanilla_mcdoc.data.loot.EntityTarget import EntityTarget
from vanilla_mcdoc.data.loot.condition.LootCondition import LootConditionEntityProperties
from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
from vanilla_mcdoc.data.villager_trade.VillagerTrade import VillagerTrade
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

IRON_INGOT_EMERALD = VillagerTrade(
    wants=TradeCost(id='minecraft:iron_ingot', count=5),
    gives=ItemStackOfComponent(id='minecraft:emerald'),
    max_uses=12,
    reputation_discount=0.05,
    xp=5,
    merchant_predicate=LootConditionEntityProperties(
        entity=EntityTarget.THIS,
        predicate=EntitySubPredicateMap(
            predicates={
                'minecraft:villager/variant': ['minecraft:desert', 'minecraft:plains', 'minecraft:savanna', 'minecraft:snow', 'minecraft:taiga'],
            },
        ),
        type='minecraft:entity_properties',
    ),
)
