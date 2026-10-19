"""Vanilla's data/predicate/block/ files"""
from vanilla_mcdoc.data.loot.condition.LootCondition import LootConditionMatchBlock

FAST_COOKING = LootConditionMatchBlock(blocks=['minecraft:smoker', 'minecraft:blast_furnace'], type='minecraft:match_block')
