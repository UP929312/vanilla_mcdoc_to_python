"""Vanilla's data/loot_table/chests/ files"""
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.advancement.predicate.LocationPredicate import LocationPredicate
from vanilla_mcdoc.data.loot.LootContextParamSets import LootContextParamSets
from vanilla_mcdoc.data.loot.LootPool import LootPool
from vanilla_mcdoc.data.loot.LootPoolEntry import LootPoolEntryEmpty, LootPoolEntryItem
from vanilla_mcdoc.data.loot.LootTable import LootTable
from vanilla_mcdoc.data.loot.condition.LootCondition import LootConditionInverted, LootConditionLocationCheck
from vanilla_mcdoc.data.loot.function.LootFunction import LootFunctionDiscard, LootFunctionEnchantRandomly, LootFunctionEnchantWithLevels, LootFunctionExplorationMap, LootFunctionFiltered, LootFunctionSetCount, LootFunctionSetDamage, LootFunctionSetInstrument, LootFunctionSetName, LootFunctionSetPotion, LootFunctionSetStewEffect
from vanilla_mcdoc.data.loot.function.SetNameTarget import SetNameTarget
from vanilla_mcdoc.data.loot.function.StewEffect import StewEffect
from vanilla_mcdoc.data.number_provider.context_float.ContextFloatProvider import ContextFloatProviderStructUniform
from vanilla_mcdoc.data.number_provider.context_int.ContextIntProvider import ContextIntProviderStructUniform
from vanilla_mcdoc.util.text.TextObject import TextObjectStruct2

ABANDONED_CAMP_COMMON_CHEST = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=6),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=4, type='minecraft:set_count'),
                    name='minecraft:arrow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:map',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=4),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:bone',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:cobweb',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:compass',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:map',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=4),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:gunpowder',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:fishing_rod',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:flint_and_steel',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:glass_bottle',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:lead',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:leather',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:bundle',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:rabbit_hide',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:saddle',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:white_candle',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=2,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:bow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:bucket',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:copper_axe',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:copper_boots',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:copper_chestplate',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:copper_leggings',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:copper_spear',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:copper_sword',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:spyglass',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:shears',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetName(
                            name=TextObjectStruct2(translate='filled_map.bamboo_camp_map'),
                            target=SetNameTarget.ITEMNAME,
                            type='minecraft:set_name',
                        ),
                        LootFunctionExplorationMap(
                            destination='#minecraft:on_abandoned_camp_bamboo_jungle',
                            decoration='minecraft:abandoned_camp',
                            type='minecraft:exploration_map',
                        ),
                        LootFunctionFiltered(
                            item_filter=ItemPredicate(predicates={'minecraft:map_id': {}}),
                            on_fail=LootFunctionDiscard(type='minecraft:discard'),
                            type='minecraft:filtered',
                        ),
                    ],
                    condition=LootConditionInverted(
                        term=LootConditionLocationCheck(
                            predicate=LocationPredicate(biomes='minecraft:bamboo_jungle'),
                            type='minecraft:location_check',
                        ),
                        type='minecraft:inverted',
                    ),
                    name='minecraft:abandoned_camp_map',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetName(
                            name=TextObjectStruct2(translate='filled_map.cherry_grove_camp_map'),
                            target=SetNameTarget.ITEMNAME,
                            type='minecraft:set_name',
                        ),
                        LootFunctionExplorationMap(
                            destination='#minecraft:on_abandoned_camp_cherry_grove',
                            decoration='minecraft:abandoned_camp',
                            type='minecraft:exploration_map',
                        ),
                        LootFunctionFiltered(
                            item_filter=ItemPredicate(predicates={'minecraft:map_id': {}}),
                            on_fail=LootFunctionDiscard(type='minecraft:discard'),
                            type='minecraft:filtered',
                        ),
                    ],
                    condition=LootConditionInverted(
                        term=LootConditionLocationCheck(
                            predicate=LocationPredicate(biomes='minecraft:cherry_grove'),
                            type='minecraft:location_check',
                        ),
                        type='minecraft:inverted',
                    ),
                    name='minecraft:abandoned_camp_map',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetName(
                            name=TextObjectStruct2(translate='filled_map.birch_forest_camp_map'),
                            target=SetNameTarget.ITEMNAME,
                            type='minecraft:set_name',
                        ),
                        LootFunctionExplorationMap(
                            destination='#minecraft:on_abandoned_camp_birch_forest',
                            decoration='minecraft:abandoned_camp',
                            type='minecraft:exploration_map',
                        ),
                        LootFunctionFiltered(
                            item_filter=ItemPredicate(predicates={'minecraft:map_id': {}}),
                            on_fail=LootFunctionDiscard(type='minecraft:discard'),
                            type='minecraft:filtered',
                        ),
                    ],
                    condition=LootConditionInverted(
                        term=LootConditionLocationCheck(
                            predicate=LocationPredicate(biomes='minecraft:birch_forest'),
                            type='minecraft:location_check',
                        ),
                        type='minecraft:inverted',
                    ),
                    name='minecraft:abandoned_camp_map',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetName(
                            name=TextObjectStruct2(translate='filled_map.dappled_forest_camp_map'),
                            target=SetNameTarget.ITEMNAME,
                            type='minecraft:set_name',
                        ),
                        LootFunctionExplorationMap(
                            destination='#minecraft:on_abandoned_camp_dappled_forest',
                            decoration='minecraft:abandoned_camp',
                            type='minecraft:exploration_map',
                        ),
                        LootFunctionFiltered(
                            item_filter=ItemPredicate(predicates={'minecraft:map_id': {}}),
                            on_fail=LootFunctionDiscard(type='minecraft:discard'),
                            type='minecraft:filtered',
                        ),
                    ],
                    condition=LootConditionInverted(
                        term=LootConditionLocationCheck(
                            predicate=LocationPredicate(biomes='minecraft:dappled_forest'),
                            type='minecraft:location_check',
                        ),
                        type='minecraft:inverted',
                    ),
                    name='minecraft:abandoned_camp_map',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetName(
                            name=TextObjectStruct2(translate='filled_map.flower_forest_camp_map'),
                            target=SetNameTarget.ITEMNAME,
                            type='minecraft:set_name',
                        ),
                        LootFunctionExplorationMap(
                            destination='#minecraft:on_abandoned_camp_flower_forest',
                            decoration='minecraft:abandoned_camp',
                            type='minecraft:exploration_map',
                        ),
                        LootFunctionFiltered(
                            item_filter=ItemPredicate(predicates={'minecraft:map_id': {}}),
                            on_fail=LootFunctionDiscard(type='minecraft:discard'),
                            type='minecraft:filtered',
                        ),
                    ],
                    condition=LootConditionInverted(
                        term=LootConditionLocationCheck(
                            predicate=LocationPredicate(biomes='minecraft:flower_forest'),
                            type='minecraft:location_check',
                        ),
                        type='minecraft:inverted',
                    ),
                    name='minecraft:abandoned_camp_map',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetName(
                            name=TextObjectStruct2(translate='filled_map.pale_garden_camp_map'),
                            target=SetNameTarget.ITEMNAME,
                            type='minecraft:set_name',
                        ),
                        LootFunctionExplorationMap(
                            destination='#minecraft:on_abandoned_camp_pale_garden',
                            decoration='minecraft:abandoned_camp',
                            type='minecraft:exploration_map',
                        ),
                        LootFunctionFiltered(
                            item_filter=ItemPredicate(predicates={'minecraft:map_id': {}}),
                            on_fail=LootFunctionDiscard(type='minecraft:discard'),
                            type='minecraft:filtered',
                        ),
                    ],
                    condition=LootConditionInverted(
                        term=LootConditionLocationCheck(
                            predicate=LocationPredicate(biomes='minecraft:pale_garden'),
                            type='minecraft:location_check',
                        ),
                        type='minecraft:inverted',
                    ),
                    name='minecraft:abandoned_camp_map',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetName(
                            name=TextObjectStruct2(translate='filled_map.swamp_camp_map'),
                            target=SetNameTarget.ITEMNAME,
                            type='minecraft:set_name',
                        ),
                        LootFunctionExplorationMap(
                            destination='#minecraft:on_abandoned_camp_swamp',
                            decoration='minecraft:abandoned_camp',
                            type='minecraft:exploration_map',
                        ),
                        LootFunctionFiltered(
                            item_filter=ItemPredicate(predicates={'minecraft:map_id': {}}),
                            on_fail=LootFunctionDiscard(type='minecraft:discard'),
                            type='minecraft:filtered',
                        ),
                    ],
                    condition=LootConditionInverted(
                        term=LootConditionLocationCheck(
                            predicate=LocationPredicate(biomes='minecraft:swamp'),
                            type='minecraft:location_check',
                        ),
                        type='minecraft:inverted',
                    ),
                    name='minecraft:abandoned_camp_map',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetName(
                            name=TextObjectStruct2(translate='filled_map.windswept_forest_camp_map'),
                            target=SetNameTarget.ITEMNAME,
                            type='minecraft:set_name',
                        ),
                        LootFunctionExplorationMap(
                            destination='#minecraft:on_abandoned_camp_windswept_forest',
                            decoration='minecraft:abandoned_camp',
                            type='minecraft:exploration_map',
                        ),
                        LootFunctionFiltered(
                            item_filter=ItemPredicate(predicates={'minecraft:map_id': {}}),
                            on_fail=LootFunctionDiscard(type='minecraft:discard'),
                            type='minecraft:filtered',
                        ),
                    ],
                    condition=LootConditionInverted(
                        term=LootConditionLocationCheck(
                            predicate=LocationPredicate(biomes='minecraft:windswept_forest'),
                            type='minecraft:location_check',
                        ),
                        type='minecraft:inverted',
                    ),
                    name='minecraft:abandoned_camp_map',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:chests/abandoned_camp_common_chest',
)

ABANDONED_CAMP_SECRET_CHEST = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=2,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:diamond',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionSetPotion(id='minecraft:healing', type='minecraft:set_potion'),
                    ],
                    name='minecraft:potion',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionSetPotion(id='minecraft:leaping', type='minecraft:set_potion'),
                    ],
                    name='minecraft:potion',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionSetPotion(id='minecraft:night_vision', type='minecraft:set_potion'),
                    ],
                    name='minecraft:potion',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionSetPotion(id='minecraft:swiftness', type='minecraft:set_potion'),
                    ],
                    name='minecraft:potion',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=6),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:map',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:copper_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:gold_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:iron_ingot',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=1),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:iron_axe',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:iron_boots',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:iron_leggings',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:iron_spear',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionExplorationMap(
                            destination='#minecraft:on_ancient_city_maps',
                            decoration='minecraft:ancient_city',
                            type='minecraft:exploration_map',
                        ),
                        LootFunctionFiltered(
                            item_filter=ItemPredicate(predicates={'minecraft:map_id': {}}),
                            on_fail=LootFunctionDiscard(type='minecraft:discard'),
                            type='minecraft:filtered',
                        ),
                    ],
                    name='minecraft:buried_ancient_city_map',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionExplorationMap(
                            destination='#minecraft:on_buried_trial_chambers_maps',
                            decoration='minecraft:trial_chambers',
                            type='minecraft:exploration_map',
                        ),
                        LootFunctionFiltered(
                            item_filter=ItemPredicate(predicates={'minecraft:map_id': {}}),
                            on_fail=LootFunctionDiscard(type='minecraft:discard'),
                            type='minecraft:filtered',
                        ),
                    ],
                    name='minecraft:buried_trial_chambers_map',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionExplorationMap(
                            destination='#minecraft:on_mineshaft_maps',
                            decoration='minecraft:mineshaft',
                            type='minecraft:exploration_map',
                        ),
                        LootFunctionFiltered(
                            item_filter=ItemPredicate(predicates={'minecraft:map_id': {}}),
                            on_fail=LootFunctionDiscard(type='minecraft:discard'),
                            type='minecraft:filtered',
                        ),
                    ],
                    name='minecraft:buried_mineshaft_map',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionExplorationMap(
                            destination='#minecraft:on_desert_pyramid_maps',
                            decoration='minecraft:desert_pyramid',
                            type='minecraft:exploration_map',
                        ),
                        LootFunctionFiltered(
                            item_filter=ItemPredicate(predicates={'minecraft:map_id': {}}),
                            on_fail=LootFunctionDiscard(type='minecraft:discard'),
                            type='minecraft:filtered',
                        ),
                    ],
                    name='minecraft:desert_pyramid_map',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionExplorationMap(
                            destination='#minecraft:on_jungle_pyramid_maps',
                            decoration='minecraft:jungle_temple',
                            type='minecraft:exploration_map',
                        ),
                        LootFunctionFiltered(
                            item_filter=ItemPredicate(predicates={'minecraft:map_id': {}}),
                            on_fail=LootFunctionDiscard(type='minecraft:discard'),
                            type='minecraft:filtered',
                        ),
                    ],
                    name='minecraft:jungle_pyramid_map',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionExplorationMap(
                            destination='#minecraft:on_ocean_ruin_warm_maps',
                            decoration='minecraft:ocean_ruin_warm',
                            type='minecraft:exploration_map',
                        ),
                        LootFunctionFiltered(
                            item_filter=ItemPredicate(predicates={'minecraft:map_id': {}}),
                            on_fail=LootFunctionDiscard(type='minecraft:discard'),
                            type='minecraft:filtered',
                        ),
                    ],
                    name='minecraft:warm_ocean_ruins_map',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionExplorationMap(
                            destination='#minecraft:on_woodland_mansion_maps',
                            type='minecraft:exploration_map',
                        ),
                        LootFunctionFiltered(
                            item_filter=ItemPredicate(predicates={'minecraft:map_id': {}}),
                            on_fail=LootFunctionDiscard(type='minecraft:discard'),
                            type='minecraft:filtered',
                        ),
                    ],
                    name='minecraft:woodland_mansion_map',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:chests/abandoned_camp_secret_chest',
)

ABANDONED_MINESHAFT = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(weight=20, name='minecraft:golden_apple', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:enchanted_golden_apple', type='minecraft:item'),
                LootPoolEntryItem(weight=30, name='minecraft:name_tag', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(options='#minecraft:on_random_loot', type='minecraft:enchant_randomly'),
                    weight=10,
                    name='minecraft:book',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=5, name='minecraft:iron_pickaxe', type='minecraft:item'),
                LootPoolEntryEmpty(weight=5, type='minecraft:empty'),
            ],
        ),
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=4),
            entries=[
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
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=9),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:redstone',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=9),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:lapis_lazuli',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:diamond',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:coal',
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
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=6),
                        type='minecraft:set_count',
                    ),
                    weight=15,
                    name='minecraft:glow_berries',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:melon_seeds',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:pumpkin_seeds',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:beetroot_seeds',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=3,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=20,
                    name='minecraft:rail',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:powered_rail',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:detector_rail',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:activator_rail',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=16),
                        type='minecraft:set_count',
                    ),
                    weight=15,
                    name='minecraft:torch',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    condition=LootConditionLocationCheck(
                        predicate=LocationPredicate(biomes='minecraft:sulfur_caves'),
                        type='minecraft:location_check',
                    ),
                    weight=10,
                    name='minecraft:music_disc_bounce',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:chests/abandoned_mineshaft',
)

ANCIENT_CITY = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=5, max=10),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:enchanted_golden_apple',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(name='minecraft:music_disc_otherside', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=2,
                    name='minecraft:compass',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:sculk_catalyst',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionSetDamage(
                            damage=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.8, max=1.0),
                            type='minecraft:set_damage',
                        ),
                        LootFunctionEnchantWithLevels(
                            levels=ContextIntProviderStructUniform(type='minecraft:uniform', min=30, max=50),
                            options='#minecraft:on_random_loot',
                            type='minecraft:enchant_with_levels',
                        ),
                    ],
                    weight=2,
                    name='minecraft:diamond_hoe',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=2,
                    name='minecraft:lead',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=2,
                    name='minecraft:diamond_horse_armor',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=5),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:leather',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=2, name='minecraft:music_disc_13', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:music_disc_cat', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantWithLevels(
                        levels=ContextIntProviderStructUniform(type='minecraft:uniform', min=30, max=50),
                        options='#minecraft:on_random_loot',
                        type='minecraft:enchant_with_levels',
                    ),
                    weight=2,
                    name='minecraft:diamond_leggings',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(options='minecraft:swift_sneak', type='minecraft:enchant_randomly'),
                    weight=3,
                    name='minecraft:book',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=10),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:sculk',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:sculk_sensor',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:candle',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=15),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:amethyst_shard',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:experience_bottle',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=15),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:glow_berries',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantWithLevels(
                        levels=ContextIntProviderStructUniform(type='minecraft:uniform', min=20, max=39),
                        options='#minecraft:on_random_loot',
                        type='minecraft:enchant_with_levels',
                    ),
                    weight=3,
                    name='minecraft:iron_leggings',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=4,
                    name='minecraft:echo_shard',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=4,
                    name='minecraft:disc_fragment_5',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetPotion(id='minecraft:strong_regeneration', type='minecraft:set_potion'),
                    ],
                    weight=5,
                    name='minecraft:potion',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(options='#minecraft:on_random_loot', type='minecraft:enchant_randomly'),
                    weight=5,
                    name='minecraft:book',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=10),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:book',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=15),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:bone',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=15),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:soul_torch',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=6, max=15),
                        type='minecraft:set_count',
                    ),
                    weight=7,
                    name='minecraft:coal',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryEmpty(weight=75, type='minecraft:empty'),
                LootPoolEntryItem(weight=4, name='minecraft:ward_armor_trim_smithing_template', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:silence_armor_trim_smithing_template', type='minecraft:item'),
            ],
        ),
    ],
    random_sequence='minecraft:chests/ancient_city',
)

ANCIENT_CITY_ICE_BOX = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=10),
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetStewEffect(
                            effects=[
                                StewEffect(
                                    type='minecraft:night_vision',
                                    duration=ContextIntProviderStructUniform(type='minecraft:uniform', min=7, max=10),
                                ),
                                StewEffect(
                                    type='minecraft:blindness',
                                    duration=ContextIntProviderStructUniform(type='minecraft:uniform', min=5, max=7),
                                ),
                            ],
                            type='minecraft:set_stew_effect',
                        ),
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=6),
                            type='minecraft:set_count',
                        ),
                    ],
                    name='minecraft:suspicious_stew',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=10),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:golden_carrot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=10),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:baked_potato',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=6),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:packed_ice',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=6),
                        type='minecraft:set_count',
                    ),
                    weight=4,
                    name='minecraft:snowball',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:chests/ancient_city_ice_box',
)

BASTION_BRIDGE = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:lodestone',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetDamage(
                            damage=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.1, max=0.5),
                            type='minecraft:set_damage',
                        ),
                        LootFunctionEnchantRandomly(
                            options='#minecraft:on_random_loot',
                            type='minecraft:enchant_randomly',
                        ),
                    ],
                    name='minecraft:crossbow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=10, max=28),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:spectral_arrow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=8, max=12),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:gilded_blackstone',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=8),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:crying_obsidian',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:gold_block',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=9),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:gold_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=9),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:iron_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:golden_sword',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionEnchantRandomly(
                            options='#minecraft:on_random_loot',
                            type='minecraft:enchant_randomly',
                        ),
                    ],
                    name='minecraft:golden_chestplate',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionEnchantRandomly(
                            options='#minecraft:on_random_loot',
                            type='minecraft:enchant_randomly',
                        ),
                    ],
                    name='minecraft:golden_helmet',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionEnchantRandomly(
                            options='#minecraft:on_random_loot',
                            type='minecraft:enchant_randomly',
                        ),
                    ],
                    name='minecraft:golden_leggings',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionEnchantRandomly(
                            options='#minecraft:on_random_loot',
                            type='minecraft:enchant_randomly',
                        ),
                    ],
                    name='minecraft:golden_boots',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionEnchantRandomly(
                            options='#minecraft:on_random_loot',
                            type='minecraft:enchant_randomly',
                        ),
                    ],
                    name='minecraft:golden_axe',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=4),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=6),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:string',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:leather',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=5, max=17),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:arrow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=6),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:iron_nugget',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=6),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:gold_nugget',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryEmpty(weight=11, type='minecraft:empty'),
                LootPoolEntryItem(name='minecraft:snout_armor_trim_smithing_template', type='minecraft:item'),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryEmpty(weight=9, type='minecraft:empty'),
                LootPoolEntryItem(name='minecraft:netherite_upgrade_smithing_template', type='minecraft:item'),
            ],
        ),
    ],
    random_sequence='minecraft:chests/bastion_bridge',
)

BASTION_HOGLIN_STABLE = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetDamage(
                            damage=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.15, max=0.8),
                            type='minecraft:set_damage',
                        ),
                        LootFunctionEnchantRandomly(
                            options='#minecraft:on_random_loot',
                            type='minecraft:enchant_randomly',
                        ),
                    ],
                    weight=15,
                    name='minecraft:diamond_shovel',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetDamage(
                            damage=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.15, max=0.95),
                            type='minecraft:set_damage',
                        ),
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionEnchantRandomly(
                            options='#minecraft:on_random_loot',
                            type='minecraft:enchant_randomly',
                        ),
                    ],
                    weight=12,
                    name='minecraft:diamond_pickaxe',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=8,
                    name='minecraft:netherite_scrap',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=12,
                    name='minecraft:ancient_debris',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=2, type='minecraft:set_count'),
                    weight=5,
                    name='minecraft:ancient_debris',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=12,
                    name='minecraft:saddle',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=16,
                    name='minecraft:gold_block',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=8, max=17),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:golden_carrot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=10,
                    name='minecraft:golden_apple',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=4),
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionEnchantRandomly(
                            options='#minecraft:on_random_loot',
                            type='minecraft:enchant_randomly',
                        ),
                    ],
                    name='minecraft:golden_axe',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=5),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:crying_obsidian',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=6),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:glowstone',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=5),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:gilded_blackstone',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=7),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:soul_sand',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=7),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:crimson_nylium',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=8),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:gold_nugget',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:leather',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=5, max=17),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:arrow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=8),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:string',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=5),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:porkchop',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=5),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:cooked_porkchop',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=7),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:crimson_fungus',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=7),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:crimson_roots',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryEmpty(weight=11, type='minecraft:empty'),
                LootPoolEntryItem(name='minecraft:snout_armor_trim_smithing_template', type='minecraft:item'),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryEmpty(weight=9, type='minecraft:empty'),
                LootPoolEntryItem(name='minecraft:netherite_upgrade_smithing_template', type='minecraft:item'),
            ],
        ),
    ],
    random_sequence='minecraft:chests/bastion_hoglin_stable',
)

BASTION_OTHER = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionEnchantRandomly(
                            options='#minecraft:on_random_loot',
                            type='minecraft:enchant_randomly',
                        ),
                    ],
                    weight=6,
                    name='minecraft:diamond_pickaxe',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=6,
                    name='minecraft:diamond_shovel',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetDamage(
                            damage=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.1, max=0.9),
                            type='minecraft:set_damage',
                        ),
                        LootFunctionEnchantRandomly(
                            options='#minecraft:on_random_loot',
                            type='minecraft:enchant_randomly',
                        ),
                    ],
                    weight=6,
                    name='minecraft:crossbow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=12,
                    name='minecraft:ancient_debris',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=4,
                    name='minecraft:netherite_scrap',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=10, max=22),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:spectral_arrow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=9,
                    name='minecraft:piglin_banner_pattern',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=5,
                    name='minecraft:music_disc_pigstep',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=6, max=17),
                        type='minecraft:set_count',
                    ),
                    weight=12,
                    name='minecraft:golden_carrot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=9,
                    name='minecraft:golden_apple',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(options='minecraft:soul_speed', type='minecraft:enchant_randomly'),
                    weight=10,
                    name='minecraft:book',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=2,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetDamage(
                            damage=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.1, max=0.9),
                            type='minecraft:set_damage',
                        ),
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionEnchantRandomly(
                            options='#minecraft:on_random_loot',
                            type='minecraft:enchant_randomly',
                        ),
                    ],
                    weight=2,
                    name='minecraft:iron_sword',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=2,
                    name='minecraft:iron_block',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionEnchantRandomly(options='minecraft:soul_speed', type='minecraft:enchant_randomly'),
                    ],
                    name='minecraft:golden_boots',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionEnchantRandomly(
                            options='#minecraft:on_random_loot',
                            type='minecraft:enchant_randomly',
                        ),
                    ],
                    name='minecraft:golden_axe',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=2,
                    name='minecraft:gold_block',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:crossbow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=6),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:gold_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=6),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:iron_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:golden_sword',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:golden_chestplate',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:golden_helmet',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:golden_leggings',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:golden_boots',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=5),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:crying_obsidian',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=4),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=5),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:gilded_blackstone',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=10),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:iron_chain',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=6),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:magma_cream',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=6),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:bone_block',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=8),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:iron_nugget',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=6),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:obsidian',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=8),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:gold_nugget',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=6),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:string',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=5, max=17),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:arrow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:cooked_porkchop',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryEmpty(weight=11, type='minecraft:empty'),
                LootPoolEntryItem(name='minecraft:snout_armor_trim_smithing_template', type='minecraft:item'),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryEmpty(weight=9, type='minecraft:empty'),
                LootPoolEntryItem(name='minecraft:netherite_upgrade_smithing_template', type='minecraft:item'),
            ],
        ),
    ],
    random_sequence='minecraft:chests/bastion_other',
)

BASTION_TREASURE = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=3,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=15,
                    name='minecraft:netherite_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=10,
                    name='minecraft:ancient_debris',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=8,
                    name='minecraft:netherite_scrap',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=2, type='minecraft:set_count'),
                    weight=4,
                    name='minecraft:ancient_debris',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetDamage(
                            damage=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.8, max=1.0),
                            type='minecraft:set_damage',
                        ),
                        LootFunctionEnchantRandomly(
                            options='#minecraft:on_random_loot',
                            type='minecraft:enchant_randomly',
                        ),
                    ],
                    weight=6,
                    name='minecraft:diamond_sword',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetDamage(
                            damage=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.8, max=1.0),
                            type='minecraft:set_damage',
                        ),
                        LootFunctionEnchantRandomly(
                            options='#minecraft:on_random_loot',
                            type='minecraft:enchant_randomly',
                        ),
                    ],
                    weight=6,
                    name='minecraft:diamond_spear',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetDamage(
                            damage=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.8, max=1.0),
                            type='minecraft:set_damage',
                        ),
                        LootFunctionEnchantRandomly(
                            options='#minecraft:on_random_loot',
                            type='minecraft:enchant_randomly',
                        ),
                    ],
                    weight=6,
                    name='minecraft:diamond_chestplate',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetDamage(
                            damage=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.8, max=1.0),
                            type='minecraft:set_damage',
                        ),
                        LootFunctionEnchantRandomly(
                            options='#minecraft:on_random_loot',
                            type='minecraft:enchant_randomly',
                        ),
                    ],
                    weight=6,
                    name='minecraft:diamond_helmet',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetDamage(
                            damage=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.8, max=1.0),
                            type='minecraft:set_damage',
                        ),
                        LootFunctionEnchantRandomly(
                            options='#minecraft:on_random_loot',
                            type='minecraft:enchant_randomly',
                        ),
                    ],
                    weight=6,
                    name='minecraft:diamond_leggings',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetDamage(
                            damage=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.8, max=1.0),
                            type='minecraft:set_damage',
                        ),
                        LootFunctionEnchantRandomly(
                            options='#minecraft:on_random_loot',
                            type='minecraft:enchant_randomly',
                        ),
                    ],
                    weight=6,
                    name='minecraft:diamond_boots',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=6, name='minecraft:diamond_sword', type='minecraft:item'),
                LootPoolEntryItem(weight=6, name='minecraft:diamond_spear', type='minecraft:item'),
                LootPoolEntryItem(weight=5, name='minecraft:diamond_chestplate', type='minecraft:item'),
                LootPoolEntryItem(weight=5, name='minecraft:diamond_helmet', type='minecraft:item'),
                LootPoolEntryItem(weight=5, name='minecraft:diamond_boots', type='minecraft:item'),
                LootPoolEntryItem(weight=5, name='minecraft:diamond_leggings', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=6),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:diamond',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=2,
                    name='minecraft:enchanted_golden_apple',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=4),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=12, max=25),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:spectral_arrow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=5),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:gold_block',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=5),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:iron_block',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=9),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:gold_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=9),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:iron_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=5),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:crying_obsidian',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=8, max=23),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:quartz',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=5, max=15),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:gilded_blackstone',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=8),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:magma_cream',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryEmpty(weight=11, type='minecraft:empty'),
                LootPoolEntryItem(name='minecraft:snout_armor_trim_smithing_template', type='minecraft:item'),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:netherite_upgrade_smithing_template', type='minecraft:item')],
        ),
    ],
    random_sequence='minecraft:chests/bastion_treasure',
)

BURIED_TREASURE = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:heart_of_the_sea', type='minecraft:item')]),
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=5, max=8),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=20,
                    name='minecraft:iron_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:gold_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:tnt',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:emerald',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:diamond',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=5),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:prismarine_crystals',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=1),
            entries=[
                LootPoolEntryItem(name='minecraft:leather_chestplate', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:iron_sword', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:iron_spear', type='minecraft:item'),
            ],
        ),
        LootPool(
            rolls=2,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=4),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:cooked_cod',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=4),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:cooked_salmon',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
            entries=[LootPoolEntryItem(name='minecraft:potion', type='minecraft:item')],
            modifier=LootFunctionSetPotion(id='minecraft:water_breathing', type='minecraft:set_potion'),
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryEmpty(weight=148, type='minecraft:empty'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=20,
                    name='minecraft:copper_nautilus_armor',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=10,
                    name='minecraft:iron_nautilus_armor',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=5,
                    name='minecraft:golden_nautilus_armor',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=2,
                    name='minecraft:diamond_nautilus_armor',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:chests/buried_treasure',
)

DESERT_PYRAMID = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=4),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:diamond',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=5),
                        type='minecraft:set_count',
                    ),
                    weight=15,
                    name='minecraft:iron_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=7),
                        type='minecraft:set_count',
                    ),
                    weight=15,
                    name='minecraft:gold_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=15,
                    name='minecraft:emerald',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=6),
                        type='minecraft:set_count',
                    ),
                    weight=25,
                    name='minecraft:bone',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=25,
                    name='minecraft:spider_eye',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=7),
                        type='minecraft:set_count',
                    ),
                    weight=25,
                    name='minecraft:rotten_flesh',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=5),
                        type='minecraft:set_count',
                    ),
                    weight=20,
                    name='minecraft:leather',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=15, name='minecraft:copper_horse_armor', type='minecraft:item'),
                LootPoolEntryItem(weight=15, name='minecraft:iron_horse_armor', type='minecraft:item'),
                LootPoolEntryItem(weight=10, name='minecraft:golden_horse_armor', type='minecraft:item'),
                LootPoolEntryItem(weight=5, name='minecraft:diamond_horse_armor', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(options='#minecraft:on_random_loot', type='minecraft:enchant_randomly'),
                    weight=20,
                    name='minecraft:book',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=20, name='minecraft:golden_apple', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:enchanted_golden_apple', type='minecraft:item'),
                LootPoolEntryEmpty(weight=15, type='minecraft:empty'),
            ],
        ),
        LootPool(
            rolls=4,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:bone',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:gunpowder',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:rotten_flesh',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:string',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:sand',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryEmpty(weight=6, type='minecraft:empty'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=2, type='minecraft:set_count'),
                    name='minecraft:dune_armor_trim_smithing_template',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:chests/desert_pyramid',
)

END_CITY_TREASURE = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=6),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=7),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:diamond',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:iron_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=7),
                        type='minecraft:set_count',
                    ),
                    weight=15,
                    name='minecraft:gold_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=6),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:emerald',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=10),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:beetroot_seeds',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=3, name='minecraft:saddle', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:copper_horse_armor', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:iron_horse_armor', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:golden_horse_armor', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:diamond_horse_armor', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantWithLevels(
                        levels=ContextIntProviderStructUniform(type='minecraft:uniform', min=20, max=39),
                        options='#minecraft:on_random_loot',
                        type='minecraft:enchant_with_levels',
                    ),
                    weight=3,
                    name='minecraft:diamond_sword',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantWithLevels(
                        levels=ContextIntProviderStructUniform(type='minecraft:uniform', min=20, max=39),
                        options='#minecraft:on_random_loot',
                        type='minecraft:enchant_with_levels',
                    ),
                    weight=3,
                    name='minecraft:diamond_spear',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantWithLevels(
                        levels=ContextIntProviderStructUniform(type='minecraft:uniform', min=20, max=39),
                        options='#minecraft:on_random_loot',
                        type='minecraft:enchant_with_levels',
                    ),
                    weight=3,
                    name='minecraft:diamond_boots',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantWithLevels(
                        levels=ContextIntProviderStructUniform(type='minecraft:uniform', min=20, max=39),
                        options='#minecraft:on_random_loot',
                        type='minecraft:enchant_with_levels',
                    ),
                    weight=3,
                    name='minecraft:diamond_chestplate',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantWithLevels(
                        levels=ContextIntProviderStructUniform(type='minecraft:uniform', min=20, max=39),
                        options='#minecraft:on_random_loot',
                        type='minecraft:enchant_with_levels',
                    ),
                    weight=3,
                    name='minecraft:diamond_leggings',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantWithLevels(
                        levels=ContextIntProviderStructUniform(type='minecraft:uniform', min=20, max=39),
                        options='#minecraft:on_random_loot',
                        type='minecraft:enchant_with_levels',
                    ),
                    weight=3,
                    name='minecraft:diamond_helmet',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantWithLevels(
                        levels=ContextIntProviderStructUniform(type='minecraft:uniform', min=20, max=39),
                        options='#minecraft:on_random_loot',
                        type='minecraft:enchant_with_levels',
                    ),
                    weight=3,
                    name='minecraft:diamond_pickaxe',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantWithLevels(
                        levels=ContextIntProviderStructUniform(type='minecraft:uniform', min=20, max=39),
                        options='#minecraft:on_random_loot',
                        type='minecraft:enchant_with_levels',
                    ),
                    weight=3,
                    name='minecraft:diamond_shovel',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantWithLevels(
                        levels=ContextIntProviderStructUniform(type='minecraft:uniform', min=20, max=39),
                        options='#minecraft:on_random_loot',
                        type='minecraft:enchant_with_levels',
                    ),
                    weight=3,
                    name='minecraft:iron_sword',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantWithLevels(
                        levels=ContextIntProviderStructUniform(type='minecraft:uniform', min=20, max=39),
                        options='#minecraft:on_random_loot',
                        type='minecraft:enchant_with_levels',
                    ),
                    weight=3,
                    name='minecraft:iron_boots',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantWithLevels(
                        levels=ContextIntProviderStructUniform(type='minecraft:uniform', min=20, max=39),
                        options='#minecraft:on_random_loot',
                        type='minecraft:enchant_with_levels',
                    ),
                    weight=3,
                    name='minecraft:iron_chestplate',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantWithLevels(
                        levels=ContextIntProviderStructUniform(type='minecraft:uniform', min=20, max=39),
                        options='#minecraft:on_random_loot',
                        type='minecraft:enchant_with_levels',
                    ),
                    weight=3,
                    name='minecraft:iron_leggings',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantWithLevels(
                        levels=ContextIntProviderStructUniform(type='minecraft:uniform', min=20, max=39),
                        options='#minecraft:on_random_loot',
                        type='minecraft:enchant_with_levels',
                    ),
                    weight=3,
                    name='minecraft:iron_helmet',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantWithLevels(
                        levels=ContextIntProviderStructUniform(type='minecraft:uniform', min=20, max=39),
                        options='#minecraft:on_random_loot',
                        type='minecraft:enchant_with_levels',
                    ),
                    weight=3,
                    name='minecraft:iron_pickaxe',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantWithLevels(
                        levels=ContextIntProviderStructUniform(type='minecraft:uniform', min=20, max=39),
                        options='#minecraft:on_random_loot',
                        type='minecraft:enchant_with_levels',
                    ),
                    weight=3,
                    name='minecraft:iron_shovel',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryEmpty(weight=14, type='minecraft:empty'),
                LootPoolEntryItem(name='minecraft:spire_armor_trim_smithing_template', type='minecraft:item'),
            ],
        ),
    ],
    random_sequence='minecraft:chests/end_city_treasure',
)

IGLOO_CHEST = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=8),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=15,
                    name='minecraft:apple',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=15,
                    name='minecraft:coal',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:gold_nugget',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=2, name='minecraft:stone_axe', type='minecraft:item'),
                LootPoolEntryItem(weight=10, name='minecraft:rotten_flesh', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:emerald', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:wheat',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:golden_apple', type='minecraft:item')]),
    ],
    random_sequence='minecraft:chests/igloo_chest',
)

JUNGLE_TEMPLE = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=6),
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
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=7),
                        type='minecraft:set_count',
                    ),
                    weight=15,
                    name='minecraft:gold_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=15,
                    name='minecraft:bamboo',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:emerald',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=6),
                        type='minecraft:set_count',
                    ),
                    weight=20,
                    name='minecraft:bone',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=7),
                        type='minecraft:set_count',
                    ),
                    weight=16,
                    name='minecraft:rotten_flesh',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=5),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:leather',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(name='minecraft:copper_horse_armor', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:iron_horse_armor', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:golden_horse_armor', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:diamond_horse_armor', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantWithLevels(
                        levels=30,
                        options='#minecraft:on_random_loot',
                        type='minecraft:enchant_with_levels',
                    ),
                    name='minecraft:book',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryEmpty(weight=2, type='minecraft:empty'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=2, type='minecraft:set_count'),
                    name='minecraft:wild_armor_trim_smithing_template',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:chests/jungle_temple',
)

JUNGLE_TEMPLE_DISPENSER = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=7),
                        type='minecraft:set_count',
                    ),
                    weight=30,
                    name='minecraft:arrow',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:chests/jungle_temple_dispenser',
)

NETHER_BRIDGE = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=4),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=5,
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
                    weight=15,
                    name='minecraft:gold_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=5, name='minecraft:golden_sword', type='minecraft:item'),
                LootPoolEntryItem(weight=5, name='minecraft:golden_chestplate', type='minecraft:item'),
                LootPoolEntryItem(weight=5, name='minecraft:flint_and_steel', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=7),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:nether_wart',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=10, name='minecraft:saddle', type='minecraft:item'),
                LootPoolEntryItem(weight=8, name='minecraft:golden_horse_armor', type='minecraft:item'),
                LootPoolEntryItem(weight=5, name='minecraft:copper_horse_armor', type='minecraft:item'),
                LootPoolEntryItem(weight=5, name='minecraft:iron_horse_armor', type='minecraft:item'),
                LootPoolEntryItem(weight=3, name='minecraft:diamond_horse_armor', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:obsidian',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryEmpty(weight=14, type='minecraft:empty'),
                LootPoolEntryItem(name='minecraft:rib_armor_trim_smithing_template', type='minecraft:item'),
            ],
        ),
    ],
    random_sequence='minecraft:chests/nether_bridge',
)

PILLAGER_OUTPOST = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=1),
            entries=[LootPoolEntryItem(name='minecraft:crossbow', type='minecraft:item')],
        ),
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=3),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=5),
                        type='minecraft:set_count',
                    ),
                    weight=7,
                    name='minecraft:wheat',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=5),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:potato',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=5),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:carrot',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=3),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:dark_oak_log',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=3),
            entries=[
                LootPoolEntryItem(weight=7, name='minecraft:experience_bottle', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=6),
                        type='minecraft:set_count',
                    ),
                    weight=4,
                    name='minecraft:string',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=7),
                        type='minecraft:set_count',
                    ),
                    weight=4,
                    name='minecraft:arrow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:tripwire_hook',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:iron_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(options='#minecraft:on_random_loot', type='minecraft:enchant_randomly'),
                    name='minecraft:book',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=1),
            entries=[LootPoolEntryItem(name='minecraft:goat_horn', type='minecraft:item')],
            modifier=LootFunctionSetInstrument(options='#minecraft:regular_goat_horns', type='minecraft:set_instrument'),
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryEmpty(weight=3, type='minecraft:empty'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=2, type='minecraft:set_count'),
                    name='minecraft:sentry_armor_trim_smithing_template',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:chests/pillager_outpost',
)

RUINED_PORTAL = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=8),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                        type='minecraft:set_count',
                    ),
                    weight=40,
                    name='minecraft:obsidian',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=40,
                    name='minecraft:flint',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=9, max=18),
                        type='minecraft:set_count',
                    ),
                    weight=40,
                    name='minecraft:iron_nugget',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=40, name='minecraft:flint_and_steel', type='minecraft:item'),
                LootPoolEntryItem(weight=40, name='minecraft:fire_charge', type='minecraft:item'),
                LootPoolEntryItem(weight=15, name='minecraft:golden_apple', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=24),
                        type='minecraft:set_count',
                    ),
                    weight=15,
                    name='minecraft:gold_nugget',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(options='#minecraft:on_random_loot', type='minecraft:enchant_randomly'),
                    weight=15,
                    name='minecraft:golden_sword',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(options='#minecraft:on_random_loot', type='minecraft:enchant_randomly'),
                    weight=15,
                    name='minecraft:golden_axe',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(options='#minecraft:on_random_loot', type='minecraft:enchant_randomly'),
                    weight=15,
                    name='minecraft:golden_hoe',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(options='#minecraft:on_random_loot', type='minecraft:enchant_randomly'),
                    weight=15,
                    name='minecraft:golden_shovel',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(options='#minecraft:on_random_loot', type='minecraft:enchant_randomly'),
                    weight=15,
                    name='minecraft:golden_pickaxe',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(options='#minecraft:on_random_loot', type='minecraft:enchant_randomly'),
                    weight=15,
                    name='minecraft:golden_boots',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(options='#minecraft:on_random_loot', type='minecraft:enchant_randomly'),
                    weight=15,
                    name='minecraft:golden_chestplate',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(options='#minecraft:on_random_loot', type='minecraft:enchant_randomly'),
                    weight=15,
                    name='minecraft:golden_helmet',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(options='#minecraft:on_random_loot', type='minecraft:enchant_randomly'),
                    weight=15,
                    name='minecraft:golden_leggings',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=12),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:glistering_melon_slice',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=5, name='minecraft:golden_horse_armor', type='minecraft:item'),
                LootPoolEntryItem(weight=5, name='minecraft:light_weighted_pressure_plate', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=12),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:golden_carrot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=5, name='minecraft:clock', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:gold_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(name='minecraft:bell', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:enchanted_golden_apple', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:gold_block',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryEmpty(type='minecraft:empty'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:lodestone',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:chests/ruined_portal',
)

SHIPWRECK_MAP = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionExplorationMap(
                            destination='#minecraft:on_treasure_maps',
                            decoration='minecraft:red_x',
                            zoom=1,
                            skip_existing_chunks=False,
                            type='minecraft:exploration_map',
                        ),
                        LootFunctionFiltered(
                            item_filter=ItemPredicate(predicates={'minecraft:map_id': {}}),
                            on_fail=LootFunctionDiscard(type='minecraft:discard'),
                            type='minecraft:filtered',
                        ),
                    ],
                    name='minecraft:buried_treasure_map',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=3,
            entries=[
                LootPoolEntryItem(name='minecraft:compass', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:map', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:clock', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=10),
                        type='minecraft:set_count',
                    ),
                    weight=20,
                    name='minecraft:paper',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=5),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:feather',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=5),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:book',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryEmpty(weight=5, type='minecraft:empty'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=2, type='minecraft:set_count'),
                    name='minecraft:coast_armor_trim_smithing_template',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryEmpty(weight=148, type='minecraft:empty'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=20,
                    name='minecraft:copper_nautilus_armor',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=10,
                    name='minecraft:iron_nautilus_armor',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=5,
                    name='minecraft:golden_nautilus_armor',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=2,
                    name='minecraft:diamond_nautilus_armor',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:chests/shipwreck_map',
)

SHIPWRECK_SUPPLY = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=10),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=12),
                        type='minecraft:set_count',
                    ),
                    weight=8,
                    name='minecraft:paper',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=6),
                        type='minecraft:set_count',
                    ),
                    weight=7,
                    name='minecraft:potato',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=7,
                    name='minecraft:moss_block',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=6),
                        type='minecraft:set_count',
                    ),
                    weight=7,
                    name='minecraft:poisonous_potato',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=7,
                    name='minecraft:carrot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=8, max=21),
                        type='minecraft:set_count',
                    ),
                    weight=7,
                    name='minecraft:wheat',
                    type='minecraft:item',
                ),
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
                    weight=10,
                    name='minecraft:suspicious_stew',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=6,
                    name='minecraft:coal',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=5, max=24),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:rotten_flesh',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:pumpkin',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:bamboo',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=5),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:gunpowder',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:tnt',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(options='#minecraft:on_random_loot', type='minecraft:enchant_randomly'),
                    weight=3,
                    name='minecraft:leather_helmet',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(options='#minecraft:on_random_loot', type='minecraft:enchant_randomly'),
                    weight=3,
                    name='minecraft:leather_chestplate',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(options='#minecraft:on_random_loot', type='minecraft:enchant_randomly'),
                    weight=3,
                    name='minecraft:leather_leggings',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(options='#minecraft:on_random_loot', type='minecraft:enchant_randomly'),
                    weight=3,
                    name='minecraft:leather_boots',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryEmpty(weight=5, type='minecraft:empty'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=2, type='minecraft:set_count'),
                    name='minecraft:coast_armor_trim_smithing_template',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryEmpty(weight=148, type='minecraft:empty'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=20,
                    name='minecraft:copper_nautilus_armor',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=10,
                    name='minecraft:iron_nautilus_armor',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=5,
                    name='minecraft:golden_nautilus_armor',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=2,
                    name='minecraft:diamond_nautilus_armor',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:chests/shipwreck_supply',
)

SHIPWRECK_TREASURE = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=6),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=5),
                        type='minecraft:set_count',
                    ),
                    weight=90,
                    name='minecraft:iron_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=5),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:gold_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=5),
                        type='minecraft:set_count',
                    ),
                    weight=40,
                    name='minecraft:emerald',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=5, name='minecraft:diamond', type='minecraft:item'),
                LootPoolEntryItem(weight=5, name='minecraft:experience_bottle', type='minecraft:item'),
            ],
        ),
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=5),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=10),
                        type='minecraft:set_count',
                    ),
                    weight=50,
                    name='minecraft:iron_nugget',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=10),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:gold_nugget',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=10),
                        type='minecraft:set_count',
                    ),
                    weight=20,
                    name='minecraft:lapis_lazuli',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryEmpty(weight=5, type='minecraft:empty'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=2, type='minecraft:set_count'),
                    name='minecraft:coast_armor_trim_smithing_template',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryEmpty(weight=148, type='minecraft:empty'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=20,
                    name='minecraft:copper_nautilus_armor',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=10,
                    name='minecraft:iron_nautilus_armor',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=5,
                    name='minecraft:golden_nautilus_armor',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=2,
                    name='minecraft:diamond_nautilus_armor',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:chests/shipwreck_treasure',
)

SIMPLE_DUNGEON = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=5),
                        type='minecraft:set_count',
                    ),
                    weight=20,
                    name='minecraft:leather',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=15, name='minecraft:golden_apple', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:enchanted_golden_apple', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:music_disc_otherside', type='minecraft:item'),
                LootPoolEntryItem(weight=15, name='minecraft:music_disc_13', type='minecraft:item'),
                LootPoolEntryItem(weight=15, name='minecraft:music_disc_cat', type='minecraft:item'),
                LootPoolEntryItem(weight=20, name='minecraft:name_tag', type='minecraft:item'),
                LootPoolEntryItem(weight=10, name='minecraft:golden_horse_armor', type='minecraft:item'),
                LootPoolEntryItem(weight=15, name='minecraft:copper_horse_armor', type='minecraft:item'),
                LootPoolEntryItem(weight=15, name='minecraft:iron_horse_armor', type='minecraft:item'),
                LootPoolEntryItem(weight=5, name='minecraft:diamond_horse_armor', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(options='#minecraft:on_random_loot', type='minecraft:enchant_randomly'),
                    weight=10,
                    name='minecraft:book',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:iron_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:gold_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=20, name='minecraft:bread', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=20,
                    name='minecraft:wheat',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=10, name='minecraft:bucket', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=15,
                    name='minecraft:redstone',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=15,
                    name='minecraft:coal',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:melon_seeds',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:pumpkin_seeds',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:beetroot_seeds',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=3,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:bone',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:gunpowder',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:rotten_flesh',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:string',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:chests/simple_dungeon',
)

SPAWN_BONUS_CHEST = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(name='minecraft:stone_axe', type='minecraft:item'),
                LootPoolEntryItem(weight=3, name='minecraft:wooden_axe', type='minecraft:item'),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(name='minecraft:stone_pickaxe', type='minecraft:item'),
                LootPoolEntryItem(weight=3, name='minecraft:wooden_pickaxe', type='minecraft:item'),
            ],
        ),
        LootPool(
            rolls=3,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:apple',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:bread',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:salmon',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=4,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=12),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:stick',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=12),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:oak_planks',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:oak_log',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:spruce_log',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:birch_log',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:jungle_log',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:acacia_log',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:dark_oak_log',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:mangrove_log',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:chests/spawn_bonus_chest',
)

STRONGHOLD_CORRIDOR = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=3),
            entries=[
                LootPoolEntryItem(weight=10, name='minecraft:ender_pearl', type='minecraft:item'),
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
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=9),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:redstone',
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
                LootPoolEntryItem(weight=5, name='minecraft:iron_chestplate', type='minecraft:item'),
                LootPoolEntryItem(weight=5, name='minecraft:iron_helmet', type='minecraft:item'),
                LootPoolEntryItem(weight=5, name='minecraft:iron_leggings', type='minecraft:item'),
                LootPoolEntryItem(weight=5, name='minecraft:iron_boots', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:golden_apple', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=5),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:leather',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(name='minecraft:copper_horse_armor', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:iron_horse_armor', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:golden_horse_armor', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:diamond_horse_armor', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:music_disc_otherside', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantWithLevels(
                        levels=30,
                        options='#minecraft:on_random_loot',
                        type='minecraft:enchant_with_levels',
                    ),
                    name='minecraft:book',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryEmpty(weight=9, type='minecraft:empty'),
                LootPoolEntryItem(name='minecraft:eye_armor_trim_smithing_template', type='minecraft:item'),
            ],
        ),
    ],
    random_sequence='minecraft:chests/stronghold_corridor',
)

STRONGHOLD_CROSSING = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
            entries=[
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
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=9),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:redstone',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:coal',
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
                LootPoolEntryItem(name='minecraft:iron_pickaxe', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantWithLevels(
                        levels=30,
                        options='#minecraft:on_random_loot',
                        type='minecraft:enchant_with_levels',
                    ),
                    name='minecraft:book',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:chests/stronghold_crossing',
)

STRONGHOLD_LIBRARY = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=10),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=20,
                    name='minecraft:book',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=7),
                        type='minecraft:set_count',
                    ),
                    weight=20,
                    name='minecraft:paper',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(name='minecraft:map', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:compass', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantWithLevels(
                        levels=30,
                        options='#minecraft:on_random_loot',
                        type='minecraft:enchant_with_levels',
                    ),
                    weight=10,
                    name='minecraft:book',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:eye_armor_trim_smithing_template', type='minecraft:item')],
        ),
    ],
    random_sequence='minecraft:chests/stronghold_library',
)

UNDERWATER_RUIN_BIG = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=8),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:coal',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:gold_nugget',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(name='minecraft:emerald', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:stone_spear', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:wheat',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(name='minecraft:golden_apple', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(options='#minecraft:on_random_loot', type='minecraft:enchant_randomly'),
                    weight=5,
                    name='minecraft:book',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(name='minecraft:leather_chestplate', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:golden_helmet', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(options='#minecraft:on_random_loot', type='minecraft:enchant_randomly'),
                    weight=5,
                    name='minecraft:fishing_rod',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionExplorationMap(
                            destination='#minecraft:on_treasure_maps',
                            decoration='minecraft:red_x',
                            zoom=1,
                            skip_existing_chunks=False,
                            type='minecraft:exploration_map',
                        ),
                        LootFunctionFiltered(
                            item_filter=ItemPredicate(predicates={'minecraft:map_id': {}}),
                            on_fail=LootFunctionDiscard(type='minecraft:discard'),
                            type='minecraft:filtered',
                        ),
                    ],
                    weight=10,
                    name='minecraft:buried_treasure_map',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryEmpty(weight=148, type='minecraft:empty'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=20,
                    name='minecraft:copper_nautilus_armor',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=10,
                    name='minecraft:iron_nautilus_armor',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=5,
                    name='minecraft:golden_nautilus_armor',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=2,
                    name='minecraft:diamond_nautilus_armor',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:chests/underwater_ruin_big',
)

UNDERWATER_RUIN_SMALL = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=8),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:coal',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=2, name='minecraft:stone_axe', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:stone_spear', type='minecraft:item'),
                LootPoolEntryItem(weight=5, name='minecraft:rotten_flesh', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:emerald', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:wheat',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(name='minecraft:leather_chestplate', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:golden_helmet', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(options='#minecraft:on_random_loot', type='minecraft:enchant_randomly'),
                    weight=5,
                    name='minecraft:fishing_rod',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionExplorationMap(
                            destination='#minecraft:on_treasure_maps',
                            decoration='minecraft:red_x',
                            zoom=1,
                            skip_existing_chunks=False,
                            type='minecraft:exploration_map',
                        ),
                        LootFunctionFiltered(
                            item_filter=ItemPredicate(predicates={'minecraft:map_id': {}}),
                            on_fail=LootFunctionDiscard(type='minecraft:discard'),
                            type='minecraft:filtered',
                        ),
                    ],
                    weight=5,
                    name='minecraft:buried_treasure_map',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryEmpty(weight=148, type='minecraft:empty'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=20,
                    name='minecraft:copper_nautilus_armor',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=10,
                    name='minecraft:iron_nautilus_armor',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=5,
                    name='minecraft:golden_nautilus_armor',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=2,
                    name='minecraft:diamond_nautilus_armor',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:chests/underwater_ruin_small',
)

WOODLAND_MANSION = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
            entries=[
                LootPoolEntryItem(weight=20, name='minecraft:lead', type='minecraft:item'),
                LootPoolEntryItem(weight=15, name='minecraft:golden_apple', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:enchanted_golden_apple', type='minecraft:item'),
                LootPoolEntryItem(weight=15, name='minecraft:music_disc_13', type='minecraft:item'),
                LootPoolEntryItem(weight=15, name='minecraft:music_disc_cat', type='minecraft:item'),
                LootPoolEntryItem(weight=10, name='minecraft:chainmail_chestplate', type='minecraft:item'),
                LootPoolEntryItem(weight=15, name='minecraft:diamond_hoe', type='minecraft:item'),
                LootPoolEntryItem(weight=5, name='minecraft:diamond_chestplate', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(options='#minecraft:on_random_loot', type='minecraft:enchant_randomly'),
                    weight=10,
                    name='minecraft:book',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:iron_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:gold_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=20, name='minecraft:bread', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=20,
                    name='minecraft:wheat',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=10, name='minecraft:bucket', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=15,
                    name='minecraft:redstone',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=15,
                    name='minecraft:coal',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:melon_seeds',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:pumpkin_seeds',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:beetroot_seeds',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=50,
                    name='minecraft:resin_clump',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=3,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:bone',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:gunpowder',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:rotten_flesh',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:string',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryEmpty(type='minecraft:empty'),
                LootPoolEntryItem(name='minecraft:vex_armor_trim_smithing_template', type='minecraft:item'),
            ],
        ),
    ],
    random_sequence='minecraft:chests/woodland_mansion',
)
