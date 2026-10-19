"""Vanilla's data/advancement/recipes/misc/ files"""
from vanilla_mcdoc.data.advancement.Advancement import Advancement
from vanilla_mcdoc.data.advancement.AdvancementCriterion import AdvancementCriterionInventoryChanged, AdvancementCriterionRecipeUnlocked
from vanilla_mcdoc.data.advancement.AdvancementRewards import AdvancementRewards
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.advancement.trigger.InventoryChangeTrigger import InventoryChangeTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.RecipeUnlockedTrigger import RecipeUnlockedTriggerTypeArg

BEACON = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_nether_star': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:nether_star')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:beacon'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_nether_star']],
    rewards=AdvancementRewards(recipes=['minecraft:beacon']),
)

BLACK_DYE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_ink_sac': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:ink_sac')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:black_dye'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_ink_sac']],
    rewards=AdvancementRewards(recipes=['minecraft:black_dye']),
)

BLACK_DYE_FROM_WITHER_ROSE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:black_dye_from_wither_rose'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_wither_rose': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:wither_rose')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_wither_rose']],
    rewards=AdvancementRewards(recipes=['minecraft:black_dye_from_wither_rose']),
)

BLUE_DYE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_lapis_lazuli': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:lapis_lazuli')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:blue_dye'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_lapis_lazuli']],
    rewards=AdvancementRewards(recipes=['minecraft:blue_dye']),
)

BLUE_DYE_FROM_CORNFLOWER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cornflower': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cornflower')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:blue_dye_from_cornflower'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cornflower']],
    rewards=AdvancementRewards(recipes=['minecraft:blue_dye_from_cornflower']),
)

BOLT_ARMOR_TRIM_SMITHING_TEMPLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_bolt_armor_trim_smithing_template': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:bolt_armor_trim_smithing_template')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:bolt_armor_trim_smithing_template'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_bolt_armor_trim_smithing_template']],
    rewards=AdvancementRewards(recipes=['minecraft:bolt_armor_trim_smithing_template']),
)

BOLT_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_smithing_trim_template': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:bolt_armor_trim_smithing_template')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:bolt_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_smithing_trim_template']],
    rewards=AdvancementRewards(recipes=['minecraft:bolt_armor_trim_smithing_template_smithing_trim']),
)

BONE_MEAL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_bone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:bone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:bone_meal'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_bone']],
    rewards=AdvancementRewards(recipes=['minecraft:bone_meal']),
)

BONE_MEAL_FROM_BONE_BLOCK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_bone_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:bone_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:bone_meal_from_bone_block'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_bone_block']],
    rewards=AdvancementRewards(recipes=['minecraft:bone_meal_from_bone_block']),
)

BOOK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_paper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:paper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:book'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_paper']],
    rewards=AdvancementRewards(recipes=['minecraft:book']),
)

BORDURE_INDENTED_BANNER_PATTERN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:bordure_indented_banner_pattern'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_vines': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:vine')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_vines']],
    rewards=AdvancementRewards(recipes=['minecraft:bordure_indented_banner_pattern']),
)

BOWL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_mushroom': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:mushrooms')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_mushroom_stew': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:mushroom_stew')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:bowl'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_mushroom', 'has_mushroom_stew']],
    rewards=AdvancementRewards(recipes=['minecraft:bowl']),
)

BRICK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_clay_ball': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:clay_ball')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:brick'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_clay_ball']],
    rewards=AdvancementRewards(recipes=['minecraft:brick']),
)

BROWN_DYE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cocoa_beans': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cocoa_beans')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:brown_dye'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cocoa_beans']],
    rewards=AdvancementRewards(recipes=['minecraft:brown_dye']),
)

BUCKET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_iron_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:bucket'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_iron_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:bucket']),
)

CHARCOAL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:logs_that_burn')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:charcoal'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_log']],
    rewards=AdvancementRewards(recipes=['minecraft:charcoal']),
)

COAL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_coal_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:coal_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:coal'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_coal_block']],
    rewards=AdvancementRewards(recipes=['minecraft:coal']),
)

COAL_FROM_BLASTING_COAL_ORE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_coal_ore': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:coal_ore')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:coal_from_blasting_coal_ore'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_coal_ore']],
    rewards=AdvancementRewards(recipes=['minecraft:coal_from_blasting_coal_ore']),
)

COAL_FROM_BLASTING_DEEPSLATE_COAL_ORE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate_coal_ore': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate_coal_ore')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:coal_from_blasting_deepslate_coal_ore'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate_coal_ore']],
    rewards=AdvancementRewards(recipes=['minecraft:coal_from_blasting_deepslate_coal_ore']),
)

COAL_FROM_SMELTING_COAL_ORE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_coal_ore': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:coal_ore')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:coal_from_smelting_coal_ore'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_coal_ore']],
    rewards=AdvancementRewards(recipes=['minecraft:coal_from_smelting_coal_ore']),
)

COAL_FROM_SMELTING_DEEPSLATE_COAL_ORE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate_coal_ore': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate_coal_ore')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:coal_from_smelting_deepslate_coal_ore'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate_coal_ore']],
    rewards=AdvancementRewards(recipes=['minecraft:coal_from_smelting_deepslate_coal_ore']),
)

COAST_ARMOR_TRIM_SMITHING_TEMPLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_coast_armor_trim_smithing_template': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:coast_armor_trim_smithing_template')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:coast_armor_trim_smithing_template'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_coast_armor_trim_smithing_template']],
    rewards=AdvancementRewards(recipes=['minecraft:coast_armor_trim_smithing_template']),
)

COAST_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_smithing_trim_template': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:coast_armor_trim_smithing_template')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:coast_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_smithing_trim_template']],
    rewards=AdvancementRewards(recipes=['minecraft:coast_armor_trim_smithing_template_smithing_trim']),
)

CONDUIT = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_nautilus_core': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:heart_of_the_sea')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_nautilus_shell': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:nautilus_shell')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:conduit'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_nautilus_core', 'has_nautilus_shell']],
    rewards=AdvancementRewards(recipes=['minecraft:conduit']),
)

COPPER_INGOT = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:copper_ingot'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_block']],
    rewards=AdvancementRewards(recipes=['minecraft:copper_ingot']),
)

COPPER_INGOT_FROM_BLASTING_COPPER_ORE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_ore': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_ore')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:copper_ingot_from_blasting_copper_ore'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_ore']],
    rewards=AdvancementRewards(recipes=['minecraft:copper_ingot_from_blasting_copper_ore']),
)

COPPER_INGOT_FROM_BLASTING_DEEPSLATE_COPPER_ORE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate_copper_ore': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate_copper_ore')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:copper_ingot_from_blasting_deepslate_copper_ore'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate_copper_ore']],
    rewards=AdvancementRewards(recipes=['minecraft:copper_ingot_from_blasting_deepslate_copper_ore']),
)

COPPER_INGOT_FROM_BLASTING_RAW_COPPER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_raw_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:raw_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:copper_ingot_from_blasting_raw_copper'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_raw_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:copper_ingot_from_blasting_raw_copper']),
)

COPPER_INGOT_FROM_NUGGETS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_nugget': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_nugget')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:copper_ingot_from_nuggets'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_nugget']],
    rewards=AdvancementRewards(recipes=['minecraft:copper_ingot_from_nuggets']),
)

COPPER_INGOT_FROM_SMELTING_COPPER_ORE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_ore': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_ore')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:copper_ingot_from_smelting_copper_ore'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_ore']],
    rewards=AdvancementRewards(recipes=['minecraft:copper_ingot_from_smelting_copper_ore']),
)

COPPER_INGOT_FROM_SMELTING_DEEPSLATE_COPPER_ORE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate_copper_ore': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate_copper_ore')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:copper_ingot_from_smelting_deepslate_copper_ore'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate_copper_ore']],
    rewards=AdvancementRewards(recipes=['minecraft:copper_ingot_from_smelting_deepslate_copper_ore']),
)

COPPER_INGOT_FROM_SMELTING_RAW_COPPER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_raw_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:raw_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:copper_ingot_from_smelting_raw_copper'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_raw_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:copper_ingot_from_smelting_raw_copper']),
)

COPPER_INGOT_FROM_WAXED_COPPER_BLOCK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:copper_ingot_from_waxed_copper_block'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_copper_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_copper_block')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_copper_block']],
    rewards=AdvancementRewards(recipes=['minecraft:copper_ingot_from_waxed_copper_block']),
)

COPPER_NUGGET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:copper_nugget'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:copper_nugget']),
)

COPPER_NUGGET_FROM_BLASTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_axe': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_axe')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_copper_boots': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_boots')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_copper_chestplate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_chestplate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_copper_helmet': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_helmet')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_copper_hoe': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_hoe')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_copper_horse_armor': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_horse_armor')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_copper_leggings': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_leggings')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_copper_nautilus_armor': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_nautilus_armor')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_copper_pickaxe': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_pickaxe')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_copper_shovel': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_shovel')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_copper_spear': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_spear')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_copper_sword': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_sword')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:copper_nugget_from_blasting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[
        [
            'has_the_recipe',
            'has_copper_pickaxe',
            'has_copper_shovel',
            'has_copper_axe',
            'has_copper_hoe',
            'has_copper_sword',
            'has_copper_spear',
            'has_copper_helmet',
            'has_copper_chestplate',
            'has_copper_leggings',
            'has_copper_boots',
            'has_copper_horse_armor',
            'has_copper_nautilus_armor',
        ],
    ],
    rewards=AdvancementRewards(recipes=['minecraft:copper_nugget_from_blasting']),
)

COPPER_NUGGET_FROM_SMELTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_axe': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_axe')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_copper_boots': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_boots')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_copper_chestplate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_chestplate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_copper_helmet': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_helmet')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_copper_hoe': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_hoe')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_copper_horse_armor': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_horse_armor')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_copper_leggings': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_leggings')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_copper_nautilus_armor': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_nautilus_armor')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_copper_pickaxe': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_pickaxe')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_copper_shovel': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_shovel')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_copper_spear': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_spear')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_copper_sword': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_sword')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:copper_nugget_from_smelting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[
        [
            'has_the_recipe',
            'has_copper_pickaxe',
            'has_copper_shovel',
            'has_copper_axe',
            'has_copper_hoe',
            'has_copper_sword',
            'has_copper_spear',
            'has_copper_helmet',
            'has_copper_chestplate',
            'has_copper_leggings',
            'has_copper_boots',
            'has_copper_horse_armor',
            'has_copper_nautilus_armor',
        ],
    ],
    rewards=AdvancementRewards(recipes=['minecraft:copper_nugget_from_smelting']),
)

CREAKING_HEART = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_resin_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:resin_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:creaking_heart'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_resin_block']],
    rewards=AdvancementRewards(recipes=['minecraft:creaking_heart']),
)

CREEPER_BANNER_PATTERN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_creeper_head': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:creeper_head')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:creeper_banner_pattern'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_creeper_head']],
    rewards=AdvancementRewards(recipes=['minecraft:creeper_banner_pattern']),
)

CYAN_DYE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blue_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blue_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_green_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:green_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cyan_dye'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_green_dye', 'has_blue_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:cyan_dye']),
)

CYAN_DYE_FROM_PITCHER_PLANT = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_pitcher_plant': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pitcher_plant')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cyan_dye_from_pitcher_plant'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_pitcher_plant']],
    rewards=AdvancementRewards(recipes=['minecraft:cyan_dye_from_pitcher_plant']),
)

DIAMOND = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_diamond_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:diamond_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:diamond'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_diamond_block']],
    rewards=AdvancementRewards(recipes=['minecraft:diamond']),
)

DIAMOND_FROM_BLASTING_DEEPSLATE_DIAMOND_ORE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate_diamond_ore': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate_diamond_ore')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:diamond_from_blasting_deepslate_diamond_ore'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate_diamond_ore']],
    rewards=AdvancementRewards(recipes=['minecraft:diamond_from_blasting_deepslate_diamond_ore']),
)

DIAMOND_FROM_BLASTING_DIAMOND_ORE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_diamond_ore': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:diamond_ore')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:diamond_from_blasting_diamond_ore'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_diamond_ore']],
    rewards=AdvancementRewards(recipes=['minecraft:diamond_from_blasting_diamond_ore']),
)

DIAMOND_FROM_SMELTING_DEEPSLATE_DIAMOND_ORE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate_diamond_ore': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate_diamond_ore')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:diamond_from_smelting_deepslate_diamond_ore'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate_diamond_ore']],
    rewards=AdvancementRewards(recipes=['minecraft:diamond_from_smelting_deepslate_diamond_ore']),
)

DIAMOND_FROM_SMELTING_DIAMOND_ORE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_diamond_ore': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:diamond_ore')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:diamond_from_smelting_diamond_ore'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_diamond_ore']],
    rewards=AdvancementRewards(recipes=['minecraft:diamond_from_smelting_diamond_ore']),
)

DUNE_ARMOR_TRIM_SMITHING_TEMPLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_dune_armor_trim_smithing_template': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dune_armor_trim_smithing_template')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dune_armor_trim_smithing_template'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_dune_armor_trim_smithing_template']],
    rewards=AdvancementRewards(recipes=['minecraft:dune_armor_trim_smithing_template']),
)

DUNE_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_smithing_trim_template': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dune_armor_trim_smithing_template')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dune_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_smithing_trim_template']],
    rewards=AdvancementRewards(recipes=['minecraft:dune_armor_trim_smithing_template_smithing_trim']),
)

EMERALD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_emerald_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:emerald_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:emerald'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_emerald_block']],
    rewards=AdvancementRewards(recipes=['minecraft:emerald']),
)

EMERALD_FROM_BLASTING_DEEPSLATE_EMERALD_ORE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate_emerald_ore': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate_emerald_ore')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:emerald_from_blasting_deepslate_emerald_ore'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate_emerald_ore']],
    rewards=AdvancementRewards(recipes=['minecraft:emerald_from_blasting_deepslate_emerald_ore']),
)

EMERALD_FROM_BLASTING_EMERALD_ORE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_emerald_ore': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:emerald_ore')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:emerald_from_blasting_emerald_ore'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_emerald_ore']],
    rewards=AdvancementRewards(recipes=['minecraft:emerald_from_blasting_emerald_ore']),
)

EMERALD_FROM_SMELTING_DEEPSLATE_EMERALD_ORE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate_emerald_ore': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate_emerald_ore')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:emerald_from_smelting_deepslate_emerald_ore'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate_emerald_ore']],
    rewards=AdvancementRewards(recipes=['minecraft:emerald_from_smelting_deepslate_emerald_ore']),
)

EMERALD_FROM_SMELTING_EMERALD_ORE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_emerald_ore': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:emerald_ore')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:emerald_from_smelting_emerald_ore'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_emerald_ore']],
    rewards=AdvancementRewards(recipes=['minecraft:emerald_from_smelting_emerald_ore']),
)

ENDER_EYE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blaze_powder': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blaze_powder')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:ender_eye'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_blaze_powder']],
    rewards=AdvancementRewards(recipes=['minecraft:ender_eye']),
)

EYE_ARMOR_TRIM_SMITHING_TEMPLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_eye_armor_trim_smithing_template': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:eye_armor_trim_smithing_template')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:eye_armor_trim_smithing_template'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_eye_armor_trim_smithing_template']],
    rewards=AdvancementRewards(recipes=['minecraft:eye_armor_trim_smithing_template']),
)

EYE_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_smithing_trim_template': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:eye_armor_trim_smithing_template')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:eye_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_smithing_trim_template']],
    rewards=AdvancementRewards(recipes=['minecraft:eye_armor_trim_smithing_template_smithing_trim']),
)

FIELD_MASONED_BANNER_PATTERN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:field_masoned_banner_pattern'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:field_masoned_banner_pattern']),
)

FIREWORK_ROCKET_SIMPLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gunpowder': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gunpowder')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:firework_rocket_simple'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_gunpowder']],
    rewards=AdvancementRewards(recipes=['minecraft:firework_rocket_simple']),
)

FIRE_CHARGE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blaze_powder': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blaze_powder')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:fire_charge'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_blaze_powder']],
    rewards=AdvancementRewards(recipes=['minecraft:fire_charge']),
)

FLOWER_BANNER_PATTERN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_oxeye_daisy': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oxeye_daisy')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:flower_banner_pattern'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_oxeye_daisy']],
    rewards=AdvancementRewards(recipes=['minecraft:flower_banner_pattern']),
)

FLOW_ARMOR_TRIM_SMITHING_TEMPLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_flow_armor_trim_smithing_template': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:flow_armor_trim_smithing_template')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:flow_armor_trim_smithing_template'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_flow_armor_trim_smithing_template']],
    rewards=AdvancementRewards(recipes=['minecraft:flow_armor_trim_smithing_template']),
)

FLOW_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_smithing_trim_template': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:flow_armor_trim_smithing_template')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:flow_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_smithing_trim_template']],
    rewards=AdvancementRewards(recipes=['minecraft:flow_armor_trim_smithing_template_smithing_trim']),
)

GOLD_INGOT_FROM_BLASTING_DEEPSLATE_GOLD_ORE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate_gold_ore': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate_gold_ore')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:gold_ingot_from_blasting_deepslate_gold_ore'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate_gold_ore']],
    rewards=AdvancementRewards(recipes=['minecraft:gold_ingot_from_blasting_deepslate_gold_ore']),
)

GOLD_INGOT_FROM_BLASTING_GOLD_ORE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gold_ore': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gold_ore')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:gold_ingot_from_blasting_gold_ore'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_gold_ore']],
    rewards=AdvancementRewards(recipes=['minecraft:gold_ingot_from_blasting_gold_ore']),
)

GOLD_INGOT_FROM_BLASTING_NETHER_GOLD_ORE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_nether_gold_ore': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:nether_gold_ore')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:gold_ingot_from_blasting_nether_gold_ore'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_nether_gold_ore']],
    rewards=AdvancementRewards(recipes=['minecraft:gold_ingot_from_blasting_nether_gold_ore']),
)

GOLD_INGOT_FROM_BLASTING_RAW_GOLD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_raw_gold': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:raw_gold')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:gold_ingot_from_blasting_raw_gold'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_raw_gold']],
    rewards=AdvancementRewards(recipes=['minecraft:gold_ingot_from_blasting_raw_gold']),
)

GOLD_INGOT_FROM_GOLD_BLOCK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gold_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gold_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:gold_ingot_from_gold_block'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_gold_block']],
    rewards=AdvancementRewards(recipes=['minecraft:gold_ingot_from_gold_block']),
)

GOLD_INGOT_FROM_NUGGETS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gold_nugget': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gold_nugget')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:gold_ingot_from_nuggets'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_gold_nugget']],
    rewards=AdvancementRewards(recipes=['minecraft:gold_ingot_from_nuggets']),
)

GOLD_INGOT_FROM_SMELTING_DEEPSLATE_GOLD_ORE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate_gold_ore': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate_gold_ore')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:gold_ingot_from_smelting_deepslate_gold_ore'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate_gold_ore']],
    rewards=AdvancementRewards(recipes=['minecraft:gold_ingot_from_smelting_deepslate_gold_ore']),
)

GOLD_INGOT_FROM_SMELTING_GOLD_ORE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gold_ore': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gold_ore')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:gold_ingot_from_smelting_gold_ore'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_gold_ore']],
    rewards=AdvancementRewards(recipes=['minecraft:gold_ingot_from_smelting_gold_ore']),
)

GOLD_INGOT_FROM_SMELTING_NETHER_GOLD_ORE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_nether_gold_ore': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:nether_gold_ore')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:gold_ingot_from_smelting_nether_gold_ore'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_nether_gold_ore']],
    rewards=AdvancementRewards(recipes=['minecraft:gold_ingot_from_smelting_nether_gold_ore']),
)

GOLD_INGOT_FROM_SMELTING_RAW_GOLD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_raw_gold': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:raw_gold')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:gold_ingot_from_smelting_raw_gold'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_raw_gold']],
    rewards=AdvancementRewards(recipes=['minecraft:gold_ingot_from_smelting_raw_gold']),
)

GOLD_NUGGET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gold_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gold_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:gold_nugget'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_gold_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:gold_nugget']),
)

GOLD_NUGGET_FROM_BLASTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_golden_axe': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:golden_axe')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_golden_boots': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:golden_boots')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_golden_chestplate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:golden_chestplate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_golden_helmet': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:golden_helmet')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_golden_hoe': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:golden_hoe')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_golden_horse_armor': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:golden_horse_armor')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_golden_leggings': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:golden_leggings')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_golden_nautilus_armor': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:golden_nautilus_armor')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_golden_pickaxe': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:golden_pickaxe')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_golden_shovel': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:golden_shovel')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_golden_spear': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:golden_spear')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_golden_sword': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:golden_sword')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:gold_nugget_from_blasting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[
        [
            'has_the_recipe',
            'has_golden_pickaxe',
            'has_golden_shovel',
            'has_golden_axe',
            'has_golden_hoe',
            'has_golden_sword',
            'has_golden_spear',
            'has_golden_helmet',
            'has_golden_chestplate',
            'has_golden_leggings',
            'has_golden_boots',
            'has_golden_horse_armor',
            'has_golden_nautilus_armor',
        ],
    ],
    rewards=AdvancementRewards(recipes=['minecraft:gold_nugget_from_blasting']),
)

GOLD_NUGGET_FROM_SMELTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_golden_axe': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:golden_axe')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_golden_boots': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:golden_boots')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_golden_chestplate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:golden_chestplate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_golden_helmet': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:golden_helmet')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_golden_hoe': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:golden_hoe')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_golden_horse_armor': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:golden_horse_armor')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_golden_leggings': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:golden_leggings')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_golden_nautilus_armor': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:golden_nautilus_armor')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_golden_pickaxe': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:golden_pickaxe')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_golden_shovel': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:golden_shovel')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_golden_spear': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:golden_spear')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_golden_sword': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:golden_sword')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:gold_nugget_from_smelting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[
        [
            'has_the_recipe',
            'has_golden_pickaxe',
            'has_golden_shovel',
            'has_golden_axe',
            'has_golden_hoe',
            'has_golden_sword',
            'has_golden_spear',
            'has_golden_helmet',
            'has_golden_chestplate',
            'has_golden_leggings',
            'has_golden_boots',
            'has_golden_horse_armor',
            'has_golden_nautilus_armor',
        ],
    ],
    rewards=AdvancementRewards(recipes=['minecraft:gold_nugget_from_smelting']),
)

GRAY_DYE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_black_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:black_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:gray_dye'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_white_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:white_dye')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_white_dye', 'has_black_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:gray_dye']),
)

GRAY_DYE_FROM_CLOSED_EYEBLOSSOM = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_closed_eyeblossom': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:closed_eyeblossom')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:gray_dye_from_closed_eyeblossom'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_closed_eyeblossom']],
    rewards=AdvancementRewards(recipes=['minecraft:gray_dye_from_closed_eyeblossom']),
)

GREEN_DYE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cactus': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cactus')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:green_dye'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cactus']],
    rewards=AdvancementRewards(recipes=['minecraft:green_dye']),
)

HOST_ARMOR_TRIM_SMITHING_TEMPLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_host_armor_trim_smithing_template': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:host_armor_trim_smithing_template')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:host_armor_trim_smithing_template'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_host_armor_trim_smithing_template']],
    rewards=AdvancementRewards(recipes=['minecraft:host_armor_trim_smithing_template']),
)

HOST_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_smithing_trim_template': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:host_armor_trim_smithing_template')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:host_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_smithing_trim_template']],
    rewards=AdvancementRewards(recipes=['minecraft:host_armor_trim_smithing_template_smithing_trim']),
)

IRON_INGOT_FROM_BLASTING_DEEPSLATE_IRON_ORE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate_iron_ore': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate_iron_ore')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:iron_ingot_from_blasting_deepslate_iron_ore'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate_iron_ore']],
    rewards=AdvancementRewards(recipes=['minecraft:iron_ingot_from_blasting_deepslate_iron_ore']),
)

IRON_INGOT_FROM_BLASTING_IRON_ORE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_iron_ore': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_ore')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:iron_ingot_from_blasting_iron_ore'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_iron_ore']],
    rewards=AdvancementRewards(recipes=['minecraft:iron_ingot_from_blasting_iron_ore']),
)

IRON_INGOT_FROM_BLASTING_RAW_IRON = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_raw_iron': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:raw_iron')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:iron_ingot_from_blasting_raw_iron'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_raw_iron']],
    rewards=AdvancementRewards(recipes=['minecraft:iron_ingot_from_blasting_raw_iron']),
)

IRON_INGOT_FROM_IRON_BLOCK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_iron_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:iron_ingot_from_iron_block'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_iron_block']],
    rewards=AdvancementRewards(recipes=['minecraft:iron_ingot_from_iron_block']),
)

IRON_INGOT_FROM_NUGGETS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_iron_nugget': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_nugget')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:iron_ingot_from_nuggets'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_iron_nugget']],
    rewards=AdvancementRewards(recipes=['minecraft:iron_ingot_from_nuggets']),
)

IRON_INGOT_FROM_SMELTING_DEEPSLATE_IRON_ORE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate_iron_ore': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate_iron_ore')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:iron_ingot_from_smelting_deepslate_iron_ore'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate_iron_ore']],
    rewards=AdvancementRewards(recipes=['minecraft:iron_ingot_from_smelting_deepslate_iron_ore']),
)

IRON_INGOT_FROM_SMELTING_IRON_ORE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_iron_ore': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_ore')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:iron_ingot_from_smelting_iron_ore'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_iron_ore']],
    rewards=AdvancementRewards(recipes=['minecraft:iron_ingot_from_smelting_iron_ore']),
)

IRON_INGOT_FROM_SMELTING_RAW_IRON = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_raw_iron': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:raw_iron')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:iron_ingot_from_smelting_raw_iron'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_raw_iron']],
    rewards=AdvancementRewards(recipes=['minecraft:iron_ingot_from_smelting_raw_iron']),
)

IRON_NUGGET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_iron_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:iron_nugget'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_iron_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:iron_nugget']),
)

IRON_NUGGET_FROM_BLASTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_chainmail_boots': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:chainmail_boots')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_chainmail_chestplate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:chainmail_chestplate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_chainmail_helmet': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:chainmail_helmet')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_chainmail_leggings': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:chainmail_leggings')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_iron_axe': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_axe')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_iron_boots': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_boots')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_iron_chestplate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_chestplate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_iron_helmet': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_helmet')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_iron_hoe': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_hoe')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_iron_horse_armor': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_horse_armor')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_iron_leggings': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_leggings')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_iron_nautilus_armor': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_nautilus_armor')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_iron_pickaxe': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_pickaxe')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_iron_shovel': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_shovel')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_iron_spear': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_spear')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_iron_sword': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_sword')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:iron_nugget_from_blasting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[
        [
            'has_the_recipe',
            'has_iron_pickaxe',
            'has_iron_shovel',
            'has_iron_axe',
            'has_iron_hoe',
            'has_iron_sword',
            'has_iron_spear',
            'has_iron_helmet',
            'has_iron_chestplate',
            'has_iron_leggings',
            'has_iron_boots',
            'has_iron_horse_armor',
            'has_chainmail_helmet',
            'has_chainmail_chestplate',
            'has_chainmail_leggings',
            'has_chainmail_boots',
            'has_iron_nautilus_armor',
        ],
    ],
    rewards=AdvancementRewards(recipes=['minecraft:iron_nugget_from_blasting']),
)

IRON_NUGGET_FROM_SMELTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_chainmail_boots': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:chainmail_boots')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_chainmail_chestplate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:chainmail_chestplate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_chainmail_helmet': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:chainmail_helmet')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_chainmail_leggings': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:chainmail_leggings')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_iron_axe': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_axe')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_iron_boots': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_boots')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_iron_chestplate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_chestplate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_iron_helmet': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_helmet')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_iron_hoe': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_hoe')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_iron_horse_armor': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_horse_armor')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_iron_leggings': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_leggings')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_iron_nautilus_armor': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_nautilus_armor')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_iron_pickaxe': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_pickaxe')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_iron_shovel': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_shovel')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_iron_spear': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_spear')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_iron_sword': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_sword')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:iron_nugget_from_smelting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[
        [
            'has_the_recipe',
            'has_iron_pickaxe',
            'has_iron_shovel',
            'has_iron_axe',
            'has_iron_hoe',
            'has_iron_sword',
            'has_iron_spear',
            'has_iron_helmet',
            'has_iron_chestplate',
            'has_iron_leggings',
            'has_iron_boots',
            'has_iron_horse_armor',
            'has_chainmail_helmet',
            'has_chainmail_chestplate',
            'has_chainmail_leggings',
            'has_chainmail_boots',
            'has_iron_nautilus_armor',
        ],
    ],
    rewards=AdvancementRewards(recipes=['minecraft:iron_nugget_from_smelting']),
)

LAPIS_LAZULI = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_lapis_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:lapis_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:lapis_lazuli'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_lapis_block']],
    rewards=AdvancementRewards(recipes=['minecraft:lapis_lazuli']),
)

LAPIS_LAZULI_FROM_BLASTING_DEEPSLATE_LAPIS_ORE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate_lapis_ore': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate_lapis_ore')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:lapis_lazuli_from_blasting_deepslate_lapis_ore'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate_lapis_ore']],
    rewards=AdvancementRewards(recipes=['minecraft:lapis_lazuli_from_blasting_deepslate_lapis_ore']),
)

LAPIS_LAZULI_FROM_BLASTING_LAPIS_ORE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_lapis_ore': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:lapis_ore')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:lapis_lazuli_from_blasting_lapis_ore'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_lapis_ore']],
    rewards=AdvancementRewards(recipes=['minecraft:lapis_lazuli_from_blasting_lapis_ore']),
)

LAPIS_LAZULI_FROM_SMELTING_DEEPSLATE_LAPIS_ORE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate_lapis_ore': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate_lapis_ore')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:lapis_lazuli_from_smelting_deepslate_lapis_ore'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate_lapis_ore']],
    rewards=AdvancementRewards(recipes=['minecraft:lapis_lazuli_from_smelting_deepslate_lapis_ore']),
)

LAPIS_LAZULI_FROM_SMELTING_LAPIS_ORE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_lapis_ore': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:lapis_ore')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:lapis_lazuli_from_smelting_lapis_ore'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_lapis_ore']],
    rewards=AdvancementRewards(recipes=['minecraft:lapis_lazuli_from_smelting_lapis_ore']),
)

LEAF_LITTER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_leaves': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:leaves')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:leaf_litter'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_leaves']],
    rewards=AdvancementRewards(recipes=['minecraft:leaf_litter']),
)

LEATHER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_rabbit_hide': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:rabbit_hide')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:leather'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_rabbit_hide']],
    rewards=AdvancementRewards(recipes=['minecraft:leather']),
)

LEATHER_BOOTS_DYED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_leather_boots': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:leather_boots')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:leather_boots_dyed'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_leather_boots']],
    rewards=AdvancementRewards(recipes=['minecraft:leather_boots_dyed']),
)

LEATHER_CHESTPLATE_DYED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_leather_chestplate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:leather_chestplate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:leather_chestplate_dyed'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_leather_chestplate']],
    rewards=AdvancementRewards(recipes=['minecraft:leather_chestplate_dyed']),
)

LEATHER_HELMET_DYED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_leather_helmet': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:leather_helmet')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:leather_helmet_dyed'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_leather_helmet']],
    rewards=AdvancementRewards(recipes=['minecraft:leather_helmet_dyed']),
)

LEATHER_HORSE_ARMOR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_leather': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:leather')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:leather_horse_armor'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_leather']],
    rewards=AdvancementRewards(recipes=['minecraft:leather_horse_armor']),
)

LEATHER_HORSE_ARMOR_DYED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_leather_horse_armor': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:leather_horse_armor')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:leather_horse_armor_dyed'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_leather_horse_armor']],
    rewards=AdvancementRewards(recipes=['minecraft:leather_horse_armor_dyed']),
)

LEATHER_LEGGINGS_DYED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_leather_leggings': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:leather_leggings')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:leather_leggings_dyed'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_leather_leggings']],
    rewards=AdvancementRewards(recipes=['minecraft:leather_leggings_dyed']),
)

LIGHT_BLUE_DYE_FROM_BLUE_ORCHID = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blue_orchid': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blue_orchid')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_blue_dye_from_blue_orchid'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_blue_orchid']],
    rewards=AdvancementRewards(recipes=['minecraft:light_blue_dye_from_blue_orchid']),
)

LIGHT_BLUE_DYE_FROM_BLUE_WHITE_DYE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blue_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blue_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_blue_dye_from_blue_white_dye'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_white_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:white_dye')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_blue_dye', 'has_white_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:light_blue_dye_from_blue_white_dye']),
)

LIGHT_GRAY_DYE_FROM_AZURE_BLUET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_azure_bluet': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:azure_bluet')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_gray_dye_from_azure_bluet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_azure_bluet']],
    rewards=AdvancementRewards(recipes=['minecraft:light_gray_dye_from_azure_bluet']),
)

LIGHT_GRAY_DYE_FROM_BLACK_WHITE_DYE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_black_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:black_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_gray_dye_from_black_white_dye'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_white_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:white_dye')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_white_dye', 'has_black_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:light_gray_dye_from_black_white_dye']),
)

LIGHT_GRAY_DYE_FROM_GRAY_WHITE_DYE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gray_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gray_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_gray_dye_from_gray_white_dye'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_white_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:white_dye')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_gray_dye', 'has_white_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:light_gray_dye_from_gray_white_dye']),
)

LIGHT_GRAY_DYE_FROM_OXEYE_DAISY = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_oxeye_daisy': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oxeye_daisy')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_gray_dye_from_oxeye_daisy'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_oxeye_daisy']],
    rewards=AdvancementRewards(recipes=['minecraft:light_gray_dye_from_oxeye_daisy']),
)

LIGHT_GRAY_DYE_FROM_WHITE_TULIP = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_gray_dye_from_white_tulip'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_white_tulip': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:white_tulip')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_white_tulip']],
    rewards=AdvancementRewards(recipes=['minecraft:light_gray_dye_from_white_tulip']),
)

LIME_DYE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_green_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:green_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:lime_dye'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_white_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:white_dye')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_green_dye', 'has_white_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:lime_dye']),
)

LIME_DYE_FROM_SMELTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sea_pickle': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sea_pickle')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:lime_dye_from_smelting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sea_pickle']],
    rewards=AdvancementRewards(recipes=['minecraft:lime_dye_from_smelting']),
)

MAGENTA_DYE_FROM_ALLIUM = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_allium': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:allium')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:magenta_dye_from_allium'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_allium']],
    rewards=AdvancementRewards(recipes=['minecraft:magenta_dye_from_allium']),
)

MAGENTA_DYE_FROM_BLUE_RED_PINK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blue_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blue_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_pink_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pink_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_red_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:magenta_dye_from_blue_red_pink'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_pink_dye', 'has_blue_dye', 'has_red_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:magenta_dye_from_blue_red_pink']),
)

MAGENTA_DYE_FROM_BLUE_RED_WHITE_DYE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blue_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blue_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_rose_red': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:magenta_dye_from_blue_red_white_dye'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_white_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:white_dye')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_blue_dye', 'has_rose_red', 'has_white_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:magenta_dye_from_blue_red_white_dye']),
)

MAGENTA_DYE_FROM_LILAC = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_lilac': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:lilac')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:magenta_dye_from_lilac'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_lilac']],
    rewards=AdvancementRewards(recipes=['minecraft:magenta_dye_from_lilac']),
)

MAGENTA_DYE_FROM_PURPLE_AND_PINK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_pink_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pink_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_purple_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:purple_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:magenta_dye_from_purple_and_pink'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_pink_dye', 'has_purple_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:magenta_dye_from_purple_and_pink']),
)

MAP = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_compass': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:compass')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:map'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_compass']],
    rewards=AdvancementRewards(recipes=['minecraft:map']),
)

MAP_CLONING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_filled_map': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:filled_map')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:map_cloning'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_filled_map']],
    rewards=AdvancementRewards(recipes=['minecraft:map_cloning']),
)

MELON_SEEDS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_melon': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:melon_slice')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:melon_seeds'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_melon']],
    rewards=AdvancementRewards(recipes=['minecraft:melon_seeds']),
)

MOJANG_BANNER_PATTERN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_enchanted_golden_apple': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:enchanted_golden_apple')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:mojang_banner_pattern'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_enchanted_golden_apple']],
    rewards=AdvancementRewards(recipes=['minecraft:mojang_banner_pattern']),
)

MUSIC_DISC_5 = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_disc_fragment_5': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:disc_fragment_5')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:music_disc_5'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_disc_fragment_5']],
    rewards=AdvancementRewards(recipes=['minecraft:music_disc_5']),
)

NETHERITE_INGOT = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_netherite_scrap': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:netherite_scrap')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:netherite_ingot'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_netherite_scrap']],
    rewards=AdvancementRewards(recipes=['minecraft:netherite_ingot']),
)

NETHERITE_INGOT_FROM_NETHERITE_BLOCK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_netherite_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:netherite_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:netherite_ingot_from_netherite_block'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_netherite_block']],
    rewards=AdvancementRewards(recipes=['minecraft:netherite_ingot_from_netherite_block']),
)

NETHERITE_SCRAP = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_ancient_debris': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:ancient_debris')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:netherite_scrap'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_ancient_debris']],
    rewards=AdvancementRewards(recipes=['minecraft:netherite_scrap']),
)

NETHERITE_SCRAP_FROM_BLASTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_ancient_debris': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:ancient_debris')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:netherite_scrap_from_blasting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_ancient_debris']],
    rewards=AdvancementRewards(recipes=['minecraft:netherite_scrap_from_blasting']),
)

NETHERITE_UPGRADE_SMITHING_TEMPLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_netherite_upgrade_smithing_template': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:netherite_upgrade_smithing_template')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:netherite_upgrade_smithing_template'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_netherite_upgrade_smithing_template']],
    rewards=AdvancementRewards(recipes=['minecraft:netherite_upgrade_smithing_template']),
)

NETHER_BRICK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_netherrack': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:netherrack')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:nether_brick'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_netherrack']],
    rewards=AdvancementRewards(recipes=['minecraft:nether_brick']),
)

ORANGE_DYE_FROM_OPEN_EYEBLOSSOM = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_open_eyeblossom': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:open_eyeblossom')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:orange_dye_from_open_eyeblossom'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_open_eyeblossom']],
    rewards=AdvancementRewards(recipes=['minecraft:orange_dye_from_open_eyeblossom']),
)

ORANGE_DYE_FROM_ORANGE_TULIP = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_orange_tulip': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:orange_tulip')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:orange_dye_from_orange_tulip'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_orange_tulip']],
    rewards=AdvancementRewards(recipes=['minecraft:orange_dye_from_orange_tulip']),
)

ORANGE_DYE_FROM_RED_YELLOW = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_red_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:orange_dye_from_red_yellow'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_yellow_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:yellow_dye')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_red_dye', 'has_yellow_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:orange_dye_from_red_yellow']),
)

ORANGE_DYE_FROM_TORCHFLOWER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:orange_dye_from_torchflower'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_torchflower': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:torchflower')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_torchflower']],
    rewards=AdvancementRewards(recipes=['minecraft:orange_dye_from_torchflower']),
)

PAPER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_reeds': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sugar_cane')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:paper'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_reeds']],
    rewards=AdvancementRewards(recipes=['minecraft:paper']),
)

PINK_DYE_FROM_CACTUS_FLOWER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cactus_flower': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cactus_flower')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pink_dye_from_cactus_flower'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cactus_flower']],
    rewards=AdvancementRewards(recipes=['minecraft:pink_dye_from_cactus_flower']),
)

PINK_DYE_FROM_PEONY = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_peony': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:peony')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pink_dye_from_peony'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_peony']],
    rewards=AdvancementRewards(recipes=['minecraft:pink_dye_from_peony']),
)

PINK_DYE_FROM_PINK_PETALS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_pink_petals': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pink_petals')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pink_dye_from_pink_petals'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_pink_petals']],
    rewards=AdvancementRewards(recipes=['minecraft:pink_dye_from_pink_petals']),
)

PINK_DYE_FROM_PINK_TULIP = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_pink_tulip': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pink_tulip')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pink_dye_from_pink_tulip'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_pink_tulip']],
    rewards=AdvancementRewards(recipes=['minecraft:pink_dye_from_pink_tulip']),
)

PINK_DYE_FROM_RED_WHITE_DYE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_red_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pink_dye_from_red_white_dye'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_white_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:white_dye')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_white_dye', 'has_red_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:pink_dye_from_red_white_dye']),
)

POPPED_CHORUS_FRUIT = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_chorus_fruit': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:chorus_fruit')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:popped_chorus_fruit'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_chorus_fruit']],
    rewards=AdvancementRewards(recipes=['minecraft:popped_chorus_fruit']),
)

PUMPKIN_SEEDS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_pumpkin': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pumpkin')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pumpkin_seeds'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_pumpkin']],
    rewards=AdvancementRewards(recipes=['minecraft:pumpkin_seeds']),
)

PURPLE_DYE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blue_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blue_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_red_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:purple_dye'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_blue_dye', 'has_red_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:purple_dye']),
)

QUARTZ = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_nether_quartz_ore': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:nether_quartz_ore')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:quartz'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_nether_quartz_ore']],
    rewards=AdvancementRewards(recipes=['minecraft:quartz']),
)

QUARTZ_FROM_BLASTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_nether_quartz_ore': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:nether_quartz_ore')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:quartz_from_blasting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_nether_quartz_ore']],
    rewards=AdvancementRewards(recipes=['minecraft:quartz_from_blasting']),
)

RAISER_ARMOR_TRIM_SMITHING_TEMPLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_raiser_armor_trim_smithing_template': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:raiser_armor_trim_smithing_template')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:raiser_armor_trim_smithing_template'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_raiser_armor_trim_smithing_template']],
    rewards=AdvancementRewards(recipes=['minecraft:raiser_armor_trim_smithing_template']),
)

RAISER_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_smithing_trim_template': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:raiser_armor_trim_smithing_template')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:raiser_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_smithing_trim_template']],
    rewards=AdvancementRewards(recipes=['minecraft:raiser_armor_trim_smithing_template_smithing_trim']),
)

RAW_COPPER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_raw_copper_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:raw_copper_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:raw_copper'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_raw_copper_block']],
    rewards=AdvancementRewards(recipes=['minecraft:raw_copper']),
)

RAW_GOLD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_raw_gold_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:raw_gold_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:raw_gold'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_raw_gold_block']],
    rewards=AdvancementRewards(recipes=['minecraft:raw_gold']),
)

RAW_IRON = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_raw_iron_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:raw_iron_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:raw_iron'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_raw_iron_block']],
    rewards=AdvancementRewards(recipes=['minecraft:raw_iron']),
)

RED_DYE_FROM_BEETROOT = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_beetroot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:beetroot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:red_dye_from_beetroot'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_beetroot']],
    rewards=AdvancementRewards(recipes=['minecraft:red_dye_from_beetroot']),
)

RED_DYE_FROM_POPPY = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_poppy': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:poppy')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:red_dye_from_poppy'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_poppy']],
    rewards=AdvancementRewards(recipes=['minecraft:red_dye_from_poppy']),
)

RED_DYE_FROM_ROSE_BUSH = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_rose_bush': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:rose_bush')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:red_dye_from_rose_bush'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_rose_bush']],
    rewards=AdvancementRewards(recipes=['minecraft:red_dye_from_rose_bush']),
)

RED_DYE_FROM_TULIP = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_red_flower': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_tulip')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:red_dye_from_tulip'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_red_flower']],
    rewards=AdvancementRewards(recipes=['minecraft:red_dye_from_tulip']),
)

RESIN_BRICK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_resin_clump': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:resin_clump')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:resin_brick'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_resin_clump']],
    rewards=AdvancementRewards(recipes=['minecraft:resin_brick']),
)

RESIN_CLUMP = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_resin_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:resin_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:resin_clump'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_resin_block']],
    rewards=AdvancementRewards(recipes=['minecraft:resin_clump']),
)

RIB_ARMOR_TRIM_SMITHING_TEMPLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_rib_armor_trim_smithing_template': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:rib_armor_trim_smithing_template')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:rib_armor_trim_smithing_template'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_rib_armor_trim_smithing_template']],
    rewards=AdvancementRewards(recipes=['minecraft:rib_armor_trim_smithing_template']),
)

RIB_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_smithing_trim_template': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:rib_armor_trim_smithing_template')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:rib_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_smithing_trim_template']],
    rewards=AdvancementRewards(recipes=['minecraft:rib_armor_trim_smithing_template_smithing_trim']),
)

SENTRY_ARMOR_TRIM_SMITHING_TEMPLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sentry_armor_trim_smithing_template': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sentry_armor_trim_smithing_template')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:sentry_armor_trim_smithing_template'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sentry_armor_trim_smithing_template']],
    rewards=AdvancementRewards(recipes=['minecraft:sentry_armor_trim_smithing_template']),
)

SENTRY_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_smithing_trim_template': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sentry_armor_trim_smithing_template')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:sentry_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_smithing_trim_template']],
    rewards=AdvancementRewards(recipes=['minecraft:sentry_armor_trim_smithing_template_smithing_trim']),
)

SHAPER_ARMOR_TRIM_SMITHING_TEMPLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_shaper_armor_trim_smithing_template': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:shaper_armor_trim_smithing_template')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:shaper_armor_trim_smithing_template'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_shaper_armor_trim_smithing_template']],
    rewards=AdvancementRewards(recipes=['minecraft:shaper_armor_trim_smithing_template']),
)

SHAPER_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_smithing_trim_template': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:shaper_armor_trim_smithing_template')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:shaper_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_smithing_trim_template']],
    rewards=AdvancementRewards(recipes=['minecraft:shaper_armor_trim_smithing_template_smithing_trim']),
)

SILENCE_ARMOR_TRIM_SMITHING_TEMPLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_silence_armor_trim_smithing_template': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:silence_armor_trim_smithing_template')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:silence_armor_trim_smithing_template'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_silence_armor_trim_smithing_template']],
    rewards=AdvancementRewards(recipes=['minecraft:silence_armor_trim_smithing_template']),
)

SILENCE_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_smithing_trim_template': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:silence_armor_trim_smithing_template')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:silence_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_smithing_trim_template']],
    rewards=AdvancementRewards(recipes=['minecraft:silence_armor_trim_smithing_template_smithing_trim']),
)

SKULL_BANNER_PATTERN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:skull_banner_pattern'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_wither_skeleton_skull': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:wither_skeleton_skull')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_wither_skeleton_skull']],
    rewards=AdvancementRewards(recipes=['minecraft:skull_banner_pattern']),
)

SLIME_BALL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_slime_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:slime_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:slime_ball'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_slime_block']],
    rewards=AdvancementRewards(recipes=['minecraft:slime_ball']),
)

SNOUT_ARMOR_TRIM_SMITHING_TEMPLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_snout_armor_trim_smithing_template': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:snout_armor_trim_smithing_template')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:snout_armor_trim_smithing_template'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_snout_armor_trim_smithing_template']],
    rewards=AdvancementRewards(recipes=['minecraft:snout_armor_trim_smithing_template']),
)

SNOUT_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_smithing_trim_template': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:snout_armor_trim_smithing_template')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:snout_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_smithing_trim_template']],
    rewards=AdvancementRewards(recipes=['minecraft:snout_armor_trim_smithing_template_smithing_trim']),
)

SPIRE_ARMOR_TRIM_SMITHING_TEMPLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_spire_armor_trim_smithing_template': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:spire_armor_trim_smithing_template')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:spire_armor_trim_smithing_template'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_spire_armor_trim_smithing_template']],
    rewards=AdvancementRewards(recipes=['minecraft:spire_armor_trim_smithing_template']),
)

SPIRE_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_smithing_trim_template': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:spire_armor_trim_smithing_template')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:spire_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_smithing_trim_template']],
    rewards=AdvancementRewards(recipes=['minecraft:spire_armor_trim_smithing_template_smithing_trim']),
)

STICK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stick'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:stick']),
)

STICK_FROM_BAMBOO_ITEM = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_bamboo': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:bamboo')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stick_from_bamboo_item'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_bamboo']],
    rewards=AdvancementRewards(recipes=['minecraft:stick_from_bamboo_item']),
)

SUGAR_FROM_HONEY_BOTTLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_honey_bottle': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:honey_bottle')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:sugar_from_honey_bottle'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_honey_bottle']],
    rewards=AdvancementRewards(recipes=['minecraft:sugar_from_honey_bottle']),
)

SUGAR_FROM_SUGAR_CANE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sugar_cane': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sugar_cane')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:sugar_from_sugar_cane'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sugar_cane']],
    rewards=AdvancementRewards(recipes=['minecraft:sugar_from_sugar_cane']),
)

TIDE_ARMOR_TRIM_SMITHING_TEMPLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:tide_armor_trim_smithing_template'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_tide_armor_trim_smithing_template': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:tide_armor_trim_smithing_template')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_tide_armor_trim_smithing_template']],
    rewards=AdvancementRewards(recipes=['minecraft:tide_armor_trim_smithing_template']),
)

TIDE_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_smithing_trim_template': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:tide_armor_trim_smithing_template')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:tide_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_smithing_trim_template']],
    rewards=AdvancementRewards(recipes=['minecraft:tide_armor_trim_smithing_template_smithing_trim']),
)

TIPPED_ARROW = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_lingering_potion': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:lingering_potion')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:tipped_arrow'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_lingering_potion']],
    rewards=AdvancementRewards(recipes=['minecraft:tipped_arrow']),
)

VEX_ARMOR_TRIM_SMITHING_TEMPLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:vex_armor_trim_smithing_template'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_vex_armor_trim_smithing_template': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:vex_armor_trim_smithing_template')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_vex_armor_trim_smithing_template']],
    rewards=AdvancementRewards(recipes=['minecraft:vex_armor_trim_smithing_template']),
)

VEX_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_smithing_trim_template': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:vex_armor_trim_smithing_template')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:vex_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_smithing_trim_template']],
    rewards=AdvancementRewards(recipes=['minecraft:vex_armor_trim_smithing_template_smithing_trim']),
)

WARD_ARMOR_TRIM_SMITHING_TEMPLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:ward_armor_trim_smithing_template'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_ward_armor_trim_smithing_template': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:ward_armor_trim_smithing_template')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_ward_armor_trim_smithing_template']],
    rewards=AdvancementRewards(recipes=['minecraft:ward_armor_trim_smithing_template']),
)

WARD_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_smithing_trim_template': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:ward_armor_trim_smithing_template')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:ward_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_smithing_trim_template']],
    rewards=AdvancementRewards(recipes=['minecraft:ward_armor_trim_smithing_template_smithing_trim']),
)

WAYFINDER_ARMOR_TRIM_SMITHING_TEMPLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:wayfinder_armor_trim_smithing_template'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_wayfinder_armor_trim_smithing_template': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(
                items=[ItemPredicate(items='minecraft:wayfinder_armor_trim_smithing_template')],
            ),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_wayfinder_armor_trim_smithing_template']],
    rewards=AdvancementRewards(recipes=['minecraft:wayfinder_armor_trim_smithing_template']),
)

WAYFINDER_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_smithing_trim_template': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(
                items=[ItemPredicate(items='minecraft:wayfinder_armor_trim_smithing_template')],
            ),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:wayfinder_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_smithing_trim_template']],
    rewards=AdvancementRewards(recipes=['minecraft:wayfinder_armor_trim_smithing_template_smithing_trim']),
)

WHEAT = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_hay_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:hay_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:wheat'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_hay_block']],
    rewards=AdvancementRewards(recipes=['minecraft:wheat']),
)

WHITE_DYE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_bone_meal': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:bone_meal')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:white_dye'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_bone_meal']],
    rewards=AdvancementRewards(recipes=['minecraft:white_dye']),
)

WHITE_DYE_FROM_LILY_OF_THE_VALLEY = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_lily_of_the_valley': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:lily_of_the_valley')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:white_dye_from_lily_of_the_valley'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_lily_of_the_valley']],
    rewards=AdvancementRewards(recipes=['minecraft:white_dye_from_lily_of_the_valley']),
)

WILD_ARMOR_TRIM_SMITHING_TEMPLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:wild_armor_trim_smithing_template'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_wild_armor_trim_smithing_template': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:wild_armor_trim_smithing_template')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_wild_armor_trim_smithing_template']],
    rewards=AdvancementRewards(recipes=['minecraft:wild_armor_trim_smithing_template']),
)

WILD_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_smithing_trim_template': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:wild_armor_trim_smithing_template')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:wild_armor_trim_smithing_template_smithing_trim'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_smithing_trim_template']],
    rewards=AdvancementRewards(recipes=['minecraft:wild_armor_trim_smithing_template_smithing_trim']),
)

WIND_CHARGE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_breeze_rod': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:breeze_rod')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:wind_charge'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_breeze_rod']],
    rewards=AdvancementRewards(recipes=['minecraft:wind_charge']),
)

WOLF_ARMOR_DYED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:wolf_armor_dyed'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_wolf_armor': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:wolf_armor')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_wolf_armor']],
    rewards=AdvancementRewards(recipes=['minecraft:wolf_armor_dyed']),
)

WRITABLE_BOOK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_book': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:book')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:writable_book'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_book']],
    rewards=AdvancementRewards(recipes=['minecraft:writable_book']),
)

YELLOW_DYE_FROM_DANDELION = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_dandelion': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dandelion')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:yellow_dye_from_dandelion'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_dandelion']],
    rewards=AdvancementRewards(recipes=['minecraft:yellow_dye_from_dandelion']),
)

YELLOW_DYE_FROM_GOLDEN_DANDELION = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_golden_dandelion': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:golden_dandelion')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:yellow_dye_from_golden_dandelion'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_golden_dandelion']],
    rewards=AdvancementRewards(recipes=['minecraft:yellow_dye_from_golden_dandelion']),
)

YELLOW_DYE_FROM_SUNFLOWER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sunflower': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sunflower')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:yellow_dye_from_sunflower'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sunflower']],
    rewards=AdvancementRewards(recipes=['minecraft:yellow_dye_from_sunflower']),
)

YELLOW_DYE_FROM_WILDFLOWERS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:yellow_dye_from_wildflowers'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_wildflowers': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:wildflowers')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_wildflowers']],
    rewards=AdvancementRewards(recipes=['minecraft:yellow_dye_from_wildflowers']),
)
