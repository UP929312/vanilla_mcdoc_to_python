"""Vanilla's data/cat_variant/ files"""
from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds
from vanilla_mcdoc.data.variants.SpawnCondition import SpawnConditionMoonBrightness, SpawnConditionStructure
from vanilla_mcdoc.data.variants.SpawnPrioritySelector import SpawnPrioritySelector
from vanilla_mcdoc.data.variants.cat.CatVariant import CatVariant

ALL_BLACK = CatVariant(
    spawn_conditions=[
        SpawnPrioritySelector(
            condition=SpawnConditionStructure(structures='#minecraft:cats_spawn_as_black', type='minecraft:structure'),
            priority=1,
        ),
        SpawnPrioritySelector(
            condition=SpawnConditionMoonBrightness(range=MinMaxBounds(min=0.9), type='minecraft:moon_brightness'),
            priority=0,
        ),
    ],
    asset_id='minecraft:entity/cat/cat_all_black',
    baby_asset_id='minecraft:entity/cat/cat_all_black_baby',
)

BLACK = CatVariant(
    spawn_conditions=[SpawnPrioritySelector(priority=0)],
    asset_id='minecraft:entity/cat/cat_black',
    baby_asset_id='minecraft:entity/cat/cat_black_baby',
)

BRITISH_SHORTHAIR = CatVariant(
    spawn_conditions=[SpawnPrioritySelector(priority=0)],
    asset_id='minecraft:entity/cat/cat_british_shorthair',
    baby_asset_id='minecraft:entity/cat/cat_british_shorthair_baby',
)

CALICO = CatVariant(
    spawn_conditions=[SpawnPrioritySelector(priority=0)],
    asset_id='minecraft:entity/cat/cat_calico',
    baby_asset_id='minecraft:entity/cat/cat_calico_baby',
)

JELLIE = CatVariant(
    spawn_conditions=[SpawnPrioritySelector(priority=0)],
    asset_id='minecraft:entity/cat/cat_jellie',
    baby_asset_id='minecraft:entity/cat/cat_jellie_baby',
)

PERSIAN = CatVariant(
    spawn_conditions=[SpawnPrioritySelector(priority=0)],
    asset_id='minecraft:entity/cat/cat_persian',
    baby_asset_id='minecraft:entity/cat/cat_persian_baby',
)

RAGDOLL = CatVariant(
    spawn_conditions=[SpawnPrioritySelector(priority=0)],
    asset_id='minecraft:entity/cat/cat_ragdoll',
    baby_asset_id='minecraft:entity/cat/cat_ragdoll_baby',
)

RED = CatVariant(
    spawn_conditions=[SpawnPrioritySelector(priority=0)],
    asset_id='minecraft:entity/cat/cat_red',
    baby_asset_id='minecraft:entity/cat/cat_red_baby',
)

SIAMESE = CatVariant(
    spawn_conditions=[SpawnPrioritySelector(priority=0)],
    asset_id='minecraft:entity/cat/cat_siamese',
    baby_asset_id='minecraft:entity/cat/cat_siamese_baby',
)

TABBY = CatVariant(
    spawn_conditions=[SpawnPrioritySelector(priority=0)],
    asset_id='minecraft:entity/cat/cat_tabby',
    baby_asset_id='minecraft:entity/cat/cat_tabby_baby',
)

WHITE = CatVariant(
    spawn_conditions=[SpawnPrioritySelector(priority=0)],
    asset_id='minecraft:entity/cat/cat_white',
    baby_asset_id='minecraft:entity/cat/cat_white_baby',
)
