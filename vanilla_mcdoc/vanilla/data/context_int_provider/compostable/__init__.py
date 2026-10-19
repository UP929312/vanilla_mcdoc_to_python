"""Vanilla's data/context_int_provider/compostable/ files"""
from vanilla_mcdoc.data.loot.condition.LootCondition import LootConditionMatchBlock
from vanilla_mcdoc.data.number_provider.context_int.ContextIntProvider import CasesStruct, ContextIntProviderStructNumberDispatcher, ContextIntProviderStructWeightedList
from vanilla_mcdoc.util.WeightedEntry import WeightedEntry

ALWAYS_ADD_ONE = 1

LOW = ContextIntProviderStructNumberDispatcher(
    type='minecraft:number_dispatcher',
    cases=[
        CasesStruct(
            condition=LootConditionMatchBlock(blocks='minecraft:composter', state={'level': '0'}, type='minecraft:match_block'),
            value=1,
        ),
    ],
    default=ContextIntProviderStructWeightedList(
        type='minecraft:weighted_list',
        distribution=[WeightedEntry(weight=30, data=1), WeightedEntry(weight=70, data=0)],
    ),
)

LOW_MEDIUM = ContextIntProviderStructNumberDispatcher(
    type='minecraft:number_dispatcher',
    cases=[
        CasesStruct(
            condition=LootConditionMatchBlock(blocks='minecraft:composter', state={'level': '0'}, type='minecraft:match_block'),
            value=1,
        ),
    ],
    default=ContextIntProviderStructWeightedList(
        type='minecraft:weighted_list',
        distribution=[WeightedEntry(weight=50, data=1), WeightedEntry(weight=50, data=0)],
    ),
)

MEDIUM = ContextIntProviderStructNumberDispatcher(
    type='minecraft:number_dispatcher',
    cases=[
        CasesStruct(
            condition=LootConditionMatchBlock(blocks='minecraft:composter', state={'level': '0'}, type='minecraft:match_block'),
            value=1,
        ),
    ],
    default=ContextIntProviderStructWeightedList(
        type='minecraft:weighted_list',
        distribution=[WeightedEntry(weight=65, data=1), WeightedEntry(weight=35, data=0)],
    ),
)

MEDIUM_HIGH = ContextIntProviderStructNumberDispatcher(
    type='minecraft:number_dispatcher',
    cases=[
        CasesStruct(
            condition=LootConditionMatchBlock(blocks='minecraft:composter', state={'level': '0'}, type='minecraft:match_block'),
            value=1,
        ),
    ],
    default=ContextIntProviderStructWeightedList(
        type='minecraft:weighted_list',
        distribution=[WeightedEntry(weight=85, data=1), WeightedEntry(weight=15, data=0)],
    ),
)
