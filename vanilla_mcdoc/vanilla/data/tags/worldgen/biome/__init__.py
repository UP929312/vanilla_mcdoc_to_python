"""Vanilla's data/tags/worldgen/biome/ files"""
from vanilla_mcdoc.data.tag.Tag import Tag

ALLOWS_SURFACE_SLIME_SPAWNS = Tag(values=['minecraft:swamp', 'minecraft:mangrove_swamp'])

ALLOWS_TROPICAL_FISH_SPAWNS_AT_ANY_HEIGHT = Tag(values=['minecraft:lush_caves'])

GENERATED_IN_BELOW_ZERO_RETROGEN = Tag(values=['#minecraft:is_cave'])

IS_BADLANDS = Tag(values=['minecraft:badlands', 'minecraft:eroded_badlands', 'minecraft:wooded_badlands'])

IS_BEACH = Tag(values=['minecraft:beach', 'minecraft:snowy_beach'])

IS_CAVE = Tag(
    values=[
        'minecraft:lush_caves',
        'minecraft:deep_dark',
        'minecraft:dripstone_caves',
        'minecraft:sulfur_caves',
        'minecraft:ice_caves',
    ],
)

IS_DEEP_OCEAN = Tag(
    values=[
        'minecraft:deep_frozen_ocean',
        'minecraft:deep_cold_ocean',
        'minecraft:deep_ocean',
        'minecraft:deep_lukewarm_ocean',
    ],
)

IS_END = Tag(
    values=[
        'minecraft:the_end',
        'minecraft:end_highlands',
        'minecraft:end_midlands',
        'minecraft:small_end_islands',
        'minecraft:end_barrens',
    ],
)

IS_FOREST = Tag(
    values=[
        'minecraft:forest',
        'minecraft:flower_forest',
        'minecraft:birch_forest',
        'minecraft:old_growth_birch_forest',
        'minecraft:dappled_forest',
        'minecraft:dark_forest',
        'minecraft:pale_garden',
        'minecraft:grove',
    ],
)

IS_HILL = Tag(values=['minecraft:windswept_hills', 'minecraft:windswept_forest', 'minecraft:windswept_gravelly_hills'])

IS_JUNGLE = Tag(values=['minecraft:bamboo_jungle', 'minecraft:jungle', 'minecraft:sparse_jungle'])

IS_MOUNTAIN = Tag(
    values=[
        'minecraft:meadow',
        'minecraft:frozen_peaks',
        'minecraft:jagged_peaks',
        'minecraft:stony_peaks',
        'minecraft:snowy_slopes',
        'minecraft:cherry_grove',
    ],
)

IS_NETHER = Tag(
    values=[
        'minecraft:nether_wastes',
        'minecraft:soul_sand_valley',
        'minecraft:crimson_forest',
        'minecraft:warped_forest',
        'minecraft:basalt_deltas',
    ],
)

IS_OCEAN = Tag(
    values=[
        '#minecraft:is_deep_ocean',
        'minecraft:frozen_ocean',
        'minecraft:ocean',
        'minecraft:cold_ocean',
        'minecraft:lukewarm_ocean',
        'minecraft:warm_ocean',
    ],
)

IS_OVERWORLD = Tag(
    values=[
        'minecraft:mushroom_fields',
        'minecraft:deep_frozen_ocean',
        'minecraft:frozen_ocean',
        'minecraft:deep_cold_ocean',
        'minecraft:cold_ocean',
        'minecraft:deep_ocean',
        'minecraft:ocean',
        'minecraft:deep_lukewarm_ocean',
        'minecraft:lukewarm_ocean',
        'minecraft:warm_ocean',
        'minecraft:stony_shore',
        'minecraft:swamp',
        'minecraft:mangrove_swamp',
        'minecraft:snowy_slopes',
        'minecraft:snowy_plains',
        'minecraft:snowy_beach',
        'minecraft:windswept_gravelly_hills',
        'minecraft:grove',
        'minecraft:windswept_hills',
        'minecraft:snowy_taiga',
        'minecraft:windswept_forest',
        'minecraft:taiga',
        'minecraft:plains',
        'minecraft:meadow',
        'minecraft:beach',
        'minecraft:forest',
        'minecraft:old_growth_spruce_taiga',
        'minecraft:flower_forest',
        'minecraft:birch_forest',
        'minecraft:dark_forest',
        'minecraft:pale_garden',
        'minecraft:savanna_plateau',
        'minecraft:savanna',
        'minecraft:jungle',
        'minecraft:badlands',
        'minecraft:desert',
        'minecraft:wooded_badlands',
        'minecraft:jagged_peaks',
        'minecraft:stony_peaks',
        'minecraft:frozen_river',
        'minecraft:river',
        'minecraft:ice_spikes',
        'minecraft:dappled_forest',
        'minecraft:old_growth_pine_taiga',
        'minecraft:sunflower_plains',
        'minecraft:old_growth_birch_forest',
        'minecraft:sparse_jungle',
        'minecraft:bamboo_jungle',
        'minecraft:eroded_badlands',
        'minecraft:windswept_savanna',
        'minecraft:cherry_grove',
        'minecraft:frozen_peaks',
        'minecraft:dripstone_caves',
        'minecraft:lush_caves',
        'minecraft:sulfur_caves',
        'minecraft:deep_dark',
        'minecraft:ice_caves',
    ],
)

IS_RIVER = Tag(values=['minecraft:river', 'minecraft:frozen_river'])

IS_SAVANNA = Tag(values=['minecraft:savanna', 'minecraft:savanna_plateau', 'minecraft:windswept_savanna'])

IS_TAIGA = Tag(
    values=['minecraft:taiga', 'minecraft:snowy_taiga', 'minecraft:old_growth_pine_taiga', 'minecraft:old_growth_spruce_taiga'],
)

MINESHAFT_BLOCKING = Tag(values=['minecraft:deep_dark'])

MORE_FREQUENT_DROWNED_SPAWNS = Tag(values=['#minecraft:is_river'])

POLAR_BEARS_SPAWN_ON_ALTERNATE_BLOCKS = Tag(values=['minecraft:frozen_ocean', 'minecraft:deep_frozen_ocean'])

PRODUCES_CORALS_FROM_BONEMEAL = Tag(values=['minecraft:warm_ocean'])

REDUCE_WATER_AMBIENT_SPAWNS = Tag(values=['#minecraft:is_river'])

REQUIRED_OCEAN_MONUMENT_SURROUNDING = Tag(values=['#minecraft:is_ocean', '#minecraft:is_river'])

SPAWNS_COLD_VARIANT_FARM_ANIMALS = Tag(
    values=[
        'minecraft:snowy_plains',
        'minecraft:ice_spikes',
        'minecraft:frozen_peaks',
        'minecraft:jagged_peaks',
        'minecraft:snowy_slopes',
        'minecraft:frozen_ocean',
        'minecraft:deep_frozen_ocean',
        'minecraft:grove',
        'minecraft:deep_dark',
        'minecraft:frozen_river',
        'minecraft:snowy_taiga',
        'minecraft:snowy_beach',
        '#minecraft:is_end',
        'minecraft:cold_ocean',
        'minecraft:deep_cold_ocean',
        'minecraft:old_growth_pine_taiga',
        'minecraft:old_growth_spruce_taiga',
        'minecraft:taiga',
        'minecraft:windswept_forest',
        'minecraft:windswept_gravelly_hills',
        'minecraft:windswept_hills',
        'minecraft:stony_peaks',
        'minecraft:dappled_forest',
        'minecraft:ice_caves',
    ],
)

SPAWNS_COLD_VARIANT_FROGS = Tag(
    values=[
        'minecraft:snowy_plains',
        'minecraft:ice_spikes',
        'minecraft:frozen_peaks',
        'minecraft:jagged_peaks',
        'minecraft:snowy_slopes',
        'minecraft:frozen_ocean',
        'minecraft:deep_frozen_ocean',
        'minecraft:grove',
        'minecraft:deep_dark',
        'minecraft:frozen_river',
        'minecraft:snowy_taiga',
        'minecraft:snowy_beach',
        '#minecraft:is_end',
        'minecraft:ice_caves',
    ],
)

SPAWNS_CORAL_VARIANT_ZOMBIE_NAUTILUS = Tag(values=['minecraft:warm_ocean'])

SPAWNS_GOLD_RABBITS = Tag(values=['minecraft:desert'])

SPAWNS_SNOW_FOXES = Tag(
    values=[
        'minecraft:snowy_plains',
        'minecraft:ice_spikes',
        'minecraft:frozen_ocean',
        'minecraft:snowy_taiga',
        'minecraft:frozen_river',
        'minecraft:snowy_beach',
        'minecraft:frozen_peaks',
        'minecraft:jagged_peaks',
        'minecraft:snowy_slopes',
        'minecraft:grove',
        'minecraft:ice_caves',
    ],
)

SPAWNS_STRAYS_WITHOUT_POWDER_SNOW = Tag(values=['minecraft:ice_caves'])

SPAWNS_WARM_VARIANT_FARM_ANIMALS = Tag(
    values=[
        'minecraft:desert',
        'minecraft:warm_ocean',
        '#minecraft:is_jungle',
        '#minecraft:is_savanna',
        '#minecraft:is_nether',
        '#minecraft:is_badlands',
        'minecraft:mangrove_swamp',
        'minecraft:deep_lukewarm_ocean',
        'minecraft:lukewarm_ocean',
    ],
)

SPAWNS_WARM_VARIANT_FROGS = Tag(
    values=[
        'minecraft:desert',
        'minecraft:warm_ocean',
        '#minecraft:is_jungle',
        '#minecraft:is_savanna',
        '#minecraft:is_nether',
        '#minecraft:is_badlands',
        'minecraft:mangrove_swamp',
    ],
)

SPAWNS_WHITE_RABBITS = Tag(
    values=[
        'minecraft:snowy_plains',
        'minecraft:ice_spikes',
        'minecraft:frozen_ocean',
        'minecraft:snowy_taiga',
        'minecraft:frozen_river',
        'minecraft:snowy_beach',
        'minecraft:frozen_peaks',
        'minecraft:jagged_peaks',
        'minecraft:snowy_slopes',
        'minecraft:grove',
        'minecraft:ice_caves',
    ],
)

STRONGHOLD_BIASED_TO = Tag(
    values=[
        'minecraft:plains',
        'minecraft:sunflower_plains',
        'minecraft:snowy_plains',
        'minecraft:ice_spikes',
        'minecraft:desert',
        'minecraft:forest',
        'minecraft:flower_forest',
        'minecraft:birch_forest',
        'minecraft:dark_forest',
        'minecraft:pale_garden',
        'minecraft:old_growth_birch_forest',
        'minecraft:old_growth_pine_taiga',
        'minecraft:old_growth_spruce_taiga',
        'minecraft:taiga',
        'minecraft:snowy_taiga',
        'minecraft:savanna',
        'minecraft:savanna_plateau',
        'minecraft:windswept_hills',
        'minecraft:windswept_gravelly_hills',
        'minecraft:windswept_forest',
        'minecraft:windswept_savanna',
        'minecraft:jungle',
        'minecraft:sparse_jungle',
        'minecraft:bamboo_jungle',
        'minecraft:badlands',
        'minecraft:eroded_badlands',
        'minecraft:wooded_badlands',
        'minecraft:meadow',
        'minecraft:cherry_grove',
        'minecraft:grove',
        'minecraft:snowy_slopes',
        'minecraft:frozen_peaks',
        'minecraft:jagged_peaks',
        'minecraft:stony_peaks',
        'minecraft:mushroom_fields',
        'minecraft:dripstone_caves',
        'minecraft:lush_caves',
        'minecraft:sulfur_caves',
    ],
)

WATER_ON_MAP_OUTLINES = Tag(values=['#minecraft:is_ocean', '#minecraft:is_river', 'minecraft:swamp', 'minecraft:mangrove_swamp'])

WITHOUT_WANDERING_TRADER_SPAWNS = Tag(values=['minecraft:the_void'])

WITHOUT_ZOMBIE_SIEGES = Tag(values=['minecraft:mushroom_fields'])
