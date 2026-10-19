"""Vanilla's data/cow_variant/ files"""
from vanilla_mcdoc.data.variants.SpawnCondition import SpawnConditionBiome
from vanilla_mcdoc.data.variants.SpawnPrioritySelector import SpawnPrioritySelector
from vanilla_mcdoc.data.variants.cow.CowModelType import CowModelType
from vanilla_mcdoc.data.variants.cow.CowVariant import CowVariant

COLD = CowVariant(
    spawn_conditions=[
        SpawnPrioritySelector(
            condition=SpawnConditionBiome(biomes='#minecraft:spawns_cold_variant_farm_animals', type='minecraft:biome'),
            priority=1,
        ),
    ],
    model=CowModelType.COLD,
    asset_id='minecraft:entity/cow/cow_cold',
    baby_asset_id='minecraft:entity/cow/cow_cold_baby',
)

TEMPERATE = CowVariant(
    spawn_conditions=[SpawnPrioritySelector(priority=0)],
    asset_id='minecraft:entity/cow/cow_temperate',
    baby_asset_id='minecraft:entity/cow/cow_temperate_baby',
)

WARM = CowVariant(
    spawn_conditions=[
        SpawnPrioritySelector(
            condition=SpawnConditionBiome(biomes='#minecraft:spawns_warm_variant_farm_animals', type='minecraft:biome'),
            priority=1,
        ),
    ],
    model=CowModelType.WARM,
    asset_id='minecraft:entity/cow/cow_warm',
    baby_asset_id='minecraft:entity/cow/cow_warm_baby',
)
