"""Vanilla's data/loot_table/entities/sheep/ files"""
from vanilla_mcdoc.data.loot.LootContextParamSets import LootContextParamSets
from vanilla_mcdoc.data.loot.LootPool import LootPool
from vanilla_mcdoc.data.loot.LootPoolEntry import LootPoolEntryItem
from vanilla_mcdoc.data.loot.LootTable import LootTable

BLACK = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:black_wool', type='minecraft:item')])],
    random_sequence='minecraft:entities/sheep/black',
)

BLUE = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:blue_wool', type='minecraft:item')])],
    random_sequence='minecraft:entities/sheep/blue',
)

BROWN = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:brown_wool', type='minecraft:item')])],
    random_sequence='minecraft:entities/sheep/brown',
)

CYAN = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:cyan_wool', type='minecraft:item')])],
    random_sequence='minecraft:entities/sheep/cyan',
)

GRAY = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:gray_wool', type='minecraft:item')])],
    random_sequence='minecraft:entities/sheep/gray',
)

GREEN = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:green_wool', type='minecraft:item')])],
    random_sequence='minecraft:entities/sheep/green',
)

LIGHT_BLUE = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:light_blue_wool', type='minecraft:item')])],
    random_sequence='minecraft:entities/sheep/light_blue',
)

LIGHT_GRAY = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:light_gray_wool', type='minecraft:item')])],
    random_sequence='minecraft:entities/sheep/light_gray',
)

LIME = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:lime_wool', type='minecraft:item')])],
    random_sequence='minecraft:entities/sheep/lime',
)

MAGENTA = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:magenta_wool', type='minecraft:item')])],
    random_sequence='minecraft:entities/sheep/magenta',
)

ORANGE = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:orange_wool', type='minecraft:item')])],
    random_sequence='minecraft:entities/sheep/orange',
)

PINK = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:pink_wool', type='minecraft:item')])],
    random_sequence='minecraft:entities/sheep/pink',
)

PURPLE = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:purple_wool', type='minecraft:item')])],
    random_sequence='minecraft:entities/sheep/purple',
)

RED = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:red_wool', type='minecraft:item')])],
    random_sequence='minecraft:entities/sheep/red',
)

WHITE = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:white_wool', type='minecraft:item')])],
    random_sequence='minecraft:entities/sheep/white',
)

YELLOW = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:yellow_wool', type='minecraft:item')])],
    random_sequence='minecraft:entities/sheep/yellow',
)
