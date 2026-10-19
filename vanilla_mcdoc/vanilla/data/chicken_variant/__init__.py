"""Vanilla's data/chicken_variant/ files"""
from vanilla_mcdoc.data.variants.SpawnCondition import SpawnConditionBiome
from vanilla_mcdoc.data.variants.SpawnPrioritySelector import SpawnPrioritySelector
from vanilla_mcdoc.data.variants.chicken.ChickenModelType import ChickenModelType
from vanilla_mcdoc.data.variants.chicken.ChickenVariant import ChickenVariant

COLD = ChickenVariant(
    spawn_conditions=[
        SpawnPrioritySelector(
            condition=SpawnConditionBiome(biomes='#minecraft:spawns_cold_variant_farm_animals', type='minecraft:biome'),
            priority=1,
        ),
    ],
    model=ChickenModelType.COLD,
    asset_id='minecraft:entity/chicken/chicken_cold',
    baby_asset_id='minecraft:entity/chicken/chicken_cold_baby',
)

TEMPERATE = ChickenVariant(
    spawn_conditions=[SpawnPrioritySelector(priority=0)],
    asset_id='minecraft:entity/chicken/chicken_temperate',
    baby_asset_id='minecraft:entity/chicken/chicken_temperate_baby',
)

WARM = ChickenVariant(
    spawn_conditions=[
        SpawnPrioritySelector(
            condition=SpawnConditionBiome(biomes='#minecraft:spawns_warm_variant_farm_animals', type='minecraft:biome'),
            priority=1,
        ),
    ],
    asset_id='minecraft:entity/chicken/chicken_warm',
    baby_asset_id='minecraft:entity/chicken/chicken_warm_baby',
)
