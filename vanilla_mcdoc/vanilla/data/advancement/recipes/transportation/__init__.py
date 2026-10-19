"""Vanilla's data/advancement/recipes/transportation/ files"""
from vanilla_mcdoc.data.advancement.Advancement import Advancement
from vanilla_mcdoc.data.advancement.AdvancementCriterion import AdvancementCriterionEnterBlock, AdvancementCriterionInventoryChanged, AdvancementCriterionRecipeUnlocked
from vanilla_mcdoc.data.advancement.AdvancementRewards import AdvancementRewards
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.advancement.trigger.EnterBlockTrigger import EnterBlockTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.InventoryChangeTrigger import InventoryChangeTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.RecipeUnlockedTrigger import RecipeUnlockedTriggerTypeArg

ACACIA_BOAT = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:acacia_boat'),
            trigger='minecraft:recipe_unlocked',
        ),
        'in_water': AdvancementCriterionEnterBlock(
            conditions=EnterBlockTriggerTypeArg(blocks='minecraft:water'),
            trigger='minecraft:enter_block',
        ),
    },
    requirements=[['has_the_recipe', 'in_water']],
    rewards=AdvancementRewards(recipes=['minecraft:acacia_boat']),
)

ACACIA_CHEST_BOAT = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_boat': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:boats')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:acacia_chest_boat'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_boat']],
    rewards=AdvancementRewards(recipes=['minecraft:acacia_chest_boat']),
)

ACTIVATOR_RAIL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_rail': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:rail')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:activator_rail'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_rail']],
    rewards=AdvancementRewards(recipes=['minecraft:activator_rail']),
)

BAMBOO_CHEST_RAFT = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_boat': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:boats')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:bamboo_chest_raft'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_boat']],
    rewards=AdvancementRewards(recipes=['minecraft:bamboo_chest_raft']),
)

BAMBOO_RAFT = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:bamboo_raft'),
            trigger='minecraft:recipe_unlocked',
        ),
        'in_water': AdvancementCriterionEnterBlock(
            conditions=EnterBlockTriggerTypeArg(blocks='minecraft:water'),
            trigger='minecraft:enter_block',
        ),
    },
    requirements=[['has_the_recipe', 'in_water']],
    rewards=AdvancementRewards(recipes=['minecraft:bamboo_raft']),
)

BIRCH_BOAT = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:birch_boat'),
            trigger='minecraft:recipe_unlocked',
        ),
        'in_water': AdvancementCriterionEnterBlock(
            conditions=EnterBlockTriggerTypeArg(blocks='minecraft:water'),
            trigger='minecraft:enter_block',
        ),
    },
    requirements=[['has_the_recipe', 'in_water']],
    rewards=AdvancementRewards(recipes=['minecraft:birch_boat']),
)

BIRCH_CHEST_BOAT = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_boat': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:boats')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:birch_chest_boat'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_boat']],
    rewards=AdvancementRewards(recipes=['minecraft:birch_chest_boat']),
)

CARROT_ON_A_STICK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_carrot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:carrot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:carrot_on_a_stick'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_carrot']],
    rewards=AdvancementRewards(recipes=['minecraft:carrot_on_a_stick']),
)

CHERRY_BOAT = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cherry_boat'),
            trigger='minecraft:recipe_unlocked',
        ),
        'in_water': AdvancementCriterionEnterBlock(
            conditions=EnterBlockTriggerTypeArg(blocks='minecraft:water'),
            trigger='minecraft:enter_block',
        ),
    },
    requirements=[['has_the_recipe', 'in_water']],
    rewards=AdvancementRewards(recipes=['minecraft:cherry_boat']),
)

CHERRY_CHEST_BOAT = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_boat': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:boats')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cherry_chest_boat'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_boat']],
    rewards=AdvancementRewards(recipes=['minecraft:cherry_chest_boat']),
)

CHEST_MINECART = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_minecart': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:minecart')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:chest_minecart'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_minecart']],
    rewards=AdvancementRewards(recipes=['minecraft:chest_minecart']),
)

DARK_OAK_BOAT = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dark_oak_boat'),
            trigger='minecraft:recipe_unlocked',
        ),
        'in_water': AdvancementCriterionEnterBlock(
            conditions=EnterBlockTriggerTypeArg(blocks='minecraft:water'),
            trigger='minecraft:enter_block',
        ),
    },
    requirements=[['has_the_recipe', 'in_water']],
    rewards=AdvancementRewards(recipes=['minecraft:dark_oak_boat']),
)

DARK_OAK_CHEST_BOAT = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_boat': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:boats')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dark_oak_chest_boat'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_boat']],
    rewards=AdvancementRewards(recipes=['minecraft:dark_oak_chest_boat']),
)

DETECTOR_RAIL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_rail': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:rail')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:detector_rail'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_rail']],
    rewards=AdvancementRewards(recipes=['minecraft:detector_rail']),
)

FURNACE_MINECART = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_minecart': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:minecart')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:furnace_minecart'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_minecart']],
    rewards=AdvancementRewards(recipes=['minecraft:furnace_minecart']),
)

HOPPER_MINECART = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_minecart': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:minecart')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:hopper_minecart'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_minecart']],
    rewards=AdvancementRewards(recipes=['minecraft:hopper_minecart']),
)

JUNGLE_BOAT = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:jungle_boat'),
            trigger='minecraft:recipe_unlocked',
        ),
        'in_water': AdvancementCriterionEnterBlock(
            conditions=EnterBlockTriggerTypeArg(blocks='minecraft:water'),
            trigger='minecraft:enter_block',
        ),
    },
    requirements=[['has_the_recipe', 'in_water']],
    rewards=AdvancementRewards(recipes=['minecraft:jungle_boat']),
)

JUNGLE_CHEST_BOAT = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_boat': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:boats')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:jungle_chest_boat'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_boat']],
    rewards=AdvancementRewards(recipes=['minecraft:jungle_chest_boat']),
)

MANGROVE_BOAT = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:mangrove_boat'),
            trigger='minecraft:recipe_unlocked',
        ),
        'in_water': AdvancementCriterionEnterBlock(
            conditions=EnterBlockTriggerTypeArg(blocks='minecraft:water'),
            trigger='minecraft:enter_block',
        ),
    },
    requirements=[['has_the_recipe', 'in_water']],
    rewards=AdvancementRewards(recipes=['minecraft:mangrove_boat']),
)

MANGROVE_CHEST_BOAT = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_boat': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:boats')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:mangrove_chest_boat'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_boat']],
    rewards=AdvancementRewards(recipes=['minecraft:mangrove_chest_boat']),
)

MINECART = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_iron_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:minecart'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_iron_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:minecart']),
)

OAK_BOAT = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:oak_boat'),
            trigger='minecraft:recipe_unlocked',
        ),
        'in_water': AdvancementCriterionEnterBlock(
            conditions=EnterBlockTriggerTypeArg(blocks='minecraft:water'),
            trigger='minecraft:enter_block',
        ),
    },
    requirements=[['has_the_recipe', 'in_water']],
    rewards=AdvancementRewards(recipes=['minecraft:oak_boat']),
)

OAK_CHEST_BOAT = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_boat': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:boats')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:oak_chest_boat'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_boat']],
    rewards=AdvancementRewards(recipes=['minecraft:oak_chest_boat']),
)

PALE_OAK_BOAT = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pale_oak_boat'),
            trigger='minecraft:recipe_unlocked',
        ),
        'in_water': AdvancementCriterionEnterBlock(
            conditions=EnterBlockTriggerTypeArg(blocks='minecraft:water'),
            trigger='minecraft:enter_block',
        ),
    },
    requirements=[['has_the_recipe', 'in_water']],
    rewards=AdvancementRewards(recipes=['minecraft:pale_oak_boat']),
)

PALE_OAK_CHEST_BOAT = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_boat': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:boats')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pale_oak_chest_boat'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_boat']],
    rewards=AdvancementRewards(recipes=['minecraft:pale_oak_chest_boat']),
)

POPLAR_BOAT = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:poplar_boat'),
            trigger='minecraft:recipe_unlocked',
        ),
        'in_water': AdvancementCriterionEnterBlock(
            conditions=EnterBlockTriggerTypeArg(blocks='minecraft:water'),
            trigger='minecraft:enter_block',
        ),
    },
    requirements=[['has_the_recipe', 'in_water']],
    rewards=AdvancementRewards(recipes=['minecraft:poplar_boat']),
)

POPLAR_CHEST_BOAT = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_boat': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:boats')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:poplar_chest_boat'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_boat']],
    rewards=AdvancementRewards(recipes=['minecraft:poplar_chest_boat']),
)

POWERED_RAIL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_rail': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:rail')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:powered_rail'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_rail']],
    rewards=AdvancementRewards(recipes=['minecraft:powered_rail']),
)

RAIL = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_minecart': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:minecart')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:rail'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_minecart']],
    rewards=AdvancementRewards(recipes=['minecraft:rail']),
)

SPRUCE_BOAT = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:spruce_boat'),
            trigger='minecraft:recipe_unlocked',
        ),
        'in_water': AdvancementCriterionEnterBlock(
            conditions=EnterBlockTriggerTypeArg(blocks='minecraft:water'),
            trigger='minecraft:enter_block',
        ),
    },
    requirements=[['has_the_recipe', 'in_water']],
    rewards=AdvancementRewards(recipes=['minecraft:spruce_boat']),
)

SPRUCE_CHEST_BOAT = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_boat': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='#minecraft:boats')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:spruce_chest_boat'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_boat']],
    rewards=AdvancementRewards(recipes=['minecraft:spruce_chest_boat']),
)

TNT_MINECART = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_minecart': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:minecart')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:tnt_minecart'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_minecart']],
    rewards=AdvancementRewards(recipes=['minecraft:tnt_minecart']),
)

WARPED_FUNGUS_ON_A_STICK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:warped_fungus_on_a_stick'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_warped_fungus': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:warped_fungus')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_warped_fungus']],
    rewards=AdvancementRewards(recipes=['minecraft:warped_fungus_on_a_stick']),
)
