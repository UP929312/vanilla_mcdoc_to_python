"""Vanilla's data/context_float_provider/cooking/ files"""
from vanilla_mcdoc.data.number_provider.context_float.ContextFloatProvider import ContextFloatProviderStructConditional

FAST_SPEED_MULTIPLIER = 2.0

NORMAL_SPEED_MULTIPLIER = 1.0

SPEED_DEFAULT = ContextFloatProviderStructConditional(
    type='minecraft:conditional',
    condition='minecraft:block/fast_cooking',
    on_true='minecraft:cooking/fast_speed_multiplier',
    on_false='minecraft:cooking/normal_speed_multiplier',
)
