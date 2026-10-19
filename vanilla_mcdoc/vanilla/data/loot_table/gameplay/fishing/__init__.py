"""Vanilla's data/loot_table/gameplay/fishing/ files"""
from vanilla_mcdoc.data.advancement.predicate.LocationPredicate import LocationPredicate
from vanilla_mcdoc.data.loot.LootContextParamSets import LootContextParamSets
from vanilla_mcdoc.data.loot.LootPool import LootPool
from vanilla_mcdoc.data.loot.LootPoolEntry import LootPoolEntryItem
from vanilla_mcdoc.data.loot.LootTable import LootTable
from vanilla_mcdoc.data.loot.condition.LootCondition import LootConditionLocationCheck
from vanilla_mcdoc.data.loot.function.LootFunction import LootFunctionEnchantWithLevels, LootFunctionSetCount, LootFunctionSetDamage, LootFunctionSetPotion
from vanilla_mcdoc.data.number_provider.context_float.ContextFloatProvider import ContextFloatProviderStructUniform

FISH = LootTable(
    type=LootContextParamSets.FISHING,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(weight=60, name='minecraft:cod', type='minecraft:item'),
                LootPoolEntryItem(weight=25, name='minecraft:salmon', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:tropical_fish', type='minecraft:item'),
                LootPoolEntryItem(weight=13, name='minecraft:pufferfish', type='minecraft:item'),
            ],
        ),
    ],
    random_sequence='minecraft:gameplay/fishing/fish',
)

JUNK = LootTable(
    type=LootContextParamSets.FISHING,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(weight=17, name='minecraft:lily_pad', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetDamage(
                        damage=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=0.9),
                        type='minecraft:set_damage',
                    ),
                    weight=10,
                    name='minecraft:leather_boots',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=10, name='minecraft:leather', type='minecraft:item'),
                LootPoolEntryItem(weight=10, name='minecraft:bone', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetPotion(id='minecraft:water', type='minecraft:set_potion'),
                    weight=10,
                    name='minecraft:potion',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=5, name='minecraft:string', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetDamage(
                        damage=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=0.9),
                        type='minecraft:set_damage',
                    ),
                    weight=2,
                    name='minecraft:fishing_rod',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=10, name='minecraft:bowl', type='minecraft:item'),
                LootPoolEntryItem(weight=5, name='minecraft:stick', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=10, type='minecraft:set_count'),
                    name='minecraft:ink_sac',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=10, name='minecraft:tripwire_hook', type='minecraft:item'),
                LootPoolEntryItem(weight=10, name='minecraft:rotten_flesh', type='minecraft:item'),
                LootPoolEntryItem(
                    condition=LootConditionLocationCheck(
                        predicate=LocationPredicate(
                            biomes=['minecraft:jungle', 'minecraft:sparse_jungle', 'minecraft:bamboo_jungle'],
                        ),
                        type='minecraft:location_check',
                    ),
                    weight=10,
                    name='minecraft:bamboo',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:gameplay/fishing/junk',
)

TREASURE = LootTable(
    type=LootContextParamSets.FISHING,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(name='minecraft:name_tag', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:saddle', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetDamage(
                            damage=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=0.25),
                            type='minecraft:set_damage',
                        ),
                        LootFunctionEnchantWithLevels(
                            levels=30,
                            options='#minecraft:on_random_loot',
                            type='minecraft:enchant_with_levels',
                        ),
                    ],
                    name='minecraft:bow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetDamage(
                            damage=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=0.25),
                            type='minecraft:set_damage',
                        ),
                        LootFunctionEnchantWithLevels(
                            levels=30,
                            options='#minecraft:on_random_loot',
                            type='minecraft:enchant_with_levels',
                        ),
                    ],
                    name='minecraft:fishing_rod',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantWithLevels(
                        levels=30,
                        options='#minecraft:on_random_loot',
                        type='minecraft:enchant_with_levels',
                    ),
                    name='minecraft:book',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(name='minecraft:nautilus_shell', type='minecraft:item'),
            ],
        ),
    ],
    random_sequence='minecraft:gameplay/fishing/treasure',
)
