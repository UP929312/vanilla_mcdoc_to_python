"""Vanilla's data/tags/worldgen/biome/has_structure/ files"""
from vanilla_mcdoc.data.tag.Tag import Tag

ABANDONED_CAMP_BAMBOO_JUNGLE = Tag(values=['minecraft:bamboo_jungle'])

ABANDONED_CAMP_BIRCH_FOREST = Tag(values=['minecraft:birch_forest'])

ABANDONED_CAMP_CHERRY_GROVE = Tag(values=['minecraft:cherry_grove'])

ABANDONED_CAMP_DAPPLED_FOREST = Tag(values=['minecraft:dappled_forest'])

ABANDONED_CAMP_FLOWER_FOREST = Tag(values=['minecraft:flower_forest'])

ABANDONED_CAMP_FOREST = Tag(values=['minecraft:forest'])

ABANDONED_CAMP_MEADOW = Tag(values=['minecraft:meadow'])

ABANDONED_CAMP_OLD_GROWTH_BIRCH_FOREST = Tag(values=['minecraft:old_growth_birch_forest'])

ABANDONED_CAMP_OLD_GROWTH_PINE_TAIGA = Tag(values=['minecraft:old_growth_pine_taiga'])

ABANDONED_CAMP_OLD_GROWTH_SPRUCE_TAIGA = Tag(values=['minecraft:old_growth_spruce_taiga'])

ABANDONED_CAMP_PALE_GARDEN = Tag(values=['minecraft:pale_garden'])

ABANDONED_CAMP_SAVANNA = Tag(values=['minecraft:savanna'])

ABANDONED_CAMP_SNOWY_TAIGA = Tag(values=['minecraft:snowy_taiga'])

ABANDONED_CAMP_SPARSE_JUNGLE = Tag(values=['minecraft:sparse_jungle'])

ABANDONED_CAMP_SWAMP = Tag(values=['minecraft:swamp'])

ABANDONED_CAMP_TAIGA = Tag(values=['minecraft:taiga'])

ABANDONED_CAMP_WINDSWEPT_FOREST = Tag(values=['minecraft:windswept_forest'])

ABANDONED_CAMP_WOODED_BADLANDS = Tag(values=['minecraft:wooded_badlands'])

ANCIENT_CITY = Tag(values=['minecraft:deep_dark'])

BASTION_REMNANT = Tag(
    values=['minecraft:crimson_forest', 'minecraft:nether_wastes', 'minecraft:soul_sand_valley', 'minecraft:warped_forest'],
)

BURIED_TREASURE = Tag(values=['#minecraft:is_beach'])

DESERT_PYRAMID = Tag(values=['minecraft:desert'])

END_CITY = Tag(values=['minecraft:end_highlands', 'minecraft:end_midlands'])

IGLOO = Tag(values=['minecraft:snowy_taiga', 'minecraft:snowy_plains', 'minecraft:snowy_slopes'])

JUNGLE_TEMPLE = Tag(values=['minecraft:bamboo_jungle', 'minecraft:jungle'])

MINESHAFT = Tag(
    values=[
        '#minecraft:is_ocean',
        '#minecraft:is_river',
        '#minecraft:is_beach',
        '#minecraft:is_mountain',
        '#minecraft:is_hill',
        '#minecraft:is_taiga',
        '#minecraft:is_jungle',
        '#minecraft:is_forest',
        'minecraft:stony_shore',
        'minecraft:mushroom_fields',
        'minecraft:ice_spikes',
        'minecraft:windswept_savanna',
        'minecraft:desert',
        'minecraft:savanna',
        'minecraft:snowy_plains',
        'minecraft:plains',
        'minecraft:sunflower_plains',
        'minecraft:swamp',
        'minecraft:mangrove_swamp',
        'minecraft:savanna_plateau',
        'minecraft:dripstone_caves',
        'minecraft:lush_caves',
        'minecraft:sulfur_caves',
        'minecraft:ice_caves',
    ],
)

MINESHAFT_MESA = Tag(values=['#minecraft:is_badlands'])

NETHER_FORTRESS = Tag(values=['#minecraft:is_nether'])

NETHER_FOSSIL = Tag(values=['minecraft:soul_sand_valley'])

OCEAN_MONUMENT = Tag(values=['#minecraft:is_deep_ocean'])

OCEAN_RUIN_COLD = Tag(
    values=[
        'minecraft:frozen_ocean',
        'minecraft:cold_ocean',
        'minecraft:ocean',
        'minecraft:deep_frozen_ocean',
        'minecraft:deep_cold_ocean',
        'minecraft:deep_ocean',
    ],
)

OCEAN_RUIN_WARM = Tag(values=['minecraft:lukewarm_ocean', 'minecraft:warm_ocean', 'minecraft:deep_lukewarm_ocean'])

PILLAGER_OUTPOST = Tag(
    values=[
        'minecraft:desert',
        'minecraft:plains',
        'minecraft:savanna',
        'minecraft:snowy_plains',
        'minecraft:taiga',
        '#minecraft:is_mountain',
        'minecraft:grove',
    ],
)

RUINED_PORTAL_DESERT = Tag(values=['minecraft:desert'])

RUINED_PORTAL_JUNGLE = Tag(values=['#minecraft:is_jungle'])

RUINED_PORTAL_MOUNTAIN = Tag(
    values=[
        '#minecraft:is_badlands',
        '#minecraft:is_hill',
        'minecraft:savanna_plateau',
        'minecraft:windswept_savanna',
        'minecraft:stony_shore',
        '#minecraft:is_mountain',
    ],
)

RUINED_PORTAL_NETHER = Tag(values=['#minecraft:is_nether'])

RUINED_PORTAL_OCEAN = Tag(values=['#minecraft:is_ocean'])

RUINED_PORTAL_STANDARD = Tag(
    values=[
        '#minecraft:is_beach',
        '#minecraft:is_river',
        '#minecraft:is_taiga',
        '#minecraft:is_forest',
        'minecraft:mushroom_fields',
        'minecraft:ice_spikes',
        'minecraft:dripstone_caves',
        'minecraft:lush_caves',
        'minecraft:sulfur_caves',
        'minecraft:savanna',
        'minecraft:snowy_plains',
        'minecraft:plains',
        'minecraft:sunflower_plains',
    ],
)

RUINED_PORTAL_SWAMP = Tag(values=['minecraft:swamp', 'minecraft:mangrove_swamp'])

SHIPWRECK = Tag(values=['#minecraft:is_ocean'])

SHIPWRECK_BEACHED = Tag(values=['#minecraft:is_beach'])

STRONGHOLD = Tag(values=['#minecraft:is_overworld'])

SWAMP_HUT = Tag(values=['minecraft:swamp'])

TRAIL_RUINS = Tag(
    values=[
        'minecraft:taiga',
        'minecraft:snowy_taiga',
        'minecraft:old_growth_pine_taiga',
        'minecraft:old_growth_spruce_taiga',
        'minecraft:old_growth_birch_forest',
        'minecraft:jungle',
    ],
)

TRIAL_CHAMBERS = Tag(
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
        'minecraft:ice_caves',
    ],
)

VILLAGE_DESERT = Tag(values=['minecraft:desert'])

VILLAGE_PLAINS = Tag(values=['minecraft:plains', 'minecraft:meadow'])

VILLAGE_SAVANNA = Tag(values=['minecraft:savanna'])

VILLAGE_SNOWY = Tag(values=['minecraft:snowy_plains'])

VILLAGE_TAIGA = Tag(values=['minecraft:taiga'])

WOODLAND_MANSION = Tag(values=['minecraft:dark_forest', 'minecraft:pale_garden'])
