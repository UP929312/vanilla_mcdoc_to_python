"""Vanilla's data/loot_table/charged_creeper/ files"""
from vanilla_mcdoc.data.advancement.predicate.EntitySubPredicateMap import EntitySubPredicateMap
from vanilla_mcdoc.data.loot.EntityTarget import EntityTarget
from vanilla_mcdoc.data.loot.LootContextParamSets import LootContextParamSets
from vanilla_mcdoc.data.loot.LootPool import LootPool
from vanilla_mcdoc.data.loot.LootPoolEntry import LootPoolEntryAlternatives, LootPoolEntryItem, LootPoolEntryLootTable
from vanilla_mcdoc.data.loot.LootTable import LootTable
from vanilla_mcdoc.data.loot.condition.LootCondition import LootConditionEntityProperties

CREEPER = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:creeper_head', type='minecraft:item')])],
    random_sequence='minecraft:charged_creeper/creeper',
)

PIGLIN = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:piglin_head', type='minecraft:item')])],
    random_sequence='minecraft:charged_creeper/piglin',
)

ROOT = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryLootTable(
                            condition=LootConditionEntityProperties(
                                entity=EntityTarget.THIS,
                                predicate=EntitySubPredicateMap(entity_type='minecraft:piglin'),
                                type='minecraft:entity_properties',
                            ),
                            value='minecraft:charged_creeper/piglin',
                            type='minecraft:loot_table',
                        ),
                        LootPoolEntryLootTable(
                            condition=LootConditionEntityProperties(
                                entity=EntityTarget.THIS,
                                predicate=EntitySubPredicateMap(entity_type='minecraft:creeper'),
                                type='minecraft:entity_properties',
                            ),
                            value='minecraft:charged_creeper/creeper',
                            type='minecraft:loot_table',
                        ),
                        LootPoolEntryLootTable(
                            condition=LootConditionEntityProperties(
                                entity=EntityTarget.THIS,
                                predicate=EntitySubPredicateMap(entity_type='minecraft:skeleton'),
                                type='minecraft:entity_properties',
                            ),
                            value='minecraft:charged_creeper/skeleton',
                            type='minecraft:loot_table',
                        ),
                        LootPoolEntryLootTable(
                            condition=LootConditionEntityProperties(
                                entity=EntityTarget.THIS,
                                predicate=EntitySubPredicateMap(entity_type='minecraft:wither_skeleton'),
                                type='minecraft:entity_properties',
                            ),
                            value='minecraft:charged_creeper/wither_skeleton',
                            type='minecraft:loot_table',
                        ),
                        LootPoolEntryLootTable(
                            condition=LootConditionEntityProperties(
                                entity=EntityTarget.THIS,
                                predicate=EntitySubPredicateMap(entity_type='minecraft:zombie'),
                                type='minecraft:entity_properties',
                            ),
                            value='minecraft:charged_creeper/zombie',
                            type='minecraft:loot_table',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:charged_creeper/root',
)

SKELETON = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:skeleton_skull', type='minecraft:item')])],
    random_sequence='minecraft:charged_creeper/skeleton',
)

WITHER_SKELETON = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:wither_skeleton_skull', type='minecraft:item')])],
    random_sequence='minecraft:charged_creeper/wither_skeleton',
)

ZOMBIE = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:zombie_head', type='minecraft:item')])],
    random_sequence='minecraft:charged_creeper/zombie',
)
