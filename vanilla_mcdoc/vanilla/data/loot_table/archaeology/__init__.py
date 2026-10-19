"""Vanilla's data/loot_table/archaeology/ files"""
from vanilla_mcdoc.data.loot.LootContextParamSets import LootContextParamSets
from vanilla_mcdoc.data.loot.LootPool import LootPool
from vanilla_mcdoc.data.loot.LootPoolEntry import LootPoolEntryItem
from vanilla_mcdoc.data.loot.LootTable import LootTable
from vanilla_mcdoc.data.loot.function.LootFunction import LootFunctionSetStewEffect
from vanilla_mcdoc.data.loot.function.StewEffect import StewEffect
from vanilla_mcdoc.data.number_provider.context_int.ContextIntProvider import ContextIntProviderStructUniform

DESERT_PYRAMID = LootTable(
    type=LootContextParamSets.ARCHAEOLOGY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(name='minecraft:archer_pottery_sherd', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:miner_pottery_sherd', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:prize_pottery_sherd', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:skull_pottery_sherd', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:diamond', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:tnt', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:gunpowder', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:emerald', type='minecraft:item'),
            ],
        ),
    ],
    random_sequence='minecraft:archaeology/desert_pyramid',
)

DESERT_WELL = LootTable(
    type=LootContextParamSets.ARCHAEOLOGY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(weight=2, name='minecraft:arms_up_pottery_sherd', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:brewer_pottery_sherd', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:brick', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:emerald', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:stick', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetStewEffect(
                        effects=[
                            StewEffect(
                                type='minecraft:night_vision',
                                duration=ContextIntProviderStructUniform(type='minecraft:uniform', min=7, max=10),
                            ),
                            StewEffect(
                                type='minecraft:jump_boost',
                                duration=ContextIntProviderStructUniform(type='minecraft:uniform', min=7, max=10),
                            ),
                            StewEffect(
                                type='minecraft:weakness',
                                duration=ContextIntProviderStructUniform(type='minecraft:uniform', min=6, max=8),
                            ),
                            StewEffect(
                                type='minecraft:blindness',
                                duration=ContextIntProviderStructUniform(type='minecraft:uniform', min=5, max=7),
                            ),
                            StewEffect(
                                type='minecraft:poison',
                                duration=ContextIntProviderStructUniform(type='minecraft:uniform', min=10, max=20),
                            ),
                            StewEffect(
                                type='minecraft:saturation',
                                duration=ContextIntProviderStructUniform(type='minecraft:uniform', min=7, max=10),
                            ),
                        ],
                        type='minecraft:set_stew_effect',
                    ),
                    name='minecraft:suspicious_stew',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:archaeology/desert_well',
)

OCEAN_RUIN_COLD = LootTable(
    type=LootContextParamSets.ARCHAEOLOGY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(name='minecraft:blade_pottery_sherd', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:explorer_pottery_sherd', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:mourner_pottery_sherd', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:plenty_pottery_sherd', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:iron_axe', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:emerald', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:wheat', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:wooden_hoe', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:coal', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:gold_nugget', type='minecraft:item'),
            ],
        ),
    ],
    random_sequence='minecraft:archaeology/ocean_ruin_cold',
)

OCEAN_RUIN_WARM = LootTable(
    type=LootContextParamSets.ARCHAEOLOGY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(name='minecraft:angler_pottery_sherd', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:shelter_pottery_sherd', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:snort_pottery_sherd', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:sniffer_egg', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:iron_axe', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:emerald', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:wheat', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:wooden_hoe', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:coal', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:gold_nugget', type='minecraft:item'),
            ],
        ),
    ],
    random_sequence='minecraft:archaeology/ocean_ruin_warm',
)

TRAIL_RUINS_COMMON = LootTable(
    type=LootContextParamSets.ARCHAEOLOGY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(weight=2, name='minecraft:emerald', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:wheat', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:wooden_hoe', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:clay', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:brick', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:yellow_dye', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:blue_dye', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:light_blue_dye', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:white_dye', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:orange_dye', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:red_candle', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:green_candle', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:purple_candle', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:brown_candle', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:magenta_stained_glass_pane', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:pink_stained_glass_pane', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:blue_stained_glass_pane', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:light_blue_stained_glass_pane', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:red_stained_glass_pane', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:yellow_stained_glass_pane', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:purple_stained_glass_pane', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:spruce_hanging_sign', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:oak_hanging_sign', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:gold_nugget', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:coal', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:wheat_seeds', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:beetroot_seeds', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:dead_bush', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:string', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:lead', type='minecraft:item'),
            ],
        ),
    ],
    random_sequence='minecraft:archaeology/trail_ruins_common',
)

TRAIL_RUINS_RARE = LootTable(
    type=LootContextParamSets.ARCHAEOLOGY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(name='minecraft:burn_pottery_sherd', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:danger_pottery_sherd', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:friend_pottery_sherd', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:heart_pottery_sherd', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:heartbreak_pottery_sherd', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:howl_pottery_sherd', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:sheaf_pottery_sherd', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:wayfinder_armor_trim_smithing_template', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:raiser_armor_trim_smithing_template', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:shaper_armor_trim_smithing_template', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:host_armor_trim_smithing_template', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:music_disc_relic', type='minecraft:item'),
            ],
        ),
    ],
    random_sequence='minecraft:archaeology/trail_ruins_rare',
)
