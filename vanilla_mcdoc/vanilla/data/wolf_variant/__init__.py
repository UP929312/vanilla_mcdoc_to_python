"""Vanilla's data/wolf_variant/ files"""
from vanilla_mcdoc.data.variants.SpawnCondition import SpawnConditionBiome
from vanilla_mcdoc.data.variants.SpawnPrioritySelector import SpawnPrioritySelector
from vanilla_mcdoc.data.variants.wolf.WolfVariant import WolfVariant
from vanilla_mcdoc.data.variants.wolf.WolfVariantAssetInfo import WolfVariantAssetInfo

ASHEN = WolfVariant(
    spawn_conditions=[
        SpawnPrioritySelector(
            condition=SpawnConditionBiome(biomes='minecraft:snowy_taiga', type='minecraft:biome'),
            priority=1,
        ),
    ],
    assets=WolfVariantAssetInfo(
        wild='minecraft:entity/wolf/wolf_ashen',
        tame='minecraft:entity/wolf/wolf_ashen_tame',
        angry='minecraft:entity/wolf/wolf_ashen_angry',
    ),
    baby_assets=WolfVariantAssetInfo(
        wild='minecraft:entity/wolf/wolf_ashen_baby',
        tame='minecraft:entity/wolf/wolf_ashen_tame_baby',
        angry='minecraft:entity/wolf/wolf_ashen_angry_baby',
    ),
)

BLACK = WolfVariant(
    spawn_conditions=[
        SpawnPrioritySelector(
            condition=SpawnConditionBiome(biomes='minecraft:old_growth_pine_taiga', type='minecraft:biome'),
            priority=1,
        ),
    ],
    assets=WolfVariantAssetInfo(
        wild='minecraft:entity/wolf/wolf_black',
        tame='minecraft:entity/wolf/wolf_black_tame',
        angry='minecraft:entity/wolf/wolf_black_angry',
    ),
    baby_assets=WolfVariantAssetInfo(
        wild='minecraft:entity/wolf/wolf_black_baby',
        tame='minecraft:entity/wolf/wolf_black_tame_baby',
        angry='minecraft:entity/wolf/wolf_black_angry_baby',
    ),
)

CHESTNUT = WolfVariant(
    spawn_conditions=[
        SpawnPrioritySelector(
            condition=SpawnConditionBiome(biomes='minecraft:old_growth_spruce_taiga', type='minecraft:biome'),
            priority=1,
        ),
    ],
    assets=WolfVariantAssetInfo(
        wild='minecraft:entity/wolf/wolf_chestnut',
        tame='minecraft:entity/wolf/wolf_chestnut_tame',
        angry='minecraft:entity/wolf/wolf_chestnut_angry',
    ),
    baby_assets=WolfVariantAssetInfo(
        wild='minecraft:entity/wolf/wolf_chestnut_baby',
        tame='minecraft:entity/wolf/wolf_chestnut_tame_baby',
        angry='minecraft:entity/wolf/wolf_chestnut_angry_baby',
    ),
)

PALE = WolfVariant(
    spawn_conditions=[SpawnPrioritySelector(priority=0)],
    assets=WolfVariantAssetInfo(
        wild='minecraft:entity/wolf/wolf',
        tame='minecraft:entity/wolf/wolf_tame',
        angry='minecraft:entity/wolf/wolf_angry',
    ),
    baby_assets=WolfVariantAssetInfo(
        wild='minecraft:entity/wolf/wolf_baby',
        tame='minecraft:entity/wolf/wolf_tame_baby',
        angry='minecraft:entity/wolf/wolf_angry_baby',
    ),
)

RUSTY = WolfVariant(
    spawn_conditions=[
        SpawnPrioritySelector(
            condition=SpawnConditionBiome(biomes='#minecraft:is_jungle', type='minecraft:biome'),
            priority=1,
        ),
    ],
    assets=WolfVariantAssetInfo(
        wild='minecraft:entity/wolf/wolf_rusty',
        tame='minecraft:entity/wolf/wolf_rusty_tame',
        angry='minecraft:entity/wolf/wolf_rusty_angry',
    ),
    baby_assets=WolfVariantAssetInfo(
        wild='minecraft:entity/wolf/wolf_rusty_baby',
        tame='minecraft:entity/wolf/wolf_rusty_tame_baby',
        angry='minecraft:entity/wolf/wolf_rusty_angry_baby',
    ),
)

SNOWY = WolfVariant(
    spawn_conditions=[
        SpawnPrioritySelector(
            condition=SpawnConditionBiome(biomes='minecraft:grove', type='minecraft:biome'),
            priority=1,
        ),
    ],
    assets=WolfVariantAssetInfo(
        wild='minecraft:entity/wolf/wolf_snowy',
        tame='minecraft:entity/wolf/wolf_snowy_tame',
        angry='minecraft:entity/wolf/wolf_snowy_angry',
    ),
    baby_assets=WolfVariantAssetInfo(
        wild='minecraft:entity/wolf/wolf_snowy_baby',
        tame='minecraft:entity/wolf/wolf_snowy_tame_baby',
        angry='minecraft:entity/wolf/wolf_snowy_angry_baby',
    ),
)

SPOTTED = WolfVariant(
    spawn_conditions=[
        SpawnPrioritySelector(
            condition=SpawnConditionBiome(biomes='#minecraft:is_savanna', type='minecraft:biome'),
            priority=1,
        ),
    ],
    assets=WolfVariantAssetInfo(
        wild='minecraft:entity/wolf/wolf_spotted',
        tame='minecraft:entity/wolf/wolf_spotted_tame',
        angry='minecraft:entity/wolf/wolf_spotted_angry',
    ),
    baby_assets=WolfVariantAssetInfo(
        wild='minecraft:entity/wolf/wolf_spotted_baby',
        tame='minecraft:entity/wolf/wolf_spotted_tame_baby',
        angry='minecraft:entity/wolf/wolf_spotted_angry_baby',
    ),
)

STRIPED = WolfVariant(
    spawn_conditions=[
        SpawnPrioritySelector(
            condition=SpawnConditionBiome(biomes='#minecraft:is_badlands', type='minecraft:biome'),
            priority=1,
        ),
    ],
    assets=WolfVariantAssetInfo(
        wild='minecraft:entity/wolf/wolf_striped',
        tame='minecraft:entity/wolf/wolf_striped_tame',
        angry='minecraft:entity/wolf/wolf_striped_angry',
    ),
    baby_assets=WolfVariantAssetInfo(
        wild='minecraft:entity/wolf/wolf_striped_baby',
        tame='minecraft:entity/wolf/wolf_striped_tame_baby',
        angry='minecraft:entity/wolf/wolf_striped_angry_baby',
    ),
)

WOODS = WolfVariant(
    spawn_conditions=[
        SpawnPrioritySelector(
            condition=SpawnConditionBiome(biomes='minecraft:forest', type='minecraft:biome'),
            priority=1,
        ),
    ],
    assets=WolfVariantAssetInfo(
        wild='minecraft:entity/wolf/wolf_woods',
        tame='minecraft:entity/wolf/wolf_woods_tame',
        angry='minecraft:entity/wolf/wolf_woods_angry',
    ),
    baby_assets=WolfVariantAssetInfo(
        wild='minecraft:entity/wolf/wolf_woods_baby',
        tame='minecraft:entity/wolf/wolf_woods_tame_baby',
        angry='minecraft:entity/wolf/wolf_woods_angry_baby',
    ),
)
