"""Vanilla's data/advancement/recipes/food/ files"""
from vanilla_mcdoc.data.advancement.Advancement import Advancement
from vanilla_mcdoc.data.advancement.AdvancementCriterion import AdvancementCriterionInventoryChanged, AdvancementCriterionRecipeUnlocked
from vanilla_mcdoc.data.advancement.AdvancementRewards import AdvancementRewards
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.advancement.trigger.InventoryChangeTrigger import InventoryChangeTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.RecipeUnlockedTrigger import RecipeUnlockedTriggerTypeArg

BAKED_POTATO = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_potato': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:potato')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:baked_potato'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_potato']],
    rewards=AdvancementRewards(recipes=['minecraft:baked_potato']),
)

BAKED_POTATO_FROM_CAMPFIRE_COOKING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_potato': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:potato')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:baked_potato_from_campfire_cooking'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_potato']],
    rewards=AdvancementRewards(recipes=['minecraft:baked_potato_from_campfire_cooking']),
)

BAKED_POTATO_FROM_SMOKING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_potato': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:potato')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:baked_potato_from_smoking'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_potato']],
    rewards=AdvancementRewards(recipes=['minecraft:baked_potato_from_smoking']),
)

BEETROOT_SOUP = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_beetroot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:beetroot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:beetroot_soup'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_beetroot']],
    rewards=AdvancementRewards(recipes=['minecraft:beetroot_soup']),
)

BREAD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:bread'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_wheat': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:wheat')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_wheat']],
    rewards=AdvancementRewards(recipes=['minecraft:bread']),
)

CAKE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_egg': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:eggs')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cake'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_egg']],
    rewards=AdvancementRewards(recipes=['minecraft:cake']),
)

COOKED_BEEF = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_beef': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:beef')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cooked_beef'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_beef']],
    rewards=AdvancementRewards(recipes=['minecraft:cooked_beef']),
)

COOKED_BEEF_FROM_CAMPFIRE_COOKING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_beef': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:beef')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cooked_beef_from_campfire_cooking'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_beef']],
    rewards=AdvancementRewards(recipes=['minecraft:cooked_beef_from_campfire_cooking']),
)

COOKED_BEEF_FROM_SMOKING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_beef': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:beef')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cooked_beef_from_smoking'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_beef']],
    rewards=AdvancementRewards(recipes=['minecraft:cooked_beef_from_smoking']),
)

COOKED_CHICKEN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_chicken': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:chicken')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cooked_chicken'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_chicken']],
    rewards=AdvancementRewards(recipes=['minecraft:cooked_chicken']),
)

COOKED_CHICKEN_FROM_CAMPFIRE_COOKING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_chicken': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:chicken')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cooked_chicken_from_campfire_cooking'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_chicken']],
    rewards=AdvancementRewards(recipes=['minecraft:cooked_chicken_from_campfire_cooking']),
)

COOKED_CHICKEN_FROM_SMOKING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_chicken': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:chicken')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cooked_chicken_from_smoking'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_chicken']],
    rewards=AdvancementRewards(recipes=['minecraft:cooked_chicken_from_smoking']),
)

COOKED_COD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cod': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cod')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cooked_cod'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cod']],
    rewards=AdvancementRewards(recipes=['minecraft:cooked_cod']),
)

COOKED_COD_FROM_CAMPFIRE_COOKING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cod': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cod')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cooked_cod_from_campfire_cooking'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cod']],
    rewards=AdvancementRewards(recipes=['minecraft:cooked_cod_from_campfire_cooking']),
)

COOKED_COD_FROM_SMOKING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cod': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cod')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cooked_cod_from_smoking'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cod']],
    rewards=AdvancementRewards(recipes=['minecraft:cooked_cod_from_smoking']),
)

COOKED_MUTTON = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_mutton': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:mutton')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cooked_mutton'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_mutton']],
    rewards=AdvancementRewards(recipes=['minecraft:cooked_mutton']),
)

COOKED_MUTTON_FROM_CAMPFIRE_COOKING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_mutton': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:mutton')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cooked_mutton_from_campfire_cooking'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_mutton']],
    rewards=AdvancementRewards(recipes=['minecraft:cooked_mutton_from_campfire_cooking']),
)

COOKED_MUTTON_FROM_SMOKING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_mutton': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:mutton')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cooked_mutton_from_smoking'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_mutton']],
    rewards=AdvancementRewards(recipes=['minecraft:cooked_mutton_from_smoking']),
)

COOKED_PORKCHOP = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_porkchop': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:porkchop')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cooked_porkchop'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_porkchop']],
    rewards=AdvancementRewards(recipes=['minecraft:cooked_porkchop']),
)

COOKED_PORKCHOP_FROM_CAMPFIRE_COOKING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_porkchop': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:porkchop')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cooked_porkchop_from_campfire_cooking'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_porkchop']],
    rewards=AdvancementRewards(recipes=['minecraft:cooked_porkchop_from_campfire_cooking']),
)

COOKED_PORKCHOP_FROM_SMOKING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_porkchop': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:porkchop')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cooked_porkchop_from_smoking'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_porkchop']],
    rewards=AdvancementRewards(recipes=['minecraft:cooked_porkchop_from_smoking']),
)

COOKED_RABBIT = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_rabbit': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:rabbit')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cooked_rabbit'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_rabbit']],
    rewards=AdvancementRewards(recipes=['minecraft:cooked_rabbit']),
)

COOKED_RABBIT_FROM_CAMPFIRE_COOKING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_rabbit': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:rabbit')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cooked_rabbit_from_campfire_cooking'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_rabbit']],
    rewards=AdvancementRewards(recipes=['minecraft:cooked_rabbit_from_campfire_cooking']),
)

COOKED_RABBIT_FROM_SMOKING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_rabbit': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:rabbit')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cooked_rabbit_from_smoking'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_rabbit']],
    rewards=AdvancementRewards(recipes=['minecraft:cooked_rabbit_from_smoking']),
)

COOKED_SALMON = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_salmon': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:salmon')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cooked_salmon'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_salmon']],
    rewards=AdvancementRewards(recipes=['minecraft:cooked_salmon']),
)

COOKED_SALMON_FROM_CAMPFIRE_COOKING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_salmon': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:salmon')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cooked_salmon_from_campfire_cooking'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_salmon']],
    rewards=AdvancementRewards(recipes=['minecraft:cooked_salmon_from_campfire_cooking']),
)

COOKED_SALMON_FROM_SMOKING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_salmon': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:salmon')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cooked_salmon_from_smoking'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_salmon']],
    rewards=AdvancementRewards(recipes=['minecraft:cooked_salmon_from_smoking']),
)

COOKIE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cocoa': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cocoa_beans')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cookie'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cocoa']],
    rewards=AdvancementRewards(recipes=['minecraft:cookie']),
)

DRIED_KELP = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_dried_kelp_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dried_kelp_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dried_kelp'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_dried_kelp_block']],
    rewards=AdvancementRewards(recipes=['minecraft:dried_kelp']),
)

DRIED_KELP_FROM_CAMPFIRE_COOKING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_kelp': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:kelp')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dried_kelp_from_campfire_cooking'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_kelp']],
    rewards=AdvancementRewards(recipes=['minecraft:dried_kelp_from_campfire_cooking']),
)

DRIED_KELP_FROM_SMELTING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_kelp': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:kelp')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dried_kelp_from_smelting'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_kelp']],
    rewards=AdvancementRewards(recipes=['minecraft:dried_kelp_from_smelting']),
)

DRIED_KELP_FROM_SMOKING = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_kelp': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:kelp')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dried_kelp_from_smoking'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_kelp']],
    rewards=AdvancementRewards(recipes=['minecraft:dried_kelp_from_smoking']),
)

GOLDEN_APPLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gold_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gold_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:golden_apple'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_gold_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:golden_apple']),
)

HONEY_BOTTLE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_honey_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:honey_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:honey_bottle'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_honey_block']],
    rewards=AdvancementRewards(recipes=['minecraft:honey_bottle']),
)

MUSHROOM_STEW = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_bowl': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:bowl')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_mushroom': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:mushrooms')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_mushroom_stew': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:mushroom_stew')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:mushroom_stew'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_mushroom_stew', 'has_bowl', 'has_mushroom']],
    rewards=AdvancementRewards(recipes=['minecraft:mushroom_stew']),
)

PUMPKIN_PIE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_carved_pumpkin': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:carved_pumpkin')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_pumpkin': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pumpkin')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pumpkin_pie'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_carved_pumpkin', 'has_pumpkin']],
    rewards=AdvancementRewards(recipes=['minecraft:pumpkin_pie']),
)

RABBIT_STEW_FROM_BROWN_MUSHROOM = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cooked_rabbit': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cooked_rabbit')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:rabbit_stew_from_brown_mushroom'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cooked_rabbit']],
    rewards=AdvancementRewards(recipes=['minecraft:rabbit_stew_from_brown_mushroom']),
)

RABBIT_STEW_FROM_RED_MUSHROOM = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cooked_rabbit': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cooked_rabbit')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:rabbit_stew_from_red_mushroom'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cooked_rabbit']],
    rewards=AdvancementRewards(recipes=['minecraft:rabbit_stew_from_red_mushroom']),
)

RABBIT_STEW_FROM_SHELF_MUSHROOM = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cooked_rabbit': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cooked_rabbit')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:rabbit_stew_from_shelf_mushroom'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cooked_rabbit']],
    rewards=AdvancementRewards(recipes=['minecraft:rabbit_stew_from_shelf_mushroom']),
)

SUSPICIOUS_STEW_FROM_ALLIUM = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_allium': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:allium')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:suspicious_stew_from_allium'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_allium']],
    rewards=AdvancementRewards(recipes=['minecraft:suspicious_stew_from_allium']),
)

SUSPICIOUS_STEW_FROM_AZURE_BLUET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_azure_bluet': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:azure_bluet')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:suspicious_stew_from_azure_bluet'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_azure_bluet']],
    rewards=AdvancementRewards(recipes=['minecraft:suspicious_stew_from_azure_bluet']),
)

SUSPICIOUS_STEW_FROM_BLUE_ORCHID = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_blue_orchid': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:blue_orchid')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:suspicious_stew_from_blue_orchid'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_blue_orchid']],
    rewards=AdvancementRewards(recipes=['minecraft:suspicious_stew_from_blue_orchid']),
)

SUSPICIOUS_STEW_FROM_CLOSED_EYEBLOSSOM = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_closed_eyeblossom': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:closed_eyeblossom')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:suspicious_stew_from_closed_eyeblossom'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_closed_eyeblossom']],
    rewards=AdvancementRewards(recipes=['minecraft:suspicious_stew_from_closed_eyeblossom']),
)

SUSPICIOUS_STEW_FROM_CORNFLOWER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cornflower': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cornflower')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:suspicious_stew_from_cornflower'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cornflower']],
    rewards=AdvancementRewards(recipes=['minecraft:suspicious_stew_from_cornflower']),
)

SUSPICIOUS_STEW_FROM_DANDELION = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_dandelion': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dandelion')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:suspicious_stew_from_dandelion'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_dandelion']],
    rewards=AdvancementRewards(recipes=['minecraft:suspicious_stew_from_dandelion']),
)

SUSPICIOUS_STEW_FROM_GOLDEN_DANDELION = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_golden_dandelion': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:golden_dandelion')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:suspicious_stew_from_golden_dandelion'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_golden_dandelion']],
    rewards=AdvancementRewards(recipes=['minecraft:suspicious_stew_from_golden_dandelion']),
)

SUSPICIOUS_STEW_FROM_LILY_OF_THE_VALLEY = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_lily_of_the_valley': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:lily_of_the_valley')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:suspicious_stew_from_lily_of_the_valley'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_lily_of_the_valley']],
    rewards=AdvancementRewards(recipes=['minecraft:suspicious_stew_from_lily_of_the_valley']),
)

SUSPICIOUS_STEW_FROM_OPEN_EYEBLOSSOM = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_open_eyeblossom': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:open_eyeblossom')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:suspicious_stew_from_open_eyeblossom'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_open_eyeblossom']],
    rewards=AdvancementRewards(recipes=['minecraft:suspicious_stew_from_open_eyeblossom']),
)

SUSPICIOUS_STEW_FROM_ORANGE_TULIP = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_orange_tulip': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:orange_tulip')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:suspicious_stew_from_orange_tulip'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_orange_tulip']],
    rewards=AdvancementRewards(recipes=['minecraft:suspicious_stew_from_orange_tulip']),
)

SUSPICIOUS_STEW_FROM_OXEYE_DAISY = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_oxeye_daisy': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oxeye_daisy')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:suspicious_stew_from_oxeye_daisy'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_oxeye_daisy']],
    rewards=AdvancementRewards(recipes=['minecraft:suspicious_stew_from_oxeye_daisy']),
)

SUSPICIOUS_STEW_FROM_PINK_TULIP = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_pink_tulip': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pink_tulip')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:suspicious_stew_from_pink_tulip'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_pink_tulip']],
    rewards=AdvancementRewards(recipes=['minecraft:suspicious_stew_from_pink_tulip']),
)

SUSPICIOUS_STEW_FROM_POPPY = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_poppy': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:poppy')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:suspicious_stew_from_poppy'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_poppy']],
    rewards=AdvancementRewards(recipes=['minecraft:suspicious_stew_from_poppy']),
)

SUSPICIOUS_STEW_FROM_RED_TULIP = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_red_tulip': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:red_tulip')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:suspicious_stew_from_red_tulip'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_red_tulip']],
    rewards=AdvancementRewards(recipes=['minecraft:suspicious_stew_from_red_tulip']),
)

SUSPICIOUS_STEW_FROM_TORCHFLOWER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:suspicious_stew_from_torchflower'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_torchflower': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:torchflower')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_torchflower']],
    rewards=AdvancementRewards(recipes=['minecraft:suspicious_stew_from_torchflower']),
)

SUSPICIOUS_STEW_FROM_WHITE_TULIP = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:suspicious_stew_from_white_tulip'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_white_tulip': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:white_tulip')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_white_tulip']],
    rewards=AdvancementRewards(recipes=['minecraft:suspicious_stew_from_white_tulip']),
)

SUSPICIOUS_STEW_FROM_WITHER_ROSE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:suspicious_stew_from_wither_rose'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_wither_rose': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:wither_rose')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_wither_rose']],
    rewards=AdvancementRewards(recipes=['minecraft:suspicious_stew_from_wither_rose']),
)
