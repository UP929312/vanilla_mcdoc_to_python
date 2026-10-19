"""Vanilla's data/loot_table/equipment/ files"""
from vanilla_mcdoc.data.loot.LootContextParamSets import LootContextParamSets
from vanilla_mcdoc.data.loot.LootPool import LootPool
from vanilla_mcdoc.data.loot.LootPoolEntry import LootPoolEntryItem, LootPoolEntryLootTable
from vanilla_mcdoc.data.loot.LootTable import LootTable
from vanilla_mcdoc.data.loot.condition.LootCondition import LootConditionRandomChance
from vanilla_mcdoc.data.loot.function.LootFunction import LootFunctionSetComponents, LootFunctionSetEnchantments
from vanilla_mcdoc.world.component.DataComponentPatch import DataComponentPatch
from vanilla_mcdoc.world.component.item.Trim import Trim

TRIAL_CHAMBER = LootTable(
    type=LootContextParamSets.EQUIPMENT,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryLootTable(
                    weight=4,
                    value=LootTable(
                        pools=[
                            LootPool(
                                rolls=1,
                                entries=[
                                    LootPoolEntryItem(
                                        modifier=[
                                            LootFunctionSetComponents(
                                                components=DataComponentPatch(
                                                    trim=Trim(material='minecraft:copper', pattern='minecraft:bolt'),
                                                ),
                                                type='minecraft:set_components',
                                            ),
                                            LootFunctionSetEnchantments(
                                                enchantments={
                                                    'minecraft:fire_protection': 4,
                                                    'minecraft:projectile_protection': 4,
                                                    'minecraft:protection': 4,
                                                },
                                                type='minecraft:set_enchantments',
                                            ),
                                        ],
                                        name='minecraft:chainmail_helmet',
                                        type='minecraft:item',
                                    ),
                                ],
                                condition=LootConditionRandomChance(chance=0.5, type='minecraft:random_chance'),
                            ),
                            LootPool(
                                rolls=1,
                                entries=[
                                    LootPoolEntryItem(
                                        modifier=[
                                            LootFunctionSetComponents(
                                                components=DataComponentPatch(
                                                    trim=Trim(material='minecraft:copper', pattern='minecraft:bolt'),
                                                ),
                                                type='minecraft:set_components',
                                            ),
                                            LootFunctionSetEnchantments(
                                                enchantments={
                                                    'minecraft:fire_protection': 4,
                                                    'minecraft:projectile_protection': 4,
                                                    'minecraft:protection': 4,
                                                },
                                                type='minecraft:set_enchantments',
                                            ),
                                        ],
                                        name='minecraft:chainmail_chestplate',
                                        type='minecraft:item',
                                    ),
                                ],
                                condition=LootConditionRandomChance(chance=0.5, type='minecraft:random_chance'),
                            ),
                        ],
                    ),
                    type='minecraft:loot_table',
                ),
                LootPoolEntryLootTable(
                    weight=2,
                    value=LootTable(
                        pools=[
                            LootPool(
                                rolls=1,
                                entries=[
                                    LootPoolEntryItem(
                                        modifier=[
                                            LootFunctionSetComponents(
                                                components=DataComponentPatch(
                                                    trim=Trim(material='minecraft:copper', pattern='minecraft:flow'),
                                                ),
                                                type='minecraft:set_components',
                                            ),
                                            LootFunctionSetEnchantments(
                                                enchantments={
                                                    'minecraft:fire_protection': 4,
                                                    'minecraft:projectile_protection': 4,
                                                    'minecraft:protection': 4,
                                                },
                                                type='minecraft:set_enchantments',
                                            ),
                                        ],
                                        name='minecraft:iron_helmet',
                                        type='minecraft:item',
                                    ),
                                ],
                                condition=LootConditionRandomChance(chance=0.5, type='minecraft:random_chance'),
                            ),
                            LootPool(
                                rolls=1,
                                entries=[
                                    LootPoolEntryItem(
                                        modifier=[
                                            LootFunctionSetComponents(
                                                components=DataComponentPatch(
                                                    trim=Trim(material='minecraft:copper', pattern='minecraft:flow'),
                                                ),
                                                type='minecraft:set_components',
                                            ),
                                            LootFunctionSetEnchantments(
                                                enchantments={
                                                    'minecraft:fire_protection': 4,
                                                    'minecraft:projectile_protection': 4,
                                                    'minecraft:protection': 4,
                                                },
                                                type='minecraft:set_enchantments',
                                            ),
                                        ],
                                        name='minecraft:iron_chestplate',
                                        type='minecraft:item',
                                    ),
                                ],
                                condition=LootConditionRandomChance(chance=0.5, type='minecraft:random_chance'),
                            ),
                        ],
                    ),
                    type='minecraft:loot_table',
                ),
                LootPoolEntryLootTable(
                    value=LootTable(
                        pools=[
                            LootPool(
                                rolls=1,
                                entries=[
                                    LootPoolEntryItem(
                                        modifier=[
                                            LootFunctionSetComponents(
                                                components=DataComponentPatch(
                                                    trim=Trim(material='minecraft:copper', pattern='minecraft:flow'),
                                                ),
                                                type='minecraft:set_components',
                                            ),
                                            LootFunctionSetEnchantments(
                                                enchantments={
                                                    'minecraft:fire_protection': 4,
                                                    'minecraft:projectile_protection': 4,
                                                    'minecraft:protection': 4,
                                                },
                                                type='minecraft:set_enchantments',
                                            ),
                                        ],
                                        name='minecraft:diamond_helmet',
                                        type='minecraft:item',
                                    ),
                                ],
                                condition=LootConditionRandomChance(chance=0.5, type='minecraft:random_chance'),
                            ),
                            LootPool(
                                rolls=1,
                                entries=[
                                    LootPoolEntryItem(
                                        modifier=[
                                            LootFunctionSetComponents(
                                                components=DataComponentPatch(
                                                    trim=Trim(material='minecraft:copper', pattern='minecraft:flow'),
                                                ),
                                                type='minecraft:set_components',
                                            ),
                                            LootFunctionSetEnchantments(
                                                enchantments={
                                                    'minecraft:fire_protection': 4,
                                                    'minecraft:projectile_protection': 4,
                                                    'minecraft:protection': 4,
                                                },
                                                type='minecraft:set_enchantments',
                                            ),
                                        ],
                                        name='minecraft:diamond_chestplate',
                                        type='minecraft:item',
                                    ),
                                ],
                                condition=LootConditionRandomChance(chance=0.5, type='minecraft:random_chance'),
                            ),
                        ],
                    ),
                    type='minecraft:loot_table',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:equipment/trial_chamber',
)

TRIAL_CHAMBER_MELEE = LootTable(
    type=LootContextParamSets.EQUIPMENT,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryLootTable(value='minecraft:equipment/trial_chamber', type='minecraft:loot_table')],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(weight=4, name='minecraft:iron_sword', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetEnchantments(
                        enchantments={'minecraft:sharpness': 1},
                        type='minecraft:set_enchantments',
                    ),
                    name='minecraft:iron_sword',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetEnchantments(
                        enchantments={'minecraft:knockback': 1},
                        type='minecraft:set_enchantments',
                    ),
                    name='minecraft:iron_sword',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(name='minecraft:diamond_sword', type='minecraft:item'),
            ],
        ),
    ],
    random_sequence='minecraft:equipment/trial_chamber_melee',
)

TRIAL_CHAMBER_RANGED = LootTable(
    type=LootContextParamSets.EQUIPMENT,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryLootTable(value='minecraft:equipment/trial_chamber', type='minecraft:loot_table')],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(weight=2, name='minecraft:bow', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetEnchantments(enchantments={'minecraft:power': 1}, type='minecraft:set_enchantments'),
                    name='minecraft:bow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetEnchantments(enchantments={'minecraft:punch': 1}, type='minecraft:set_enchantments'),
                    name='minecraft:bow',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:equipment/trial_chamber_ranged',
)
