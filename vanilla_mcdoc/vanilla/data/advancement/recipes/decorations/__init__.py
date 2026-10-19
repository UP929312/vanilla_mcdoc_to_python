"""Vanilla's data/advancement/recipes/decorations/ files"""
from vanilla_mcdoc.data.advancement.Advancement import Advancement
from vanilla_mcdoc.data.advancement.AdvancementCriterion import AdvancementCriterionInventoryChanged, AdvancementCriterionRecipeUnlocked, AdvancementCriterionTick
from vanilla_mcdoc.data.advancement.AdvancementRewards import AdvancementRewards
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.advancement.trigger.InventoryChangeTrigger import InventoryChangeTriggerTypeArg, SlotsStruct
from vanilla_mcdoc.data.advancement.trigger.RecipeUnlockedTrigger import RecipeUnlockedTriggerTypeArg
from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds

ACACIA_FENCE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:acacia_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:acacia_fence'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:acacia_fence']),
)

ACACIA_HANGING_SIGN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stripped_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_acacia_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:acacia_hanging_sign'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stripped_log']],
    rewards=AdvancementRewards(recipes=['minecraft:acacia_hanging_sign']),
)

ACACIA_SHELF = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stripped_acacia_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_acacia_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:acacia_shelf'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stripped_acacia_log']],
    rewards=AdvancementRewards(recipes=['minecraft:acacia_shelf']),
)

ACACIA_SIGN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:acacia_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:acacia_sign'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:acacia_sign']),
)

ANDESITE_WALL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_andesite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:andesite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:andesite_wall'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_andesite']],
    rewards=AdvancementRewards(recipes=['minecraft:andesite_wall']),
)

ANDESITE_WALL_FROM_ANDESITE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_andesite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:andesite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:andesite_wall_from_andesite_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_andesite']],
    rewards=AdvancementRewards(recipes=['minecraft:andesite_wall_from_andesite_stonecutting']),
)

ANVIL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_iron_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:anvil'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_iron_block']],
    rewards=AdvancementRewards(recipes=['minecraft:anvil']),
)

ARMOR_STAND = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stone_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:smooth_stone_slab')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:armor_stand'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stone_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:armor_stand']),
)

BAMBOO_FENCE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:bamboo_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:bamboo_fence'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:bamboo_fence']),
)

BAMBOO_HANGING_SIGN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stripped_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_bamboo_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:bamboo_hanging_sign'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stripped_log']],
    rewards=AdvancementRewards(recipes=['minecraft:bamboo_hanging_sign']),
)

BAMBOO_MOSAIC = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_bamboo_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:bamboo_slab')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:bamboo_mosaic'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_bamboo_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:bamboo_mosaic']),
)

BAMBOO_SHELF = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stripped_bamboo_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_bamboo_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:bamboo_shelf'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stripped_bamboo_block']],
    rewards=AdvancementRewards(recipes=['minecraft:bamboo_shelf']),
)

BAMBOO_SIGN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:bamboo_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:bamboo_sign'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:bamboo_sign']),
)

BARREL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:barrel'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_wood_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:wooden_slabs')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks', 'has_wood_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:barrel']),
)

BEEHIVE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_honeycomb': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:honeycomb')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:beehive'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_honeycomb']],
    rewards=AdvancementRewards(recipes=['minecraft:beehive']),
)

BIRCH_FENCE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:birch_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:birch_fence'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:birch_fence']),
)

BIRCH_HANGING_SIGN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stripped_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_birch_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:birch_hanging_sign'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stripped_log']],
    rewards=AdvancementRewards(recipes=['minecraft:birch_hanging_sign']),
)

BIRCH_SHELF = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stripped_birch_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_birch_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:birch_shelf'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stripped_birch_log']],
    rewards=AdvancementRewards(recipes=['minecraft:birch_shelf']),
)

BIRCH_SIGN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:birch_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:birch_sign'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:birch_sign']),
)

BLACKSTONE_WALL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blackstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blackstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:blackstone_wall'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_blackstone']],
    rewards=AdvancementRewards(recipes=['minecraft:blackstone_wall']),
)

BLACKSTONE_WALL_FROM_BLACKSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blackstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blackstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:blackstone_wall_from_blackstone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_blackstone']],
    rewards=AdvancementRewards(recipes=['minecraft:blackstone_wall_from_blackstone_stonecutting']),
)

BLACK_BANNER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_black_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:black_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:black_banner'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_black_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:black_banner']),
)

BLACK_BED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_black_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:black_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:black_bed'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_black_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:black_bed']),
)

BLACK_CANDLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_black_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:black_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:black_candle'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_black_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:black_candle']),
)

BLACK_CARPET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_black_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:black_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:black_carpet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_black_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:black_carpet']),
)

BLACK_CUSHION = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_black_wool_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:black_wool_slab')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:black_cushion'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_black_wool_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:black_cushion']),
)

BLACK_GLAZED_TERRACOTTA = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_black_terracotta': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:black_terracotta')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:black_glazed_terracotta'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_black_terracotta']],
    rewards=AdvancementRewards(recipes=['minecraft:black_glazed_terracotta']),
)

BLACK_SHULKER_BOX = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_shulker_box': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:shulker_boxes')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:black_shulker_box'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_shulker_box']],
    rewards=AdvancementRewards(recipes=['minecraft:black_shulker_box']),
)

BLACK_STAINED_GLASS_PANE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:black_stained_glass')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:black_stained_glass_pane'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass']],
    rewards=AdvancementRewards(recipes=['minecraft:black_stained_glass_pane']),
)

BLACK_STAINED_GLASS_PANE_FROM_GLASS_PANE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_black_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:black_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_glass_pane': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glass_pane')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:black_stained_glass_pane_from_glass_pane'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass_pane', 'has_black_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:black_stained_glass_pane_from_glass_pane']),
)

BLAST_FURNACE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_smooth_stone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:smooth_stone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:blast_furnace'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_smooth_stone']],
    rewards=AdvancementRewards(recipes=['minecraft:blast_furnace']),
)

BLUE_BANNER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blue_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blue_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:blue_banner'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_blue_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:blue_banner']),
)

BLUE_BED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blue_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blue_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:blue_bed'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_blue_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:blue_bed']),
)

BLUE_CANDLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blue_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blue_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:blue_candle'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_blue_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:blue_candle']),
)

BLUE_CARPET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blue_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blue_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:blue_carpet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_blue_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:blue_carpet']),
)

BLUE_CUSHION = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blue_wool_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blue_wool_slab')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:blue_cushion'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_blue_wool_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:blue_cushion']),
)

BLUE_GLAZED_TERRACOTTA = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blue_terracotta': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blue_terracotta')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:blue_glazed_terracotta'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_blue_terracotta']],
    rewards=AdvancementRewards(recipes=['minecraft:blue_glazed_terracotta']),
)

BLUE_SHULKER_BOX = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_shulker_box': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:shulker_boxes')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:blue_shulker_box'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_shulker_box']],
    rewards=AdvancementRewards(recipes=['minecraft:blue_shulker_box']),
)

BLUE_STAINED_GLASS_PANE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blue_stained_glass')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:blue_stained_glass_pane'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass']],
    rewards=AdvancementRewards(recipes=['minecraft:blue_stained_glass_pane']),
)

BLUE_STAINED_GLASS_PANE_FROM_GLASS_PANE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blue_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blue_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_glass_pane': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glass_pane')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:blue_stained_glass_pane_from_glass_pane'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass_pane', 'has_blue_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:blue_stained_glass_pane_from_glass_pane']),
)

BRICK_WALL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:brick_wall'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:brick_wall']),
)

BRICK_WALL_FROM_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:brick_wall_from_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:brick_wall_from_bricks_stonecutting']),
)

BROWN_BANNER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_brown_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:brown_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:brown_banner'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_brown_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:brown_banner']),
)

BROWN_BED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_brown_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:brown_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:brown_bed'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_brown_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:brown_bed']),
)

BROWN_CANDLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_brown_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:brown_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:brown_candle'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_brown_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:brown_candle']),
)

BROWN_CARPET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_brown_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:brown_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:brown_carpet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_brown_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:brown_carpet']),
)

BROWN_CUSHION = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_brown_wool_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:brown_wool_slab')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:brown_cushion'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_brown_wool_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:brown_cushion']),
)

BROWN_GLAZED_TERRACOTTA = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_brown_terracotta': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:brown_terracotta')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:brown_glazed_terracotta'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_brown_terracotta']],
    rewards=AdvancementRewards(recipes=['minecraft:brown_glazed_terracotta']),
)

BROWN_SHULKER_BOX = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_shulker_box': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:shulker_boxes')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:brown_shulker_box'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_shulker_box']],
    rewards=AdvancementRewards(recipes=['minecraft:brown_shulker_box']),
)

BROWN_STAINED_GLASS_PANE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:brown_stained_glass')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:brown_stained_glass_pane'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass']],
    rewards=AdvancementRewards(recipes=['minecraft:brown_stained_glass_pane']),
)

BROWN_STAINED_GLASS_PANE_FROM_GLASS_PANE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_brown_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:brown_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_glass_pane': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glass_pane')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:brown_stained_glass_pane_from_glass_pane'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass_pane', 'has_brown_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:brown_stained_glass_pane_from_glass_pane']),
)

CAMPFIRE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_coal': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:coals')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_stick': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stick')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:campfire'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stick', 'has_coal']],
    rewards=AdvancementRewards(recipes=['minecraft:campfire']),
)

CANDLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_honeycomb': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:honeycomb')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_string': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:string')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:candle'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_string', 'has_honeycomb']],
    rewards=AdvancementRewards(recipes=['minecraft:candle']),
)

CARTOGRAPHY_TABLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_paper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:paper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cartography_table'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_paper']],
    rewards=AdvancementRewards(recipes=['minecraft:cartography_table']),
)

CHERRY_FENCE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cherry_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cherry_fence'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:cherry_fence']),
)

CHERRY_HANGING_SIGN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stripped_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_cherry_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cherry_hanging_sign'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stripped_log']],
    rewards=AdvancementRewards(recipes=['minecraft:cherry_hanging_sign']),
)

CHERRY_SHELF = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stripped_cherry_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_cherry_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cherry_shelf'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stripped_cherry_log']],
    rewards=AdvancementRewards(recipes=['minecraft:cherry_shelf']),
)

CHERRY_SIGN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cherry_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cherry_sign'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:cherry_sign']),
)

CHEST = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_lots_of_items': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(slots=SlotsStruct(occupied=MinMaxBounds(min=10))),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:chest'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_lots_of_items']],
    rewards=AdvancementRewards(recipes=['minecraft:chest']),
)

CINNABAR_BRICK_WALL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cinnabar_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cinnabar_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cinnabar_brick_wall'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cinnabar_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:cinnabar_brick_wall']),
)

CINNABAR_BRICK_WALL_FROM_CINNABAR_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cinnabar_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cinnabar_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cinnabar_brick_wall_from_cinnabar_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cinnabar_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:cinnabar_brick_wall_from_cinnabar_bricks_stonecutting']),
)

CINNABAR_BRICK_WALL_FROM_CINNABAR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cinnabar': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cinnabar')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cinnabar_brick_wall_from_cinnabar_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cinnabar']],
    rewards=AdvancementRewards(recipes=['minecraft:cinnabar_brick_wall_from_cinnabar_stonecutting']),
)

CINNABAR_BRICK_WALL_FROM_POLISHED_CINNABAR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_cinnabar': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_cinnabar')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cinnabar_brick_wall_from_polished_cinnabar_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_cinnabar']],
    rewards=AdvancementRewards(recipes=['minecraft:cinnabar_brick_wall_from_polished_cinnabar_stonecutting']),
)

CINNABAR_WALL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cinnabar': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cinnabar')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cinnabar_wall'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cinnabar']],
    rewards=AdvancementRewards(recipes=['minecraft:cinnabar_wall']),
)

CINNABAR_WALL_FROM_CINNABAR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cinnabar': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cinnabar')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cinnabar_wall_from_cinnabar_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cinnabar']],
    rewards=AdvancementRewards(recipes=['minecraft:cinnabar_wall_from_cinnabar_stonecutting']),
)

COBBLED_DEEPSLATE_WALL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cobbled_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cobbled_deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cobbled_deepslate_wall'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cobbled_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:cobbled_deepslate_wall']),
)

COBBLED_DEEPSLATE_WALL_FROM_COBBLED_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cobbled_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cobbled_deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cobbled_deepslate_wall_from_cobbled_deepslate_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cobbled_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:cobbled_deepslate_wall_from_cobbled_deepslate_stonecutting']),
)

COBBLED_DEEPSLATE_WALL_FROM_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cobbled_deepslate_wall_from_deepslate_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:cobbled_deepslate_wall_from_deepslate_stonecutting']),
)

COBBLESTONE_WALL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cobblestone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cobblestone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cobblestone_wall'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cobblestone']],
    rewards=AdvancementRewards(recipes=['minecraft:cobblestone_wall']),
)

COBBLESTONE_WALL_FROM_COBBLESTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cobblestone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cobblestone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cobblestone_wall_from_cobblestone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cobblestone']],
    rewards=AdvancementRewards(recipes=['minecraft:cobblestone_wall_from_cobblestone_stonecutting']),
)

COBBLESTONE_WALL_FROM_STONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cobblestone_wall_from_stone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stone']],
    rewards=AdvancementRewards(recipes=['minecraft:cobblestone_wall_from_stone_stonecutting']),
)

COMPOSTER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:composter'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_wood_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:wooden_slabs')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_wood_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:composter']),
)

COPPER_BARS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:copper_bars'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:copper_bars']),
)

COPPER_CHAIN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_copper_nugget': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_nugget')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:copper_chain'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_nugget', 'has_copper_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:copper_chain']),
)

COPPER_CHEST = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_chest': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_chest')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:copper_chest'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_chest']],
    rewards=AdvancementRewards(recipes=['minecraft:copper_chest']),
)

COPPER_LANTERN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_torch': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_torch')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:copper_lantern'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_torch']],
    rewards=AdvancementRewards(recipes=['minecraft:copper_lantern']),
)

COPPER_TORCH = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_nugget': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_nugget')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:copper_torch'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_nugget']],
    rewards=AdvancementRewards(recipes=['minecraft:copper_torch']),
)

CRAFTING_TABLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:crafting_table'),
            trigger='minecraft:recipe_unlocked',
        ),
        'unlock_right_away': AdvancementCriterionTick(trigger='minecraft:tick'),
    },
    requirements=[['has_the_recipe', 'unlock_right_away']],
    rewards=AdvancementRewards(recipes=['minecraft:crafting_table']),
)

CRIMSON_FENCE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:crimson_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:crimson_fence'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:crimson_fence']),
)

CRIMSON_HANGING_SIGN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stripped_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_crimson_stem')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:crimson_hanging_sign'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stripped_log']],
    rewards=AdvancementRewards(recipes=['minecraft:crimson_hanging_sign']),
)

CRIMSON_SHELF = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stripped_crimson_stem': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_crimson_stem')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:crimson_shelf'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stripped_crimson_stem']],
    rewards=AdvancementRewards(recipes=['minecraft:crimson_shelf']),
)

CRIMSON_SIGN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:crimson_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:crimson_sign'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:crimson_sign']),
)

CYAN_BANNER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cyan_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cyan_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cyan_banner'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cyan_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:cyan_banner']),
)

CYAN_BED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cyan_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cyan_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cyan_bed'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cyan_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:cyan_bed']),
)

CYAN_CANDLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cyan_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cyan_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cyan_candle'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cyan_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:cyan_candle']),
)

CYAN_CARPET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cyan_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cyan_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cyan_carpet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cyan_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:cyan_carpet']),
)

CYAN_CUSHION = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cyan_wool_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cyan_wool_slab')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cyan_cushion'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cyan_wool_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:cyan_cushion']),
)

CYAN_GLAZED_TERRACOTTA = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cyan_terracotta': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cyan_terracotta')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cyan_glazed_terracotta'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cyan_terracotta']],
    rewards=AdvancementRewards(recipes=['minecraft:cyan_glazed_terracotta']),
)

CYAN_SHULKER_BOX = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_shulker_box': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:shulker_boxes')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cyan_shulker_box'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_shulker_box']],
    rewards=AdvancementRewards(recipes=['minecraft:cyan_shulker_box']),
)

CYAN_STAINED_GLASS_PANE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cyan_stained_glass')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cyan_stained_glass_pane'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass']],
    rewards=AdvancementRewards(recipes=['minecraft:cyan_stained_glass_pane']),
)

CYAN_STAINED_GLASS_PANE_FROM_GLASS_PANE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cyan_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cyan_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_glass_pane': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glass_pane')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cyan_stained_glass_pane_from_glass_pane'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass_pane', 'has_cyan_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:cyan_stained_glass_pane_from_glass_pane']),
)

DARK_OAK_FENCE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dark_oak_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dark_oak_fence'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:dark_oak_fence']),
)

DARK_OAK_HANGING_SIGN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stripped_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_dark_oak_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dark_oak_hanging_sign'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stripped_log']],
    rewards=AdvancementRewards(recipes=['minecraft:dark_oak_hanging_sign']),
)

DARK_OAK_SHELF = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stripped_dark_oak_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_dark_oak_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dark_oak_shelf'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stripped_dark_oak_log']],
    rewards=AdvancementRewards(recipes=['minecraft:dark_oak_shelf']),
)

DARK_OAK_SIGN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dark_oak_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dark_oak_sign'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:dark_oak_sign']),
)

DECORATED_POT_SIMPLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_brick': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:decorated_pot_ingredients')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:decorated_pot_simple'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_brick']],
    rewards=AdvancementRewards(recipes=['minecraft:decorated_pot_simple']),
)

DEEPSLATE_BRICK_WALL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_brick_wall'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_brick_wall']),
)

DEEPSLATE_BRICK_WALL_FROM_COBBLED_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cobbled_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cobbled_deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_brick_wall_from_cobbled_deepslate_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cobbled_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_brick_wall_from_cobbled_deepslate_stonecutting']),
)

DEEPSLATE_BRICK_WALL_FROM_DEEPSLATE_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_brick_wall_from_deepslate_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_brick_wall_from_deepslate_bricks_stonecutting']),
)

DEEPSLATE_BRICK_WALL_FROM_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_brick_wall_from_deepslate_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_brick_wall_from_deepslate_stonecutting']),
)

DEEPSLATE_BRICK_WALL_FROM_POLISHED_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_brick_wall_from_polished_deepslate_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_brick_wall_from_polished_deepslate_stonecutting']),
)

DEEPSLATE_TILE_WALL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate_tiles': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate_tiles')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_tile_wall'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate_tiles']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_tile_wall']),
)

DEEPSLATE_TILE_WALL_FROM_COBBLED_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cobbled_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cobbled_deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_tile_wall_from_cobbled_deepslate_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cobbled_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_tile_wall_from_cobbled_deepslate_stonecutting']),
)

DEEPSLATE_TILE_WALL_FROM_DEEPSLATE_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_tile_wall_from_deepslate_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_tile_wall_from_deepslate_bricks_stonecutting']),
)

DEEPSLATE_TILE_WALL_FROM_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_tile_wall_from_deepslate_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_tile_wall_from_deepslate_stonecutting']),
)

DEEPSLATE_TILE_WALL_FROM_DEEPSLATE_TILES_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate_tiles': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate_tiles')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_tile_wall_from_deepslate_tiles_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate_tiles']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_tile_wall_from_deepslate_tiles_stonecutting']),
)

DEEPSLATE_TILE_WALL_FROM_POLISHED_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:deepslate_tile_wall_from_polished_deepslate_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:deepslate_tile_wall_from_polished_deepslate_stonecutting']),
)

DIORITE_WALL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_diorite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:diorite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:diorite_wall'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_diorite']],
    rewards=AdvancementRewards(recipes=['minecraft:diorite_wall']),
)

DIORITE_WALL_FROM_DIORITE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_diorite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:diorite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:diorite_wall_from_diorite_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_diorite']],
    rewards=AdvancementRewards(recipes=['minecraft:diorite_wall_from_diorite_stonecutting']),
)

DYE_BLACK_BED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:black_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_black_bed'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_black_bed']),
)

DYE_BLACK_CARPET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:black_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_black_carpet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_black_carpet']),
)

DYE_BLACK_CUSHION = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:black_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_black_cushion'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_black_cushion']),
)

DYE_BLUE_BED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blue_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_blue_bed'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_blue_bed']),
)

DYE_BLUE_CARPET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blue_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_blue_carpet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_blue_carpet']),
)

DYE_BLUE_CUSHION = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blue_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_blue_cushion'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_blue_cushion']),
)

DYE_BROWN_BED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:brown_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_brown_bed'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_brown_bed']),
)

DYE_BROWN_CARPET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:brown_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_brown_carpet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_brown_carpet']),
)

DYE_BROWN_CUSHION = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:brown_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_brown_cushion'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_brown_cushion']),
)

DYE_CYAN_BED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cyan_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_cyan_bed'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_cyan_bed']),
)

DYE_CYAN_CARPET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cyan_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_cyan_carpet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_cyan_carpet']),
)

DYE_CYAN_CUSHION = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cyan_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_cyan_cushion'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_cyan_cushion']),
)

DYE_GRAY_BED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gray_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_gray_bed'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_gray_bed']),
)

DYE_GRAY_CARPET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gray_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_gray_carpet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_gray_carpet']),
)

DYE_GRAY_CUSHION = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gray_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_gray_cushion'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_gray_cushion']),
)

DYE_GREEN_BED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:green_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_green_bed'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_green_bed']),
)

DYE_GREEN_CARPET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:green_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_green_carpet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_green_carpet']),
)

DYE_GREEN_CUSHION = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:green_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_green_cushion'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_green_cushion']),
)

DYE_LIGHT_BLUE_BED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_blue_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_light_blue_bed'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_light_blue_bed']),
)

DYE_LIGHT_BLUE_CARPET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_blue_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_light_blue_carpet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_light_blue_carpet']),
)

DYE_LIGHT_BLUE_CUSHION = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_blue_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_light_blue_cushion'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_light_blue_cushion']),
)

DYE_LIGHT_GRAY_BED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_gray_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_light_gray_bed'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_light_gray_bed']),
)

DYE_LIGHT_GRAY_CARPET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_gray_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_light_gray_carpet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_light_gray_carpet']),
)

DYE_LIGHT_GRAY_CUSHION = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_gray_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_light_gray_cushion'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_light_gray_cushion']),
)

DYE_LIME_BED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:lime_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_lime_bed'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_lime_bed']),
)

DYE_LIME_CARPET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:lime_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_lime_carpet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_lime_carpet']),
)

DYE_LIME_CUSHION = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:lime_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_lime_cushion'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_lime_cushion']),
)

DYE_MAGENTA_BED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:magenta_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_magenta_bed'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_magenta_bed']),
)

DYE_MAGENTA_CARPET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:magenta_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_magenta_carpet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_magenta_carpet']),
)

DYE_MAGENTA_CUSHION = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:magenta_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_magenta_cushion'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_magenta_cushion']),
)

DYE_ORANGE_BED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:orange_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_orange_bed'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_orange_bed']),
)

DYE_ORANGE_CARPET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:orange_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_orange_carpet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_orange_carpet']),
)

DYE_ORANGE_CUSHION = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:orange_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_orange_cushion'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_orange_cushion']),
)

DYE_PINK_BED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pink_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_pink_bed'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_pink_bed']),
)

DYE_PINK_CARPET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pink_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_pink_carpet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_pink_carpet']),
)

DYE_PINK_CUSHION = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pink_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_pink_cushion'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_pink_cushion']),
)

DYE_PURPLE_BED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:purple_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_purple_bed'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_purple_bed']),
)

DYE_PURPLE_CARPET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:purple_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_purple_carpet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_purple_carpet']),
)

DYE_PURPLE_CUSHION = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:purple_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_purple_cushion'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_purple_cushion']),
)

DYE_RED_BED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_red_bed'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_red_bed']),
)

DYE_RED_CARPET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_red_carpet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_red_carpet']),
)

DYE_RED_CUSHION = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_red_cushion'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_red_cushion']),
)

DYE_WHITE_BED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:white_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_white_bed'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_white_bed']),
)

DYE_WHITE_CARPET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:white_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_white_carpet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_white_carpet']),
)

DYE_WHITE_CUSHION = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:white_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_white_cushion'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_white_cushion']),
)

DYE_YELLOW_BED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:yellow_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_yellow_bed'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_yellow_bed']),
)

DYE_YELLOW_CARPET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:yellow_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_yellow_carpet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_yellow_carpet']),
)

DYE_YELLOW_CUSHION = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_needed_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:yellow_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dye_yellow_cushion'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_needed_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:dye_yellow_cushion']),
)

ENCHANTING_TABLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_obsidian': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:obsidian')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:enchanting_table'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_obsidian']],
    rewards=AdvancementRewards(recipes=['minecraft:enchanting_table']),
)

ENDER_CHEST = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_ender_eye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:ender_eye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:ender_chest'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_ender_eye']],
    rewards=AdvancementRewards(recipes=['minecraft:ender_chest']),
)

END_CRYSTAL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_ender_eye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:ender_eye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:end_crystal'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_ender_eye']],
    rewards=AdvancementRewards(recipes=['minecraft:end_crystal']),
)

END_ROD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_chorus_fruit_popped': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:popped_chorus_fruit')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:end_rod'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_chorus_fruit_popped']],
    rewards=AdvancementRewards(recipes=['minecraft:end_rod']),
)

END_STONE_BRICK_WALL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_end_stone_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:end_stone_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:end_stone_brick_wall'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_end_stone_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:end_stone_brick_wall']),
)

END_STONE_BRICK_WALL_FROM_END_STONE_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_end_stone_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:end_stone_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:end_stone_brick_wall_from_end_stone_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_end_stone_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:end_stone_brick_wall_from_end_stone_bricks_stonecutting']),
)

END_STONE_BRICK_WALL_FROM_END_STONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_end_stone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:end_stone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:end_stone_brick_wall_from_end_stone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_end_stone']],
    rewards=AdvancementRewards(recipes=['minecraft:end_stone_brick_wall_from_end_stone_stonecutting']),
)

FLETCHING_TABLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_flint': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:flint')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:fletching_table'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_flint']],
    rewards=AdvancementRewards(recipes=['minecraft:fletching_table']),
)

FLOWER_POT = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_brick': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:brick')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:flower_pot'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_brick']],
    rewards=AdvancementRewards(recipes=['minecraft:flower_pot']),
)

FURNACE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cobblestone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:stone_crafting_materials')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:furnace'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cobblestone']],
    rewards=AdvancementRewards(recipes=['minecraft:furnace']),
)

GLASS_PANE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glass')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:glass_pane'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass']],
    rewards=AdvancementRewards(recipes=['minecraft:glass_pane']),
)

GLOW_ITEM_FRAME = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glow_ink_sac': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glow_ink_sac')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_item_frame': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:item_frame')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:glow_item_frame'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_item_frame', 'has_glow_ink_sac']],
    rewards=AdvancementRewards(recipes=['minecraft:glow_item_frame']),
)

GOLDEN_DANDELION = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_dandelion': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dandelion')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_gold_nugget': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gold_nugget')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:golden_dandelion'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_gold_nugget', 'has_dandelion']],
    rewards=AdvancementRewards(recipes=['minecraft:golden_dandelion']),
)

GRANITE_WALL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_granite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:granite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:granite_wall'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_granite']],
    rewards=AdvancementRewards(recipes=['minecraft:granite_wall']),
)

GRANITE_WALL_FROM_GRANITE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_granite': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:granite')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:granite_wall_from_granite_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_granite']],
    rewards=AdvancementRewards(recipes=['minecraft:granite_wall_from_granite_stonecutting']),
)

GRAY_BANNER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gray_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gray_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:gray_banner'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_gray_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:gray_banner']),
)

GRAY_BED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gray_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gray_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:gray_bed'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_gray_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:gray_bed']),
)

GRAY_CANDLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gray_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gray_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:gray_candle'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_gray_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:gray_candle']),
)

GRAY_CARPET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gray_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gray_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:gray_carpet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_gray_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:gray_carpet']),
)

GRAY_CUSHION = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gray_wool_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gray_wool_slab')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:gray_cushion'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_gray_wool_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:gray_cushion']),
)

GRAY_GLAZED_TERRACOTTA = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gray_terracotta': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gray_terracotta')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:gray_glazed_terracotta'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_gray_terracotta']],
    rewards=AdvancementRewards(recipes=['minecraft:gray_glazed_terracotta']),
)

GRAY_SHULKER_BOX = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_shulker_box': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:shulker_boxes')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:gray_shulker_box'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_shulker_box']],
    rewards=AdvancementRewards(recipes=['minecraft:gray_shulker_box']),
)

GRAY_STAINED_GLASS_PANE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gray_stained_glass')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:gray_stained_glass_pane'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass']],
    rewards=AdvancementRewards(recipes=['minecraft:gray_stained_glass_pane']),
)

GRAY_STAINED_GLASS_PANE_FROM_GLASS_PANE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass_pane': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glass_pane')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_gray_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gray_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:gray_stained_glass_pane_from_glass_pane'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass_pane', 'has_gray_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:gray_stained_glass_pane_from_glass_pane']),
)

GREEN_BANNER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_green_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:green_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:green_banner'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_green_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:green_banner']),
)

GREEN_BED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_green_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:green_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:green_bed'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_green_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:green_bed']),
)

GREEN_CANDLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_green_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:green_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:green_candle'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_green_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:green_candle']),
)

GREEN_CARPET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_green_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:green_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:green_carpet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_green_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:green_carpet']),
)

GREEN_CUSHION = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_green_wool_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:green_wool_slab')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:green_cushion'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_green_wool_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:green_cushion']),
)

GREEN_GLAZED_TERRACOTTA = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_green_terracotta': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:green_terracotta')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:green_glazed_terracotta'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_green_terracotta']],
    rewards=AdvancementRewards(recipes=['minecraft:green_glazed_terracotta']),
)

GREEN_SHULKER_BOX = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_shulker_box': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:shulker_boxes')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:green_shulker_box'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_shulker_box']],
    rewards=AdvancementRewards(recipes=['minecraft:green_shulker_box']),
)

GREEN_STAINED_GLASS_PANE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:green_stained_glass')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:green_stained_glass_pane'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass']],
    rewards=AdvancementRewards(recipes=['minecraft:green_stained_glass_pane']),
)

GREEN_STAINED_GLASS_PANE_FROM_GLASS_PANE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass_pane': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glass_pane')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_green_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:green_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:green_stained_glass_pane_from_glass_pane'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass_pane', 'has_green_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:green_stained_glass_pane_from_glass_pane']),
)

GRINDSTONE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stone_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stone_slab')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:grindstone'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stone_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:grindstone']),
)

HONEYCOMB_BLOCK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_honeycomb': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:honeycomb')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:honeycomb_block'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_honeycomb']],
    rewards=AdvancementRewards(recipes=['minecraft:honeycomb_block']),
)

IRON_BARS = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_iron_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:iron_bars'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_iron_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:iron_bars']),
)

IRON_CHAIN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_iron_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_iron_nugget': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_nugget')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:iron_chain'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_iron_nugget', 'has_iron_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:iron_chain']),
)

ITEM_FRAME = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_leather': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:leather')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:item_frame'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_leather']],
    rewards=AdvancementRewards(recipes=['minecraft:item_frame']),
)

JUKEBOX = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_diamond': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:diamond')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:jukebox'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_diamond']],
    rewards=AdvancementRewards(recipes=['minecraft:jukebox']),
)

JUNGLE_FENCE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:jungle_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:jungle_fence'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:jungle_fence']),
)

JUNGLE_HANGING_SIGN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stripped_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_jungle_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:jungle_hanging_sign'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stripped_log']],
    rewards=AdvancementRewards(recipes=['minecraft:jungle_hanging_sign']),
)

JUNGLE_SHELF = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stripped_jungle_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_jungle_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:jungle_shelf'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stripped_jungle_log']],
    rewards=AdvancementRewards(recipes=['minecraft:jungle_shelf']),
)

JUNGLE_SIGN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:jungle_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:jungle_sign'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:jungle_sign']),
)

LADDER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stick': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stick')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:ladder'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stick']],
    rewards=AdvancementRewards(recipes=['minecraft:ladder']),
)

LANTERN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_iron_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_iron_nugget': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_nugget')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:lantern'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_iron_nugget', 'has_iron_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:lantern']),
)

LIGHT_BLUE_BANNER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_light_blue_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_blue_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_blue_banner'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_light_blue_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:light_blue_banner']),
)

LIGHT_BLUE_BED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_light_blue_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_blue_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_blue_bed'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_light_blue_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:light_blue_bed']),
)

LIGHT_BLUE_CANDLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_light_blue_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_blue_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_blue_candle'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_light_blue_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:light_blue_candle']),
)

LIGHT_BLUE_CARPET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_light_blue_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_blue_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_blue_carpet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_light_blue_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:light_blue_carpet']),
)

LIGHT_BLUE_CUSHION = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_light_blue_wool_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_blue_wool_slab')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_blue_cushion'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_light_blue_wool_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:light_blue_cushion']),
)

LIGHT_BLUE_GLAZED_TERRACOTTA = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_light_blue_terracotta': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_blue_terracotta')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_blue_glazed_terracotta'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_light_blue_terracotta']],
    rewards=AdvancementRewards(recipes=['minecraft:light_blue_glazed_terracotta']),
)

LIGHT_BLUE_SHULKER_BOX = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_shulker_box': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:shulker_boxes')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_blue_shulker_box'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_shulker_box']],
    rewards=AdvancementRewards(recipes=['minecraft:light_blue_shulker_box']),
)

LIGHT_BLUE_STAINED_GLASS_PANE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_blue_stained_glass')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_blue_stained_glass_pane'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass']],
    rewards=AdvancementRewards(recipes=['minecraft:light_blue_stained_glass_pane']),
)

LIGHT_BLUE_STAINED_GLASS_PANE_FROM_GLASS_PANE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass_pane': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glass_pane')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_light_blue_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_blue_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_blue_stained_glass_pane_from_glass_pane'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass_pane', 'has_light_blue_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:light_blue_stained_glass_pane_from_glass_pane']),
)

LIGHT_GRAY_BANNER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_light_gray_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_gray_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_gray_banner'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_light_gray_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:light_gray_banner']),
)

LIGHT_GRAY_BED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_light_gray_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_gray_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_gray_bed'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_light_gray_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:light_gray_bed']),
)

LIGHT_GRAY_CANDLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_light_gray_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_gray_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_gray_candle'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_light_gray_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:light_gray_candle']),
)

LIGHT_GRAY_CARPET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_light_gray_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_gray_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_gray_carpet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_light_gray_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:light_gray_carpet']),
)

LIGHT_GRAY_CUSHION = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_light_gray_wool_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_gray_wool_slab')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_gray_cushion'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_light_gray_wool_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:light_gray_cushion']),
)

LIGHT_GRAY_GLAZED_TERRACOTTA = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_light_gray_terracotta': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_gray_terracotta')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_gray_glazed_terracotta'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_light_gray_terracotta']],
    rewards=AdvancementRewards(recipes=['minecraft:light_gray_glazed_terracotta']),
)

LIGHT_GRAY_SHULKER_BOX = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_shulker_box': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:shulker_boxes')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_gray_shulker_box'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_shulker_box']],
    rewards=AdvancementRewards(recipes=['minecraft:light_gray_shulker_box']),
)

LIGHT_GRAY_STAINED_GLASS_PANE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_gray_stained_glass')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_gray_stained_glass_pane'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass']],
    rewards=AdvancementRewards(recipes=['minecraft:light_gray_stained_glass_pane']),
)

LIGHT_GRAY_STAINED_GLASS_PANE_FROM_GLASS_PANE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass_pane': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glass_pane')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_light_gray_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:light_gray_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_gray_stained_glass_pane_from_glass_pane'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass_pane', 'has_light_gray_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:light_gray_stained_glass_pane_from_glass_pane']),
)

LIME_BANNER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_lime_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:lime_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:lime_banner'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_lime_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:lime_banner']),
)

LIME_BED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_lime_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:lime_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:lime_bed'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_lime_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:lime_bed']),
)

LIME_CANDLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_lime_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:lime_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:lime_candle'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_lime_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:lime_candle']),
)

LIME_CARPET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_lime_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:lime_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:lime_carpet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_lime_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:lime_carpet']),
)

LIME_CUSHION = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_lime_wool_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:lime_wool_slab')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:lime_cushion'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_lime_wool_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:lime_cushion']),
)

LIME_GLAZED_TERRACOTTA = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_lime_terracotta': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:lime_terracotta')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:lime_glazed_terracotta'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_lime_terracotta']],
    rewards=AdvancementRewards(recipes=['minecraft:lime_glazed_terracotta']),
)

LIME_SHULKER_BOX = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_shulker_box': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:shulker_boxes')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:lime_shulker_box'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_shulker_box']],
    rewards=AdvancementRewards(recipes=['minecraft:lime_shulker_box']),
)

LIME_STAINED_GLASS_PANE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:lime_stained_glass')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:lime_stained_glass_pane'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass']],
    rewards=AdvancementRewards(recipes=['minecraft:lime_stained_glass_pane']),
)

LIME_STAINED_GLASS_PANE_FROM_GLASS_PANE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass_pane': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glass_pane')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_lime_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:lime_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:lime_stained_glass_pane_from_glass_pane'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass_pane', 'has_lime_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:lime_stained_glass_pane_from_glass_pane']),
)

LODESTONE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_iron_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_lodestone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:lodestone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:lodestone'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_iron_ingot', 'has_lodestone']],
    rewards=AdvancementRewards(recipes=['minecraft:lodestone']),
)

LOOM = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_string': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:string')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:loom'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_string']],
    rewards=AdvancementRewards(recipes=['minecraft:loom']),
)

MAGENTA_BANNER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_magenta_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:magenta_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:magenta_banner'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_magenta_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:magenta_banner']),
)

MAGENTA_BED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_magenta_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:magenta_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:magenta_bed'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_magenta_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:magenta_bed']),
)

MAGENTA_CANDLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_magenta_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:magenta_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:magenta_candle'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_magenta_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:magenta_candle']),
)

MAGENTA_CARPET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_magenta_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:magenta_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:magenta_carpet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_magenta_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:magenta_carpet']),
)

MAGENTA_CUSHION = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_magenta_wool_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:magenta_wool_slab')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:magenta_cushion'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_magenta_wool_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:magenta_cushion']),
)

MAGENTA_GLAZED_TERRACOTTA = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_magenta_terracotta': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:magenta_terracotta')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:magenta_glazed_terracotta'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_magenta_terracotta']],
    rewards=AdvancementRewards(recipes=['minecraft:magenta_glazed_terracotta']),
)

MAGENTA_SHULKER_BOX = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_shulker_box': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:shulker_boxes')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:magenta_shulker_box'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_shulker_box']],
    rewards=AdvancementRewards(recipes=['minecraft:magenta_shulker_box']),
)

MAGENTA_STAINED_GLASS_PANE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:magenta_stained_glass')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:magenta_stained_glass_pane'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass']],
    rewards=AdvancementRewards(recipes=['minecraft:magenta_stained_glass_pane']),
)

MAGENTA_STAINED_GLASS_PANE_FROM_GLASS_PANE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass_pane': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glass_pane')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_magenta_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:magenta_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:magenta_stained_glass_pane_from_glass_pane'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass_pane', 'has_magenta_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:magenta_stained_glass_pane_from_glass_pane']),
)

MANGROVE_FENCE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:mangrove_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:mangrove_fence'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:mangrove_fence']),
)

MANGROVE_HANGING_SIGN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stripped_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_mangrove_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:mangrove_hanging_sign'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stripped_log']],
    rewards=AdvancementRewards(recipes=['minecraft:mangrove_hanging_sign']),
)

MANGROVE_SHELF = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stripped_mangrove_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_mangrove_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:mangrove_shelf'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stripped_mangrove_log']],
    rewards=AdvancementRewards(recipes=['minecraft:mangrove_shelf']),
)

MANGROVE_SIGN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:mangrove_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:mangrove_sign'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:mangrove_sign']),
)

MOSSY_COBBLESTONE_WALL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_mossy_cobblestone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:mossy_cobblestone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:mossy_cobblestone_wall'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_mossy_cobblestone']],
    rewards=AdvancementRewards(recipes=['minecraft:mossy_cobblestone_wall']),
)

MOSSY_COBBLESTONE_WALL_FROM_MOSSY_COBBLESTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_mossy_cobblestone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:mossy_cobblestone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:mossy_cobblestone_wall_from_mossy_cobblestone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_mossy_cobblestone']],
    rewards=AdvancementRewards(recipes=['minecraft:mossy_cobblestone_wall_from_mossy_cobblestone_stonecutting']),
)

MOSSY_STONE_BRICK_WALL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_mossy_stone_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:mossy_stone_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:mossy_stone_brick_wall'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_mossy_stone_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:mossy_stone_brick_wall']),
)

MOSSY_STONE_BRICK_WALL_FROM_MOSSY_STONE_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_mossy_stone_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:mossy_stone_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:mossy_stone_brick_wall_from_mossy_stone_bricks_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_mossy_stone_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:mossy_stone_brick_wall_from_mossy_stone_bricks_stonecutting']),
)

MOSS_CARPET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_moss_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:moss_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:moss_carpet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_moss_block']],
    rewards=AdvancementRewards(recipes=['minecraft:moss_carpet']),
)

MUD_BRICK_WALL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_mud_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:mud_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:mud_brick_wall'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_mud_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:mud_brick_wall']),
)

MUD_BRICK_WALL_FROM_MUD_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_mud_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:mud_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:mud_brick_wall_from_mud_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_mud_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:mud_brick_wall_from_mud_bricks_stonecutting']),
)

NETHER_BRICK_FENCE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_nether_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:nether_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:nether_brick_fence'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_nether_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:nether_brick_fence']),
)

NETHER_BRICK_WALL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_nether_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:nether_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:nether_brick_wall'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_nether_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:nether_brick_wall']),
)

NETHER_BRICK_WALL_FROM_NETHER_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_nether_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:nether_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:nether_brick_wall_from_nether_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_nether_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:nether_brick_wall_from_nether_bricks_stonecutting']),
)

OAK_FENCE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oak_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:oak_fence'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:oak_fence']),
)

OAK_HANGING_SIGN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stripped_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_oak_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:oak_hanging_sign'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stripped_log']],
    rewards=AdvancementRewards(recipes=['minecraft:oak_hanging_sign']),
)

OAK_SHELF = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stripped_oak_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_oak_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:oak_shelf'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stripped_oak_log']],
    rewards=AdvancementRewards(recipes=['minecraft:oak_shelf']),
)

OAK_SIGN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oak_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:oak_sign'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:oak_sign']),
)

ORANGE_BANNER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_orange_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:orange_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:orange_banner'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_orange_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:orange_banner']),
)

ORANGE_BED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_orange_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:orange_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:orange_bed'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_orange_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:orange_bed']),
)

ORANGE_CANDLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_orange_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:orange_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:orange_candle'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_orange_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:orange_candle']),
)

ORANGE_CARPET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_orange_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:orange_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:orange_carpet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_orange_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:orange_carpet']),
)

ORANGE_CUSHION = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_orange_wool_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:orange_wool_slab')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:orange_cushion'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_orange_wool_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:orange_cushion']),
)

ORANGE_GLAZED_TERRACOTTA = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_orange_terracotta': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:orange_terracotta')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:orange_glazed_terracotta'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_orange_terracotta']],
    rewards=AdvancementRewards(recipes=['minecraft:orange_glazed_terracotta']),
)

ORANGE_SHULKER_BOX = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_shulker_box': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:shulker_boxes')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:orange_shulker_box'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_shulker_box']],
    rewards=AdvancementRewards(recipes=['minecraft:orange_shulker_box']),
)

ORANGE_STAINED_GLASS_PANE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:orange_stained_glass')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:orange_stained_glass_pane'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass']],
    rewards=AdvancementRewards(recipes=['minecraft:orange_stained_glass_pane']),
)

ORANGE_STAINED_GLASS_PANE_FROM_GLASS_PANE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass_pane': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glass_pane')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_orange_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:orange_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:orange_stained_glass_pane_from_glass_pane'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass_pane', 'has_orange_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:orange_stained_glass_pane_from_glass_pane']),
)

PAINTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:painting'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:wool')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:painting']),
)

PALE_MOSS_CARPET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_pale_moss_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pale_moss_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pale_moss_carpet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_pale_moss_block']],
    rewards=AdvancementRewards(recipes=['minecraft:pale_moss_carpet']),
)

PALE_OAK_FENCE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pale_oak_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pale_oak_fence'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:pale_oak_fence']),
)

PALE_OAK_HANGING_SIGN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stripped_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_pale_oak_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pale_oak_hanging_sign'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stripped_log']],
    rewards=AdvancementRewards(recipes=['minecraft:pale_oak_hanging_sign']),
)

PALE_OAK_SHELF = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stripped_pale_oak_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_pale_oak_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pale_oak_shelf'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stripped_pale_oak_log']],
    rewards=AdvancementRewards(recipes=['minecraft:pale_oak_shelf']),
)

PALE_OAK_SIGN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pale_oak_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pale_oak_sign'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:pale_oak_sign']),
)

PINK_BANNER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_pink_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pink_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pink_banner'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_pink_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:pink_banner']),
)

PINK_BED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_pink_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pink_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pink_bed'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_pink_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:pink_bed']),
)

PINK_CANDLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_pink_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pink_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pink_candle'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_pink_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:pink_candle']),
)

PINK_CARPET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_pink_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pink_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pink_carpet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_pink_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:pink_carpet']),
)

PINK_CUSHION = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_pink_wool_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pink_wool_slab')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pink_cushion'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_pink_wool_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:pink_cushion']),
)

PINK_GLAZED_TERRACOTTA = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_pink_terracotta': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pink_terracotta')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pink_glazed_terracotta'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_pink_terracotta']],
    rewards=AdvancementRewards(recipes=['minecraft:pink_glazed_terracotta']),
)

PINK_SHULKER_BOX = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_shulker_box': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:shulker_boxes')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pink_shulker_box'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_shulker_box']],
    rewards=AdvancementRewards(recipes=['minecraft:pink_shulker_box']),
)

PINK_STAINED_GLASS_PANE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pink_stained_glass')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pink_stained_glass_pane'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass']],
    rewards=AdvancementRewards(recipes=['minecraft:pink_stained_glass_pane']),
)

PINK_STAINED_GLASS_PANE_FROM_GLASS_PANE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass_pane': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glass_pane')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_pink_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pink_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pink_stained_glass_pane_from_glass_pane'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass_pane', 'has_pink_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:pink_stained_glass_pane_from_glass_pane']),
)

POLISHED_BLACKSTONE_BRICK_WALL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_blackstone_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_blackstone_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_blackstone_brick_wall'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_blackstone_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_blackstone_brick_wall']),
)

POLISHED_BLACKSTONE_BRICK_WALL_FROM_BLACKSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blackstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blackstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:polished_blackstone_brick_wall_from_blackstone_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_blackstone']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_blackstone_brick_wall_from_blackstone_stonecutting']),
)

POLISHED_BLACKSTONE_BRICK_WALL_FROM_POLISHED_BLACKSTONE_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_blackstone_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_blackstone_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:polished_blackstone_brick_wall_from_polished_blackstone_bricks_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_blackstone_bricks']],
    rewards=AdvancementRewards(
        recipes=['minecraft:polished_blackstone_brick_wall_from_polished_blackstone_bricks_stonecutting'],
    ),
)

POLISHED_BLACKSTONE_BRICK_WALL_FROM_POLISHED_BLACKSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_blackstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_blackstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:polished_blackstone_brick_wall_from_polished_blackstone_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_blackstone']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_blackstone_brick_wall_from_polished_blackstone_stonecutting']),
)

POLISHED_BLACKSTONE_WALL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_blackstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_blackstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_blackstone_wall'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_blackstone']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_blackstone_wall']),
)

POLISHED_BLACKSTONE_WALL_FROM_BLACKSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blackstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blackstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_blackstone_wall_from_blackstone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_blackstone']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_blackstone_wall_from_blackstone_stonecutting']),
)

POLISHED_BLACKSTONE_WALL_FROM_POLISHED_BLACKSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_blackstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_blackstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:polished_blackstone_wall_from_polished_blackstone_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_blackstone']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_blackstone_wall_from_polished_blackstone_stonecutting']),
)

POLISHED_CINNABAR_WALL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_cinnabar': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_cinnabar')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_cinnabar_wall'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_cinnabar']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_cinnabar_wall']),
)

POLISHED_CINNABAR_WALL_FROM_CINNABAR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cinnabar': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cinnabar')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_cinnabar_wall_from_cinnabar_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cinnabar']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_cinnabar_wall_from_cinnabar_stonecutting']),
)

POLISHED_CINNABAR_WALL_FROM_POLISHED_CINNABAR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_cinnabar': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_cinnabar')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_cinnabar_wall_from_polished_cinnabar_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_cinnabar']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_cinnabar_wall_from_polished_cinnabar_stonecutting']),
)

POLISHED_DEEPSLATE_WALL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_deepslate_wall'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_deepslate_wall']),
)

POLISHED_DEEPSLATE_WALL_FROM_COBBLED_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cobbled_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cobbled_deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:polished_deepslate_wall_from_cobbled_deepslate_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cobbled_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_deepslate_wall_from_cobbled_deepslate_stonecutting']),
)

POLISHED_DEEPSLATE_WALL_FROM_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_deepslate_wall_from_deepslate_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_deepslate_wall_from_deepslate_stonecutting']),
)

POLISHED_DEEPSLATE_WALL_FROM_POLISHED_DEEPSLATE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_deepslate': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_deepslate')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(
                recipes='minecraft:polished_deepslate_wall_from_polished_deepslate_stonecutting',
            ),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_deepslate']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_deepslate_wall_from_polished_deepslate_stonecutting']),
)

POLISHED_SULFUR_WALL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_sulfur': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_sulfur')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_sulfur_wall'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_sulfur']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_sulfur_wall']),
)

POLISHED_SULFUR_WALL_FROM_POLISHED_SULFUR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_sulfur': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_sulfur')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_sulfur_wall_from_polished_sulfur_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_sulfur']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_sulfur_wall_from_polished_sulfur_stonecutting']),
)

POLISHED_SULFUR_WALL_FROM_SULFUR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sulfur': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sulfur')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_sulfur_wall_from_sulfur_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sulfur']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_sulfur_wall_from_sulfur_stonecutting']),
)

POLISHED_TUFF_WALL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_tuff': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_tuff')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_tuff_wall'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_tuff']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_tuff_wall']),
)

POLISHED_TUFF_WALL_FROM_POLISHED_TUFF_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_tuff': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_tuff')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_tuff_wall_from_polished_tuff_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_tuff']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_tuff_wall_from_polished_tuff_stonecutting']),
)

POLISHED_TUFF_WALL_FROM_TUFF_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_tuff_wall_from_tuff_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_tuff': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:tuff')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_tuff']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_tuff_wall_from_tuff_stonecutting']),
)

POPLAR_FENCE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:poplar_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:poplar_fence'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:poplar_fence']),
)

POPLAR_HANGING_SIGN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stripped_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_poplar_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:poplar_hanging_sign'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stripped_log']],
    rewards=AdvancementRewards(recipes=['minecraft:poplar_hanging_sign']),
)

POPLAR_SHELF = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stripped_poplar_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_poplar_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:poplar_shelf'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stripped_poplar_log']],
    rewards=AdvancementRewards(recipes=['minecraft:poplar_shelf']),
)

POPLAR_SIGN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:poplar_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:poplar_sign'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:poplar_sign']),
)

PRISMARINE_WALL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_prismarine': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:prismarine')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:prismarine_wall'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_prismarine']],
    rewards=AdvancementRewards(recipes=['minecraft:prismarine_wall']),
)

PRISMARINE_WALL_FROM_PRISMARINE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_prismarine': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:prismarine')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:prismarine_wall_from_prismarine_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_prismarine']],
    rewards=AdvancementRewards(recipes=['minecraft:prismarine_wall_from_prismarine_stonecutting']),
)

PURPLE_BANNER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_purple_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:purple_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:purple_banner'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_purple_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:purple_banner']),
)

PURPLE_BED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_purple_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:purple_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:purple_bed'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_purple_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:purple_bed']),
)

PURPLE_CANDLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_purple_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:purple_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:purple_candle'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_purple_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:purple_candle']),
)

PURPLE_CARPET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_purple_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:purple_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:purple_carpet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_purple_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:purple_carpet']),
)

PURPLE_CUSHION = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_purple_wool_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:purple_wool_slab')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:purple_cushion'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_purple_wool_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:purple_cushion']),
)

PURPLE_GLAZED_TERRACOTTA = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_purple_terracotta': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:purple_terracotta')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:purple_glazed_terracotta'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_purple_terracotta']],
    rewards=AdvancementRewards(recipes=['minecraft:purple_glazed_terracotta']),
)

PURPLE_SHULKER_BOX = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_shulker_box': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:shulker_boxes')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:purple_shulker_box'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_shulker_box']],
    rewards=AdvancementRewards(recipes=['minecraft:purple_shulker_box']),
)

PURPLE_STAINED_GLASS_PANE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:purple_stained_glass')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:purple_stained_glass_pane'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass']],
    rewards=AdvancementRewards(recipes=['minecraft:purple_stained_glass_pane']),
)

PURPLE_STAINED_GLASS_PANE_FROM_GLASS_PANE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass_pane': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glass_pane')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_purple_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:purple_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:purple_stained_glass_pane_from_glass_pane'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass_pane', 'has_purple_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:purple_stained_glass_pane_from_glass_pane']),
)

RED_BANNER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_red_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:red_banner'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_red_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:red_banner']),
)

RED_BED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_red_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:red_bed'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_red_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:red_bed']),
)

RED_CANDLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_red_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:red_candle'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_red_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:red_candle']),
)

RED_CARPET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_red_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_wool')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:red_carpet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_red_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:red_carpet']),
)

RED_CUSHION = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_red_wool_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_wool_slab')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:red_cushion'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_red_wool_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:red_cushion']),
)

RED_GLAZED_TERRACOTTA = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_red_terracotta': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_terracotta')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:red_glazed_terracotta'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_red_terracotta']],
    rewards=AdvancementRewards(recipes=['minecraft:red_glazed_terracotta']),
)

RED_NETHER_BRICK_WALL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_red_nether_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_nether_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:red_nether_brick_wall'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_red_nether_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:red_nether_brick_wall']),
)

RED_NETHER_BRICK_WALL_FROM_RED_NETHER_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_red_nether_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_nether_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:red_nether_brick_wall_from_red_nether_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_red_nether_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:red_nether_brick_wall_from_red_nether_bricks_stonecutting']),
)

RED_SANDSTONE_WALL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_red_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:red_sandstone_wall'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_red_sandstone']],
    rewards=AdvancementRewards(recipes=['minecraft:red_sandstone_wall']),
)

RED_SANDSTONE_WALL_FROM_RED_SANDSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_red_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:red_sandstone_wall_from_red_sandstone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_red_sandstone']],
    rewards=AdvancementRewards(recipes=['minecraft:red_sandstone_wall_from_red_sandstone_stonecutting']),
)

RED_SHULKER_BOX = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_shulker_box': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:shulker_boxes')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:red_shulker_box'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_shulker_box']],
    rewards=AdvancementRewards(recipes=['minecraft:red_shulker_box']),
)

RED_STAINED_GLASS_PANE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_stained_glass')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:red_stained_glass_pane'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass']],
    rewards=AdvancementRewards(recipes=['minecraft:red_stained_glass_pane']),
)

RED_STAINED_GLASS_PANE_FROM_GLASS_PANE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass_pane': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glass_pane')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_red_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_dye')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:red_stained_glass_pane_from_glass_pane'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass_pane', 'has_red_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:red_stained_glass_pane_from_glass_pane']),
)

RESIN_BRICK_WALL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_resin_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:resin_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:resin_brick_wall'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_resin_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:resin_brick_wall']),
)

RESIN_BRICK_WALL_FROM_RESIN_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_resin_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:resin_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:resin_brick_wall_from_resin_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_resin_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:resin_brick_wall_from_resin_bricks_stonecutting']),
)

RESPAWN_ANCHOR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_obsidian': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:crying_obsidian')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:respawn_anchor'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_obsidian']],
    rewards=AdvancementRewards(recipes=['minecraft:respawn_anchor']),
)

SANDSTONE_WALL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:sandstone_wall'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sandstone']],
    rewards=AdvancementRewards(recipes=['minecraft:sandstone_wall']),
)

SANDSTONE_WALL_FROM_SANDSTONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sandstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sandstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:sandstone_wall_from_sandstone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sandstone']],
    rewards=AdvancementRewards(recipes=['minecraft:sandstone_wall_from_sandstone_stonecutting']),
)

SCAFFOLDING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_bamboo': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:bamboo')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:scaffolding'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_bamboo']],
    rewards=AdvancementRewards(recipes=['minecraft:scaffolding']),
)

SHULKER_BOX = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_shulker_shell': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:shulker_shell')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:shulker_box'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_shulker_shell']],
    rewards=AdvancementRewards(recipes=['minecraft:shulker_box']),
)

SMITHING_TABLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_iron_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:smithing_table'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_iron_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:smithing_table']),
)

SMOKER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_furnace': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:furnace')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:smoker'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_furnace']],
    rewards=AdvancementRewards(recipes=['minecraft:smoker']),
)

SNOW = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_snowball': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:snowball')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:snow'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_snowball']],
    rewards=AdvancementRewards(recipes=['minecraft:snow']),
)

SOUL_CAMPFIRE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_soul_sand': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:soul_fire_base_blocks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:soul_campfire'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_soul_sand']],
    rewards=AdvancementRewards(recipes=['minecraft:soul_campfire']),
)

SOUL_LANTERN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_soul_torch': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:soul_torch')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:soul_lantern'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_soul_torch']],
    rewards=AdvancementRewards(recipes=['minecraft:soul_lantern']),
)

SOUL_TORCH = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_soul_sand': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:soul_fire_base_blocks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:soul_torch'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_soul_sand']],
    rewards=AdvancementRewards(recipes=['minecraft:soul_torch']),
)

SPRUCE_FENCE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:spruce_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:spruce_fence'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:spruce_fence']),
)

SPRUCE_HANGING_SIGN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stripped_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_spruce_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:spruce_hanging_sign'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stripped_log']],
    rewards=AdvancementRewards(recipes=['minecraft:spruce_hanging_sign']),
)

SPRUCE_SHELF = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stripped_spruce_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_spruce_log')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:spruce_shelf'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stripped_spruce_log']],
    rewards=AdvancementRewards(recipes=['minecraft:spruce_shelf']),
)

SPRUCE_SIGN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:spruce_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:spruce_sign'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:spruce_sign']),
)

STONECUTTER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stonecutter'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stone']],
    rewards=AdvancementRewards(recipes=['minecraft:stonecutter']),
)

STONE_BRICK_WALL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stone_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stone_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stone_brick_wall'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stone_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:stone_brick_wall']),
)

STONE_BRICK_WALL_FROM_STONE_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stone_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stone_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stone_brick_wall_from_stone_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stone_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:stone_brick_wall_from_stone_bricks_stonecutting']),
)

STONE_BRICK_WALL_FROM_STONE_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stone_brick_wall_from_stone_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stone']],
    rewards=AdvancementRewards(recipes=['minecraft:stone_brick_wall_from_stone_stonecutting']),
)

STRAW_BED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_hay_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:hay_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_straw_bed': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:straw_bed')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:straw_bed'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_hay_block', 'has_straw_bed']],
    rewards=AdvancementRewards(recipes=['minecraft:straw_bed']),
)

SULFUR_BRICK_WALL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sulfur_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sulfur_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:sulfur_brick_wall'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sulfur_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:sulfur_brick_wall']),
)

SULFUR_BRICK_WALL_FROM_POLISHED_SULFUR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_sulfur': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_sulfur')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:sulfur_brick_wall_from_polished_sulfur_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_sulfur']],
    rewards=AdvancementRewards(recipes=['minecraft:sulfur_brick_wall_from_polished_sulfur_stonecutting']),
)

SULFUR_BRICK_WALL_FROM_SULFUR_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sulfur_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sulfur_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:sulfur_brick_wall_from_sulfur_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sulfur_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:sulfur_brick_wall_from_sulfur_bricks_stonecutting']),
)

SULFUR_BRICK_WALL_FROM_SULFUR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sulfur': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sulfur')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:sulfur_brick_wall_from_sulfur_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sulfur']],
    rewards=AdvancementRewards(recipes=['minecraft:sulfur_brick_wall_from_sulfur_stonecutting']),
)

SULFUR_WALL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sulfur': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sulfur')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:sulfur_wall'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sulfur']],
    rewards=AdvancementRewards(recipes=['minecraft:sulfur_wall']),
)

SULFUR_WALL_FROM_SULFUR_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_sulfur': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sulfur')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:sulfur_wall_from_sulfur_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_sulfur']],
    rewards=AdvancementRewards(recipes=['minecraft:sulfur_wall_from_sulfur_stonecutting']),
)

TORCH = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stone_pickaxe': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stone_pickaxe')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:torch'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stone_pickaxe']],
    rewards=AdvancementRewards(recipes=['minecraft:torch']),
)

TUFF_BRICK_WALL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:tuff_brick_wall'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_tuff_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:tuff_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_tuff_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:tuff_brick_wall']),
)

TUFF_BRICK_WALL_FROM_POLISHED_TUFF_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_tuff': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_tuff')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:tuff_brick_wall_from_polished_tuff_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_tuff']],
    rewards=AdvancementRewards(recipes=['minecraft:tuff_brick_wall_from_polished_tuff_stonecutting']),
)

TUFF_BRICK_WALL_FROM_TUFF_BRICKS_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:tuff_brick_wall_from_tuff_bricks_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_tuff_bricks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:tuff_bricks')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_tuff_bricks']],
    rewards=AdvancementRewards(recipes=['minecraft:tuff_brick_wall_from_tuff_bricks_stonecutting']),
)

TUFF_BRICK_WALL_FROM_TUFF_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:tuff_brick_wall_from_tuff_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_tuff': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:tuff')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_tuff']],
    rewards=AdvancementRewards(recipes=['minecraft:tuff_brick_wall_from_tuff_stonecutting']),
)

TUFF_WALL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:tuff_wall'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_tuff': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:tuff')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_tuff']],
    rewards=AdvancementRewards(recipes=['minecraft:tuff_wall']),
)

TUFF_WALL_FROM_TUFF_STONECUTTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:tuff_wall_from_tuff_stonecutting'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_tuff': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:tuff')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_tuff']],
    rewards=AdvancementRewards(recipes=['minecraft:tuff_wall_from_tuff_stonecutting']),
)

WARPED_FENCE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:warped_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:warped_fence'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:warped_fence']),
)

WARPED_HANGING_SIGN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stripped_log': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_warped_stem')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:warped_hanging_sign'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stripped_log']],
    rewards=AdvancementRewards(recipes=['minecraft:warped_hanging_sign']),
)

WARPED_SHELF = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stripped_warped_stem': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stripped_warped_stem')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:warped_shelf'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stripped_warped_stem']],
    rewards=AdvancementRewards(recipes=['minecraft:warped_shelf']),
)

WARPED_SIGN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:warped_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:warped_sign'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:warped_sign']),
)

WHITE_BANNER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:white_banner'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_white_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:white_wool')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_white_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:white_banner']),
)

WHITE_BED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:white_bed'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_white_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:white_wool')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_white_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:white_bed']),
)

WHITE_CANDLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:white_candle'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_white_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:white_dye')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_white_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:white_candle']),
)

WHITE_CARPET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:white_carpet'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_white_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:white_wool')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_white_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:white_carpet']),
)

WHITE_CUSHION = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:white_cushion'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_white_wool_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:white_wool_slab')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_white_wool_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:white_cushion']),
)

WHITE_GLAZED_TERRACOTTA = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:white_glazed_terracotta'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_white_terracotta': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:white_terracotta')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_white_terracotta']],
    rewards=AdvancementRewards(recipes=['minecraft:white_glazed_terracotta']),
)

WHITE_SHULKER_BOX = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_shulker_box': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:shulker_boxes')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:white_shulker_box'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_shulker_box']],
    rewards=AdvancementRewards(recipes=['minecraft:white_shulker_box']),
)

WHITE_STAINED_GLASS_PANE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:white_stained_glass')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:white_stained_glass_pane'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass']],
    rewards=AdvancementRewards(recipes=['minecraft:white_stained_glass_pane']),
)

WHITE_STAINED_GLASS_PANE_FROM_GLASS_PANE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass_pane': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glass_pane')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:white_stained_glass_pane_from_glass_pane'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_white_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:white_dye')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass_pane', 'has_white_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:white_stained_glass_pane_from_glass_pane']),
)

YELLOW_BANNER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:yellow_banner'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_yellow_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:yellow_wool')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_yellow_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:yellow_banner']),
)

YELLOW_BED = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:yellow_bed'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_yellow_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:yellow_wool')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_yellow_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:yellow_bed']),
)

YELLOW_CANDLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:yellow_candle'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_yellow_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:yellow_dye')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_yellow_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:yellow_candle']),
)

YELLOW_CARPET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:yellow_carpet'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_yellow_wool': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:yellow_wool')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_yellow_wool']],
    rewards=AdvancementRewards(recipes=['minecraft:yellow_carpet']),
)

YELLOW_CUSHION = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:yellow_cushion'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_yellow_wool_slab': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:yellow_wool_slab')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_yellow_wool_slab']],
    rewards=AdvancementRewards(recipes=['minecraft:yellow_cushion']),
)

YELLOW_GLAZED_TERRACOTTA = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:yellow_glazed_terracotta'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_yellow_terracotta': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:yellow_terracotta')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_yellow_terracotta']],
    rewards=AdvancementRewards(recipes=['minecraft:yellow_glazed_terracotta']),
)

YELLOW_SHULKER_BOX = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_shulker_box': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:shulker_boxes')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:yellow_shulker_box'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_shulker_box']],
    rewards=AdvancementRewards(recipes=['minecraft:yellow_shulker_box']),
)

YELLOW_STAINED_GLASS_PANE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:yellow_stained_glass')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:yellow_stained_glass_pane'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass']],
    rewards=AdvancementRewards(recipes=['minecraft:yellow_stained_glass_pane']),
)

YELLOW_STAINED_GLASS_PANE_FROM_GLASS_PANE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glass_pane': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glass_pane')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:yellow_stained_glass_pane_from_glass_pane'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_yellow_dye': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:yellow_dye')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_glass_pane', 'has_yellow_dye']],
    rewards=AdvancementRewards(recipes=['minecraft:yellow_stained_glass_pane_from_glass_pane']),
)
