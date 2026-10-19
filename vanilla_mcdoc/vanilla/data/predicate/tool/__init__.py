"""Vanilla's data/predicate/tool/ files"""
from vanilla_mcdoc.data.advancement.predicate.EnchantmentPredicate import EnchantmentPredicate
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.loot.condition.LootCondition import LootConditionMatchTool
from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds

CAN_SHEAR = LootConditionMatchTool(predicate=ItemPredicate(items='minecraft:shears'), type='minecraft:match_tool')

CAN_SILK_TOUCH = LootConditionMatchTool(
    predicate=ItemPredicate(
        predicates={
            'minecraft:enchantments': [EnchantmentPredicate(enchantments='minecraft:silk_touch', levels=MinMaxBounds(min=1))],
        },
    ),
    type='minecraft:match_tool',
)
