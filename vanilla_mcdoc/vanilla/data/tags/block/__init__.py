"""Vanilla's data/tags/block/ files"""
from vanilla_mcdoc.data.tag.Tag import Tag

ACACIA_LOGS = Tag(
    values=['minecraft:acacia_log', 'minecraft:acacia_wood', 'minecraft:stripped_acacia_log', 'minecraft:stripped_acacia_wood'],
)

AIR = Tag(values=['minecraft:air', 'minecraft:void_air', 'minecraft:cave_air'])

ALL_HANGING_SIGNS = Tag(values=['#minecraft:ceiling_hanging_signs', '#minecraft:wall_hanging_signs'])

ALL_SIGNS = Tag(values=['#minecraft:signs', '#minecraft:all_hanging_signs'])

ANCIENT_CITY_REPLACEABLE = Tag(
    values=[
        'minecraft:deepslate',
        'minecraft:deepslate_bricks',
        'minecraft:deepslate_tiles',
        'minecraft:deepslate_brick_slab',
        'minecraft:deepslate_tile_slab',
        'minecraft:deepslate_brick_stairs',
        'minecraft:deepslate_tile_wall',
        'minecraft:deepslate_brick_wall',
        'minecraft:cobbled_deepslate',
        'minecraft:cracked_deepslate_bricks',
        'minecraft:cracked_deepslate_tiles',
        'minecraft:gray_wool',
    ],
)

ANIMALS_SPAWNABLE_ON = Tag(values=['minecraft:grass_block'])

ANVIL = Tag(values=['minecraft:anvil', 'minecraft:chipped_anvil', 'minecraft:damaged_anvil'])

ARMADILLO_SPAWNABLE_ON = Tag(
    values=['#minecraft:animals_spawnable_on', '#minecraft:badlands_terracotta', 'minecraft:red_sand', 'minecraft:coarse_dirt'],
)

AXOLOTLS_SPAWNABLE_ON = Tag(values=['minecraft:clay'])

AZALEA_GROWS_ON = Tag(
    values=[
        '#minecraft:substrate_overworld',
        '#minecraft:sand',
        '#minecraft:terracotta',
        'minecraft:snow_block',
        'minecraft:powder_snow',
    ],
)

AZALEA_ROOT_REPLACEABLE = Tag(
    values=[
        '#minecraft:base_stone_overworld',
        '#minecraft:substrate_overworld',
        '#minecraft:terracotta',
        'minecraft:red_sand',
        'minecraft:clay',
        'minecraft:gravel',
        'minecraft:sand',
        'minecraft:snow_block',
        'minecraft:powder_snow',
    ],
)

BADLANDS_TERRACOTTA = Tag(
    values=[
        'minecraft:terracotta',
        'minecraft:white_terracotta',
        'minecraft:yellow_terracotta',
        'minecraft:orange_terracotta',
        'minecraft:red_terracotta',
        'minecraft:brown_terracotta',
        'minecraft:light_gray_terracotta',
    ],
)

BAMBOO_BLOCKS = Tag(values=['minecraft:bamboo_block', 'minecraft:stripped_bamboo_block'])

BANNERS = Tag(
    values=[
        'minecraft:white_banner',
        'minecraft:orange_banner',
        'minecraft:magenta_banner',
        'minecraft:light_blue_banner',
        'minecraft:yellow_banner',
        'minecraft:lime_banner',
        'minecraft:pink_banner',
        'minecraft:gray_banner',
        'minecraft:light_gray_banner',
        'minecraft:cyan_banner',
        'minecraft:purple_banner',
        'minecraft:blue_banner',
        'minecraft:brown_banner',
        'minecraft:green_banner',
        'minecraft:red_banner',
        'minecraft:black_banner',
        'minecraft:white_wall_banner',
        'minecraft:orange_wall_banner',
        'minecraft:magenta_wall_banner',
        'minecraft:light_blue_wall_banner',
        'minecraft:yellow_wall_banner',
        'minecraft:lime_wall_banner',
        'minecraft:pink_wall_banner',
        'minecraft:gray_wall_banner',
        'minecraft:light_gray_wall_banner',
        'minecraft:cyan_wall_banner',
        'minecraft:purple_wall_banner',
        'minecraft:blue_wall_banner',
        'minecraft:brown_wall_banner',
        'minecraft:green_wall_banner',
        'minecraft:red_wall_banner',
        'minecraft:black_wall_banner',
    ],
)

BARS = Tag(
    values=[
        'minecraft:iron_bars',
        'minecraft:copper_bars',
        'minecraft:exposed_copper_bars',
        'minecraft:weathered_copper_bars',
        'minecraft:oxidized_copper_bars',
        'minecraft:waxed_copper_bars',
        'minecraft:waxed_exposed_copper_bars',
        'minecraft:waxed_weathered_copper_bars',
        'minecraft:waxed_oxidized_copper_bars',
    ],
)

BASE_STONE_NETHER = Tag(values=['minecraft:netherrack', 'minecraft:basalt', 'minecraft:blackstone'])

BASE_STONE_OVERWORLD = Tag(
    values=[
        'minecraft:stone',
        'minecraft:granite',
        'minecraft:diorite',
        'minecraft:andesite',
        'minecraft:tuff',
        'minecraft:deepslate',
    ],
)

BATS_SPAWNABLE_ON = Tag(values=['#minecraft:base_stone_overworld'])

BEACON_BASE_BLOCKS = Tag(
    values=[
        'minecraft:netherite_block',
        'minecraft:emerald_block',
        'minecraft:diamond_block',
        'minecraft:gold_block',
        'minecraft:iron_block',
    ],
)

BEDS = Tag(
    values=[
        'minecraft:white_bed',
        'minecraft:orange_bed',
        'minecraft:magenta_bed',
        'minecraft:light_blue_bed',
        'minecraft:yellow_bed',
        'minecraft:lime_bed',
        'minecraft:pink_bed',
        'minecraft:gray_bed',
        'minecraft:light_gray_bed',
        'minecraft:cyan_bed',
        'minecraft:purple_bed',
        'minecraft:blue_bed',
        'minecraft:brown_bed',
        'minecraft:green_bed',
        'minecraft:red_bed',
        'minecraft:black_bed',
    ],
)

BEEHIVES = Tag(values=['minecraft:bee_nest', 'minecraft:beehive'])

BEE_ATTRACTIVE = Tag(
    values=[
        'minecraft:dandelion',
        'minecraft:open_eyeblossom',
        'minecraft:poppy',
        'minecraft:blue_orchid',
        'minecraft:allium',
        'minecraft:azure_bluet',
        'minecraft:red_tulip',
        'minecraft:orange_tulip',
        'minecraft:white_tulip',
        'minecraft:pink_tulip',
        'minecraft:oxeye_daisy',
        'minecraft:cornflower',
        'minecraft:lily_of_the_valley',
        'minecraft:wither_rose',
        'minecraft:torchflower',
        'minecraft:sunflower',
        'minecraft:lilac',
        'minecraft:peony',
        'minecraft:rose_bush',
        'minecraft:pitcher_plant',
        'minecraft:flowering_azalea_leaves',
        'minecraft:flowering_azalea',
        'minecraft:mangrove_propagule',
        'minecraft:cherry_leaves',
        'minecraft:pink_petals',
        'minecraft:wildflowers',
        'minecraft:chorus_flower',
        'minecraft:spore_blossom',
        'minecraft:cactus_flower',
    ],
)

BEE_GROWABLES = Tag(values=['#minecraft:crops', 'minecraft:sweet_berry_bush', 'minecraft:cave_vines', 'minecraft:cave_vines_plant'])

BENEATH_BAMBOO_PODZOL_REPLACEABLE = Tag(values=['#minecraft:substrate_overworld'])

BENEATH_TREE_PODZOL_REPLACEABLE = Tag(values=['#minecraft:substrate_overworld'])

BIRCH_LOGS = Tag(
    values=['minecraft:birch_log', 'minecraft:birch_wood', 'minecraft:stripped_birch_log', 'minecraft:stripped_birch_wood'],
)

BLOCKS_DOLPHIN_JUMP = Tag(values=['#minecraft:blocks_motion'])

BLOCKS_FLUID_FLOW = Tag(values=['#minecraft:blocks_motion', '#minecraft:all_signs'])

BLOCKS_LAVA_FIRE_SPREAD = Tag(values=['#minecraft:blocks_motion'])

BLOCKS_MOTION = Tag(values=['#minecraft:blocks_motion_no_leaves', '#minecraft:leaves'])

BLOCKS_MOTION_IN_HEIGHTMAP = Tag(values=['#minecraft:blocks_motion'])

BLOCKS_MOTION_IN_HEIGHTMAP_NO_LEAVES = Tag(values=['#minecraft:blocks_motion_no_leaves'])

BLOCKS_MOTION_NO_LEAVES = Tag(
    values=[
        '#minecraft:all_hanging_signs',
        '#minecraft:chains',
        '#minecraft:banners',
        '#minecraft:shulker_boxes',
        '#minecraft:lanterns',
        '#minecraft:candle_cakes',
        '#minecraft:lightning_rods',
        '#minecraft:beds',
        '#minecraft:wool',
        '#minecraft:bars',
        '#minecraft:cauldrons',
        '#minecraft:terracotta',
        '#minecraft:glazed_terracotta',
        '#minecraft:concrete',
        '#minecraft:concrete_powders',
        '#minecraft:copper',
        '#minecraft:copper_chests',
        '#minecraft:pressure_plates',
        '#minecraft:fences',
        '#minecraft:fence_gates',
        '#minecraft:walls',
        '#minecraft:coral_blocks',
        '#minecraft:planks',
        '#minecraft:logs',
        '#minecraft:bamboo_blocks',
        '#minecraft:wooden_shelves',
        '#minecraft:stairs',
        '#minecraft:slabs',
        '#minecraft:doors',
        '#minecraft:trapdoors',
        '#minecraft:ores',
        '#minecraft:speleothems',
        '#minecraft:grass_blocks',
        '#minecraft:dirt',
        '#minecraft:sand',
        '#minecraft:ice',
        '#minecraft:stone_bricks',
        '#minecraft:anvil',
        'minecraft:white_stained_glass',
        'minecraft:orange_stained_glass',
        'minecraft:magenta_stained_glass',
        'minecraft:light_blue_stained_glass',
        'minecraft:yellow_stained_glass',
        'minecraft:lime_stained_glass',
        'minecraft:pink_stained_glass',
        'minecraft:gray_stained_glass',
        'minecraft:light_gray_stained_glass',
        'minecraft:cyan_stained_glass',
        'minecraft:purple_stained_glass',
        'minecraft:blue_stained_glass',
        'minecraft:brown_stained_glass',
        'minecraft:green_stained_glass',
        'minecraft:red_stained_glass',
        'minecraft:black_stained_glass',
        'minecraft:white_stained_glass_pane',
        'minecraft:orange_stained_glass_pane',
        'minecraft:magenta_stained_glass_pane',
        'minecraft:light_blue_stained_glass_pane',
        'minecraft:yellow_stained_glass_pane',
        'minecraft:lime_stained_glass_pane',
        'minecraft:pink_stained_glass_pane',
        'minecraft:gray_stained_glass_pane',
        'minecraft:light_gray_stained_glass_pane',
        'minecraft:cyan_stained_glass_pane',
        'minecraft:purple_stained_glass_pane',
        'minecraft:blue_stained_glass_pane',
        'minecraft:brown_stained_glass_pane',
        'minecraft:green_stained_glass_pane',
        'minecraft:red_stained_glass_pane',
        'minecraft:black_stained_glass_pane',
        'minecraft:cut_copper',
        'minecraft:exposed_cut_copper',
        'minecraft:weathered_cut_copper',
        'minecraft:oxidized_cut_copper',
        'minecraft:waxed_cut_copper',
        'minecraft:waxed_exposed_cut_copper',
        'minecraft:waxed_weathered_cut_copper',
        'minecraft:waxed_oxidized_cut_copper',
        'minecraft:chiseled_copper',
        'minecraft:exposed_chiseled_copper',
        'minecraft:weathered_chiseled_copper',
        'minecraft:oxidized_chiseled_copper',
        'minecraft:waxed_chiseled_copper',
        'minecraft:waxed_exposed_chiseled_copper',
        'minecraft:waxed_weathered_chiseled_copper',
        'minecraft:waxed_oxidized_chiseled_copper',
        'minecraft:copper_grate',
        'minecraft:exposed_copper_grate',
        'minecraft:weathered_copper_grate',
        'minecraft:oxidized_copper_grate',
        'minecraft:waxed_copper_grate',
        'minecraft:waxed_exposed_copper_grate',
        'minecraft:waxed_weathered_copper_grate',
        'minecraft:waxed_oxidized_copper_grate',
        'minecraft:copper_bulb',
        'minecraft:exposed_copper_bulb',
        'minecraft:weathered_copper_bulb',
        'minecraft:oxidized_copper_bulb',
        'minecraft:waxed_copper_bulb',
        'minecraft:waxed_exposed_copper_bulb',
        'minecraft:waxed_weathered_copper_bulb',
        'minecraft:waxed_oxidized_copper_bulb',
        'minecraft:dead_tube_coral_wall_fan',
        'minecraft:dead_brain_coral_wall_fan',
        'minecraft:dead_bubble_coral_wall_fan',
        'minecraft:dead_fire_coral_wall_fan',
        'minecraft:dead_horn_coral_wall_fan',
        'minecraft:moving_piston',
        'minecraft:piston_head',
        'minecraft:cake',
        'minecraft:turtle_egg',
        'minecraft:dried_ghast',
        'minecraft:dead_tube_coral_block',
        'minecraft:dead_brain_coral_block',
        'minecraft:dead_bubble_coral_block',
        'minecraft:dead_fire_coral_block',
        'minecraft:dead_horn_coral_block',
        'minecraft:dead_tube_coral',
        'minecraft:dead_brain_coral',
        'minecraft:dead_bubble_coral',
        'minecraft:dead_fire_coral',
        'minecraft:dead_horn_coral',
        'minecraft:dead_tube_coral_fan',
        'minecraft:dead_brain_coral_fan',
        'minecraft:dead_bubble_coral_fan',
        'minecraft:dead_fire_coral_fan',
        'minecraft:dead_horn_coral_fan',
        'minecraft:conduit',
        'minecraft:bamboo',
        'minecraft:bell',
        'minecraft:amethyst_cluster',
        'minecraft:large_amethyst_bud',
        'minecraft:medium_amethyst_bud',
        'minecraft:small_amethyst_bud',
        'minecraft:sculk_vein',
        'minecraft:stone',
        'minecraft:granite',
        'minecraft:polished_granite',
        'minecraft:diorite',
        'minecraft:polished_diorite',
        'minecraft:andesite',
        'minecraft:polished_andesite',
        'minecraft:cobblestone',
        'minecraft:bamboo_mosaic',
        'minecraft:bedrock',
        'minecraft:gravel',
        'minecraft:suspicious_gravel',
        'minecraft:mangrove_roots',
        'minecraft:muddy_mangrove_roots',
        'minecraft:sponge',
        'minecraft:wet_sponge',
        'minecraft:glass',
        'minecraft:lapis_block',
        'minecraft:dispenser',
        'minecraft:sandstone',
        'minecraft:chiseled_sandstone',
        'minecraft:cut_sandstone',
        'minecraft:note_block',
        'minecraft:sticky_piston',
        'minecraft:piston',
        'minecraft:gold_block',
        'minecraft:iron_block',
        'minecraft:bricks',
        'minecraft:tnt',
        'minecraft:bookshelf',
        'minecraft:chiseled_bookshelf',
        'minecraft:mossy_cobblestone',
        'minecraft:obsidian',
        'minecraft:spawner',
        'minecraft:creaking_heart',
        'minecraft:chest',
        'minecraft:diamond_block',
        'minecraft:crafting_table',
        'minecraft:farmland',
        'minecraft:furnace',
        'minecraft:snow_block',
        'minecraft:cactus',
        'minecraft:clay',
        'minecraft:jukebox',
        'minecraft:netherrack',
        'minecraft:soul_sand',
        'minecraft:soul_soil',
        'minecraft:basalt',
        'minecraft:polished_basalt',
        'minecraft:glowstone',
        'minecraft:carved_pumpkin',
        'minecraft:jack_o_lantern',
        'minecraft:packed_mud',
        'minecraft:mud_bricks',
        'minecraft:infested_stone',
        'minecraft:infested_cobblestone',
        'minecraft:infested_stone_bricks',
        'minecraft:infested_mossy_stone_bricks',
        'minecraft:infested_cracked_stone_bricks',
        'minecraft:infested_chiseled_stone_bricks',
        'minecraft:brown_mushroom_block',
        'minecraft:red_mushroom_block',
        'minecraft:mushroom_stem',
        'minecraft:glass_pane',
        'minecraft:pumpkin',
        'minecraft:melon',
        'minecraft:resin_block',
        'minecraft:resin_bricks',
        'minecraft:chiseled_resin_bricks',
        'minecraft:nether_bricks',
        'minecraft:enchanting_table',
        'minecraft:brewing_stand',
        'minecraft:end_portal_frame',
        'minecraft:end_stone',
        'minecraft:dragon_egg',
        'minecraft:redstone_lamp',
        'minecraft:ender_chest',
        'minecraft:emerald_block',
        'minecraft:command_block',
        'minecraft:beacon',
        'minecraft:trapped_chest',
        'minecraft:daylight_detector',
        'minecraft:redstone_block',
        'minecraft:hopper',
        'minecraft:quartz_block',
        'minecraft:chiseled_quartz_block',
        'minecraft:quartz_pillar',
        'minecraft:dropper',
        'minecraft:slime_block',
        'minecraft:barrier',
        'minecraft:prismarine',
        'minecraft:prismarine_bricks',
        'minecraft:dark_prismarine',
        'minecraft:sea_lantern',
        'minecraft:hay_block',
        'minecraft:coal_block',
        'minecraft:red_sandstone',
        'minecraft:chiseled_red_sandstone',
        'minecraft:cut_red_sandstone',
        'minecraft:smooth_stone',
        'minecraft:smooth_sandstone',
        'minecraft:smooth_quartz',
        'minecraft:smooth_red_sandstone',
        'minecraft:purpur_block',
        'minecraft:purpur_pillar',
        'minecraft:end_stone_bricks',
        'minecraft:dirt_path',
        'minecraft:repeating_command_block',
        'minecraft:chain_command_block',
        'minecraft:magma_block',
        'minecraft:nether_wart_block',
        'minecraft:red_nether_bricks',
        'minecraft:bone_block',
        'minecraft:observer',
        'minecraft:dried_kelp_block',
        'minecraft:sniffer_egg',
        'minecraft:loom',
        'minecraft:barrel',
        'minecraft:smoker',
        'minecraft:blast_furnace',
        'minecraft:cartography_table',
        'minecraft:fletching_table',
        'minecraft:grindstone',
        'minecraft:lectern',
        'minecraft:smithing_table',
        'minecraft:stonecutter',
        'minecraft:campfire',
        'minecraft:soul_campfire',
        'minecraft:warped_nylium',
        'minecraft:warped_wart_block',
        'minecraft:crimson_nylium',
        'minecraft:shroomlight',
        'minecraft:structure_block',
        'minecraft:jigsaw',
        'minecraft:test_block',
        'minecraft:test_instance_block',
        'minecraft:composter',
        'minecraft:target',
        'minecraft:bee_nest',
        'minecraft:beehive',
        'minecraft:honey_block',
        'minecraft:honeycomb_block',
        'minecraft:netherite_block',
        'minecraft:ancient_debris',
        'minecraft:crying_obsidian',
        'minecraft:respawn_anchor',
        'minecraft:lodestone',
        'minecraft:blackstone',
        'minecraft:polished_blackstone',
        'minecraft:polished_blackstone_bricks',
        'minecraft:cracked_polished_blackstone_bricks',
        'minecraft:chiseled_polished_blackstone',
        'minecraft:gilded_blackstone',
        'minecraft:chiseled_nether_bricks',
        'minecraft:cracked_nether_bricks',
        'minecraft:quartz_bricks',
        'minecraft:amethyst_block',
        'minecraft:budding_amethyst',
        'minecraft:tuff',
        'minecraft:polished_tuff',
        'minecraft:chiseled_tuff',
        'minecraft:tuff_bricks',
        'minecraft:chiseled_tuff_bricks',
        'minecraft:sulfur',
        'minecraft:potent_sulfur',
        'minecraft:polished_sulfur',
        'minecraft:sulfur_bricks',
        'minecraft:chiseled_sulfur',
        'minecraft:cinnabar',
        'minecraft:polished_cinnabar',
        'minecraft:cinnabar_bricks',
        'minecraft:chiseled_cinnabar',
        'minecraft:calcite',
        'minecraft:tinted_glass',
        'minecraft:sculk_sensor',
        'minecraft:calibrated_sculk_sensor',
        'minecraft:sculk',
        'minecraft:sculk_catalyst',
        'minecraft:sculk_shrieker',
        'minecraft:dripstone_block',
        'minecraft:moss_block',
        'minecraft:mud',
        'minecraft:deepslate',
        'minecraft:cobbled_deepslate',
        'minecraft:polished_deepslate',
        'minecraft:deepslate_tiles',
        'minecraft:deepslate_bricks',
        'minecraft:chiseled_deepslate',
        'minecraft:cracked_deepslate_bricks',
        'minecraft:cracked_deepslate_tiles',
        'minecraft:infested_deepslate',
        'minecraft:smooth_basalt',
        'minecraft:raw_iron_block',
        'minecraft:raw_copper_block',
        'minecraft:raw_gold_block',
        'minecraft:ochre_froglight',
        'minecraft:verdant_froglight',
        'minecraft:pearlescent_froglight',
        'minecraft:reinforced_deepslate',
        'minecraft:decorated_pot',
        'minecraft:crafter',
        'minecraft:trial_spawner',
        'minecraft:vault',
        'minecraft:pale_moss_block',
        'minecraft:straw_bed',
    ],
)

BLOCKS_WIND_CHARGE_EXPLOSIONS = Tag(values=['minecraft:barrier', 'minecraft:bedrock'])

BUTTONS = Tag(values=['#minecraft:wooden_buttons', '#minecraft:stone_buttons'])

CAMELS_SPAWNABLE_ON = Tag(values=['#minecraft:sand'])

CAMEL_SAND_STEP_SOUND_BLOCKS = Tag(values=['#minecraft:sand', '#minecraft:concrete_powders'])

CAMPFIRES = Tag(values=['minecraft:campfire', 'minecraft:soul_campfire'])

CANDLES = Tag(
    values=[
        'minecraft:candle',
        'minecraft:white_candle',
        'minecraft:orange_candle',
        'minecraft:magenta_candle',
        'minecraft:light_blue_candle',
        'minecraft:yellow_candle',
        'minecraft:lime_candle',
        'minecraft:pink_candle',
        'minecraft:gray_candle',
        'minecraft:light_gray_candle',
        'minecraft:cyan_candle',
        'minecraft:purple_candle',
        'minecraft:blue_candle',
        'minecraft:brown_candle',
        'minecraft:green_candle',
        'minecraft:red_candle',
        'minecraft:black_candle',
    ],
)

CANDLE_CAKES = Tag(
    values=[
        'minecraft:candle_cake',
        'minecraft:white_candle_cake',
        'minecraft:orange_candle_cake',
        'minecraft:magenta_candle_cake',
        'minecraft:light_blue_candle_cake',
        'minecraft:yellow_candle_cake',
        'minecraft:lime_candle_cake',
        'minecraft:pink_candle_cake',
        'minecraft:gray_candle_cake',
        'minecraft:light_gray_candle_cake',
        'minecraft:cyan_candle_cake',
        'minecraft:purple_candle_cake',
        'minecraft:blue_candle_cake',
        'minecraft:brown_candle_cake',
        'minecraft:green_candle_cake',
        'minecraft:red_candle_cake',
        'minecraft:black_candle_cake',
    ],
)

CANNOT_PLACE_BASALT_PILLAR_ON = Tag(
    values=[
        'minecraft:lava',
        'minecraft:bedrock',
        'minecraft:magma_block',
        'minecraft:soul_sand',
        'minecraft:nether_bricks',
        'minecraft:nether_brick_fence',
        'minecraft:nether_brick_stairs',
        'minecraft:nether_wart',
        'minecraft:chest',
        'minecraft:spawner',
    ],
)

CANNOT_REPLACE_BELOW_TREE_TRUNK = Tag(values=['#minecraft:dirt', '#minecraft:mud', '#minecraft:moss_blocks', 'minecraft:podzol'])

CANNOT_SUPPORT_KELP = Tag(values=['minecraft:magma_block'])

CANNOT_SUPPORT_SEAGRASS = Tag(values=['minecraft:magma_block'])

CANNOT_SUPPORT_SNOW_LAYER = Tag(values=['minecraft:ice', 'minecraft:barrier'])

CAN_GLIDE_THROUGH = Tag(
    values=[
        'minecraft:vine',
        'minecraft:twisting_vines',
        'minecraft:twisting_vines_plant',
        'minecraft:weeping_vines',
        'minecraft:weeping_vines_plant',
        '#minecraft:cave_vines',
    ],
)

CATS_CAN_LIE_ON = Tag(values=['#minecraft:beds'])

CATS_CAN_SIT_ON = Tag(values=['minecraft:furnace', 'minecraft:chest', '#minecraft:beds'])

CAT_DOES_NOT_TELEPORT_TO = Tag(values=['#minecraft:dangerous_for_teleportation'])

CAULDRONS = Tag(
    values=['minecraft:cauldron', 'minecraft:water_cauldron', 'minecraft:lava_cauldron', 'minecraft:powder_snow_cauldron'],
)

CAUSES_CONTINUOUS_GEYSER_ERUPTIONS = Tag(values=['minecraft:lava'])

CAUSES_PERIODIC_GEYSER_ERUPTIONS = Tag(values=['minecraft:magma_block'])

CAUSES_SUFFOCATION = Tag(values=['#minecraft:blocks_motion'])

CAVE_VINES = Tag(values=['minecraft:cave_vines_plant', 'minecraft:cave_vines'])

CEILING_HANGING_SIGNS = Tag(
    values=[
        'minecraft:oak_hanging_sign',
        'minecraft:spruce_hanging_sign',
        'minecraft:birch_hanging_sign',
        'minecraft:acacia_hanging_sign',
        'minecraft:cherry_hanging_sign',
        'minecraft:jungle_hanging_sign',
        'minecraft:dark_oak_hanging_sign',
        'minecraft:pale_oak_hanging_sign',
        'minecraft:crimson_hanging_sign',
        'minecraft:warped_hanging_sign',
        'minecraft:mangrove_hanging_sign',
        'minecraft:poplar_hanging_sign',
        'minecraft:bamboo_hanging_sign',
    ],
)

CHAINS = Tag(
    values=[
        'minecraft:iron_chain',
        'minecraft:copper_chain',
        'minecraft:exposed_copper_chain',
        'minecraft:weathered_copper_chain',
        'minecraft:oxidized_copper_chain',
        'minecraft:waxed_copper_chain',
        'minecraft:waxed_exposed_copper_chain',
        'minecraft:waxed_weathered_copper_chain',
        'minecraft:waxed_oxidized_copper_chain',
    ],
)

CHERRY_LOGS = Tag(
    values=['minecraft:cherry_log', 'minecraft:cherry_wood', 'minecraft:stripped_cherry_log', 'minecraft:stripped_cherry_wood'],
)

CLIMBABLE = Tag(
    values=[
        'minecraft:ladder',
        'minecraft:vine',
        'minecraft:scaffolding',
        'minecraft:weeping_vines',
        'minecraft:weeping_vines_plant',
        'minecraft:twisting_vines',
        'minecraft:twisting_vines_plant',
        'minecraft:cave_vines',
        'minecraft:cave_vines_plant',
    ],
)

COAL_ORES = Tag(values=['minecraft:coal_ore', 'minecraft:deepslate_coal_ore'])

COMBINATION_STEP_SOUND_BLOCKS = Tag(
    values=[
        '#minecraft:wool_carpets',
        'minecraft:moss_carpet',
        'minecraft:pale_moss_carpet',
        'minecraft:snow',
        'minecraft:nether_sprouts',
        'minecraft:warped_roots',
        'minecraft:crimson_roots',
        'minecraft:resin_clump',
    ],
)

COMPLETES_FIND_TREE_TUTORIAL = Tag(values=['#minecraft:logs', '#minecraft:leaves', '#minecraft:wart_blocks'])

CONCRETE = Tag(
    values=[
        'minecraft:white_concrete',
        'minecraft:orange_concrete',
        'minecraft:magenta_concrete',
        'minecraft:light_blue_concrete',
        'minecraft:yellow_concrete',
        'minecraft:lime_concrete',
        'minecraft:pink_concrete',
        'minecraft:gray_concrete',
        'minecraft:light_gray_concrete',
        'minecraft:cyan_concrete',
        'minecraft:purple_concrete',
        'minecraft:blue_concrete',
        'minecraft:brown_concrete',
        'minecraft:green_concrete',
        'minecraft:red_concrete',
        'minecraft:black_concrete',
    ],
)

CONCRETE_POWDERS = Tag(
    values=[
        'minecraft:white_concrete_powder',
        'minecraft:orange_concrete_powder',
        'minecraft:magenta_concrete_powder',
        'minecraft:light_blue_concrete_powder',
        'minecraft:yellow_concrete_powder',
        'minecraft:lime_concrete_powder',
        'minecraft:pink_concrete_powder',
        'minecraft:gray_concrete_powder',
        'minecraft:light_gray_concrete_powder',
        'minecraft:cyan_concrete_powder',
        'minecraft:purple_concrete_powder',
        'minecraft:blue_concrete_powder',
        'minecraft:brown_concrete_powder',
        'minecraft:green_concrete_powder',
        'minecraft:red_concrete_powder',
        'minecraft:black_concrete_powder',
    ],
)

CONCRETE_SLABS = Tag(
    values=[
        'minecraft:white_concrete_slab',
        'minecraft:orange_concrete_slab',
        'minecraft:magenta_concrete_slab',
        'minecraft:light_blue_concrete_slab',
        'minecraft:yellow_concrete_slab',
        'minecraft:lime_concrete_slab',
        'minecraft:pink_concrete_slab',
        'minecraft:gray_concrete_slab',
        'minecraft:light_gray_concrete_slab',
        'minecraft:cyan_concrete_slab',
        'minecraft:purple_concrete_slab',
        'minecraft:blue_concrete_slab',
        'minecraft:brown_concrete_slab',
        'minecraft:green_concrete_slab',
        'minecraft:red_concrete_slab',
        'minecraft:black_concrete_slab',
    ],
)

CONCRETE_STAIRS = Tag(
    values=[
        'minecraft:white_concrete_stairs',
        'minecraft:orange_concrete_stairs',
        'minecraft:magenta_concrete_stairs',
        'minecraft:light_blue_concrete_stairs',
        'minecraft:yellow_concrete_stairs',
        'minecraft:lime_concrete_stairs',
        'minecraft:pink_concrete_stairs',
        'minecraft:gray_concrete_stairs',
        'minecraft:light_gray_concrete_stairs',
        'minecraft:cyan_concrete_stairs',
        'minecraft:purple_concrete_stairs',
        'minecraft:blue_concrete_stairs',
        'minecraft:brown_concrete_stairs',
        'minecraft:green_concrete_stairs',
        'minecraft:red_concrete_stairs',
        'minecraft:black_concrete_stairs',
    ],
)

CONDUIT_EFFECT_BLOCK = Tag(
    values=['minecraft:prismarine', 'minecraft:prismarine_bricks', 'minecraft:sea_lantern', 'minecraft:dark_prismarine'],
)

CONVERTIBLE_TO_MUD = Tag(values=['minecraft:dirt', 'minecraft:coarse_dirt', 'minecraft:rooted_dirt'])

COPPER = Tag(
    values=[
        'minecraft:copper_block',
        'minecraft:exposed_copper',
        'minecraft:weathered_copper',
        'minecraft:oxidized_copper',
        'minecraft:waxed_copper_block',
        'minecraft:waxed_exposed_copper',
        'minecraft:waxed_weathered_copper',
        'minecraft:waxed_oxidized_copper',
    ],
)

COPPER_CHESTS = Tag(
    values=[
        'minecraft:copper_chest',
        'minecraft:exposed_copper_chest',
        'minecraft:weathered_copper_chest',
        'minecraft:oxidized_copper_chest',
        'minecraft:waxed_copper_chest',
        'minecraft:waxed_exposed_copper_chest',
        'minecraft:waxed_weathered_copper_chest',
        'minecraft:waxed_oxidized_copper_chest',
    ],
)

COPPER_GOLEM_STATUES = Tag(
    values=[
        'minecraft:copper_golem_statue',
        'minecraft:exposed_copper_golem_statue',
        'minecraft:weathered_copper_golem_statue',
        'minecraft:oxidized_copper_golem_statue',
        'minecraft:waxed_copper_golem_statue',
        'minecraft:waxed_exposed_copper_golem_statue',
        'minecraft:waxed_weathered_copper_golem_statue',
        'minecraft:waxed_oxidized_copper_golem_statue',
    ],
)

COPPER_ORES = Tag(values=['minecraft:copper_ore', 'minecraft:deepslate_copper_ore'])

CORALS = Tag(
    values=[
        '#minecraft:coral_plants',
        'minecraft:tube_coral_fan',
        'minecraft:brain_coral_fan',
        'minecraft:bubble_coral_fan',
        'minecraft:fire_coral_fan',
        'minecraft:horn_coral_fan',
    ],
)

CORAL_BLOCKS = Tag(
    values=[
        'minecraft:tube_coral_block',
        'minecraft:brain_coral_block',
        'minecraft:bubble_coral_block',
        'minecraft:fire_coral_block',
        'minecraft:horn_coral_block',
    ],
)

CORAL_PLANTS = Tag(
    values=[
        'minecraft:tube_coral',
        'minecraft:brain_coral',
        'minecraft:bubble_coral',
        'minecraft:fire_coral',
        'minecraft:horn_coral',
    ],
)

CRIMSON_STEMS = Tag(
    values=[
        'minecraft:crimson_stem',
        'minecraft:stripped_crimson_stem',
        'minecraft:crimson_hyphae',
        'minecraft:stripped_crimson_hyphae',
    ],
)

CROPS = Tag(
    values=[
        'minecraft:beetroots',
        'minecraft:carrots',
        'minecraft:potatoes',
        'minecraft:wheat',
        'minecraft:melon_stem',
        'minecraft:pumpkin_stem',
        'minecraft:torchflower_crop',
        'minecraft:pitcher_crop',
    ],
)

CRYSTAL_SOUND_BLOCKS = Tag(values=['minecraft:amethyst_block', 'minecraft:budding_amethyst'])

CUSHION_USES_COLLISION_SHAPE = Tag(values=['#minecraft:cauldrons', 'minecraft:hopper', 'minecraft:composter'])

DAMPENS_VIBRATIONS = Tag(values=['#minecraft:wool', '#minecraft:wool_carpets', '#minecraft:wool_slabs', '#minecraft:wool_stairs'])

DANGEROUS_FOR_TELEPORTATION = Tag(
    values=[
        'minecraft:fire',
        'minecraft:soul_fire',
        'minecraft:lava_cauldron',
        'minecraft:campfire',
        'minecraft:soul_campfire',
        'minecraft:cactus',
        'minecraft:magma_block',
        'minecraft:sweet_berry_bush',
        'minecraft:wither_rose',
        'minecraft:pointed_dripstone',
        'minecraft:powder_snow',
    ],
)

DARK_OAK_LOGS = Tag(
    values=[
        'minecraft:dark_oak_log',
        'minecraft:dark_oak_wood',
        'minecraft:stripped_dark_oak_log',
        'minecraft:stripped_dark_oak_wood',
    ],
)

DEEPSLATE_ORE_REPLACEABLES = Tag(values=['minecraft:deepslate'])

DEFAULT_IMMUNE_TO = Tag(values=[])

DIAMOND_ORES = Tag(values=['minecraft:diamond_ore', 'minecraft:deepslate_diamond_ore'])

DIRT = Tag(values=['minecraft:dirt', 'minecraft:coarse_dirt', 'minecraft:rooted_dirt'])

DOES_NOT_BLOCK_HOPPERS = Tag(values=['#minecraft:beehives'])

DOORS = Tag(
    values=[
        '#minecraft:wooden_doors',
        'minecraft:copper_door',
        'minecraft:exposed_copper_door',
        'minecraft:weathered_copper_door',
        'minecraft:oxidized_copper_door',
        'minecraft:waxed_copper_door',
        'minecraft:waxed_exposed_copper_door',
        'minecraft:waxed_weathered_copper_door',
        'minecraft:waxed_oxidized_copper_door',
        'minecraft:iron_door',
    ],
)

DRAGON_IMMUNE = Tag(
    values=[
        'minecraft:barrier',
        'minecraft:bedrock',
        'minecraft:end_portal',
        'minecraft:end_portal_frame',
        'minecraft:end_gateway',
        'minecraft:command_block',
        'minecraft:repeating_command_block',
        'minecraft:chain_command_block',
        'minecraft:structure_block',
        'minecraft:jigsaw',
        'minecraft:moving_piston',
        'minecraft:obsidian',
        'minecraft:crying_obsidian',
        'minecraft:end_stone',
        'minecraft:iron_bars',
        'minecraft:respawn_anchor',
        'minecraft:reinforced_deepslate',
        'minecraft:test_block',
        'minecraft:test_instance_block',
    ],
)

DRAGON_TRANSPARENT = Tag(values=['minecraft:light', '#minecraft:fire'])

DRIPSTONE_REPLACEABLE_BLOCKS = Tag(values=['#minecraft:base_stone_overworld'])

EDIBLE_FOR_SHEEP = Tag(values=['minecraft:short_grass', 'minecraft:short_dry_grass', 'minecraft:tall_dry_grass', 'minecraft:fern'])

EMERALD_ORES = Tag(values=['minecraft:emerald_ore', 'minecraft:deepslate_emerald_ore'])

ENABLES_BUBBLE_COLUMN_DRAG_DOWN = Tag(values=['minecraft:magma_block'])

ENABLES_BUBBLE_COLUMN_PUSH_UP = Tag(values=['minecraft:soul_sand'])

ENCHANTMENT_POWER_PROVIDER = Tag(values=['minecraft:bookshelf'])

ENCHANTMENT_POWER_TRANSMITTER = Tag(values=['#minecraft:replaceable'])

ENDERMAN_DOES_NOT_TELEPORT_TO = Tag(values=['#minecraft:dangerous_for_teleportation', 'minecraft:bedrock'])

ENDERMAN_HOLDABLE = Tag(
    values=[
        '#minecraft:small_flowers',
        '#minecraft:dirt',
        '#minecraft:mud',
        '#minecraft:moss_blocks',
        '#minecraft:grass_blocks',
        'minecraft:sand',
        'minecraft:red_sand',
        'minecraft:gravel',
        'minecraft:brown_mushroom',
        'minecraft:red_mushroom',
        'minecraft:tnt',
        'minecraft:cactus',
        'minecraft:clay',
        'minecraft:pumpkin',
        'minecraft:carved_pumpkin',
        'minecraft:melon',
        'minecraft:crimson_fungus',
        'minecraft:crimson_nylium',
        'minecraft:crimson_roots',
        'minecraft:warped_fungus',
        'minecraft:warped_nylium',
        'minecraft:warped_roots',
        'minecraft:cactus_flower',
    ],
)

ENTITIES_CAN_TELEPORT_TO = Tag(values=['#minecraft:blocks_motion'])

FACE_OCCLUDING_ICE_BLOCKS = Tag(values=['minecraft:ice', 'minecraft:brittle_ice', 'minecraft:frosted_ice'])

FALL_DAMAGE_RESETTING = Tag(values=['#minecraft:climbable', 'minecraft:sweet_berry_bush', 'minecraft:cobweb'])

FEATURES_CANNOT_REPLACE = Tag(
    values=[
        'minecraft:bedrock',
        'minecraft:spawner',
        'minecraft:chest',
        'minecraft:end_portal_frame',
        'minecraft:reinforced_deepslate',
        'minecraft:trial_spawner',
        'minecraft:vault',
    ],
)

FENCES = Tag(values=['#minecraft:wooden_fences', 'minecraft:nether_brick_fence'])

FENCE_GATES = Tag(
    values=[
        'minecraft:acacia_fence_gate',
        'minecraft:birch_fence_gate',
        'minecraft:dark_oak_fence_gate',
        'minecraft:pale_oak_fence_gate',
        'minecraft:jungle_fence_gate',
        'minecraft:oak_fence_gate',
        'minecraft:spruce_fence_gate',
        'minecraft:crimson_fence_gate',
        'minecraft:warped_fence_gate',
        'minecraft:mangrove_fence_gate',
        'minecraft:bamboo_fence_gate',
        'minecraft:cherry_fence_gate',
        'minecraft:poplar_fence_gate',
    ],
)

FIRE = Tag(values=['minecraft:fire', 'minecraft:soul_fire'])

FLOWERS = Tag(
    values=[
        '#minecraft:small_flowers',
        'minecraft:sunflower',
        'minecraft:lilac',
        'minecraft:peony',
        'minecraft:rose_bush',
        'minecraft:pitcher_plant',
        'minecraft:flowering_azalea_leaves',
        'minecraft:flowering_azalea',
        'minecraft:mangrove_propagule',
        'minecraft:cherry_leaves',
        'minecraft:pink_petals',
        'minecraft:wildflowers',
        'minecraft:chorus_flower',
        'minecraft:spore_blossom',
        'minecraft:cactus_flower',
    ],
)

FLOWER_POTS = Tag(
    values=[
        'minecraft:flower_pot',
        'minecraft:potted_open_eyeblossom',
        'minecraft:potted_closed_eyeblossom',
        'minecraft:potted_poppy',
        'minecraft:potted_blue_orchid',
        'minecraft:potted_allium',
        'minecraft:potted_azure_bluet',
        'minecraft:potted_red_tulip',
        'minecraft:potted_orange_tulip',
        'minecraft:potted_white_tulip',
        'minecraft:potted_pink_tulip',
        'minecraft:potted_oxeye_daisy',
        'minecraft:potted_dandelion',
        'minecraft:potted_oak_sapling',
        'minecraft:potted_spruce_sapling',
        'minecraft:potted_birch_sapling',
        'minecraft:potted_jungle_sapling',
        'minecraft:potted_acacia_sapling',
        'minecraft:potted_dark_oak_sapling',
        'minecraft:potted_pale_oak_sapling',
        'minecraft:potted_red_mushroom',
        'minecraft:potted_brown_mushroom',
        'minecraft:potted_dead_bush',
        'minecraft:potted_fern',
        'minecraft:potted_cactus',
        'minecraft:potted_cornflower',
        'minecraft:potted_lily_of_the_valley',
        'minecraft:potted_wither_rose',
        'minecraft:potted_bamboo',
        'minecraft:potted_crimson_fungus',
        'minecraft:potted_warped_fungus',
        'minecraft:potted_crimson_roots',
        'minecraft:potted_warped_roots',
        'minecraft:potted_azalea_bush',
        'minecraft:potted_flowering_azalea_bush',
        'minecraft:potted_mangrove_propagule',
        'minecraft:potted_cherry_sapling',
        'minecraft:potted_torchflower',
        'minecraft:potted_golden_dandelion',
        'minecraft:potted_poplar_sapling',
    ],
)

FOREST_ROCK_CAN_PLACE_ON = Tag(values=['#minecraft:substrate_overworld', '#minecraft:base_stone_overworld'])

FOXES_SPAWNABLE_ON = Tag(
    values=['minecraft:grass_block', 'minecraft:snow', 'minecraft:snow_block', 'minecraft:podzol', 'minecraft:coarse_dirt'],
)

FOX_IMMUNE_TO = Tag(values=['minecraft:sweet_berry_bush'])

FROGS_SPAWNABLE_ON = Tag(values=['minecraft:grass_block', 'minecraft:mud', 'minecraft:mangrove_roots', 'minecraft:muddy_mangrove_roots'])

FROG_PREFER_JUMP_TO = Tag(values=['minecraft:lily_pad', 'minecraft:big_dripleaf'])

GEODE_INVALID_BLOCKS = Tag(
    values=[
        'minecraft:bedrock',
        'minecraft:water',
        'minecraft:lava',
        'minecraft:ice',
        'minecraft:packed_ice',
        'minecraft:blue_ice',
    ],
)

GLAZED_TERRACOTTA = Tag(
    values=[
        'minecraft:white_glazed_terracotta',
        'minecraft:orange_glazed_terracotta',
        'minecraft:magenta_glazed_terracotta',
        'minecraft:light_blue_glazed_terracotta',
        'minecraft:yellow_glazed_terracotta',
        'minecraft:lime_glazed_terracotta',
        'minecraft:pink_glazed_terracotta',
        'minecraft:gray_glazed_terracotta',
        'minecraft:light_gray_glazed_terracotta',
        'minecraft:cyan_glazed_terracotta',
        'minecraft:purple_glazed_terracotta',
        'minecraft:blue_glazed_terracotta',
        'minecraft:brown_glazed_terracotta',
        'minecraft:green_glazed_terracotta',
        'minecraft:red_glazed_terracotta',
        'minecraft:black_glazed_terracotta',
    ],
)

GOATS_SPAWNABLE_ON = Tag(
    values=[
        '#minecraft:animals_spawnable_on',
        'minecraft:stone',
        'minecraft:snow',
        'minecraft:snow_block',
        'minecraft:packed_ice',
        'minecraft:gravel',
    ],
)

GOLD_ORES = Tag(values=['minecraft:gold_ore', 'minecraft:nether_gold_ore', 'minecraft:deepslate_gold_ore'])

GRASS_BLOCKS = Tag(values=['minecraft:grass_block', 'minecraft:podzol', 'minecraft:mycelium'])

GROWS_CROPS = Tag(values=['minecraft:farmland'])

GUARDED_BY_PIGLINS = Tag(
    values=[
        '#minecraft:copper_chests',
        'minecraft:gold_block',
        'minecraft:barrel',
        'minecraft:chest',
        'minecraft:ender_chest',
        'minecraft:gilded_blackstone',
        'minecraft:trapped_chest',
        'minecraft:raw_gold_block',
        '#minecraft:shulker_boxes',
        '#minecraft:gold_ores',
    ],
)

HAPPY_GHAST_AVOIDS = Tag(
    values=[
        'minecraft:sweet_berry_bush',
        'minecraft:cactus',
        'minecraft:wither_rose',
        'minecraft:magma_block',
        'minecraft:fire',
        '#minecraft:speleothems',
    ],
)

HEIGHT_SPECIFIC_ORE_REPLACEABLES = Tag(values=['minecraft:tuff'])

HOGLIN_REPELLENTS = Tag(
    values=['minecraft:warped_fungus', 'minecraft:potted_warped_fungus', 'minecraft:nether_portal', 'minecraft:respawn_anchor'],
)

HUGE_BROWN_MUSHROOM_CAN_PLACE_ON = Tag(
    values=[
        '#minecraft:substrate_overworld',
        'minecraft:mycelium',
        'minecraft:podzol',
        'minecraft:crimson_nylium',
        'minecraft:warped_nylium',
    ],
)

HUGE_RED_MUSHROOM_CAN_PLACE_ON = Tag(
    values=[
        '#minecraft:substrate_overworld',
        'minecraft:mycelium',
        'minecraft:podzol',
        'minecraft:crimson_nylium',
        'minecraft:warped_nylium',
    ],
)

ICE = Tag(
    values=['minecraft:ice', 'minecraft:packed_ice', 'minecraft:blue_ice', 'minecraft:brittle_ice', 'minecraft:frosted_ice'],
)

ICE_CAVE_ORE_REPLACEABLES = Tag(values=['minecraft:calcite', 'minecraft:packed_ice'])

ICE_CREVASSE_REPLACEABLES = Tag(
    values=[
        '#minecraft:stone_ore_replaceables',
        '#minecraft:deepslate_ore_replaceables',
        '#minecraft:height_specific_ore_replaceables',
        '#minecraft:ice_cave_ore_replaceables',
    ],
)

ICE_MELTS_WHEN_DESTROYED_ABOVE = Tag(values=['#minecraft:blocks_motion'])

ICE_SPIKE_REPLACEABLE = Tag(values=['#minecraft:substrate_overworld', 'minecraft:snow_block', 'minecraft:ice'])

IMPERMEABLE = Tag(
    values=[
        'minecraft:white_stained_glass',
        'minecraft:orange_stained_glass',
        'minecraft:magenta_stained_glass',
        'minecraft:light_blue_stained_glass',
        'minecraft:yellow_stained_glass',
        'minecraft:lime_stained_glass',
        'minecraft:pink_stained_glass',
        'minecraft:gray_stained_glass',
        'minecraft:light_gray_stained_glass',
        'minecraft:cyan_stained_glass',
        'minecraft:purple_stained_glass',
        'minecraft:blue_stained_glass',
        'minecraft:brown_stained_glass',
        'minecraft:green_stained_glass',
        'minecraft:red_stained_glass',
        'minecraft:black_stained_glass',
        'minecraft:glass',
        'minecraft:tinted_glass',
        'minecraft:barrier',
    ],
)

INCORRECT_FOR_COPPER_TOOL = Tag(values=['#minecraft:needs_diamond_tool', '#minecraft:needs_iron_tool'])

INCORRECT_FOR_DIAMOND_TOOL = Tag(values=[])

INCORRECT_FOR_GOLD_TOOL = Tag(values=['#minecraft:needs_diamond_tool', '#minecraft:needs_iron_tool', '#minecraft:needs_stone_tool'])

INCORRECT_FOR_IRON_TOOL = Tag(values=['#minecraft:needs_diamond_tool'])

INCORRECT_FOR_NETHERITE_TOOL = Tag(values=[])

INCORRECT_FOR_STONE_TOOL = Tag(values=['#minecraft:needs_diamond_tool', '#minecraft:needs_iron_tool'])

INCORRECT_FOR_WOODEN_TOOL = Tag(values=['#minecraft:needs_diamond_tool', '#minecraft:needs_iron_tool', '#minecraft:needs_stone_tool'])

INFINIBURN_END = Tag(values=['#minecraft:infiniburn_overworld', 'minecraft:bedrock'])

INFINIBURN_NETHER = Tag(values=['#minecraft:infiniburn_overworld'])

INFINIBURN_OVERWORLD = Tag(values=['minecraft:netherrack', 'minecraft:magma_block'])

INSIDE_STEP_SOUND_BLOCKS = Tag(
    values=[
        'minecraft:powder_snow',
        'minecraft:sculk_vein',
        'minecraft:glow_lichen',
        'minecraft:lily_pad',
        'minecraft:small_amethyst_bud',
        'minecraft:pink_petals',
        'minecraft:wildflowers',
        'minecraft:leaf_litter',
    ],
)

INVALID_SPAWN_INSIDE = Tag(values=['minecraft:end_portal', 'minecraft:end_gateway'])

IRON_ORES = Tag(values=['minecraft:iron_ore', 'minecraft:deepslate_iron_ore'])

JUKEBOX_CONTAINERS = Tag(
    values=[
        'minecraft:chest',
        'minecraft:trapped_chest',
        'minecraft:copper_chest',
        'minecraft:exposed_copper_chest',
        'minecraft:weathered_copper_chest',
        'minecraft:oxidized_copper_chest',
        'minecraft:waxed_copper_chest',
        'minecraft:waxed_exposed_copper_chest',
        'minecraft:waxed_weathered_copper_chest',
        'minecraft:waxed_oxidized_copper_chest',
    ],
)

JUNGLE_LOGS = Tag(
    values=['minecraft:jungle_log', 'minecraft:jungle_wood', 'minecraft:stripped_jungle_log', 'minecraft:stripped_jungle_wood'],
)

LANTERNS = Tag(
    values=[
        'minecraft:lantern',
        'minecraft:soul_lantern',
        'minecraft:copper_lantern',
        'minecraft:exposed_copper_lantern',
        'minecraft:weathered_copper_lantern',
        'minecraft:oxidized_copper_lantern',
        'minecraft:waxed_copper_lantern',
        'minecraft:waxed_exposed_copper_lantern',
        'minecraft:waxed_weathered_copper_lantern',
        'minecraft:waxed_oxidized_copper_lantern',
    ],
)

LAPIS_ORES = Tag(values=['minecraft:lapis_ore', 'minecraft:deepslate_lapis_ore'])

LARGE_ICICLE_REPLACEABLE = Tag(values=['minecraft:calcite', 'minecraft:stone', 'minecraft:deepslate', 'minecraft:packed_ice'])

LAVA_POOL_STONE_CANNOT_REPLACE = Tag(values=['#minecraft:features_cannot_replace', '#minecraft:leaves', '#minecraft:logs'])

LEAVES = Tag(
    values=[
        'minecraft:jungle_leaves',
        'minecraft:oak_leaves',
        'minecraft:spruce_leaves',
        'minecraft:pale_oak_leaves',
        'minecraft:dark_oak_leaves',
        'minecraft:acacia_leaves',
        'minecraft:birch_leaves',
        'minecraft:azalea_leaves',
        'minecraft:flowering_azalea_leaves',
        'minecraft:mangrove_leaves',
        'minecraft:cherry_leaves',
        'minecraft:red_poplar_leaves',
        'minecraft:orange_poplar_leaves',
        'minecraft:yellow_poplar_leaves',
    ],
)

LIGHTNING_RODS = Tag(
    values=[
        'minecraft:lightning_rod',
        'minecraft:exposed_lightning_rod',
        'minecraft:weathered_lightning_rod',
        'minecraft:oxidized_lightning_rod',
        'minecraft:waxed_lightning_rod',
        'minecraft:waxed_exposed_lightning_rod',
        'minecraft:waxed_weathered_lightning_rod',
        'minecraft:waxed_oxidized_lightning_rod',
    ],
)

LOGS = Tag(values=['#minecraft:logs_that_burn', '#minecraft:crimson_stems', '#minecraft:warped_stems'])

LOGS_THAT_BURN = Tag(
    values=[
        '#minecraft:dark_oak_logs',
        '#minecraft:pale_oak_logs',
        '#minecraft:oak_logs',
        '#minecraft:acacia_logs',
        '#minecraft:birch_logs',
        '#minecraft:jungle_logs',
        '#minecraft:spruce_logs',
        '#minecraft:mangrove_logs',
        '#minecraft:cherry_logs',
        '#minecraft:poplar_logs',
    ],
)

LUSH_GROUND_REPLACEABLE = Tag(values=['#minecraft:moss_replaceable', 'minecraft:clay', 'minecraft:gravel', 'minecraft:sand'])

MAINTAINS_FARMLAND = Tag(
    values=[
        'minecraft:pumpkin_stem',
        'minecraft:attached_pumpkin_stem',
        'minecraft:melon_stem',
        'minecraft:attached_melon_stem',
        'minecraft:beetroots',
        'minecraft:carrots',
        'minecraft:potatoes',
        'minecraft:torchflower_crop',
        'minecraft:torchflower',
        'minecraft:pitcher_crop',
        'minecraft:wheat',
        'minecraft:moving_piston',
        '#minecraft:fence_gates',
    ],
)

MANGROVE_LOGS = Tag(
    values=[
        'minecraft:mangrove_log',
        'minecraft:mangrove_wood',
        'minecraft:stripped_mangrove_log',
        'minecraft:stripped_mangrove_wood',
    ],
)

MANGROVE_LOGS_CAN_GROW_THROUGH = Tag(
    values=[
        'minecraft:mud',
        'minecraft:muddy_mangrove_roots',
        'minecraft:mangrove_roots',
        'minecraft:mangrove_leaves',
        'minecraft:mangrove_log',
        'minecraft:mangrove_propagule',
        'minecraft:moss_carpet',
        'minecraft:vine',
    ],
)

MANGROVE_ROOTS_CAN_GROW_THROUGH = Tag(
    values=[
        'minecraft:mud',
        'minecraft:muddy_mangrove_roots',
        'minecraft:mangrove_roots',
        'minecraft:moss_carpet',
        'minecraft:vine',
        'minecraft:mangrove_propagule',
        'minecraft:snow',
    ],
)

MELTS_ICICLE_ABOVE = Tag(values=['minecraft:magma_block'])

MOB_INTERACTABLE_DOORS = Tag(
    values=[
        '#minecraft:wooden_doors',
        'minecraft:copper_door',
        'minecraft:exposed_copper_door',
        'minecraft:weathered_copper_door',
        'minecraft:oxidized_copper_door',
        'minecraft:waxed_copper_door',
        'minecraft:waxed_exposed_copper_door',
        'minecraft:waxed_weathered_copper_door',
        'minecraft:waxed_oxidized_copper_door',
    ],
)

MOOSHROOMS_SPAWNABLE_ON = Tag(values=['minecraft:mycelium'])

MOSS_BLOCKS = Tag(values=['minecraft:moss_block', 'minecraft:pale_moss_block'])

MOSS_REPLACEABLE = Tag(
    values=[
        '#minecraft:base_stone_overworld',
        '#minecraft:cave_vines',
        '#minecraft:dirt',
        '#minecraft:mud',
        '#minecraft:moss_blocks',
        '#minecraft:grass_blocks',
    ],
)

MUD = Tag(values=['minecraft:mud', 'minecraft:muddy_mangrove_roots'])

NEEDS_DIAMOND_TOOL = Tag(
    values=[
        'minecraft:obsidian',
        'minecraft:crying_obsidian',
        'minecraft:netherite_block',
        'minecraft:respawn_anchor',
        'minecraft:ancient_debris',
    ],
)

NEEDS_IRON_TOOL = Tag(
    values=[
        'minecraft:diamond_block',
        'minecraft:diamond_ore',
        'minecraft:deepslate_diamond_ore',
        'minecraft:emerald_ore',
        'minecraft:deepslate_emerald_ore',
        'minecraft:emerald_block',
        'minecraft:gold_block',
        'minecraft:raw_gold_block',
        'minecraft:gold_ore',
        'minecraft:deepslate_gold_ore',
        'minecraft:redstone_ore',
        'minecraft:deepslate_redstone_ore',
    ],
)

NEEDS_STONE_TOOL = Tag(
    values=[
        'minecraft:iron_block',
        'minecraft:raw_iron_block',
        'minecraft:iron_ore',
        'minecraft:deepslate_iron_ore',
        'minecraft:lapis_block',
        'minecraft:lapis_ore',
        'minecraft:deepslate_lapis_ore',
        'minecraft:raw_copper_block',
        'minecraft:copper_ore',
        'minecraft:deepslate_copper_ore',
        'minecraft:crafter',
        '#minecraft:copper_chests',
        '#minecraft:lightning_rods',
        'minecraft:copper_block',
        'minecraft:exposed_copper',
        'minecraft:weathered_copper',
        'minecraft:oxidized_copper',
        'minecraft:waxed_copper_block',
        'minecraft:waxed_exposed_copper',
        'minecraft:waxed_weathered_copper',
        'minecraft:waxed_oxidized_copper',
        'minecraft:copper_bulb',
        'minecraft:exposed_copper_bulb',
        'minecraft:weathered_copper_bulb',
        'minecraft:oxidized_copper_bulb',
        'minecraft:waxed_copper_bulb',
        'minecraft:waxed_exposed_copper_bulb',
        'minecraft:waxed_weathered_copper_bulb',
        'minecraft:waxed_oxidized_copper_bulb',
        'minecraft:cut_copper',
        'minecraft:exposed_cut_copper',
        'minecraft:weathered_cut_copper',
        'minecraft:oxidized_cut_copper',
        'minecraft:waxed_cut_copper',
        'minecraft:waxed_exposed_cut_copper',
        'minecraft:waxed_weathered_cut_copper',
        'minecraft:waxed_oxidized_cut_copper',
        'minecraft:chiseled_copper',
        'minecraft:exposed_chiseled_copper',
        'minecraft:weathered_chiseled_copper',
        'minecraft:oxidized_chiseled_copper',
        'minecraft:waxed_chiseled_copper',
        'minecraft:waxed_exposed_chiseled_copper',
        'minecraft:waxed_weathered_chiseled_copper',
        'minecraft:waxed_oxidized_chiseled_copper',
        'minecraft:cut_copper_stairs',
        'minecraft:exposed_cut_copper_stairs',
        'minecraft:weathered_cut_copper_stairs',
        'minecraft:oxidized_cut_copper_stairs',
        'minecraft:waxed_cut_copper_stairs',
        'minecraft:waxed_exposed_cut_copper_stairs',
        'minecraft:waxed_weathered_cut_copper_stairs',
        'minecraft:waxed_oxidized_cut_copper_stairs',
        'minecraft:cut_copper_slab',
        'minecraft:exposed_cut_copper_slab',
        'minecraft:weathered_cut_copper_slab',
        'minecraft:oxidized_cut_copper_slab',
        'minecraft:waxed_cut_copper_slab',
        'minecraft:waxed_exposed_cut_copper_slab',
        'minecraft:waxed_weathered_cut_copper_slab',
        'minecraft:waxed_oxidized_cut_copper_slab',
        'minecraft:copper_trapdoor',
        'minecraft:exposed_copper_trapdoor',
        'minecraft:weathered_copper_trapdoor',
        'minecraft:oxidized_copper_trapdoor',
        'minecraft:waxed_copper_trapdoor',
        'minecraft:waxed_exposed_copper_trapdoor',
        'minecraft:waxed_weathered_copper_trapdoor',
        'minecraft:waxed_oxidized_copper_trapdoor',
        'minecraft:copper_grate',
        'minecraft:exposed_copper_grate',
        'minecraft:weathered_copper_grate',
        'minecraft:oxidized_copper_grate',
        'minecraft:waxed_copper_grate',
        'minecraft:waxed_exposed_copper_grate',
        'minecraft:waxed_weathered_copper_grate',
        'minecraft:waxed_oxidized_copper_grate',
    ],
)

NETHER_PORTAL_FRAME = Tag(values=['minecraft:obsidian'])

NYLIUM = Tag(values=['minecraft:crimson_nylium', 'minecraft:warped_nylium'])

OAK_LOGS = Tag(values=['minecraft:oak_log', 'minecraft:oak_wood', 'minecraft:stripped_oak_log', 'minecraft:stripped_oak_wood'])

OCCLUDES_VIBRATION_SIGNALS = Tag(values=['#minecraft:wool'])

ORES = Tag(
    values=[
        '#minecraft:copper_ores',
        '#minecraft:gold_ores',
        '#minecraft:iron_ores',
        '#minecraft:coal_ores',
        '#minecraft:diamond_ores',
        '#minecraft:emerald_ores',
        '#minecraft:lapis_ores',
        '#minecraft:redstone_ores',
        'minecraft:nether_quartz_ore',
    ],
)

OVERRIDES_MUSHROOM_LIGHT_REQUIREMENT = Tag(values=['minecraft:mycelium', 'minecraft:podzol', 'minecraft:crimson_nylium', 'minecraft:warped_nylium'])

OVERWORLD_NATURAL_LOGS = Tag(
    values=[
        'minecraft:acacia_log',
        'minecraft:birch_log',
        'minecraft:oak_log',
        'minecraft:jungle_log',
        'minecraft:spruce_log',
        'minecraft:dark_oak_log',
        'minecraft:pale_oak_log',
        'minecraft:mangrove_log',
        'minecraft:cherry_log',
        'minecraft:poplar_log',
    ],
)

PALE_OAK_LOGS = Tag(
    values=[
        'minecraft:pale_oak_log',
        'minecraft:pale_oak_wood',
        'minecraft:stripped_pale_oak_log',
        'minecraft:stripped_pale_oak_wood',
    ],
)

PARROTS_SPAWNABLE_ON = Tag(values=['minecraft:grass_block', 'minecraft:air', '#minecraft:leaves', '#minecraft:logs'])

PIGLIN_REPELLENTS = Tag(
    values=[
        'minecraft:soul_fire',
        'minecraft:soul_torch',
        'minecraft:soul_lantern',
        'minecraft:soul_wall_torch',
        'minecraft:soul_campfire',
    ],
)

PLANKS = Tag(
    values=[
        'minecraft:oak_planks',
        'minecraft:spruce_planks',
        'minecraft:birch_planks',
        'minecraft:jungle_planks',
        'minecraft:acacia_planks',
        'minecraft:dark_oak_planks',
        'minecraft:pale_oak_planks',
        'minecraft:crimson_planks',
        'minecraft:warped_planks',
        'minecraft:mangrove_planks',
        'minecraft:bamboo_planks',
        'minecraft:cherry_planks',
        'minecraft:poplar_planks',
    ],
)

POLAR_BEARS_SPAWNABLE_ON_ALTERNATE = Tag(values=['minecraft:ice'])

POLAR_BEAR_IMMUNE_TO = Tag(values=['minecraft:powder_snow'])

POPLAR_LOGS = Tag(
    values=['minecraft:poplar_log', 'minecraft:poplar_wood', 'minecraft:stripped_poplar_log', 'minecraft:stripped_poplar_wood'],
)

PORTALS = Tag(values=['minecraft:nether_portal', 'minecraft:end_portal', 'minecraft:end_gateway'])

PRESSURE_PLATES = Tag(
    values=[
        'minecraft:light_weighted_pressure_plate',
        'minecraft:heavy_weighted_pressure_plate',
        '#minecraft:wooden_pressure_plates',
        '#minecraft:stone_pressure_plates',
    ],
)

PREVENTS_NEARBY_LEAF_DECAY = Tag(values=['#minecraft:logs'])

PREVENT_MOB_SPAWNING_INSIDE = Tag(values=['#minecraft:rails'])

RABBITS_SPAWNABLE_ON = Tag(values=['minecraft:grass_block', 'minecraft:snow', 'minecraft:snow_block', 'minecraft:sand'])

RAILS = Tag(values=['minecraft:rail', 'minecraft:powered_rail', 'minecraft:detector_rail', 'minecraft:activator_rail'])

REDSTONE_ORES = Tag(values=['minecraft:redstone_ore', 'minecraft:deepslate_redstone_ore'])

REPLACEABLE = Tag(
    values=[
        'minecraft:air',
        'minecraft:water',
        'minecraft:lava',
        'minecraft:short_grass',
        'minecraft:fern',
        'minecraft:dead_bush',
        'minecraft:bush',
        'minecraft:red_shrub',
        'minecraft:short_dry_grass',
        'minecraft:tall_dry_grass',
        'minecraft:seagrass',
        'minecraft:tall_seagrass',
        'minecraft:fire',
        'minecraft:soul_fire',
        'minecraft:snow',
        'minecraft:vine',
        'minecraft:glow_lichen',
        'minecraft:resin_clump',
        'minecraft:light',
        'minecraft:tall_grass',
        'minecraft:large_fern',
        'minecraft:structure_void',
        'minecraft:void_air',
        'minecraft:cave_air',
        'minecraft:bubble_column',
        'minecraft:warped_roots',
        'minecraft:nether_sprouts',
        'minecraft:crimson_roots',
        'minecraft:leaf_litter',
        'minecraft:hanging_roots',
    ],
)

REPLACEABLE_BY_MUSHROOMS = Tag(
    values=[
        '#minecraft:leaves',
        '#minecraft:small_flowers',
        'minecraft:pale_moss_carpet',
        'minecraft:short_grass',
        'minecraft:fern',
        'minecraft:dead_bush',
        'minecraft:vine',
        'minecraft:glow_lichen',
        'minecraft:sunflower',
        'minecraft:lilac',
        'minecraft:rose_bush',
        'minecraft:peony',
        'minecraft:tall_grass',
        'minecraft:large_fern',
        'minecraft:hanging_roots',
        'minecraft:pitcher_plant',
        'minecraft:water',
        'minecraft:seagrass',
        'minecraft:tall_seagrass',
        'minecraft:brown_mushroom',
        'minecraft:red_mushroom',
        'minecraft:brown_mushroom_block',
        'minecraft:red_mushroom_block',
        'minecraft:warped_roots',
        'minecraft:nether_sprouts',
        'minecraft:crimson_roots',
        'minecraft:leaf_litter',
        'minecraft:short_dry_grass',
        'minecraft:tall_dry_grass',
        'minecraft:bush',
        'minecraft:red_shrub',
        'minecraft:firefly_bush',
    ],
)

REPLACEABLE_BY_TREES = Tag(
    values=[
        '#minecraft:leaves',
        '#minecraft:small_flowers',
        'minecraft:pale_moss_carpet',
        'minecraft:short_grass',
        'minecraft:fern',
        'minecraft:dead_bush',
        'minecraft:vine',
        'minecraft:glow_lichen',
        'minecraft:sunflower',
        'minecraft:lilac',
        'minecraft:rose_bush',
        'minecraft:peony',
        'minecraft:tall_grass',
        'minecraft:large_fern',
        'minecraft:hanging_roots',
        'minecraft:pitcher_plant',
        'minecraft:water',
        'minecraft:seagrass',
        'minecraft:tall_seagrass',
        'minecraft:bush',
        'minecraft:firefly_bush',
        'minecraft:warped_roots',
        'minecraft:nether_sprouts',
        'minecraft:crimson_roots',
        'minecraft:leaf_litter',
        'minecraft:short_dry_grass',
        'minecraft:tall_dry_grass',
        'minecraft:shelf_mushroom',
    ],
)

REQUIRED_FOR_POPLAR_LEAF_AMBIENCE = Tag(values=['#minecraft:overworld_natural_logs'])

SAND = Tag(values=['minecraft:sand', 'minecraft:red_sand', 'minecraft:suspicious_sand'])

SAPLINGS = Tag(
    values=[
        'minecraft:oak_sapling',
        'minecraft:spruce_sapling',
        'minecraft:birch_sapling',
        'minecraft:jungle_sapling',
        'minecraft:acacia_sapling',
        'minecraft:dark_oak_sapling',
        'minecraft:pale_oak_sapling',
        'minecraft:azalea',
        'minecraft:flowering_azalea',
        'minecraft:mangrove_propagule',
        'minecraft:cherry_sapling',
        'minecraft:poplar_sapling',
    ],
)

SCULK_GROWTH_INHIBITORS = Tag(values=['minecraft:sculk_sensor', 'minecraft:sculk_shrieker'])

SCULK_REPLACEABLE = Tag(
    values=[
        '#minecraft:base_stone_overworld',
        '#minecraft:substrate_overworld',
        '#minecraft:terracotta',
        '#minecraft:nylium',
        '#minecraft:base_stone_nether',
        'minecraft:sand',
        'minecraft:red_sand',
        'minecraft:gravel',
        'minecraft:soul_sand',
        'minecraft:soul_soil',
        'minecraft:calcite',
        'minecraft:smooth_basalt',
        'minecraft:clay',
        'minecraft:dripstone_block',
        'minecraft:end_stone',
        'minecraft:red_sandstone',
        'minecraft:sandstone',
        'minecraft:sulfur',
        'minecraft:cinnabar',
    ],
)

SCULK_REPLACEABLE_WORLD_GEN = Tag(
    values=[
        '#minecraft:sculk_replaceable',
        'minecraft:deepslate_bricks',
        'minecraft:deepslate_tiles',
        'minecraft:cobbled_deepslate',
        'minecraft:cracked_deepslate_bricks',
        'minecraft:cracked_deepslate_tiles',
        'minecraft:polished_deepslate',
    ],
)

SHEARS_EXTREME_BREAKING_SPEED = Tag(values=['#minecraft:leaves'])

SHEARS_MAJOR_BREAKING_SPEED = Tag(values=['#minecraft:wool', '#minecraft:wool_slabs', '#minecraft:wool_stairs'])

SHEARS_MINOR_BREAKING_SPEED = Tag(values=['minecraft:glow_lichen', 'minecraft:vine'])

SHULKER_BOXES = Tag(
    values=[
        'minecraft:shulker_box',
        'minecraft:white_shulker_box',
        'minecraft:orange_shulker_box',
        'minecraft:magenta_shulker_box',
        'minecraft:light_blue_shulker_box',
        'minecraft:yellow_shulker_box',
        'minecraft:lime_shulker_box',
        'minecraft:pink_shulker_box',
        'minecraft:gray_shulker_box',
        'minecraft:light_gray_shulker_box',
        'minecraft:cyan_shulker_box',
        'minecraft:purple_shulker_box',
        'minecraft:blue_shulker_box',
        'minecraft:brown_shulker_box',
        'minecraft:green_shulker_box',
        'minecraft:red_shulker_box',
        'minecraft:black_shulker_box',
    ],
)

SHULKER_DOES_NOT_TELEPORT_TO = Tag(values=['minecraft:bedrock'])

SIGNS = Tag(values=['#minecraft:standing_signs', '#minecraft:wall_signs'])

SKULLS = Tag(
    values=[
        'minecraft:player_head',
        'minecraft:creeper_head',
        'minecraft:zombie_head',
        'minecraft:skeleton_skull',
        'minecraft:wither_skeleton_skull',
        'minecraft:dragon_head',
        'minecraft:piglin_head',
    ],
)

SLABS = Tag(
    values=[
        '#minecraft:wooden_slabs',
        'minecraft:stone_slab',
        'minecraft:smooth_stone_slab',
        'minecraft:stone_brick_slab',
        'minecraft:sandstone_slab',
        'minecraft:cobblestone_slab',
        'minecraft:brick_slab',
        'minecraft:nether_brick_slab',
        'minecraft:quartz_slab',
        'minecraft:red_sandstone_slab',
        'minecraft:prismarine_slab',
        'minecraft:prismarine_brick_slab',
        'minecraft:dark_prismarine_slab',
        'minecraft:purpur_slab',
        'minecraft:end_stone_brick_slab',
        'minecraft:petrified_oak_slab',
        'minecraft:cut_sandstone_slab',
        'minecraft:smooth_sandstone_slab',
        'minecraft:cut_red_sandstone_slab',
        'minecraft:smooth_red_sandstone_slab',
        'minecraft:smooth_quartz_slab',
        'minecraft:mossy_cobblestone_slab',
        'minecraft:mossy_stone_brick_slab',
        'minecraft:granite_slab',
        'minecraft:polished_granite_slab',
        'minecraft:diorite_slab',
        'minecraft:polished_diorite_slab',
        'minecraft:andesite_slab',
        'minecraft:polished_andesite_slab',
        'minecraft:red_nether_brick_slab',
        'minecraft:blackstone_slab',
        'minecraft:polished_blackstone_slab',
        'minecraft:polished_blackstone_brick_slab',
        'minecraft:cut_copper_slab',
        'minecraft:exposed_cut_copper_slab',
        'minecraft:weathered_cut_copper_slab',
        'minecraft:oxidized_cut_copper_slab',
        'minecraft:waxed_cut_copper_slab',
        'minecraft:waxed_exposed_cut_copper_slab',
        'minecraft:waxed_weathered_cut_copper_slab',
        'minecraft:waxed_oxidized_cut_copper_slab',
        'minecraft:cobbled_deepslate_slab',
        'minecraft:polished_deepslate_slab',
        'minecraft:deepslate_brick_slab',
        'minecraft:deepslate_tile_slab',
        'minecraft:mud_brick_slab',
        'minecraft:bamboo_mosaic_slab',
        'minecraft:tuff_slab',
        'minecraft:polished_tuff_slab',
        'minecraft:tuff_brick_slab',
        'minecraft:resin_brick_slab',
        'minecraft:cinnabar_slab',
        'minecraft:polished_cinnabar_slab',
        'minecraft:cinnabar_brick_slab',
        'minecraft:sulfur_slab',
        'minecraft:polished_sulfur_slab',
        'minecraft:sulfur_brick_slab',
        '#minecraft:wool_slabs',
        '#minecraft:concrete_slabs',
    ],
)

SMALL_FLOWERS = Tag(
    values=[
        'minecraft:dandelion',
        'minecraft:open_eyeblossom',
        'minecraft:poppy',
        'minecraft:blue_orchid',
        'minecraft:allium',
        'minecraft:azure_bluet',
        'minecraft:red_tulip',
        'minecraft:orange_tulip',
        'minecraft:white_tulip',
        'minecraft:pink_tulip',
        'minecraft:oxeye_daisy',
        'minecraft:cornflower',
        'minecraft:lily_of_the_valley',
        'minecraft:wither_rose',
        'minecraft:torchflower',
        'minecraft:closed_eyeblossom',
        'minecraft:golden_dandelion',
    ],
)

SMELTS_TO_GLASS = Tag(values=['minecraft:sand', 'minecraft:red_sand'])

SNAPS_GOAT_HORN = Tag(
    values=[
        '#minecraft:overworld_natural_logs',
        'minecraft:stone',
        'minecraft:packed_ice',
        'minecraft:iron_ore',
        'minecraft:coal_ore',
        'minecraft:copper_ore',
        'minecraft:emerald_ore',
    ],
)

SNIFFER_DIGGABLE_BLOCK = Tag(values=['#minecraft:dirt', '#minecraft:mud', '#minecraft:moss_blocks', 'minecraft:grass_block', 'minecraft:podzol'])

SNIFFER_EGG_HATCH_BOOST = Tag(values=['minecraft:moss_block'])

SNOW = Tag(values=['minecraft:snow', 'minecraft:snow_block', 'minecraft:powder_snow'])

SNOW_GOLEM_IMMUNE_TO = Tag(values=['minecraft:powder_snow'])

SOUL_FIRE_BASE_BLOCKS = Tag(values=['minecraft:soul_sand', 'minecraft:soul_soil'])

SOUL_SPEED_BLOCKS = Tag(values=['minecraft:soul_sand', 'minecraft:soul_soil'])

SPEEDS_UP_ZOMBIE_VILLAGER_CURING = Tag(values=['minecraft:iron_bars', '#minecraft:beds'])

SPELEOTHEMS = Tag(values=['minecraft:icicle', 'minecraft:pointed_dripstone', 'minecraft:sulfur_spike'])

SPRUCE_LOGS = Tag(
    values=['minecraft:spruce_log', 'minecraft:spruce_wood', 'minecraft:stripped_spruce_log', 'minecraft:stripped_spruce_wood'],
)

STAIRS = Tag(
    values=[
        '#minecraft:wooden_stairs',
        'minecraft:cobblestone_stairs',
        'minecraft:sandstone_stairs',
        'minecraft:brick_stairs',
        'minecraft:stone_brick_stairs',
        'minecraft:nether_brick_stairs',
        'minecraft:quartz_stairs',
        'minecraft:red_sandstone_stairs',
        'minecraft:prismarine_stairs',
        'minecraft:prismarine_brick_stairs',
        'minecraft:dark_prismarine_stairs',
        'minecraft:purpur_stairs',
        'minecraft:end_stone_brick_stairs',
        'minecraft:stone_stairs',
        'minecraft:smooth_sandstone_stairs',
        'minecraft:smooth_red_sandstone_stairs',
        'minecraft:smooth_quartz_stairs',
        'minecraft:mossy_cobblestone_stairs',
        'minecraft:mossy_stone_brick_stairs',
        'minecraft:granite_stairs',
        'minecraft:polished_granite_stairs',
        'minecraft:diorite_stairs',
        'minecraft:polished_diorite_stairs',
        'minecraft:andesite_stairs',
        'minecraft:polished_andesite_stairs',
        'minecraft:red_nether_brick_stairs',
        'minecraft:blackstone_stairs',
        'minecraft:polished_blackstone_stairs',
        'minecraft:polished_blackstone_brick_stairs',
        'minecraft:cut_copper_stairs',
        'minecraft:exposed_cut_copper_stairs',
        'minecraft:weathered_cut_copper_stairs',
        'minecraft:oxidized_cut_copper_stairs',
        'minecraft:waxed_cut_copper_stairs',
        'minecraft:waxed_exposed_cut_copper_stairs',
        'minecraft:waxed_weathered_cut_copper_stairs',
        'minecraft:waxed_oxidized_cut_copper_stairs',
        'minecraft:cobbled_deepslate_stairs',
        'minecraft:polished_deepslate_stairs',
        'minecraft:deepslate_brick_stairs',
        'minecraft:deepslate_tile_stairs',
        'minecraft:mud_brick_stairs',
        'minecraft:bamboo_mosaic_stairs',
        'minecraft:tuff_stairs',
        'minecraft:polished_tuff_stairs',
        'minecraft:tuff_brick_stairs',
        'minecraft:resin_brick_stairs',
        'minecraft:cinnabar_stairs',
        'minecraft:polished_cinnabar_stairs',
        'minecraft:cinnabar_brick_stairs',
        'minecraft:sulfur_stairs',
        'minecraft:polished_sulfur_stairs',
        'minecraft:sulfur_brick_stairs',
        '#minecraft:wool_stairs',
        '#minecraft:concrete_stairs',
    ],
)

STANDING_SIGNS = Tag(
    values=[
        'minecraft:oak_sign',
        'minecraft:spruce_sign',
        'minecraft:birch_sign',
        'minecraft:acacia_sign',
        'minecraft:jungle_sign',
        'minecraft:dark_oak_sign',
        'minecraft:pale_oak_sign',
        'minecraft:crimson_sign',
        'minecraft:warped_sign',
        'minecraft:mangrove_sign',
        'minecraft:poplar_sign',
        'minecraft:bamboo_sign',
        'minecraft:cherry_sign',
    ],
)

STONE_BRICKS = Tag(
    values=[
        'minecraft:stone_bricks',
        'minecraft:mossy_stone_bricks',
        'minecraft:cracked_stone_bricks',
        'minecraft:chiseled_stone_bricks',
    ],
)

STONE_BUTTONS = Tag(values=['minecraft:stone_button', 'minecraft:polished_blackstone_button'])

STONE_ORE_REPLACEABLES = Tag(values=['minecraft:stone', 'minecraft:granite', 'minecraft:diorite', 'minecraft:andesite'])

STONE_PRESSURE_PLATES = Tag(values=['minecraft:stone_pressure_plate', 'minecraft:polished_blackstone_pressure_plate'])

STRAY_IMMUNE_TO = Tag(values=['minecraft:powder_snow'])

STRIDER_WARM_BLOCKS = Tag(values=['minecraft:lava'])

SUBSTRATE_OVERWORLD = Tag(values=['#minecraft:dirt', '#minecraft:mud', '#minecraft:moss_blocks', '#minecraft:grass_blocks'])

SULFUR_SPIKE_REPLACEABLE_BLOCKS = Tag(values=['minecraft:sulfur', 'minecraft:cinnabar'])

SUPPORTS_AZALEA = Tag(values=['#minecraft:supports_vegetation', 'minecraft:clay'])

SUPPORTS_BAMBOO = Tag(
    values=[
        '#minecraft:sand',
        '#minecraft:substrate_overworld',
        'minecraft:bamboo',
        'minecraft:bamboo_sapling',
        'minecraft:gravel',
        'minecraft:suspicious_gravel',
    ],
)

SUPPORTS_BIG_DRIPLEAF = Tag(
    values=[
        '#minecraft:supports_small_dripleaf',
        'minecraft:dirt',
        'minecraft:grass_block',
        'minecraft:podzol',
        'minecraft:coarse_dirt',
        'minecraft:mycelium',
        'minecraft:rooted_dirt',
        'minecraft:moss_block',
        'minecraft:mud',
        'minecraft:muddy_mangrove_roots',
        'minecraft:farmland',
    ],
)

SUPPORTS_CACTUS = Tag(values=['#minecraft:sand'])

SUPPORTS_CHORUS_FLOWER = Tag(values=['minecraft:end_stone'])

SUPPORTS_CHORUS_PLANT = Tag(values=['minecraft:end_stone'])

SUPPORTS_COCOA = Tag(values=['#minecraft:jungle_logs'])

SUPPORTS_CRIMSON_FUNGUS = Tag(values=['#minecraft:supports_warped_fungus'])

SUPPORTS_CRIMSON_ROOTS = Tag(values=['#minecraft:supports_warped_roots'])

SUPPORTS_CROPS = Tag(values=['minecraft:farmland'])

SUPPORTS_DRY_VEGETATION = Tag(values=['#minecraft:sand', '#minecraft:terracotta', '#minecraft:supports_vegetation'])

SUPPORTS_FROGSPAWN = Tag(values=[])

SUPPORTS_HANGING_MANGROVE_PROPAGULE = Tag(values=['minecraft:mangrove_leaves'])

SUPPORTS_LILY_PAD = Tag(values=['minecraft:ice', 'minecraft:frosted_ice'])

SUPPORTS_MANGROVE_PROPAGULE = Tag(values=['#minecraft:supports_vegetation', 'minecraft:clay'])

SUPPORTS_MELON_STEM = Tag(values=['#minecraft:supports_stem_crops'])

SUPPORTS_MELON_STEM_FRUIT = Tag(values=['#minecraft:supports_stem_fruit'])

SUPPORTS_NETHER_SPROUTS = Tag(values=['#minecraft:supports_vegetation', '#minecraft:nylium', 'minecraft:soul_soil'])

SUPPORTS_NETHER_WART = Tag(values=['minecraft:soul_sand'])

SUPPORTS_PUMPKIN_STEM = Tag(values=['#minecraft:supports_stem_crops'])

SUPPORTS_PUMPKIN_STEM_FRUIT = Tag(values=['#minecraft:supports_stem_fruit'])

SUPPORTS_SMALL_DRIPLEAF = Tag(values=['minecraft:clay', 'minecraft:moss_block'])

SUPPORTS_STEM_CROPS = Tag(values=['#minecraft:supports_crops'])

SUPPORTS_STEM_FRUIT = Tag(values=['#minecraft:supports_vegetation'])

SUPPORTS_SUGAR_CANE = Tag(values=['#minecraft:substrate_overworld', '#minecraft:sand'])

SUPPORTS_SUGAR_CANE_ADJACENTLY = Tag(values=['minecraft:frosted_ice'])

SUPPORTS_VEGETATION = Tag(values=['#minecraft:substrate_overworld', 'minecraft:farmland'])

SUPPORTS_WARPED_FUNGUS = Tag(values=['#minecraft:supports_vegetation', '#minecraft:nylium', 'minecraft:mycelium', 'minecraft:soul_soil'])

SUPPORTS_WARPED_ROOTS = Tag(values=['#minecraft:supports_vegetation', '#minecraft:nylium', 'minecraft:soul_soil'])

SUPPORTS_WITHER_ROSE = Tag(values=['#minecraft:supports_vegetation', 'minecraft:netherrack', 'minecraft:soul_sand', 'minecraft:soul_soil'])

SUPPORT_OVERRIDE_CACTUS_FLOWER = Tag(values=['minecraft:cactus', 'minecraft:farmland'])

SUPPORT_OVERRIDE_SNOW_LAYER = Tag(values=['minecraft:honey_block', 'minecraft:soul_sand', 'minecraft:mud'])

SUPPRESSES_BOUNCE = Tag(values=['minecraft:honey_block'])

SWORD_EFFICIENT = Tag(
    values=[
        '#minecraft:leaves',
        'minecraft:vine',
        'minecraft:glow_lichen',
        'minecraft:pumpkin',
        'minecraft:carved_pumpkin',
        'minecraft:jack_o_lantern',
        'minecraft:melon',
        'minecraft:cocoa',
        'minecraft:big_dripleaf',
        'minecraft:big_dripleaf_stem',
        'minecraft:chorus_plant',
        'minecraft:chorus_flower',
    ],
)

SWORD_INSTANTLY_MINES = Tag(values=['minecraft:bamboo', 'minecraft:bamboo_sapling'])

TERRACOTTA = Tag(
    values=[
        'minecraft:terracotta',
        'minecraft:white_terracotta',
        'minecraft:orange_terracotta',
        'minecraft:magenta_terracotta',
        'minecraft:light_blue_terracotta',
        'minecraft:yellow_terracotta',
        'minecraft:lime_terracotta',
        'minecraft:pink_terracotta',
        'minecraft:gray_terracotta',
        'minecraft:light_gray_terracotta',
        'minecraft:cyan_terracotta',
        'minecraft:purple_terracotta',
        'minecraft:blue_terracotta',
        'minecraft:brown_terracotta',
        'minecraft:green_terracotta',
        'minecraft:red_terracotta',
        'minecraft:black_terracotta',
    ],
)

TRAIL_RUINS_REPLACEABLE = Tag(values=['minecraft:gravel'])

TRAPDOORS = Tag(
    values=[
        '#minecraft:wooden_trapdoors',
        'minecraft:iron_trapdoor',
        'minecraft:copper_trapdoor',
        'minecraft:exposed_copper_trapdoor',
        'minecraft:weathered_copper_trapdoor',
        'minecraft:oxidized_copper_trapdoor',
        'minecraft:waxed_copper_trapdoor',
        'minecraft:waxed_exposed_copper_trapdoor',
        'minecraft:waxed_weathered_copper_trapdoor',
        'minecraft:waxed_oxidized_copper_trapdoor',
    ],
)

TRIGGERS_AMBIENT_DESERT_DRY_VEGETATION_BLOCK_SOUNDS = Tag(values=['#minecraft:terracotta', 'minecraft:sand', 'minecraft:red_sand'])

TRIGGERS_AMBIENT_DESERT_SAND_BLOCK_SOUNDS = Tag(values=['minecraft:sand', 'minecraft:red_sand'])

TRIGGERS_AMBIENT_DRIED_GHAST_BLOCK_SOUNDS = Tag(values=['minecraft:soul_sand', 'minecraft:soul_soil'])

TURNS_INTO_DIRT_PATH = Tag(
    values=[
        'minecraft:grass_block',
        'minecraft:dirt',
        'minecraft:podzol',
        'minecraft:coarse_dirt',
        'minecraft:mycelium',
        'minecraft:rooted_dirt',
    ],
)

TURNS_INTO_FARMLAND = Tag(values=['minecraft:grass_block', 'minecraft:dirt_path', 'minecraft:dirt'])

UNCARVABLE = Tag(values=['minecraft:bedrock'])

UNDERWATER_BONEMEALS = Tag(values=['minecraft:seagrass', '#minecraft:corals', '#minecraft:wall_corals'])

UNSTABLE_BOTTOM_CENTER = Tag(values=['#minecraft:fence_gates'])

VALID_SPAWN = Tag(values=['minecraft:grass_block', 'minecraft:podzol'])

VIBRATION_RESONATORS = Tag(values=['minecraft:amethyst_block'])

VILLAGERS_CAN_SLEEP_ON_BED = Tag(values=['#minecraft:beds'])

VILLAGER_BABIES_CAN_JUMP_ON_BED = Tag(values=['#minecraft:beds'])

WALLS = Tag(
    values=[
        'minecraft:cobblestone_wall',
        'minecraft:mossy_cobblestone_wall',
        'minecraft:brick_wall',
        'minecraft:prismarine_wall',
        'minecraft:red_sandstone_wall',
        'minecraft:mossy_stone_brick_wall',
        'minecraft:granite_wall',
        'minecraft:stone_brick_wall',
        'minecraft:nether_brick_wall',
        'minecraft:andesite_wall',
        'minecraft:red_nether_brick_wall',
        'minecraft:sandstone_wall',
        'minecraft:end_stone_brick_wall',
        'minecraft:diorite_wall',
        'minecraft:blackstone_wall',
        'minecraft:polished_blackstone_brick_wall',
        'minecraft:polished_blackstone_wall',
        'minecraft:cobbled_deepslate_wall',
        'minecraft:polished_deepslate_wall',
        'minecraft:deepslate_tile_wall',
        'minecraft:deepslate_brick_wall',
        'minecraft:mud_brick_wall',
        'minecraft:tuff_wall',
        'minecraft:polished_tuff_wall',
        'minecraft:tuff_brick_wall',
        'minecraft:resin_brick_wall',
        'minecraft:cinnabar_wall',
        'minecraft:polished_cinnabar_wall',
        'minecraft:cinnabar_brick_wall',
        'minecraft:sulfur_wall',
        'minecraft:polished_sulfur_wall',
        'minecraft:sulfur_brick_wall',
    ],
)

WALL_CORALS = Tag(
    values=[
        'minecraft:tube_coral_wall_fan',
        'minecraft:brain_coral_wall_fan',
        'minecraft:bubble_coral_wall_fan',
        'minecraft:fire_coral_wall_fan',
        'minecraft:horn_coral_wall_fan',
    ],
)

WALL_HANGING_SIGNS = Tag(
    values=[
        'minecraft:oak_wall_hanging_sign',
        'minecraft:spruce_wall_hanging_sign',
        'minecraft:birch_wall_hanging_sign',
        'minecraft:acacia_wall_hanging_sign',
        'minecraft:cherry_wall_hanging_sign',
        'minecraft:jungle_wall_hanging_sign',
        'minecraft:dark_oak_wall_hanging_sign',
        'minecraft:pale_oak_wall_hanging_sign',
        'minecraft:crimson_wall_hanging_sign',
        'minecraft:warped_wall_hanging_sign',
        'minecraft:mangrove_wall_hanging_sign',
        'minecraft:bamboo_wall_hanging_sign',
        'minecraft:poplar_wall_hanging_sign',
    ],
)

WALL_POST_OVERRIDE = Tag(
    values=[
        'minecraft:torch',
        'minecraft:soul_torch',
        'minecraft:redstone_torch',
        'minecraft:copper_torch',
        'minecraft:tripwire',
        '#minecraft:signs',
        '#minecraft:banners',
        '#minecraft:pressure_plates',
        'minecraft:cactus_flower',
    ],
)

WALL_SIGNS = Tag(
    values=[
        'minecraft:oak_wall_sign',
        'minecraft:spruce_wall_sign',
        'minecraft:birch_wall_sign',
        'minecraft:acacia_wall_sign',
        'minecraft:jungle_wall_sign',
        'minecraft:dark_oak_wall_sign',
        'minecraft:pale_oak_wall_sign',
        'minecraft:crimson_wall_sign',
        'minecraft:warped_wall_sign',
        'minecraft:mangrove_wall_sign',
        'minecraft:bamboo_wall_sign',
        'minecraft:cherry_wall_sign',
        'minecraft:poplar_wall_sign',
    ],
)

WARPED_STEMS = Tag(
    values=[
        'minecraft:warped_stem',
        'minecraft:stripped_warped_stem',
        'minecraft:warped_hyphae',
        'minecraft:stripped_warped_hyphae',
    ],
)

WART_BLOCKS = Tag(values=['minecraft:nether_wart_block', 'minecraft:warped_wart_block'])

WASHED_AWAY_BY_FLUIDS = Tag(
    values=[
        '#minecraft:fire',
        '#minecraft:saplings',
        '#minecraft:corals',
        '#minecraft:wall_corals',
        '#minecraft:air',
        '#minecraft:flower_pots',
        '#minecraft:buttons',
        '#minecraft:wool_carpets',
        '#minecraft:candles',
        '#minecraft:rails',
        '#minecraft:skulls',
        'minecraft:copper_golem_statue',
        'minecraft:exposed_copper_golem_statue',
        'minecraft:weathered_copper_golem_statue',
        'minecraft:oxidized_copper_golem_statue',
        'minecraft:waxed_copper_golem_statue',
        'minecraft:waxed_exposed_copper_golem_statue',
        'minecraft:waxed_weathered_copper_golem_statue',
        'minecraft:waxed_oxidized_copper_golem_statue',
        'minecraft:water',
        'minecraft:lava',
        'minecraft:tall_seagrass',
        'minecraft:wall_torch',
        'minecraft:redstone_wall_torch',
        'minecraft:soul_wall_torch',
        'minecraft:copper_wall_torch',
        'minecraft:attached_pumpkin_stem',
        'minecraft:attached_melon_stem',
        'minecraft:kelp_plant',
        'minecraft:weeping_vines_plant',
        'minecraft:twisting_vines_plant',
        'minecraft:cave_vines_plant',
        'minecraft:big_dripleaf_stem',
        'minecraft:skeleton_wall_skull',
        'minecraft:wither_skeleton_wall_skull',
        'minecraft:zombie_wall_head',
        'minecraft:player_wall_head',
        'minecraft:creeper_wall_head',
        'minecraft:dragon_wall_head',
        'minecraft:piglin_wall_head',
        'minecraft:bamboo_sapling',
        'minecraft:cobweb',
        'minecraft:snow',
        'minecraft:end_rod',
        'minecraft:chorus_plant',
        'minecraft:chorus_flower',
        'minecraft:big_dripleaf',
        'minecraft:scaffolding',
        'minecraft:powder_snow',
        'minecraft:short_grass',
        'minecraft:fern',
        'minecraft:dead_bush',
        'minecraft:bush',
        'minecraft:short_dry_grass',
        'minecraft:tall_dry_grass',
        'minecraft:seagrass',
        'minecraft:dandelion',
        'minecraft:golden_dandelion',
        'minecraft:torchflower',
        'minecraft:poppy',
        'minecraft:blue_orchid',
        'minecraft:allium',
        'minecraft:azure_bluet',
        'minecraft:red_tulip',
        'minecraft:orange_tulip',
        'minecraft:white_tulip',
        'minecraft:pink_tulip',
        'minecraft:oxeye_daisy',
        'minecraft:cornflower',
        'minecraft:wither_rose',
        'minecraft:lily_of_the_valley',
        'minecraft:brown_mushroom',
        'minecraft:red_mushroom',
        'minecraft:torch',
        'minecraft:redstone_wire',
        'minecraft:wheat',
        'minecraft:lever',
        'minecraft:redstone_torch',
        'minecraft:cactus_flower',
        'minecraft:soul_torch',
        'minecraft:copper_torch',
        'minecraft:pumpkin_stem',
        'minecraft:melon_stem',
        'minecraft:vine',
        'minecraft:glow_lichen',
        'minecraft:resin_clump',
        'minecraft:nether_wart',
        'minecraft:tripwire_hook',
        'minecraft:tripwire',
        'minecraft:carrots',
        'minecraft:potatoes',
        'minecraft:light',
        'minecraft:sunflower',
        'minecraft:lilac',
        'minecraft:rose_bush',
        'minecraft:peony',
        'minecraft:tall_grass',
        'minecraft:large_fern',
        'minecraft:torchflower_crop',
        'minecraft:pitcher_crop',
        'minecraft:pitcher_plant',
        'minecraft:beetroots',
        'minecraft:kelp',
        'minecraft:sweet_berry_bush',
        'minecraft:warped_fungus',
        'minecraft:warped_roots',
        'minecraft:nether_sprouts',
        'minecraft:crimson_fungus',
        'minecraft:weeping_vines',
        'minecraft:twisting_vines',
        'minecraft:crimson_roots',
        'minecraft:cave_vines',
        'minecraft:spore_blossom',
        'minecraft:pink_petals',
        'minecraft:wildflowers',
        'minecraft:leaf_litter',
        'minecraft:small_dripleaf',
        'minecraft:hanging_roots',
        'minecraft:frogspawn',
        'minecraft:pale_hanging_moss',
        'minecraft:open_eyeblossom',
        'minecraft:closed_eyeblossom',
        'minecraft:firefly_bush',
        'minecraft:repeater',
        'minecraft:lily_pad',
        'minecraft:cocoa',
        'minecraft:comparator',
        'minecraft:sea_pickle',
        'minecraft:moss_carpet',
        'minecraft:heavy_core',
        'minecraft:pale_moss_carpet',
        'minecraft:red_shrub',
        'minecraft:shelf_mushroom',
        'minecraft:straw_bed',
    ],
)

WITHER_IMMUNE = Tag(
    values=[
        'minecraft:barrier',
        'minecraft:bedrock',
        'minecraft:end_portal',
        'minecraft:end_portal_frame',
        'minecraft:end_gateway',
        'minecraft:command_block',
        'minecraft:repeating_command_block',
        'minecraft:chain_command_block',
        'minecraft:structure_block',
        'minecraft:jigsaw',
        'minecraft:moving_piston',
        'minecraft:light',
        'minecraft:reinforced_deepslate',
        'minecraft:test_block',
        'minecraft:test_instance_block',
    ],
)

WITHER_IMMUNE_TO = Tag(values=['minecraft:wither_rose'])

WITHER_SKELETON_IMMUNE_TO = Tag(values=['minecraft:wither_rose'])

WITHER_SUMMON_BASE_BLOCKS = Tag(values=['minecraft:soul_sand', 'minecraft:soul_soil'])

WOLVES_SPAWNABLE_ON = Tag(
    values=['minecraft:grass_block', 'minecraft:snow', 'minecraft:snow_block', 'minecraft:coarse_dirt', 'minecraft:podzol'],
)

WOODEN_BUTTONS = Tag(
    values=[
        'minecraft:oak_button',
        'minecraft:spruce_button',
        'minecraft:birch_button',
        'minecraft:jungle_button',
        'minecraft:acacia_button',
        'minecraft:dark_oak_button',
        'minecraft:pale_oak_button',
        'minecraft:crimson_button',
        'minecraft:warped_button',
        'minecraft:mangrove_button',
        'minecraft:bamboo_button',
        'minecraft:cherry_button',
        'minecraft:poplar_button',
    ],
)

WOODEN_DOORS = Tag(
    values=[
        'minecraft:oak_door',
        'minecraft:spruce_door',
        'minecraft:birch_door',
        'minecraft:jungle_door',
        'minecraft:acacia_door',
        'minecraft:dark_oak_door',
        'minecraft:pale_oak_door',
        'minecraft:crimson_door',
        'minecraft:warped_door',
        'minecraft:mangrove_door',
        'minecraft:bamboo_door',
        'minecraft:cherry_door',
        'minecraft:poplar_door',
    ],
)

WOODEN_FENCES = Tag(
    values=[
        'minecraft:oak_fence',
        'minecraft:acacia_fence',
        'minecraft:dark_oak_fence',
        'minecraft:pale_oak_fence',
        'minecraft:spruce_fence',
        'minecraft:birch_fence',
        'minecraft:jungle_fence',
        'minecraft:crimson_fence',
        'minecraft:warped_fence',
        'minecraft:mangrove_fence',
        'minecraft:bamboo_fence',
        'minecraft:cherry_fence',
        'minecraft:poplar_fence',
    ],
)

WOODEN_PRESSURE_PLATES = Tag(
    values=[
        'minecraft:oak_pressure_plate',
        'minecraft:spruce_pressure_plate',
        'minecraft:birch_pressure_plate',
        'minecraft:jungle_pressure_plate',
        'minecraft:acacia_pressure_plate',
        'minecraft:dark_oak_pressure_plate',
        'minecraft:pale_oak_pressure_plate',
        'minecraft:crimson_pressure_plate',
        'minecraft:warped_pressure_plate',
        'minecraft:mangrove_pressure_plate',
        'minecraft:bamboo_pressure_plate',
        'minecraft:cherry_pressure_plate',
        'minecraft:poplar_pressure_plate',
    ],
)

WOODEN_SHELVES = Tag(
    values=[
        'minecraft:acacia_shelf',
        'minecraft:bamboo_shelf',
        'minecraft:birch_shelf',
        'minecraft:cherry_shelf',
        'minecraft:crimson_shelf',
        'minecraft:dark_oak_shelf',
        'minecraft:jungle_shelf',
        'minecraft:mangrove_shelf',
        'minecraft:oak_shelf',
        'minecraft:pale_oak_shelf',
        'minecraft:spruce_shelf',
        'minecraft:warped_shelf',
        'minecraft:poplar_shelf',
    ],
)

WOODEN_SLABS = Tag(
    values=[
        'minecraft:oak_slab',
        'minecraft:spruce_slab',
        'minecraft:birch_slab',
        'minecraft:jungle_slab',
        'minecraft:acacia_slab',
        'minecraft:dark_oak_slab',
        'minecraft:pale_oak_slab',
        'minecraft:crimson_slab',
        'minecraft:warped_slab',
        'minecraft:mangrove_slab',
        'minecraft:bamboo_slab',
        'minecraft:cherry_slab',
        'minecraft:poplar_slab',
    ],
)

WOODEN_STAIRS = Tag(
    values=[
        'minecraft:oak_stairs',
        'minecraft:spruce_stairs',
        'minecraft:birch_stairs',
        'minecraft:jungle_stairs',
        'minecraft:acacia_stairs',
        'minecraft:dark_oak_stairs',
        'minecraft:pale_oak_stairs',
        'minecraft:crimson_stairs',
        'minecraft:warped_stairs',
        'minecraft:mangrove_stairs',
        'minecraft:bamboo_stairs',
        'minecraft:cherry_stairs',
        'minecraft:poplar_stairs',
    ],
)

WOODEN_TRAPDOORS = Tag(
    values=[
        'minecraft:acacia_trapdoor',
        'minecraft:birch_trapdoor',
        'minecraft:dark_oak_trapdoor',
        'minecraft:pale_oak_trapdoor',
        'minecraft:jungle_trapdoor',
        'minecraft:oak_trapdoor',
        'minecraft:spruce_trapdoor',
        'minecraft:crimson_trapdoor',
        'minecraft:warped_trapdoor',
        'minecraft:mangrove_trapdoor',
        'minecraft:bamboo_trapdoor',
        'minecraft:cherry_trapdoor',
        'minecraft:poplar_trapdoor',
    ],
)

WOOL = Tag(
    values=[
        'minecraft:white_wool',
        'minecraft:orange_wool',
        'minecraft:magenta_wool',
        'minecraft:light_blue_wool',
        'minecraft:yellow_wool',
        'minecraft:lime_wool',
        'minecraft:pink_wool',
        'minecraft:gray_wool',
        'minecraft:light_gray_wool',
        'minecraft:cyan_wool',
        'minecraft:purple_wool',
        'minecraft:blue_wool',
        'minecraft:brown_wool',
        'minecraft:green_wool',
        'minecraft:red_wool',
        'minecraft:black_wool',
    ],
)

WOOL_CARPETS = Tag(
    values=[
        'minecraft:white_carpet',
        'minecraft:orange_carpet',
        'minecraft:magenta_carpet',
        'minecraft:light_blue_carpet',
        'minecraft:yellow_carpet',
        'minecraft:lime_carpet',
        'minecraft:pink_carpet',
        'minecraft:gray_carpet',
        'minecraft:light_gray_carpet',
        'minecraft:cyan_carpet',
        'minecraft:purple_carpet',
        'minecraft:blue_carpet',
        'minecraft:brown_carpet',
        'minecraft:green_carpet',
        'minecraft:red_carpet',
        'minecraft:black_carpet',
    ],
)

WOOL_SLABS = Tag(
    values=[
        'minecraft:white_wool_slab',
        'minecraft:orange_wool_slab',
        'minecraft:magenta_wool_slab',
        'minecraft:light_blue_wool_slab',
        'minecraft:yellow_wool_slab',
        'minecraft:lime_wool_slab',
        'minecraft:pink_wool_slab',
        'minecraft:gray_wool_slab',
        'minecraft:light_gray_wool_slab',
        'minecraft:cyan_wool_slab',
        'minecraft:purple_wool_slab',
        'minecraft:blue_wool_slab',
        'minecraft:brown_wool_slab',
        'minecraft:green_wool_slab',
        'minecraft:red_wool_slab',
        'minecraft:black_wool_slab',
    ],
)

WOOL_STAIRS = Tag(
    values=[
        'minecraft:white_wool_stairs',
        'minecraft:orange_wool_stairs',
        'minecraft:magenta_wool_stairs',
        'minecraft:light_blue_wool_stairs',
        'minecraft:yellow_wool_stairs',
        'minecraft:lime_wool_stairs',
        'minecraft:pink_wool_stairs',
        'minecraft:gray_wool_stairs',
        'minecraft:light_gray_wool_stairs',
        'minecraft:cyan_wool_stairs',
        'minecraft:purple_wool_stairs',
        'minecraft:blue_wool_stairs',
        'minecraft:brown_wool_stairs',
        'minecraft:green_wool_stairs',
        'minecraft:red_wool_stairs',
        'minecraft:black_wool_stairs',
    ],
)
