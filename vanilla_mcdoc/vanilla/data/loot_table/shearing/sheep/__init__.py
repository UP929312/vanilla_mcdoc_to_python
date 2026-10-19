"""Vanilla's data/loot_table/shearing/sheep/ files"""
from vanilla_mcdoc.data.loot.LootContextParamSets import LootContextParamSets
from vanilla_mcdoc.data.loot.LootPool import LootPool
from vanilla_mcdoc.data.loot.LootPoolEntry import LootPoolEntryItem
from vanilla_mcdoc.data.loot.LootTable import LootTable
from vanilla_mcdoc.data.number_provider.context_int.ContextIntProvider import ContextIntProviderStructUniform

BLACK = LootTable(
    type=LootContextParamSets.SHEARING,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
            entries=[LootPoolEntryItem(name='minecraft:black_wool', type='minecraft:item')],
        ),
    ],
    random_sequence='minecraft:shearing/sheep/black',
)

BLUE = LootTable(
    type=LootContextParamSets.SHEARING,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
            entries=[LootPoolEntryItem(name='minecraft:blue_wool', type='minecraft:item')],
        ),
    ],
    random_sequence='minecraft:shearing/sheep/blue',
)

BROWN = LootTable(
    type=LootContextParamSets.SHEARING,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
            entries=[LootPoolEntryItem(name='minecraft:brown_wool', type='minecraft:item')],
        ),
    ],
    random_sequence='minecraft:shearing/sheep/brown',
)

CYAN = LootTable(
    type=LootContextParamSets.SHEARING,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
            entries=[LootPoolEntryItem(name='minecraft:cyan_wool', type='minecraft:item')],
        ),
    ],
    random_sequence='minecraft:shearing/sheep/cyan',
)

GRAY = LootTable(
    type=LootContextParamSets.SHEARING,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
            entries=[LootPoolEntryItem(name='minecraft:gray_wool', type='minecraft:item')],
        ),
    ],
    random_sequence='minecraft:shearing/sheep/gray',
)

GREEN = LootTable(
    type=LootContextParamSets.SHEARING,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
            entries=[LootPoolEntryItem(name='minecraft:green_wool', type='minecraft:item')],
        ),
    ],
    random_sequence='minecraft:shearing/sheep/green',
)

LIGHT_BLUE = LootTable(
    type=LootContextParamSets.SHEARING,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
            entries=[LootPoolEntryItem(name='minecraft:light_blue_wool', type='minecraft:item')],
        ),
    ],
    random_sequence='minecraft:shearing/sheep/light_blue',
)

LIGHT_GRAY = LootTable(
    type=LootContextParamSets.SHEARING,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
            entries=[LootPoolEntryItem(name='minecraft:light_gray_wool', type='minecraft:item')],
        ),
    ],
    random_sequence='minecraft:shearing/sheep/light_gray',
)

LIME = LootTable(
    type=LootContextParamSets.SHEARING,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
            entries=[LootPoolEntryItem(name='minecraft:lime_wool', type='minecraft:item')],
        ),
    ],
    random_sequence='minecraft:shearing/sheep/lime',
)

MAGENTA = LootTable(
    type=LootContextParamSets.SHEARING,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
            entries=[LootPoolEntryItem(name='minecraft:magenta_wool', type='minecraft:item')],
        ),
    ],
    random_sequence='minecraft:shearing/sheep/magenta',
)

ORANGE = LootTable(
    type=LootContextParamSets.SHEARING,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
            entries=[LootPoolEntryItem(name='minecraft:orange_wool', type='minecraft:item')],
        ),
    ],
    random_sequence='minecraft:shearing/sheep/orange',
)

PINK = LootTable(
    type=LootContextParamSets.SHEARING,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
            entries=[LootPoolEntryItem(name='minecraft:pink_wool', type='minecraft:item')],
        ),
    ],
    random_sequence='minecraft:shearing/sheep/pink',
)

PURPLE = LootTable(
    type=LootContextParamSets.SHEARING,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
            entries=[LootPoolEntryItem(name='minecraft:purple_wool', type='minecraft:item')],
        ),
    ],
    random_sequence='minecraft:shearing/sheep/purple',
)

RED = LootTable(
    type=LootContextParamSets.SHEARING,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
            entries=[LootPoolEntryItem(name='minecraft:red_wool', type='minecraft:item')],
        ),
    ],
    random_sequence='minecraft:shearing/sheep/red',
)

WHITE = LootTable(
    type=LootContextParamSets.SHEARING,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
            entries=[LootPoolEntryItem(name='minecraft:white_wool', type='minecraft:item')],
        ),
    ],
    random_sequence='minecraft:shearing/sheep/white',
)

YELLOW = LootTable(
    type=LootContextParamSets.SHEARING,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
            entries=[LootPoolEntryItem(name='minecraft:yellow_wool', type='minecraft:item')],
        ),
    ],
    random_sequence='minecraft:shearing/sheep/yellow',
)
