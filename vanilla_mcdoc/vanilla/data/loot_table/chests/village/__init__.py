"""Vanilla's data/loot_table/chests/village/ files"""
from vanilla_mcdoc.data.loot.LootContextParamSets import LootContextParamSets
from vanilla_mcdoc.data.loot.LootPool import LootPool
from vanilla_mcdoc.data.loot.LootPoolEntry import LootPoolEntryEmpty, LootPoolEntryItem
from vanilla_mcdoc.data.loot.LootTable import LootTable
from vanilla_mcdoc.data.loot.function.LootFunction import LootFunctionSetCount
from vanilla_mcdoc.data.number_provider.context_int.ContextIntProvider import ContextIntProviderStructUniform

VILLAGE_ARMORER = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=5),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:iron_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=4,
                    name='minecraft:bread',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(name='minecraft:iron_helmet', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:emerald', type='minecraft:item'),
            ],
        ),
    ],
    random_sequence='minecraft:chests/village/village_armorer',
)

VILLAGE_BUTCHER = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=5),
            entries=[
                LootPoolEntryItem(name='minecraft:emerald', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=6,
                    name='minecraft:porkchop',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=6,
                    name='minecraft:wheat',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=6,
                    name='minecraft:beef',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=6,
                    name='minecraft:mutton',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:coal',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:chests/village/village_butcher',
)

VILLAGE_CARTOGRAPHER = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=5),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:map',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=5),
                        type='minecraft:set_count',
                    ),
                    weight=15,
                    name='minecraft:paper',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=5, name='minecraft:compass', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=15,
                    name='minecraft:bread',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:stick',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:bundle',
                    type='minecraft:item',
                ),
                LootPoolEntryEmpty(weight=2, type='minecraft:empty'),
            ],
        ),
    ],
    random_sequence='minecraft:chests/village/village_cartographer',
)

VILLAGE_DESERT_HOUSE = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=8),
            entries=[
                LootPoolEntryItem(name='minecraft:clay_ball', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:green_dye', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:cactus',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=7),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:wheat',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:bread',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(name='minecraft:book', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:dead_bush',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:emerald',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:bundle',
                    type='minecraft:item',
                ),
                LootPoolEntryEmpty(weight=2, type='minecraft:empty'),
            ],
        ),
    ],
    random_sequence='minecraft:chests/village/village_desert_house',
)

VILLAGE_FISHER = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=5),
            entries=[
                LootPoolEntryItem(name='minecraft:emerald', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:cod',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:salmon',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:water_bucket',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:barrel',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:wheat_seeds',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:coal',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:chests/village/village_fisher',
)

VILLAGE_FLETCHER = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=5),
            entries=[
                LootPoolEntryItem(name='minecraft:emerald', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:arrow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=6,
                    name='minecraft:feather',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:egg',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=6,
                    name='minecraft:flint',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=6,
                    name='minecraft:stick',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:chests/village/village_fletcher',
)

VILLAGE_MASON = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=5),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:clay_ball',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:stone', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:stone_bricks', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=4,
                    name='minecraft:bread',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(name='minecraft:yellow_dye', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:smooth_stone', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:emerald', type='minecraft:item'),
            ],
        ),
    ],
    random_sequence='minecraft:chests/village/village_mason',
)

VILLAGE_PLAINS_HOUSE = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=8),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:gold_nugget',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=2, name='minecraft:dandelion', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:poppy', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=7),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:potato',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:bread',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=5),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:apple',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(name='minecraft:book', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:feather', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:emerald',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:oak_sapling',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:bundle',
                    type='minecraft:item',
                ),
                LootPoolEntryEmpty(weight=2, type='minecraft:empty'),
            ],
        ),
    ],
    random_sequence='minecraft:chests/village/village_plains_house',
)

VILLAGE_SAVANNA_HOUSE = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=8),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:gold_nugget',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=5, name='minecraft:short_grass', type='minecraft:item'),
                LootPoolEntryItem(weight=5, name='minecraft:tall_grass', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:bread',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=5),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:wheat_seeds',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:emerald',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:acacia_sapling',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(name='minecraft:saddle', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:torch',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(name='minecraft:bucket', type='minecraft:item'),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:bundle',
                    type='minecraft:item',
                ),
                LootPoolEntryEmpty(weight=2, type='minecraft:empty'),
            ],
        ),
    ],
    random_sequence='minecraft:chests/village/village_savanna_house',
)

VILLAGE_SHEPHERD = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=5),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=6,
                    name='minecraft:white_wool',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:black_wool',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:gray_wool',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:brown_wool',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:light_gray_wool',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(name='minecraft:emerald', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:shears', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=6),
                        type='minecraft:set_count',
                    ),
                    weight=6,
                    name='minecraft:wheat',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:chests/village/village_shepherd',
)

VILLAGE_SNOWY_HOUSE = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=8),
            entries=[
                LootPoolEntryItem(name='minecraft:blue_ice', type='minecraft:item'),
                LootPoolEntryItem(weight=4, name='minecraft:snow_block', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=7),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:potato',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:bread',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=5),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:beetroot_seeds',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(name='minecraft:beetroot_soup', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:furnace', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:emerald',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=7),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:snowball',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:coal',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:bundle',
                    type='minecraft:item',
                ),
                LootPoolEntryEmpty(weight=2, type='minecraft:empty'),
            ],
        ),
    ],
    random_sequence='minecraft:chests/village/village_snowy_house',
)

VILLAGE_TAIGA_HOUSE = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=8),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=5),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:iron_nugget',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=2, name='minecraft:fern', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:large_fern', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=7),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:potato',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=7),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:sweet_berries',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:bread',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=5),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:pumpkin_seeds',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(name='minecraft:pumpkin_pie', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:emerald',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=5),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:spruce_sapling',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(name='minecraft:spruce_sign', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=5),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:spruce_log',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:bundle',
                    type='minecraft:item',
                ),
                LootPoolEntryEmpty(weight=2, type='minecraft:empty'),
            ],
        ),
    ],
    random_sequence='minecraft:chests/village/village_taiga_house',
)

VILLAGE_TANNERY = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=5),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:leather',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=2, name='minecraft:leather_chestplate', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:leather_boots', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:leather_helmet', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:bread',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=2, name='minecraft:leather_leggings', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:saddle', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:emerald',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:bundle',
                    type='minecraft:item',
                ),
                LootPoolEntryEmpty(weight=2, type='minecraft:empty'),
            ],
        ),
    ],
    random_sequence='minecraft:chests/village/village_tannery',
)

VILLAGE_TEMPLE = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=8),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:redstone',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=7,
                    name='minecraft:bread',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=7,
                    name='minecraft:rotten_flesh',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:lapis_lazuli',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:gold_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:emerald',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:chests/village/village_temple',
)

VILLAGE_TOOLSMITH = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=8),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:diamond',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=5),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:iron_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:gold_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=15,
                    name='minecraft:bread',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=5, name='minecraft:iron_pickaxe', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:coal',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=20,
                    name='minecraft:stick',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=5, name='minecraft:iron_shovel', type='minecraft:item'),
            ],
        ),
    ],
    random_sequence='minecraft:chests/village/village_toolsmith',
)

VILLAGE_WEAPONSMITH = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=8),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:diamond',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=5),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:iron_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:gold_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=15,
                    name='minecraft:bread',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=15,
                    name='minecraft:apple',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=5, name='minecraft:iron_pickaxe', type='minecraft:item'),
                LootPoolEntryItem(weight=5, name='minecraft:iron_sword', type='minecraft:item'),
                LootPoolEntryItem(weight=5, name='minecraft:iron_spear', type='minecraft:item'),
                LootPoolEntryItem(weight=7, name='minecraft:copper_spear', type='minecraft:item'),
                LootPoolEntryItem(weight=5, name='minecraft:iron_chestplate', type='minecraft:item'),
                LootPoolEntryItem(weight=5, name='minecraft:iron_helmet', type='minecraft:item'),
                LootPoolEntryItem(weight=5, name='minecraft:iron_leggings', type='minecraft:item'),
                LootPoolEntryItem(weight=5, name='minecraft:iron_boots', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=7),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:obsidian',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=7),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:oak_sapling',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=3, name='minecraft:saddle', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:copper_horse_armor', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:iron_horse_armor', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:golden_horse_armor', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:diamond_horse_armor', type='minecraft:item'),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:bundle',
                    type='minecraft:item',
                ),
                LootPoolEntryEmpty(weight=2, type='minecraft:empty'),
            ],
        ),
    ],
    random_sequence='minecraft:chests/village/village_weaponsmith',
)
