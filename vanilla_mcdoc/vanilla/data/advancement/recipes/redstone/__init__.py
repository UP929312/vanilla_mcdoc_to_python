"""Vanilla's data/advancement/recipes/redstone/ files"""
from vanilla_mcdoc.data.advancement.Advancement import Advancement
from vanilla_mcdoc.data.advancement.AdvancementCriterion import AdvancementCriterionInventoryChanged, AdvancementCriterionRecipeUnlocked
from vanilla_mcdoc.data.advancement.AdvancementRewards import AdvancementRewards
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.advancement.trigger.InventoryChangeTrigger import InventoryChangeTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.RecipeUnlockedTrigger import RecipeUnlockedTriggerTypeArg

ACACIA_BUTTON = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:acacia_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:acacia_button'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:acacia_button']),
)

ACACIA_DOOR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:acacia_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:acacia_door'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:acacia_door']),
)

ACACIA_FENCE_GATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:acacia_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:acacia_fence_gate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:acacia_fence_gate']),
)

ACACIA_PRESSURE_PLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:acacia_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:acacia_pressure_plate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:acacia_pressure_plate']),
)

ACACIA_TRAPDOOR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:acacia_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:acacia_trapdoor'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:acacia_trapdoor']),
)

BAMBOO_BUTTON = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:bamboo_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:bamboo_button'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:bamboo_button']),
)

BAMBOO_DOOR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:bamboo_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:bamboo_door'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:bamboo_door']),
)

BAMBOO_FENCE_GATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:bamboo_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:bamboo_fence_gate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:bamboo_fence_gate']),
)

BAMBOO_PRESSURE_PLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:bamboo_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:bamboo_pressure_plate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:bamboo_pressure_plate']),
)

BAMBOO_TRAPDOOR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:bamboo_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:bamboo_trapdoor'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:bamboo_trapdoor']),
)

BIRCH_BUTTON = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:birch_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:birch_button'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:birch_button']),
)

BIRCH_DOOR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:birch_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:birch_door'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:birch_door']),
)

BIRCH_FENCE_GATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:birch_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:birch_fence_gate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:birch_fence_gate']),
)

BIRCH_PRESSURE_PLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:birch_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:birch_pressure_plate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:birch_pressure_plate']),
)

BIRCH_TRAPDOOR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:birch_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:birch_trapdoor'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:birch_trapdoor']),
)

CALIBRATED_SCULK_SENSOR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_amethyst_shard': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:amethyst_shard')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:calibrated_sculk_sensor'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_amethyst_shard']],
    rewards=AdvancementRewards(recipes=['minecraft:calibrated_sculk_sensor']),
)

CHERRY_BUTTON = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cherry_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cherry_button'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:cherry_button']),
)

CHERRY_DOOR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cherry_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cherry_door'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:cherry_door']),
)

CHERRY_FENCE_GATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cherry_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cherry_fence_gate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:cherry_fence_gate']),
)

CHERRY_PRESSURE_PLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cherry_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cherry_pressure_plate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:cherry_pressure_plate']),
)

CHERRY_TRAPDOOR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cherry_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:cherry_trapdoor'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:cherry_trapdoor']),
)

COMPARATOR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_quartz': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:quartz')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:comparator'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_quartz']],
    rewards=AdvancementRewards(recipes=['minecraft:comparator']),
)

COPPER_BULB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:copper_bulb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_block']],
    rewards=AdvancementRewards(recipes=['minecraft:copper_bulb']),
)

COPPER_DOOR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:copper_door'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:copper_door']),
)

COPPER_TRAPDOOR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:copper_trapdoor'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:copper_trapdoor']),
)

CRAFTER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_dropper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dropper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:crafter'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_dropper']],
    rewards=AdvancementRewards(recipes=['minecraft:crafter']),
)

CRIMSON_BUTTON = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:crimson_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:crimson_button'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:crimson_button']),
)

CRIMSON_DOOR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:crimson_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:crimson_door'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:crimson_door']),
)

CRIMSON_FENCE_GATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:crimson_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:crimson_fence_gate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:crimson_fence_gate']),
)

CRIMSON_PRESSURE_PLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:crimson_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:crimson_pressure_plate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:crimson_pressure_plate']),
)

CRIMSON_TRAPDOOR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:crimson_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:crimson_trapdoor'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:crimson_trapdoor']),
)

DARK_OAK_BUTTON = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dark_oak_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dark_oak_button'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:dark_oak_button']),
)

DARK_OAK_DOOR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dark_oak_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dark_oak_door'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:dark_oak_door']),
)

DARK_OAK_FENCE_GATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dark_oak_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dark_oak_fence_gate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:dark_oak_fence_gate']),
)

DARK_OAK_PRESSURE_PLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dark_oak_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dark_oak_pressure_plate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:dark_oak_pressure_plate']),
)

DARK_OAK_TRAPDOOR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:dark_oak_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dark_oak_trapdoor'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:dark_oak_trapdoor']),
)

DAYLIGHT_DETECTOR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_quartz': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:quartz')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:daylight_detector'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_quartz']],
    rewards=AdvancementRewards(recipes=['minecraft:daylight_detector']),
)

DISPENSER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_bow': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:bow')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dispenser'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_bow']],
    rewards=AdvancementRewards(recipes=['minecraft:dispenser']),
)

DROPPER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_redstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:redstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:dropper'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_redstone']],
    rewards=AdvancementRewards(recipes=['minecraft:dropper']),
)

EXPOSED_COPPER_BULB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_exposed_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:exposed_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:exposed_copper_bulb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_exposed_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:exposed_copper_bulb']),
)

HEAVY_WEIGHTED_PRESSURE_PLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_iron_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:heavy_weighted_pressure_plate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_iron_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:heavy_weighted_pressure_plate']),
)

HONEY_BLOCK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_honey_bottle': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:honey_bottle')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:honey_block'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_honey_bottle']],
    rewards=AdvancementRewards(recipes=['minecraft:honey_block']),
)

HOPPER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_iron_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:hopper'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_iron_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:hopper']),
)

IRON_DOOR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_iron_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:iron_door'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_iron_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:iron_door']),
)

IRON_TRAPDOOR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_iron_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:iron_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:iron_trapdoor'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_iron_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:iron_trapdoor']),
)

JUNGLE_BUTTON = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:jungle_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:jungle_button'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:jungle_button']),
)

JUNGLE_DOOR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:jungle_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:jungle_door'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:jungle_door']),
)

JUNGLE_FENCE_GATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:jungle_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:jungle_fence_gate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:jungle_fence_gate']),
)

JUNGLE_PRESSURE_PLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:jungle_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:jungle_pressure_plate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:jungle_pressure_plate']),
)

JUNGLE_TRAPDOOR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:jungle_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:jungle_trapdoor'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:jungle_trapdoor']),
)

LECTERN = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_book': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:book')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:lectern'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_book']],
    rewards=AdvancementRewards(recipes=['minecraft:lectern']),
)

LEVER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_cobblestone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:cobblestone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:lever'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_cobblestone']],
    rewards=AdvancementRewards(recipes=['minecraft:lever']),
)

LIGHTNING_ROD = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:lightning_rod'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:lightning_rod']),
)

LIGHT_WEIGHTED_PRESSURE_PLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gold_ingot': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gold_ingot')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:light_weighted_pressure_plate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_gold_ingot']],
    rewards=AdvancementRewards(recipes=['minecraft:light_weighted_pressure_plate']),
)

MANGROVE_BUTTON = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:mangrove_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:mangrove_button'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:mangrove_button']),
)

MANGROVE_DOOR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:mangrove_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:mangrove_door'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:mangrove_door']),
)

MANGROVE_FENCE_GATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:mangrove_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:mangrove_fence_gate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:mangrove_fence_gate']),
)

MANGROVE_PRESSURE_PLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:mangrove_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:mangrove_pressure_plate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:mangrove_pressure_plate']),
)

MANGROVE_TRAPDOOR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:mangrove_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:mangrove_trapdoor'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:mangrove_trapdoor']),
)

NOTE_BLOCK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_redstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:redstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:note_block'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_redstone']],
    rewards=AdvancementRewards(recipes=['minecraft:note_block']),
)

OAK_BUTTON = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oak_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:oak_button'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:oak_button']),
)

OAK_DOOR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oak_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:oak_door'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:oak_door']),
)

OAK_FENCE_GATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oak_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:oak_fence_gate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:oak_fence_gate']),
)

OAK_PRESSURE_PLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oak_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:oak_pressure_plate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:oak_pressure_plate']),
)

OAK_TRAPDOOR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oak_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:oak_trapdoor'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:oak_trapdoor']),
)

OBSERVER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_quartz': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:quartz')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:observer'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_quartz']],
    rewards=AdvancementRewards(recipes=['minecraft:observer']),
)

OXIDIZED_COPPER_BULB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_oxidized_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oxidized_copper')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:oxidized_copper_bulb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_oxidized_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:oxidized_copper_bulb']),
)

PALE_OAK_BUTTON = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pale_oak_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pale_oak_button'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:pale_oak_button']),
)

PALE_OAK_DOOR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pale_oak_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pale_oak_door'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:pale_oak_door']),
)

PALE_OAK_FENCE_GATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pale_oak_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pale_oak_fence_gate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:pale_oak_fence_gate']),
)

PALE_OAK_PRESSURE_PLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pale_oak_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pale_oak_pressure_plate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:pale_oak_pressure_plate']),
)

PALE_OAK_TRAPDOOR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:pale_oak_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:pale_oak_trapdoor'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:pale_oak_trapdoor']),
)

PISTON = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_redstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:redstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:piston'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_redstone']],
    rewards=AdvancementRewards(recipes=['minecraft:piston']),
)

POLISHED_BLACKSTONE_BUTTON = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_blackstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_blackstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_blackstone_button'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_blackstone']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_blackstone_button']),
)

POLISHED_BLACKSTONE_PRESSURE_PLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_polished_blackstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:polished_blackstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:polished_blackstone_pressure_plate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_polished_blackstone']],
    rewards=AdvancementRewards(recipes=['minecraft:polished_blackstone_pressure_plate']),
)

POPLAR_BUTTON = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:poplar_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:poplar_button'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:poplar_button']),
)

POPLAR_DOOR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:poplar_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:poplar_door'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:poplar_door']),
)

POPLAR_FENCE_GATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:poplar_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:poplar_fence_gate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:poplar_fence_gate']),
)

POPLAR_PRESSURE_PLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:poplar_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:poplar_pressure_plate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:poplar_pressure_plate']),
)

POPLAR_TRAPDOOR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:poplar_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:poplar_trapdoor'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:poplar_trapdoor']),
)

REDSTONE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_redstone_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:redstone_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:redstone'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_redstone_block']],
    rewards=AdvancementRewards(recipes=['minecraft:redstone']),
)

REDSTONE_BLOCK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_redstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:redstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:redstone_block'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_redstone']],
    rewards=AdvancementRewards(recipes=['minecraft:redstone_block']),
)

REDSTONE_FROM_BLASTING_DEEPSLATE_REDSTONE_ORE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate_redstone_ore': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate_redstone_ore')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:redstone_from_blasting_deepslate_redstone_ore'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate_redstone_ore']],
    rewards=AdvancementRewards(recipes=['minecraft:redstone_from_blasting_deepslate_redstone_ore']),
)

REDSTONE_FROM_BLASTING_REDSTONE_ORE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_redstone_ore': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:redstone_ore')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:redstone_from_blasting_redstone_ore'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_redstone_ore']],
    rewards=AdvancementRewards(recipes=['minecraft:redstone_from_blasting_redstone_ore']),
)

REDSTONE_FROM_SMELTING_DEEPSLATE_REDSTONE_ORE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_deepslate_redstone_ore': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:deepslate_redstone_ore')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:redstone_from_smelting_deepslate_redstone_ore'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_deepslate_redstone_ore']],
    rewards=AdvancementRewards(recipes=['minecraft:redstone_from_smelting_deepslate_redstone_ore']),
)

REDSTONE_FROM_SMELTING_REDSTONE_ORE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_redstone_ore': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:redstone_ore')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:redstone_from_smelting_redstone_ore'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_redstone_ore']],
    rewards=AdvancementRewards(recipes=['minecraft:redstone_from_smelting_redstone_ore']),
)

REDSTONE_LAMP = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_glowstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:glowstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:redstone_lamp'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_glowstone']],
    rewards=AdvancementRewards(recipes=['minecraft:redstone_lamp']),
)

REDSTONE_TORCH = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_redstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:redstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:redstone_torch'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_redstone']],
    rewards=AdvancementRewards(recipes=['minecraft:redstone_torch']),
)

REPEATER = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_redstone_torch': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:redstone_torch')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:repeater'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_redstone_torch']],
    rewards=AdvancementRewards(recipes=['minecraft:repeater']),
)

SLIME_BLOCK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_slime_ball': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:slime_ball')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:slime_block'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_slime_ball']],
    rewards=AdvancementRewards(recipes=['minecraft:slime_block']),
)

SPRUCE_BUTTON = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:spruce_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:spruce_button'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:spruce_button']),
)

SPRUCE_DOOR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:spruce_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:spruce_door'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:spruce_door']),
)

SPRUCE_FENCE_GATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:spruce_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:spruce_fence_gate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:spruce_fence_gate']),
)

SPRUCE_PRESSURE_PLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:spruce_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:spruce_pressure_plate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:spruce_pressure_plate']),
)

SPRUCE_TRAPDOOR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:spruce_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:spruce_trapdoor'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:spruce_trapdoor']),
)

STICKY_PISTON = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_slime_ball': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:slime_ball')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:sticky_piston'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_slime_ball']],
    rewards=AdvancementRewards(recipes=['minecraft:sticky_piston']),
)

STONE_BUTTON = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stone_button'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stone']],
    rewards=AdvancementRewards(recipes=['minecraft:stone_button']),
)

STONE_PRESSURE_PLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_stone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:stone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:stone_pressure_plate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_stone']],
    rewards=AdvancementRewards(recipes=['minecraft:stone_pressure_plate']),
)

TARGET = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_hay_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:hay_block')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_redstone': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:redstone')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:target'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_redstone', 'has_hay_block']],
    rewards=AdvancementRewards(recipes=['minecraft:target']),
)

TNT = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_gunpowder': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:gunpowder')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:tnt'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_gunpowder']],
    rewards=AdvancementRewards(recipes=['minecraft:tnt']),
)

TRAPPED_CHEST = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:trapped_chest'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_tripwire_hook': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:tripwire_hook')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_tripwire_hook']],
    rewards=AdvancementRewards(recipes=['minecraft:trapped_chest']),
)

TRIPWIRE_HOOK = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_string': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:string')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:tripwire_hook'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_string']],
    rewards=AdvancementRewards(recipes=['minecraft:tripwire_hook']),
)

WARPED_BUTTON = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:warped_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:warped_button'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:warped_button']),
)

WARPED_DOOR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:warped_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:warped_door'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:warped_door']),
)

WARPED_FENCE_GATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:warped_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:warped_fence_gate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:warped_fence_gate']),
)

WARPED_PRESSURE_PLATE = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:warped_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:warped_pressure_plate'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:warped_pressure_plate']),
)

WARPED_TRAPDOOR = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_planks': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:warped_planks')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:warped_trapdoor'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_planks']],
    rewards=AdvancementRewards(recipes=['minecraft:warped_trapdoor']),
)

WAXED_COPPER_BULB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_copper_bulb'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_copper_block': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_copper_block')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_copper_block']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_copper_bulb']),
)

WAXED_COPPER_BULB_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_bulb': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_bulb')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_copper_bulb_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_bulb']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_copper_bulb_from_honeycomb']),
)

WAXED_COPPER_DOOR_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_door': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_door')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_copper_door_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_door']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_copper_door_from_honeycomb']),
)

WAXED_COPPER_TRAPDOOR_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_copper_trapdoor': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:copper_trapdoor')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_copper_trapdoor_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_copper_trapdoor']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_copper_trapdoor_from_honeycomb']),
)

WAXED_EXPOSED_COPPER_BULB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_exposed_copper_bulb'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_exposed_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_exposed_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_exposed_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_exposed_copper_bulb']),
)

WAXED_EXPOSED_COPPER_BULB_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_exposed_copper_bulb': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:exposed_copper_bulb')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_exposed_copper_bulb_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_exposed_copper_bulb']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_exposed_copper_bulb_from_honeycomb']),
)

WAXED_EXPOSED_COPPER_DOOR_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_exposed_copper_door': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:exposed_copper_door')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_exposed_copper_door_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_exposed_copper_door']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_exposed_copper_door_from_honeycomb']),
)

WAXED_EXPOSED_COPPER_TRAPDOOR_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_exposed_copper_trapdoor': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:exposed_copper_trapdoor')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_exposed_copper_trapdoor_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_exposed_copper_trapdoor']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_exposed_copper_trapdoor_from_honeycomb']),
)

WAXED_OXIDIZED_COPPER_BULB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_oxidized_copper_bulb'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_oxidized_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_oxidized_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_oxidized_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_oxidized_copper_bulb']),
)

WAXED_OXIDIZED_COPPER_BULB_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_oxidized_copper_bulb': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oxidized_copper_bulb')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_oxidized_copper_bulb_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_oxidized_copper_bulb']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_oxidized_copper_bulb_from_honeycomb']),
)

WAXED_OXIDIZED_COPPER_DOOR_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_oxidized_copper_door': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oxidized_copper_door')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_oxidized_copper_door_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_oxidized_copper_door']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_oxidized_copper_door_from_honeycomb']),
)

WAXED_OXIDIZED_COPPER_TRAPDOOR_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_oxidized_copper_trapdoor': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:oxidized_copper_trapdoor')]),
            trigger='minecraft:inventory_changed',
        ),
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_oxidized_copper_trapdoor_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
    },
    requirements=[['has_the_recipe', 'has_oxidized_copper_trapdoor']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_oxidized_copper_trapdoor_from_honeycomb']),
)

WAXED_WEATHERED_COPPER_BULB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_weathered_copper_bulb'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_waxed_weathered_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:waxed_weathered_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_waxed_weathered_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_weathered_copper_bulb']),
)

WAXED_WEATHERED_COPPER_BULB_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_weathered_copper_bulb_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_weathered_copper_bulb': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:weathered_copper_bulb')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_weathered_copper_bulb']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_weathered_copper_bulb_from_honeycomb']),
)

WAXED_WEATHERED_COPPER_DOOR_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_weathered_copper_door_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_weathered_copper_door': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:weathered_copper_door')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_weathered_copper_door']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_weathered_copper_door_from_honeycomb']),
)

WAXED_WEATHERED_COPPER_TRAPDOOR_FROM_HONEYCOMB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:waxed_weathered_copper_trapdoor_from_honeycomb'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_weathered_copper_trapdoor': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:weathered_copper_trapdoor')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_weathered_copper_trapdoor']],
    rewards=AdvancementRewards(recipes=['minecraft:waxed_weathered_copper_trapdoor_from_honeycomb']),
)

WEATHERED_COPPER_BULB = Advancement(
    parent='minecraft:recipes/root',
    criteria={
        'has_the_recipe': AdvancementCriterionRecipeUnlocked(
            conditions=RecipeUnlockedTriggerTypeArg(recipes='minecraft:weathered_copper_bulb'),
            trigger='minecraft:recipe_unlocked',
        ),
        'has_weathered_copper': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:weathered_copper')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['has_the_recipe', 'has_weathered_copper']],
    rewards=AdvancementRewards(recipes=['minecraft:weathered_copper_bulb']),
)
