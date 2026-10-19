"""Vanilla's data/advancement/recipes/combat/ files"""
from vanilla_mcdoc.data.advancement.Advancement import Advancement
from vanilla_mcdoc.data.advancement.AdvancementCriterion import AdvancementCriterionInventoryChanged, AdvancementCriterionRecipeUnlocked
from vanilla_mcdoc.data.advancement.AdvancementRewards import AdvancementRewards
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.advancement.trigger.InventoryChangeTrigger import InventoryChangeTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.RecipeUnlockedTrigger import RecipeUnlockedTriggerTypeArg

ARROW = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_feather': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:feather')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_flint': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:flint')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:arrow'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_feather', 'has_flint']],
    rewards=AdvancementRewards(recipes=['minecraft:arrow']),
)

BLACK_HARNESS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_dried_ghast': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dried_ghast')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:black_harness'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_dried_ghast']],
    rewards=AdvancementRewards(recipes=['minecraft:black_harness']),
)

BLUE_HARNESS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_dried_ghast': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dried_ghast')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:blue_harness'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_dried_ghast']],
    rewards=AdvancementRewards(recipes=['minecraft:blue_harness']),
)

BOW = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_string': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:string')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:bow'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_string']],
    rewards=AdvancementRewards(recipes=['minecraft:bow']),
)

BROWN_HARNESS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_dried_ghast': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dried_ghast')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:brown_harness'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_dried_ghast']],
    rewards=AdvancementRewards(recipes=['minecraft:brown_harness']),
)

COPPER_BOOTS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:copper_boots'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:copper_boots']),
)

COPPER_CHESTPLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:copper_chestplate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:copper_chestplate']),
)

COPPER_HELMET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:copper_helmet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:copper_helmet']),
)

COPPER_LEGGINGS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:copper_leggings'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:copper_leggings']),
)

COPPER_SPEAR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:copper_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:copper_spear'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:copper_spear']),
)

COPPER_SWORD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:copper_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:copper_sword'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:copper_sword']),
)

CROSSBOW = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_iron_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_string': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:string')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:crossbow'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_tripwire_hook': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:tripwire_hook')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_string', 'has_iron_ingot', 'has_tripwire_hook']],
    rewards=AdvancementRewards(recipes=['minecraft:crossbow']),
)

CYAN_HARNESS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_dried_ghast': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dried_ghast')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cyan_harness'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_dried_ghast']],
    rewards=AdvancementRewards(recipes=['minecraft:cyan_harness']),
)

DIAMOND_BOOTS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_diamond': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:diamond')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:diamond_boots'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_diamond']],
    rewards=AdvancementRewards(recipes=['minecraft:diamond_boots']),
)

DIAMOND_CHESTPLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_diamond': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:diamond')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:diamond_chestplate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_diamond']],
    rewards=AdvancementRewards(recipes=['minecraft:diamond_chestplate']),
)

DIAMOND_HELMET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_diamond': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:diamond')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:diamond_helmet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_diamond']],
    rewards=AdvancementRewards(recipes=['minecraft:diamond_helmet']),
)

DIAMOND_LEGGINGS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_diamond': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:diamond')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:diamond_leggings'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_diamond']],
    rewards=AdvancementRewards(recipes=['minecraft:diamond_leggings']),
)

DIAMOND_SPEAR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_diamond': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:diamond_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:diamond_spear'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_diamond']],
    rewards=AdvancementRewards(recipes=['minecraft:diamond_spear']),
)

DIAMOND_SWORD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_diamond': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:diamond_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:diamond_sword'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_diamond']],
    rewards=AdvancementRewards(recipes=['minecraft:diamond_sword']),
)

DYE_BLACK_HARNESS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:black_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_black_harness'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_black_harness']),
)

DYE_BLUE_HARNESS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blue_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_blue_harness'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_blue_harness']),
)

DYE_BROWN_HARNESS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:brown_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_brown_harness'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_brown_harness']),
)

DYE_CYAN_HARNESS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cyan_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_cyan_harness'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_cyan_harness']),
)

DYE_GRAY_HARNESS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gray_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_gray_harness'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_gray_harness']),
)

DYE_GREEN_HARNESS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:green_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_green_harness'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_green_harness']),
)

DYE_LIGHT_BLUE_HARNESS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_blue_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_light_blue_harness'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_light_blue_harness']),
)

DYE_LIGHT_GRAY_HARNESS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_gray_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_light_gray_harness'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_light_gray_harness']),
)

DYE_LIME_HARNESS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:lime_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_lime_harness'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_lime_harness']),
)

DYE_MAGENTA_HARNESS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:magenta_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_magenta_harness'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_magenta_harness']),
)

DYE_ORANGE_HARNESS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:orange_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_orange_harness'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_orange_harness']),
)

DYE_PINK_HARNESS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pink_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_pink_harness'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_pink_harness']),
)

DYE_PURPLE_HARNESS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:purple_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_purple_harness'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_purple_harness']),
)

DYE_RED_HARNESS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_red_harness'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_red_harness']),
)

DYE_WHITE_HARNESS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:white_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_white_harness'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_white_harness']),
)

DYE_YELLOW_HARNESS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:yellow_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_yellow_harness'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_yellow_harness']),
)

GOLDEN_BOOTS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gold_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gold_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:golden_boots'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_gold_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:golden_boots']),
)

GOLDEN_CHESTPLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gold_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gold_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:golden_chestplate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_gold_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:golden_chestplate']),
)

GOLDEN_HELMET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gold_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gold_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:golden_helmet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_gold_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:golden_helmet']),
)

GOLDEN_LEGGINGS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gold_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gold_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:golden_leggings'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_gold_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:golden_leggings']),
)

GOLDEN_SPEAR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gold_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:gold_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:golden_spear'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_gold_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:golden_spear']),
)

GOLDEN_SWORD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gold_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:gold_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:golden_sword'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_gold_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:golden_sword']),
)

GRAY_HARNESS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_dried_ghast': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dried_ghast')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:gray_harness'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_dried_ghast']],
    rewards=AdvancementRewards(recipes=['minecraft:gray_harness']),
)

GREEN_HARNESS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_dried_ghast': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dried_ghast')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:green_harness'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_dried_ghast']],
    rewards=AdvancementRewards(recipes=['minecraft:green_harness']),
)

IRON_BOOTS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_iron_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:iron_boots'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_iron_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:iron_boots']),
)

IRON_CHESTPLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_iron_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:iron_chestplate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_iron_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:iron_chestplate']),
)

IRON_HELMET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_iron_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:iron_helmet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_iron_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:iron_helmet']),
)

IRON_LEGGINGS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_iron_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:iron_leggings'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_iron_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:iron_leggings']),
)

IRON_SPEAR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_iron_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:iron_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:iron_spear'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_iron_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:iron_spear']),
)

IRON_SWORD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_iron_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:iron_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:iron_sword'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_iron_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:iron_sword']),
)

LEATHER_BOOTS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_leather': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:leather')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:leather_boots'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_leather']],
    rewards=AdvancementRewards(recipes=['minecraft:leather_boots']),
)

LEATHER_CHESTPLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_leather': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:leather')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:leather_chestplate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_leather']],
    rewards=AdvancementRewards(recipes=['minecraft:leather_chestplate']),
)

LEATHER_HELMET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_leather': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:leather')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:leather_helmet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_leather']],
    rewards=AdvancementRewards(recipes=['minecraft:leather_helmet']),
)

LEATHER_LEGGINGS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_leather': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:leather')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:leather_leggings'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_leather']],
    rewards=AdvancementRewards(recipes=['minecraft:leather_leggings']),
)

LIGHT_BLUE_HARNESS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_dried_ghast': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dried_ghast')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_blue_harness'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_dried_ghast']],
    rewards=AdvancementRewards(recipes=['minecraft:light_blue_harness']),
)

LIGHT_GRAY_HARNESS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_dried_ghast': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dried_ghast')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_gray_harness'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_dried_ghast']],
    rewards=AdvancementRewards(recipes=['minecraft:light_gray_harness']),
)

LIME_HARNESS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_dried_ghast': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dried_ghast')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:lime_harness'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_dried_ghast']],
    rewards=AdvancementRewards(recipes=['minecraft:lime_harness']),
)

MACE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_breeze_rod': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:breeze_rod')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_heavy_core': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:heavy_core')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:mace'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_breeze_rod', 'has_heavy_core']],
    rewards=AdvancementRewards(recipes=['minecraft:mace']),
)

MAGENTA_HARNESS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_dried_ghast': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dried_ghast')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:magenta_harness'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_dried_ghast']],
    rewards=AdvancementRewards(recipes=['minecraft:magenta_harness']),
)

NETHERITE_BOOTS_SMITHING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_netherite_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:netherite_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:netherite_boots_smithing'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_netherite_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:netherite_boots_smithing']),
)

NETHERITE_CHESTPLATE_SMITHING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_netherite_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:netherite_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:netherite_chestplate_smithing'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_netherite_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:netherite_chestplate_smithing']),
)

NETHERITE_HELMET_SMITHING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_netherite_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:netherite_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:netherite_helmet_smithing'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_netherite_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:netherite_helmet_smithing']),
)

NETHERITE_HORSE_ARMOR_SMITHING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_netherite_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:netherite_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:netherite_horse_armor_smithing'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_netherite_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:netherite_horse_armor_smithing']),
)

NETHERITE_LEGGINGS_SMITHING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_netherite_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:netherite_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:netherite_leggings_smithing'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_netherite_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:netherite_leggings_smithing']),
)

NETHERITE_NAUTILUS_ARMOR_SMITHING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_netherite_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:netherite_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:netherite_nautilus_armor_smithing'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_netherite_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:netherite_nautilus_armor_smithing']),
)

NETHERITE_SPEAR_SMITHING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_netherite_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:netherite_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:netherite_spear_smithing'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_netherite_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:netherite_spear_smithing']),
)

NETHERITE_SWORD_SMITHING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_netherite_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:netherite_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:netherite_sword_smithing'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_netherite_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:netherite_sword_smithing']),
)

ORANGE_HARNESS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_dried_ghast': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dried_ghast')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:orange_harness'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_dried_ghast']],
    rewards=AdvancementRewards(recipes=['minecraft:orange_harness']),
)

PINK_HARNESS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_dried_ghast': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dried_ghast')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pink_harness'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_dried_ghast']],
    rewards=AdvancementRewards(recipes=['minecraft:pink_harness']),
)

PURPLE_HARNESS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_dried_ghast': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dried_ghast')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:purple_harness'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_dried_ghast']],
    rewards=AdvancementRewards(recipes=['minecraft:purple_harness']),
)

RED_HARNESS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_dried_ghast': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dried_ghast')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:red_harness'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_dried_ghast']],
    rewards=AdvancementRewards(recipes=['minecraft:red_harness']),
)

SADDLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_leather': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:leather')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:saddle'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_leather']],
    rewards=AdvancementRewards(recipes=['minecraft:saddle']),
)

SHIELD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_iron_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:shield'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_iron_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:shield']),
)

SPECTRAL_ARROW = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glowstone_dust': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glowstone_dust')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:spectral_arrow'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glowstone_dust']],
    rewards=AdvancementRewards(recipes=['minecraft:spectral_arrow']),
)

STONE_SPEAR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cobblestone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:stone_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stone_spear'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cobblestone']],
    rewards=AdvancementRewards(recipes=['minecraft:stone_spear']),
)

STONE_SWORD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cobblestone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:stone_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stone_sword'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cobblestone']],
    rewards=AdvancementRewards(recipes=['minecraft:stone_sword']),
)

TURTLE_HELMET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:turtle_helmet'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_turtle_scute': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:turtle_scute')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_turtle_scute']],
    rewards=AdvancementRewards(recipes=['minecraft:turtle_helmet']),
)

WHITE_HARNESS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_dried_ghast': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dried_ghast')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:white_harness'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_dried_ghast']],
    rewards=AdvancementRewards(recipes=['minecraft:white_harness']),
)

WOLF_ARMOR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_armadillo_scute': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:armadillo_scute')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:wolf_armor'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_armadillo_scute']],
    rewards=AdvancementRewards(recipes=['minecraft:wolf_armor']),
)

WOODEN_SPEAR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stick': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stick')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:wooden_spear'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stick']],
    rewards=AdvancementRewards(recipes=['minecraft:wooden_spear']),
)

WOODEN_SWORD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stick': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stick')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:wooden_sword'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stick']],
    rewards=AdvancementRewards(recipes=['minecraft:wooden_sword']),
)

YELLOW_HARNESS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_dried_ghast': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dried_ghast')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:yellow_harness'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_dried_ghast']],
    rewards=AdvancementRewards(recipes=['minecraft:yellow_harness']),
)
