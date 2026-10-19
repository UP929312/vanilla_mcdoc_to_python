"""Vanilla's data/frog_variant/ files"""
from vanilla_mcdoc.data.variants.SpawnCondition import SpawnConditionBiome
from vanilla_mcdoc.data.variants.SpawnPrioritySelector import SpawnPrioritySelector
from vanilla_mcdoc.data.variants.frog.FrogVariant import FrogVariant

COLD = FrogVariant(
    spawn_conditions=[
        SpawnPrioritySelector(
            condition=SpawnConditionBiome(biomes='#minecraft:spawns_cold_variant_frogs', type='minecraft:biome'),
            priority=1,
        ),
    ],
    asset_id='minecraft:entity/frog/frog_cold',
)

TEMPERATE = FrogVariant(spawn_conditions=[SpawnPrioritySelector(priority=0)], asset_id='minecraft:entity/frog/frog_temperate')

WARM = FrogVariant(
    spawn_conditions=[
        SpawnPrioritySelector(
            condition=SpawnConditionBiome(biomes='#minecraft:spawns_warm_variant_frogs', type='minecraft:biome'),
            priority=1,
        ),
    ],
    asset_id='minecraft:entity/frog/frog_warm',
)
