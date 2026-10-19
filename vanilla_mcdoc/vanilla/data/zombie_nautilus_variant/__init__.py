"""Vanilla's data/zombie_nautilus_variant/ files"""
from vanilla_mcdoc.data.variants.SpawnCondition import SpawnConditionBiome
from vanilla_mcdoc.data.variants.SpawnPrioritySelector import SpawnPrioritySelector
from vanilla_mcdoc.data.variants.zombie_nautilus.ZombieNautilusModelType import ZombieNautilusModelType
from vanilla_mcdoc.data.variants.zombie_nautilus.ZombieNautilusVariant import ZombieNautilusVariant

TEMPERATE = ZombieNautilusVariant(
    spawn_conditions=[SpawnPrioritySelector(priority=0)],
    asset_id='minecraft:entity/nautilus/zombie_nautilus',
)

WARM = ZombieNautilusVariant(
    spawn_conditions=[
        SpawnPrioritySelector(
            condition=SpawnConditionBiome(biomes='#minecraft:spawns_coral_variant_zombie_nautilus', type='minecraft:biome'),
            priority=1,
        ),
    ],
    model=ZombieNautilusModelType.WARM,
    asset_id='minecraft:entity/nautilus/zombie_nautilus_coral',
)
