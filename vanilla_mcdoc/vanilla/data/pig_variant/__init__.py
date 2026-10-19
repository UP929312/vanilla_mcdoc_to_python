"""Vanilla's data/pig_variant/ files"""
from vanilla_mcdoc.data.variants.SpawnCondition import SpawnConditionBiome
from vanilla_mcdoc.data.variants.SpawnPrioritySelector import SpawnPrioritySelector
from vanilla_mcdoc.data.variants.pig.PigModelType import PigModelType
from vanilla_mcdoc.data.variants.pig.PigVariant import PigVariant

COLD = PigVariant(
    spawn_conditions=[
        SpawnPrioritySelector(
            condition=SpawnConditionBiome(biomes='#minecraft:spawns_cold_variant_farm_animals', type='minecraft:biome'),
            priority=1,
        ),
    ],
    model=PigModelType.COLD,
    asset_id='minecraft:entity/pig/pig_cold',
    baby_asset_id='minecraft:entity/pig/pig_cold_baby',
)

TEMPERATE = PigVariant(
    spawn_conditions=[SpawnPrioritySelector(priority=0)],
    asset_id='minecraft:entity/pig/pig_temperate',
    baby_asset_id='minecraft:entity/pig/pig_temperate_baby',
)

WARM = PigVariant(
    spawn_conditions=[
        SpawnPrioritySelector(
            condition=SpawnConditionBiome(biomes='#minecraft:spawns_warm_variant_farm_animals', type='minecraft:biome'),
            priority=1,
        ),
    ],
    asset_id='minecraft:entity/pig/pig_warm',
    baby_asset_id='minecraft:entity/pig/pig_warm_baby',
)
