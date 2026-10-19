"""Vanilla's data/context_int_provider/cooking/ files"""
from vanilla_mcdoc.data.number_provider.context_int.ContextIntProvider import ContextIntProviderStructConditional, ContextIntProviderStructDiv

FAST_BURN_TIME_REDUCTION_FACTOR = 2

NORMAL_BURN_TIME_REDUCTION_FACTOR = 1

TIME_BAMBOO = ContextIntProviderStructDiv(
    left=50,
    right=ContextIntProviderStructConditional(
        type='minecraft:conditional',
        condition='minecraft:block/fast_cooking',
        on_true='minecraft:cooking/fast_burn_time_reduction_factor',
        on_false='minecraft:cooking/normal_burn_time_reduction_factor',
    ),
    type='minecraft:div',
)

TIME_BLAZE_ROD = ContextIntProviderStructDiv(
    left=2400,
    right=ContextIntProviderStructConditional(
        type='minecraft:conditional',
        condition='minecraft:block/fast_cooking',
        on_true='minecraft:cooking/fast_burn_time_reduction_factor',
        on_false='minecraft:cooking/normal_burn_time_reduction_factor',
    ),
    type='minecraft:div',
)

TIME_BOATS = ContextIntProviderStructDiv(
    left=1200,
    right=ContextIntProviderStructConditional(
        type='minecraft:conditional',
        condition='minecraft:block/fast_cooking',
        on_true='minecraft:cooking/fast_burn_time_reduction_factor',
        on_false='minecraft:cooking/normal_burn_time_reduction_factor',
    ),
    type='minecraft:div',
)

TIME_COAL = ContextIntProviderStructDiv(
    left=1600,
    right=ContextIntProviderStructConditional(
        type='minecraft:conditional',
        condition='minecraft:block/fast_cooking',
        on_true='minecraft:cooking/fast_burn_time_reduction_factor',
        on_false='minecraft:cooking/normal_burn_time_reduction_factor',
    ),
    type='minecraft:div',
)

TIME_COAL_BLOCK = ContextIntProviderStructDiv(
    left=16000,
    right=ContextIntProviderStructConditional(
        type='minecraft:conditional',
        condition='minecraft:block/fast_cooking',
        on_true='minecraft:cooking/fast_burn_time_reduction_factor',
        on_false='minecraft:cooking/normal_burn_time_reduction_factor',
    ),
    type='minecraft:div',
)

TIME_DRIED_KELP_BLOCK = ContextIntProviderStructDiv(
    left=4001,
    right=ContextIntProviderStructConditional(
        type='minecraft:conditional',
        condition='minecraft:block/fast_cooking',
        on_true='minecraft:cooking/fast_burn_time_reduction_factor',
        on_false='minecraft:cooking/normal_burn_time_reduction_factor',
    ),
    type='minecraft:div',
)

TIME_DRY_PLANTS = ContextIntProviderStructDiv(
    left=100,
    right=ContextIntProviderStructConditional(
        type='minecraft:conditional',
        condition='minecraft:block/fast_cooking',
        on_true='minecraft:cooking/fast_burn_time_reduction_factor',
        on_false='minecraft:cooking/normal_burn_time_reduction_factor',
    ),
    type='minecraft:div',
)

TIME_HANGING_SIGNS = ContextIntProviderStructDiv(
    left=800,
    right=ContextIntProviderStructConditional(
        type='minecraft:conditional',
        condition='minecraft:block/fast_cooking',
        on_true='minecraft:cooking/fast_burn_time_reduction_factor',
        on_false='minecraft:cooking/normal_burn_time_reduction_factor',
    ),
    type='minecraft:div',
)

TIME_LAVA_BUCKET = ContextIntProviderStructDiv(
    left=20000,
    right=ContextIntProviderStructConditional(
        type='minecraft:conditional',
        condition='minecraft:block/fast_cooking',
        on_true='minecraft:cooking/fast_burn_time_reduction_factor',
        on_false='minecraft:cooking/normal_burn_time_reduction_factor',
    ),
    type='minecraft:div',
)

TIME_ROOTS = ContextIntProviderStructDiv(
    left=300,
    right=ContextIntProviderStructConditional(
        type='minecraft:conditional',
        condition='minecraft:block/fast_cooking',
        on_true='minecraft:cooking/fast_burn_time_reduction_factor',
        on_false='minecraft:cooking/normal_burn_time_reduction_factor',
    ),
    type='minecraft:div',
)

TIME_WOOD_BLOCKS = ContextIntProviderStructDiv(
    left=300,
    right=ContextIntProviderStructConditional(
        type='minecraft:conditional',
        condition='minecraft:block/fast_cooking',
        on_true='minecraft:cooking/fast_burn_time_reduction_factor',
        on_false='minecraft:cooking/normal_burn_time_reduction_factor',
    ),
    type='minecraft:div',
)

TIME_WOOD_ITEMS_EXTRA_SMALL = ContextIntProviderStructDiv(
    left=100,
    right=ContextIntProviderStructConditional(
        type='minecraft:conditional',
        condition='minecraft:block/fast_cooking',
        on_true='minecraft:cooking/fast_burn_time_reduction_factor',
        on_false='minecraft:cooking/normal_burn_time_reduction_factor',
    ),
    type='minecraft:div',
)

TIME_WOOD_ITEMS_LARGE = ContextIntProviderStructDiv(
    left=200,
    right=ContextIntProviderStructConditional(
        type='minecraft:conditional',
        condition='minecraft:block/fast_cooking',
        on_true='minecraft:cooking/fast_burn_time_reduction_factor',
        on_false='minecraft:cooking/normal_burn_time_reduction_factor',
    ),
    type='minecraft:div',
)

TIME_WOOD_ITEMS_SMALL = ContextIntProviderStructDiv(
    left=300,
    right=ContextIntProviderStructConditional(
        type='minecraft:conditional',
        condition='minecraft:block/fast_cooking',
        on_true='minecraft:cooking/fast_burn_time_reduction_factor',
        on_false='minecraft:cooking/normal_burn_time_reduction_factor',
    ),
    type='minecraft:div',
)

TIME_WOOD_SLABS = ContextIntProviderStructDiv(
    left=150,
    right=ContextIntProviderStructConditional(
        type='minecraft:conditional',
        condition='minecraft:block/fast_cooking',
        on_true='minecraft:cooking/fast_burn_time_reduction_factor',
        on_false='minecraft:cooking/normal_burn_time_reduction_factor',
    ),
    type='minecraft:div',
)

TIME_WOOL = ContextIntProviderStructDiv(
    left=100,
    right=ContextIntProviderStructConditional(
        type='minecraft:conditional',
        condition='minecraft:block/fast_cooking',
        on_true='minecraft:cooking/fast_burn_time_reduction_factor',
        on_false='minecraft:cooking/normal_burn_time_reduction_factor',
    ),
    type='minecraft:div',
)

TIME_WOOL_CARPETS = ContextIntProviderStructDiv(
    left=67,
    right=ContextIntProviderStructConditional(
        type='minecraft:conditional',
        condition='minecraft:block/fast_cooking',
        on_true='minecraft:cooking/fast_burn_time_reduction_factor',
        on_false='minecraft:cooking/normal_burn_time_reduction_factor',
    ),
    type='minecraft:div',
)

TIME_WOOL_SLABS = ContextIntProviderStructDiv(
    left=50,
    right=ContextIntProviderStructConditional(
        type='minecraft:conditional',
        condition='minecraft:block/fast_cooking',
        on_true='minecraft:cooking/fast_burn_time_reduction_factor',
        on_false='minecraft:cooking/normal_burn_time_reduction_factor',
    ),
    type='minecraft:div',
)
