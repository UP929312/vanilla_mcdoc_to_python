"""Vanilla's data/loot_table/entities/ files"""
from vanilla_mcdoc.data.advancement.predicate.DamageSourcePredicate import DamageSourcePredicate
from vanilla_mcdoc.data.advancement.predicate.DamageTagPredicate import DamageTagPredicate
from vanilla_mcdoc.data.advancement.predicate.EnchantmentPredicate import EnchantmentPredicate
from vanilla_mcdoc.data.advancement.predicate.EntityFlagsPredicate import EntityFlagsPredicate
from vanilla_mcdoc.data.advancement.predicate.EntitySubPredicateMap import EntitySubPredicateMap
from vanilla_mcdoc.data.advancement.predicate.EquipmentPredicateSlot import EquipmentPredicateSlot
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.advancement.predicate.RaiderPredicate import RaiderPredicate
from vanilla_mcdoc.data.advancement.predicate.SheepPredicate import SheepPredicate
from vanilla_mcdoc.data.advancement.predicate.SlimePredicate import SlimePredicate
from vanilla_mcdoc.data.enchantment.level_based_value.LevelBasedValueMap import LevelBasedValueMapLinear
from vanilla_mcdoc.data.loot.EntityTarget import EntityTarget
from vanilla_mcdoc.data.loot.LootContextParamSets import LootContextParamSets
from vanilla_mcdoc.data.loot.LootPool import LootPool
from vanilla_mcdoc.data.loot.LootPoolEntry import LootPoolEntryAlternatives, LootPoolEntryEmpty, LootPoolEntryItem, LootPoolEntryLootTable, LootPoolEntryTag
from vanilla_mcdoc.data.loot.LootTable import LootTable
from vanilla_mcdoc.data.loot.condition.LootCondition import LootConditionAllOf, LootConditionAnyOf, LootConditionDamageSourceProperties, LootConditionEntityProperties, LootConditionInverted, LootConditionKilledByPlayer, LootConditionRandomChance, LootConditionRandomChanceWithEnchantedBonus
from vanilla_mcdoc.data.loot.function.LootFunction import LootFunctionEnchantedCountIncrease, LootFunctionFurnaceSmelt, LootFunctionSetCount, LootFunctionSetOminousBottleAmplifier, LootFunctionSetPotion
from vanilla_mcdoc.data.number_provider.context_float.ContextFloatProvider import ContextFloatProviderStructUniform
from vanilla_mcdoc.data.number_provider.context_int.ContextIntProvider import ContextIntProviderStructUniform
from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds
from vanilla_mcdoc.util.color.DyeColor import DyeColor
from vanilla_mcdoc.world.component.DataComponentExactPredicate import DataComponentExactPredicate

ALLAY = LootTable(type=LootContextParamSets.ENTITY, random_sequence='minecraft:entities/allay')

ARMADILLO = LootTable(type=LootContextParamSets.ENTITY, random_sequence='minecraft:entities/armadillo')

ARMOR_STAND = LootTable(type=LootContextParamSets.ENTITY, random_sequence='minecraft:entities/armor_stand')

AXOLOTL = LootTable(type=LootContextParamSets.ENTITY, random_sequence='minecraft:entities/axolotl')

BAT = LootTable(type=LootContextParamSets.ENTITY, random_sequence='minecraft:entities/bat')

BEE = LootTable(type=LootContextParamSets.ENTITY, random_sequence='minecraft:entities/bee')

BLAZE = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=1),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:blaze_rod',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionKilledByPlayer(type='minecraft:killed_by_player'),
        ),
    ],
    random_sequence='minecraft:entities/blaze',
)

BOGGED = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:arrow',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:bone',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=1),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            limit=1,
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                        LootFunctionSetPotion(id='minecraft:poison', type='minecraft:set_potion'),
                    ],
                    name='minecraft:tipped_arrow',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionKilledByPlayer(type='minecraft:killed_by_player'),
        ),
    ],
    random_sequence='minecraft:entities/bogged',
)

BREEZE = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=1.0, max=2.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:breeze_rod',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionKilledByPlayer(type='minecraft:killed_by_player'),
        ),
    ],
    random_sequence='minecraft:entities/breeze',
)

CAMEL = LootTable(type=LootContextParamSets.ENTITY, random_sequence='minecraft:entities/camel')

CAMEL_HUSK = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=3),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:rotten_flesh',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:entities/camel_husk',
)

CAT = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:string',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:entities/cat',
)

CAVE_SPIDER = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:string',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=-1, max=1),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:spider_eye',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionKilledByPlayer(type='minecraft:killed_by_player'),
        ),
    ],
    random_sequence='minecraft:entities/cave_spider',
)

CHICKEN = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:feather',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionFurnaceSmelt(
                            condition=LootConditionAnyOf(
                                terms=[
                                    LootConditionEntityProperties(
                                        entity=EntityTarget.THIS,
                                        predicate=EntitySubPredicateMap(flags=EntityFlagsPredicate(is_on_fire=True)),
                                        type='minecraft:entity_properties',
                                    ),
                                    LootConditionEntityProperties(
                                        entity=EntityTarget.DIRECTATTACKER,
                                        predicate=EntitySubPredicateMap(
                                            equipment={
                                                EquipmentPredicateSlot.MAINHAND: ItemPredicate(
                                                    predicates={
                                                        'minecraft:enchantments': [EnchantmentPredicate(enchantments='#minecraft:smelts_loot')],
                                                    },
                                                ),
                                            },
                                        ),
                                        type='minecraft:entity_properties',
                                    ),
                                ],
                                type='minecraft:any_of',
                            ),
                            type='minecraft:furnace_smelt',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:chicken',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:entities/chicken',
)

COD = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionFurnaceSmelt(
                        condition=LootConditionAnyOf(
                            terms=[
                                LootConditionEntityProperties(
                                    entity=EntityTarget.THIS,
                                    predicate=EntitySubPredicateMap(flags=EntityFlagsPredicate(is_on_fire=True)),
                                    type='minecraft:entity_properties',
                                ),
                                LootConditionEntityProperties(
                                    entity=EntityTarget.DIRECTATTACKER,
                                    predicate=EntitySubPredicateMap(
                                        equipment={
                                            EquipmentPredicateSlot.MAINHAND: ItemPredicate(
                                                predicates={
                                                    'minecraft:enchantments': [EnchantmentPredicate(enchantments='#minecraft:smelts_loot')],
                                                },
                                            ),
                                        },
                                    ),
                                    type='minecraft:entity_properties',
                                ),
                            ],
                            type='minecraft:any_of',
                        ),
                        type='minecraft:furnace_smelt',
                    ),
                    name='minecraft:cod',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:bone_meal', type='minecraft:item')],
            condition=LootConditionRandomChance(chance=0.05, type='minecraft:random_chance'),
        ),
    ],
    random_sequence='minecraft:entities/cod',
)

COPPER_GOLEM = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:copper_ingot',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:entities/copper_golem',
)

COW = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:leather',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                            type='minecraft:set_count',
                        ),
                        LootFunctionFurnaceSmelt(
                            condition=LootConditionAnyOf(
                                terms=[
                                    LootConditionEntityProperties(
                                        entity=EntityTarget.THIS,
                                        predicate=EntitySubPredicateMap(flags=EntityFlagsPredicate(is_on_fire=True)),
                                        type='minecraft:entity_properties',
                                    ),
                                    LootConditionEntityProperties(
                                        entity=EntityTarget.DIRECTATTACKER,
                                        predicate=EntitySubPredicateMap(
                                            equipment={
                                                EquipmentPredicateSlot.MAINHAND: ItemPredicate(
                                                    predicates={
                                                        'minecraft:enchantments': [EnchantmentPredicate(enchantments='#minecraft:smelts_loot')],
                                                    },
                                                ),
                                            },
                                        ),
                                        type='minecraft:entity_properties',
                                    ),
                                ],
                                type='minecraft:any_of',
                            ),
                            type='minecraft:furnace_smelt',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:beef',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:entities/cow',
)

CREAKING = LootTable(type=LootContextParamSets.ENTITY, random_sequence='minecraft:entities/creaking')

CREEPER = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:gunpowder',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryTag(items='#minecraft:creeper_drop_music_discs', expand=True, type='minecraft:tag')],
            condition=LootConditionEntityProperties(
                entity=EntityTarget.ATTACKER,
                predicate=EntitySubPredicateMap(entity_type='#minecraft:skeletons'),
                type='minecraft:entity_properties',
            ),
        ),
    ],
    random_sequence='minecraft:entities/creeper',
)

DOLPHIN = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=1),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                        LootFunctionFurnaceSmelt(
                            condition=LootConditionAnyOf(
                                terms=[
                                    LootConditionEntityProperties(
                                        entity=EntityTarget.THIS,
                                        predicate=EntitySubPredicateMap(flags=EntityFlagsPredicate(is_on_fire=True)),
                                        type='minecraft:entity_properties',
                                    ),
                                    LootConditionEntityProperties(
                                        entity=EntityTarget.DIRECTATTACKER,
                                        predicate=EntitySubPredicateMap(
                                            equipment={
                                                EquipmentPredicateSlot.MAINHAND: ItemPredicate(
                                                    predicates={
                                                        'minecraft:enchantments': [EnchantmentPredicate(enchantments='#minecraft:smelts_loot')],
                                                    },
                                                ),
                                            },
                                        ),
                                        type='minecraft:entity_properties',
                                    ),
                                ],
                                type='minecraft:any_of',
                            ),
                            type='minecraft:furnace_smelt',
                        ),
                    ],
                    name='minecraft:cod',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:entities/dolphin',
)

DONKEY = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:leather',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:entities/donkey',
)

DROWNED = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:rotten_flesh',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:copper_ingot', type='minecraft:item')],
            condition=LootConditionAllOf(
                terms=[
                    LootConditionKilledByPlayer(type='minecraft:killed_by_player'),
                    LootConditionRandomChanceWithEnchantedBonus(
                        unenchanted_chance=0.11,
                        enchanted_chance=LevelBasedValueMapLinear(base=0.13, per_level_above_first=0.02, type='minecraft:linear'),
                        enchantment='minecraft:looting',
                        type='minecraft:random_chance_with_enchanted_bonus',
                    ),
                ],
                type='minecraft:all_of',
            ),
        ),
    ],
    random_sequence='minecraft:entities/drowned',
)

ELDER_GUARDIAN = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:prismarine_shard',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                        LootFunctionFurnaceSmelt(
                            condition=LootConditionAnyOf(
                                terms=[
                                    LootConditionEntityProperties(
                                        entity=EntityTarget.THIS,
                                        predicate=EntitySubPredicateMap(flags=EntityFlagsPredicate(is_on_fire=True)),
                                        type='minecraft:entity_properties',
                                    ),
                                    LootConditionEntityProperties(
                                        entity=EntityTarget.DIRECTATTACKER,
                                        predicate=EntitySubPredicateMap(
                                            equipment={
                                                EquipmentPredicateSlot.MAINHAND: ItemPredicate(
                                                    predicates={
                                                        'minecraft:enchantments': [EnchantmentPredicate(enchantments='#minecraft:smelts_loot')],
                                                    },
                                                ),
                                            },
                                        ),
                                        type='minecraft:entity_properties',
                                    ),
                                ],
                                type='minecraft:any_of',
                            ),
                            type='minecraft:furnace_smelt',
                        ),
                    ],
                    weight=3,
                    name='minecraft:cod',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantedCountIncrease(
                        count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                        enchantment='minecraft:looting',
                        type='minecraft:enchanted_count_increase',
                    ),
                    weight=2,
                    name='minecraft:prismarine_crystals',
                    type='minecraft:item',
                ),
                LootPoolEntryEmpty(type='minecraft:empty'),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:wet_sponge', type='minecraft:item')],
            condition=LootConditionKilledByPlayer(type='minecraft:killed_by_player'),
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryLootTable(
                    modifier=LootFunctionFurnaceSmelt(
                        condition=LootConditionAnyOf(
                            terms=[
                                LootConditionEntityProperties(
                                    entity=EntityTarget.THIS,
                                    predicate=EntitySubPredicateMap(flags=EntityFlagsPredicate(is_on_fire=True)),
                                    type='minecraft:entity_properties',
                                ),
                                LootConditionEntityProperties(
                                    entity=EntityTarget.DIRECTATTACKER,
                                    predicate=EntitySubPredicateMap(
                                        equipment={
                                            EquipmentPredicateSlot.MAINHAND: ItemPredicate(
                                                predicates={
                                                    'minecraft:enchantments': [EnchantmentPredicate(enchantments='#minecraft:smelts_loot')],
                                                },
                                            ),
                                        },
                                    ),
                                    type='minecraft:entity_properties',
                                ),
                            ],
                            type='minecraft:any_of',
                        ),
                        type='minecraft:furnace_smelt',
                    ),
                    value='minecraft:gameplay/fishing/fish',
                    type='minecraft:loot_table',
                ),
            ],
            condition=LootConditionAllOf(
                terms=[
                    LootConditionKilledByPlayer(type='minecraft:killed_by_player'),
                    LootConditionRandomChanceWithEnchantedBonus(
                        unenchanted_chance=0.025,
                        enchanted_chance=LevelBasedValueMapLinear(base=0.035, per_level_above_first=0.01, type='minecraft:linear'),
                        enchantment='minecraft:looting',
                        type='minecraft:random_chance_with_enchanted_bonus',
                    ),
                ],
                type='minecraft:all_of',
            ),
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryEmpty(weight=4, type='minecraft:empty'),
                LootPoolEntryItem(name='minecraft:tide_armor_trim_smithing_template', type='minecraft:item'),
            ],
        ),
    ],
    random_sequence='minecraft:entities/elder_guardian',
)

ENDERMAN = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=1),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:ender_pearl',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:entities/enderman',
)

ENDERMITE = LootTable(type=LootContextParamSets.ENTITY, random_sequence='minecraft:entities/endermite')

ENDER_DRAGON = LootTable(type=LootContextParamSets.ENTITY, random_sequence='minecraft:entities/ender_dragon')

EVOKER = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:totem_of_undying', type='minecraft:item')]),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=1),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:emerald',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionKilledByPlayer(type='minecraft:killed_by_player'),
        ),
    ],
    random_sequence='minecraft:entities/evoker',
)

FOX = LootTable(type=LootContextParamSets.ENTITY, random_sequence='minecraft:entities/fox')

FROG = LootTable(type=LootContextParamSets.ENTITY, random_sequence='minecraft:entities/frog')

FROSTBITE = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:rotten_flesh',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=3),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:ice_ball',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:entities/frostbite',
)

GHAST = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=1),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:ghast_tear',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:gunpowder',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:music_disc_tears', type='minecraft:item')],
            modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
            condition=LootConditionAllOf(
                terms=[
                    LootConditionDamageSourceProperties(
                        predicate=DamageSourcePredicate(
                            tags=[DamageTagPredicate(id='#minecraft:is_projectile', expected=True)],
                            direct_entity=EntitySubPredicateMap(entity_type='minecraft:fireball'),
                        ),
                        type='minecraft:damage_source_properties',
                    ),
                    LootConditionKilledByPlayer(type='minecraft:killed_by_player'),
                ],
                type='minecraft:all_of',
            ),
        ),
    ],
    random_sequence='minecraft:entities/ghast',
)

GIANT = LootTable(type=LootContextParamSets.ENTITY, random_sequence='minecraft:entities/giant')

GLOW_SQUID = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:glow_ink_sac',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:entities/glow_squid',
)

GOAT = LootTable(type=LootContextParamSets.ENTITY, random_sequence='minecraft:entities/goat')

GUARDIAN = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:prismarine_shard',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                        LootFunctionFurnaceSmelt(
                            condition=LootConditionAnyOf(
                                terms=[
                                    LootConditionEntityProperties(
                                        entity=EntityTarget.THIS,
                                        predicate=EntitySubPredicateMap(flags=EntityFlagsPredicate(is_on_fire=True)),
                                        type='minecraft:entity_properties',
                                    ),
                                    LootConditionEntityProperties(
                                        entity=EntityTarget.DIRECTATTACKER,
                                        predicate=EntitySubPredicateMap(
                                            equipment={
                                                EquipmentPredicateSlot.MAINHAND: ItemPredicate(
                                                    predicates={
                                                        'minecraft:enchantments': [EnchantmentPredicate(enchantments='#minecraft:smelts_loot')],
                                                    },
                                                ),
                                            },
                                        ),
                                        type='minecraft:entity_properties',
                                    ),
                                ],
                                type='minecraft:any_of',
                            ),
                            type='minecraft:furnace_smelt',
                        ),
                    ],
                    weight=2,
                    name='minecraft:cod',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantedCountIncrease(
                        count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                        enchantment='minecraft:looting',
                        type='minecraft:enchanted_count_increase',
                    ),
                    weight=2,
                    name='minecraft:prismarine_crystals',
                    type='minecraft:item',
                ),
                LootPoolEntryEmpty(type='minecraft:empty'),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryLootTable(
                    modifier=LootFunctionFurnaceSmelt(
                        condition=LootConditionAnyOf(
                            terms=[
                                LootConditionEntityProperties(
                                    entity=EntityTarget.THIS,
                                    predicate=EntitySubPredicateMap(flags=EntityFlagsPredicate(is_on_fire=True)),
                                    type='minecraft:entity_properties',
                                ),
                                LootConditionEntityProperties(
                                    entity=EntityTarget.DIRECTATTACKER,
                                    predicate=EntitySubPredicateMap(
                                        equipment={
                                            EquipmentPredicateSlot.MAINHAND: ItemPredicate(
                                                predicates={
                                                    'minecraft:enchantments': [EnchantmentPredicate(enchantments='#minecraft:smelts_loot')],
                                                },
                                            ),
                                        },
                                    ),
                                    type='minecraft:entity_properties',
                                ),
                            ],
                            type='minecraft:any_of',
                        ),
                        type='minecraft:furnace_smelt',
                    ),
                    value='minecraft:gameplay/fishing/fish',
                    type='minecraft:loot_table',
                ),
            ],
            condition=LootConditionAllOf(
                terms=[
                    LootConditionKilledByPlayer(type='minecraft:killed_by_player'),
                    LootConditionRandomChanceWithEnchantedBonus(
                        unenchanted_chance=0.025,
                        enchanted_chance=LevelBasedValueMapLinear(base=0.035, per_level_above_first=0.01, type='minecraft:linear'),
                        enchantment='minecraft:looting',
                        type='minecraft:random_chance_with_enchanted_bonus',
                    ),
                ],
                type='minecraft:all_of',
            ),
        ),
    ],
    random_sequence='minecraft:entities/guardian',
)

HAPPY_GHAST = LootTable(type=LootContextParamSets.ENTITY, random_sequence='minecraft:entities/happy_ghast')

HOGLIN = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=4),
                            type='minecraft:set_count',
                        ),
                        LootFunctionFurnaceSmelt(
                            condition=LootConditionAnyOf(
                                terms=[
                                    LootConditionEntityProperties(
                                        entity=EntityTarget.THIS,
                                        predicate=EntitySubPredicateMap(flags=EntityFlagsPredicate(is_on_fire=True)),
                                        type='minecraft:entity_properties',
                                    ),
                                    LootConditionEntityProperties(
                                        entity=EntityTarget.DIRECTATTACKER,
                                        predicate=EntitySubPredicateMap(
                                            equipment={
                                                EquipmentPredicateSlot.MAINHAND: ItemPredicate(
                                                    predicates={
                                                        'minecraft:enchantments': [EnchantmentPredicate(enchantments='#minecraft:smelts_loot')],
                                                    },
                                                ),
                                            },
                                        ),
                                        type='minecraft:entity_properties',
                                    ),
                                ],
                                type='minecraft:any_of',
                            ),
                            type='minecraft:furnace_smelt',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:porkchop',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=1),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:leather',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:entities/hoglin',
)

HORSE = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:leather',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:entities/horse',
)

HUSK = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:rotten_flesh',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=1),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    condition=LootConditionEntityProperties(
                        entity=EntityTarget.THIS,
                        predicate=EntitySubPredicateMap(vehicle=EntitySubPredicateMap(entity_type='minecraft:camel_husk')),
                        type='minecraft:entity_properties',
                    ),
                    name='minecraft:rabbit_foot',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(name='minecraft:iron_ingot', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:carrot', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionFurnaceSmelt(
                        condition=LootConditionAnyOf(
                            terms=[
                                LootConditionEntityProperties(
                                    entity=EntityTarget.THIS,
                                    predicate=EntitySubPredicateMap(flags=EntityFlagsPredicate(is_on_fire=True)),
                                    type='minecraft:entity_properties',
                                ),
                                LootConditionEntityProperties(
                                    entity=EntityTarget.DIRECTATTACKER,
                                    predicate=EntitySubPredicateMap(
                                        equipment={
                                            EquipmentPredicateSlot.MAINHAND: ItemPredicate(
                                                predicates={
                                                    'minecraft:enchantments': [EnchantmentPredicate(enchantments='#minecraft:smelts_loot')],
                                                },
                                            ),
                                        },
                                    ),
                                    type='minecraft:entity_properties',
                                ),
                            ],
                            type='minecraft:any_of',
                        ),
                        type='minecraft:furnace_smelt',
                    ),
                    name='minecraft:potato',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionAllOf(
                terms=[
                    LootConditionKilledByPlayer(type='minecraft:killed_by_player'),
                    LootConditionRandomChanceWithEnchantedBonus(
                        unenchanted_chance=0.025,
                        enchanted_chance=LevelBasedValueMapLinear(base=0.035, per_level_above_first=0.01, type='minecraft:linear'),
                        enchantment='minecraft:looting',
                        type='minecraft:random_chance_with_enchanted_bonus',
                    ),
                ],
                type='minecraft:all_of',
            ),
        ),
    ],
    random_sequence='minecraft:entities/husk',
)

ILLUSIONER = LootTable(type=LootContextParamSets.ENTITY, random_sequence='minecraft:entities/illusioner')

IRON_GOLEM = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:poppy',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=5),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:iron_ingot',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:entities/iron_golem',
)

LLAMA = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:leather',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:entities/llama',
)

MAGMA_CUBE = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=-2, max=1),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    condition=LootConditionAllOf(
                        terms=[
                            LootConditionInverted(
                                term=LootConditionDamageSourceProperties(
                                    predicate=DamageSourcePredicate(
                                        source_entity=EntitySubPredicateMap(entity_type='minecraft:frog'),
                                    ),
                                    type='minecraft:damage_source_properties',
                                ),
                                type='minecraft:inverted',
                            ),
                            LootConditionEntityProperties(
                                entity=EntityTarget.THIS,
                                predicate=EntitySubPredicateMap(type_specific_cube_mob=SlimePredicate(size=MinMaxBounds(min=2))),
                                type='minecraft:entity_properties',
                            ),
                        ],
                        type='minecraft:all_of',
                    ),
                    name='minecraft:magma_cream',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    condition=LootConditionDamageSourceProperties(
                        predicate=DamageSourcePredicate(
                            source_entity=EntitySubPredicateMap(
                                components=DataComponentExactPredicate(frog_variant='minecraft:warm'),
                                entity_type='minecraft:frog',
                            ),
                        ),
                        type='minecraft:damage_source_properties',
                    ),
                    name='minecraft:pearlescent_froglight',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    condition=LootConditionDamageSourceProperties(
                        predicate=DamageSourcePredicate(
                            source_entity=EntitySubPredicateMap(
                                components=DataComponentExactPredicate(frog_variant='minecraft:cold'),
                                entity_type='minecraft:frog',
                            ),
                        ),
                        type='minecraft:damage_source_properties',
                    ),
                    name='minecraft:verdant_froglight',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    condition=LootConditionDamageSourceProperties(
                        predicate=DamageSourcePredicate(
                            source_entity=EntitySubPredicateMap(
                                components=DataComponentExactPredicate(frog_variant='minecraft:temperate'),
                                entity_type='minecraft:frog',
                            ),
                        ),
                        type='minecraft:damage_source_properties',
                    ),
                    name='minecraft:ochre_froglight',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:entities/magma_cube',
)

MANNEQUIN = LootTable(type=LootContextParamSets.ENTITY, random_sequence='minecraft:entities/mannequin')

MOOSHROOM = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:leather',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                            type='minecraft:set_count',
                        ),
                        LootFunctionFurnaceSmelt(
                            condition=LootConditionAnyOf(
                                terms=[
                                    LootConditionEntityProperties(
                                        entity=EntityTarget.THIS,
                                        predicate=EntitySubPredicateMap(flags=EntityFlagsPredicate(is_on_fire=True)),
                                        type='minecraft:entity_properties',
                                    ),
                                    LootConditionEntityProperties(
                                        entity=EntityTarget.DIRECTATTACKER,
                                        predicate=EntitySubPredicateMap(
                                            equipment={
                                                EquipmentPredicateSlot.MAINHAND: ItemPredicate(
                                                    predicates={
                                                        'minecraft:enchantments': [EnchantmentPredicate(enchantments='#minecraft:smelts_loot')],
                                                    },
                                                ),
                                            },
                                        ),
                                        type='minecraft:entity_properties',
                                    ),
                                ],
                                type='minecraft:any_of',
                            ),
                            type='minecraft:furnace_smelt',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:beef',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:entities/mooshroom',
)

MULE = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:leather',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:entities/mule',
)

NAUTILUS = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:nautilus_shell', type='minecraft:item')],
            condition=LootConditionAllOf(
                terms=[
                    LootConditionKilledByPlayer(type='minecraft:killed_by_player'),
                    LootConditionRandomChanceWithEnchantedBonus(
                        unenchanted_chance=0.05,
                        enchanted_chance=LevelBasedValueMapLinear(base=0.060000002, per_level_above_first=0.01, type='minecraft:linear'),
                        enchantment='minecraft:looting',
                        type='minecraft:random_chance_with_enchanted_bonus',
                    ),
                ],
                type='minecraft:all_of',
            ),
        ),
    ],
    random_sequence='minecraft:entities/nautilus',
)

OCELOT = LootTable(type=LootContextParamSets.ENTITY, random_sequence='minecraft:entities/ocelot')

PANDA = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:bamboo',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:entities/panda',
)

PARCHED = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:arrow',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:bone',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=1),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            limit=1,
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                        LootFunctionSetPotion(id='minecraft:weakness', type='minecraft:set_potion'),
                    ],
                    name='minecraft:tipped_arrow',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionKilledByPlayer(type='minecraft:killed_by_player'),
        ),
    ],
    random_sequence='minecraft:entities/parched',
)

PARROT = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:feather',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:entities/parrot',
)

PHANTOM = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=1),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:phantom_membrane',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionKilledByPlayer(type='minecraft:killed_by_player'),
        ),
    ],
    random_sequence='minecraft:entities/phantom',
)

PIG = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                            type='minecraft:set_count',
                        ),
                        LootFunctionFurnaceSmelt(
                            condition=LootConditionAnyOf(
                                terms=[
                                    LootConditionEntityProperties(
                                        entity=EntityTarget.THIS,
                                        predicate=EntitySubPredicateMap(flags=EntityFlagsPredicate(is_on_fire=True)),
                                        type='minecraft:entity_properties',
                                    ),
                                    LootConditionEntityProperties(
                                        entity=EntityTarget.DIRECTATTACKER,
                                        predicate=EntitySubPredicateMap(
                                            equipment={
                                                EquipmentPredicateSlot.MAINHAND: ItemPredicate(
                                                    predicates={
                                                        'minecraft:enchantments': [EnchantmentPredicate(enchantments='#minecraft:smelts_loot')],
                                                    },
                                                ),
                                            },
                                        ),
                                        type='minecraft:entity_properties',
                                    ),
                                ],
                                type='minecraft:any_of',
                            ),
                            type='minecraft:furnace_smelt',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:porkchop',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:entities/pig',
)

PIGLIN = LootTable(type=LootContextParamSets.ENTITY, random_sequence='minecraft:entities/piglin')

PIGLIN_BRUTE = LootTable(type=LootContextParamSets.ENTITY, random_sequence='minecraft:entities/piglin_brute')

PILLAGER = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionSetOminousBottleAmplifier(
                            amplifier=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=4),
                            type='minecraft:set_ominous_bottle_amplifier',
                        ),
                    ],
                    name='minecraft:ominous_bottle',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionEntityProperties(
                entity=EntityTarget.THIS,
                predicate=EntitySubPredicateMap(type_specific_raider=RaiderPredicate(is_captain=True)),
                type='minecraft:entity_properties',
            ),
        ),
    ],
    random_sequence='minecraft:entities/pillager',
)

PLAYER = LootTable(type=LootContextParamSets.ENTITY, random_sequence='minecraft:entities/player')

POLAR_BEAR = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionFurnaceSmelt(
                            condition=LootConditionAnyOf(
                                terms=[
                                    LootConditionEntityProperties(
                                        entity=EntityTarget.THIS,
                                        predicate=EntitySubPredicateMap(flags=EntityFlagsPredicate(is_on_fire=True)),
                                        type='minecraft:entity_properties',
                                    ),
                                    LootConditionEntityProperties(
                                        entity=EntityTarget.DIRECTATTACKER,
                                        predicate=EntitySubPredicateMap(
                                            equipment={
                                                EquipmentPredicateSlot.MAINHAND: ItemPredicate(
                                                    predicates={
                                                        'minecraft:enchantments': [EnchantmentPredicate(enchantments='#minecraft:smelts_loot')],
                                                    },
                                                ),
                                            },
                                        ),
                                        type='minecraft:entity_properties',
                                    ),
                                ],
                                type='minecraft:any_of',
                            ),
                            type='minecraft:furnace_smelt',
                        ),
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    weight=3,
                    name='minecraft:cod',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionFurnaceSmelt(
                            condition=LootConditionAnyOf(
                                terms=[
                                    LootConditionEntityProperties(
                                        entity=EntityTarget.THIS,
                                        predicate=EntitySubPredicateMap(flags=EntityFlagsPredicate(is_on_fire=True)),
                                        type='minecraft:entity_properties',
                                    ),
                                    LootConditionEntityProperties(
                                        entity=EntityTarget.DIRECTATTACKER,
                                        predicate=EntitySubPredicateMap(
                                            equipment={
                                                EquipmentPredicateSlot.MAINHAND: ItemPredicate(
                                                    predicates={
                                                        'minecraft:enchantments': [EnchantmentPredicate(enchantments='#minecraft:smelts_loot')],
                                                    },
                                                ),
                                            },
                                        ),
                                        type='minecraft:entity_properties',
                                    ),
                                ],
                                type='minecraft:any_of',
                            ),
                            type='minecraft:furnace_smelt',
                        ),
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:salmon',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:entities/polar_bear',
)

PUFFERFISH = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:pufferfish',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:bone_meal', type='minecraft:item')],
            condition=LootConditionRandomChance(chance=0.05, type='minecraft:random_chance'),
        ),
    ],
    random_sequence='minecraft:entities/pufferfish',
)

RABBIT = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=1),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:rabbit_hide',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionFurnaceSmelt(
                            condition=LootConditionAnyOf(
                                terms=[
                                    LootConditionEntityProperties(
                                        entity=EntityTarget.THIS,
                                        predicate=EntitySubPredicateMap(flags=EntityFlagsPredicate(is_on_fire=True)),
                                        type='minecraft:entity_properties',
                                    ),
                                    LootConditionEntityProperties(
                                        entity=EntityTarget.DIRECTATTACKER,
                                        predicate=EntitySubPredicateMap(
                                            equipment={
                                                EquipmentPredicateSlot.MAINHAND: ItemPredicate(
                                                    predicates={
                                                        'minecraft:enchantments': [EnchantmentPredicate(enchantments='#minecraft:smelts_loot')],
                                                    },
                                                ),
                                            },
                                        ),
                                        type='minecraft:entity_properties',
                                    ),
                                ],
                                type='minecraft:any_of',
                            ),
                            type='minecraft:furnace_smelt',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:rabbit',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:rabbit_foot', type='minecraft:item')],
            condition=LootConditionAllOf(
                terms=[
                    LootConditionKilledByPlayer(type='minecraft:killed_by_player'),
                    LootConditionRandomChanceWithEnchantedBonus(
                        unenchanted_chance=0.1,
                        enchanted_chance=LevelBasedValueMapLinear(base=0.13, per_level_above_first=0.03, type='minecraft:linear'),
                        enchantment='minecraft:looting',
                        type='minecraft:random_chance_with_enchanted_bonus',
                    ),
                ],
                type='minecraft:all_of',
            ),
        ),
    ],
    random_sequence='minecraft:entities/rabbit',
)

RAVAGER = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:saddle',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:entities/ravager',
)

SALMON = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionFurnaceSmelt(
                        condition=LootConditionAnyOf(
                            terms=[
                                LootConditionEntityProperties(
                                    entity=EntityTarget.THIS,
                                    predicate=EntitySubPredicateMap(flags=EntityFlagsPredicate(is_on_fire=True)),
                                    type='minecraft:entity_properties',
                                ),
                                LootConditionEntityProperties(
                                    entity=EntityTarget.DIRECTATTACKER,
                                    predicate=EntitySubPredicateMap(
                                        equipment={
                                            EquipmentPredicateSlot.MAINHAND: ItemPredicate(
                                                predicates={
                                                    'minecraft:enchantments': [EnchantmentPredicate(enchantments='#minecraft:smelts_loot')],
                                                },
                                            ),
                                        },
                                    ),
                                    type='minecraft:entity_properties',
                                ),
                            ],
                            type='minecraft:any_of',
                        ),
                        type='minecraft:furnace_smelt',
                    ),
                    name='minecraft:salmon',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:bone_meal', type='minecraft:item')],
            condition=LootConditionRandomChance(chance=0.05, type='minecraft:random_chance'),
        ),
    ],
    random_sequence='minecraft:entities/salmon',
)

SHEEP = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionFurnaceSmelt(
                            condition=LootConditionAnyOf(
                                terms=[
                                    LootConditionEntityProperties(
                                        entity=EntityTarget.THIS,
                                        predicate=EntitySubPredicateMap(flags=EntityFlagsPredicate(is_on_fire=True)),
                                        type='minecraft:entity_properties',
                                    ),
                                    LootConditionEntityProperties(
                                        entity=EntityTarget.DIRECTATTACKER,
                                        predicate=EntitySubPredicateMap(
                                            equipment={
                                                EquipmentPredicateSlot.MAINHAND: ItemPredicate(
                                                    predicates={
                                                        'minecraft:enchantments': [EnchantmentPredicate(enchantments='#minecraft:smelts_loot')],
                                                    },
                                                ),
                                            },
                                        ),
                                        type='minecraft:entity_properties',
                                    ),
                                ],
                                type='minecraft:any_of',
                            ),
                            type='minecraft:furnace_smelt',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:mutton',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryLootTable(
                            condition=LootConditionEntityProperties(
                                entity=EntityTarget.THIS,
                                predicate=EntitySubPredicateMap(
                                    components=DataComponentExactPredicate(sheep_color=DyeColor.WHITE),
                                    type_specific_sheep=SheepPredicate(sheared=False),
                                ),
                                type='minecraft:entity_properties',
                            ),
                            value='minecraft:entities/sheep/white',
                            type='minecraft:loot_table',
                        ),
                        LootPoolEntryLootTable(
                            condition=LootConditionEntityProperties(
                                entity=EntityTarget.THIS,
                                predicate=EntitySubPredicateMap(
                                    components=DataComponentExactPredicate(sheep_color=DyeColor.ORANGE),
                                    type_specific_sheep=SheepPredicate(sheared=False),
                                ),
                                type='minecraft:entity_properties',
                            ),
                            value='minecraft:entities/sheep/orange',
                            type='minecraft:loot_table',
                        ),
                        LootPoolEntryLootTable(
                            condition=LootConditionEntityProperties(
                                entity=EntityTarget.THIS,
                                predicate=EntitySubPredicateMap(
                                    components=DataComponentExactPredicate(sheep_color=DyeColor.MAGENTA),
                                    type_specific_sheep=SheepPredicate(sheared=False),
                                ),
                                type='minecraft:entity_properties',
                            ),
                            value='minecraft:entities/sheep/magenta',
                            type='minecraft:loot_table',
                        ),
                        LootPoolEntryLootTable(
                            condition=LootConditionEntityProperties(
                                entity=EntityTarget.THIS,
                                predicate=EntitySubPredicateMap(
                                    components=DataComponentExactPredicate(sheep_color=DyeColor.LIGHTBLUE),
                                    type_specific_sheep=SheepPredicate(sheared=False),
                                ),
                                type='minecraft:entity_properties',
                            ),
                            value='minecraft:entities/sheep/light_blue',
                            type='minecraft:loot_table',
                        ),
                        LootPoolEntryLootTable(
                            condition=LootConditionEntityProperties(
                                entity=EntityTarget.THIS,
                                predicate=EntitySubPredicateMap(
                                    components=DataComponentExactPredicate(sheep_color=DyeColor.YELLOW),
                                    type_specific_sheep=SheepPredicate(sheared=False),
                                ),
                                type='minecraft:entity_properties',
                            ),
                            value='minecraft:entities/sheep/yellow',
                            type='minecraft:loot_table',
                        ),
                        LootPoolEntryLootTable(
                            condition=LootConditionEntityProperties(
                                entity=EntityTarget.THIS,
                                predicate=EntitySubPredicateMap(
                                    components=DataComponentExactPredicate(sheep_color=DyeColor.LIME),
                                    type_specific_sheep=SheepPredicate(sheared=False),
                                ),
                                type='minecraft:entity_properties',
                            ),
                            value='minecraft:entities/sheep/lime',
                            type='minecraft:loot_table',
                        ),
                        LootPoolEntryLootTable(
                            condition=LootConditionEntityProperties(
                                entity=EntityTarget.THIS,
                                predicate=EntitySubPredicateMap(
                                    components=DataComponentExactPredicate(sheep_color=DyeColor.PINK),
                                    type_specific_sheep=SheepPredicate(sheared=False),
                                ),
                                type='minecraft:entity_properties',
                            ),
                            value='minecraft:entities/sheep/pink',
                            type='minecraft:loot_table',
                        ),
                        LootPoolEntryLootTable(
                            condition=LootConditionEntityProperties(
                                entity=EntityTarget.THIS,
                                predicate=EntitySubPredicateMap(
                                    components=DataComponentExactPredicate(sheep_color=DyeColor.GRAY),
                                    type_specific_sheep=SheepPredicate(sheared=False),
                                ),
                                type='minecraft:entity_properties',
                            ),
                            value='minecraft:entities/sheep/gray',
                            type='minecraft:loot_table',
                        ),
                        LootPoolEntryLootTable(
                            condition=LootConditionEntityProperties(
                                entity=EntityTarget.THIS,
                                predicate=EntitySubPredicateMap(
                                    components=DataComponentExactPredicate(sheep_color=DyeColor.LIGHTGRAY),
                                    type_specific_sheep=SheepPredicate(sheared=False),
                                ),
                                type='minecraft:entity_properties',
                            ),
                            value='minecraft:entities/sheep/light_gray',
                            type='minecraft:loot_table',
                        ),
                        LootPoolEntryLootTable(
                            condition=LootConditionEntityProperties(
                                entity=EntityTarget.THIS,
                                predicate=EntitySubPredicateMap(
                                    components=DataComponentExactPredicate(sheep_color=DyeColor.CYAN),
                                    type_specific_sheep=SheepPredicate(sheared=False),
                                ),
                                type='minecraft:entity_properties',
                            ),
                            value='minecraft:entities/sheep/cyan',
                            type='minecraft:loot_table',
                        ),
                        LootPoolEntryLootTable(
                            condition=LootConditionEntityProperties(
                                entity=EntityTarget.THIS,
                                predicate=EntitySubPredicateMap(
                                    components=DataComponentExactPredicate(sheep_color=DyeColor.PURPLE),
                                    type_specific_sheep=SheepPredicate(sheared=False),
                                ),
                                type='minecraft:entity_properties',
                            ),
                            value='minecraft:entities/sheep/purple',
                            type='minecraft:loot_table',
                        ),
                        LootPoolEntryLootTable(
                            condition=LootConditionEntityProperties(
                                entity=EntityTarget.THIS,
                                predicate=EntitySubPredicateMap(
                                    components=DataComponentExactPredicate(sheep_color=DyeColor.BLUE),
                                    type_specific_sheep=SheepPredicate(sheared=False),
                                ),
                                type='minecraft:entity_properties',
                            ),
                            value='minecraft:entities/sheep/blue',
                            type='minecraft:loot_table',
                        ),
                        LootPoolEntryLootTable(
                            condition=LootConditionEntityProperties(
                                entity=EntityTarget.THIS,
                                predicate=EntitySubPredicateMap(
                                    components=DataComponentExactPredicate(sheep_color=DyeColor.BROWN),
                                    type_specific_sheep=SheepPredicate(sheared=False),
                                ),
                                type='minecraft:entity_properties',
                            ),
                            value='minecraft:entities/sheep/brown',
                            type='minecraft:loot_table',
                        ),
                        LootPoolEntryLootTable(
                            condition=LootConditionEntityProperties(
                                entity=EntityTarget.THIS,
                                predicate=EntitySubPredicateMap(
                                    components=DataComponentExactPredicate(sheep_color=DyeColor.GREEN),
                                    type_specific_sheep=SheepPredicate(sheared=False),
                                ),
                                type='minecraft:entity_properties',
                            ),
                            value='minecraft:entities/sheep/green',
                            type='minecraft:loot_table',
                        ),
                        LootPoolEntryLootTable(
                            condition=LootConditionEntityProperties(
                                entity=EntityTarget.THIS,
                                predicate=EntitySubPredicateMap(
                                    components=DataComponentExactPredicate(sheep_color=DyeColor.RED),
                                    type_specific_sheep=SheepPredicate(sheared=False),
                                ),
                                type='minecraft:entity_properties',
                            ),
                            value='minecraft:entities/sheep/red',
                            type='minecraft:loot_table',
                        ),
                        LootPoolEntryLootTable(
                            condition=LootConditionEntityProperties(
                                entity=EntityTarget.THIS,
                                predicate=EntitySubPredicateMap(
                                    components=DataComponentExactPredicate(sheep_color=DyeColor.BLACK),
                                    type_specific_sheep=SheepPredicate(sheared=False),
                                ),
                                type='minecraft:entity_properties',
                            ),
                            value='minecraft:entities/sheep/black',
                            type='minecraft:loot_table',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:entities/sheep',
)

SHULKER = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:shulker_shell', type='minecraft:item')],
            condition=LootConditionRandomChanceWithEnchantedBonus(
                unenchanted_chance=0.5,
                enchanted_chance=LevelBasedValueMapLinear(base=0.5625, per_level_above_first=0.0625, type='minecraft:linear'),
                enchantment='minecraft:looting',
                type='minecraft:random_chance_with_enchanted_bonus',
            ),
        ),
    ],
    random_sequence='minecraft:entities/shulker',
)

SILVERFISH = LootTable(type=LootContextParamSets.ENTITY, random_sequence='minecraft:entities/silverfish')

SKELETON = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:arrow',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:bone',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:entities/skeleton',
)

SKELETON_HORSE = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:bone',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:entities/skeleton_horse',
)

SLIME = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    condition=LootConditionInverted(
                        term=LootConditionDamageSourceProperties(
                            predicate=DamageSourcePredicate(source_entity=EntitySubPredicateMap(entity_type='minecraft:frog')),
                            type='minecraft:damage_source_properties',
                        ),
                        type='minecraft:inverted',
                    ),
                    name='minecraft:slime_ball',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    condition=LootConditionDamageSourceProperties(
                        predicate=DamageSourcePredicate(source_entity=EntitySubPredicateMap(entity_type='minecraft:frog')),
                        type='minecraft:damage_source_properties',
                    ),
                    name='minecraft:slime_ball',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionEntityProperties(
                entity=EntityTarget.THIS,
                predicate=EntitySubPredicateMap(type_specific_cube_mob=SlimePredicate(size=1)),
                type='minecraft:entity_properties',
            ),
        ),
    ],
    random_sequence='minecraft:entities/slime',
)

SNIFFER = LootTable(type=LootContextParamSets.ENTITY, random_sequence='minecraft:entities/sniffer')

SNOW_GOLEM = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=15),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:snowball',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:entities/snow_golem',
)

SPIDER = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:string',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=-1, max=1),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:spider_eye',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionKilledByPlayer(type='minecraft:killed_by_player'),
        ),
    ],
    random_sequence='minecraft:entities/spider',
)

SQUID = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:ink_sac',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:entities/squid',
)

STRAY = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:arrow',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:bone',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=1),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            limit=1,
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                        LootFunctionSetPotion(id='minecraft:slowness', type='minecraft:set_potion'),
                    ],
                    name='minecraft:tipped_arrow',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionKilledByPlayer(type='minecraft:killed_by_player'),
        ),
    ],
    random_sequence='minecraft:entities/stray',
)

STRIDER = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=5),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:string',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:entities/strider',
)

SULFUR_CUBE = LootTable(type=LootContextParamSets.ENTITY, random_sequence='minecraft:entities/sulfur_cube')

TADPOLE = LootTable(type=LootContextParamSets.ENTITY, random_sequence='minecraft:entities/tadpole')

TRADER_LLAMA = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:leather',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:entities/trader_llama',
)

TROPICAL_FISH = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:tropical_fish',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:bone_meal', type='minecraft:item')],
            condition=LootConditionRandomChance(chance=0.05, type='minecraft:random_chance'),
        ),
    ],
    random_sequence='minecraft:entities/tropical_fish',
)

TURTLE = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    weight=3,
                    name='minecraft:seagrass',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:bowl', type='minecraft:item')],
            condition=LootConditionDamageSourceProperties(
                predicate=DamageSourcePredicate(tags=[DamageTagPredicate(id='#minecraft:is_lightning', expected=True)]),
                type='minecraft:damage_source_properties',
            ),
        ),
    ],
    random_sequence='minecraft:entities/turtle',
)

VEX = LootTable(type=LootContextParamSets.ENTITY, random_sequence='minecraft:entities/vex')

VILLAGER = LootTable(type=LootContextParamSets.ENTITY, random_sequence='minecraft:entities/villager')

VINDICATOR = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=1),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:emerald',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionKilledByPlayer(type='minecraft:killed_by_player'),
        ),
    ],
    random_sequence='minecraft:entities/vindicator',
)

WANDERING_TRADER = LootTable(type=LootContextParamSets.ENTITY, random_sequence='minecraft:entities/wandering_trader')

WARDEN = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:sculk_catalyst', type='minecraft:item')])],
    random_sequence='minecraft:entities/warden',
)

WITCH = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:glowstone_dust',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:sugar',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:spider_eye',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:glass_bottle',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:gunpowder',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    weight=2,
                    name='minecraft:stick',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=8),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:redstone',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:entities/witch',
)

WITHER = LootTable(type=LootContextParamSets.ENTITY, random_sequence='minecraft:entities/wither')

WITHER_SKELETON = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=-1, max=1),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:coal',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:bone',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:wither_skeleton_skull', type='minecraft:item')],
            condition=LootConditionAllOf(
                terms=[
                    LootConditionKilledByPlayer(type='minecraft:killed_by_player'),
                    LootConditionRandomChanceWithEnchantedBonus(
                        unenchanted_chance=0.025,
                        enchanted_chance=LevelBasedValueMapLinear(base=0.035, per_level_above_first=0.01, type='minecraft:linear'),
                        enchantment='minecraft:looting',
                        type='minecraft:random_chance_with_enchanted_bonus',
                    ),
                ],
                type='minecraft:all_of',
            ),
        ),
    ],
    random_sequence='minecraft:entities/wither_skeleton',
)

WOLF = LootTable(type=LootContextParamSets.ENTITY, random_sequence='minecraft:entities/wolf')

ZOGLIN = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:rotten_flesh',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:entities/zoglin',
)

ZOMBIE = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:rotten_flesh',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=1),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    condition=LootConditionEntityProperties(
                        entity=EntityTarget.THIS,
                        predicate=EntitySubPredicateMap(vehicle=EntitySubPredicateMap(entity_type='minecraft:zombie_horse')),
                        type='minecraft:entity_properties',
                    ),
                    name='minecraft:red_mushroom',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(name='minecraft:iron_ingot', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:carrot', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionFurnaceSmelt(
                        condition=LootConditionAnyOf(
                            terms=[
                                LootConditionEntityProperties(
                                    entity=EntityTarget.THIS,
                                    predicate=EntitySubPredicateMap(flags=EntityFlagsPredicate(is_on_fire=True)),
                                    type='minecraft:entity_properties',
                                ),
                                LootConditionEntityProperties(
                                    entity=EntityTarget.DIRECTATTACKER,
                                    predicate=EntitySubPredicateMap(
                                        equipment={
                                            EquipmentPredicateSlot.MAINHAND: ItemPredicate(
                                                predicates={
                                                    'minecraft:enchantments': [EnchantmentPredicate(enchantments='#minecraft:smelts_loot')],
                                                },
                                            ),
                                        },
                                    ),
                                    type='minecraft:entity_properties',
                                ),
                            ],
                            type='minecraft:any_of',
                        ),
                        type='minecraft:furnace_smelt',
                    ),
                    name='minecraft:potato',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionAllOf(
                terms=[
                    LootConditionKilledByPlayer(type='minecraft:killed_by_player'),
                    LootConditionRandomChanceWithEnchantedBonus(
                        unenchanted_chance=0.025,
                        enchanted_chance=LevelBasedValueMapLinear(base=0.035, per_level_above_first=0.01, type='minecraft:linear'),
                        enchantment='minecraft:looting',
                        type='minecraft:random_chance_with_enchanted_bonus',
                    ),
                ],
                type='minecraft:all_of',
            ),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:music_disc_lava_chicken', type='minecraft:item')],
            condition=LootConditionAllOf(
                terms=[
                    LootConditionKilledByPlayer(type='minecraft:killed_by_player'),
                    LootConditionEntityProperties(
                        entity=EntityTarget.THIS,
                        predicate=EntitySubPredicateMap(
                            flags=EntityFlagsPredicate(is_baby=True),
                            vehicle=EntitySubPredicateMap(entity_type='minecraft:chicken'),
                        ),
                        type='minecraft:entity_properties',
                    ),
                ],
                type='minecraft:all_of',
            ),
        ),
    ],
    random_sequence='minecraft:entities/zombie',
)

ZOMBIE_HORSE = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=3),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:rotten_flesh',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:entities/zombie_horse',
)

ZOMBIE_NAUTILUS = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=3),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:rotten_flesh',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionKilledByPlayer(type='minecraft:killed_by_player'),
        ),
    ],
    random_sequence='minecraft:entities/zombie_nautilus',
)

ZOMBIE_VILLAGER = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:rotten_flesh',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(name='minecraft:iron_ingot', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:carrot', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionFurnaceSmelt(
                        condition=LootConditionAnyOf(
                            terms=[
                                LootConditionEntityProperties(
                                    entity=EntityTarget.THIS,
                                    predicate=EntitySubPredicateMap(flags=EntityFlagsPredicate(is_on_fire=True)),
                                    type='minecraft:entity_properties',
                                ),
                                LootConditionEntityProperties(
                                    entity=EntityTarget.DIRECTATTACKER,
                                    predicate=EntitySubPredicateMap(
                                        equipment={
                                            EquipmentPredicateSlot.MAINHAND: ItemPredicate(
                                                predicates={
                                                    'minecraft:enchantments': [EnchantmentPredicate(enchantments='#minecraft:smelts_loot')],
                                                },
                                            ),
                                        },
                                    ),
                                    type='minecraft:entity_properties',
                                ),
                            ],
                            type='minecraft:any_of',
                        ),
                        type='minecraft:furnace_smelt',
                    ),
                    name='minecraft:potato',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionAllOf(
                terms=[
                    LootConditionKilledByPlayer(type='minecraft:killed_by_player'),
                    LootConditionRandomChanceWithEnchantedBonus(
                        unenchanted_chance=0.025,
                        enchanted_chance=LevelBasedValueMapLinear(base=0.035, per_level_above_first=0.01, type='minecraft:linear'),
                        enchantment='minecraft:looting',
                        type='minecraft:random_chance_with_enchanted_bonus',
                    ),
                ],
                type='minecraft:all_of',
            ),
        ),
    ],
    random_sequence='minecraft:entities/zombie_villager',
)

ZOMBIFIED_PIGLIN = LootTable(
    type=LootContextParamSets.ENTITY,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=1),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:rotten_flesh',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=1),
                            type='minecraft:set_count',
                        ),
                        LootFunctionEnchantedCountIncrease(
                            count=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.0, max=1.0),
                            enchantment='minecraft:looting',
                            type='minecraft:enchanted_count_increase',
                        ),
                    ],
                    name='minecraft:gold_nugget',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:gold_ingot', type='minecraft:item')],
            condition=LootConditionAllOf(
                terms=[
                    LootConditionKilledByPlayer(type='minecraft:killed_by_player'),
                    LootConditionRandomChanceWithEnchantedBonus(
                        unenchanted_chance=0.025,
                        enchanted_chance=LevelBasedValueMapLinear(base=0.035, per_level_above_first=0.01, type='minecraft:linear'),
                        enchantment='minecraft:looting',
                        type='minecraft:random_chance_with_enchanted_bonus',
                    ),
                ],
                type='minecraft:all_of',
            ),
        ),
    ],
    random_sequence='minecraft:entities/zombified_piglin',
)
