"""Vanilla's data/advancement/recipes/brewing/ files"""
from vanilla_mcdoc.data.advancement.Advancement import Advancement
from vanilla_mcdoc.data.advancement.AdvancementCriterion import AdvancementCriterionInventoryChanged, AdvancementCriterionRecipeUnlocked
from vanilla_mcdoc.data.advancement.AdvancementRewards import AdvancementRewards
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.advancement.trigger.InventoryChangeTrigger import InventoryChangeTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.RecipeUnlockedTrigger import RecipeUnlockedTriggerTypeArg

BLAZE_POWDER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blaze_rod': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blaze_rod')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:blaze_powder'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_blaze_rod']],
    rewards=AdvancementRewards(recipes=['minecraft:blaze_powder']),
)

BREWING_STAND = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blaze_rod': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blaze_rod')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:brewing_stand'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_blaze_rod']],
    rewards=AdvancementRewards(recipes=['minecraft:brewing_stand']),
)

CAULDRON = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cauldron'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_water_bucket': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:water_bucket')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_water_bucket']],
    rewards=AdvancementRewards(recipes=['minecraft:cauldron']),
)

FERMENTED_SPIDER_EYE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_spider_eye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:spider_eye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:fermented_spider_eye'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_spider_eye']],
    rewards=AdvancementRewards(recipes=['minecraft:fermented_spider_eye']),
)

GLASS_BOTTLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glass')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:glass_bottle'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass']],
    rewards=AdvancementRewards(recipes=['minecraft:glass_bottle']),
)

GLISTERING_MELON_SLICE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_melon': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:melon_slice')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:glistering_melon_slice'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_melon']],
    rewards=AdvancementRewards(recipes=['minecraft:glistering_melon_slice']),
)

GOLDEN_CARROT = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gold_nugget': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gold_nugget')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:golden_carrot'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_gold_nugget']],
    rewards=AdvancementRewards(recipes=['minecraft:golden_carrot']),
)

MAGMA_CREAM = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blaze_powder': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blaze_powder')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:magma_cream'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_blaze_powder']],
    rewards=AdvancementRewards(recipes=['minecraft:magma_cream']),
)
