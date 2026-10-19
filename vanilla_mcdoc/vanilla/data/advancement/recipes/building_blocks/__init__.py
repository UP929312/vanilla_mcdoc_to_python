"""Vanilla's data/advancement/recipes/building_blocks/ files"""
from vanilla_mcdoc.data.advancement.Advancement import Advancement
from vanilla_mcdoc.data.advancement.AdvancementCriterion import AdvancementCriterionInventoryChanged, AdvancementCriterionRecipeUnlocked
from vanilla_mcdoc.data.advancement.AdvancementRewards import AdvancementRewards
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.advancement.trigger.InventoryChangeTrigger import InventoryChangeTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.RecipeUnlockedTrigger import RecipeUnlockedTriggerTypeArg

ACACIA_PLANKS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:acacia_logs')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:acacia_planks'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_log']],
    rewards=AdvancementRewards(recipes=['minecraft:acacia_planks']),
)

ACACIA_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:acacia_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:acacia_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:acacia_slab']),
)

ACACIA_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:acacia_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:acacia_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:acacia_stairs']),
)

ACACIA_WOOD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:acacia_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:acacia_wood'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_log']],
    rewards=AdvancementRewards(recipes=['minecraft:acacia_wood']),
)

AMETHYST_BLOCK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_amethyst_shard': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:amethyst_shard')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:amethyst_block'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_amethyst_shard']],
    rewards=AdvancementRewards(recipes=['minecraft:amethyst_block']),
)

ANDESITE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:diorite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:andesite'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stone']],
    rewards=AdvancementRewards(recipes=['minecraft:andesite']),
)

ANDESITE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_andesite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:andesite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:andesite_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_andesite']],
    rewards=AdvancementRewards(recipes=['minecraft:andesite_slab']),
)

ANDESITE_SLAB_FROM_ANDESITE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_andesite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:andesite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:andesite_slab_from_andesite_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_andesite']],
    rewards=AdvancementRewards(recipes=['minecraft:andesite_slab_from_andesite_stonecutting']),
)

ANDESITE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_andesite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:andesite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:andesite_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_andesite']],
    rewards=AdvancementRewards(recipes=['minecraft:andesite_stairs']),
)

ANDESITE_STAIRS_FROM_ANDESITE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_andesite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:andesite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:andesite_stairs_from_andesite_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_andesite']],
    rewards=AdvancementRewards(recipes=['minecraft:andesite_stairs_from_andesite_stonecutting']),
)

BAMBOO_BLOCK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_bamboo': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:bamboo')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:bamboo_block'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_bamboo']],
    rewards=AdvancementRewards(recipes=['minecraft:bamboo_block']),
)

BAMBOO_MOSAIC_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_bamboo_mosaic': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:bamboo_mosaic')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:bamboo_mosaic_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_bamboo_mosaic']],
    rewards=AdvancementRewards(recipes=['minecraft:bamboo_mosaic_slab']),
)

BAMBOO_MOSAIC_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_bamboo_mosaic': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:bamboo_mosaic')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:bamboo_mosaic_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_bamboo_mosaic']],
    rewards=AdvancementRewards(recipes=['minecraft:bamboo_mosaic_stairs']),
)

BAMBOO_PLANKS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_logs': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:bamboo_blocks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:bamboo_planks'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_logs']],
    rewards=AdvancementRewards(recipes=['minecraft:bamboo_planks']),
)

BAMBOO_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:bamboo_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:bamboo_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:bamboo_slab']),
)

BAMBOO_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:bamboo_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:bamboo_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:bamboo_stairs']),
)

BIRCH_PLANKS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_logs': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:birch_logs')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:birch_planks'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_logs']],
    rewards=AdvancementRewards(recipes=['minecraft:birch_planks']),
)

BIRCH_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:birch_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:birch_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:birch_slab']),
)

BIRCH_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:birch_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:birch_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:birch_stairs']),
)

BIRCH_WOOD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:birch_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:birch_wood'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_log']],
    rewards=AdvancementRewards(recipes=['minecraft:birch_wood']),
)

BLACKSTONE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blackstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blackstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:blackstone_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_blackstone']],
    rewards=AdvancementRewards(recipes=['minecraft:blackstone_slab']),
)

BLACKSTONE_SLAB_FROM_BLACKSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blackstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blackstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:blackstone_slab_from_blackstone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_blackstone']],
    rewards=AdvancementRewards(recipes=['minecraft:blackstone_slab_from_blackstone_stonecutting']),
)

BLACKSTONE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blackstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blackstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:blackstone_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_blackstone']],
    rewards=AdvancementRewards(recipes=['minecraft:blackstone_stairs']),
)

BLACKSTONE_STAIRS_FROM_BLACKSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blackstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blackstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:blackstone_stairs_from_blackstone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_blackstone']],
    rewards=AdvancementRewards(recipes=['minecraft:blackstone_stairs_from_blackstone_stonecutting']),
)

BLACK_CONCRETE_POWDER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gravel': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gravel')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_sand': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sand')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:black_concrete_powder'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sand', 'has_gravel']],
    rewards=AdvancementRewards(recipes=['minecraft:black_concrete_powder']),
)

BLACK_CONCRETE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_black_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:black_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:black_concrete_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_black_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:black_concrete_slab']),
)

BLACK_CONCRETE_SLAB_FROM_BLACK_CONCRETE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_black_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:black_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:black_concrete_slab_from_black_concrete_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_black_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:black_concrete_slab_from_black_concrete_stonecutting']),
)

BLACK_CONCRETE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_black_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:black_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:black_concrete_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_black_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:black_concrete_stairs']),
)

BLACK_CONCRETE_STAIRS_FROM_BLACK_CONCRETE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_black_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:black_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:black_concrete_stairs_from_black_concrete_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_black_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:black_concrete_stairs_from_black_concrete_stonecutting']),
)

BLACK_STAINED_GLASS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glass')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:black_stained_glass'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass']],
    rewards=AdvancementRewards(recipes=['minecraft:black_stained_glass']),
)

BLACK_TERRACOTTA = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_terracotta': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:terracotta')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:black_terracotta'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_terracotta']],
    rewards=AdvancementRewards(recipes=['minecraft:black_terracotta']),
)

BLACK_WOOL_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_black_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:black_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:black_wool_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_black_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:black_wool_slab']),
)

BLACK_WOOL_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_black_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:black_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:black_wool_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_black_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:black_wool_stairs']),
)

BLUE_CONCRETE_POWDER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gravel': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gravel')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_sand': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sand')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:blue_concrete_powder'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sand', 'has_gravel']],
    rewards=AdvancementRewards(recipes=['minecraft:blue_concrete_powder']),
)

BLUE_CONCRETE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blue_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blue_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:blue_concrete_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_blue_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:blue_concrete_slab']),
)

BLUE_CONCRETE_SLAB_FROM_BLUE_CONCRETE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blue_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blue_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:blue_concrete_slab_from_blue_concrete_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_blue_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:blue_concrete_slab_from_blue_concrete_stonecutting']),
)

BLUE_CONCRETE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blue_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blue_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:blue_concrete_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_blue_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:blue_concrete_stairs']),
)

BLUE_CONCRETE_STAIRS_FROM_BLUE_CONCRETE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blue_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blue_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:blue_concrete_stairs_from_blue_concrete_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_blue_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:blue_concrete_stairs_from_blue_concrete_stonecutting']),
)

BLUE_ICE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_packed_ice': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:packed_ice')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:blue_ice'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_packed_ice']],
    rewards=AdvancementRewards(recipes=['minecraft:blue_ice']),
)

BLUE_STAINED_GLASS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glass')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:blue_stained_glass'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass']],
    rewards=AdvancementRewards(recipes=['minecraft:blue_stained_glass']),
)

BLUE_TERRACOTTA = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_terracotta': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:terracotta')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:blue_terracotta'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_terracotta']],
    rewards=AdvancementRewards(recipes=['minecraft:blue_terracotta']),
)

BLUE_WOOL_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blue_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blue_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:blue_wool_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_blue_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:blue_wool_slab']),
)

BLUE_WOOL_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blue_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blue_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:blue_wool_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_blue_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:blue_wool_stairs']),
)

BONE_BLOCK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_bone_meal': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:bone_meal')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:bone_block'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_bone_meal']],
    rewards=AdvancementRewards(recipes=['minecraft:bone_block']),
)

BOOKSHELF = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_book': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:book')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:bookshelf'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_book']],
    rewards=AdvancementRewards(recipes=['minecraft:bookshelf']),
)

BRICKS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_brick': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:brick')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:bricks'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_brick']],
    rewards=AdvancementRewards(recipes=['minecraft:bricks']),
)

BRICK_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:brick_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:brick_slab']),
)

BRICK_SLAB_FROM_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:brick_slab_from_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:brick_slab_from_bricks_stonecutting']),
)

BRICK_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:brick_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:brick_stairs']),
)

BRICK_STAIRS_FROM_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:brick_stairs_from_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:brick_stairs_from_bricks_stonecutting']),
)

BROWN_CONCRETE_POWDER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gravel': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gravel')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_sand': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sand')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:brown_concrete_powder'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sand', 'has_gravel']],
    rewards=AdvancementRewards(recipes=['minecraft:brown_concrete_powder']),
)

BROWN_CONCRETE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_brown_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:brown_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:brown_concrete_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_brown_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:brown_concrete_slab']),
)

BROWN_CONCRETE_SLAB_FROM_BROWN_CONCRETE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_brown_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:brown_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:brown_concrete_slab_from_brown_concrete_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_brown_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:brown_concrete_slab_from_brown_concrete_stonecutting']),
)

BROWN_CONCRETE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_brown_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:brown_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:brown_concrete_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_brown_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:brown_concrete_stairs']),
)

BROWN_CONCRETE_STAIRS_FROM_BROWN_CONCRETE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_brown_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:brown_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:brown_concrete_stairs_from_brown_concrete_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_brown_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:brown_concrete_stairs_from_brown_concrete_stonecutting']),
)

BROWN_STAINED_GLASS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glass')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:brown_stained_glass'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass']],
    rewards=AdvancementRewards(recipes=['minecraft:brown_stained_glass']),
)

BROWN_TERRACOTTA = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_terracotta': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:terracotta')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:brown_terracotta'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_terracotta']],
    rewards=AdvancementRewards(recipes=['minecraft:brown_terracotta']),
)

BROWN_WOOL_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_brown_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:brown_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:brown_wool_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_brown_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:brown_wool_slab']),
)

BROWN_WOOL_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_brown_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:brown_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:brown_wool_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_brown_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:brown_wool_stairs']),
)

CHERRY_PLANKS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:cherry_logs')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cherry_planks'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_log']],
    rewards=AdvancementRewards(recipes=['minecraft:cherry_planks']),
)

CHERRY_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cherry_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cherry_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:cherry_slab']),
)

CHERRY_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cherry_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cherry_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:cherry_stairs']),
)

CHERRY_WOOD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cherry_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cherry_wood'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_log']],
    rewards=AdvancementRewards(recipes=['minecraft:cherry_wood']),
)

CHISELED_BOOKSHELF = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_book': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:book')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:chiseled_bookshelf'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_book']],
    rewards=AdvancementRewards(recipes=['minecraft:chiseled_bookshelf']),
)

CHISELED_CINNABAR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cinnabar_slab')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:chiseled_cinnabar'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:chiseled_cinnabar']),
)

CHISELED_CINNABAR_FROM_CINNABAR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cinnabar': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cinnabar')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:chiseled_cinnabar_from_cinnabar_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cinnabar']],
    rewards=AdvancementRewards(recipes=['minecraft:chiseled_cinnabar_from_cinnabar_stonecutting']),
)

CHISELED_COPPER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cut_copper_slab')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:chiseled_copper'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:chiseled_copper']),
)

CHISELED_COPPER_FROM_COPPER_BLOCK_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:chiseled_copper_from_copper_block_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_block']],
    rewards=AdvancementRewards(recipes=['minecraft:chiseled_copper_from_copper_block_stonecutting']),
)

CHISELED_COPPER_FROM_CUT_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:chiseled_copper_from_cut_copper_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:chiseled_copper_from_cut_copper_stonecutting']),
)

CHISELED_DEEPSLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cobbled_deepslate_slab')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:chiseled_deepslate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:chiseled_deepslate']),
)

CHISELED_DEEPSLATE_FROM_COBBLED_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cobbled_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cobbled_deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:chiseled_deepslate_from_cobbled_deepslate_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cobbled_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:chiseled_deepslate_from_cobbled_deepslate_stonecutting']),
)

CHISELED_DEEPSLATE_FROM_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:chiseled_deepslate_from_deepslate_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:chiseled_deepslate_from_deepslate_stonecutting']),
)

CHISELED_NETHER_BRICKS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:nether_brick_slab')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:chiseled_nether_bricks'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:chiseled_nether_bricks']),
)

CHISELED_NETHER_BRICKS_FROM_NETHER_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_nether_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:nether_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:chiseled_nether_bricks_from_nether_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_nether_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:chiseled_nether_bricks_from_nether_bricks_stonecutting']),
)

CHISELED_POLISHED_BLACKSTONE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_blackstone_slab')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:chiseled_polished_blackstone'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:chiseled_polished_blackstone']),
)

CHISELED_POLISHED_BLACKSTONE_FROM_BLACKSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blackstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blackstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:chiseled_polished_blackstone_from_blackstone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_blackstone']],
    rewards=AdvancementRewards(recipes=['minecraft:chiseled_polished_blackstone_from_blackstone_stonecutting']),
)

CHISELED_POLISHED_BLACKSTONE_FROM_POLISHED_BLACKSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_blackstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_blackstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:chiseled_polished_blackstone_from_polished_blackstone_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_blackstone']],
    rewards=AdvancementRewards(recipes=['minecraft:chiseled_polished_blackstone_from_polished_blackstone_stonecutting']),
)

CHISELED_QUARTZ_BLOCK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_chiseled_quartz_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:chiseled_quartz_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_quartz_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:quartz_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_quartz_pillar': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:quartz_pillar')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:chiseled_quartz_block'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_chiseled_quartz_block', 'has_quartz_block', 'has_quartz_pillar']],
    rewards=AdvancementRewards(recipes=['minecraft:chiseled_quartz_block']),
)

CHISELED_QUARTZ_BLOCK_FROM_QUARTZ_BLOCK_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_quartz_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:quartz_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:chiseled_quartz_block_from_quartz_block_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_quartz_block']],
    rewards=AdvancementRewards(recipes=['minecraft:chiseled_quartz_block_from_quartz_block_stonecutting']),
)

CHISELED_RED_SANDSTONE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_chiseled_red_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:chiseled_red_sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_cut_red_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cut_red_sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_red_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:chiseled_red_sandstone'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_red_sandstone', 'has_chiseled_red_sandstone', 'has_cut_red_sandstone']],
    rewards=AdvancementRewards(recipes=['minecraft:chiseled_red_sandstone']),
)

CHISELED_RED_SANDSTONE_FROM_RED_SANDSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_red_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:chiseled_red_sandstone_from_red_sandstone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_red_sandstone']],
    rewards=AdvancementRewards(recipes=['minecraft:chiseled_red_sandstone_from_red_sandstone_stonecutting']),
)

CHISELED_RESIN_BRICKS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:resin_brick_slab')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:chiseled_resin_bricks'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:chiseled_resin_bricks']),
)

CHISELED_RESIN_BRICKS_FROM_RESIN_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_resin_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:resin_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:chiseled_resin_bricks_from_resin_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_resin_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:chiseled_resin_bricks_from_resin_bricks_stonecutting']),
)

CHISELED_SANDSTONE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sandstone_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sandstone_slab')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:chiseled_sandstone'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sandstone_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:chiseled_sandstone']),
)

CHISELED_SANDSTONE_FROM_SANDSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:chiseled_sandstone_from_sandstone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sandstone']],
    rewards=AdvancementRewards(recipes=['minecraft:chiseled_sandstone_from_sandstone_stonecutting']),
)

CHISELED_STONE_BRICKS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_tag': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:stone_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:chiseled_stone_bricks'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_tag']],
    rewards=AdvancementRewards(recipes=['minecraft:chiseled_stone_bricks']),
)

CHISELED_STONE_BRICKS_FROM_STONE_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stone_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stone_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:chiseled_stone_bricks_from_stone_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stone_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:chiseled_stone_bricks_from_stone_bricks_stonecutting']),
)

CHISELED_STONE_BRICKS_FROM_STONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:chiseled_stone_bricks_from_stone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stone']],
    rewards=AdvancementRewards(recipes=['minecraft:chiseled_stone_bricks_from_stone_stonecutting']),
)

CHISELED_SULFUR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sulfur_slab')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:chiseled_sulfur'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:chiseled_sulfur']),
)

CHISELED_SULFUR_FROM_SULFUR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sulfur': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sulfur')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:chiseled_sulfur_from_sulfur_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sulfur']],
    rewards=AdvancementRewards(recipes=['minecraft:chiseled_sulfur_from_sulfur_stonecutting']),
)

CHISELED_TUFF = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:tuff_slab')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:chiseled_tuff'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:chiseled_tuff']),
)

CHISELED_TUFF_BRICKS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:tuff_brick_slab')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:chiseled_tuff_bricks'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:chiseled_tuff_bricks']),
)

CHISELED_TUFF_BRICKS_FROM_POLISHED_TUFF_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_tuff': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_tuff')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:chiseled_tuff_bricks_from_polished_tuff_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_tuff']],
    rewards=AdvancementRewards(recipes=['minecraft:chiseled_tuff_bricks_from_polished_tuff_stonecutting']),
)

CHISELED_TUFF_BRICKS_FROM_TUFF_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:chiseled_tuff_bricks_from_tuff_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_tuff_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:tuff_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_tuff_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:chiseled_tuff_bricks_from_tuff_bricks_stonecutting']),
)

CHISELED_TUFF_BRICKS_FROM_TUFF_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:chiseled_tuff_bricks_from_tuff_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_tuff': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:tuff')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_tuff']],
    rewards=AdvancementRewards(recipes=['minecraft:chiseled_tuff_bricks_from_tuff_stonecutting']),
)

CHISELED_TUFF_FROM_TUFF_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:chiseled_tuff_from_tuff_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_tuff': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:tuff')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_tuff']],
    rewards=AdvancementRewards(recipes=['minecraft:chiseled_tuff_from_tuff_stonecutting']),
)

CINNABAR_BRICKS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_cinnabar': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_cinnabar')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cinnabar_bricks'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_cinnabar']],
    rewards=AdvancementRewards(recipes=['minecraft:cinnabar_bricks']),
)

CINNABAR_BRICKS_FROM_CINNABAR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cinnabar': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cinnabar')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cinnabar_bricks_from_cinnabar_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cinnabar']],
    rewards=AdvancementRewards(recipes=['minecraft:cinnabar_bricks_from_cinnabar_stonecutting']),
)

CINNABAR_BRICKS_FROM_POLISHED_CINNABAR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_cinnabar': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_cinnabar')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cinnabar_bricks_from_polished_cinnabar_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_cinnabar']],
    rewards=AdvancementRewards(recipes=['minecraft:cinnabar_bricks_from_polished_cinnabar_stonecutting']),
)

CINNABAR_BRICK_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cinnabar_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cinnabar_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cinnabar_brick_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cinnabar_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:cinnabar_brick_slab']),
)

CINNABAR_BRICK_SLAB_FROM_CINNABAR_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cinnabar_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cinnabar_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cinnabar_brick_slab_from_cinnabar_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cinnabar_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:cinnabar_brick_slab_from_cinnabar_bricks_stonecutting']),
)

CINNABAR_BRICK_SLAB_FROM_CINNABAR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cinnabar': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cinnabar')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cinnabar_brick_slab_from_cinnabar_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cinnabar']],
    rewards=AdvancementRewards(recipes=['minecraft:cinnabar_brick_slab_from_cinnabar_stonecutting']),
)

CINNABAR_BRICK_SLAB_FROM_POLISHED_CINNABAR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_cinnabar': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_cinnabar')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cinnabar_brick_slab_from_polished_cinnabar_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_cinnabar']],
    rewards=AdvancementRewards(recipes=['minecraft:cinnabar_brick_slab_from_polished_cinnabar_stonecutting']),
)

CINNABAR_BRICK_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cinnabar_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cinnabar_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cinnabar_brick_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cinnabar_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:cinnabar_brick_stairs']),
)

CINNABAR_BRICK_STAIRS_FROM_CINNABAR_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cinnabar_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cinnabar_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cinnabar_brick_stairs_from_cinnabar_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cinnabar_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:cinnabar_brick_stairs_from_cinnabar_bricks_stonecutting']),
)

CINNABAR_BRICK_STAIRS_FROM_CINNABAR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cinnabar': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cinnabar')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cinnabar_brick_stairs_from_cinnabar_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cinnabar']],
    rewards=AdvancementRewards(recipes=['minecraft:cinnabar_brick_stairs_from_cinnabar_stonecutting']),
)

CINNABAR_BRICK_STAIRS_FROM_POLISHED_CINNABAR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_cinnabar': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_cinnabar')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cinnabar_brick_stairs_from_polished_cinnabar_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_cinnabar']],
    rewards=AdvancementRewards(recipes=['minecraft:cinnabar_brick_stairs_from_polished_cinnabar_stonecutting']),
)

CINNABAR_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cinnabar': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cinnabar')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cinnabar_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cinnabar']],
    rewards=AdvancementRewards(recipes=['minecraft:cinnabar_slab']),
)

CINNABAR_SLAB_FROM_CINNABAR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cinnabar': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cinnabar')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cinnabar_slab_from_cinnabar_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cinnabar']],
    rewards=AdvancementRewards(recipes=['minecraft:cinnabar_slab_from_cinnabar_stonecutting']),
)

CINNABAR_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cinnabar': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cinnabar')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cinnabar_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cinnabar']],
    rewards=AdvancementRewards(recipes=['minecraft:cinnabar_stairs']),
)

CINNABAR_STAIRS_FROM_CINNABAR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cinnabar': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cinnabar')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cinnabar_stairs_from_cinnabar_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cinnabar']],
    rewards=AdvancementRewards(recipes=['minecraft:cinnabar_stairs_from_cinnabar_stonecutting']),
)

CLAY = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_clay_ball': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:clay_ball')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:clay'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_clay_ball']],
    rewards=AdvancementRewards(recipes=['minecraft:clay']),
)

COAL_BLOCK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_coal': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:coal')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:coal_block'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_coal']],
    rewards=AdvancementRewards(recipes=['minecraft:coal_block']),
)

COARSE_DIRT = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gravel': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gravel')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:coarse_dirt'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_gravel']],
    rewards=AdvancementRewards(recipes=['minecraft:coarse_dirt']),
)

COBBLED_DEEPSLATE_FROM_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cobbled_deepslate_from_deepslate_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:cobbled_deepslate_from_deepslate_stonecutting']),
)

COBBLED_DEEPSLATE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cobbled_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cobbled_deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cobbled_deepslate_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cobbled_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:cobbled_deepslate_slab']),
)

COBBLED_DEEPSLATE_SLAB_FROM_COBBLED_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cobbled_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cobbled_deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cobbled_deepslate_slab_from_cobbled_deepslate_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cobbled_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:cobbled_deepslate_slab_from_cobbled_deepslate_stonecutting']),
)

COBBLED_DEEPSLATE_SLAB_FROM_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cobbled_deepslate_slab_from_deepslate_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:cobbled_deepslate_slab_from_deepslate_stonecutting']),
)

COBBLED_DEEPSLATE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cobbled_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cobbled_deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cobbled_deepslate_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cobbled_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:cobbled_deepslate_stairs']),
)

COBBLED_DEEPSLATE_STAIRS_FROM_COBBLED_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cobbled_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cobbled_deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:cobbled_deepslate_stairs_from_cobbled_deepslate_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cobbled_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:cobbled_deepslate_stairs_from_cobbled_deepslate_stonecutting']),
)

COBBLED_DEEPSLATE_STAIRS_FROM_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cobbled_deepslate_stairs_from_deepslate_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:cobbled_deepslate_stairs_from_deepslate_stonecutting']),
)

COBBLESTONE_FROM_STONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cobblestone_from_stone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stone']],
    rewards=AdvancementRewards(recipes=['minecraft:cobblestone_from_stone_stonecutting']),
)

COBBLESTONE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cobblestone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cobblestone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cobblestone_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cobblestone']],
    rewards=AdvancementRewards(recipes=['minecraft:cobblestone_slab']),
)

COBBLESTONE_SLAB_FROM_COBBLESTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cobblestone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cobblestone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cobblestone_slab_from_cobblestone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cobblestone']],
    rewards=AdvancementRewards(recipes=['minecraft:cobblestone_slab_from_cobblestone_stonecutting']),
)

COBBLESTONE_SLAB_FROM_STONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cobblestone_slab_from_stone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stone']],
    rewards=AdvancementRewards(recipes=['minecraft:cobblestone_slab_from_stone_stonecutting']),
)

COBBLESTONE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cobblestone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cobblestone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cobblestone_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cobblestone']],
    rewards=AdvancementRewards(recipes=['minecraft:cobblestone_stairs']),
)

COBBLESTONE_STAIRS_FROM_COBBLESTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cobblestone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cobblestone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cobblestone_stairs_from_cobblestone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cobblestone']],
    rewards=AdvancementRewards(recipes=['minecraft:cobblestone_stairs_from_cobblestone_stonecutting']),
)

COBBLESTONE_STAIRS_FROM_STONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cobblestone_stairs_from_stone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stone']],
    rewards=AdvancementRewards(recipes=['minecraft:cobblestone_stairs_from_stone_stonecutting']),
)

COPPER_BLOCK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:copper_block'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:copper_block']),
)

COPPER_GRATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:copper_grate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_block']],
    rewards=AdvancementRewards(recipes=['minecraft:copper_grate']),
)

COPPER_GRATE_FROM_COPPER_BLOCK_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:copper_grate_from_copper_block_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_block']],
    rewards=AdvancementRewards(recipes=['minecraft:copper_grate_from_copper_block_stonecutting']),
)

CRACKED_DEEPSLATE_BRICKS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cracked_deepslate_bricks'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:cracked_deepslate_bricks']),
)

CRACKED_DEEPSLATE_TILES = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate_tiles': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate_tiles')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cracked_deepslate_tiles'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate_tiles']],
    rewards=AdvancementRewards(recipes=['minecraft:cracked_deepslate_tiles']),
)

CRACKED_NETHER_BRICKS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_nether_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:nether_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cracked_nether_bricks'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_nether_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:cracked_nether_bricks']),
)

CRACKED_POLISHED_BLACKSTONE_BRICKS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_blackstone_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_blackstone_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cracked_polished_blackstone_bricks'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_blackstone_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:cracked_polished_blackstone_bricks']),
)

CRACKED_STONE_BRICKS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stone_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stone_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cracked_stone_bricks'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stone_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:cracked_stone_bricks']),
)

CRIMSON_HYPHAE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:crimson_stem')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:crimson_hyphae'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_log']],
    rewards=AdvancementRewards(recipes=['minecraft:crimson_hyphae']),
)

CRIMSON_PLANKS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_logs': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:crimson_stems')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:crimson_planks'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_logs']],
    rewards=AdvancementRewards(recipes=['minecraft:crimson_planks']),
)

CRIMSON_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:crimson_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:crimson_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:crimson_slab']),
)

CRIMSON_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:crimson_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:crimson_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:crimson_stairs']),
)

CUT_COPPER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cut_copper'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_block']],
    rewards=AdvancementRewards(recipes=['minecraft:cut_copper']),
)

CUT_COPPER_FROM_COPPER_BLOCK_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cut_copper_from_copper_block_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_block']],
    rewards=AdvancementRewards(recipes=['minecraft:cut_copper_from_copper_block_stonecutting']),
)

CUT_COPPER_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cut_copper_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:cut_copper_slab']),
)

CUT_COPPER_SLAB_FROM_COPPER_BLOCK_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cut_copper_slab_from_copper_block_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_block']],
    rewards=AdvancementRewards(recipes=['minecraft:cut_copper_slab_from_copper_block_stonecutting']),
)

CUT_COPPER_SLAB_FROM_CUT_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cut_copper_slab_from_cut_copper_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:cut_copper_slab_from_cut_copper_stonecutting']),
)

CUT_COPPER_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cut_copper_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:cut_copper_stairs']),
)

CUT_COPPER_STAIRS_FROM_COPPER_BLOCK_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cut_copper_stairs_from_copper_block_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_block']],
    rewards=AdvancementRewards(recipes=['minecraft:cut_copper_stairs_from_copper_block_stonecutting']),
)

CUT_COPPER_STAIRS_FROM_CUT_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cut_copper_stairs_from_cut_copper_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:cut_copper_stairs_from_cut_copper_stonecutting']),
)

CUT_RED_SANDSTONE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_red_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cut_red_sandstone'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_red_sandstone']],
    rewards=AdvancementRewards(recipes=['minecraft:cut_red_sandstone']),
)

CUT_RED_SANDSTONE_FROM_RED_SANDSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_red_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cut_red_sandstone_from_red_sandstone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_red_sandstone']],
    rewards=AdvancementRewards(recipes=['minecraft:cut_red_sandstone_from_red_sandstone_stonecutting']),
)

CUT_RED_SANDSTONE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cut_red_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cut_red_sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cut_red_sandstone_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cut_red_sandstone']],
    rewards=AdvancementRewards(recipes=['minecraft:cut_red_sandstone_slab']),
)

CUT_RED_SANDSTONE_SLAB_FROM_CUT_RED_SANDSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cut_red_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cut_red_sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cut_red_sandstone_slab_from_cut_red_sandstone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cut_red_sandstone']],
    rewards=AdvancementRewards(recipes=['minecraft:cut_red_sandstone_slab_from_cut_red_sandstone_stonecutting']),
)

CUT_RED_SANDSTONE_SLAB_FROM_RED_SANDSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_red_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cut_red_sandstone_slab_from_red_sandstone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_red_sandstone']],
    rewards=AdvancementRewards(recipes=['minecraft:cut_red_sandstone_slab_from_red_sandstone_stonecutting']),
)

CUT_SANDSTONE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cut_sandstone'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sandstone']],
    rewards=AdvancementRewards(recipes=['minecraft:cut_sandstone']),
)

CUT_SANDSTONE_FROM_SANDSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cut_sandstone_from_sandstone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sandstone']],
    rewards=AdvancementRewards(recipes=['minecraft:cut_sandstone_from_sandstone_stonecutting']),
)

CUT_SANDSTONE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cut_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cut_sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cut_sandstone_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cut_sandstone']],
    rewards=AdvancementRewards(recipes=['minecraft:cut_sandstone_slab']),
)

CUT_SANDSTONE_SLAB_FROM_CUT_SANDSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cut_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cut_sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cut_sandstone_slab_from_cut_sandstone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cut_sandstone']],
    rewards=AdvancementRewards(recipes=['minecraft:cut_sandstone_slab_from_cut_sandstone_stonecutting']),
)

CUT_SANDSTONE_SLAB_FROM_SANDSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cut_sandstone_slab_from_sandstone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sandstone']],
    rewards=AdvancementRewards(recipes=['minecraft:cut_sandstone_slab_from_sandstone_stonecutting']),
)

CYAN_CONCRETE_POWDER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gravel': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gravel')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_sand': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sand')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cyan_concrete_powder'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sand', 'has_gravel']],
    rewards=AdvancementRewards(recipes=['minecraft:cyan_concrete_powder']),
)

CYAN_CONCRETE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cyan_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cyan_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cyan_concrete_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cyan_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:cyan_concrete_slab']),
)

CYAN_CONCRETE_SLAB_FROM_CYAN_CONCRETE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cyan_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cyan_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cyan_concrete_slab_from_cyan_concrete_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cyan_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:cyan_concrete_slab_from_cyan_concrete_stonecutting']),
)

CYAN_CONCRETE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cyan_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cyan_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cyan_concrete_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cyan_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:cyan_concrete_stairs']),
)

CYAN_CONCRETE_STAIRS_FROM_CYAN_CONCRETE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cyan_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cyan_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cyan_concrete_stairs_from_cyan_concrete_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cyan_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:cyan_concrete_stairs_from_cyan_concrete_stonecutting']),
)

CYAN_STAINED_GLASS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glass')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cyan_stained_glass'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass']],
    rewards=AdvancementRewards(recipes=['minecraft:cyan_stained_glass']),
)

CYAN_TERRACOTTA = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_terracotta': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:terracotta')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cyan_terracotta'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_terracotta']],
    rewards=AdvancementRewards(recipes=['minecraft:cyan_terracotta']),
)

CYAN_WOOL_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cyan_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cyan_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cyan_wool_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cyan_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:cyan_wool_slab']),
)

CYAN_WOOL_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cyan_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cyan_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cyan_wool_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cyan_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:cyan_wool_stairs']),
)

DARK_OAK_PLANKS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:dark_oak_logs')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dark_oak_planks'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_log']],
    rewards=AdvancementRewards(recipes=['minecraft:dark_oak_planks']),
)

DARK_OAK_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dark_oak_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dark_oak_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:dark_oak_slab']),
)

DARK_OAK_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dark_oak_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dark_oak_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:dark_oak_stairs']),
)

DARK_OAK_WOOD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dark_oak_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dark_oak_wood'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_log']],
    rewards=AdvancementRewards(recipes=['minecraft:dark_oak_wood']),
)

DARK_PRISMARINE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_prismarine_shard': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:prismarine_shard')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dark_prismarine'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_prismarine_shard']],
    rewards=AdvancementRewards(recipes=['minecraft:dark_prismarine']),
)

DARK_PRISMARINE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_dark_prismarine': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dark_prismarine')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dark_prismarine_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_dark_prismarine']],
    rewards=AdvancementRewards(recipes=['minecraft:dark_prismarine_slab']),
)

DARK_PRISMARINE_SLAB_FROM_DARK_PRISMARINE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_dark_prismarine': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dark_prismarine')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dark_prismarine_slab_from_dark_prismarine_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_dark_prismarine']],
    rewards=AdvancementRewards(recipes=['minecraft:dark_prismarine_slab_from_dark_prismarine_stonecutting']),
)

DARK_PRISMARINE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_dark_prismarine': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dark_prismarine')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dark_prismarine_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_dark_prismarine']],
    rewards=AdvancementRewards(recipes=['minecraft:dark_prismarine_stairs']),
)

DARK_PRISMARINE_STAIRS_FROM_DARK_PRISMARINE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_dark_prismarine': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dark_prismarine')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dark_prismarine_stairs_from_dark_prismarine_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_dark_prismarine']],
    rewards=AdvancementRewards(recipes=['minecraft:dark_prismarine_stairs_from_dark_prismarine_stonecutting']),
)

DEEPSLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cobbled_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cobbled_deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cobbled_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate']),
)

DEEPSLATE_BRICKS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_bricks'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_bricks']),
)

DEEPSLATE_BRICKS_FROM_COBBLED_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cobbled_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cobbled_deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_bricks_from_cobbled_deepslate_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cobbled_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_bricks_from_cobbled_deepslate_stonecutting']),
)

DEEPSLATE_BRICKS_FROM_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_bricks_from_deepslate_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_bricks_from_deepslate_stonecutting']),
)

DEEPSLATE_BRICKS_FROM_POLISHED_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_bricks_from_polished_deepslate_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_bricks_from_polished_deepslate_stonecutting']),
)

DEEPSLATE_BRICK_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_brick_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_brick_slab']),
)

DEEPSLATE_BRICK_SLAB_FROM_COBBLED_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cobbled_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cobbled_deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_brick_slab_from_cobbled_deepslate_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cobbled_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_brick_slab_from_cobbled_deepslate_stonecutting']),
)

DEEPSLATE_BRICK_SLAB_FROM_DEEPSLATE_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_brick_slab_from_deepslate_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_brick_slab_from_deepslate_bricks_stonecutting']),
)

DEEPSLATE_BRICK_SLAB_FROM_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_brick_slab_from_deepslate_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_brick_slab_from_deepslate_stonecutting']),
)

DEEPSLATE_BRICK_SLAB_FROM_POLISHED_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_brick_slab_from_polished_deepslate_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_brick_slab_from_polished_deepslate_stonecutting']),
)

DEEPSLATE_BRICK_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_brick_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_brick_stairs']),
)

DEEPSLATE_BRICK_STAIRS_FROM_COBBLED_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cobbled_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cobbled_deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_brick_stairs_from_cobbled_deepslate_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cobbled_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_brick_stairs_from_cobbled_deepslate_stonecutting']),
)

DEEPSLATE_BRICK_STAIRS_FROM_DEEPSLATE_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_brick_stairs_from_deepslate_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_brick_stairs_from_deepslate_bricks_stonecutting']),
)

DEEPSLATE_BRICK_STAIRS_FROM_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_brick_stairs_from_deepslate_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_brick_stairs_from_deepslate_stonecutting']),
)

DEEPSLATE_BRICK_STAIRS_FROM_POLISHED_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:deepslate_brick_stairs_from_polished_deepslate_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_brick_stairs_from_polished_deepslate_stonecutting']),
)

DEEPSLATE_TILES = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_tiles'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_tiles']),
)

DEEPSLATE_TILES_FROM_COBBLED_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cobbled_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cobbled_deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_tiles_from_cobbled_deepslate_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cobbled_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_tiles_from_cobbled_deepslate_stonecutting']),
)

DEEPSLATE_TILES_FROM_DEEPSLATE_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_tiles_from_deepslate_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_tiles_from_deepslate_bricks_stonecutting']),
)

DEEPSLATE_TILES_FROM_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_tiles_from_deepslate_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_tiles_from_deepslate_stonecutting']),
)

DEEPSLATE_TILES_FROM_POLISHED_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_tiles_from_polished_deepslate_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_tiles_from_polished_deepslate_stonecutting']),
)

DEEPSLATE_TILE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate_tiles': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate_tiles')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_tile_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate_tiles']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_tile_slab']),
)

DEEPSLATE_TILE_SLAB_FROM_COBBLED_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cobbled_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cobbled_deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_tile_slab_from_cobbled_deepslate_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cobbled_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_tile_slab_from_cobbled_deepslate_stonecutting']),
)

DEEPSLATE_TILE_SLAB_FROM_DEEPSLATE_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_tile_slab_from_deepslate_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_tile_slab_from_deepslate_bricks_stonecutting']),
)

DEEPSLATE_TILE_SLAB_FROM_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_tile_slab_from_deepslate_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_tile_slab_from_deepslate_stonecutting']),
)

DEEPSLATE_TILE_SLAB_FROM_DEEPSLATE_TILES_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate_tiles': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate_tiles')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_tile_slab_from_deepslate_tiles_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate_tiles']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_tile_slab_from_deepslate_tiles_stonecutting']),
)

DEEPSLATE_TILE_SLAB_FROM_POLISHED_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_tile_slab_from_polished_deepslate_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_tile_slab_from_polished_deepslate_stonecutting']),
)

DEEPSLATE_TILE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate_tiles': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate_tiles')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_tile_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate_tiles']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_tile_stairs']),
)

DEEPSLATE_TILE_STAIRS_FROM_COBBLED_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cobbled_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cobbled_deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_tile_stairs_from_cobbled_deepslate_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cobbled_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_tile_stairs_from_cobbled_deepslate_stonecutting']),
)

DEEPSLATE_TILE_STAIRS_FROM_DEEPSLATE_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_tile_stairs_from_deepslate_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_tile_stairs_from_deepslate_bricks_stonecutting']),
)

DEEPSLATE_TILE_STAIRS_FROM_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_tile_stairs_from_deepslate_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_tile_stairs_from_deepslate_stonecutting']),
)

DEEPSLATE_TILE_STAIRS_FROM_DEEPSLATE_TILES_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate_tiles': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate_tiles')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_tile_stairs_from_deepslate_tiles_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate_tiles']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_tile_stairs_from_deepslate_tiles_stonecutting']),
)

DEEPSLATE_TILE_STAIRS_FROM_POLISHED_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_tile_stairs_from_polished_deepslate_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_tile_stairs_from_polished_deepslate_stonecutting']),
)

DIAMOND_BLOCK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_diamond': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:diamond')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:diamond_block'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_diamond']],
    rewards=AdvancementRewards(recipes=['minecraft:diamond_block']),
)

DIORITE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_quartz': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:quartz')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:diorite'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_quartz']],
    rewards=AdvancementRewards(recipes=['minecraft:diorite']),
)

DIORITE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_diorite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:diorite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:diorite_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_diorite']],
    rewards=AdvancementRewards(recipes=['minecraft:diorite_slab']),
)

DIORITE_SLAB_FROM_DIORITE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_diorite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:diorite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:diorite_slab_from_diorite_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_diorite']],
    rewards=AdvancementRewards(recipes=['minecraft:diorite_slab_from_diorite_stonecutting']),
)

DIORITE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_diorite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:diorite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:diorite_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_diorite']],
    rewards=AdvancementRewards(recipes=['minecraft:diorite_stairs']),
)

DIORITE_STAIRS_FROM_DIORITE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_diorite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:diorite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:diorite_stairs_from_diorite_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_diorite']],
    rewards=AdvancementRewards(recipes=['minecraft:diorite_stairs_from_diorite_stonecutting']),
)

DRIED_GHAST = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_ghast_tear': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:ghast_tear')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dried_ghast'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_ghast_tear']],
    rewards=AdvancementRewards(recipes=['minecraft:dried_ghast']),
)

DRIED_KELP_BLOCK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_dried_kelp': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dried_kelp')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dried_kelp_block'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_dried_kelp']],
    rewards=AdvancementRewards(recipes=['minecraft:dried_kelp_block']),
)

DRIPSTONE_BLOCK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_pointed_dripstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pointed_dripstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dripstone_block'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_pointed_dripstone']],
    rewards=AdvancementRewards(recipes=['minecraft:dripstone_block']),
)

DYE_BLACK_WOOL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:black_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_black_wool'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_black_wool']),
)

DYE_BLACK_WOOL_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:black_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_black_wool_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_black_wool_slab']),
)

DYE_BLACK_WOOL_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:black_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_black_wool_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_black_wool_stairs']),
)

DYE_BLUE_WOOL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blue_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_blue_wool'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_blue_wool']),
)

DYE_BLUE_WOOL_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blue_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_blue_wool_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_blue_wool_slab']),
)

DYE_BLUE_WOOL_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blue_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_blue_wool_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_blue_wool_stairs']),
)

DYE_BROWN_WOOL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:brown_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_brown_wool'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_brown_wool']),
)

DYE_BROWN_WOOL_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:brown_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_brown_wool_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_brown_wool_slab']),
)

DYE_BROWN_WOOL_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:brown_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_brown_wool_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_brown_wool_stairs']),
)

DYE_CYAN_WOOL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cyan_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_cyan_wool'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_cyan_wool']),
)

DYE_CYAN_WOOL_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cyan_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_cyan_wool_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_cyan_wool_slab']),
)

DYE_CYAN_WOOL_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cyan_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_cyan_wool_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_cyan_wool_stairs']),
)

DYE_GRAY_WOOL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gray_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_gray_wool'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_gray_wool']),
)

DYE_GRAY_WOOL_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gray_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_gray_wool_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_gray_wool_slab']),
)

DYE_GRAY_WOOL_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gray_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_gray_wool_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_gray_wool_stairs']),
)

DYE_GREEN_WOOL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:green_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_green_wool'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_green_wool']),
)

DYE_GREEN_WOOL_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:green_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_green_wool_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_green_wool_slab']),
)

DYE_GREEN_WOOL_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:green_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_green_wool_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_green_wool_stairs']),
)

DYE_LIGHT_BLUE_WOOL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_blue_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_light_blue_wool'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_light_blue_wool']),
)

DYE_LIGHT_BLUE_WOOL_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_blue_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_light_blue_wool_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_light_blue_wool_slab']),
)

DYE_LIGHT_BLUE_WOOL_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_blue_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_light_blue_wool_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_light_blue_wool_stairs']),
)

DYE_LIGHT_GRAY_WOOL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_gray_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_light_gray_wool'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_light_gray_wool']),
)

DYE_LIGHT_GRAY_WOOL_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_gray_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_light_gray_wool_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_light_gray_wool_slab']),
)

DYE_LIGHT_GRAY_WOOL_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_gray_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_light_gray_wool_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_light_gray_wool_stairs']),
)

DYE_LIME_WOOL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:lime_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_lime_wool'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_lime_wool']),
)

DYE_LIME_WOOL_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:lime_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_lime_wool_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_lime_wool_slab']),
)

DYE_LIME_WOOL_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:lime_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_lime_wool_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_lime_wool_stairs']),
)

DYE_MAGENTA_WOOL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:magenta_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_magenta_wool'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_magenta_wool']),
)

DYE_MAGENTA_WOOL_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:magenta_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_magenta_wool_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_magenta_wool_slab']),
)

DYE_MAGENTA_WOOL_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:magenta_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_magenta_wool_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_magenta_wool_stairs']),
)

DYE_ORANGE_WOOL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:orange_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_orange_wool'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_orange_wool']),
)

DYE_ORANGE_WOOL_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:orange_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_orange_wool_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_orange_wool_slab']),
)

DYE_ORANGE_WOOL_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:orange_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_orange_wool_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_orange_wool_stairs']),
)

DYE_PINK_WOOL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pink_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_pink_wool'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_pink_wool']),
)

DYE_PINK_WOOL_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pink_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_pink_wool_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_pink_wool_slab']),
)

DYE_PINK_WOOL_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pink_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_pink_wool_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_pink_wool_stairs']),
)

DYE_PURPLE_WOOL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:purple_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_purple_wool'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_purple_wool']),
)

DYE_PURPLE_WOOL_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:purple_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_purple_wool_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_purple_wool_slab']),
)

DYE_PURPLE_WOOL_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:purple_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_purple_wool_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_purple_wool_stairs']),
)

DYE_RED_WOOL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_red_wool'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_red_wool']),
)

DYE_RED_WOOL_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_red_wool_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_red_wool_slab']),
)

DYE_RED_WOOL_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_red_wool_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_red_wool_stairs']),
)

DYE_WHITE_WOOL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:white_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_white_wool'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_white_wool']),
)

DYE_WHITE_WOOL_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:white_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_white_wool_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_white_wool_slab']),
)

DYE_WHITE_WOOL_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:white_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_white_wool_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_white_wool_stairs']),
)

DYE_YELLOW_WOOL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:yellow_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_yellow_wool'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_yellow_wool']),
)

DYE_YELLOW_WOOL_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:yellow_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_yellow_wool_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_yellow_wool_slab']),
)

DYE_YELLOW_WOOL_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:yellow_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_yellow_wool_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_yellow_wool_stairs']),
)

EMERALD_BLOCK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_emerald': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:emerald')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:emerald_block'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_emerald']],
    rewards=AdvancementRewards(recipes=['minecraft:emerald_block']),
)

END_STONE_BRICKS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_end_stone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:end_stone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:end_stone_bricks'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_end_stone']],
    rewards=AdvancementRewards(recipes=['minecraft:end_stone_bricks']),
)

END_STONE_BRICKS_FROM_END_STONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_end_stone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:end_stone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:end_stone_bricks_from_end_stone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_end_stone']],
    rewards=AdvancementRewards(recipes=['minecraft:end_stone_bricks_from_end_stone_stonecutting']),
)

END_STONE_BRICK_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_end_stone_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:end_stone_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:end_stone_brick_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_end_stone_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:end_stone_brick_slab']),
)

END_STONE_BRICK_SLAB_FROM_END_STONE_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_end_stone_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:end_stone_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:end_stone_brick_slab_from_end_stone_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_end_stone_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:end_stone_brick_slab_from_end_stone_bricks_stonecutting']),
)

END_STONE_BRICK_SLAB_FROM_END_STONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_end_stone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:end_stone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:end_stone_brick_slab_from_end_stone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_end_stone']],
    rewards=AdvancementRewards(recipes=['minecraft:end_stone_brick_slab_from_end_stone_stonecutting']),
)

END_STONE_BRICK_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_end_stone_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:end_stone_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:end_stone_brick_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_end_stone_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:end_stone_brick_stairs']),
)

END_STONE_BRICK_STAIRS_FROM_END_STONE_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_end_stone_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:end_stone_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:end_stone_brick_stairs_from_end_stone_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_end_stone_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:end_stone_brick_stairs_from_end_stone_bricks_stonecutting']),
)

END_STONE_BRICK_STAIRS_FROM_END_STONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_end_stone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:end_stone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:end_stone_brick_stairs_from_end_stone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_end_stone']],
    rewards=AdvancementRewards(recipes=['minecraft:end_stone_brick_stairs_from_end_stone_stonecutting']),
)

EXPOSED_CHISELED_COPPER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:exposed_cut_copper_slab')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:exposed_chiseled_copper'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:exposed_chiseled_copper']),
)

EXPOSED_CHISELED_COPPER_FROM_EXPOSED_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_exposed_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:exposed_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:exposed_chiseled_copper_from_exposed_copper_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_exposed_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:exposed_chiseled_copper_from_exposed_copper_stonecutting']),
)

EXPOSED_CHISELED_COPPER_FROM_EXPOSED_CUT_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_exposed_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:exposed_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:exposed_chiseled_copper_from_exposed_cut_copper_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_exposed_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:exposed_chiseled_copper_from_exposed_cut_copper_stonecutting']),
)

EXPOSED_COPPER_GRATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_exposed_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:exposed_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:exposed_copper_grate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_exposed_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:exposed_copper_grate']),
)

EXPOSED_COPPER_GRATE_FROM_EXPOSED_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_exposed_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:exposed_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:exposed_copper_grate_from_exposed_copper_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_exposed_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:exposed_copper_grate_from_exposed_copper_stonecutting']),
)

EXPOSED_CUT_COPPER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_exposed_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:exposed_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:exposed_cut_copper'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_exposed_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:exposed_cut_copper']),
)

EXPOSED_CUT_COPPER_FROM_EXPOSED_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_exposed_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:exposed_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:exposed_cut_copper_from_exposed_copper_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_exposed_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:exposed_cut_copper_from_exposed_copper_stonecutting']),
)

EXPOSED_CUT_COPPER_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_exposed_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:exposed_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:exposed_cut_copper_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_exposed_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:exposed_cut_copper_slab']),
)

EXPOSED_CUT_COPPER_SLAB_FROM_EXPOSED_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_exposed_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:exposed_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:exposed_cut_copper_slab_from_exposed_copper_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_exposed_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:exposed_cut_copper_slab_from_exposed_copper_stonecutting']),
)

EXPOSED_CUT_COPPER_SLAB_FROM_EXPOSED_CUT_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_exposed_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:exposed_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:exposed_cut_copper_slab_from_exposed_cut_copper_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_exposed_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:exposed_cut_copper_slab_from_exposed_cut_copper_stonecutting']),
)

EXPOSED_CUT_COPPER_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_exposed_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:exposed_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:exposed_cut_copper_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_exposed_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:exposed_cut_copper_stairs']),
)

EXPOSED_CUT_COPPER_STAIRS_FROM_EXPOSED_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_exposed_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:exposed_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:exposed_cut_copper_stairs_from_exposed_copper_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_exposed_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:exposed_cut_copper_stairs_from_exposed_copper_stonecutting']),
)

EXPOSED_CUT_COPPER_STAIRS_FROM_EXPOSED_CUT_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_exposed_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:exposed_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:exposed_cut_copper_stairs_from_exposed_cut_copper_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_exposed_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:exposed_cut_copper_stairs_from_exposed_cut_copper_stonecutting']),
)

GLASS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_smelts_to_glass': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:smelts_to_glass')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:glass'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_smelts_to_glass']],
    rewards=AdvancementRewards(recipes=['minecraft:glass']),
)

GLOWSTONE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glowstone_dust': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glowstone_dust')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:glowstone'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glowstone_dust']],
    rewards=AdvancementRewards(recipes=['minecraft:glowstone']),
)

GOLD_BLOCK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gold_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gold_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:gold_block'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_gold_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:gold_block']),
)

GRANITE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_quartz': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:quartz')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:granite'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_quartz']],
    rewards=AdvancementRewards(recipes=['minecraft:granite']),
)

GRANITE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_granite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:granite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:granite_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_granite']],
    rewards=AdvancementRewards(recipes=['minecraft:granite_slab']),
)

GRANITE_SLAB_FROM_GRANITE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_granite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:granite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:granite_slab_from_granite_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_granite']],
    rewards=AdvancementRewards(recipes=['minecraft:granite_slab_from_granite_stonecutting']),
)

GRANITE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_granite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:granite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:granite_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_granite']],
    rewards=AdvancementRewards(recipes=['minecraft:granite_stairs']),
)

GRANITE_STAIRS_FROM_GRANITE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_granite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:granite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:granite_stairs_from_granite_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_granite']],
    rewards=AdvancementRewards(recipes=['minecraft:granite_stairs_from_granite_stonecutting']),
)

GRAY_CONCRETE_POWDER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gravel': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gravel')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_sand': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sand')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:gray_concrete_powder'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sand', 'has_gravel']],
    rewards=AdvancementRewards(recipes=['minecraft:gray_concrete_powder']),
)

GRAY_CONCRETE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gray_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gray_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:gray_concrete_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_gray_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:gray_concrete_slab']),
)

GRAY_CONCRETE_SLAB_FROM_GRAY_CONCRETE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gray_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gray_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:gray_concrete_slab_from_gray_concrete_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_gray_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:gray_concrete_slab_from_gray_concrete_stonecutting']),
)

GRAY_CONCRETE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gray_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gray_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:gray_concrete_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_gray_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:gray_concrete_stairs']),
)

GRAY_CONCRETE_STAIRS_FROM_GRAY_CONCRETE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gray_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gray_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:gray_concrete_stairs_from_gray_concrete_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_gray_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:gray_concrete_stairs_from_gray_concrete_stonecutting']),
)

GRAY_STAINED_GLASS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glass')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:gray_stained_glass'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass']],
    rewards=AdvancementRewards(recipes=['minecraft:gray_stained_glass']),
)

GRAY_TERRACOTTA = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_terracotta': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:terracotta')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:gray_terracotta'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_terracotta']],
    rewards=AdvancementRewards(recipes=['minecraft:gray_terracotta']),
)

GRAY_WOOL_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gray_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gray_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:gray_wool_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_gray_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:gray_wool_slab']),
)

GRAY_WOOL_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gray_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gray_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:gray_wool_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_gray_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:gray_wool_stairs']),
)

GREEN_CONCRETE_POWDER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gravel': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gravel')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_sand': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sand')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:green_concrete_powder'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sand', 'has_gravel']],
    rewards=AdvancementRewards(recipes=['minecraft:green_concrete_powder']),
)

GREEN_CONCRETE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_green_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:green_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:green_concrete_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_green_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:green_concrete_slab']),
)

GREEN_CONCRETE_SLAB_FROM_GREEN_CONCRETE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_green_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:green_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:green_concrete_slab_from_green_concrete_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_green_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:green_concrete_slab_from_green_concrete_stonecutting']),
)

GREEN_CONCRETE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_green_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:green_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:green_concrete_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_green_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:green_concrete_stairs']),
)

GREEN_CONCRETE_STAIRS_FROM_GREEN_CONCRETE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_green_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:green_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:green_concrete_stairs_from_green_concrete_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_green_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:green_concrete_stairs_from_green_concrete_stonecutting']),
)

GREEN_STAINED_GLASS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glass')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:green_stained_glass'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass']],
    rewards=AdvancementRewards(recipes=['minecraft:green_stained_glass']),
)

GREEN_TERRACOTTA = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_terracotta': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:terracotta')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:green_terracotta'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_terracotta']],
    rewards=AdvancementRewards(recipes=['minecraft:green_terracotta']),
)

GREEN_WOOL_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_green_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:green_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:green_wool_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_green_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:green_wool_slab']),
)

GREEN_WOOL_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_green_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:green_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:green_wool_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_green_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:green_wool_stairs']),
)

HAY_BLOCK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:hay_block'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_wheat': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:wheat')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_wheat']],
    rewards=AdvancementRewards(recipes=['minecraft:hay_block']),
)

IRON_BLOCK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_iron_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:iron_block'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_iron_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:iron_block']),
)

JACK_O_LANTERN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_carved_pumpkin': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:carved_pumpkin')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:jack_o_lantern'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_carved_pumpkin']],
    rewards=AdvancementRewards(recipes=['minecraft:jack_o_lantern']),
)

JUNGLE_PLANKS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_logs': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:jungle_logs')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:jungle_planks'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_logs']],
    rewards=AdvancementRewards(recipes=['minecraft:jungle_planks']),
)

JUNGLE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:jungle_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:jungle_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:jungle_slab']),
)

JUNGLE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:jungle_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:jungle_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:jungle_stairs']),
)

JUNGLE_WOOD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:jungle_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:jungle_wood'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_log']],
    rewards=AdvancementRewards(recipes=['minecraft:jungle_wood']),
)

LAPIS_BLOCK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_lapis_lazuli': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:lapis_lazuli')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:lapis_block'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_lapis_lazuli']],
    rewards=AdvancementRewards(recipes=['minecraft:lapis_block']),
)

LIGHT_BLUE_CONCRETE_POWDER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gravel': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gravel')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_sand': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sand')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_blue_concrete_powder'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sand', 'has_gravel']],
    rewards=AdvancementRewards(recipes=['minecraft:light_blue_concrete_powder']),
)

LIGHT_BLUE_CONCRETE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_light_blue_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_blue_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_blue_concrete_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_light_blue_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:light_blue_concrete_slab']),
)

LIGHT_BLUE_CONCRETE_SLAB_FROM_LIGHT_BLUE_CONCRETE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_light_blue_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_blue_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:light_blue_concrete_slab_from_light_blue_concrete_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_light_blue_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:light_blue_concrete_slab_from_light_blue_concrete_stonecutting']),
)

LIGHT_BLUE_CONCRETE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_light_blue_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_blue_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_blue_concrete_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_light_blue_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:light_blue_concrete_stairs']),
)

LIGHT_BLUE_CONCRETE_STAIRS_FROM_LIGHT_BLUE_CONCRETE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_light_blue_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_blue_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:light_blue_concrete_stairs_from_light_blue_concrete_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_light_blue_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:light_blue_concrete_stairs_from_light_blue_concrete_stonecutting']),
)

LIGHT_BLUE_STAINED_GLASS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glass')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_blue_stained_glass'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass']],
    rewards=AdvancementRewards(recipes=['minecraft:light_blue_stained_glass']),
)

LIGHT_BLUE_TERRACOTTA = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_terracotta': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:terracotta')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_blue_terracotta'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_terracotta']],
    rewards=AdvancementRewards(recipes=['minecraft:light_blue_terracotta']),
)

LIGHT_BLUE_WOOL_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_light_blue_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_blue_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_blue_wool_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_light_blue_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:light_blue_wool_slab']),
)

LIGHT_BLUE_WOOL_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_light_blue_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_blue_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_blue_wool_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_light_blue_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:light_blue_wool_stairs']),
)

LIGHT_GRAY_CONCRETE_POWDER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gravel': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gravel')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_sand': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sand')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_gray_concrete_powder'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sand', 'has_gravel']],
    rewards=AdvancementRewards(recipes=['minecraft:light_gray_concrete_powder']),
)

LIGHT_GRAY_CONCRETE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_light_gray_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_gray_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_gray_concrete_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_light_gray_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:light_gray_concrete_slab']),
)

LIGHT_GRAY_CONCRETE_SLAB_FROM_LIGHT_GRAY_CONCRETE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_light_gray_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_gray_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:light_gray_concrete_slab_from_light_gray_concrete_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_light_gray_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:light_gray_concrete_slab_from_light_gray_concrete_stonecutting']),
)

LIGHT_GRAY_CONCRETE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_light_gray_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_gray_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_gray_concrete_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_light_gray_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:light_gray_concrete_stairs']),
)

LIGHT_GRAY_CONCRETE_STAIRS_FROM_LIGHT_GRAY_CONCRETE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_light_gray_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_gray_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:light_gray_concrete_stairs_from_light_gray_concrete_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_light_gray_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:light_gray_concrete_stairs_from_light_gray_concrete_stonecutting']),
)

LIGHT_GRAY_STAINED_GLASS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glass')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_gray_stained_glass'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass']],
    rewards=AdvancementRewards(recipes=['minecraft:light_gray_stained_glass']),
)

LIGHT_GRAY_TERRACOTTA = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_terracotta': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:terracotta')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_gray_terracotta'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_terracotta']],
    rewards=AdvancementRewards(recipes=['minecraft:light_gray_terracotta']),
)

LIGHT_GRAY_WOOL_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_light_gray_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_gray_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_gray_wool_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_light_gray_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:light_gray_wool_slab']),
)

LIGHT_GRAY_WOOL_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_light_gray_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_gray_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_gray_wool_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_light_gray_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:light_gray_wool_stairs']),
)

LIME_CONCRETE_POWDER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gravel': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gravel')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_sand': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sand')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:lime_concrete_powder'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sand', 'has_gravel']],
    rewards=AdvancementRewards(recipes=['minecraft:lime_concrete_powder']),
)

LIME_CONCRETE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_lime_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:lime_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:lime_concrete_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_lime_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:lime_concrete_slab']),
)

LIME_CONCRETE_SLAB_FROM_LIME_CONCRETE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_lime_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:lime_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:lime_concrete_slab_from_lime_concrete_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_lime_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:lime_concrete_slab_from_lime_concrete_stonecutting']),
)

LIME_CONCRETE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_lime_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:lime_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:lime_concrete_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_lime_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:lime_concrete_stairs']),
)

LIME_CONCRETE_STAIRS_FROM_LIME_CONCRETE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_lime_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:lime_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:lime_concrete_stairs_from_lime_concrete_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_lime_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:lime_concrete_stairs_from_lime_concrete_stonecutting']),
)

LIME_STAINED_GLASS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glass')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:lime_stained_glass'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass']],
    rewards=AdvancementRewards(recipes=['minecraft:lime_stained_glass']),
)

LIME_TERRACOTTA = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_terracotta': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:terracotta')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:lime_terracotta'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_terracotta']],
    rewards=AdvancementRewards(recipes=['minecraft:lime_terracotta']),
)

LIME_WOOL_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_lime_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:lime_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:lime_wool_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_lime_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:lime_wool_slab']),
)

LIME_WOOL_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_lime_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:lime_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:lime_wool_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_lime_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:lime_wool_stairs']),
)

MAGENTA_CONCRETE_POWDER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gravel': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gravel')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_sand': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sand')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:magenta_concrete_powder'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sand', 'has_gravel']],
    rewards=AdvancementRewards(recipes=['minecraft:magenta_concrete_powder']),
)

MAGENTA_CONCRETE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_magenta_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:magenta_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:magenta_concrete_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_magenta_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:magenta_concrete_slab']),
)

MAGENTA_CONCRETE_SLAB_FROM_MAGENTA_CONCRETE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_magenta_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:magenta_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:magenta_concrete_slab_from_magenta_concrete_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_magenta_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:magenta_concrete_slab_from_magenta_concrete_stonecutting']),
)

MAGENTA_CONCRETE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_magenta_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:magenta_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:magenta_concrete_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_magenta_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:magenta_concrete_stairs']),
)

MAGENTA_CONCRETE_STAIRS_FROM_MAGENTA_CONCRETE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_magenta_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:magenta_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:magenta_concrete_stairs_from_magenta_concrete_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_magenta_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:magenta_concrete_stairs_from_magenta_concrete_stonecutting']),
)

MAGENTA_STAINED_GLASS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glass')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:magenta_stained_glass'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass']],
    rewards=AdvancementRewards(recipes=['minecraft:magenta_stained_glass']),
)

MAGENTA_TERRACOTTA = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_terracotta': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:terracotta')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:magenta_terracotta'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_terracotta']],
    rewards=AdvancementRewards(recipes=['minecraft:magenta_terracotta']),
)

MAGENTA_WOOL_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_magenta_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:magenta_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:magenta_wool_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_magenta_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:magenta_wool_slab']),
)

MAGENTA_WOOL_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_magenta_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:magenta_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:magenta_wool_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_magenta_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:magenta_wool_stairs']),
)

MAGMA_BLOCK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_magma_cream': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:magma_cream')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:magma_block'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_magma_cream']],
    rewards=AdvancementRewards(recipes=['minecraft:magma_block']),
)

MANGROVE_PLANKS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_logs': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:mangrove_logs')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:mangrove_planks'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_logs']],
    rewards=AdvancementRewards(recipes=['minecraft:mangrove_planks']),
)

MANGROVE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:mangrove_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:mangrove_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:mangrove_slab']),
)

MANGROVE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:mangrove_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:mangrove_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:mangrove_stairs']),
)

MANGROVE_WOOD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:mangrove_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:mangrove_wood'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_log']],
    rewards=AdvancementRewards(recipes=['minecraft:mangrove_wood']),
)

MELON = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_melon': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:melon_slice')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:melon'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_melon']],
    rewards=AdvancementRewards(recipes=['minecraft:melon']),
)

MOSSY_COBBLESTONE_FROM_MOSS_BLOCK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_moss_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:moss_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:mossy_cobblestone_from_moss_block'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_moss_block']],
    rewards=AdvancementRewards(recipes=['minecraft:mossy_cobblestone_from_moss_block']),
)

MOSSY_COBBLESTONE_FROM_VINE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:mossy_cobblestone_from_vine'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_vine': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:vine')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_vine']],
    rewards=AdvancementRewards(recipes=['minecraft:mossy_cobblestone_from_vine']),
)

MOSSY_COBBLESTONE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_mossy_cobblestone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:mossy_cobblestone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:mossy_cobblestone_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_mossy_cobblestone']],
    rewards=AdvancementRewards(recipes=['minecraft:mossy_cobblestone_slab']),
)

MOSSY_COBBLESTONE_SLAB_FROM_MOSSY_COBBLESTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_mossy_cobblestone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:mossy_cobblestone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:mossy_cobblestone_slab_from_mossy_cobblestone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_mossy_cobblestone']],
    rewards=AdvancementRewards(recipes=['minecraft:mossy_cobblestone_slab_from_mossy_cobblestone_stonecutting']),
)

MOSSY_COBBLESTONE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_mossy_cobblestone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:mossy_cobblestone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:mossy_cobblestone_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_mossy_cobblestone']],
    rewards=AdvancementRewards(recipes=['minecraft:mossy_cobblestone_stairs']),
)

MOSSY_COBBLESTONE_STAIRS_FROM_MOSSY_COBBLESTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_mossy_cobblestone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:mossy_cobblestone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:mossy_cobblestone_stairs_from_mossy_cobblestone_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_mossy_cobblestone']],
    rewards=AdvancementRewards(recipes=['minecraft:mossy_cobblestone_stairs_from_mossy_cobblestone_stonecutting']),
)

MOSSY_STONE_BRICKS_FROM_MOSS_BLOCK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_moss_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:moss_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:mossy_stone_bricks_from_moss_block'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_moss_block']],
    rewards=AdvancementRewards(recipes=['minecraft:mossy_stone_bricks_from_moss_block']),
)

MOSSY_STONE_BRICKS_FROM_VINE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:mossy_stone_bricks_from_vine'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_vine': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:vine')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_vine']],
    rewards=AdvancementRewards(recipes=['minecraft:mossy_stone_bricks_from_vine']),
)

MOSSY_STONE_BRICK_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_mossy_stone_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:mossy_stone_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:mossy_stone_brick_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_mossy_stone_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:mossy_stone_brick_slab']),
)

MOSSY_STONE_BRICK_SLAB_FROM_MOSSY_STONE_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_mossy_stone_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:mossy_stone_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:mossy_stone_brick_slab_from_mossy_stone_bricks_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_mossy_stone_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:mossy_stone_brick_slab_from_mossy_stone_bricks_stonecutting']),
)

MOSSY_STONE_BRICK_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_mossy_stone_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:mossy_stone_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:mossy_stone_brick_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_mossy_stone_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:mossy_stone_brick_stairs']),
)

MOSSY_STONE_BRICK_STAIRS_FROM_MOSSY_STONE_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_mossy_stone_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:mossy_stone_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:mossy_stone_brick_stairs_from_mossy_stone_bricks_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_mossy_stone_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:mossy_stone_brick_stairs_from_mossy_stone_bricks_stonecutting']),
)

MUDDY_MANGROVE_ROOTS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_mangrove_roots': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:mangrove_roots')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:muddy_mangrove_roots'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_mangrove_roots']],
    rewards=AdvancementRewards(recipes=['minecraft:muddy_mangrove_roots']),
)

MUD_BRICKS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_packed_mud': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:packed_mud')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:mud_bricks'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_packed_mud']],
    rewards=AdvancementRewards(recipes=['minecraft:mud_bricks']),
)

MUD_BRICK_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_mud_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:mud_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:mud_brick_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_mud_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:mud_brick_slab']),
)

MUD_BRICK_SLAB_FROM_MUD_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_mud_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:mud_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:mud_brick_slab_from_mud_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_mud_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:mud_brick_slab_from_mud_bricks_stonecutting']),
)

MUD_BRICK_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_mud_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:mud_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:mud_brick_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_mud_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:mud_brick_stairs']),
)

MUD_BRICK_STAIRS_FROM_MUD_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_mud_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:mud_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:mud_brick_stairs_from_mud_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_mud_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:mud_brick_stairs_from_mud_bricks_stonecutting']),
)

NETHERITE_BLOCK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_netherite_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:netherite_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:netherite_block'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_netherite_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:netherite_block']),
)

NETHER_BRICKS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_nether_brick': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:nether_brick')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:nether_bricks'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_nether_brick']],
    rewards=AdvancementRewards(recipes=['minecraft:nether_bricks']),
)

NETHER_BRICK_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_nether_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:nether_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:nether_brick_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_nether_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:nether_brick_slab']),
)

NETHER_BRICK_SLAB_FROM_NETHER_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_nether_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:nether_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:nether_brick_slab_from_nether_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_nether_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:nether_brick_slab_from_nether_bricks_stonecutting']),
)

NETHER_BRICK_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_nether_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:nether_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:nether_brick_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_nether_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:nether_brick_stairs']),
)

NETHER_BRICK_STAIRS_FROM_NETHER_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_nether_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:nether_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:nether_brick_stairs_from_nether_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_nether_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:nether_brick_stairs_from_nether_bricks_stonecutting']),
)

NETHER_WART_BLOCK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_nether_wart': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:nether_wart')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:nether_wart_block'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_nether_wart']],
    rewards=AdvancementRewards(recipes=['minecraft:nether_wart_block']),
)

OAK_PLANKS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_logs': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:oak_logs')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:oak_planks'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_logs']],
    rewards=AdvancementRewards(recipes=['minecraft:oak_planks']),
)

OAK_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oak_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:oak_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:oak_slab']),
)

OAK_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oak_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:oak_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:oak_stairs']),
)

OAK_WOOD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oak_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:oak_wood'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_log']],
    rewards=AdvancementRewards(recipes=['minecraft:oak_wood']),
)

ORANGE_CONCRETE_POWDER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gravel': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gravel')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_sand': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sand')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:orange_concrete_powder'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sand', 'has_gravel']],
    rewards=AdvancementRewards(recipes=['minecraft:orange_concrete_powder']),
)

ORANGE_CONCRETE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_orange_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:orange_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:orange_concrete_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_orange_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:orange_concrete_slab']),
)

ORANGE_CONCRETE_SLAB_FROM_ORANGE_CONCRETE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_orange_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:orange_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:orange_concrete_slab_from_orange_concrete_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_orange_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:orange_concrete_slab_from_orange_concrete_stonecutting']),
)

ORANGE_CONCRETE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_orange_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:orange_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:orange_concrete_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_orange_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:orange_concrete_stairs']),
)

ORANGE_CONCRETE_STAIRS_FROM_ORANGE_CONCRETE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_orange_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:orange_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:orange_concrete_stairs_from_orange_concrete_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_orange_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:orange_concrete_stairs_from_orange_concrete_stonecutting']),
)

ORANGE_STAINED_GLASS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glass')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:orange_stained_glass'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass']],
    rewards=AdvancementRewards(recipes=['minecraft:orange_stained_glass']),
)

ORANGE_TERRACOTTA = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_terracotta': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:terracotta')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:orange_terracotta'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_terracotta']],
    rewards=AdvancementRewards(recipes=['minecraft:orange_terracotta']),
)

ORANGE_WOOL_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_orange_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:orange_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:orange_wool_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_orange_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:orange_wool_slab']),
)

ORANGE_WOOL_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_orange_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:orange_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:orange_wool_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_orange_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:orange_wool_stairs']),
)

OXIDIZED_CHISELED_COPPER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oxidized_cut_copper_slab')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:oxidized_chiseled_copper'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:oxidized_chiseled_copper']),
)

OXIDIZED_CHISELED_COPPER_FROM_OXIDIZED_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_oxidized_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oxidized_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:oxidized_chiseled_copper_from_oxidized_copper_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_oxidized_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:oxidized_chiseled_copper_from_oxidized_copper_stonecutting']),
)

OXIDIZED_CHISELED_COPPER_FROM_OXIDIZED_CUT_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_oxidized_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oxidized_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:oxidized_chiseled_copper_from_oxidized_cut_copper_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_oxidized_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:oxidized_chiseled_copper_from_oxidized_cut_copper_stonecutting']),
)

OXIDIZED_COPPER_GRATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_oxidized_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oxidized_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:oxidized_copper_grate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_oxidized_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:oxidized_copper_grate']),
)

OXIDIZED_COPPER_GRATE_FROM_OXIDIZED_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_oxidized_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oxidized_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:oxidized_copper_grate_from_oxidized_copper_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_oxidized_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:oxidized_copper_grate_from_oxidized_copper_stonecutting']),
)

OXIDIZED_CUT_COPPER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_oxidized_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oxidized_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:oxidized_cut_copper'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_oxidized_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:oxidized_cut_copper']),
)

OXIDIZED_CUT_COPPER_FROM_OXIDIZED_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_oxidized_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oxidized_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:oxidized_cut_copper_from_oxidized_copper_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_oxidized_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:oxidized_cut_copper_from_oxidized_copper_stonecutting']),
)

OXIDIZED_CUT_COPPER_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_oxidized_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oxidized_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:oxidized_cut_copper_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_oxidized_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:oxidized_cut_copper_slab']),
)

OXIDIZED_CUT_COPPER_SLAB_FROM_OXIDIZED_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_oxidized_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oxidized_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:oxidized_cut_copper_slab_from_oxidized_copper_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_oxidized_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:oxidized_cut_copper_slab_from_oxidized_copper_stonecutting']),
)

OXIDIZED_CUT_COPPER_SLAB_FROM_OXIDIZED_CUT_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_oxidized_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oxidized_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:oxidized_cut_copper_slab_from_oxidized_cut_copper_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_oxidized_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:oxidized_cut_copper_slab_from_oxidized_cut_copper_stonecutting']),
)

OXIDIZED_CUT_COPPER_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_oxidized_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oxidized_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:oxidized_cut_copper_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_oxidized_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:oxidized_cut_copper_stairs']),
)

OXIDIZED_CUT_COPPER_STAIRS_FROM_OXIDIZED_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_oxidized_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oxidized_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:oxidized_cut_copper_stairs_from_oxidized_copper_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_oxidized_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:oxidized_cut_copper_stairs_from_oxidized_copper_stonecutting']),
)

OXIDIZED_CUT_COPPER_STAIRS_FROM_OXIDIZED_CUT_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_oxidized_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oxidized_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:oxidized_cut_copper_stairs_from_oxidized_cut_copper_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_oxidized_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:oxidized_cut_copper_stairs_from_oxidized_cut_copper_stonecutting']),
)

PACKED_ICE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_ice': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:ice')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:packed_ice'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_ice']],
    rewards=AdvancementRewards(recipes=['minecraft:packed_ice']),
)

PACKED_MUD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_mud': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:mud')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:packed_mud'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_mud']],
    rewards=AdvancementRewards(recipes=['minecraft:packed_mud']),
)

PALE_OAK_PLANKS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:pale_oak_logs')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pale_oak_planks'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_log']],
    rewards=AdvancementRewards(recipes=['minecraft:pale_oak_planks']),
)

PALE_OAK_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pale_oak_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pale_oak_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:pale_oak_slab']),
)

PALE_OAK_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pale_oak_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pale_oak_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:pale_oak_stairs']),
)

PALE_OAK_WOOD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pale_oak_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pale_oak_wood'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_log']],
    rewards=AdvancementRewards(recipes=['minecraft:pale_oak_wood']),
)

PINK_CONCRETE_POWDER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gravel': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gravel')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_sand': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sand')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pink_concrete_powder'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sand', 'has_gravel']],
    rewards=AdvancementRewards(recipes=['minecraft:pink_concrete_powder']),
)

PINK_CONCRETE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_pink_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pink_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pink_concrete_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_pink_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:pink_concrete_slab']),
)

PINK_CONCRETE_SLAB_FROM_PINK_CONCRETE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_pink_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pink_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pink_concrete_slab_from_pink_concrete_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_pink_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:pink_concrete_slab_from_pink_concrete_stonecutting']),
)

PINK_CONCRETE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_pink_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pink_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pink_concrete_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_pink_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:pink_concrete_stairs']),
)

PINK_CONCRETE_STAIRS_FROM_PINK_CONCRETE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_pink_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pink_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pink_concrete_stairs_from_pink_concrete_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_pink_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:pink_concrete_stairs_from_pink_concrete_stonecutting']),
)

PINK_STAINED_GLASS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glass')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pink_stained_glass'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass']],
    rewards=AdvancementRewards(recipes=['minecraft:pink_stained_glass']),
)

PINK_TERRACOTTA = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_terracotta': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:terracotta')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pink_terracotta'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_terracotta']],
    rewards=AdvancementRewards(recipes=['minecraft:pink_terracotta']),
)

PINK_WOOL_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_pink_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pink_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pink_wool_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_pink_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:pink_wool_slab']),
)

PINK_WOOL_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_pink_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pink_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pink_wool_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_pink_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:pink_wool_stairs']),
)

POLISHED_ANDESITE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_andesite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:andesite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_andesite'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_andesite']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_andesite']),
)

POLISHED_ANDESITE_FROM_ANDESITE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_andesite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:andesite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_andesite_from_andesite_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_andesite']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_andesite_from_andesite_stonecutting']),
)

POLISHED_ANDESITE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_andesite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_andesite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_andesite_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_andesite']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_andesite_slab']),
)

POLISHED_ANDESITE_SLAB_FROM_ANDESITE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_andesite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:andesite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_andesite_slab_from_andesite_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_andesite']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_andesite_slab_from_andesite_stonecutting']),
)

POLISHED_ANDESITE_SLAB_FROM_POLISHED_ANDESITE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_andesite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_andesite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_andesite_slab_from_polished_andesite_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_andesite']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_andesite_slab_from_polished_andesite_stonecutting']),
)

POLISHED_ANDESITE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_andesite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_andesite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_andesite_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_andesite']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_andesite_stairs']),
)

POLISHED_ANDESITE_STAIRS_FROM_ANDESITE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_andesite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:andesite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_andesite_stairs_from_andesite_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_andesite']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_andesite_stairs_from_andesite_stonecutting']),
)

POLISHED_ANDESITE_STAIRS_FROM_POLISHED_ANDESITE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_andesite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_andesite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:polished_andesite_stairs_from_polished_andesite_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_andesite']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_andesite_stairs_from_polished_andesite_stonecutting']),
)

POLISHED_BASALT = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_basalt': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:basalt')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_basalt'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_basalt']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_basalt']),
)

POLISHED_BASALT_FROM_BASALT_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_basalt': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:basalt')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_basalt_from_basalt_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_basalt']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_basalt_from_basalt_stonecutting']),
)

POLISHED_BLACKSTONE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blackstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blackstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_blackstone'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_blackstone']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_blackstone']),
)

POLISHED_BLACKSTONE_BRICKS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_blackstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_blackstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_blackstone_bricks'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_blackstone']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_blackstone_bricks']),
)

POLISHED_BLACKSTONE_BRICKS_FROM_BLACKSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blackstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blackstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_blackstone_bricks_from_blackstone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_blackstone']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_blackstone_bricks_from_blackstone_stonecutting']),
)

POLISHED_BLACKSTONE_BRICKS_FROM_POLISHED_BLACKSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_blackstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_blackstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:polished_blackstone_bricks_from_polished_blackstone_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_blackstone']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_blackstone_bricks_from_polished_blackstone_stonecutting']),
)

POLISHED_BLACKSTONE_BRICK_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_blackstone_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_blackstone_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_blackstone_brick_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_blackstone_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_blackstone_brick_slab']),
)

POLISHED_BLACKSTONE_BRICK_SLAB_FROM_BLACKSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blackstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blackstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:polished_blackstone_brick_slab_from_blackstone_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_blackstone']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_blackstone_brick_slab_from_blackstone_stonecutting']),
)

POLISHED_BLACKSTONE_BRICK_SLAB_FROM_POLISHED_BLACKSTONE_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_blackstone_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_blackstone_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:polished_blackstone_brick_slab_from_polished_blackstone_bricks_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_blackstone_bricks']],
    rewards=AdvancementRewards(
        recipes=['minecraft:polished_blackstone_brick_slab_from_polished_blackstone_bricks_stonecutting'],
    ),
)

POLISHED_BLACKSTONE_BRICK_SLAB_FROM_POLISHED_BLACKSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_blackstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_blackstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:polished_blackstone_brick_slab_from_polished_blackstone_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_blackstone']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_blackstone_brick_slab_from_polished_blackstone_stonecutting']),
)

POLISHED_BLACKSTONE_BRICK_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_blackstone_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_blackstone_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_blackstone_brick_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_blackstone_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_blackstone_brick_stairs']),
)

POLISHED_BLACKSTONE_BRICK_STAIRS_FROM_BLACKSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blackstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blackstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:polished_blackstone_brick_stairs_from_blackstone_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_blackstone']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_blackstone_brick_stairs_from_blackstone_stonecutting']),
)

POLISHED_BLACKSTONE_BRICK_STAIRS_FROM_POLISHED_BLACKSTONE_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_blackstone_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_blackstone_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:polished_blackstone_brick_stairs_from_polished_blackstone_bricks_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_blackstone_bricks']],
    rewards=AdvancementRewards(
        recipes=['minecraft:polished_blackstone_brick_stairs_from_polished_blackstone_bricks_stonecutting'],
    ),
)

POLISHED_BLACKSTONE_BRICK_STAIRS_FROM_POLISHED_BLACKSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_blackstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_blackstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:polished_blackstone_brick_stairs_from_polished_blackstone_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_blackstone']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_blackstone_brick_stairs_from_polished_blackstone_stonecutting']),
)

POLISHED_BLACKSTONE_FROM_BLACKSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blackstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blackstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_blackstone_from_blackstone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_blackstone']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_blackstone_from_blackstone_stonecutting']),
)

POLISHED_BLACKSTONE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_blackstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_blackstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_blackstone_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_blackstone']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_blackstone_slab']),
)

POLISHED_BLACKSTONE_SLAB_FROM_BLACKSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blackstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blackstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_blackstone_slab_from_blackstone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_blackstone']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_blackstone_slab_from_blackstone_stonecutting']),
)

POLISHED_BLACKSTONE_SLAB_FROM_POLISHED_BLACKSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_blackstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_blackstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:polished_blackstone_slab_from_polished_blackstone_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_blackstone']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_blackstone_slab_from_polished_blackstone_stonecutting']),
)

POLISHED_BLACKSTONE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_blackstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_blackstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_blackstone_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_blackstone']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_blackstone_stairs']),
)

POLISHED_BLACKSTONE_STAIRS_FROM_BLACKSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blackstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blackstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_blackstone_stairs_from_blackstone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_blackstone']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_blackstone_stairs_from_blackstone_stonecutting']),
)

POLISHED_BLACKSTONE_STAIRS_FROM_POLISHED_BLACKSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_blackstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_blackstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:polished_blackstone_stairs_from_polished_blackstone_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_blackstone']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_blackstone_stairs_from_polished_blackstone_stonecutting']),
)

POLISHED_CINNABAR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cinnabar': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cinnabar')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_cinnabar'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cinnabar']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_cinnabar']),
)

POLISHED_CINNABAR_FROM_CINNABAR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cinnabar': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cinnabar')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_cinnabar_from_cinnabar_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cinnabar']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_cinnabar_from_cinnabar_stonecutting']),
)

POLISHED_CINNABAR_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_cinnabar': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_cinnabar')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_cinnabar_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_cinnabar']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_cinnabar_slab']),
)

POLISHED_CINNABAR_SLAB_FROM_CINNABAR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cinnabar': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cinnabar')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_cinnabar_slab_from_cinnabar_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cinnabar']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_cinnabar_slab_from_cinnabar_stonecutting']),
)

POLISHED_CINNABAR_SLAB_FROM_POLISHED_CINNABAR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_cinnabar': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_cinnabar')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_cinnabar_slab_from_polished_cinnabar_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_cinnabar']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_cinnabar_slab_from_polished_cinnabar_stonecutting']),
)

POLISHED_CINNABAR_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_cinnabar': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_cinnabar')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_cinnabar_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_cinnabar']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_cinnabar_stairs']),
)

POLISHED_CINNABAR_STAIRS_FROM_CINNABAR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cinnabar': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cinnabar')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_cinnabar_stairs_from_cinnabar_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cinnabar']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_cinnabar_stairs_from_cinnabar_stonecutting']),
)

POLISHED_CINNABAR_STAIRS_FROM_POLISHED_CINNABAR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_cinnabar': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_cinnabar')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:polished_cinnabar_stairs_from_polished_cinnabar_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_cinnabar']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_cinnabar_stairs_from_polished_cinnabar_stonecutting']),
)

POLISHED_DEEPSLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cobbled_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cobbled_deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_deepslate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cobbled_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_deepslate']),
)

POLISHED_DEEPSLATE_FROM_COBBLED_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cobbled_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cobbled_deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_deepslate_from_cobbled_deepslate_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cobbled_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_deepslate_from_cobbled_deepslate_stonecutting']),
)

POLISHED_DEEPSLATE_FROM_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_deepslate_from_deepslate_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_deepslate_from_deepslate_stonecutting']),
)

POLISHED_DEEPSLATE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_deepslate_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_deepslate_slab']),
)

POLISHED_DEEPSLATE_SLAB_FROM_COBBLED_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cobbled_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cobbled_deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:polished_deepslate_slab_from_cobbled_deepslate_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cobbled_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_deepslate_slab_from_cobbled_deepslate_stonecutting']),
)

POLISHED_DEEPSLATE_SLAB_FROM_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_deepslate_slab_from_deepslate_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_deepslate_slab_from_deepslate_stonecutting']),
)

POLISHED_DEEPSLATE_SLAB_FROM_POLISHED_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:polished_deepslate_slab_from_polished_deepslate_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_deepslate_slab_from_polished_deepslate_stonecutting']),
)

POLISHED_DEEPSLATE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_deepslate_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_deepslate_stairs']),
)

POLISHED_DEEPSLATE_STAIRS_FROM_COBBLED_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cobbled_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cobbled_deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:polished_deepslate_stairs_from_cobbled_deepslate_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cobbled_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_deepslate_stairs_from_cobbled_deepslate_stonecutting']),
)

POLISHED_DEEPSLATE_STAIRS_FROM_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_deepslate_stairs_from_deepslate_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_deepslate_stairs_from_deepslate_stonecutting']),
)

POLISHED_DEEPSLATE_STAIRS_FROM_POLISHED_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:polished_deepslate_stairs_from_polished_deepslate_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_deepslate_stairs_from_polished_deepslate_stonecutting']),
)

POLISHED_DIORITE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_diorite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:diorite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_diorite'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_diorite']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_diorite']),
)

POLISHED_DIORITE_FROM_DIORITE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_diorite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:diorite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_diorite_from_diorite_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_diorite']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_diorite_from_diorite_stonecutting']),
)

POLISHED_DIORITE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_diorite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_diorite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_diorite_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_diorite']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_diorite_slab']),
)

POLISHED_DIORITE_SLAB_FROM_DIORITE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_diorite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:diorite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_diorite_slab_from_diorite_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_diorite']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_diorite_slab_from_diorite_stonecutting']),
)

POLISHED_DIORITE_SLAB_FROM_POLISHED_DIORITE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_diorite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_diorite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_diorite_slab_from_polished_diorite_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_diorite']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_diorite_slab_from_polished_diorite_stonecutting']),
)

POLISHED_DIORITE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_diorite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_diorite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_diorite_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_diorite']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_diorite_stairs']),
)

POLISHED_DIORITE_STAIRS_FROM_DIORITE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_diorite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:diorite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_diorite_stairs_from_diorite_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_diorite']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_diorite_stairs_from_diorite_stonecutting']),
)

POLISHED_DIORITE_STAIRS_FROM_POLISHED_DIORITE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_diorite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_diorite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_diorite_stairs_from_polished_diorite_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_diorite']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_diorite_stairs_from_polished_diorite_stonecutting']),
)

POLISHED_GRANITE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_granite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:granite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_granite'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_granite']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_granite']),
)

POLISHED_GRANITE_FROM_GRANITE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_granite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:granite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_granite_from_granite_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_granite']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_granite_from_granite_stonecutting']),
)

POLISHED_GRANITE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_granite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_granite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_granite_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_granite']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_granite_slab']),
)

POLISHED_GRANITE_SLAB_FROM_GRANITE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_granite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:granite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_granite_slab_from_granite_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_granite']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_granite_slab_from_granite_stonecutting']),
)

POLISHED_GRANITE_SLAB_FROM_POLISHED_GRANITE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_granite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_granite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_granite_slab_from_polished_granite_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_granite']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_granite_slab_from_polished_granite_stonecutting']),
)

POLISHED_GRANITE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_granite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_granite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_granite_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_granite']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_granite_stairs']),
)

POLISHED_GRANITE_STAIRS_FROM_GRANITE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_granite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:granite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_granite_stairs_from_granite_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_granite']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_granite_stairs_from_granite_stonecutting']),
)

POLISHED_GRANITE_STAIRS_FROM_POLISHED_GRANITE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_granite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_granite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_granite_stairs_from_polished_granite_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_granite']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_granite_stairs_from_polished_granite_stonecutting']),
)

POLISHED_SULFUR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sulfur': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sulfur')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_sulfur'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sulfur']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_sulfur']),
)

POLISHED_SULFUR_FROM_SULFUR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sulfur': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sulfur')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_sulfur_from_sulfur_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sulfur']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_sulfur_from_sulfur_stonecutting']),
)

POLISHED_SULFUR_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_sulfur': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_sulfur')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_sulfur_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_sulfur']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_sulfur_slab']),
)

POLISHED_SULFUR_SLAB_FROM_POLISHED_SULFUR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_sulfur': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_sulfur')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_sulfur_slab_from_polished_sulfur_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_sulfur']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_sulfur_slab_from_polished_sulfur_stonecutting']),
)

POLISHED_SULFUR_SLAB_FROM_SULFUR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sulfur': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sulfur')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_sulfur_slab_from_sulfur_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sulfur']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_sulfur_slab_from_sulfur_stonecutting']),
)

POLISHED_SULFUR_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_sulfur': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_sulfur')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_sulfur_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_sulfur']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_sulfur_stairs']),
)

POLISHED_SULFUR_STAIRS_FROM_POLISHED_SULFUR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_sulfur': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_sulfur')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_sulfur_stairs_from_polished_sulfur_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_sulfur']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_sulfur_stairs_from_polished_sulfur_stonecutting']),
)

POLISHED_SULFUR_STAIRS_FROM_SULFUR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sulfur': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sulfur')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_sulfur_stairs_from_sulfur_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sulfur']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_sulfur_stairs_from_sulfur_stonecutting']),
)

POLISHED_TUFF = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_tuff'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_tuff': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:tuff')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_tuff']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_tuff']),
)

POLISHED_TUFF_FROM_TUFF_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_tuff_from_tuff_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_tuff': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:tuff')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_tuff']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_tuff_from_tuff_stonecutting']),
)

POLISHED_TUFF_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_tuff': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_tuff')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_tuff_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_tuff']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_tuff_slab']),
)

POLISHED_TUFF_SLAB_FROM_POLISHED_TUFF_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_tuff': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_tuff')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_tuff_slab_from_polished_tuff_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_tuff']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_tuff_slab_from_polished_tuff_stonecutting']),
)

POLISHED_TUFF_SLAB_FROM_TUFF_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_tuff_slab_from_tuff_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_tuff': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:tuff')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_tuff']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_tuff_slab_from_tuff_stonecutting']),
)

POLISHED_TUFF_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_tuff': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_tuff')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_tuff_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_tuff']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_tuff_stairs']),
)

POLISHED_TUFF_STAIRS_FROM_POLISHED_TUFF_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_tuff': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_tuff')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_tuff_stairs_from_polished_tuff_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_tuff']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_tuff_stairs_from_polished_tuff_stonecutting']),
)

POLISHED_TUFF_STAIRS_FROM_TUFF_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_tuff_stairs_from_tuff_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_tuff': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:tuff')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_tuff']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_tuff_stairs_from_tuff_stonecutting']),
)

POPLAR_PLANKS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_logs': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:poplar_logs')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:poplar_planks'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_logs']],
    rewards=AdvancementRewards(recipes=['minecraft:poplar_planks']),
)

POPLAR_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:poplar_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:poplar_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:poplar_slab']),
)

POPLAR_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:poplar_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:poplar_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:poplar_stairs']),
)

POPLAR_WOOD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:poplar_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:poplar_wood'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_log']],
    rewards=AdvancementRewards(recipes=['minecraft:poplar_wood']),
)

POTENT_SULFUR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sulfur': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sulfur')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:potent_sulfur'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sulfur']],
    rewards=AdvancementRewards(recipes=['minecraft:potent_sulfur']),
)

PRISMARINE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_prismarine_shard': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:prismarine_shard')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:prismarine'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_prismarine_shard']],
    rewards=AdvancementRewards(recipes=['minecraft:prismarine']),
)

PRISMARINE_BRICKS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_prismarine_shard': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:prismarine_shard')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:prismarine_bricks'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_prismarine_shard']],
    rewards=AdvancementRewards(recipes=['minecraft:prismarine_bricks']),
)

PRISMARINE_BRICK_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_prismarine_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:prismarine_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:prismarine_brick_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_prismarine_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:prismarine_brick_slab']),
)

PRISMARINE_BRICK_SLAB_FROM_PRISMARINE_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_prismarine_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:prismarine_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:prismarine_brick_slab_from_prismarine_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_prismarine_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:prismarine_brick_slab_from_prismarine_bricks_stonecutting']),
)

PRISMARINE_BRICK_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_prismarine_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:prismarine_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:prismarine_brick_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_prismarine_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:prismarine_brick_stairs']),
)

PRISMARINE_BRICK_STAIRS_FROM_PRISMARINE_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_prismarine_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:prismarine_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:prismarine_brick_stairs_from_prismarine_bricks_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_prismarine_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:prismarine_brick_stairs_from_prismarine_bricks_stonecutting']),
)

PRISMARINE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_prismarine': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:prismarine')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:prismarine_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_prismarine']],
    rewards=AdvancementRewards(recipes=['minecraft:prismarine_slab']),
)

PRISMARINE_SLAB_FROM_PRISMARINE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_prismarine': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:prismarine')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:prismarine_slab_from_prismarine_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_prismarine']],
    rewards=AdvancementRewards(recipes=['minecraft:prismarine_slab_from_prismarine_stonecutting']),
)

PRISMARINE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_prismarine': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:prismarine')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:prismarine_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_prismarine']],
    rewards=AdvancementRewards(recipes=['minecraft:prismarine_stairs']),
)

PRISMARINE_STAIRS_FROM_PRISMARINE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_prismarine': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:prismarine')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:prismarine_stairs_from_prismarine_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_prismarine']],
    rewards=AdvancementRewards(recipes=['minecraft:prismarine_stairs_from_prismarine_stonecutting']),
)

PURPLE_CONCRETE_POWDER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gravel': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gravel')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_sand': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sand')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:purple_concrete_powder'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sand', 'has_gravel']],
    rewards=AdvancementRewards(recipes=['minecraft:purple_concrete_powder']),
)

PURPLE_CONCRETE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_purple_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:purple_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:purple_concrete_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_purple_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:purple_concrete_slab']),
)

PURPLE_CONCRETE_SLAB_FROM_PURPLE_CONCRETE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_purple_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:purple_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:purple_concrete_slab_from_purple_concrete_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_purple_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:purple_concrete_slab_from_purple_concrete_stonecutting']),
)

PURPLE_CONCRETE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_purple_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:purple_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:purple_concrete_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_purple_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:purple_concrete_stairs']),
)

PURPLE_CONCRETE_STAIRS_FROM_PURPLE_CONCRETE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_purple_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:purple_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:purple_concrete_stairs_from_purple_concrete_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_purple_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:purple_concrete_stairs_from_purple_concrete_stonecutting']),
)

PURPLE_STAINED_GLASS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glass')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:purple_stained_glass'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass']],
    rewards=AdvancementRewards(recipes=['minecraft:purple_stained_glass']),
)

PURPLE_TERRACOTTA = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_terracotta': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:terracotta')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:purple_terracotta'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_terracotta']],
    rewards=AdvancementRewards(recipes=['minecraft:purple_terracotta']),
)

PURPLE_WOOL_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_purple_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:purple_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:purple_wool_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_purple_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:purple_wool_slab']),
)

PURPLE_WOOL_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_purple_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:purple_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:purple_wool_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_purple_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:purple_wool_stairs']),
)

PURPUR_BLOCK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_chorus_fruit_popped': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:popped_chorus_fruit')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:purpur_block'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_chorus_fruit_popped']],
    rewards=AdvancementRewards(recipes=['minecraft:purpur_block']),
)

PURPUR_PILLAR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_purpur_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:purpur_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:purpur_pillar'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_purpur_block']],
    rewards=AdvancementRewards(recipes=['minecraft:purpur_pillar']),
)

PURPUR_PILLAR_FROM_PURPUR_BLOCK_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_purpur_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:purpur_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:purpur_pillar_from_purpur_block_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_purpur_block']],
    rewards=AdvancementRewards(recipes=['minecraft:purpur_pillar_from_purpur_block_stonecutting']),
)

PURPUR_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_purpur_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:purpur_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:purpur_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_purpur_block']],
    rewards=AdvancementRewards(recipes=['minecraft:purpur_slab']),
)

PURPUR_SLAB_FROM_PURPUR_BLOCK_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_purpur_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:purpur_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:purpur_slab_from_purpur_block_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_purpur_block']],
    rewards=AdvancementRewards(recipes=['minecraft:purpur_slab_from_purpur_block_stonecutting']),
)

PURPUR_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_purpur_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:purpur_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:purpur_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_purpur_block']],
    rewards=AdvancementRewards(recipes=['minecraft:purpur_stairs']),
)

PURPUR_STAIRS_FROM_PURPUR_BLOCK_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_purpur_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:purpur_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:purpur_stairs_from_purpur_block_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_purpur_block']],
    rewards=AdvancementRewards(recipes=['minecraft:purpur_stairs_from_purpur_block_stonecutting']),
)

QUARTZ_BLOCK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_quartz': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:quartz')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:quartz_block'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_quartz']],
    rewards=AdvancementRewards(recipes=['minecraft:quartz_block']),
)

QUARTZ_BRICKS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_quartz_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:quartz_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:quartz_bricks'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_quartz_block']],
    rewards=AdvancementRewards(recipes=['minecraft:quartz_bricks']),
)

QUARTZ_BRICKS_FROM_QUARTZ_BLOCK_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_quartz_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:quartz_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:quartz_bricks_from_quartz_block_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_quartz_block']],
    rewards=AdvancementRewards(recipes=['minecraft:quartz_bricks_from_quartz_block_stonecutting']),
)

QUARTZ_PILLAR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_chiseled_quartz_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:chiseled_quartz_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_quartz_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:quartz_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_quartz_pillar': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:quartz_pillar')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:quartz_pillar'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_chiseled_quartz_block', 'has_quartz_block', 'has_quartz_pillar']],
    rewards=AdvancementRewards(recipes=['minecraft:quartz_pillar']),
)

QUARTZ_PILLAR_FROM_QUARTZ_BLOCK_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_quartz_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:quartz_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:quartz_pillar_from_quartz_block_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_quartz_block']],
    rewards=AdvancementRewards(recipes=['minecraft:quartz_pillar_from_quartz_block_stonecutting']),
)

QUARTZ_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_chiseled_quartz_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:chiseled_quartz_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_quartz_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:quartz_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_quartz_pillar': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:quartz_pillar')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:quartz_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_chiseled_quartz_block', 'has_quartz_block', 'has_quartz_pillar']],
    rewards=AdvancementRewards(recipes=['minecraft:quartz_slab']),
)

QUARTZ_SLAB_FROM_QUARTZ_BLOCK_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_quartz_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:quartz_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:quartz_slab_from_quartz_block_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_quartz_block']],
    rewards=AdvancementRewards(recipes=['minecraft:quartz_slab_from_quartz_block_stonecutting']),
)

QUARTZ_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_chiseled_quartz_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:chiseled_quartz_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_quartz_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:quartz_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_quartz_pillar': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:quartz_pillar')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:quartz_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_chiseled_quartz_block', 'has_quartz_block', 'has_quartz_pillar']],
    rewards=AdvancementRewards(recipes=['minecraft:quartz_stairs']),
)

QUARTZ_STAIRS_FROM_QUARTZ_BLOCK_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_quartz_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:quartz_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:quartz_stairs_from_quartz_block_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_quartz_block']],
    rewards=AdvancementRewards(recipes=['minecraft:quartz_stairs_from_quartz_block_stonecutting']),
)

RAW_COPPER_BLOCK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_raw_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:raw_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:raw_copper_block'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_raw_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:raw_copper_block']),
)

RAW_GOLD_BLOCK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_raw_gold': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:raw_gold')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:raw_gold_block'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_raw_gold']],
    rewards=AdvancementRewards(recipes=['minecraft:raw_gold_block']),
)

RAW_IRON_BLOCK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_raw_iron': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:raw_iron')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:raw_iron_block'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_raw_iron']],
    rewards=AdvancementRewards(recipes=['minecraft:raw_iron_block']),
)

RED_CONCRETE_POWDER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gravel': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gravel')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_sand': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sand')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:red_concrete_powder'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sand', 'has_gravel']],
    rewards=AdvancementRewards(recipes=['minecraft:red_concrete_powder']),
)

RED_CONCRETE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_red_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:red_concrete_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_red_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:red_concrete_slab']),
)

RED_CONCRETE_SLAB_FROM_RED_CONCRETE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_red_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:red_concrete_slab_from_red_concrete_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_red_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:red_concrete_slab_from_red_concrete_stonecutting']),
)

RED_CONCRETE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_red_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:red_concrete_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_red_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:red_concrete_stairs']),
)

RED_CONCRETE_STAIRS_FROM_RED_CONCRETE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_red_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:red_concrete_stairs_from_red_concrete_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_red_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:red_concrete_stairs_from_red_concrete_stonecutting']),
)

RED_NETHER_BRICKS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_nether_wart': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:nether_wart')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:red_nether_bricks'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_nether_wart']],
    rewards=AdvancementRewards(recipes=['minecraft:red_nether_bricks']),
)

RED_NETHER_BRICK_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_red_nether_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_nether_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:red_nether_brick_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_red_nether_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:red_nether_brick_slab']),
)

RED_NETHER_BRICK_SLAB_FROM_RED_NETHER_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_red_nether_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_nether_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:red_nether_brick_slab_from_red_nether_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_red_nether_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:red_nether_brick_slab_from_red_nether_bricks_stonecutting']),
)

RED_NETHER_BRICK_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_red_nether_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_nether_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:red_nether_brick_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_red_nether_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:red_nether_brick_stairs']),
)

RED_NETHER_BRICK_STAIRS_FROM_RED_NETHER_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_red_nether_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_nether_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:red_nether_brick_stairs_from_red_nether_bricks_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_red_nether_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:red_nether_brick_stairs_from_red_nether_bricks_stonecutting']),
)

RED_SANDSTONE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sand': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_sand')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:red_sandstone'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sand']],
    rewards=AdvancementRewards(recipes=['minecraft:red_sandstone']),
)

RED_SANDSTONE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_chiseled_red_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:chiseled_red_sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_red_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:red_sandstone_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_red_sandstone', 'has_chiseled_red_sandstone']],
    rewards=AdvancementRewards(recipes=['minecraft:red_sandstone_slab']),
)

RED_SANDSTONE_SLAB_FROM_RED_SANDSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_red_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:red_sandstone_slab_from_red_sandstone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_red_sandstone']],
    rewards=AdvancementRewards(recipes=['minecraft:red_sandstone_slab_from_red_sandstone_stonecutting']),
)

RED_SANDSTONE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_chiseled_red_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:chiseled_red_sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_cut_red_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cut_red_sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_red_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:red_sandstone_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_red_sandstone', 'has_chiseled_red_sandstone', 'has_cut_red_sandstone']],
    rewards=AdvancementRewards(recipes=['minecraft:red_sandstone_stairs']),
)

RED_SANDSTONE_STAIRS_FROM_RED_SANDSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_red_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:red_sandstone_stairs_from_red_sandstone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_red_sandstone']],
    rewards=AdvancementRewards(recipes=['minecraft:red_sandstone_stairs_from_red_sandstone_stonecutting']),
)

RED_STAINED_GLASS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glass')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:red_stained_glass'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass']],
    rewards=AdvancementRewards(recipes=['minecraft:red_stained_glass']),
)

RED_TERRACOTTA = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_terracotta': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:terracotta')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:red_terracotta'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_terracotta']],
    rewards=AdvancementRewards(recipes=['minecraft:red_terracotta']),
)

RED_WOOL_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_red_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:red_wool_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_red_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:red_wool_slab']),
)

RED_WOOL_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_red_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:red_wool_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_red_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:red_wool_stairs']),
)

RESIN_BLOCK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_resin_clump': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:resin_clump')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:resin_block'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_resin_clump']],
    rewards=AdvancementRewards(recipes=['minecraft:resin_block']),
)

RESIN_BRICKS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_resin_brick': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:resin_brick')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:resin_bricks'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_resin_brick']],
    rewards=AdvancementRewards(recipes=['minecraft:resin_bricks']),
)

RESIN_BRICK_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_resin_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:resin_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:resin_brick_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_resin_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:resin_brick_slab']),
)

RESIN_BRICK_SLAB_FROM_RESIN_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_resin_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:resin_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:resin_brick_slab_from_resin_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_resin_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:resin_brick_slab_from_resin_bricks_stonecutting']),
)

RESIN_BRICK_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_resin_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:resin_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:resin_brick_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_resin_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:resin_brick_stairs']),
)

RESIN_BRICK_STAIRS_FROM_RESIN_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_resin_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:resin_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:resin_brick_stairs_from_resin_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_resin_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:resin_brick_stairs_from_resin_bricks_stonecutting']),
)

SANDSTONE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sand': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sand')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:sandstone'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sand']],
    rewards=AdvancementRewards(recipes=['minecraft:sandstone']),
)

SANDSTONE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_chiseled_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:chiseled_sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:sandstone_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sandstone', 'has_chiseled_sandstone']],
    rewards=AdvancementRewards(recipes=['minecraft:sandstone_slab']),
)

SANDSTONE_SLAB_FROM_SANDSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:sandstone_slab_from_sandstone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sandstone']],
    rewards=AdvancementRewards(recipes=['minecraft:sandstone_slab_from_sandstone_stonecutting']),
)

SANDSTONE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_chiseled_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:chiseled_sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_cut_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cut_sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:sandstone_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sandstone', 'has_chiseled_sandstone', 'has_cut_sandstone']],
    rewards=AdvancementRewards(recipes=['minecraft:sandstone_stairs']),
)

SANDSTONE_STAIRS_FROM_SANDSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:sandstone_stairs_from_sandstone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sandstone']],
    rewards=AdvancementRewards(recipes=['minecraft:sandstone_stairs_from_sandstone_stonecutting']),
)

SEA_LANTERN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_prismarine_crystals': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:prismarine_crystals')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:sea_lantern'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_prismarine_crystals']],
    rewards=AdvancementRewards(recipes=['minecraft:sea_lantern']),
)

SMOOTH_BASALT = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_basalt': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:basalt')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:smooth_basalt'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_basalt']],
    rewards=AdvancementRewards(recipes=['minecraft:smooth_basalt']),
)

SMOOTH_QUARTZ = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_quartz_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:quartz_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:smooth_quartz'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_quartz_block']],
    rewards=AdvancementRewards(recipes=['minecraft:smooth_quartz']),
)

SMOOTH_QUARTZ_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_smooth_quartz': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:smooth_quartz')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:smooth_quartz_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_smooth_quartz']],
    rewards=AdvancementRewards(recipes=['minecraft:smooth_quartz_slab']),
)

SMOOTH_QUARTZ_SLAB_FROM_SMOOTH_QUARTZ_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_smooth_quartz': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:smooth_quartz')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:smooth_quartz_slab_from_smooth_quartz_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_smooth_quartz']],
    rewards=AdvancementRewards(recipes=['minecraft:smooth_quartz_slab_from_smooth_quartz_stonecutting']),
)

SMOOTH_QUARTZ_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_smooth_quartz': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:smooth_quartz')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:smooth_quartz_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_smooth_quartz']],
    rewards=AdvancementRewards(recipes=['minecraft:smooth_quartz_stairs']),
)

SMOOTH_QUARTZ_STAIRS_FROM_SMOOTH_QUARTZ_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_smooth_quartz': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:smooth_quartz')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:smooth_quartz_stairs_from_smooth_quartz_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_smooth_quartz']],
    rewards=AdvancementRewards(recipes=['minecraft:smooth_quartz_stairs_from_smooth_quartz_stonecutting']),
)

SMOOTH_RED_SANDSTONE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_red_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:smooth_red_sandstone'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_red_sandstone']],
    rewards=AdvancementRewards(recipes=['minecraft:smooth_red_sandstone']),
)

SMOOTH_RED_SANDSTONE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_smooth_red_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:smooth_red_sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:smooth_red_sandstone_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_smooth_red_sandstone']],
    rewards=AdvancementRewards(recipes=['minecraft:smooth_red_sandstone_slab']),
)

SMOOTH_RED_SANDSTONE_SLAB_FROM_SMOOTH_RED_SANDSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_smooth_red_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:smooth_red_sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:smooth_red_sandstone_slab_from_smooth_red_sandstone_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_smooth_red_sandstone']],
    rewards=AdvancementRewards(recipes=['minecraft:smooth_red_sandstone_slab_from_smooth_red_sandstone_stonecutting']),
)

SMOOTH_RED_SANDSTONE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_smooth_red_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:smooth_red_sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:smooth_red_sandstone_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_smooth_red_sandstone']],
    rewards=AdvancementRewards(recipes=['minecraft:smooth_red_sandstone_stairs']),
)

SMOOTH_RED_SANDSTONE_STAIRS_FROM_SMOOTH_RED_SANDSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_smooth_red_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:smooth_red_sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:smooth_red_sandstone_stairs_from_smooth_red_sandstone_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_smooth_red_sandstone']],
    rewards=AdvancementRewards(recipes=['minecraft:smooth_red_sandstone_stairs_from_smooth_red_sandstone_stonecutting']),
)

SMOOTH_SANDSTONE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:smooth_sandstone'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sandstone']],
    rewards=AdvancementRewards(recipes=['minecraft:smooth_sandstone']),
)

SMOOTH_SANDSTONE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_smooth_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:smooth_sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:smooth_sandstone_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_smooth_sandstone']],
    rewards=AdvancementRewards(recipes=['minecraft:smooth_sandstone_slab']),
)

SMOOTH_SANDSTONE_SLAB_FROM_SMOOTH_SANDSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_smooth_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:smooth_sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:smooth_sandstone_slab_from_smooth_sandstone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_smooth_sandstone']],
    rewards=AdvancementRewards(recipes=['minecraft:smooth_sandstone_slab_from_smooth_sandstone_stonecutting']),
)

SMOOTH_SANDSTONE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_smooth_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:smooth_sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:smooth_sandstone_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_smooth_sandstone']],
    rewards=AdvancementRewards(recipes=['minecraft:smooth_sandstone_stairs']),
)

SMOOTH_SANDSTONE_STAIRS_FROM_SMOOTH_SANDSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_smooth_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:smooth_sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:smooth_sandstone_stairs_from_smooth_sandstone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_smooth_sandstone']],
    rewards=AdvancementRewards(recipes=['minecraft:smooth_sandstone_stairs_from_smooth_sandstone_stonecutting']),
)

SMOOTH_STONE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:smooth_stone'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stone']],
    rewards=AdvancementRewards(recipes=['minecraft:smooth_stone']),
)

SMOOTH_STONE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_smooth_stone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:smooth_stone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:smooth_stone_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_smooth_stone']],
    rewards=AdvancementRewards(recipes=['minecraft:smooth_stone_slab']),
)

SMOOTH_STONE_SLAB_FROM_SMOOTH_STONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_smooth_stone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:smooth_stone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:smooth_stone_slab_from_smooth_stone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_smooth_stone']],
    rewards=AdvancementRewards(recipes=['minecraft:smooth_stone_slab_from_smooth_stone_stonecutting']),
)

SNOW_BLOCK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_snowball': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:snowball')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:snow_block'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_snowball']],
    rewards=AdvancementRewards(recipes=['minecraft:snow_block']),
)

SPONGE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:sponge'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_wet_sponge': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:wet_sponge')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_wet_sponge']],
    rewards=AdvancementRewards(recipes=['minecraft:sponge']),
)

SPRUCE_PLANKS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_logs': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:spruce_logs')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:spruce_planks'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_logs']],
    rewards=AdvancementRewards(recipes=['minecraft:spruce_planks']),
)

SPRUCE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:spruce_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:spruce_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:spruce_slab']),
)

SPRUCE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:spruce_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:spruce_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:spruce_stairs']),
)

SPRUCE_WOOD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:spruce_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:spruce_wood'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_log']],
    rewards=AdvancementRewards(recipes=['minecraft:spruce_wood']),
)

STONE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cobblestone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cobblestone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stone'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cobblestone']],
    rewards=AdvancementRewards(recipes=['minecraft:stone']),
)

STONE_BRICKS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stone_bricks'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stone']],
    rewards=AdvancementRewards(recipes=['minecraft:stone_bricks']),
)

STONE_BRICKS_FROM_STONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stone_bricks_from_stone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stone']],
    rewards=AdvancementRewards(recipes=['minecraft:stone_bricks_from_stone_stonecutting']),
)

STONE_BRICK_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stone_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:stone_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stone_brick_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stone_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:stone_brick_slab']),
)

STONE_BRICK_SLAB_FROM_STONE_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stone_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stone_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stone_brick_slab_from_stone_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stone_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:stone_brick_slab_from_stone_bricks_stonecutting']),
)

STONE_BRICK_SLAB_FROM_STONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stone_brick_slab_from_stone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stone']],
    rewards=AdvancementRewards(recipes=['minecraft:stone_brick_slab_from_stone_stonecutting']),
)

STONE_BRICK_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stone_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:stone_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stone_brick_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stone_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:stone_brick_stairs']),
)

STONE_BRICK_STAIRS_FROM_STONE_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stone_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stone_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stone_brick_stairs_from_stone_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stone_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:stone_brick_stairs_from_stone_bricks_stonecutting']),
)

STONE_BRICK_STAIRS_FROM_STONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stone_brick_stairs_from_stone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stone']],
    rewards=AdvancementRewards(recipes=['minecraft:stone_brick_stairs_from_stone_stonecutting']),
)

STONE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stone_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stone']],
    rewards=AdvancementRewards(recipes=['minecraft:stone_slab']),
)

STONE_SLAB_FROM_STONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stone_slab_from_stone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stone']],
    rewards=AdvancementRewards(recipes=['minecraft:stone_slab_from_stone_stonecutting']),
)

STONE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stone_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stone']],
    rewards=AdvancementRewards(recipes=['minecraft:stone_stairs']),
)

STONE_STAIRS_FROM_STONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stone_stairs_from_stone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stone']],
    rewards=AdvancementRewards(recipes=['minecraft:stone_stairs_from_stone_stonecutting']),
)

STRIPPED_ACACIA_WOOD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_acacia_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stripped_acacia_wood'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_log']],
    rewards=AdvancementRewards(recipes=['minecraft:stripped_acacia_wood']),
)

STRIPPED_BIRCH_WOOD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_birch_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stripped_birch_wood'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_log']],
    rewards=AdvancementRewards(recipes=['minecraft:stripped_birch_wood']),
)

STRIPPED_CHERRY_WOOD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_cherry_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stripped_cherry_wood'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_log']],
    rewards=AdvancementRewards(recipes=['minecraft:stripped_cherry_wood']),
)

STRIPPED_CRIMSON_HYPHAE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_crimson_stem')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stripped_crimson_hyphae'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_log']],
    rewards=AdvancementRewards(recipes=['minecraft:stripped_crimson_hyphae']),
)

STRIPPED_DARK_OAK_WOOD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_dark_oak_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stripped_dark_oak_wood'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_log']],
    rewards=AdvancementRewards(recipes=['minecraft:stripped_dark_oak_wood']),
)

STRIPPED_JUNGLE_WOOD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_jungle_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stripped_jungle_wood'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_log']],
    rewards=AdvancementRewards(recipes=['minecraft:stripped_jungle_wood']),
)

STRIPPED_MANGROVE_WOOD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_mangrove_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stripped_mangrove_wood'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_log']],
    rewards=AdvancementRewards(recipes=['minecraft:stripped_mangrove_wood']),
)

STRIPPED_OAK_WOOD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_oak_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stripped_oak_wood'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_log']],
    rewards=AdvancementRewards(recipes=['minecraft:stripped_oak_wood']),
)

STRIPPED_PALE_OAK_WOOD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_pale_oak_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stripped_pale_oak_wood'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_log']],
    rewards=AdvancementRewards(recipes=['minecraft:stripped_pale_oak_wood']),
)

STRIPPED_POPLAR_WOOD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_poplar_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stripped_poplar_wood'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_log']],
    rewards=AdvancementRewards(recipes=['minecraft:stripped_poplar_wood']),
)

STRIPPED_SPRUCE_WOOD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_spruce_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stripped_spruce_wood'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_log']],
    rewards=AdvancementRewards(recipes=['minecraft:stripped_spruce_wood']),
)

STRIPPED_WARPED_HYPHAE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_warped_stem')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stripped_warped_hyphae'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_log']],
    rewards=AdvancementRewards(recipes=['minecraft:stripped_warped_hyphae']),
)

SULFUR_BRICKS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_sulfur': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_sulfur')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:sulfur_bricks'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_sulfur']],
    rewards=AdvancementRewards(recipes=['minecraft:sulfur_bricks']),
)

SULFUR_BRICKS_FROM_POLISHED_SULFUR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_sulfur': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_sulfur')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:sulfur_bricks_from_polished_sulfur_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_sulfur']],
    rewards=AdvancementRewards(recipes=['minecraft:sulfur_bricks_from_polished_sulfur_stonecutting']),
)

SULFUR_BRICKS_FROM_SULFUR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sulfur': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sulfur')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:sulfur_bricks_from_sulfur_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sulfur']],
    rewards=AdvancementRewards(recipes=['minecraft:sulfur_bricks_from_sulfur_stonecutting']),
)

SULFUR_BRICK_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sulfur_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sulfur_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:sulfur_brick_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sulfur_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:sulfur_brick_slab']),
)

SULFUR_BRICK_SLAB_FROM_POLISHED_SULFUR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_sulfur': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_sulfur')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:sulfur_brick_slab_from_polished_sulfur_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_sulfur']],
    rewards=AdvancementRewards(recipes=['minecraft:sulfur_brick_slab_from_polished_sulfur_stonecutting']),
)

SULFUR_BRICK_SLAB_FROM_SULFUR_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sulfur_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sulfur_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:sulfur_brick_slab_from_sulfur_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sulfur_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:sulfur_brick_slab_from_sulfur_bricks_stonecutting']),
)

SULFUR_BRICK_SLAB_FROM_SULFUR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sulfur': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sulfur')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:sulfur_brick_slab_from_sulfur_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sulfur']],
    rewards=AdvancementRewards(recipes=['minecraft:sulfur_brick_slab_from_sulfur_stonecutting']),
)

SULFUR_BRICK_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sulfur_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sulfur_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:sulfur_brick_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sulfur_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:sulfur_brick_stairs']),
)

SULFUR_BRICK_STAIRS_FROM_POLISHED_SULFUR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_sulfur': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_sulfur')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:sulfur_brick_stairs_from_polished_sulfur_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_sulfur']],
    rewards=AdvancementRewards(recipes=['minecraft:sulfur_brick_stairs_from_polished_sulfur_stonecutting']),
)

SULFUR_BRICK_STAIRS_FROM_SULFUR_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sulfur_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sulfur_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:sulfur_brick_stairs_from_sulfur_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sulfur_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:sulfur_brick_stairs_from_sulfur_bricks_stonecutting']),
)

SULFUR_BRICK_STAIRS_FROM_SULFUR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sulfur': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sulfur')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:sulfur_brick_stairs_from_sulfur_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sulfur']],
    rewards=AdvancementRewards(recipes=['minecraft:sulfur_brick_stairs_from_sulfur_stonecutting']),
)

SULFUR_FROM_SULFUR_SPIKES = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sulfur_spike': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sulfur_spike')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:sulfur_from_sulfur_spikes'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sulfur_spike']],
    rewards=AdvancementRewards(recipes=['minecraft:sulfur_from_sulfur_spikes']),
)

SULFUR_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sulfur': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sulfur')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:sulfur_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sulfur']],
    rewards=AdvancementRewards(recipes=['minecraft:sulfur_slab']),
)

SULFUR_SLAB_FROM_SULFUR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sulfur': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sulfur')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:sulfur_slab_from_sulfur_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sulfur']],
    rewards=AdvancementRewards(recipes=['minecraft:sulfur_slab_from_sulfur_stonecutting']),
)

SULFUR_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sulfur': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sulfur')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:sulfur_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sulfur']],
    rewards=AdvancementRewards(recipes=['minecraft:sulfur_stairs']),
)

SULFUR_STAIRS_FROM_SULFUR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sulfur': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sulfur')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:sulfur_stairs_from_sulfur_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sulfur']],
    rewards=AdvancementRewards(recipes=['minecraft:sulfur_stairs_from_sulfur_stonecutting']),
)

TERRACOTTA = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_clay_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:clay')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:terracotta'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_clay_block']],
    rewards=AdvancementRewards(recipes=['minecraft:terracotta']),
)

TINTED_GLASS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_amethyst_shard': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:amethyst_shard')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:tinted_glass'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_amethyst_shard']],
    rewards=AdvancementRewards(recipes=['minecraft:tinted_glass']),
)

TUFF_BRICKS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_tuff': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_tuff')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:tuff_bricks'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_tuff']],
    rewards=AdvancementRewards(recipes=['minecraft:tuff_bricks']),
)

TUFF_BRICKS_FROM_POLISHED_TUFF_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_tuff': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_tuff')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:tuff_bricks_from_polished_tuff_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_tuff']],
    rewards=AdvancementRewards(recipes=['minecraft:tuff_bricks_from_polished_tuff_stonecutting']),
)

TUFF_BRICKS_FROM_TUFF_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:tuff_bricks_from_tuff_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_tuff': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:tuff')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_tuff']],
    rewards=AdvancementRewards(recipes=['minecraft:tuff_bricks_from_tuff_stonecutting']),
)

TUFF_BRICK_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:tuff_brick_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_tuff_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:tuff_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_tuff_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:tuff_brick_slab']),
)

TUFF_BRICK_SLAB_FROM_POLISHED_TUFF_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_tuff': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_tuff')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:tuff_brick_slab_from_polished_tuff_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_tuff']],
    rewards=AdvancementRewards(recipes=['minecraft:tuff_brick_slab_from_polished_tuff_stonecutting']),
)

TUFF_BRICK_SLAB_FROM_TUFF_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:tuff_brick_slab_from_tuff_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_tuff_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:tuff_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_tuff_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:tuff_brick_slab_from_tuff_bricks_stonecutting']),
)

TUFF_BRICK_SLAB_FROM_TUFF_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:tuff_brick_slab_from_tuff_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_tuff': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:tuff')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_tuff']],
    rewards=AdvancementRewards(recipes=['minecraft:tuff_brick_slab_from_tuff_stonecutting']),
)

TUFF_BRICK_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:tuff_brick_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_tuff_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:tuff_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_tuff_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:tuff_brick_stairs']),
)

TUFF_BRICK_STAIRS_FROM_POLISHED_TUFF_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_tuff': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_tuff')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:tuff_brick_stairs_from_polished_tuff_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_tuff']],
    rewards=AdvancementRewards(recipes=['minecraft:tuff_brick_stairs_from_polished_tuff_stonecutting']),
)

TUFF_BRICK_STAIRS_FROM_TUFF_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:tuff_brick_stairs_from_tuff_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_tuff_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:tuff_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_tuff_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:tuff_brick_stairs_from_tuff_bricks_stonecutting']),
)

TUFF_BRICK_STAIRS_FROM_TUFF_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:tuff_brick_stairs_from_tuff_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_tuff': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:tuff')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_tuff']],
    rewards=AdvancementRewards(recipes=['minecraft:tuff_brick_stairs_from_tuff_stonecutting']),
)

TUFF_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:tuff_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_tuff': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:tuff')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_tuff']],
    rewards=AdvancementRewards(recipes=['minecraft:tuff_slab']),
)

TUFF_SLAB_FROM_TUFF_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:tuff_slab_from_tuff_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_tuff': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:tuff')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_tuff']],
    rewards=AdvancementRewards(recipes=['minecraft:tuff_slab_from_tuff_stonecutting']),
)

TUFF_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:tuff_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_tuff': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:tuff')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_tuff']],
    rewards=AdvancementRewards(recipes=['minecraft:tuff_stairs']),
)

TUFF_STAIRS_FROM_TUFF_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:tuff_stairs_from_tuff_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_tuff': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:tuff')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_tuff']],
    rewards=AdvancementRewards(recipes=['minecraft:tuff_stairs_from_tuff_stonecutting']),
)

WARPED_HYPHAE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:warped_stem')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:warped_hyphae'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_log']],
    rewards=AdvancementRewards(recipes=['minecraft:warped_hyphae']),
)

WARPED_PLANKS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_logs': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:warped_stems')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:warped_planks'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_logs']],
    rewards=AdvancementRewards(recipes=['minecraft:warped_planks']),
)

WARPED_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:warped_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:warped_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:warped_slab']),
)

WARPED_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:warped_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:warped_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:warped_stairs']),
)

WAXED_CHISELED_COPPER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_chiseled_copper'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_cut_copper_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_cut_copper_slab')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_cut_copper_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_chiseled_copper']),
)

WAXED_CHISELED_COPPER_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_chiseled_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:chiseled_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_chiseled_copper_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_chiseled_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_chiseled_copper_from_honeycomb']),
)

WAXED_CHISELED_COPPER_FROM_WAXED_COPPER_BLOCK_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_chiseled_copper_from_waxed_copper_block_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_copper_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_copper_block')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_copper_block']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_chiseled_copper_from_waxed_copper_block_stonecutting']),
)

WAXED_CHISELED_COPPER_FROM_WAXED_CUT_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_chiseled_copper_from_waxed_cut_copper_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_chiseled_copper_from_waxed_cut_copper_stonecutting']),
)

WAXED_COPPER_BARS_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_bars': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_bars')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_copper_bars_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_bars']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_copper_bars_from_honeycomb']),
)

WAXED_COPPER_BLOCK_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_copper_block_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_block']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_copper_block_from_honeycomb']),
)

WAXED_COPPER_CHAIN_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_chain': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_chain')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_copper_chain_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_chain']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_copper_chain_from_honeycomb']),
)

WAXED_COPPER_CHEST_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_chest': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_chest')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_copper_chest_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_chest']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_copper_chest_from_honeycomb']),
)

WAXED_COPPER_GOLEM_STATUE_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_golem_statue': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_golem_statue')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_copper_golem_statue_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_golem_statue']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_copper_golem_statue_from_honeycomb']),
)

WAXED_COPPER_GRATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_copper_grate'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_copper_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_copper_block')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_copper_block']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_copper_grate']),
)

WAXED_COPPER_GRATE_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_grate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_grate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_copper_grate_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_grate']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_copper_grate_from_honeycomb']),
)

WAXED_COPPER_GRATE_FROM_WAXED_COPPER_BLOCK_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_copper_grate_from_waxed_copper_block_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_copper_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_copper_block')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_copper_block']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_copper_grate_from_waxed_copper_block_stonecutting']),
)

WAXED_COPPER_LANTERN_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_lantern': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_lantern')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_copper_lantern_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_lantern']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_copper_lantern_from_honeycomb']),
)

WAXED_CUT_COPPER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_cut_copper'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_copper_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_copper_block')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_copper_block']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_cut_copper']),
)

WAXED_CUT_COPPER_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_cut_copper_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_cut_copper_from_honeycomb']),
)

WAXED_CUT_COPPER_FROM_WAXED_COPPER_BLOCK_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_cut_copper_from_waxed_copper_block_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_copper_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_copper_block')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_copper_block']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_cut_copper_from_waxed_copper_block_stonecutting']),
)

WAXED_CUT_COPPER_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_cut_copper_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_cut_copper_slab']),
)

WAXED_CUT_COPPER_SLAB_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cut_copper_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cut_copper_slab')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_cut_copper_slab_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cut_copper_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_cut_copper_slab_from_honeycomb']),
)

WAXED_CUT_COPPER_SLAB_FROM_WAXED_COPPER_BLOCK_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_cut_copper_slab_from_waxed_copper_block_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_copper_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_copper_block')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_copper_block']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_cut_copper_slab_from_waxed_copper_block_stonecutting']),
)

WAXED_CUT_COPPER_SLAB_FROM_WAXED_CUT_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_cut_copper_slab_from_waxed_cut_copper_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_cut_copper_slab_from_waxed_cut_copper_stonecutting']),
)

WAXED_CUT_COPPER_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_cut_copper_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_cut_copper_stairs']),
)

WAXED_CUT_COPPER_STAIRS_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cut_copper_stairs': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cut_copper_stairs')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_cut_copper_stairs_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cut_copper_stairs']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_cut_copper_stairs_from_honeycomb']),
)

WAXED_CUT_COPPER_STAIRS_FROM_WAXED_COPPER_BLOCK_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:waxed_cut_copper_stairs_from_waxed_copper_block_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_copper_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_copper_block')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_copper_block']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_cut_copper_stairs_from_waxed_copper_block_stonecutting']),
)

WAXED_CUT_COPPER_STAIRS_FROM_WAXED_CUT_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_cut_copper_stairs_from_waxed_cut_copper_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_cut_copper_stairs_from_waxed_cut_copper_stonecutting']),
)

WAXED_EXPOSED_CHISELED_COPPER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_exposed_chiseled_copper'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_exposed_cut_copper_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_exposed_cut_copper_slab')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_exposed_cut_copper_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_exposed_chiseled_copper']),
)

WAXED_EXPOSED_CHISELED_COPPER_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_exposed_chiseled_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:exposed_chiseled_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_exposed_chiseled_copper_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_exposed_chiseled_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_exposed_chiseled_copper_from_honeycomb']),
)

WAXED_EXPOSED_CHISELED_COPPER_FROM_WAXED_EXPOSED_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:waxed_exposed_chiseled_copper_from_waxed_exposed_copper_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_exposed_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_exposed_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_exposed_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_exposed_chiseled_copper_from_waxed_exposed_copper_stonecutting']),
)

WAXED_EXPOSED_CHISELED_COPPER_FROM_WAXED_EXPOSED_CUT_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:waxed_exposed_chiseled_copper_from_waxed_exposed_cut_copper_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_exposed_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_exposed_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_exposed_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_exposed_chiseled_copper_from_waxed_exposed_cut_copper_stonecutting']),
)

WAXED_EXPOSED_COPPER_BARS_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_exposed_copper_bars': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:exposed_copper_bars')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_exposed_copper_bars_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_exposed_copper_bars']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_exposed_copper_bars_from_honeycomb']),
)

WAXED_EXPOSED_COPPER_CHAIN_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_exposed_copper_chain': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:exposed_copper_chain')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_exposed_copper_chain_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_exposed_copper_chain']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_exposed_copper_chain_from_honeycomb']),
)

WAXED_EXPOSED_COPPER_CHEST_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_exposed_copper_chest': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:exposed_copper_chest')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_exposed_copper_chest_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_exposed_copper_chest']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_exposed_copper_chest_from_honeycomb']),
)

WAXED_EXPOSED_COPPER_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_exposed_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:exposed_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_exposed_copper_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_exposed_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_exposed_copper_from_honeycomb']),
)

WAXED_EXPOSED_COPPER_GOLEM_STATUE_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_exposed_copper_golem_statue': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:exposed_copper_golem_statue')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_exposed_copper_golem_statue_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_exposed_copper_golem_statue']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_exposed_copper_golem_statue_from_honeycomb']),
)

WAXED_EXPOSED_COPPER_GRATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_exposed_copper_grate'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_exposed_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_exposed_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_exposed_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_exposed_copper_grate']),
)

WAXED_EXPOSED_COPPER_GRATE_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_exposed_copper_grate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:exposed_copper_grate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_exposed_copper_grate_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_exposed_copper_grate']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_exposed_copper_grate_from_honeycomb']),
)

WAXED_EXPOSED_COPPER_GRATE_FROM_WAXED_EXPOSED_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:waxed_exposed_copper_grate_from_waxed_exposed_copper_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_exposed_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_exposed_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_exposed_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_exposed_copper_grate_from_waxed_exposed_copper_stonecutting']),
)

WAXED_EXPOSED_COPPER_LANTERN_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_exposed_copper_lantern': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:exposed_copper_lantern')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_exposed_copper_lantern_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_exposed_copper_lantern']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_exposed_copper_lantern_from_honeycomb']),
)

WAXED_EXPOSED_CUT_COPPER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_exposed_cut_copper'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_exposed_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_exposed_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_exposed_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_exposed_cut_copper']),
)

WAXED_EXPOSED_CUT_COPPER_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_exposed_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:exposed_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_exposed_cut_copper_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_exposed_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_exposed_cut_copper_from_honeycomb']),
)

WAXED_EXPOSED_CUT_COPPER_FROM_WAXED_EXPOSED_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:waxed_exposed_cut_copper_from_waxed_exposed_copper_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_exposed_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_exposed_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_exposed_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_exposed_cut_copper_from_waxed_exposed_copper_stonecutting']),
)

WAXED_EXPOSED_CUT_COPPER_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_exposed_cut_copper_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_exposed_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_exposed_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_exposed_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_exposed_cut_copper_slab']),
)

WAXED_EXPOSED_CUT_COPPER_SLAB_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_exposed_cut_copper_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:exposed_cut_copper_slab')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_exposed_cut_copper_slab_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_exposed_cut_copper_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_exposed_cut_copper_slab_from_honeycomb']),
)

WAXED_EXPOSED_CUT_COPPER_SLAB_FROM_WAXED_EXPOSED_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:waxed_exposed_cut_copper_slab_from_waxed_exposed_copper_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_exposed_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_exposed_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_exposed_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_exposed_cut_copper_slab_from_waxed_exposed_copper_stonecutting']),
)

WAXED_EXPOSED_CUT_COPPER_SLAB_FROM_WAXED_EXPOSED_CUT_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:waxed_exposed_cut_copper_slab_from_waxed_exposed_cut_copper_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_exposed_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_exposed_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_exposed_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_exposed_cut_copper_slab_from_waxed_exposed_cut_copper_stonecutting']),
)

WAXED_EXPOSED_CUT_COPPER_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_exposed_cut_copper_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_exposed_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_exposed_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_exposed_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_exposed_cut_copper_stairs']),
)

WAXED_EXPOSED_CUT_COPPER_STAIRS_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_exposed_cut_copper_stairs': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:exposed_cut_copper_stairs')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_exposed_cut_copper_stairs_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_exposed_cut_copper_stairs']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_exposed_cut_copper_stairs_from_honeycomb']),
)

WAXED_EXPOSED_CUT_COPPER_STAIRS_FROM_WAXED_EXPOSED_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:waxed_exposed_cut_copper_stairs_from_waxed_exposed_copper_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_exposed_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_exposed_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_exposed_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_exposed_cut_copper_stairs_from_waxed_exposed_copper_stonecutting']),
)

WAXED_EXPOSED_CUT_COPPER_STAIRS_FROM_WAXED_EXPOSED_CUT_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:waxed_exposed_cut_copper_stairs_from_waxed_exposed_cut_copper_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_exposed_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_exposed_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_exposed_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_exposed_cut_copper_stairs_from_waxed_exposed_cut_copper_stonecutting']),
)

WAXED_EXPOSED_LIGHTNING_ROD_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_exposed_lightning_rod': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:exposed_lightning_rod')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_exposed_lightning_rod_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_exposed_lightning_rod']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_exposed_lightning_rod_from_honeycomb']),
)

WAXED_LIGHTNING_ROD_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_lightning_rod': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:lightning_rod')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_lightning_rod_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_lightning_rod']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_lightning_rod_from_honeycomb']),
)

WAXED_OXIDIZED_CHISELED_COPPER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_oxidized_chiseled_copper'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_oxidized_cut_copper_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_oxidized_cut_copper_slab')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_oxidized_cut_copper_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_oxidized_chiseled_copper']),
)

WAXED_OXIDIZED_CHISELED_COPPER_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_oxidized_chiseled_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oxidized_chiseled_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_oxidized_chiseled_copper_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_oxidized_chiseled_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_oxidized_chiseled_copper_from_honeycomb']),
)

WAXED_OXIDIZED_CHISELED_COPPER_FROM_WAXED_OXIDIZED_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:waxed_oxidized_chiseled_copper_from_waxed_oxidized_copper_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_oxidized_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_oxidized_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_oxidized_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_oxidized_chiseled_copper_from_waxed_oxidized_copper_stonecutting']),
)

WAXED_OXIDIZED_CHISELED_COPPER_FROM_WAXED_OXIDIZED_CUT_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:waxed_oxidized_chiseled_copper_from_waxed_oxidized_cut_copper_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_oxidized_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_oxidized_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_oxidized_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_oxidized_chiseled_copper_from_waxed_oxidized_cut_copper_stonecutting']),
)

WAXED_OXIDIZED_COPPER_BARS_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_oxidized_copper_bars': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oxidized_copper_bars')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_oxidized_copper_bars_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_oxidized_copper_bars']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_oxidized_copper_bars_from_honeycomb']),
)

WAXED_OXIDIZED_COPPER_CHAIN_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_oxidized_copper_chain': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oxidized_copper_chain')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_oxidized_copper_chain_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_oxidized_copper_chain']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_oxidized_copper_chain_from_honeycomb']),
)

WAXED_OXIDIZED_COPPER_CHEST_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_oxidized_copper_chest': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oxidized_copper_chest')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_oxidized_copper_chest_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_oxidized_copper_chest']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_oxidized_copper_chest_from_honeycomb']),
)

WAXED_OXIDIZED_COPPER_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_oxidized_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oxidized_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_oxidized_copper_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_oxidized_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_oxidized_copper_from_honeycomb']),
)

WAXED_OXIDIZED_COPPER_GOLEM_STATUE_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_oxidized_copper_golem_statue': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oxidized_copper_golem_statue')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_oxidized_copper_golem_statue_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_oxidized_copper_golem_statue']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_oxidized_copper_golem_statue_from_honeycomb']),
)

WAXED_OXIDIZED_COPPER_GRATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_oxidized_copper_grate'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_oxidized_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_oxidized_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_oxidized_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_oxidized_copper_grate']),
)

WAXED_OXIDIZED_COPPER_GRATE_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_oxidized_copper_grate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oxidized_copper_grate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_oxidized_copper_grate_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_oxidized_copper_grate']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_oxidized_copper_grate_from_honeycomb']),
)

WAXED_OXIDIZED_COPPER_GRATE_FROM_WAXED_OXIDIZED_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:waxed_oxidized_copper_grate_from_waxed_oxidized_copper_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_oxidized_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_oxidized_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_oxidized_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_oxidized_copper_grate_from_waxed_oxidized_copper_stonecutting']),
)

WAXED_OXIDIZED_COPPER_LANTERN_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_oxidized_copper_lantern': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oxidized_copper_lantern')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_oxidized_copper_lantern_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_oxidized_copper_lantern']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_oxidized_copper_lantern_from_honeycomb']),
)

WAXED_OXIDIZED_CUT_COPPER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_oxidized_cut_copper'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_oxidized_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_oxidized_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_oxidized_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_oxidized_cut_copper']),
)

WAXED_OXIDIZED_CUT_COPPER_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_oxidized_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oxidized_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_oxidized_cut_copper_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_oxidized_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_oxidized_cut_copper_from_honeycomb']),
)

WAXED_OXIDIZED_CUT_COPPER_FROM_WAXED_OXIDIZED_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:waxed_oxidized_cut_copper_from_waxed_oxidized_copper_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_oxidized_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_oxidized_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_oxidized_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_oxidized_cut_copper_from_waxed_oxidized_copper_stonecutting']),
)

WAXED_OXIDIZED_CUT_COPPER_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_oxidized_cut_copper_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_oxidized_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_oxidized_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_oxidized_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_oxidized_cut_copper_slab']),
)

WAXED_OXIDIZED_CUT_COPPER_SLAB_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_oxidized_cut_copper_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oxidized_cut_copper_slab')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_oxidized_cut_copper_slab_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_oxidized_cut_copper_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_oxidized_cut_copper_slab_from_honeycomb']),
)

WAXED_OXIDIZED_CUT_COPPER_SLAB_FROM_WAXED_OXIDIZED_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:waxed_oxidized_cut_copper_slab_from_waxed_oxidized_copper_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_oxidized_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_oxidized_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_oxidized_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_oxidized_cut_copper_slab_from_waxed_oxidized_copper_stonecutting']),
)

WAXED_OXIDIZED_CUT_COPPER_SLAB_FROM_WAXED_OXIDIZED_CUT_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:waxed_oxidized_cut_copper_slab_from_waxed_oxidized_cut_copper_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_oxidized_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_oxidized_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_oxidized_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_oxidized_cut_copper_slab_from_waxed_oxidized_cut_copper_stonecutting']),
)

WAXED_OXIDIZED_CUT_COPPER_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_oxidized_cut_copper_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_oxidized_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_oxidized_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_oxidized_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_oxidized_cut_copper_stairs']),
)

WAXED_OXIDIZED_CUT_COPPER_STAIRS_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_oxidized_cut_copper_stairs': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oxidized_cut_copper_stairs')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_oxidized_cut_copper_stairs_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_oxidized_cut_copper_stairs']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_oxidized_cut_copper_stairs_from_honeycomb']),
)

WAXED_OXIDIZED_CUT_COPPER_STAIRS_FROM_WAXED_OXIDIZED_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:waxed_oxidized_cut_copper_stairs_from_waxed_oxidized_copper_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_oxidized_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_oxidized_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_oxidized_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_oxidized_cut_copper_stairs_from_waxed_oxidized_copper_stonecutting']),
)

WAXED_OXIDIZED_CUT_COPPER_STAIRS_FROM_WAXED_OXIDIZED_CUT_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:waxed_oxidized_cut_copper_stairs_from_waxed_oxidized_cut_copper_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_oxidized_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_oxidized_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_oxidized_cut_copper']],
    rewards=AdvancementRewards(
        recipes=['minecraft:waxed_oxidized_cut_copper_stairs_from_waxed_oxidized_cut_copper_stonecutting'],
    ),
)

WAXED_OXIDIZED_LIGHTNING_ROD_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_oxidized_lightning_rod': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oxidized_lightning_rod')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_oxidized_lightning_rod_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_oxidized_lightning_rod']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_oxidized_lightning_rod_from_honeycomb']),
)

WAXED_WEATHERED_CHISELED_COPPER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_weathered_chiseled_copper'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_weathered_cut_copper_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_weathered_cut_copper_slab')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_weathered_cut_copper_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_weathered_chiseled_copper']),
)

WAXED_WEATHERED_CHISELED_COPPER_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_weathered_chiseled_copper_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_weathered_chiseled_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:weathered_chiseled_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_weathered_chiseled_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_weathered_chiseled_copper_from_honeycomb']),
)

WAXED_WEATHERED_CHISELED_COPPER_FROM_WAXED_WEATHERED_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:waxed_weathered_chiseled_copper_from_waxed_weathered_copper_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_weathered_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_weathered_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_weathered_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_weathered_chiseled_copper_from_waxed_weathered_copper_stonecutting']),
)

WAXED_WEATHERED_CHISELED_COPPER_FROM_WAXED_WEATHERED_CUT_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:waxed_weathered_chiseled_copper_from_waxed_weathered_cut_copper_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_weathered_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_weathered_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_weathered_cut_copper']],
    rewards=AdvancementRewards(
        recipes=['minecraft:waxed_weathered_chiseled_copper_from_waxed_weathered_cut_copper_stonecutting'],
    ),
)

WAXED_WEATHERED_COPPER_BARS_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_weathered_copper_bars_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_weathered_copper_bars': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:weathered_copper_bars')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_weathered_copper_bars']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_weathered_copper_bars_from_honeycomb']),
)

WAXED_WEATHERED_COPPER_CHAIN_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_weathered_copper_chain_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_weathered_copper_chain': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:weathered_copper_chain')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_weathered_copper_chain']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_weathered_copper_chain_from_honeycomb']),
)

WAXED_WEATHERED_COPPER_CHEST_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_weathered_copper_chest_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_weathered_copper_chest': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:weathered_copper_chest')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_weathered_copper_chest']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_weathered_copper_chest_from_honeycomb']),
)

WAXED_WEATHERED_COPPER_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_weathered_copper_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_weathered_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:weathered_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_weathered_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_weathered_copper_from_honeycomb']),
)

WAXED_WEATHERED_COPPER_GOLEM_STATUE_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_weathered_copper_golem_statue_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_weathered_copper_golem_statue': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:weathered_copper_golem_statue')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_weathered_copper_golem_statue']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_weathered_copper_golem_statue_from_honeycomb']),
)

WAXED_WEATHERED_COPPER_GRATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_weathered_copper_grate'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_weathered_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_weathered_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_weathered_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_weathered_copper_grate']),
)

WAXED_WEATHERED_COPPER_GRATE_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_weathered_copper_grate_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_weathered_copper_grate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:weathered_copper_grate')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_weathered_copper_grate']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_weathered_copper_grate_from_honeycomb']),
)

WAXED_WEATHERED_COPPER_GRATE_FROM_WAXED_WEATHERED_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:waxed_weathered_copper_grate_from_waxed_weathered_copper_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_weathered_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_weathered_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_weathered_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_weathered_copper_grate_from_waxed_weathered_copper_stonecutting']),
)

WAXED_WEATHERED_COPPER_LANTERN_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_weathered_copper_lantern_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_weathered_copper_lantern': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:weathered_copper_lantern')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_weathered_copper_lantern']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_weathered_copper_lantern_from_honeycomb']),
)

WAXED_WEATHERED_CUT_COPPER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_weathered_cut_copper'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_weathered_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_weathered_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_weathered_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_weathered_cut_copper']),
)

WAXED_WEATHERED_CUT_COPPER_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_weathered_cut_copper_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_weathered_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:weathered_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_weathered_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_weathered_cut_copper_from_honeycomb']),
)

WAXED_WEATHERED_CUT_COPPER_FROM_WAXED_WEATHERED_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:waxed_weathered_cut_copper_from_waxed_weathered_copper_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_weathered_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_weathered_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_weathered_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_weathered_cut_copper_from_waxed_weathered_copper_stonecutting']),
)

WAXED_WEATHERED_CUT_COPPER_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_weathered_cut_copper_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_weathered_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_weathered_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_weathered_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_weathered_cut_copper_slab']),
)

WAXED_WEATHERED_CUT_COPPER_SLAB_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_weathered_cut_copper_slab_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_weathered_cut_copper_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:weathered_cut_copper_slab')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_weathered_cut_copper_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_weathered_cut_copper_slab_from_honeycomb']),
)

WAXED_WEATHERED_CUT_COPPER_SLAB_FROM_WAXED_WEATHERED_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:waxed_weathered_cut_copper_slab_from_waxed_weathered_copper_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_weathered_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_weathered_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_weathered_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_weathered_cut_copper_slab_from_waxed_weathered_copper_stonecutting']),
)

WAXED_WEATHERED_CUT_COPPER_SLAB_FROM_WAXED_WEATHERED_CUT_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:waxed_weathered_cut_copper_slab_from_waxed_weathered_cut_copper_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_weathered_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_weathered_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_weathered_cut_copper']],
    rewards=AdvancementRewards(
        recipes=['minecraft:waxed_weathered_cut_copper_slab_from_waxed_weathered_cut_copper_stonecutting'],
    ),
)

WAXED_WEATHERED_CUT_COPPER_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_weathered_cut_copper_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_weathered_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_weathered_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_weathered_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_weathered_cut_copper_stairs']),
)

WAXED_WEATHERED_CUT_COPPER_STAIRS_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_weathered_cut_copper_stairs_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_weathered_cut_copper_stairs': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:weathered_cut_copper_stairs')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_weathered_cut_copper_stairs']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_weathered_cut_copper_stairs_from_honeycomb']),
)

WAXED_WEATHERED_CUT_COPPER_STAIRS_FROM_WAXED_WEATHERED_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:waxed_weathered_cut_copper_stairs_from_waxed_weathered_copper_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_weathered_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_weathered_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_weathered_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_weathered_cut_copper_stairs_from_waxed_weathered_copper_stonecutting']),
)

WAXED_WEATHERED_CUT_COPPER_STAIRS_FROM_WAXED_WEATHERED_CUT_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:waxed_weathered_cut_copper_stairs_from_waxed_weathered_cut_copper_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_weathered_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_weathered_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_weathered_cut_copper']],
    rewards=AdvancementRewards(
        recipes=['minecraft:waxed_weathered_cut_copper_stairs_from_waxed_weathered_cut_copper_stonecutting'],
    ),
)

WAXED_WEATHERED_LIGHTNING_ROD_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_weathered_lightning_rod_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_weathered_lightning_rod': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:weathered_lightning_rod')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_weathered_lightning_rod']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_weathered_lightning_rod_from_honeycomb']),
)

WEATHERED_CHISELED_COPPER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:weathered_cut_copper_slab')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:weathered_chiseled_copper'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:weathered_chiseled_copper']),
)

WEATHERED_CHISELED_COPPER_FROM_WEATHERED_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:weathered_chiseled_copper_from_weathered_copper_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_weathered_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:weathered_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_weathered_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:weathered_chiseled_copper_from_weathered_copper_stonecutting']),
)

WEATHERED_CHISELED_COPPER_FROM_WEATHERED_CUT_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:weathered_chiseled_copper_from_weathered_cut_copper_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_weathered_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:weathered_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_weathered_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:weathered_chiseled_copper_from_weathered_cut_copper_stonecutting']),
)

WEATHERED_COPPER_GRATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:weathered_copper_grate'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_weathered_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:weathered_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_weathered_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:weathered_copper_grate']),
)

WEATHERED_COPPER_GRATE_FROM_WEATHERED_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:weathered_copper_grate_from_weathered_copper_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_weathered_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:weathered_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_weathered_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:weathered_copper_grate_from_weathered_copper_stonecutting']),
)

WEATHERED_CUT_COPPER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:weathered_cut_copper'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_weathered_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:weathered_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_weathered_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:weathered_cut_copper']),
)

WEATHERED_CUT_COPPER_FROM_WEATHERED_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:weathered_cut_copper_from_weathered_copper_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_weathered_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:weathered_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_weathered_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:weathered_cut_copper_from_weathered_copper_stonecutting']),
)

WEATHERED_CUT_COPPER_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:weathered_cut_copper_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_weathered_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:weathered_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_weathered_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:weathered_cut_copper_slab']),
)

WEATHERED_CUT_COPPER_SLAB_FROM_WEATHERED_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:weathered_cut_copper_slab_from_weathered_copper_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_weathered_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:weathered_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_weathered_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:weathered_cut_copper_slab_from_weathered_copper_stonecutting']),
)

WEATHERED_CUT_COPPER_SLAB_FROM_WEATHERED_CUT_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:weathered_cut_copper_slab_from_weathered_cut_copper_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_weathered_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:weathered_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_weathered_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:weathered_cut_copper_slab_from_weathered_cut_copper_stonecutting']),
)

WEATHERED_CUT_COPPER_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:weathered_cut_copper_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_weathered_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:weathered_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_weathered_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:weathered_cut_copper_stairs']),
)

WEATHERED_CUT_COPPER_STAIRS_FROM_WEATHERED_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:weathered_cut_copper_stairs_from_weathered_copper_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_weathered_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:weathered_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_weathered_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:weathered_cut_copper_stairs_from_weathered_copper_stonecutting']),
)

WEATHERED_CUT_COPPER_STAIRS_FROM_WEATHERED_CUT_COPPER_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:weathered_cut_copper_stairs_from_weathered_cut_copper_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_weathered_cut_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:weathered_cut_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_weathered_cut_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:weathered_cut_copper_stairs_from_weathered_cut_copper_stonecutting']),
)

WHITE_CONCRETE_POWDER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gravel': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gravel')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_sand': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sand')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:white_concrete_powder'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sand', 'has_gravel']],
    rewards=AdvancementRewards(recipes=['minecraft:white_concrete_powder']),
)

WHITE_CONCRETE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:white_concrete_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_white_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:white_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_white_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:white_concrete_slab']),
)

WHITE_CONCRETE_SLAB_FROM_WHITE_CONCRETE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:white_concrete_slab_from_white_concrete_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_white_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:white_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_white_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:white_concrete_slab_from_white_concrete_stonecutting']),
)

WHITE_CONCRETE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:white_concrete_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_white_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:white_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_white_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:white_concrete_stairs']),
)

WHITE_CONCRETE_STAIRS_FROM_WHITE_CONCRETE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:white_concrete_stairs_from_white_concrete_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_white_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:white_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_white_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:white_concrete_stairs_from_white_concrete_stonecutting']),
)

WHITE_STAINED_GLASS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glass')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:white_stained_glass'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass']],
    rewards=AdvancementRewards(recipes=['minecraft:white_stained_glass']),
)

WHITE_TERRACOTTA = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_terracotta': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:terracotta')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:white_terracotta'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_terracotta']],
    rewards=AdvancementRewards(recipes=['minecraft:white_terracotta']),
)

WHITE_WOOL_FROM_STRING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_string': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:string')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:white_wool_from_string'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_string']],
    rewards=AdvancementRewards(recipes=['minecraft:white_wool_from_string']),
)

WHITE_WOOL_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:white_wool_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_white_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:white_wool')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_white_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:white_wool_slab']),
)

WHITE_WOOL_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:white_wool_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_white_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:white_wool')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_white_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:white_wool_stairs']),
)

YELLOW_CONCRETE_POWDER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gravel': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gravel')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_sand': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sand')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:yellow_concrete_powder'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sand', 'has_gravel']],
    rewards=AdvancementRewards(recipes=['minecraft:yellow_concrete_powder']),
)

YELLOW_CONCRETE_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:yellow_concrete_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_yellow_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:yellow_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_yellow_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:yellow_concrete_slab']),
)

YELLOW_CONCRETE_SLAB_FROM_YELLOW_CONCRETE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:yellow_concrete_slab_from_yellow_concrete_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_yellow_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:yellow_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_yellow_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:yellow_concrete_slab_from_yellow_concrete_stonecutting']),
)

YELLOW_CONCRETE_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:yellow_concrete_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_yellow_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:yellow_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_yellow_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:yellow_concrete_stairs']),
)

YELLOW_CONCRETE_STAIRS_FROM_YELLOW_CONCRETE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:yellow_concrete_stairs_from_yellow_concrete_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_yellow_concrete': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:yellow_concrete')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_yellow_concrete']],
    rewards=AdvancementRewards(recipes=['minecraft:yellow_concrete_stairs_from_yellow_concrete_stonecutting']),
)

YELLOW_STAINED_GLASS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glass')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:yellow_stained_glass'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass']],
    rewards=AdvancementRewards(recipes=['minecraft:yellow_stained_glass']),
)

YELLOW_TERRACOTTA = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_terracotta': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:terracotta')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:yellow_terracotta'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_terracotta']],
    rewards=AdvancementRewards(recipes=['minecraft:yellow_terracotta']),
)

YELLOW_WOOL_SLAB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:yellow_wool_slab'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_yellow_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:yellow_wool')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_yellow_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:yellow_wool_slab']),
)

YELLOW_WOOL_STAIRS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:yellow_wool_stairs'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_yellow_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:yellow_wool')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_yellow_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:yellow_wool_stairs']),
)
