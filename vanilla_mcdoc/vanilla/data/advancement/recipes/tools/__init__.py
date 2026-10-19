"""Vanilla's data/advancement/recipes/tools/ files"""
from vanilla_mcdoc.data.advancement.Advancement import Advancement
from vanilla_mcdoc.data.advancement.AdvancementCriterion import AdvancementCriterionInventoryChanged, AdvancementCriterionRecipeUnlocked
from vanilla_mcdoc.data.advancement.AdvancementRewards import AdvancementRewards
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.advancement.trigger.InventoryChangeTrigger import InventoryChangeTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.RecipeUnlockedTrigger import RecipeUnlockedTriggerTypeArg

BLACK_BUNDLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_black_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:black_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:black_bundle'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_black_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:black_bundle']),
)

BLUE_BUNDLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blue_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blue_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:blue_bundle'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_blue_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:blue_bundle']),
)

BROWN_BUNDLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_brown_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:brown_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:brown_bundle'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_brown_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:brown_bundle']),
)

BRUSH = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:brush'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:brush']),
)

BUNDLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_string': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:string')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:bundle'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_string']],
    rewards=AdvancementRewards(recipes=['minecraft:bundle']),
)

CLOCK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_redstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:redstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:clock'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_redstone']],
    rewards=AdvancementRewards(recipes=['minecraft:clock']),
)

COMPASS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_redstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:redstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:compass'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_redstone']],
    rewards=AdvancementRewards(recipes=['minecraft:compass']),
)

COPPER_AXE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:copper_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:copper_axe'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:copper_axe']),
)

COPPER_HOE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:copper_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:copper_hoe'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:copper_hoe']),
)

COPPER_PICKAXE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:copper_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:copper_pickaxe'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:copper_pickaxe']),
)

COPPER_SHOVEL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:copper_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:copper_shovel'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:copper_shovel']),
)

CYAN_BUNDLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cyan_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cyan_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cyan_bundle'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cyan_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:cyan_bundle']),
)

DIAMOND_AXE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_diamond': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:diamond_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:diamond_axe'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_diamond']],
    rewards=AdvancementRewards(recipes=['minecraft:diamond_axe']),
)

DIAMOND_HOE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_diamond': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:diamond_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:diamond_hoe'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_diamond']],
    rewards=AdvancementRewards(recipes=['minecraft:diamond_hoe']),
)

DIAMOND_PICKAXE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_diamond': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:diamond_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:diamond_pickaxe'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_diamond']],
    rewards=AdvancementRewards(recipes=['minecraft:diamond_pickaxe']),
)

DIAMOND_SHOVEL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_diamond': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:diamond_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:diamond_shovel'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_diamond']],
    rewards=AdvancementRewards(recipes=['minecraft:diamond_shovel']),
)

FISHING_ROD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_string': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:string')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:fishing_rod'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_string']],
    rewards=AdvancementRewards(recipes=['minecraft:fishing_rod']),
)

FLINT_AND_STEEL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_flint': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:flint')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_obsidian': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:obsidian')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:flint_and_steel'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_flint', 'has_obsidian']],
    rewards=AdvancementRewards(recipes=['minecraft:flint_and_steel']),
)

GOLDEN_AXE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gold_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:gold_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:golden_axe'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_gold_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:golden_axe']),
)

GOLDEN_HOE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gold_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:gold_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:golden_hoe'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_gold_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:golden_hoe']),
)

GOLDEN_PICKAXE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gold_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:gold_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:golden_pickaxe'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_gold_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:golden_pickaxe']),
)

GOLDEN_SHOVEL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gold_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:gold_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:golden_shovel'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_gold_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:golden_shovel']),
)

GRAY_BUNDLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gray_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gray_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:gray_bundle'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_gray_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:gray_bundle']),
)

GREEN_BUNDLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_green_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:green_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:green_bundle'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_green_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:green_bundle']),
)

IRON_AXE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_iron_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:iron_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:iron_axe'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_iron_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:iron_axe']),
)

IRON_HOE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_iron_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:iron_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:iron_hoe'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_iron_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:iron_hoe']),
)

IRON_PICKAXE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_iron_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:iron_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:iron_pickaxe'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_iron_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:iron_pickaxe']),
)

IRON_SHOVEL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_iron_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:iron_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:iron_shovel'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_iron_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:iron_shovel']),
)

LEAD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_string': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:string')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:lead'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_string']],
    rewards=AdvancementRewards(recipes=['minecraft:lead']),
)

LIGHT_BLUE_BUNDLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_light_blue_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_blue_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_blue_bundle'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_light_blue_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:light_blue_bundle']),
)

LIGHT_GRAY_BUNDLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_light_gray_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_gray_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_gray_bundle'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_light_gray_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:light_gray_bundle']),
)

LIME_BUNDLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_lime_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:lime_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:lime_bundle'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_lime_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:lime_bundle']),
)

MAGENTA_BUNDLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_magenta_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:magenta_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:magenta_bundle'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_magenta_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:magenta_bundle']),
)

NAME_TAG = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_metal_nugget': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:metal_nuggets')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_name_tag': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:name_tag')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_paper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:paper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:name_tag'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_metal_nugget', 'has_paper', 'has_name_tag']],
    rewards=AdvancementRewards(recipes=['minecraft:name_tag']),
)

NETHERITE_AXE_SMITHING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_netherite_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:netherite_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:netherite_axe_smithing'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_netherite_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:netherite_axe_smithing']),
)

NETHERITE_HOE_SMITHING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_netherite_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:netherite_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:netherite_hoe_smithing'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_netherite_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:netherite_hoe_smithing']),
)

NETHERITE_PICKAXE_SMITHING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_netherite_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:netherite_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:netherite_pickaxe_smithing'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_netherite_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:netherite_pickaxe_smithing']),
)

NETHERITE_SHOVEL_SMITHING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_netherite_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:netherite_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:netherite_shovel_smithing'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_netherite_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:netherite_shovel_smithing']),
)

ORANGE_BUNDLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_orange_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:orange_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:orange_bundle'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_orange_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:orange_bundle']),
)

PINK_BUNDLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_pink_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pink_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pink_bundle'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_pink_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:pink_bundle']),
)

PURPLE_BUNDLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_purple_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:purple_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:purple_bundle'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_purple_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:purple_bundle']),
)

RECOVERY_COMPASS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_echo_shard': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:echo_shard')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:recovery_compass'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_echo_shard']],
    rewards=AdvancementRewards(recipes=['minecraft:recovery_compass']),
)

RED_BUNDLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_red_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:red_bundle'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_red_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:red_bundle']),
)

SHEARS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_iron_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:shears'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_iron_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:shears']),
)

SPYGLASS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_amethyst_shard': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:amethyst_shard')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:spyglass'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_amethyst_shard']],
    rewards=AdvancementRewards(recipes=['minecraft:spyglass']),
)

STONE_AXE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cobblestone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:stone_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stone_axe'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cobblestone']],
    rewards=AdvancementRewards(recipes=['minecraft:stone_axe']),
)

STONE_HOE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cobblestone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:stone_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stone_hoe'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cobblestone']],
    rewards=AdvancementRewards(recipes=['minecraft:stone_hoe']),
)

STONE_PICKAXE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cobblestone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:stone_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stone_pickaxe'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cobblestone']],
    rewards=AdvancementRewards(recipes=['minecraft:stone_pickaxe']),
)

STONE_SHOVEL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cobblestone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:stone_tool_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stone_shovel'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cobblestone']],
    rewards=AdvancementRewards(recipes=['minecraft:stone_shovel']),
)

WHITE_BUNDLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:white_bundle'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_white_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:white_dye')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_white_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:white_bundle']),
)

WOODEN_AXE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stick': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stick')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:wooden_axe'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stick']],
    rewards=AdvancementRewards(recipes=['minecraft:wooden_axe']),
)

WOODEN_HOE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stick': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stick')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:wooden_hoe'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stick']],
    rewards=AdvancementRewards(recipes=['minecraft:wooden_hoe']),
)

WOODEN_PICKAXE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stick': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stick')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:wooden_pickaxe'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stick']],
    rewards=AdvancementRewards(recipes=['minecraft:wooden_pickaxe']),
)

WOODEN_SHOVEL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stick': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stick')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:wooden_shovel'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stick']],
    rewards=AdvancementRewards(recipes=['minecraft:wooden_shovel']),
)

YELLOW_BUNDLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:yellow_bundle'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_yellow_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:yellow_dye')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_yellow_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:yellow_bundle']),
)
