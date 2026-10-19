"""Vanilla's data/recipe/ files"""
from typing import Any
from vanilla_mcdoc.data.recipe.CookingBookCategory import CookingBookCategory
from vanilla_mcdoc.data.recipe.CraftingBookCategory import CraftingBookCategory
from vanilla_mcdoc.data.recipe.Recipe import RecipeBlasting, RecipeCampfireCooking, RecipeCraftingDecoratedPot, RecipeCraftingDye, RecipeCraftingImbue, RecipeCraftingShaped, RecipeCraftingShapeless, RecipeCraftingSpecialBannerduplicate, RecipeCraftingSpecialBookcloning, RecipeCraftingSpecialFireworkRocket, RecipeCraftingSpecialFireworkStar, RecipeCraftingSpecialFireworkStarFade, RecipeCraftingSpecialMapextending, RecipeCraftingSpecialRepairitem, RecipeCraftingSpecialShielddecoration, RecipeCraftingTransmute, RecipeSmelting, RecipeSmithingTransform, RecipeSmithingTrim, RecipeSmoking, RecipeStonecutting
from vanilla_mcdoc.data.recipe.TransmuteResult import TransmuteResult
from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds
from vanilla_mcdoc.world.component.DataComponentPatch import DataComponentPatch
from vanilla_mcdoc.world.component.item.SuspiciousStewEffect import SuspiciousStewEffect
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

ACACIA_BOAT = RecipeCraftingShaped(
    group='boat',
    pattern=['# #', '###'],
    key={'#': 'minecraft:acacia_planks'},
    result=ItemStackOfComponent(id='minecraft:acacia_boat'),
    type='minecraft:crafting_shaped',
)

ACACIA_BUTTON = RecipeCraftingShapeless(
    group='wooden_button',
    category=CraftingBookCategory.REDSTONE,
    ingredients=['minecraft:acacia_planks'],
    result=ItemStackOfComponent(id='minecraft:acacia_button'),
    type='minecraft:crafting_shapeless',
)

ACACIA_CHEST_BOAT = RecipeCraftingShapeless(
    group='chest_boat',
    ingredients=['minecraft:chest', 'minecraft:acacia_boat'],
    result=ItemStackOfComponent(id='minecraft:acacia_chest_boat'),
    type='minecraft:crafting_shapeless',
)

ACACIA_DOOR = RecipeCraftingShaped(
    group='wooden_door',
    category=CraftingBookCategory.REDSTONE,
    pattern=['##', '##', '##'],
    key={'#': 'minecraft:acacia_planks'},
    result=ItemStackOfComponent(id='minecraft:acacia_door', count=3),
    type='minecraft:crafting_shaped',
)

ACACIA_FENCE = RecipeCraftingShaped(
    group='wooden_fence',
    pattern=['W#W', 'W#W'],
    key={'#': 'minecraft:stick', 'W': 'minecraft:acacia_planks'},
    result=ItemStackOfComponent(id='minecraft:acacia_fence', count=3),
    type='minecraft:crafting_shaped',
)

ACACIA_FENCE_GATE = RecipeCraftingShaped(
    group='wooden_fence_gate',
    category=CraftingBookCategory.REDSTONE,
    pattern=['#W#', '#W#'],
    key={'#': 'minecraft:stick', 'W': 'minecraft:acacia_planks'},
    result=ItemStackOfComponent(id='minecraft:acacia_fence_gate'),
    type='minecraft:crafting_shaped',
)

ACACIA_HANGING_SIGN = RecipeCraftingShaped(
    group='wooden_hanging_sign',
    pattern=['X X', '###', '###'],
    key={'#': 'minecraft:stripped_acacia_log', 'X': 'minecraft:iron_chain'},
    result=ItemStackOfComponent(id='minecraft:acacia_hanging_sign', count=6),
    type='minecraft:crafting_shaped',
)

ACACIA_PLANKS = RecipeCraftingShapeless(
    group='planks',
    category=CraftingBookCategory.BUILDING,
    ingredients=['#minecraft:acacia_logs'],
    result=ItemStackOfComponent(id='minecraft:acacia_planks', count=4),
    type='minecraft:crafting_shapeless',
)

ACACIA_PRESSURE_PLATE = RecipeCraftingShaped(
    group='wooden_pressure_plate',
    category=CraftingBookCategory.REDSTONE,
    pattern=['##'],
    key={'#': 'minecraft:acacia_planks'},
    result=ItemStackOfComponent(id='minecraft:acacia_pressure_plate'),
    type='minecraft:crafting_shaped',
)

ACACIA_SHELF = RecipeCraftingShaped(
    group='shelf',
    pattern=['###', '   ', '###'],
    key={'#': 'minecraft:stripped_acacia_log'},
    result=ItemStackOfComponent(id='minecraft:acacia_shelf', count=6),
    type='minecraft:crafting_shaped',
)

ACACIA_SIGN = RecipeCraftingShaped(
    group='wooden_sign',
    pattern=['###', '###', ' X '],
    key={'#': 'minecraft:acacia_planks', 'X': 'minecraft:stick'},
    result=ItemStackOfComponent(id='minecraft:acacia_sign', count=3),
    type='minecraft:crafting_shaped',
)

ACACIA_SLAB = RecipeCraftingShaped(
    group='wooden_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:acacia_planks'},
    result=ItemStackOfComponent(id='minecraft:acacia_slab', count=6),
    type='minecraft:crafting_shaped',
)

ACACIA_STAIRS = RecipeCraftingShaped(
    group='wooden_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:acacia_planks'},
    result=ItemStackOfComponent(id='minecraft:acacia_stairs', count=4),
    type='minecraft:crafting_shaped',
)

ACACIA_TRAPDOOR = RecipeCraftingShaped(
    group='wooden_trapdoor',
    category=CraftingBookCategory.REDSTONE,
    pattern=['###', '###'],
    key={'#': 'minecraft:acacia_planks'},
    result=ItemStackOfComponent(id='minecraft:acacia_trapdoor', count=2),
    type='minecraft:crafting_shaped',
)

ACACIA_WOOD = RecipeCraftingShaped(
    group='bark',
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:acacia_log'},
    result=ItemStackOfComponent(id='minecraft:acacia_wood', count=3),
    type='minecraft:crafting_shaped',
)

ACTIVATOR_RAIL = RecipeCraftingShaped(
    pattern=['XSX', 'X#X', 'XSX'],
    key={'#': 'minecraft:redstone_torch', 'S': 'minecraft:stick', 'X': 'minecraft:iron_ingot'},
    result=ItemStackOfComponent(id='minecraft:activator_rail', count=6),
    type='minecraft:crafting_shaped',
)

AMETHYST_BLOCK = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:amethyst_shard'},
    result=ItemStackOfComponent(id='minecraft:amethyst_block'),
    type='minecraft:crafting_shaped',
)

ANDESITE = RecipeCraftingShapeless(
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:diorite', 'minecraft:cobblestone'],
    result=ItemStackOfComponent(id='minecraft:andesite', count=2),
    type='minecraft:crafting_shapeless',
)

ANDESITE_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:andesite'},
    result=ItemStackOfComponent(id='minecraft:andesite_slab', count=6),
    type='minecraft:crafting_shaped',
)

ANDESITE_SLAB_FROM_ANDESITE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:andesite',
    result=ItemStackOfComponent(id='minecraft:andesite_slab', count=2),
    type='minecraft:stonecutting',
)

ANDESITE_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:andesite'},
    result=ItemStackOfComponent(id='minecraft:andesite_stairs', count=4),
    type='minecraft:crafting_shaped',
)

ANDESITE_STAIRS_FROM_ANDESITE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:andesite',
    result=ItemStackOfComponent(id='minecraft:andesite_stairs'),
    type='minecraft:stonecutting',
)

ANDESITE_WALL = RecipeCraftingShaped(
    pattern=['###', '###'],
    key={'#': 'minecraft:andesite'},
    result=ItemStackOfComponent(id='minecraft:andesite_wall', count=6),
    type='minecraft:crafting_shaped',
)

ANDESITE_WALL_FROM_ANDESITE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:andesite',
    result=ItemStackOfComponent(id='minecraft:andesite_wall'),
    type='minecraft:stonecutting',
)

ANVIL = RecipeCraftingShaped(
    pattern=['III', ' i ', 'iii'],
    key={'I': 'minecraft:iron_block', 'i': 'minecraft:iron_ingot'},
    result=ItemStackOfComponent(id='minecraft:anvil'),
    type='minecraft:crafting_shaped',
)

ARMOR_STAND = RecipeCraftingShaped(
    pattern=['///', ' / ', '/_/'],
    key={'/': 'minecraft:stick', '_': 'minecraft:smooth_stone_slab'},
    result=ItemStackOfComponent(id='minecraft:armor_stand'),
    type='minecraft:crafting_shaped',
)

ARROW = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['X', '#', 'Y'],
    key={'#': 'minecraft:stick', 'X': 'minecraft:flint', 'Y': 'minecraft:feather'},
    result=ItemStackOfComponent(id='minecraft:arrow', count=4),
    type='minecraft:crafting_shaped',
)

BAKED_POTATO = RecipeSmelting(
    category=CookingBookCategory.FOOD,
    ingredient='minecraft:potato',
    result=ItemStackOfComponent(id='minecraft:baked_potato'),
    experience=0.35,
    cookingtime=200,
    type='minecraft:smelting',
)

BAKED_POTATO_FROM_CAMPFIRE_COOKING = RecipeCampfireCooking(
    category=CookingBookCategory.FOOD,
    ingredient='minecraft:potato',
    result=ItemStackOfComponent(id='minecraft:baked_potato'),
    experience=0.35,
    cookingtime=600,
    type='minecraft:campfire_cooking',
)

BAKED_POTATO_FROM_SMOKING = RecipeSmoking(
    category=CookingBookCategory.FOOD,
    ingredient='minecraft:potato',
    result=ItemStackOfComponent(id='minecraft:baked_potato'),
    experience=0.35,
    cookingtime=200,
    type='minecraft:smoking',
)

BAMBOO_BLOCK = RecipeCraftingShapeless(
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:bamboo',
        'minecraft:bamboo',
        'minecraft:bamboo',
        'minecraft:bamboo',
        'minecraft:bamboo',
        'minecraft:bamboo',
        'minecraft:bamboo',
        'minecraft:bamboo',
        'minecraft:bamboo',
    ],
    result=ItemStackOfComponent(id='minecraft:bamboo_block'),
    type='minecraft:crafting_shapeless',
)

BAMBOO_BUTTON = RecipeCraftingShapeless(
    group='wooden_button',
    category=CraftingBookCategory.REDSTONE,
    ingredients=['minecraft:bamboo_planks'],
    result=ItemStackOfComponent(id='minecraft:bamboo_button'),
    type='minecraft:crafting_shapeless',
)

BAMBOO_CHEST_RAFT = RecipeCraftingShapeless(
    group='chest_boat',
    ingredients=['minecraft:chest', 'minecraft:bamboo_raft'],
    result=ItemStackOfComponent(id='minecraft:bamboo_chest_raft'),
    type='minecraft:crafting_shapeless',
)

BAMBOO_DOOR = RecipeCraftingShaped(
    group='wooden_door',
    category=CraftingBookCategory.REDSTONE,
    pattern=['##', '##', '##'],
    key={'#': 'minecraft:bamboo_planks'},
    result=ItemStackOfComponent(id='minecraft:bamboo_door', count=3),
    type='minecraft:crafting_shaped',
)

BAMBOO_FENCE = RecipeCraftingShaped(
    group='wooden_fence',
    pattern=['W#W', 'W#W'],
    key={'#': 'minecraft:stick', 'W': 'minecraft:bamboo_planks'},
    result=ItemStackOfComponent(id='minecraft:bamboo_fence', count=3),
    type='minecraft:crafting_shaped',
)

BAMBOO_FENCE_GATE = RecipeCraftingShaped(
    group='wooden_fence_gate',
    category=CraftingBookCategory.REDSTONE,
    pattern=['#W#', '#W#'],
    key={'#': 'minecraft:stick', 'W': 'minecraft:bamboo_planks'},
    result=ItemStackOfComponent(id='minecraft:bamboo_fence_gate'),
    type='minecraft:crafting_shaped',
)

BAMBOO_HANGING_SIGN = RecipeCraftingShaped(
    group='wooden_hanging_sign',
    pattern=['X X', '###', '###'],
    key={'#': 'minecraft:stripped_bamboo_block', 'X': 'minecraft:iron_chain'},
    result=ItemStackOfComponent(id='minecraft:bamboo_hanging_sign', count=6),
    type='minecraft:crafting_shaped',
)

BAMBOO_MOSAIC = RecipeCraftingShaped(
    pattern=['#', '#'],
    key={'#': 'minecraft:bamboo_slab'},
    result=ItemStackOfComponent(id='minecraft:bamboo_mosaic'),
    type='minecraft:crafting_shaped',
)

BAMBOO_MOSAIC_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:bamboo_mosaic'},
    result=ItemStackOfComponent(id='minecraft:bamboo_mosaic_slab', count=6),
    type='minecraft:crafting_shaped',
)

BAMBOO_MOSAIC_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:bamboo_mosaic'},
    result=ItemStackOfComponent(id='minecraft:bamboo_mosaic_stairs', count=4),
    type='minecraft:crafting_shaped',
)

BAMBOO_PLANKS = RecipeCraftingShapeless(
    group='planks',
    category=CraftingBookCategory.BUILDING,
    ingredients=['#minecraft:bamboo_blocks'],
    result=ItemStackOfComponent(id='minecraft:bamboo_planks', count=2),
    type='minecraft:crafting_shapeless',
)

BAMBOO_PRESSURE_PLATE = RecipeCraftingShaped(
    group='wooden_pressure_plate',
    category=CraftingBookCategory.REDSTONE,
    pattern=['##'],
    key={'#': 'minecraft:bamboo_planks'},
    result=ItemStackOfComponent(id='minecraft:bamboo_pressure_plate'),
    type='minecraft:crafting_shaped',
)

BAMBOO_RAFT = RecipeCraftingShaped(
    group='boat',
    pattern=['# #', '###'],
    key={'#': 'minecraft:bamboo_planks'},
    result=ItemStackOfComponent(id='minecraft:bamboo_raft'),
    type='minecraft:crafting_shaped',
)

BAMBOO_SHELF = RecipeCraftingShaped(
    group='shelf',
    pattern=['###', '   ', '###'],
    key={'#': 'minecraft:stripped_bamboo_block'},
    result=ItemStackOfComponent(id='minecraft:bamboo_shelf', count=6),
    type='minecraft:crafting_shaped',
)

BAMBOO_SIGN = RecipeCraftingShaped(
    group='wooden_sign',
    pattern=['###', '###', ' X '],
    key={'#': 'minecraft:bamboo_planks', 'X': 'minecraft:stick'},
    result=ItemStackOfComponent(id='minecraft:bamboo_sign', count=3),
    type='minecraft:crafting_shaped',
)

BAMBOO_SLAB = RecipeCraftingShaped(
    group='wooden_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:bamboo_planks'},
    result=ItemStackOfComponent(id='minecraft:bamboo_slab', count=6),
    type='minecraft:crafting_shaped',
)

BAMBOO_STAIRS = RecipeCraftingShaped(
    group='wooden_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:bamboo_planks'},
    result=ItemStackOfComponent(id='minecraft:bamboo_stairs', count=4),
    type='minecraft:crafting_shaped',
)

BAMBOO_TRAPDOOR = RecipeCraftingShaped(
    group='wooden_trapdoor',
    category=CraftingBookCategory.REDSTONE,
    pattern=['###', '###'],
    key={'#': 'minecraft:bamboo_planks'},
    result=ItemStackOfComponent(id='minecraft:bamboo_trapdoor', count=2),
    type='minecraft:crafting_shaped',
)

BARREL = RecipeCraftingShaped(
    pattern=['PSP', 'P P', 'PSP'],
    key={'P': '#minecraft:planks', 'S': '#minecraft:wooden_slabs'},
    result=ItemStackOfComponent(id='minecraft:barrel'),
    type='minecraft:crafting_shaped',
)

BEACON = RecipeCraftingShaped(
    pattern=['GGG', 'GSG', 'OOO'],
    key={'G': 'minecraft:glass', 'O': 'minecraft:obsidian', 'S': 'minecraft:nether_star'},
    result=ItemStackOfComponent(id='minecraft:beacon'),
    type='minecraft:crafting_shaped',
)

BEEHIVE = RecipeCraftingShaped(
    pattern=['PPP', 'HHH', 'PPP'],
    key={'H': 'minecraft:honeycomb', 'P': '#minecraft:planks'},
    result=ItemStackOfComponent(id='minecraft:beehive'),
    type='minecraft:crafting_shaped',
)

BEETROOT_SOUP = RecipeCraftingShapeless(
    ingredients=[
        'minecraft:bowl',
        'minecraft:beetroot',
        'minecraft:beetroot',
        'minecraft:beetroot',
        'minecraft:beetroot',
        'minecraft:beetroot',
        'minecraft:beetroot',
    ],
    result=ItemStackOfComponent(id='minecraft:beetroot_soup'),
    type='minecraft:crafting_shapeless',
)

BIRCH_BOAT = RecipeCraftingShaped(
    group='boat',
    pattern=['# #', '###'],
    key={'#': 'minecraft:birch_planks'},
    result=ItemStackOfComponent(id='minecraft:birch_boat'),
    type='minecraft:crafting_shaped',
)

BIRCH_BUTTON = RecipeCraftingShapeless(
    group='wooden_button',
    category=CraftingBookCategory.REDSTONE,
    ingredients=['minecraft:birch_planks'],
    result=ItemStackOfComponent(id='minecraft:birch_button'),
    type='minecraft:crafting_shapeless',
)

BIRCH_CHEST_BOAT = RecipeCraftingShapeless(
    group='chest_boat',
    ingredients=['minecraft:chest', 'minecraft:birch_boat'],
    result=ItemStackOfComponent(id='minecraft:birch_chest_boat'),
    type='minecraft:crafting_shapeless',
)

BIRCH_DOOR = RecipeCraftingShaped(
    group='wooden_door',
    category=CraftingBookCategory.REDSTONE,
    pattern=['##', '##', '##'],
    key={'#': 'minecraft:birch_planks'},
    result=ItemStackOfComponent(id='minecraft:birch_door', count=3),
    type='minecraft:crafting_shaped',
)

BIRCH_FENCE = RecipeCraftingShaped(
    group='wooden_fence',
    pattern=['W#W', 'W#W'],
    key={'#': 'minecraft:stick', 'W': 'minecraft:birch_planks'},
    result=ItemStackOfComponent(id='minecraft:birch_fence', count=3),
    type='minecraft:crafting_shaped',
)

BIRCH_FENCE_GATE = RecipeCraftingShaped(
    group='wooden_fence_gate',
    category=CraftingBookCategory.REDSTONE,
    pattern=['#W#', '#W#'],
    key={'#': 'minecraft:stick', 'W': 'minecraft:birch_planks'},
    result=ItemStackOfComponent(id='minecraft:birch_fence_gate'),
    type='minecraft:crafting_shaped',
)

BIRCH_HANGING_SIGN = RecipeCraftingShaped(
    group='wooden_hanging_sign',
    pattern=['X X', '###', '###'],
    key={'#': 'minecraft:stripped_birch_log', 'X': 'minecraft:iron_chain'},
    result=ItemStackOfComponent(id='minecraft:birch_hanging_sign', count=6),
    type='minecraft:crafting_shaped',
)

BIRCH_PLANKS = RecipeCraftingShapeless(
    group='planks',
    category=CraftingBookCategory.BUILDING,
    ingredients=['#minecraft:birch_logs'],
    result=ItemStackOfComponent(id='minecraft:birch_planks', count=4),
    type='minecraft:crafting_shapeless',
)

BIRCH_PRESSURE_PLATE = RecipeCraftingShaped(
    group='wooden_pressure_plate',
    category=CraftingBookCategory.REDSTONE,
    pattern=['##'],
    key={'#': 'minecraft:birch_planks'},
    result=ItemStackOfComponent(id='minecraft:birch_pressure_plate'),
    type='minecraft:crafting_shaped',
)

BIRCH_SHELF = RecipeCraftingShaped(
    group='shelf',
    pattern=['###', '   ', '###'],
    key={'#': 'minecraft:stripped_birch_log'},
    result=ItemStackOfComponent(id='minecraft:birch_shelf', count=6),
    type='minecraft:crafting_shaped',
)

BIRCH_SIGN = RecipeCraftingShaped(
    group='wooden_sign',
    pattern=['###', '###', ' X '],
    key={'#': 'minecraft:birch_planks', 'X': 'minecraft:stick'},
    result=ItemStackOfComponent(id='minecraft:birch_sign', count=3),
    type='minecraft:crafting_shaped',
)

BIRCH_SLAB = RecipeCraftingShaped(
    group='wooden_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:birch_planks'},
    result=ItemStackOfComponent(id='minecraft:birch_slab', count=6),
    type='minecraft:crafting_shaped',
)

BIRCH_STAIRS = RecipeCraftingShaped(
    group='wooden_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:birch_planks'},
    result=ItemStackOfComponent(id='minecraft:birch_stairs', count=4),
    type='minecraft:crafting_shaped',
)

BIRCH_TRAPDOOR = RecipeCraftingShaped(
    group='wooden_trapdoor',
    category=CraftingBookCategory.REDSTONE,
    pattern=['###', '###'],
    key={'#': 'minecraft:birch_planks'},
    result=ItemStackOfComponent(id='minecraft:birch_trapdoor', count=2),
    type='minecraft:crafting_shaped',
)

BIRCH_WOOD = RecipeCraftingShaped(
    group='bark',
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:birch_log'},
    result=ItemStackOfComponent(id='minecraft:birch_wood', count=3),
    type='minecraft:crafting_shaped',
)

BLACKSTONE_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:blackstone'},
    result=ItemStackOfComponent(id='minecraft:blackstone_slab', count=6),
    type='minecraft:crafting_shaped',
)

BLACKSTONE_SLAB_FROM_BLACKSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:blackstone',
    result=ItemStackOfComponent(id='minecraft:blackstone_slab', count=2),
    type='minecraft:stonecutting',
)

BLACKSTONE_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:blackstone'},
    result=ItemStackOfComponent(id='minecraft:blackstone_stairs', count=4),
    type='minecraft:crafting_shaped',
)

BLACKSTONE_STAIRS_FROM_BLACKSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:blackstone',
    result=ItemStackOfComponent(id='minecraft:blackstone_stairs'),
    type='minecraft:stonecutting',
)

BLACKSTONE_WALL = RecipeCraftingShaped(
    pattern=['###', '###'],
    key={'#': 'minecraft:blackstone'},
    result=ItemStackOfComponent(id='minecraft:blackstone_wall', count=6),
    type='minecraft:crafting_shaped',
)

BLACKSTONE_WALL_FROM_BLACKSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:blackstone',
    result=ItemStackOfComponent(id='minecraft:blackstone_wall'),
    type='minecraft:stonecutting',
)

BLACK_BANNER = RecipeCraftingShaped(
    group='banner',
    pattern=['###', '###', ' | '],
    key={'#': 'minecraft:black_wool', '|': 'minecraft:stick'},
    result=ItemStackOfComponent(id='minecraft:black_banner'),
    type='minecraft:crafting_shaped',
)

BLACK_BANNER_DUPLICATE = RecipeCraftingSpecialBannerduplicate(
    type='minecraft:crafting_special_bannerduplicate',
    **dict[str, Any]({'banner': 'minecraft:black_banner', 'result': {'id': 'minecraft:black_banner'}}),
)

BLACK_BED = RecipeCraftingShaped(
    group='bed',
    pattern=['###', 'XXX'],
    key={'#': 'minecraft:black_wool', 'X': '#minecraft:planks'},
    result=ItemStackOfComponent(id='minecraft:black_bed'),
    type='minecraft:crafting_shaped',
)

BLACK_BUNDLE = RecipeCraftingTransmute(
    group='bundle_dye',
    category=CraftingBookCategory.EQUIPMENT,
    input='#minecraft:bundles',
    material='minecraft:black_dye',
    result=TransmuteResult(id='minecraft:black_bundle'),
    type='minecraft:crafting_transmute',
)

BLACK_CANDLE = RecipeCraftingShapeless(
    group='dyed_candle',
    ingredients=['minecraft:candle', 'minecraft:black_dye'],
    result=ItemStackOfComponent(id='minecraft:black_candle'),
    type='minecraft:crafting_shapeless',
)

BLACK_CARPET = RecipeCraftingShaped(
    group='woolen_carpet',
    pattern=['##'],
    key={'#': 'minecraft:black_wool'},
    result=ItemStackOfComponent(id='minecraft:black_carpet', count=3),
    type='minecraft:crafting_shaped',
)

BLACK_CONCRETE_POWDER = RecipeCraftingShapeless(
    group='concrete_powder',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:black_dye',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:gravel',
        'minecraft:gravel',
        'minecraft:gravel',
        'minecraft:gravel',
    ],
    result=ItemStackOfComponent(id='minecraft:black_concrete_powder', count=8),
    type='minecraft:crafting_shapeless',
)

BLACK_CONCRETE_SLAB = RecipeCraftingShaped(
    group='concrete_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:black_concrete'},
    result=ItemStackOfComponent(id='minecraft:black_concrete_slab', count=6),
    type='minecraft:crafting_shaped',
)

BLACK_CONCRETE_SLAB_FROM_BLACK_CONCRETE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:black_concrete',
    result=ItemStackOfComponent(id='minecraft:black_concrete_slab', count=2),
    type='minecraft:stonecutting',
)

BLACK_CONCRETE_STAIRS = RecipeCraftingShaped(
    group='concrete_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:black_concrete'},
    result=ItemStackOfComponent(id='minecraft:black_concrete_stairs', count=4),
    type='minecraft:crafting_shaped',
)

BLACK_CONCRETE_STAIRS_FROM_BLACK_CONCRETE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:black_concrete',
    result=ItemStackOfComponent(id='minecraft:black_concrete_stairs'),
    type='minecraft:stonecutting',
)

BLACK_CUSHION = RecipeCraftingShaped(
    group='cushion',
    pattern=['###'],
    key={'#': 'minecraft:black_wool_slab'},
    result=ItemStackOfComponent(id='minecraft:black_cushion'),
    type='minecraft:crafting_shaped',
)

BLACK_DYE = RecipeCraftingShapeless(
    group='black_dye',
    ingredients=['minecraft:ink_sac'],
    result=ItemStackOfComponent(id='minecraft:black_dye'),
    type='minecraft:crafting_shapeless',
)

BLACK_DYE_FROM_WITHER_ROSE = RecipeCraftingShapeless(
    group='black_dye',
    ingredients=['minecraft:wither_rose'],
    result=ItemStackOfComponent(id='minecraft:black_dye'),
    type='minecraft:crafting_shapeless',
)

BLACK_GLAZED_TERRACOTTA = RecipeSmelting(
    category=CookingBookCategory.BLOCKS,
    ingredient='minecraft:black_terracotta',
    result=ItemStackOfComponent(id='minecraft:black_glazed_terracotta'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

BLACK_HARNESS = RecipeCraftingShaped(
    group='harness',
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['LLL', 'G#G'],
    key={'#': 'minecraft:black_wool', 'G': 'minecraft:glass', 'L': 'minecraft:leather'},
    result=ItemStackOfComponent(id='minecraft:black_harness'),
    type='minecraft:crafting_shaped',
)

BLACK_SHULKER_BOX = RecipeCraftingTransmute(
    group='shulker_box_dye',
    input='#minecraft:shulker_boxes',
    material='minecraft:black_dye',
    result=TransmuteResult(id='minecraft:black_shulker_box'),
    type='minecraft:crafting_transmute',
)

BLACK_STAINED_GLASS = RecipeCraftingShaped(
    group='stained_glass',
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:glass', 'X': 'minecraft:black_dye'},
    result=ItemStackOfComponent(id='minecraft:black_stained_glass', count=8),
    type='minecraft:crafting_shaped',
)

BLACK_STAINED_GLASS_PANE = RecipeCraftingShaped(
    group='stained_glass_pane',
    pattern=['###', '###'],
    key={'#': 'minecraft:black_stained_glass'},
    result=ItemStackOfComponent(id='minecraft:black_stained_glass_pane', count=16),
    type='minecraft:crafting_shaped',
)

BLACK_STAINED_GLASS_PANE_FROM_GLASS_PANE = RecipeCraftingShaped(
    group='stained_glass_pane',
    pattern=['###', '#$#', '###'],
    key={'#': 'minecraft:glass_pane', '$': 'minecraft:black_dye'},
    result=ItemStackOfComponent(id='minecraft:black_stained_glass_pane', count=8),
    type='minecraft:crafting_shaped',
)

BLACK_TERRACOTTA = RecipeCraftingShaped(
    group='stained_terracotta',
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:terracotta', 'X': 'minecraft:black_dye'},
    result=ItemStackOfComponent(id='minecraft:black_terracotta', count=8),
    type='minecraft:crafting_shaped',
)

BLACK_WOOL_SLAB = RecipeCraftingShaped(
    group='woolen_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:black_wool'},
    result=ItemStackOfComponent(id='minecraft:black_wool_slab', count=6),
    type='minecraft:crafting_shaped',
)

BLACK_WOOL_STAIRS = RecipeCraftingShaped(
    group='woolen_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:black_wool'},
    result=ItemStackOfComponent(id='minecraft:black_wool_stairs', count=4),
    type='minecraft:crafting_shaped',
)

BLAST_FURNACE = RecipeCraftingShaped(
    pattern=['III', 'IXI', '###'],
    key={'#': 'minecraft:smooth_stone', 'I': 'minecraft:iron_ingot', 'X': 'minecraft:furnace'},
    result=ItemStackOfComponent(id='minecraft:blast_furnace'),
    type='minecraft:crafting_shaped',
)

BLAZE_POWDER = RecipeCraftingShapeless(
    ingredients=['minecraft:blaze_rod'],
    result=ItemStackOfComponent(id='minecraft:blaze_powder', count=2),
    type='minecraft:crafting_shapeless',
)

BLUE_BANNER = RecipeCraftingShaped(
    group='banner',
    pattern=['###', '###', ' | '],
    key={'#': 'minecraft:blue_wool', '|': 'minecraft:stick'},
    result=ItemStackOfComponent(id='minecraft:blue_banner'),
    type='minecraft:crafting_shaped',
)

BLUE_BANNER_DUPLICATE = RecipeCraftingSpecialBannerduplicate(
    type='minecraft:crafting_special_bannerduplicate',
    **dict[str, Any]({'banner': 'minecraft:blue_banner', 'result': {'id': 'minecraft:blue_banner'}}),
)

BLUE_BED = RecipeCraftingShaped(
    group='bed',
    pattern=['###', 'XXX'],
    key={'#': 'minecraft:blue_wool', 'X': '#minecraft:planks'},
    result=ItemStackOfComponent(id='minecraft:blue_bed'),
    type='minecraft:crafting_shaped',
)

BLUE_BUNDLE = RecipeCraftingTransmute(
    group='bundle_dye',
    category=CraftingBookCategory.EQUIPMENT,
    input='#minecraft:bundles',
    material='minecraft:blue_dye',
    result=TransmuteResult(id='minecraft:blue_bundle'),
    type='minecraft:crafting_transmute',
)

BLUE_CANDLE = RecipeCraftingShapeless(
    group='dyed_candle',
    ingredients=['minecraft:candle', 'minecraft:blue_dye'],
    result=ItemStackOfComponent(id='minecraft:blue_candle'),
    type='minecraft:crafting_shapeless',
)

BLUE_CARPET = RecipeCraftingShaped(
    group='woolen_carpet',
    pattern=['##'],
    key={'#': 'minecraft:blue_wool'},
    result=ItemStackOfComponent(id='minecraft:blue_carpet', count=3),
    type='minecraft:crafting_shaped',
)

BLUE_CONCRETE_POWDER = RecipeCraftingShapeless(
    group='concrete_powder',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:blue_dye',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:gravel',
        'minecraft:gravel',
        'minecraft:gravel',
        'minecraft:gravel',
    ],
    result=ItemStackOfComponent(id='minecraft:blue_concrete_powder', count=8),
    type='minecraft:crafting_shapeless',
)

BLUE_CONCRETE_SLAB = RecipeCraftingShaped(
    group='concrete_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:blue_concrete'},
    result=ItemStackOfComponent(id='minecraft:blue_concrete_slab', count=6),
    type='minecraft:crafting_shaped',
)

BLUE_CONCRETE_SLAB_FROM_BLUE_CONCRETE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:blue_concrete',
    result=ItemStackOfComponent(id='minecraft:blue_concrete_slab', count=2),
    type='minecraft:stonecutting',
)

BLUE_CONCRETE_STAIRS = RecipeCraftingShaped(
    group='concrete_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:blue_concrete'},
    result=ItemStackOfComponent(id='minecraft:blue_concrete_stairs', count=4),
    type='minecraft:crafting_shaped',
)

BLUE_CONCRETE_STAIRS_FROM_BLUE_CONCRETE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:blue_concrete',
    result=ItemStackOfComponent(id='minecraft:blue_concrete_stairs'),
    type='minecraft:stonecutting',
)

BLUE_CUSHION = RecipeCraftingShaped(
    group='cushion',
    pattern=['###'],
    key={'#': 'minecraft:blue_wool_slab'},
    result=ItemStackOfComponent(id='minecraft:blue_cushion'),
    type='minecraft:crafting_shaped',
)

BLUE_DYE = RecipeCraftingShapeless(
    group='blue_dye',
    ingredients=['minecraft:lapis_lazuli'],
    result=ItemStackOfComponent(id='minecraft:blue_dye'),
    type='minecraft:crafting_shapeless',
)

BLUE_DYE_FROM_CORNFLOWER = RecipeCraftingShapeless(
    group='blue_dye',
    ingredients=['minecraft:cornflower'],
    result=ItemStackOfComponent(id='minecraft:blue_dye'),
    type='minecraft:crafting_shapeless',
)

BLUE_GLAZED_TERRACOTTA = RecipeSmelting(
    category=CookingBookCategory.BLOCKS,
    ingredient='minecraft:blue_terracotta',
    result=ItemStackOfComponent(id='minecraft:blue_glazed_terracotta'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

BLUE_HARNESS = RecipeCraftingShaped(
    group='harness',
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['LLL', 'G#G'],
    key={'#': 'minecraft:blue_wool', 'G': 'minecraft:glass', 'L': 'minecraft:leather'},
    result=ItemStackOfComponent(id='minecraft:blue_harness'),
    type='minecraft:crafting_shaped',
)

BLUE_ICE = RecipeCraftingShapeless(
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:packed_ice',
        'minecraft:packed_ice',
        'minecraft:packed_ice',
        'minecraft:packed_ice',
        'minecraft:packed_ice',
        'minecraft:packed_ice',
        'minecraft:packed_ice',
        'minecraft:packed_ice',
        'minecraft:packed_ice',
    ],
    result=ItemStackOfComponent(id='minecraft:blue_ice'),
    type='minecraft:crafting_shapeless',
)

BLUE_SHULKER_BOX = RecipeCraftingTransmute(
    group='shulker_box_dye',
    input='#minecraft:shulker_boxes',
    material='minecraft:blue_dye',
    result=TransmuteResult(id='minecraft:blue_shulker_box'),
    type='minecraft:crafting_transmute',
)

BLUE_STAINED_GLASS = RecipeCraftingShaped(
    group='stained_glass',
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:glass', 'X': 'minecraft:blue_dye'},
    result=ItemStackOfComponent(id='minecraft:blue_stained_glass', count=8),
    type='minecraft:crafting_shaped',
)

BLUE_STAINED_GLASS_PANE = RecipeCraftingShaped(
    group='stained_glass_pane',
    pattern=['###', '###'],
    key={'#': 'minecraft:blue_stained_glass'},
    result=ItemStackOfComponent(id='minecraft:blue_stained_glass_pane', count=16),
    type='minecraft:crafting_shaped',
)

BLUE_STAINED_GLASS_PANE_FROM_GLASS_PANE = RecipeCraftingShaped(
    group='stained_glass_pane',
    pattern=['###', '#$#', '###'],
    key={'#': 'minecraft:glass_pane', '$': 'minecraft:blue_dye'},
    result=ItemStackOfComponent(id='minecraft:blue_stained_glass_pane', count=8),
    type='minecraft:crafting_shaped',
)

BLUE_TERRACOTTA = RecipeCraftingShaped(
    group='stained_terracotta',
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:terracotta', 'X': 'minecraft:blue_dye'},
    result=ItemStackOfComponent(id='minecraft:blue_terracotta', count=8),
    type='minecraft:crafting_shaped',
)

BLUE_WOOL_SLAB = RecipeCraftingShaped(
    group='woolen_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:blue_wool'},
    result=ItemStackOfComponent(id='minecraft:blue_wool_slab', count=6),
    type='minecraft:crafting_shaped',
)

BLUE_WOOL_STAIRS = RecipeCraftingShaped(
    group='woolen_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:blue_wool'},
    result=ItemStackOfComponent(id='minecraft:blue_wool_stairs', count=4),
    type='minecraft:crafting_shaped',
)

BOLT_ARMOR_TRIM_SMITHING_TEMPLATE = RecipeCraftingShaped(
    pattern=['#S#', '#C#', '###'],
    key={
        '#': 'minecraft:diamond',
        'C': ['minecraft:copper_block', 'minecraft:waxed_copper_block'],
        'S': 'minecraft:bolt_armor_trim_smithing_template',
    },
    result=ItemStackOfComponent(id='minecraft:bolt_armor_trim_smithing_template', count=2),
    type='minecraft:crafting_shaped',
)

BOLT_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = RecipeSmithingTrim(
    base='#minecraft:trimmable_armor',
    addition='#minecraft:trim_materials',
    template='minecraft:bolt_armor_trim_smithing_template',
    pattern='minecraft:bolt',
    type='minecraft:smithing_trim',
)

BONE_BLOCK = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '###', '###'],
    key={'#': 'minecraft:bone_meal'},
    result=ItemStackOfComponent(id='minecraft:bone_block'),
    type='minecraft:crafting_shaped',
)

BONE_MEAL = RecipeCraftingShapeless(
    group='bonemeal',
    ingredients=['minecraft:bone'],
    result=ItemStackOfComponent(id='minecraft:bone_meal', count=3),
    type='minecraft:crafting_shapeless',
)

BONE_MEAL_FROM_BONE_BLOCK = RecipeCraftingShapeless(
    group='bonemeal',
    ingredients=['minecraft:bone_block'],
    result=ItemStackOfComponent(id='minecraft:bone_meal', count=9),
    type='minecraft:crafting_shapeless',
)

BOOK = RecipeCraftingShapeless(
    ingredients=['minecraft:paper', 'minecraft:paper', 'minecraft:paper', 'minecraft:leather'],
    result=ItemStackOfComponent(id='minecraft:book'),
    type='minecraft:crafting_shapeless',
)

BOOKSHELF = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###', 'XXX', '###'],
    key={'#': '#minecraft:planks', 'X': 'minecraft:book'},
    result=ItemStackOfComponent(id='minecraft:bookshelf'),
    type='minecraft:crafting_shaped',
)

BOOK_CLONING = RecipeCraftingSpecialBookcloning(
    type='minecraft:crafting_special_bookcloning',
    **dict[str, Any]({
        'material': '#minecraft:book_cloning_target',
        'result': {'id': 'minecraft:written_book'},
        'source': 'minecraft:written_book',
    }),
)

BORDURE_INDENTED_BANNER_PATTERN = RecipeCraftingShapeless(
    ingredients=['minecraft:paper', 'minecraft:vine'],
    result=ItemStackOfComponent(id='minecraft:bordure_indented_banner_pattern'),
    type='minecraft:crafting_shapeless',
)

BOW = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=[' #X', '# X', ' #X'],
    key={'#': 'minecraft:stick', 'X': 'minecraft:string'},
    result=ItemStackOfComponent(id='minecraft:bow'),
    type='minecraft:crafting_shaped',
)

BOWL = RecipeCraftingShaped(
    pattern=['# #', ' # '],
    key={'#': '#minecraft:planks'},
    result=ItemStackOfComponent(id='minecraft:bowl', count=4),
    type='minecraft:crafting_shaped',
)

BREAD = RecipeCraftingShaped(
    pattern=['###'],
    key={'#': 'minecraft:wheat'},
    result=ItemStackOfComponent(id='minecraft:bread'),
    type='minecraft:crafting_shaped',
)

BREWING_STAND = RecipeCraftingShaped(
    pattern=[' B ', '###'],
    key={'#': '#minecraft:stone_crafting_materials', 'B': 'minecraft:blaze_rod'},
    result=ItemStackOfComponent(id='minecraft:brewing_stand'),
    type='minecraft:crafting_shaped',
)

BRICK = RecipeSmelting(
    ingredient='minecraft:clay_ball',
    result=ItemStackOfComponent(id='minecraft:brick'),
    experience=0.3,
    cookingtime=200,
    type='minecraft:smelting',
)

BRICKS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:brick'},
    result=ItemStackOfComponent(id='minecraft:bricks'),
    type='minecraft:crafting_shaped',
)

BRICK_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:bricks'},
    result=ItemStackOfComponent(id='minecraft:brick_slab', count=6),
    type='minecraft:crafting_shaped',
)

BRICK_SLAB_FROM_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:bricks',
    result=ItemStackOfComponent(id='minecraft:brick_slab', count=2),
    type='minecraft:stonecutting',
)

BRICK_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:bricks'},
    result=ItemStackOfComponent(id='minecraft:brick_stairs', count=4),
    type='minecraft:crafting_shaped',
)

BRICK_STAIRS_FROM_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:bricks',
    result=ItemStackOfComponent(id='minecraft:brick_stairs'),
    type='minecraft:stonecutting',
)

BRICK_WALL = RecipeCraftingShaped(
    pattern=['###', '###'],
    key={'#': 'minecraft:bricks'},
    result=ItemStackOfComponent(id='minecraft:brick_wall', count=6),
    type='minecraft:crafting_shaped',
)

BRICK_WALL_FROM_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:bricks',
    result=ItemStackOfComponent(id='minecraft:brick_wall'),
    type='minecraft:stonecutting',
)

BROWN_BANNER = RecipeCraftingShaped(
    group='banner',
    pattern=['###', '###', ' | '],
    key={'#': 'minecraft:brown_wool', '|': 'minecraft:stick'},
    result=ItemStackOfComponent(id='minecraft:brown_banner'),
    type='minecraft:crafting_shaped',
)

BROWN_BANNER_DUPLICATE = RecipeCraftingSpecialBannerduplicate(
    type='minecraft:crafting_special_bannerduplicate',
    **dict[str, Any]({'banner': 'minecraft:brown_banner', 'result': {'id': 'minecraft:brown_banner'}}),
)

BROWN_BED = RecipeCraftingShaped(
    group='bed',
    pattern=['###', 'XXX'],
    key={'#': 'minecraft:brown_wool', 'X': '#minecraft:planks'},
    result=ItemStackOfComponent(id='minecraft:brown_bed'),
    type='minecraft:crafting_shaped',
)

BROWN_BUNDLE = RecipeCraftingTransmute(
    group='bundle_dye',
    category=CraftingBookCategory.EQUIPMENT,
    input='#minecraft:bundles',
    material='minecraft:brown_dye',
    result=TransmuteResult(id='minecraft:brown_bundle'),
    type='minecraft:crafting_transmute',
)

BROWN_CANDLE = RecipeCraftingShapeless(
    group='dyed_candle',
    ingredients=['minecraft:candle', 'minecraft:brown_dye'],
    result=ItemStackOfComponent(id='minecraft:brown_candle'),
    type='minecraft:crafting_shapeless',
)

BROWN_CARPET = RecipeCraftingShaped(
    group='woolen_carpet',
    pattern=['##'],
    key={'#': 'minecraft:brown_wool'},
    result=ItemStackOfComponent(id='minecraft:brown_carpet', count=3),
    type='minecraft:crafting_shaped',
)

BROWN_CONCRETE_POWDER = RecipeCraftingShapeless(
    group='concrete_powder',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:brown_dye',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:gravel',
        'minecraft:gravel',
        'minecraft:gravel',
        'minecraft:gravel',
    ],
    result=ItemStackOfComponent(id='minecraft:brown_concrete_powder', count=8),
    type='minecraft:crafting_shapeless',
)

BROWN_CONCRETE_SLAB = RecipeCraftingShaped(
    group='concrete_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:brown_concrete'},
    result=ItemStackOfComponent(id='minecraft:brown_concrete_slab', count=6),
    type='minecraft:crafting_shaped',
)

BROWN_CONCRETE_SLAB_FROM_BROWN_CONCRETE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:brown_concrete',
    result=ItemStackOfComponent(id='minecraft:brown_concrete_slab', count=2),
    type='minecraft:stonecutting',
)

BROWN_CONCRETE_STAIRS = RecipeCraftingShaped(
    group='concrete_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:brown_concrete'},
    result=ItemStackOfComponent(id='minecraft:brown_concrete_stairs', count=4),
    type='minecraft:crafting_shaped',
)

BROWN_CONCRETE_STAIRS_FROM_BROWN_CONCRETE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:brown_concrete',
    result=ItemStackOfComponent(id='minecraft:brown_concrete_stairs'),
    type='minecraft:stonecutting',
)

BROWN_CUSHION = RecipeCraftingShaped(
    group='cushion',
    pattern=['###'],
    key={'#': 'minecraft:brown_wool_slab'},
    result=ItemStackOfComponent(id='minecraft:brown_cushion'),
    type='minecraft:crafting_shaped',
)

BROWN_DYE = RecipeCraftingShapeless(
    group='brown_dye',
    ingredients=['minecraft:cocoa_beans'],
    result=ItemStackOfComponent(id='minecraft:brown_dye'),
    type='minecraft:crafting_shapeless',
)

BROWN_GLAZED_TERRACOTTA = RecipeSmelting(
    category=CookingBookCategory.BLOCKS,
    ingredient='minecraft:brown_terracotta',
    result=ItemStackOfComponent(id='minecraft:brown_glazed_terracotta'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

BROWN_HARNESS = RecipeCraftingShaped(
    group='harness',
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['LLL', 'G#G'],
    key={'#': 'minecraft:brown_wool', 'G': 'minecraft:glass', 'L': 'minecraft:leather'},
    result=ItemStackOfComponent(id='minecraft:brown_harness'),
    type='minecraft:crafting_shaped',
)

BROWN_SHULKER_BOX = RecipeCraftingTransmute(
    group='shulker_box_dye',
    input='#minecraft:shulker_boxes',
    material='minecraft:brown_dye',
    result=TransmuteResult(id='minecraft:brown_shulker_box'),
    type='minecraft:crafting_transmute',
)

BROWN_STAINED_GLASS = RecipeCraftingShaped(
    group='stained_glass',
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:glass', 'X': 'minecraft:brown_dye'},
    result=ItemStackOfComponent(id='minecraft:brown_stained_glass', count=8),
    type='minecraft:crafting_shaped',
)

BROWN_STAINED_GLASS_PANE = RecipeCraftingShaped(
    group='stained_glass_pane',
    pattern=['###', '###'],
    key={'#': 'minecraft:brown_stained_glass'},
    result=ItemStackOfComponent(id='minecraft:brown_stained_glass_pane', count=16),
    type='minecraft:crafting_shaped',
)

BROWN_STAINED_GLASS_PANE_FROM_GLASS_PANE = RecipeCraftingShaped(
    group='stained_glass_pane',
    pattern=['###', '#$#', '###'],
    key={'#': 'minecraft:glass_pane', '$': 'minecraft:brown_dye'},
    result=ItemStackOfComponent(id='minecraft:brown_stained_glass_pane', count=8),
    type='minecraft:crafting_shaped',
)

BROWN_TERRACOTTA = RecipeCraftingShaped(
    group='stained_terracotta',
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:terracotta', 'X': 'minecraft:brown_dye'},
    result=ItemStackOfComponent(id='minecraft:brown_terracotta', count=8),
    type='minecraft:crafting_shaped',
)

BROWN_WOOL_SLAB = RecipeCraftingShaped(
    group='woolen_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:brown_wool'},
    result=ItemStackOfComponent(id='minecraft:brown_wool_slab', count=6),
    type='minecraft:crafting_shaped',
)

BROWN_WOOL_STAIRS = RecipeCraftingShaped(
    group='woolen_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:brown_wool'},
    result=ItemStackOfComponent(id='minecraft:brown_wool_stairs', count=4),
    type='minecraft:crafting_shaped',
)

BRUSH = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['X', '#', 'I'],
    key={'#': 'minecraft:copper_ingot', 'I': 'minecraft:stick', 'X': 'minecraft:feather'},
    result=ItemStackOfComponent(id='minecraft:brush'),
    type='minecraft:crafting_shaped',
)

BUCKET = RecipeCraftingShaped(
    pattern=['# #', ' # '],
    key={'#': 'minecraft:iron_ingot'},
    result=ItemStackOfComponent(id='minecraft:bucket'),
    type='minecraft:crafting_shaped',
)

BUNDLE = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['-', '#'],
    key={'#': 'minecraft:leather', '-': 'minecraft:string'},
    result=ItemStackOfComponent(id='minecraft:bundle'),
    type='minecraft:crafting_shaped',
)

CAKE = RecipeCraftingShaped(
    pattern=['AAA', 'BEB', 'CCC'],
    key={'A': 'minecraft:milk_bucket', 'B': 'minecraft:sugar', 'C': 'minecraft:wheat', 'E': '#minecraft:eggs'},
    result=ItemStackOfComponent(id='minecraft:cake'),
    type='minecraft:crafting_shaped',
)

CALIBRATED_SCULK_SENSOR = RecipeCraftingShaped(
    category=CraftingBookCategory.REDSTONE,
    pattern=[' # ', '#X#'],
    key={'#': 'minecraft:amethyst_shard', 'X': 'minecraft:sculk_sensor'},
    result=ItemStackOfComponent(id='minecraft:calibrated_sculk_sensor'),
    type='minecraft:crafting_shaped',
)

CAMPFIRE = RecipeCraftingShaped(
    pattern=[' S ', 'SCS', 'LLL'],
    key={'C': '#minecraft:coals', 'L': '#minecraft:logs', 'S': 'minecraft:stick'},
    result=ItemStackOfComponent(id='minecraft:campfire'),
    type='minecraft:crafting_shaped',
)

CANDLE = RecipeCraftingShaped(
    pattern=['S', 'H'],
    key={'H': 'minecraft:honeycomb', 'S': 'minecraft:string'},
    result=ItemStackOfComponent(id='minecraft:candle'),
    type='minecraft:crafting_shaped',
)

CARROT_ON_A_STICK = RecipeCraftingShaped(
    pattern=['# ', ' X'],
    key={'#': 'minecraft:fishing_rod', 'X': 'minecraft:carrot'},
    result=ItemStackOfComponent(id='minecraft:carrot_on_a_stick'),
    type='minecraft:crafting_shaped',
)

CARTOGRAPHY_TABLE = RecipeCraftingShaped(
    pattern=['@@', '##', '##'],
    key={'#': '#minecraft:planks', '@': 'minecraft:paper'},
    result=ItemStackOfComponent(id='minecraft:cartography_table'),
    type='minecraft:crafting_shaped',
)

CAULDRON = RecipeCraftingShaped(
    pattern=['# #', '# #', '###'],
    key={'#': 'minecraft:iron_ingot'},
    result=ItemStackOfComponent(id='minecraft:cauldron'),
    type='minecraft:crafting_shaped',
)

CHARCOAL = RecipeSmelting(
    ingredient='#minecraft:logs_that_burn',
    result=ItemStackOfComponent(id='minecraft:charcoal'),
    experience=0.15,
    cookingtime=200,
    type='minecraft:smelting',
)

CHERRY_BOAT = RecipeCraftingShaped(
    group='boat',
    pattern=['# #', '###'],
    key={'#': 'minecraft:cherry_planks'},
    result=ItemStackOfComponent(id='minecraft:cherry_boat'),
    type='minecraft:crafting_shaped',
)

CHERRY_BUTTON = RecipeCraftingShapeless(
    group='wooden_button',
    category=CraftingBookCategory.REDSTONE,
    ingredients=['minecraft:cherry_planks'],
    result=ItemStackOfComponent(id='minecraft:cherry_button'),
    type='minecraft:crafting_shapeless',
)

CHERRY_CHEST_BOAT = RecipeCraftingShapeless(
    group='chest_boat',
    ingredients=['minecraft:chest', 'minecraft:cherry_boat'],
    result=ItemStackOfComponent(id='minecraft:cherry_chest_boat'),
    type='minecraft:crafting_shapeless',
)

CHERRY_DOOR = RecipeCraftingShaped(
    group='wooden_door',
    category=CraftingBookCategory.REDSTONE,
    pattern=['##', '##', '##'],
    key={'#': 'minecraft:cherry_planks'},
    result=ItemStackOfComponent(id='minecraft:cherry_door', count=3),
    type='minecraft:crafting_shaped',
)

CHERRY_FENCE = RecipeCraftingShaped(
    group='wooden_fence',
    pattern=['W#W', 'W#W'],
    key={'#': 'minecraft:stick', 'W': 'minecraft:cherry_planks'},
    result=ItemStackOfComponent(id='minecraft:cherry_fence', count=3),
    type='minecraft:crafting_shaped',
)

CHERRY_FENCE_GATE = RecipeCraftingShaped(
    group='wooden_fence_gate',
    category=CraftingBookCategory.REDSTONE,
    pattern=['#W#', '#W#'],
    key={'#': 'minecraft:stick', 'W': 'minecraft:cherry_planks'},
    result=ItemStackOfComponent(id='minecraft:cherry_fence_gate'),
    type='minecraft:crafting_shaped',
)

CHERRY_HANGING_SIGN = RecipeCraftingShaped(
    group='wooden_hanging_sign',
    pattern=['X X', '###', '###'],
    key={'#': 'minecraft:stripped_cherry_log', 'X': 'minecraft:iron_chain'},
    result=ItemStackOfComponent(id='minecraft:cherry_hanging_sign', count=6),
    type='minecraft:crafting_shaped',
)

CHERRY_PLANKS = RecipeCraftingShapeless(
    group='planks',
    category=CraftingBookCategory.BUILDING,
    ingredients=['#minecraft:cherry_logs'],
    result=ItemStackOfComponent(id='minecraft:cherry_planks', count=4),
    type='minecraft:crafting_shapeless',
)

CHERRY_PRESSURE_PLATE = RecipeCraftingShaped(
    group='wooden_pressure_plate',
    category=CraftingBookCategory.REDSTONE,
    pattern=['##'],
    key={'#': 'minecraft:cherry_planks'},
    result=ItemStackOfComponent(id='minecraft:cherry_pressure_plate'),
    type='minecraft:crafting_shaped',
)

CHERRY_SHELF = RecipeCraftingShaped(
    group='shelf',
    pattern=['###', '   ', '###'],
    key={'#': 'minecraft:stripped_cherry_log'},
    result=ItemStackOfComponent(id='minecraft:cherry_shelf', count=6),
    type='minecraft:crafting_shaped',
)

CHERRY_SIGN = RecipeCraftingShaped(
    group='wooden_sign',
    pattern=['###', '###', ' X '],
    key={'#': 'minecraft:cherry_planks', 'X': 'minecraft:stick'},
    result=ItemStackOfComponent(id='minecraft:cherry_sign', count=3),
    type='minecraft:crafting_shaped',
)

CHERRY_SLAB = RecipeCraftingShaped(
    group='wooden_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:cherry_planks'},
    result=ItemStackOfComponent(id='minecraft:cherry_slab', count=6),
    type='minecraft:crafting_shaped',
)

CHERRY_STAIRS = RecipeCraftingShaped(
    group='wooden_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:cherry_planks'},
    result=ItemStackOfComponent(id='minecraft:cherry_stairs', count=4),
    type='minecraft:crafting_shaped',
)

CHERRY_TRAPDOOR = RecipeCraftingShaped(
    group='wooden_trapdoor',
    category=CraftingBookCategory.REDSTONE,
    pattern=['###', '###'],
    key={'#': 'minecraft:cherry_planks'},
    result=ItemStackOfComponent(id='minecraft:cherry_trapdoor', count=2),
    type='minecraft:crafting_shaped',
)

CHERRY_WOOD = RecipeCraftingShaped(
    group='bark',
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:cherry_log'},
    result=ItemStackOfComponent(id='minecraft:cherry_wood', count=3),
    type='minecraft:crafting_shaped',
)

CHEST = RecipeCraftingShaped(
    pattern=['###', '# #', '###'],
    key={'#': '#minecraft:planks'},
    result=ItemStackOfComponent(id='minecraft:chest'),
    type='minecraft:crafting_shaped',
)

CHEST_MINECART = RecipeCraftingShapeless(
    ingredients=['minecraft:chest', 'minecraft:minecart'],
    result=ItemStackOfComponent(id='minecraft:chest_minecart'),
    type='minecraft:crafting_shapeless',
)

CHISELED_BOOKSHELF = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###', 'XXX', '###'],
    key={'#': '#minecraft:planks', 'X': '#minecraft:wooden_slabs'},
    result=ItemStackOfComponent(id='minecraft:chiseled_bookshelf'),
    type='minecraft:crafting_shaped',
)

CHISELED_CINNABAR = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#', '#'],
    key={'#': 'minecraft:cinnabar_slab'},
    result=ItemStackOfComponent(id='minecraft:chiseled_cinnabar'),
    type='minecraft:crafting_shaped',
)

CHISELED_CINNABAR_FROM_CINNABAR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cinnabar',
    result=ItemStackOfComponent(id='minecraft:chiseled_cinnabar'),
    type='minecraft:stonecutting',
)

CHISELED_COPPER = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#', '#'],
    key={'#': 'minecraft:cut_copper_slab'},
    result=ItemStackOfComponent(id='minecraft:chiseled_copper'),
    type='minecraft:crafting_shaped',
)

CHISELED_COPPER_FROM_COPPER_BLOCK_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:copper_block',
    result=ItemStackOfComponent(id='minecraft:chiseled_copper', count=4),
    type='minecraft:stonecutting',
)

CHISELED_COPPER_FROM_CUT_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cut_copper',
    result=ItemStackOfComponent(id='minecraft:chiseled_copper'),
    type='minecraft:stonecutting',
)

CHISELED_DEEPSLATE = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#', '#'],
    key={'#': 'minecraft:cobbled_deepslate_slab'},
    result=ItemStackOfComponent(id='minecraft:chiseled_deepslate'),
    type='minecraft:crafting_shaped',
)

CHISELED_DEEPSLATE_FROM_COBBLED_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cobbled_deepslate',
    result=ItemStackOfComponent(id='minecraft:chiseled_deepslate'),
    type='minecraft:stonecutting',
)

CHISELED_DEEPSLATE_FROM_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:deepslate',
    result=ItemStackOfComponent(id='minecraft:chiseled_deepslate'),
    type='minecraft:stonecutting',
)

CHISELED_NETHER_BRICKS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#', '#'],
    key={'#': 'minecraft:nether_brick_slab'},
    result=ItemStackOfComponent(id='minecraft:chiseled_nether_bricks'),
    type='minecraft:crafting_shaped',
)

CHISELED_NETHER_BRICKS_FROM_NETHER_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:nether_bricks',
    result=ItemStackOfComponent(id='minecraft:chiseled_nether_bricks'),
    type='minecraft:stonecutting',
)

CHISELED_POLISHED_BLACKSTONE = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#', '#'],
    key={'#': 'minecraft:polished_blackstone_slab'},
    result=ItemStackOfComponent(id='minecraft:chiseled_polished_blackstone'),
    type='minecraft:crafting_shaped',
)

CHISELED_POLISHED_BLACKSTONE_FROM_BLACKSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:blackstone',
    result=ItemStackOfComponent(id='minecraft:chiseled_polished_blackstone'),
    type='minecraft:stonecutting',
)

CHISELED_POLISHED_BLACKSTONE_FROM_POLISHED_BLACKSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_blackstone',
    result=ItemStackOfComponent(id='minecraft:chiseled_polished_blackstone'),
    type='minecraft:stonecutting',
)

CHISELED_QUARTZ_BLOCK = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#', '#'],
    key={'#': 'minecraft:quartz_slab'},
    result=ItemStackOfComponent(id='minecraft:chiseled_quartz_block'),
    type='minecraft:crafting_shaped',
)

CHISELED_QUARTZ_BLOCK_FROM_QUARTZ_BLOCK_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:quartz_block',
    result=ItemStackOfComponent(id='minecraft:chiseled_quartz_block'),
    type='minecraft:stonecutting',
)

CHISELED_RED_SANDSTONE = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#', '#'],
    key={'#': 'minecraft:red_sandstone_slab'},
    result=ItemStackOfComponent(id='minecraft:chiseled_red_sandstone'),
    type='minecraft:crafting_shaped',
)

CHISELED_RED_SANDSTONE_FROM_RED_SANDSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:red_sandstone',
    result=ItemStackOfComponent(id='minecraft:chiseled_red_sandstone'),
    type='minecraft:stonecutting',
)

CHISELED_RESIN_BRICKS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#', '#'],
    key={'#': 'minecraft:resin_brick_slab'},
    result=ItemStackOfComponent(id='minecraft:chiseled_resin_bricks'),
    type='minecraft:crafting_shaped',
)

CHISELED_RESIN_BRICKS_FROM_RESIN_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:resin_bricks',
    result=ItemStackOfComponent(id='minecraft:chiseled_resin_bricks'),
    type='minecraft:stonecutting',
)

CHISELED_SANDSTONE = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#', '#'],
    key={'#': 'minecraft:sandstone_slab'},
    result=ItemStackOfComponent(id='minecraft:chiseled_sandstone'),
    type='minecraft:crafting_shaped',
)

CHISELED_SANDSTONE_FROM_SANDSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:sandstone',
    result=ItemStackOfComponent(id='minecraft:chiseled_sandstone'),
    type='minecraft:stonecutting',
)

CHISELED_STONE_BRICKS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#', '#'],
    key={'#': 'minecraft:stone_brick_slab'},
    result=ItemStackOfComponent(id='minecraft:chiseled_stone_bricks'),
    type='minecraft:crafting_shaped',
)

CHISELED_STONE_BRICKS_FROM_STONE_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:stone_bricks',
    result=ItemStackOfComponent(id='minecraft:chiseled_stone_bricks'),
    type='minecraft:stonecutting',
)

CHISELED_STONE_BRICKS_FROM_STONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:stone',
    result=ItemStackOfComponent(id='minecraft:chiseled_stone_bricks'),
    type='minecraft:stonecutting',
)

CHISELED_SULFUR = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#', '#'],
    key={'#': 'minecraft:sulfur_slab'},
    result=ItemStackOfComponent(id='minecraft:chiseled_sulfur'),
    type='minecraft:crafting_shaped',
)

CHISELED_SULFUR_FROM_SULFUR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:sulfur',
    result=ItemStackOfComponent(id='minecraft:chiseled_sulfur'),
    type='minecraft:stonecutting',
)

CHISELED_TUFF = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#', '#'],
    key={'#': 'minecraft:tuff_slab'},
    result=ItemStackOfComponent(id='minecraft:chiseled_tuff'),
    type='minecraft:crafting_shaped',
)

CHISELED_TUFF_BRICKS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#', '#'],
    key={'#': 'minecraft:tuff_brick_slab'},
    result=ItemStackOfComponent(id='minecraft:chiseled_tuff_bricks'),
    type='minecraft:crafting_shaped',
)

CHISELED_TUFF_BRICKS_FROM_POLISHED_TUFF_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_tuff',
    result=ItemStackOfComponent(id='minecraft:chiseled_tuff_bricks'),
    type='minecraft:stonecutting',
)

CHISELED_TUFF_BRICKS_FROM_TUFF_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:tuff_bricks',
    result=ItemStackOfComponent(id='minecraft:chiseled_tuff_bricks'),
    type='minecraft:stonecutting',
)

CHISELED_TUFF_BRICKS_FROM_TUFF_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:tuff',
    result=ItemStackOfComponent(id='minecraft:chiseled_tuff_bricks'),
    type='minecraft:stonecutting',
)

CHISELED_TUFF_FROM_TUFF_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:tuff',
    result=ItemStackOfComponent(id='minecraft:chiseled_tuff'),
    type='minecraft:stonecutting',
)

CINNABAR_BRICKS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:polished_cinnabar'},
    result=ItemStackOfComponent(id='minecraft:cinnabar_bricks', count=4),
    type='minecraft:crafting_shaped',
)

CINNABAR_BRICKS_FROM_CINNABAR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cinnabar',
    result=ItemStackOfComponent(id='minecraft:cinnabar_bricks'),
    type='minecraft:stonecutting',
)

CINNABAR_BRICKS_FROM_POLISHED_CINNABAR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_cinnabar',
    result=ItemStackOfComponent(id='minecraft:cinnabar_bricks'),
    type='minecraft:stonecutting',
)

CINNABAR_BRICK_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:cinnabar_bricks'},
    result=ItemStackOfComponent(id='minecraft:cinnabar_brick_slab', count=6),
    type='minecraft:crafting_shaped',
)

CINNABAR_BRICK_SLAB_FROM_CINNABAR_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cinnabar_bricks',
    result=ItemStackOfComponent(id='minecraft:cinnabar_brick_slab', count=2),
    type='minecraft:stonecutting',
)

CINNABAR_BRICK_SLAB_FROM_CINNABAR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cinnabar',
    result=ItemStackOfComponent(id='minecraft:cinnabar_brick_slab', count=2),
    type='minecraft:stonecutting',
)

CINNABAR_BRICK_SLAB_FROM_POLISHED_CINNABAR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_cinnabar',
    result=ItemStackOfComponent(id='minecraft:cinnabar_brick_slab', count=2),
    type='minecraft:stonecutting',
)

CINNABAR_BRICK_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:cinnabar_bricks'},
    result=ItemStackOfComponent(id='minecraft:cinnabar_brick_stairs', count=4),
    type='minecraft:crafting_shaped',
)

CINNABAR_BRICK_STAIRS_FROM_CINNABAR_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cinnabar_bricks',
    result=ItemStackOfComponent(id='minecraft:cinnabar_brick_stairs'),
    type='minecraft:stonecutting',
)

CINNABAR_BRICK_STAIRS_FROM_CINNABAR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cinnabar',
    result=ItemStackOfComponent(id='minecraft:cinnabar_brick_stairs'),
    type='minecraft:stonecutting',
)

CINNABAR_BRICK_STAIRS_FROM_POLISHED_CINNABAR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_cinnabar',
    result=ItemStackOfComponent(id='minecraft:cinnabar_brick_stairs'),
    type='minecraft:stonecutting',
)

CINNABAR_BRICK_WALL = RecipeCraftingShaped(
    pattern=['###', '###'],
    key={'#': 'minecraft:cinnabar_bricks'},
    result=ItemStackOfComponent(id='minecraft:cinnabar_brick_wall', count=6),
    type='minecraft:crafting_shaped',
)

CINNABAR_BRICK_WALL_FROM_CINNABAR_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cinnabar_bricks',
    result=ItemStackOfComponent(id='minecraft:cinnabar_brick_wall'),
    type='minecraft:stonecutting',
)

CINNABAR_BRICK_WALL_FROM_CINNABAR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cinnabar',
    result=ItemStackOfComponent(id='minecraft:cinnabar_brick_wall'),
    type='minecraft:stonecutting',
)

CINNABAR_BRICK_WALL_FROM_POLISHED_CINNABAR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_cinnabar',
    result=ItemStackOfComponent(id='minecraft:cinnabar_brick_wall'),
    type='minecraft:stonecutting',
)

CINNABAR_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:cinnabar'},
    result=ItemStackOfComponent(id='minecraft:cinnabar_slab', count=6),
    type='minecraft:crafting_shaped',
)

CINNABAR_SLAB_FROM_CINNABAR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cinnabar',
    result=ItemStackOfComponent(id='minecraft:cinnabar_slab', count=2),
    type='minecraft:stonecutting',
)

CINNABAR_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:cinnabar'},
    result=ItemStackOfComponent(id='minecraft:cinnabar_stairs', count=4),
    type='minecraft:crafting_shaped',
)

CINNABAR_STAIRS_FROM_CINNABAR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cinnabar',
    result=ItemStackOfComponent(id='minecraft:cinnabar_stairs'),
    type='minecraft:stonecutting',
)

CINNABAR_WALL = RecipeCraftingShaped(
    pattern=['###', '###'],
    key={'#': 'minecraft:cinnabar'},
    result=ItemStackOfComponent(id='minecraft:cinnabar_wall', count=6),
    type='minecraft:crafting_shaped',
)

CINNABAR_WALL_FROM_CINNABAR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cinnabar',
    result=ItemStackOfComponent(id='minecraft:cinnabar_wall'),
    type='minecraft:stonecutting',
)

CLAY = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:clay_ball'},
    result=ItemStackOfComponent(id='minecraft:clay'),
    type='minecraft:crafting_shaped',
)

CLOCK = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=[' # ', '#X#', ' # '],
    key={'#': 'minecraft:gold_ingot', 'X': 'minecraft:redstone'},
    result=ItemStackOfComponent(id='minecraft:clock'),
    type='minecraft:crafting_shaped',
)

COAL = RecipeCraftingShapeless(
    ingredients=['minecraft:coal_block'],
    result=ItemStackOfComponent(id='minecraft:coal', count=9),
    type='minecraft:crafting_shapeless',
)

COAL_BLOCK = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '###', '###'],
    key={'#': 'minecraft:coal'},
    result=ItemStackOfComponent(id='minecraft:coal_block'),
    type='minecraft:crafting_shaped',
)

COAL_FROM_BLASTING_COAL_ORE = RecipeBlasting(
    group='coal',
    ingredient='minecraft:coal_ore',
    result=ItemStackOfComponent(id='minecraft:coal'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:blasting',
)

COAL_FROM_BLASTING_DEEPSLATE_COAL_ORE = RecipeBlasting(
    group='coal',
    ingredient='minecraft:deepslate_coal_ore',
    result=ItemStackOfComponent(id='minecraft:coal'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:blasting',
)

COAL_FROM_SMELTING_COAL_ORE = RecipeSmelting(
    group='coal',
    ingredient='minecraft:coal_ore',
    result=ItemStackOfComponent(id='minecraft:coal'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

COAL_FROM_SMELTING_DEEPSLATE_COAL_ORE = RecipeSmelting(
    group='coal',
    ingredient='minecraft:deepslate_coal_ore',
    result=ItemStackOfComponent(id='minecraft:coal'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

COARSE_DIRT = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['DG', 'GD'],
    key={'D': 'minecraft:dirt', 'G': 'minecraft:gravel'},
    result=ItemStackOfComponent(id='minecraft:coarse_dirt', count=4),
    type='minecraft:crafting_shaped',
)

COAST_ARMOR_TRIM_SMITHING_TEMPLATE = RecipeCraftingShaped(
    pattern=['#S#', '#C#', '###'],
    key={'#': 'minecraft:diamond', 'C': 'minecraft:cobblestone', 'S': 'minecraft:coast_armor_trim_smithing_template'},
    result=ItemStackOfComponent(id='minecraft:coast_armor_trim_smithing_template', count=2),
    type='minecraft:crafting_shaped',
)

COAST_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = RecipeSmithingTrim(
    base='#minecraft:trimmable_armor',
    addition='#minecraft:trim_materials',
    template='minecraft:coast_armor_trim_smithing_template',
    pattern='minecraft:coast',
    type='minecraft:smithing_trim',
)

COBBLED_DEEPSLATE_FROM_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:deepslate',
    result=ItemStackOfComponent(id='minecraft:cobbled_deepslate'),
    type='minecraft:stonecutting',
)

COBBLED_DEEPSLATE_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:cobbled_deepslate'},
    result=ItemStackOfComponent(id='minecraft:cobbled_deepslate_slab', count=6),
    type='minecraft:crafting_shaped',
)

COBBLED_DEEPSLATE_SLAB_FROM_COBBLED_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cobbled_deepslate',
    result=ItemStackOfComponent(id='minecraft:cobbled_deepslate_slab', count=2),
    type='minecraft:stonecutting',
)

COBBLED_DEEPSLATE_SLAB_FROM_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:deepslate',
    result=ItemStackOfComponent(id='minecraft:cobbled_deepslate_slab', count=2),
    type='minecraft:stonecutting',
)

COBBLED_DEEPSLATE_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:cobbled_deepslate'},
    result=ItemStackOfComponent(id='minecraft:cobbled_deepslate_stairs', count=4),
    type='minecraft:crafting_shaped',
)

COBBLED_DEEPSLATE_STAIRS_FROM_COBBLED_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cobbled_deepslate',
    result=ItemStackOfComponent(id='minecraft:cobbled_deepslate_stairs'),
    type='minecraft:stonecutting',
)

COBBLED_DEEPSLATE_STAIRS_FROM_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:deepslate',
    result=ItemStackOfComponent(id='minecraft:cobbled_deepslate_stairs'),
    type='minecraft:stonecutting',
)

COBBLED_DEEPSLATE_WALL = RecipeCraftingShaped(
    pattern=['###', '###'],
    key={'#': 'minecraft:cobbled_deepslate'},
    result=ItemStackOfComponent(id='minecraft:cobbled_deepslate_wall', count=6),
    type='minecraft:crafting_shaped',
)

COBBLED_DEEPSLATE_WALL_FROM_COBBLED_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cobbled_deepslate',
    result=ItemStackOfComponent(id='minecraft:cobbled_deepslate_wall'),
    type='minecraft:stonecutting',
)

COBBLED_DEEPSLATE_WALL_FROM_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:deepslate',
    result=ItemStackOfComponent(id='minecraft:cobbled_deepslate_wall'),
    type='minecraft:stonecutting',
)

COBBLESTONE_FROM_STONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:stone',
    result=ItemStackOfComponent(id='minecraft:cobblestone'),
    type='minecraft:stonecutting',
)

COBBLESTONE_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:cobblestone'},
    result=ItemStackOfComponent(id='minecraft:cobblestone_slab', count=6),
    type='minecraft:crafting_shaped',
)

COBBLESTONE_SLAB_FROM_COBBLESTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cobblestone',
    result=ItemStackOfComponent(id='minecraft:cobblestone_slab', count=2),
    type='minecraft:stonecutting',
)

COBBLESTONE_SLAB_FROM_STONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:stone',
    result=ItemStackOfComponent(id='minecraft:cobblestone_slab', count=2),
    type='minecraft:stonecutting',
)

COBBLESTONE_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:cobblestone'},
    result=ItemStackOfComponent(id='minecraft:cobblestone_stairs', count=4),
    type='minecraft:crafting_shaped',
)

COBBLESTONE_STAIRS_FROM_COBBLESTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cobblestone',
    result=ItemStackOfComponent(id='minecraft:cobblestone_stairs'),
    type='minecraft:stonecutting',
)

COBBLESTONE_STAIRS_FROM_STONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:stone',
    result=ItemStackOfComponent(id='minecraft:cobblestone_stairs'),
    type='minecraft:stonecutting',
)

COBBLESTONE_WALL = RecipeCraftingShaped(
    pattern=['###', '###'],
    key={'#': 'minecraft:cobblestone'},
    result=ItemStackOfComponent(id='minecraft:cobblestone_wall', count=6),
    type='minecraft:crafting_shaped',
)

COBBLESTONE_WALL_FROM_COBBLESTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cobblestone',
    result=ItemStackOfComponent(id='minecraft:cobblestone_wall'),
    type='minecraft:stonecutting',
)

COBBLESTONE_WALL_FROM_STONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:stone',
    result=ItemStackOfComponent(id='minecraft:cobblestone_wall'),
    type='minecraft:stonecutting',
)

COMPARATOR = RecipeCraftingShaped(
    category=CraftingBookCategory.REDSTONE,
    pattern=[' # ', '#X#', 'III'],
    key={'#': 'minecraft:redstone_torch', 'I': 'minecraft:stone', 'X': 'minecraft:quartz'},
    result=ItemStackOfComponent(id='minecraft:comparator'),
    type='minecraft:crafting_shaped',
)

COMPASS = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=[' # ', '#X#', ' # '],
    key={'#': 'minecraft:iron_ingot', 'X': 'minecraft:redstone'},
    result=ItemStackOfComponent(id='minecraft:compass'),
    type='minecraft:crafting_shaped',
)

COMPOSTER = RecipeCraftingShaped(
    pattern=['# #', '# #', '###'],
    key={'#': '#minecraft:wooden_slabs'},
    result=ItemStackOfComponent(id='minecraft:composter'),
    type='minecraft:crafting_shaped',
)

CONDUIT = RecipeCraftingShaped(
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:nautilus_shell', 'X': 'minecraft:heart_of_the_sea'},
    result=ItemStackOfComponent(id='minecraft:conduit'),
    type='minecraft:crafting_shaped',
)

COOKED_BEEF = RecipeSmelting(
    category=CookingBookCategory.FOOD,
    ingredient='minecraft:beef',
    result=ItemStackOfComponent(id='minecraft:cooked_beef'),
    experience=0.35,
    cookingtime=200,
    type='minecraft:smelting',
)

COOKED_BEEF_FROM_CAMPFIRE_COOKING = RecipeCampfireCooking(
    category=CookingBookCategory.FOOD,
    ingredient='minecraft:beef',
    result=ItemStackOfComponent(id='minecraft:cooked_beef'),
    experience=0.35,
    cookingtime=600,
    type='minecraft:campfire_cooking',
)

COOKED_BEEF_FROM_SMOKING = RecipeSmoking(
    category=CookingBookCategory.FOOD,
    ingredient='minecraft:beef',
    result=ItemStackOfComponent(id='minecraft:cooked_beef'),
    experience=0.35,
    cookingtime=200,
    type='minecraft:smoking',
)

COOKED_CHICKEN = RecipeSmelting(
    category=CookingBookCategory.FOOD,
    ingredient='minecraft:chicken',
    result=ItemStackOfComponent(id='minecraft:cooked_chicken'),
    experience=0.35,
    cookingtime=200,
    type='minecraft:smelting',
)

COOKED_CHICKEN_FROM_CAMPFIRE_COOKING = RecipeCampfireCooking(
    category=CookingBookCategory.FOOD,
    ingredient='minecraft:chicken',
    result=ItemStackOfComponent(id='minecraft:cooked_chicken'),
    experience=0.35,
    cookingtime=600,
    type='minecraft:campfire_cooking',
)

COOKED_CHICKEN_FROM_SMOKING = RecipeSmoking(
    category=CookingBookCategory.FOOD,
    ingredient='minecraft:chicken',
    result=ItemStackOfComponent(id='minecraft:cooked_chicken'),
    experience=0.35,
    cookingtime=200,
    type='minecraft:smoking',
)

COOKED_COD = RecipeSmelting(
    category=CookingBookCategory.FOOD,
    ingredient='minecraft:cod',
    result=ItemStackOfComponent(id='minecraft:cooked_cod'),
    experience=0.35,
    cookingtime=200,
    type='minecraft:smelting',
)

COOKED_COD_FROM_CAMPFIRE_COOKING = RecipeCampfireCooking(
    category=CookingBookCategory.FOOD,
    ingredient='minecraft:cod',
    result=ItemStackOfComponent(id='minecraft:cooked_cod'),
    experience=0.35,
    cookingtime=600,
    type='minecraft:campfire_cooking',
)

COOKED_COD_FROM_SMOKING = RecipeSmoking(
    category=CookingBookCategory.FOOD,
    ingredient='minecraft:cod',
    result=ItemStackOfComponent(id='minecraft:cooked_cod'),
    experience=0.35,
    cookingtime=200,
    type='minecraft:smoking',
)

COOKED_MUTTON = RecipeSmelting(
    category=CookingBookCategory.FOOD,
    ingredient='minecraft:mutton',
    result=ItemStackOfComponent(id='minecraft:cooked_mutton'),
    experience=0.35,
    cookingtime=200,
    type='minecraft:smelting',
)

COOKED_MUTTON_FROM_CAMPFIRE_COOKING = RecipeCampfireCooking(
    category=CookingBookCategory.FOOD,
    ingredient='minecraft:mutton',
    result=ItemStackOfComponent(id='minecraft:cooked_mutton'),
    experience=0.35,
    cookingtime=600,
    type='minecraft:campfire_cooking',
)

COOKED_MUTTON_FROM_SMOKING = RecipeSmoking(
    category=CookingBookCategory.FOOD,
    ingredient='minecraft:mutton',
    result=ItemStackOfComponent(id='minecraft:cooked_mutton'),
    experience=0.35,
    cookingtime=200,
    type='minecraft:smoking',
)

COOKED_PORKCHOP = RecipeSmelting(
    category=CookingBookCategory.FOOD,
    ingredient='minecraft:porkchop',
    result=ItemStackOfComponent(id='minecraft:cooked_porkchop'),
    experience=0.35,
    cookingtime=200,
    type='minecraft:smelting',
)

COOKED_PORKCHOP_FROM_CAMPFIRE_COOKING = RecipeCampfireCooking(
    category=CookingBookCategory.FOOD,
    ingredient='minecraft:porkchop',
    result=ItemStackOfComponent(id='minecraft:cooked_porkchop'),
    experience=0.35,
    cookingtime=600,
    type='minecraft:campfire_cooking',
)

COOKED_PORKCHOP_FROM_SMOKING = RecipeSmoking(
    category=CookingBookCategory.FOOD,
    ingredient='minecraft:porkchop',
    result=ItemStackOfComponent(id='minecraft:cooked_porkchop'),
    experience=0.35,
    cookingtime=200,
    type='minecraft:smoking',
)

COOKED_RABBIT = RecipeSmelting(
    category=CookingBookCategory.FOOD,
    ingredient='minecraft:rabbit',
    result=ItemStackOfComponent(id='minecraft:cooked_rabbit'),
    experience=0.35,
    cookingtime=200,
    type='minecraft:smelting',
)

COOKED_RABBIT_FROM_CAMPFIRE_COOKING = RecipeCampfireCooking(
    category=CookingBookCategory.FOOD,
    ingredient='minecraft:rabbit',
    result=ItemStackOfComponent(id='minecraft:cooked_rabbit'),
    experience=0.35,
    cookingtime=600,
    type='minecraft:campfire_cooking',
)

COOKED_RABBIT_FROM_SMOKING = RecipeSmoking(
    category=CookingBookCategory.FOOD,
    ingredient='minecraft:rabbit',
    result=ItemStackOfComponent(id='minecraft:cooked_rabbit'),
    experience=0.35,
    cookingtime=200,
    type='minecraft:smoking',
)

COOKED_SALMON = RecipeSmelting(
    category=CookingBookCategory.FOOD,
    ingredient='minecraft:salmon',
    result=ItemStackOfComponent(id='minecraft:cooked_salmon'),
    experience=0.35,
    cookingtime=200,
    type='minecraft:smelting',
)

COOKED_SALMON_FROM_CAMPFIRE_COOKING = RecipeCampfireCooking(
    category=CookingBookCategory.FOOD,
    ingredient='minecraft:salmon',
    result=ItemStackOfComponent(id='minecraft:cooked_salmon'),
    experience=0.35,
    cookingtime=600,
    type='minecraft:campfire_cooking',
)

COOKED_SALMON_FROM_SMOKING = RecipeSmoking(
    category=CookingBookCategory.FOOD,
    ingredient='minecraft:salmon',
    result=ItemStackOfComponent(id='minecraft:cooked_salmon'),
    experience=0.35,
    cookingtime=200,
    type='minecraft:smoking',
)

COOKIE = RecipeCraftingShaped(
    pattern=['#X#'],
    key={'#': 'minecraft:wheat', 'X': 'minecraft:cocoa_beans'},
    result=ItemStackOfComponent(id='minecraft:cookie', count=8),
    type='minecraft:crafting_shaped',
)

COPPER_AXE = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['XX', 'X#', ' #'],
    key={'#': 'minecraft:stick', 'X': '#minecraft:copper_tool_materials'},
    result=ItemStackOfComponent(id='minecraft:copper_axe'),
    type='minecraft:crafting_shaped',
)

COPPER_BARS = RecipeCraftingShaped(
    pattern=['###', '###'],
    key={'#': 'minecraft:copper_ingot'},
    result=ItemStackOfComponent(id='minecraft:copper_bars', count=16),
    type='minecraft:crafting_shaped',
)

COPPER_BLOCK = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '###', '###'],
    key={'#': 'minecraft:copper_ingot'},
    result=ItemStackOfComponent(id='minecraft:copper_block'),
    type='minecraft:crafting_shaped',
)

COPPER_BOOTS = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['X X', 'X X'],
    key={'X': 'minecraft:copper_ingot'},
    result=ItemStackOfComponent(id='minecraft:copper_boots'),
    type='minecraft:crafting_shaped',
)

COPPER_BULB = RecipeCraftingShaped(
    group='copper_bulb',
    category=CraftingBookCategory.REDSTONE,
    pattern=[' C ', 'CBC', ' R '],
    key={'B': 'minecraft:blaze_rod', 'C': 'minecraft:copper_block', 'R': 'minecraft:redstone'},
    result=ItemStackOfComponent(id='minecraft:copper_bulb', count=4),
    type='minecraft:crafting_shaped',
)

COPPER_CHAIN = RecipeCraftingShaped(
    pattern=['N', 'I', 'N'],
    key={'I': 'minecraft:copper_ingot', 'N': 'minecraft:copper_nugget'},
    result=ItemStackOfComponent(id='minecraft:copper_chain'),
    type='minecraft:crafting_shaped',
)

COPPER_CHEST = RecipeCraftingShaped(
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:copper_ingot', 'X': 'minecraft:chest'},
    result=ItemStackOfComponent(id='minecraft:copper_chest'),
    type='minecraft:crafting_shaped',
)

COPPER_CHESTPLATE = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['X X', 'XXX', 'XXX'],
    key={'X': 'minecraft:copper_ingot'},
    result=ItemStackOfComponent(id='minecraft:copper_chestplate'),
    type='minecraft:crafting_shaped',
)

COPPER_DOOR = RecipeCraftingShaped(
    category=CraftingBookCategory.REDSTONE,
    pattern=['##', '##', '##'],
    key={'#': 'minecraft:copper_ingot'},
    result=ItemStackOfComponent(id='minecraft:copper_door', count=3),
    type='minecraft:crafting_shaped',
)

COPPER_GRATE = RecipeCraftingShaped(
    group='copper_grate',
    category=CraftingBookCategory.BUILDING,
    pattern=[' M ', 'M M', ' M '],
    key={'M': 'minecraft:copper_block'},
    result=ItemStackOfComponent(id='minecraft:copper_grate', count=4),
    type='minecraft:crafting_shaped',
)

COPPER_GRATE_FROM_COPPER_BLOCK_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:copper_block',
    result=ItemStackOfComponent(id='minecraft:copper_grate', count=4),
    type='minecraft:stonecutting',
)

COPPER_HELMET = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['XXX', 'X X'],
    key={'X': 'minecraft:copper_ingot'},
    result=ItemStackOfComponent(id='minecraft:copper_helmet'),
    type='minecraft:crafting_shaped',
)

COPPER_HOE = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['XX', ' #', ' #'],
    key={'#': 'minecraft:stick', 'X': '#minecraft:copper_tool_materials'},
    result=ItemStackOfComponent(id='minecraft:copper_hoe'),
    type='minecraft:crafting_shaped',
)

COPPER_INGOT = RecipeCraftingShapeless(
    group='copper_ingot',
    ingredients=['minecraft:copper_block'],
    result=ItemStackOfComponent(id='minecraft:copper_ingot', count=9),
    type='minecraft:crafting_shapeless',
)

COPPER_INGOT_FROM_BLASTING_COPPER_ORE = RecipeBlasting(
    group='copper_ingot',
    ingredient='minecraft:copper_ore',
    result=ItemStackOfComponent(id='minecraft:copper_ingot'),
    experience=0.7,
    cookingtime=200,
    type='minecraft:blasting',
)

COPPER_INGOT_FROM_BLASTING_DEEPSLATE_COPPER_ORE = RecipeBlasting(
    group='copper_ingot',
    ingredient='minecraft:deepslate_copper_ore',
    result=ItemStackOfComponent(id='minecraft:copper_ingot'),
    experience=0.7,
    cookingtime=200,
    type='minecraft:blasting',
)

COPPER_INGOT_FROM_BLASTING_RAW_COPPER = RecipeBlasting(
    group='copper_ingot',
    ingredient='minecraft:raw_copper',
    result=ItemStackOfComponent(id='minecraft:copper_ingot'),
    experience=0.7,
    cookingtime=200,
    type='minecraft:blasting',
)

COPPER_INGOT_FROM_NUGGETS = RecipeCraftingShaped(
    group='copper_ingot',
    pattern=['###', '###', '###'],
    key={'#': 'minecraft:copper_nugget'},
    result=ItemStackOfComponent(id='minecraft:copper_ingot'),
    type='minecraft:crafting_shaped',
)

COPPER_INGOT_FROM_SMELTING_COPPER_ORE = RecipeSmelting(
    group='copper_ingot',
    ingredient='minecraft:copper_ore',
    result=ItemStackOfComponent(id='minecraft:copper_ingot'),
    experience=0.7,
    cookingtime=200,
    type='minecraft:smelting',
)

COPPER_INGOT_FROM_SMELTING_DEEPSLATE_COPPER_ORE = RecipeSmelting(
    group='copper_ingot',
    ingredient='minecraft:deepslate_copper_ore',
    result=ItemStackOfComponent(id='minecraft:copper_ingot'),
    experience=0.7,
    cookingtime=200,
    type='minecraft:smelting',
)

COPPER_INGOT_FROM_SMELTING_RAW_COPPER = RecipeSmelting(
    group='copper_ingot',
    ingredient='minecraft:raw_copper',
    result=ItemStackOfComponent(id='minecraft:copper_ingot'),
    experience=0.7,
    cookingtime=200,
    type='minecraft:smelting',
)

COPPER_INGOT_FROM_WAXED_COPPER_BLOCK = RecipeCraftingShapeless(
    group='copper_ingot',
    ingredients=['minecraft:waxed_copper_block'],
    result=ItemStackOfComponent(id='minecraft:copper_ingot', count=9),
    type='minecraft:crafting_shapeless',
)

COPPER_LANTERN = RecipeCraftingShaped(
    pattern=['XXX', 'X#X', 'XXX'],
    key={'#': 'minecraft:copper_torch', 'X': 'minecraft:copper_nugget'},
    result=ItemStackOfComponent(id='minecraft:copper_lantern'),
    type='minecraft:crafting_shaped',
)

COPPER_LEGGINGS = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['XXX', 'X X', 'X X'],
    key={'X': 'minecraft:copper_ingot'},
    result=ItemStackOfComponent(id='minecraft:copper_leggings'),
    type='minecraft:crafting_shaped',
)

COPPER_NUGGET = RecipeCraftingShapeless(
    ingredients=['minecraft:copper_ingot'],
    result=ItemStackOfComponent(id='minecraft:copper_nugget', count=9),
    type='minecraft:crafting_shapeless',
)

COPPER_NUGGET_FROM_BLASTING = RecipeBlasting(
    ingredient=[
        'minecraft:copper_pickaxe',
        'minecraft:copper_shovel',
        'minecraft:copper_axe',
        'minecraft:copper_hoe',
        'minecraft:copper_sword',
        'minecraft:copper_spear',
        'minecraft:copper_helmet',
        'minecraft:copper_chestplate',
        'minecraft:copper_leggings',
        'minecraft:copper_boots',
        'minecraft:copper_horse_armor',
        'minecraft:copper_nautilus_armor',
    ],
    result=ItemStackOfComponent(id='minecraft:copper_nugget'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:blasting',
)

COPPER_NUGGET_FROM_SMELTING = RecipeSmelting(
    ingredient=[
        'minecraft:copper_pickaxe',
        'minecraft:copper_shovel',
        'minecraft:copper_axe',
        'minecraft:copper_hoe',
        'minecraft:copper_sword',
        'minecraft:copper_spear',
        'minecraft:copper_helmet',
        'minecraft:copper_chestplate',
        'minecraft:copper_leggings',
        'minecraft:copper_boots',
        'minecraft:copper_horse_armor',
        'minecraft:copper_nautilus_armor',
    ],
    result=ItemStackOfComponent(id='minecraft:copper_nugget'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

COPPER_PICKAXE = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['XXX', ' # ', ' # '],
    key={'#': 'minecraft:stick', 'X': '#minecraft:copper_tool_materials'},
    result=ItemStackOfComponent(id='minecraft:copper_pickaxe'),
    type='minecraft:crafting_shaped',
)

COPPER_SHOVEL = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['X', '#', '#'],
    key={'#': 'minecraft:stick', 'X': '#minecraft:copper_tool_materials'},
    result=ItemStackOfComponent(id='minecraft:copper_shovel'),
    type='minecraft:crafting_shaped',
)

COPPER_SPEAR = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['  X', ' # ', '#  '],
    key={'#': 'minecraft:stick', 'X': '#minecraft:copper_tool_materials'},
    result=ItemStackOfComponent(id='minecraft:copper_spear'),
    type='minecraft:crafting_shaped',
)

COPPER_SWORD = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['X', 'X', '#'],
    key={'#': 'minecraft:stick', 'X': '#minecraft:copper_tool_materials'},
    result=ItemStackOfComponent(id='minecraft:copper_sword'),
    type='minecraft:crafting_shaped',
)

COPPER_TORCH = RecipeCraftingShaped(
    pattern=['C', 'X', '#'],
    key={'#': 'minecraft:stick', 'C': 'minecraft:copper_nugget', 'X': ['minecraft:coal', 'minecraft:charcoal']},
    result=ItemStackOfComponent(id='minecraft:copper_torch', count=4),
    type='minecraft:crafting_shaped',
)

COPPER_TRAPDOOR = RecipeCraftingShaped(
    category=CraftingBookCategory.REDSTONE,
    pattern=['##', '##'],
    key={'#': 'minecraft:copper_ingot'},
    result=ItemStackOfComponent(id='minecraft:copper_trapdoor'),
    type='minecraft:crafting_shaped',
)

CRACKED_DEEPSLATE_BRICKS = RecipeSmelting(
    category=CookingBookCategory.BLOCKS,
    ingredient='minecraft:deepslate_bricks',
    result=ItemStackOfComponent(id='minecraft:cracked_deepslate_bricks'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

CRACKED_DEEPSLATE_TILES = RecipeSmelting(
    category=CookingBookCategory.BLOCKS,
    ingredient='minecraft:deepslate_tiles',
    result=ItemStackOfComponent(id='minecraft:cracked_deepslate_tiles'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

CRACKED_NETHER_BRICKS = RecipeSmelting(
    category=CookingBookCategory.BLOCKS,
    ingredient='minecraft:nether_bricks',
    result=ItemStackOfComponent(id='minecraft:cracked_nether_bricks'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

CRACKED_POLISHED_BLACKSTONE_BRICKS = RecipeSmelting(
    category=CookingBookCategory.BLOCKS,
    ingredient='minecraft:polished_blackstone_bricks',
    result=ItemStackOfComponent(id='minecraft:cracked_polished_blackstone_bricks'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

CRACKED_STONE_BRICKS = RecipeSmelting(
    category=CookingBookCategory.BLOCKS,
    ingredient='minecraft:stone_bricks',
    result=ItemStackOfComponent(id='minecraft:cracked_stone_bricks'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

CRAFTER = RecipeCraftingShaped(
    category=CraftingBookCategory.REDSTONE,
    pattern=['###', '#C#', 'RDR'],
    key={'#': 'minecraft:iron_ingot', 'C': 'minecraft:crafting_table', 'D': 'minecraft:dropper', 'R': 'minecraft:redstone'},
    result=ItemStackOfComponent(id='minecraft:crafter'),
    type='minecraft:crafting_shaped',
)

CRAFTING_TABLE = RecipeCraftingShaped(
    show_notification=False,
    pattern=['##', '##'],
    key={'#': '#minecraft:planks'},
    result=ItemStackOfComponent(id='minecraft:crafting_table'),
    type='minecraft:crafting_shaped',
)

CREAKING_HEART = RecipeCraftingShaped(
    pattern=[' L ', ' R ', ' L '],
    key={'L': 'minecraft:pale_oak_log', 'R': 'minecraft:resin_block'},
    result=ItemStackOfComponent(id='minecraft:creaking_heart'),
    type='minecraft:crafting_shaped',
)

CREEPER_BANNER_PATTERN = RecipeCraftingShapeless(
    ingredients=['minecraft:paper', 'minecraft:creeper_head'],
    result=ItemStackOfComponent(id='minecraft:creeper_banner_pattern'),
    type='minecraft:crafting_shapeless',
)

CRIMSON_BUTTON = RecipeCraftingShapeless(
    group='wooden_button',
    category=CraftingBookCategory.REDSTONE,
    ingredients=['minecraft:crimson_planks'],
    result=ItemStackOfComponent(id='minecraft:crimson_button'),
    type='minecraft:crafting_shapeless',
)

CRIMSON_DOOR = RecipeCraftingShaped(
    group='wooden_door',
    category=CraftingBookCategory.REDSTONE,
    pattern=['##', '##', '##'],
    key={'#': 'minecraft:crimson_planks'},
    result=ItemStackOfComponent(id='minecraft:crimson_door', count=3),
    type='minecraft:crafting_shaped',
)

CRIMSON_FENCE = RecipeCraftingShaped(
    group='wooden_fence',
    pattern=['W#W', 'W#W'],
    key={'#': 'minecraft:stick', 'W': 'minecraft:crimson_planks'},
    result=ItemStackOfComponent(id='minecraft:crimson_fence', count=3),
    type='minecraft:crafting_shaped',
)

CRIMSON_FENCE_GATE = RecipeCraftingShaped(
    group='wooden_fence_gate',
    category=CraftingBookCategory.REDSTONE,
    pattern=['#W#', '#W#'],
    key={'#': 'minecraft:stick', 'W': 'minecraft:crimson_planks'},
    result=ItemStackOfComponent(id='minecraft:crimson_fence_gate'),
    type='minecraft:crafting_shaped',
)

CRIMSON_HANGING_SIGN = RecipeCraftingShaped(
    group='wooden_hanging_sign',
    pattern=['X X', '###', '###'],
    key={'#': 'minecraft:stripped_crimson_stem', 'X': 'minecraft:iron_chain'},
    result=ItemStackOfComponent(id='minecraft:crimson_hanging_sign', count=6),
    type='minecraft:crafting_shaped',
)

CRIMSON_HYPHAE = RecipeCraftingShaped(
    group='bark',
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:crimson_stem'},
    result=ItemStackOfComponent(id='minecraft:crimson_hyphae', count=3),
    type='minecraft:crafting_shaped',
)

CRIMSON_PLANKS = RecipeCraftingShapeless(
    group='planks',
    category=CraftingBookCategory.BUILDING,
    ingredients=['#minecraft:crimson_stems'],
    result=ItemStackOfComponent(id='minecraft:crimson_planks', count=4),
    type='minecraft:crafting_shapeless',
)

CRIMSON_PRESSURE_PLATE = RecipeCraftingShaped(
    group='wooden_pressure_plate',
    category=CraftingBookCategory.REDSTONE,
    pattern=['##'],
    key={'#': 'minecraft:crimson_planks'},
    result=ItemStackOfComponent(id='minecraft:crimson_pressure_plate'),
    type='minecraft:crafting_shaped',
)

CRIMSON_SHELF = RecipeCraftingShaped(
    group='shelf',
    pattern=['###', '   ', '###'],
    key={'#': 'minecraft:stripped_crimson_stem'},
    result=ItemStackOfComponent(id='minecraft:crimson_shelf', count=6),
    type='minecraft:crafting_shaped',
)

CRIMSON_SIGN = RecipeCraftingShaped(
    group='wooden_sign',
    pattern=['###', '###', ' X '],
    key={'#': 'minecraft:crimson_planks', 'X': 'minecraft:stick'},
    result=ItemStackOfComponent(id='minecraft:crimson_sign', count=3),
    type='minecraft:crafting_shaped',
)

CRIMSON_SLAB = RecipeCraftingShaped(
    group='wooden_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:crimson_planks'},
    result=ItemStackOfComponent(id='minecraft:crimson_slab', count=6),
    type='minecraft:crafting_shaped',
)

CRIMSON_STAIRS = RecipeCraftingShaped(
    group='wooden_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:crimson_planks'},
    result=ItemStackOfComponent(id='minecraft:crimson_stairs', count=4),
    type='minecraft:crafting_shaped',
)

CRIMSON_TRAPDOOR = RecipeCraftingShaped(
    group='wooden_trapdoor',
    category=CraftingBookCategory.REDSTONE,
    pattern=['###', '###'],
    key={'#': 'minecraft:crimson_planks'},
    result=ItemStackOfComponent(id='minecraft:crimson_trapdoor', count=2),
    type='minecraft:crafting_shaped',
)

CROSSBOW = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['#&#', '~$~', ' # '],
    key={'#': 'minecraft:stick', '$': 'minecraft:tripwire_hook', '&': 'minecraft:iron_ingot', '~': 'minecraft:string'},
    result=ItemStackOfComponent(id='minecraft:crossbow'),
    type='minecraft:crafting_shaped',
)

CUT_COPPER = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:copper_block'},
    result=ItemStackOfComponent(id='minecraft:cut_copper', count=4),
    type='minecraft:crafting_shaped',
)

CUT_COPPER_FROM_COPPER_BLOCK_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:copper_block',
    result=ItemStackOfComponent(id='minecraft:cut_copper', count=4),
    type='minecraft:stonecutting',
)

CUT_COPPER_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:cut_copper'},
    result=ItemStackOfComponent(id='minecraft:cut_copper_slab', count=6),
    type='minecraft:crafting_shaped',
)

CUT_COPPER_SLAB_FROM_COPPER_BLOCK_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:copper_block',
    result=ItemStackOfComponent(id='minecraft:cut_copper_slab', count=8),
    type='minecraft:stonecutting',
)

CUT_COPPER_SLAB_FROM_CUT_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cut_copper',
    result=ItemStackOfComponent(id='minecraft:cut_copper_slab', count=2),
    type='minecraft:stonecutting',
)

CUT_COPPER_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:cut_copper'},
    result=ItemStackOfComponent(id='minecraft:cut_copper_stairs', count=4),
    type='minecraft:crafting_shaped',
)

CUT_COPPER_STAIRS_FROM_COPPER_BLOCK_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:copper_block',
    result=ItemStackOfComponent(id='minecraft:cut_copper_stairs', count=4),
    type='minecraft:stonecutting',
)

CUT_COPPER_STAIRS_FROM_CUT_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cut_copper',
    result=ItemStackOfComponent(id='minecraft:cut_copper_stairs'),
    type='minecraft:stonecutting',
)

CUT_RED_SANDSTONE = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:red_sandstone'},
    result=ItemStackOfComponent(id='minecraft:cut_red_sandstone', count=4),
    type='minecraft:crafting_shaped',
)

CUT_RED_SANDSTONE_FROM_RED_SANDSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:red_sandstone',
    result=ItemStackOfComponent(id='minecraft:cut_red_sandstone'),
    type='minecraft:stonecutting',
)

CUT_RED_SANDSTONE_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:cut_red_sandstone'},
    result=ItemStackOfComponent(id='minecraft:cut_red_sandstone_slab', count=6),
    type='minecraft:crafting_shaped',
)

CUT_RED_SANDSTONE_SLAB_FROM_CUT_RED_SANDSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cut_red_sandstone',
    result=ItemStackOfComponent(id='minecraft:cut_red_sandstone_slab', count=2),
    type='minecraft:stonecutting',
)

CUT_RED_SANDSTONE_SLAB_FROM_RED_SANDSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:red_sandstone',
    result=ItemStackOfComponent(id='minecraft:cut_red_sandstone_slab', count=2),
    type='minecraft:stonecutting',
)

CUT_SANDSTONE = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:sandstone'},
    result=ItemStackOfComponent(id='minecraft:cut_sandstone', count=4),
    type='minecraft:crafting_shaped',
)

CUT_SANDSTONE_FROM_SANDSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:sandstone',
    result=ItemStackOfComponent(id='minecraft:cut_sandstone'),
    type='minecraft:stonecutting',
)

CUT_SANDSTONE_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:cut_sandstone'},
    result=ItemStackOfComponent(id='minecraft:cut_sandstone_slab', count=6),
    type='minecraft:crafting_shaped',
)

CUT_SANDSTONE_SLAB_FROM_CUT_SANDSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cut_sandstone',
    result=ItemStackOfComponent(id='minecraft:cut_sandstone_slab', count=2),
    type='minecraft:stonecutting',
)

CUT_SANDSTONE_SLAB_FROM_SANDSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:sandstone',
    result=ItemStackOfComponent(id='minecraft:cut_sandstone_slab', count=2),
    type='minecraft:stonecutting',
)

CYAN_BANNER = RecipeCraftingShaped(
    group='banner',
    pattern=['###', '###', ' | '],
    key={'#': 'minecraft:cyan_wool', '|': 'minecraft:stick'},
    result=ItemStackOfComponent(id='minecraft:cyan_banner'),
    type='minecraft:crafting_shaped',
)

CYAN_BANNER_DUPLICATE = RecipeCraftingSpecialBannerduplicate(
    type='minecraft:crafting_special_bannerduplicate',
    **dict[str, Any]({'banner': 'minecraft:cyan_banner', 'result': {'id': 'minecraft:cyan_banner'}}),
)

CYAN_BED = RecipeCraftingShaped(
    group='bed',
    pattern=['###', 'XXX'],
    key={'#': 'minecraft:cyan_wool', 'X': '#minecraft:planks'},
    result=ItemStackOfComponent(id='minecraft:cyan_bed'),
    type='minecraft:crafting_shaped',
)

CYAN_BUNDLE = RecipeCraftingTransmute(
    group='bundle_dye',
    category=CraftingBookCategory.EQUIPMENT,
    input='#minecraft:bundles',
    material='minecraft:cyan_dye',
    result=TransmuteResult(id='minecraft:cyan_bundle'),
    type='minecraft:crafting_transmute',
)

CYAN_CANDLE = RecipeCraftingShapeless(
    group='dyed_candle',
    ingredients=['minecraft:candle', 'minecraft:cyan_dye'],
    result=ItemStackOfComponent(id='minecraft:cyan_candle'),
    type='minecraft:crafting_shapeless',
)

CYAN_CARPET = RecipeCraftingShaped(
    group='woolen_carpet',
    pattern=['##'],
    key={'#': 'minecraft:cyan_wool'},
    result=ItemStackOfComponent(id='minecraft:cyan_carpet', count=3),
    type='minecraft:crafting_shaped',
)

CYAN_CONCRETE_POWDER = RecipeCraftingShapeless(
    group='concrete_powder',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:cyan_dye',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:gravel',
        'minecraft:gravel',
        'minecraft:gravel',
        'minecraft:gravel',
    ],
    result=ItemStackOfComponent(id='minecraft:cyan_concrete_powder', count=8),
    type='minecraft:crafting_shapeless',
)

CYAN_CONCRETE_SLAB = RecipeCraftingShaped(
    group='concrete_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:cyan_concrete'},
    result=ItemStackOfComponent(id='minecraft:cyan_concrete_slab', count=6),
    type='minecraft:crafting_shaped',
)

CYAN_CONCRETE_SLAB_FROM_CYAN_CONCRETE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cyan_concrete',
    result=ItemStackOfComponent(id='minecraft:cyan_concrete_slab', count=2),
    type='minecraft:stonecutting',
)

CYAN_CONCRETE_STAIRS = RecipeCraftingShaped(
    group='concrete_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:cyan_concrete'},
    result=ItemStackOfComponent(id='minecraft:cyan_concrete_stairs', count=4),
    type='minecraft:crafting_shaped',
)

CYAN_CONCRETE_STAIRS_FROM_CYAN_CONCRETE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cyan_concrete',
    result=ItemStackOfComponent(id='minecraft:cyan_concrete_stairs'),
    type='minecraft:stonecutting',
)

CYAN_CUSHION = RecipeCraftingShaped(
    group='cushion',
    pattern=['###'],
    key={'#': 'minecraft:cyan_wool_slab'},
    result=ItemStackOfComponent(id='minecraft:cyan_cushion'),
    type='minecraft:crafting_shaped',
)

CYAN_DYE = RecipeCraftingShapeless(
    group='cyan_dye',
    ingredients=['minecraft:blue_dye', 'minecraft:green_dye'],
    result=ItemStackOfComponent(id='minecraft:cyan_dye', count=2),
    type='minecraft:crafting_shapeless',
)

CYAN_DYE_FROM_PITCHER_PLANT = RecipeCraftingShapeless(
    group='cyan_dye',
    ingredients=['minecraft:pitcher_plant'],
    result=ItemStackOfComponent(id='minecraft:cyan_dye', count=2),
    type='minecraft:crafting_shapeless',
)

CYAN_GLAZED_TERRACOTTA = RecipeSmelting(
    category=CookingBookCategory.BLOCKS,
    ingredient='minecraft:cyan_terracotta',
    result=ItemStackOfComponent(id='minecraft:cyan_glazed_terracotta'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

CYAN_HARNESS = RecipeCraftingShaped(
    group='harness',
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['LLL', 'G#G'],
    key={'#': 'minecraft:cyan_wool', 'G': 'minecraft:glass', 'L': 'minecraft:leather'},
    result=ItemStackOfComponent(id='minecraft:cyan_harness'),
    type='minecraft:crafting_shaped',
)

CYAN_SHULKER_BOX = RecipeCraftingTransmute(
    group='shulker_box_dye',
    input='#minecraft:shulker_boxes',
    material='minecraft:cyan_dye',
    result=TransmuteResult(id='minecraft:cyan_shulker_box'),
    type='minecraft:crafting_transmute',
)

CYAN_STAINED_GLASS = RecipeCraftingShaped(
    group='stained_glass',
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:glass', 'X': 'minecraft:cyan_dye'},
    result=ItemStackOfComponent(id='minecraft:cyan_stained_glass', count=8),
    type='minecraft:crafting_shaped',
)

CYAN_STAINED_GLASS_PANE = RecipeCraftingShaped(
    group='stained_glass_pane',
    pattern=['###', '###'],
    key={'#': 'minecraft:cyan_stained_glass'},
    result=ItemStackOfComponent(id='minecraft:cyan_stained_glass_pane', count=16),
    type='minecraft:crafting_shaped',
)

CYAN_STAINED_GLASS_PANE_FROM_GLASS_PANE = RecipeCraftingShaped(
    group='stained_glass_pane',
    pattern=['###', '#$#', '###'],
    key={'#': 'minecraft:glass_pane', '$': 'minecraft:cyan_dye'},
    result=ItemStackOfComponent(id='minecraft:cyan_stained_glass_pane', count=8),
    type='minecraft:crafting_shaped',
)

CYAN_TERRACOTTA = RecipeCraftingShaped(
    group='stained_terracotta',
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:terracotta', 'X': 'minecraft:cyan_dye'},
    result=ItemStackOfComponent(id='minecraft:cyan_terracotta', count=8),
    type='minecraft:crafting_shaped',
)

CYAN_WOOL_SLAB = RecipeCraftingShaped(
    group='woolen_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:cyan_wool'},
    result=ItemStackOfComponent(id='minecraft:cyan_wool_slab', count=6),
    type='minecraft:crafting_shaped',
)

CYAN_WOOL_STAIRS = RecipeCraftingShaped(
    group='woolen_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:cyan_wool'},
    result=ItemStackOfComponent(id='minecraft:cyan_wool_stairs', count=4),
    type='minecraft:crafting_shaped',
)

DARK_OAK_BOAT = RecipeCraftingShaped(
    group='boat',
    pattern=['# #', '###'],
    key={'#': 'minecraft:dark_oak_planks'},
    result=ItemStackOfComponent(id='minecraft:dark_oak_boat'),
    type='minecraft:crafting_shaped',
)

DARK_OAK_BUTTON = RecipeCraftingShapeless(
    group='wooden_button',
    category=CraftingBookCategory.REDSTONE,
    ingredients=['minecraft:dark_oak_planks'],
    result=ItemStackOfComponent(id='minecraft:dark_oak_button'),
    type='minecraft:crafting_shapeless',
)

DARK_OAK_CHEST_BOAT = RecipeCraftingShapeless(
    group='chest_boat',
    ingredients=['minecraft:chest', 'minecraft:dark_oak_boat'],
    result=ItemStackOfComponent(id='minecraft:dark_oak_chest_boat'),
    type='minecraft:crafting_shapeless',
)

DARK_OAK_DOOR = RecipeCraftingShaped(
    group='wooden_door',
    category=CraftingBookCategory.REDSTONE,
    pattern=['##', '##', '##'],
    key={'#': 'minecraft:dark_oak_planks'},
    result=ItemStackOfComponent(id='minecraft:dark_oak_door', count=3),
    type='minecraft:crafting_shaped',
)

DARK_OAK_FENCE = RecipeCraftingShaped(
    group='wooden_fence',
    pattern=['W#W', 'W#W'],
    key={'#': 'minecraft:stick', 'W': 'minecraft:dark_oak_planks'},
    result=ItemStackOfComponent(id='minecraft:dark_oak_fence', count=3),
    type='minecraft:crafting_shaped',
)

DARK_OAK_FENCE_GATE = RecipeCraftingShaped(
    group='wooden_fence_gate',
    category=CraftingBookCategory.REDSTONE,
    pattern=['#W#', '#W#'],
    key={'#': 'minecraft:stick', 'W': 'minecraft:dark_oak_planks'},
    result=ItemStackOfComponent(id='minecraft:dark_oak_fence_gate'),
    type='minecraft:crafting_shaped',
)

DARK_OAK_HANGING_SIGN = RecipeCraftingShaped(
    group='wooden_hanging_sign',
    pattern=['X X', '###', '###'],
    key={'#': 'minecraft:stripped_dark_oak_log', 'X': 'minecraft:iron_chain'},
    result=ItemStackOfComponent(id='minecraft:dark_oak_hanging_sign', count=6),
    type='minecraft:crafting_shaped',
)

DARK_OAK_PLANKS = RecipeCraftingShapeless(
    group='planks',
    category=CraftingBookCategory.BUILDING,
    ingredients=['#minecraft:dark_oak_logs'],
    result=ItemStackOfComponent(id='minecraft:dark_oak_planks', count=4),
    type='minecraft:crafting_shapeless',
)

DARK_OAK_PRESSURE_PLATE = RecipeCraftingShaped(
    group='wooden_pressure_plate',
    category=CraftingBookCategory.REDSTONE,
    pattern=['##'],
    key={'#': 'minecraft:dark_oak_planks'},
    result=ItemStackOfComponent(id='minecraft:dark_oak_pressure_plate'),
    type='minecraft:crafting_shaped',
)

DARK_OAK_SHELF = RecipeCraftingShaped(
    group='shelf',
    pattern=['###', '   ', '###'],
    key={'#': 'minecraft:stripped_dark_oak_log'},
    result=ItemStackOfComponent(id='minecraft:dark_oak_shelf', count=6),
    type='minecraft:crafting_shaped',
)

DARK_OAK_SIGN = RecipeCraftingShaped(
    group='wooden_sign',
    pattern=['###', '###', ' X '],
    key={'#': 'minecraft:dark_oak_planks', 'X': 'minecraft:stick'},
    result=ItemStackOfComponent(id='minecraft:dark_oak_sign', count=3),
    type='minecraft:crafting_shaped',
)

DARK_OAK_SLAB = RecipeCraftingShaped(
    group='wooden_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:dark_oak_planks'},
    result=ItemStackOfComponent(id='minecraft:dark_oak_slab', count=6),
    type='minecraft:crafting_shaped',
)

DARK_OAK_STAIRS = RecipeCraftingShaped(
    group='wooden_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:dark_oak_planks'},
    result=ItemStackOfComponent(id='minecraft:dark_oak_stairs', count=4),
    type='minecraft:crafting_shaped',
)

DARK_OAK_TRAPDOOR = RecipeCraftingShaped(
    group='wooden_trapdoor',
    category=CraftingBookCategory.REDSTONE,
    pattern=['###', '###'],
    key={'#': 'minecraft:dark_oak_planks'},
    result=ItemStackOfComponent(id='minecraft:dark_oak_trapdoor', count=2),
    type='minecraft:crafting_shaped',
)

DARK_OAK_WOOD = RecipeCraftingShaped(
    group='bark',
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:dark_oak_log'},
    result=ItemStackOfComponent(id='minecraft:dark_oak_wood', count=3),
    type='minecraft:crafting_shaped',
)

DARK_PRISMARINE = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['SSS', 'SIS', 'SSS'],
    key={'I': 'minecraft:black_dye', 'S': 'minecraft:prismarine_shard'},
    result=ItemStackOfComponent(id='minecraft:dark_prismarine'),
    type='minecraft:crafting_shaped',
)

DARK_PRISMARINE_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:dark_prismarine'},
    result=ItemStackOfComponent(id='minecraft:dark_prismarine_slab', count=6),
    type='minecraft:crafting_shaped',
)

DARK_PRISMARINE_SLAB_FROM_DARK_PRISMARINE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:dark_prismarine',
    result=ItemStackOfComponent(id='minecraft:dark_prismarine_slab', count=2),
    type='minecraft:stonecutting',
)

DARK_PRISMARINE_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:dark_prismarine'},
    result=ItemStackOfComponent(id='minecraft:dark_prismarine_stairs', count=4),
    type='minecraft:crafting_shaped',
)

DARK_PRISMARINE_STAIRS_FROM_DARK_PRISMARINE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:dark_prismarine',
    result=ItemStackOfComponent(id='minecraft:dark_prismarine_stairs'),
    type='minecraft:stonecutting',
)

DAYLIGHT_DETECTOR = RecipeCraftingShaped(
    category=CraftingBookCategory.REDSTONE,
    pattern=['GGG', 'QQQ', 'WWW'],
    key={'G': 'minecraft:glass', 'Q': 'minecraft:quartz', 'W': '#minecraft:wooden_slabs'},
    result=ItemStackOfComponent(id='minecraft:daylight_detector'),
    type='minecraft:crafting_shaped',
)

DECORATED_POT = RecipeCraftingDecoratedPot(
    type='minecraft:crafting_decorated_pot',
    **dict[str, Any]({
        'back': '#minecraft:decorated_pot_ingredients',
        'front': '#minecraft:decorated_pot_ingredients',
        'left': '#minecraft:decorated_pot_ingredients',
        'result': {'id': 'minecraft:decorated_pot'},
        'right': '#minecraft:decorated_pot_ingredients',
    }),
)

DECORATED_POT_SIMPLE = RecipeCraftingShaped(
    pattern=[' # ', '# #', ' # '],
    key={'#': 'minecraft:brick'},
    result=ItemStackOfComponent(id='minecraft:decorated_pot'),
    type='minecraft:crafting_shaped',
)

DEEPSLATE = RecipeSmelting(
    category=CookingBookCategory.BLOCKS,
    ingredient='minecraft:cobbled_deepslate',
    result=ItemStackOfComponent(id='minecraft:deepslate'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

DEEPSLATE_BRICKS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:polished_deepslate'},
    result=ItemStackOfComponent(id='minecraft:deepslate_bricks', count=4),
    type='minecraft:crafting_shaped',
)

DEEPSLATE_BRICKS_FROM_COBBLED_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cobbled_deepslate',
    result=ItemStackOfComponent(id='minecraft:deepslate_bricks'),
    type='minecraft:stonecutting',
)

DEEPSLATE_BRICKS_FROM_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:deepslate',
    result=ItemStackOfComponent(id='minecraft:deepslate_bricks'),
    type='minecraft:stonecutting',
)

DEEPSLATE_BRICKS_FROM_POLISHED_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_deepslate',
    result=ItemStackOfComponent(id='minecraft:deepslate_bricks'),
    type='minecraft:stonecutting',
)

DEEPSLATE_BRICK_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:deepslate_bricks'},
    result=ItemStackOfComponent(id='minecraft:deepslate_brick_slab', count=6),
    type='minecraft:crafting_shaped',
)

DEEPSLATE_BRICK_SLAB_FROM_COBBLED_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cobbled_deepslate',
    result=ItemStackOfComponent(id='minecraft:deepslate_brick_slab', count=2),
    type='minecraft:stonecutting',
)

DEEPSLATE_BRICK_SLAB_FROM_DEEPSLATE_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:deepslate_bricks',
    result=ItemStackOfComponent(id='minecraft:deepslate_brick_slab', count=2),
    type='minecraft:stonecutting',
)

DEEPSLATE_BRICK_SLAB_FROM_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:deepslate',
    result=ItemStackOfComponent(id='minecraft:deepslate_brick_slab', count=2),
    type='minecraft:stonecutting',
)

DEEPSLATE_BRICK_SLAB_FROM_POLISHED_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_deepslate',
    result=ItemStackOfComponent(id='minecraft:deepslate_brick_slab', count=2),
    type='minecraft:stonecutting',
)

DEEPSLATE_BRICK_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:deepslate_bricks'},
    result=ItemStackOfComponent(id='minecraft:deepslate_brick_stairs', count=4),
    type='minecraft:crafting_shaped',
)

DEEPSLATE_BRICK_STAIRS_FROM_COBBLED_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cobbled_deepslate',
    result=ItemStackOfComponent(id='minecraft:deepslate_brick_stairs'),
    type='minecraft:stonecutting',
)

DEEPSLATE_BRICK_STAIRS_FROM_DEEPSLATE_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:deepslate_bricks',
    result=ItemStackOfComponent(id='minecraft:deepslate_brick_stairs'),
    type='minecraft:stonecutting',
)

DEEPSLATE_BRICK_STAIRS_FROM_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:deepslate',
    result=ItemStackOfComponent(id='minecraft:deepslate_brick_stairs'),
    type='minecraft:stonecutting',
)

DEEPSLATE_BRICK_STAIRS_FROM_POLISHED_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_deepslate',
    result=ItemStackOfComponent(id='minecraft:deepslate_brick_stairs'),
    type='minecraft:stonecutting',
)

DEEPSLATE_BRICK_WALL = RecipeCraftingShaped(
    pattern=['###', '###'],
    key={'#': 'minecraft:deepslate_bricks'},
    result=ItemStackOfComponent(id='minecraft:deepslate_brick_wall', count=6),
    type='minecraft:crafting_shaped',
)

DEEPSLATE_BRICK_WALL_FROM_COBBLED_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cobbled_deepslate',
    result=ItemStackOfComponent(id='minecraft:deepslate_brick_wall'),
    type='minecraft:stonecutting',
)

DEEPSLATE_BRICK_WALL_FROM_DEEPSLATE_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:deepslate_bricks',
    result=ItemStackOfComponent(id='minecraft:deepslate_brick_wall'),
    type='minecraft:stonecutting',
)

DEEPSLATE_BRICK_WALL_FROM_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:deepslate',
    result=ItemStackOfComponent(id='minecraft:deepslate_brick_wall'),
    type='minecraft:stonecutting',
)

DEEPSLATE_BRICK_WALL_FROM_POLISHED_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_deepslate',
    result=ItemStackOfComponent(id='minecraft:deepslate_brick_wall'),
    type='minecraft:stonecutting',
)

DEEPSLATE_TILES = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:deepslate_bricks'},
    result=ItemStackOfComponent(id='minecraft:deepslate_tiles', count=4),
    type='minecraft:crafting_shaped',
)

DEEPSLATE_TILES_FROM_COBBLED_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cobbled_deepslate',
    result=ItemStackOfComponent(id='minecraft:deepslate_tiles'),
    type='minecraft:stonecutting',
)

DEEPSLATE_TILES_FROM_DEEPSLATE_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:deepslate_bricks',
    result=ItemStackOfComponent(id='minecraft:deepslate_tiles'),
    type='minecraft:stonecutting',
)

DEEPSLATE_TILES_FROM_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:deepslate',
    result=ItemStackOfComponent(id='minecraft:deepslate_tiles'),
    type='minecraft:stonecutting',
)

DEEPSLATE_TILES_FROM_POLISHED_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_deepslate',
    result=ItemStackOfComponent(id='minecraft:deepslate_tiles'),
    type='minecraft:stonecutting',
)

DEEPSLATE_TILE_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:deepslate_tiles'},
    result=ItemStackOfComponent(id='minecraft:deepslate_tile_slab', count=6),
    type='minecraft:crafting_shaped',
)

DEEPSLATE_TILE_SLAB_FROM_COBBLED_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cobbled_deepslate',
    result=ItemStackOfComponent(id='minecraft:deepslate_tile_slab', count=2),
    type='minecraft:stonecutting',
)

DEEPSLATE_TILE_SLAB_FROM_DEEPSLATE_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:deepslate_bricks',
    result=ItemStackOfComponent(id='minecraft:deepslate_tile_slab', count=2),
    type='minecraft:stonecutting',
)

DEEPSLATE_TILE_SLAB_FROM_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:deepslate',
    result=ItemStackOfComponent(id='minecraft:deepslate_tile_slab', count=2),
    type='minecraft:stonecutting',
)

DEEPSLATE_TILE_SLAB_FROM_DEEPSLATE_TILES_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:deepslate_tiles',
    result=ItemStackOfComponent(id='minecraft:deepslate_tile_slab', count=2),
    type='minecraft:stonecutting',
)

DEEPSLATE_TILE_SLAB_FROM_POLISHED_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_deepslate',
    result=ItemStackOfComponent(id='minecraft:deepslate_tile_slab', count=2),
    type='minecraft:stonecutting',
)

DEEPSLATE_TILE_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:deepslate_tiles'},
    result=ItemStackOfComponent(id='minecraft:deepslate_tile_stairs', count=4),
    type='minecraft:crafting_shaped',
)

DEEPSLATE_TILE_STAIRS_FROM_COBBLED_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cobbled_deepslate',
    result=ItemStackOfComponent(id='minecraft:deepslate_tile_stairs'),
    type='minecraft:stonecutting',
)

DEEPSLATE_TILE_STAIRS_FROM_DEEPSLATE_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:deepslate_bricks',
    result=ItemStackOfComponent(id='minecraft:deepslate_tile_stairs'),
    type='minecraft:stonecutting',
)

DEEPSLATE_TILE_STAIRS_FROM_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:deepslate',
    result=ItemStackOfComponent(id='minecraft:deepslate_tile_stairs'),
    type='minecraft:stonecutting',
)

DEEPSLATE_TILE_STAIRS_FROM_DEEPSLATE_TILES_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:deepslate_tiles',
    result=ItemStackOfComponent(id='minecraft:deepslate_tile_stairs'),
    type='minecraft:stonecutting',
)

DEEPSLATE_TILE_STAIRS_FROM_POLISHED_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_deepslate',
    result=ItemStackOfComponent(id='minecraft:deepslate_tile_stairs'),
    type='minecraft:stonecutting',
)

DEEPSLATE_TILE_WALL = RecipeCraftingShaped(
    pattern=['###', '###'],
    key={'#': 'minecraft:deepslate_tiles'},
    result=ItemStackOfComponent(id='minecraft:deepslate_tile_wall', count=6),
    type='minecraft:crafting_shaped',
)

DEEPSLATE_TILE_WALL_FROM_COBBLED_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cobbled_deepslate',
    result=ItemStackOfComponent(id='minecraft:deepslate_tile_wall'),
    type='minecraft:stonecutting',
)

DEEPSLATE_TILE_WALL_FROM_DEEPSLATE_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:deepslate_bricks',
    result=ItemStackOfComponent(id='minecraft:deepslate_tile_wall'),
    type='minecraft:stonecutting',
)

DEEPSLATE_TILE_WALL_FROM_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:deepslate',
    result=ItemStackOfComponent(id='minecraft:deepslate_tile_wall'),
    type='minecraft:stonecutting',
)

DEEPSLATE_TILE_WALL_FROM_DEEPSLATE_TILES_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:deepslate_tiles',
    result=ItemStackOfComponent(id='minecraft:deepslate_tile_wall'),
    type='minecraft:stonecutting',
)

DEEPSLATE_TILE_WALL_FROM_POLISHED_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_deepslate',
    result=ItemStackOfComponent(id='minecraft:deepslate_tile_wall'),
    type='minecraft:stonecutting',
)

DETECTOR_RAIL = RecipeCraftingShaped(
    pattern=['X X', 'X#X', 'XRX'],
    key={'#': 'minecraft:stone_pressure_plate', 'R': 'minecraft:redstone', 'X': 'minecraft:iron_ingot'},
    result=ItemStackOfComponent(id='minecraft:detector_rail', count=6),
    type='minecraft:crafting_shaped',
)

DIAMOND = RecipeCraftingShapeless(
    ingredients=['minecraft:diamond_block'],
    result=ItemStackOfComponent(id='minecraft:diamond', count=9),
    type='minecraft:crafting_shapeless',
)

DIAMOND_AXE = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['XX', 'X#', ' #'],
    key={'#': 'minecraft:stick', 'X': '#minecraft:diamond_tool_materials'},
    result=ItemStackOfComponent(id='minecraft:diamond_axe'),
    type='minecraft:crafting_shaped',
)

DIAMOND_BLOCK = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '###', '###'],
    key={'#': 'minecraft:diamond'},
    result=ItemStackOfComponent(id='minecraft:diamond_block'),
    type='minecraft:crafting_shaped',
)

DIAMOND_BOOTS = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['X X', 'X X'],
    key={'X': 'minecraft:diamond'},
    result=ItemStackOfComponent(id='minecraft:diamond_boots'),
    type='minecraft:crafting_shaped',
)

DIAMOND_CHESTPLATE = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['X X', 'XXX', 'XXX'],
    key={'X': 'minecraft:diamond'},
    result=ItemStackOfComponent(id='minecraft:diamond_chestplate'),
    type='minecraft:crafting_shaped',
)

DIAMOND_FROM_BLASTING_DEEPSLATE_DIAMOND_ORE = RecipeBlasting(
    group='diamond',
    ingredient='minecraft:deepslate_diamond_ore',
    result=ItemStackOfComponent(id='minecraft:diamond'),
    experience=1.0,
    cookingtime=200,
    type='minecraft:blasting',
)

DIAMOND_FROM_BLASTING_DIAMOND_ORE = RecipeBlasting(
    group='diamond',
    ingredient='minecraft:diamond_ore',
    result=ItemStackOfComponent(id='minecraft:diamond'),
    experience=1.0,
    cookingtime=200,
    type='minecraft:blasting',
)

DIAMOND_FROM_SMELTING_DEEPSLATE_DIAMOND_ORE = RecipeSmelting(
    group='diamond',
    ingredient='minecraft:deepslate_diamond_ore',
    result=ItemStackOfComponent(id='minecraft:diamond'),
    experience=1.0,
    cookingtime=200,
    type='minecraft:smelting',
)

DIAMOND_FROM_SMELTING_DIAMOND_ORE = RecipeSmelting(
    group='diamond',
    ingredient='minecraft:diamond_ore',
    result=ItemStackOfComponent(id='minecraft:diamond'),
    experience=1.0,
    cookingtime=200,
    type='minecraft:smelting',
)

DIAMOND_HELMET = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['XXX', 'X X'],
    key={'X': 'minecraft:diamond'},
    result=ItemStackOfComponent(id='minecraft:diamond_helmet'),
    type='minecraft:crafting_shaped',
)

DIAMOND_HOE = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['XX', ' #', ' #'],
    key={'#': 'minecraft:stick', 'X': '#minecraft:diamond_tool_materials'},
    result=ItemStackOfComponent(id='minecraft:diamond_hoe'),
    type='minecraft:crafting_shaped',
)

DIAMOND_LEGGINGS = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['XXX', 'X X', 'X X'],
    key={'X': 'minecraft:diamond'},
    result=ItemStackOfComponent(id='minecraft:diamond_leggings'),
    type='minecraft:crafting_shaped',
)

DIAMOND_PICKAXE = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['XXX', ' # ', ' # '],
    key={'#': 'minecraft:stick', 'X': '#minecraft:diamond_tool_materials'},
    result=ItemStackOfComponent(id='minecraft:diamond_pickaxe'),
    type='minecraft:crafting_shaped',
)

DIAMOND_SHOVEL = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['X', '#', '#'],
    key={'#': 'minecraft:stick', 'X': '#minecraft:diamond_tool_materials'},
    result=ItemStackOfComponent(id='minecraft:diamond_shovel'),
    type='minecraft:crafting_shaped',
)

DIAMOND_SPEAR = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['  X', ' # ', '#  '],
    key={'#': 'minecraft:stick', 'X': '#minecraft:diamond_tool_materials'},
    result=ItemStackOfComponent(id='minecraft:diamond_spear'),
    type='minecraft:crafting_shaped',
)

DIAMOND_SWORD = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['X', 'X', '#'],
    key={'#': 'minecraft:stick', 'X': '#minecraft:diamond_tool_materials'},
    result=ItemStackOfComponent(id='minecraft:diamond_sword'),
    type='minecraft:crafting_shaped',
)

DIORITE = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['CQ', 'QC'],
    key={'C': 'minecraft:cobblestone', 'Q': 'minecraft:quartz'},
    result=ItemStackOfComponent(id='minecraft:diorite', count=2),
    type='minecraft:crafting_shaped',
)

DIORITE_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:diorite'},
    result=ItemStackOfComponent(id='minecraft:diorite_slab', count=6),
    type='minecraft:crafting_shaped',
)

DIORITE_SLAB_FROM_DIORITE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:diorite',
    result=ItemStackOfComponent(id='minecraft:diorite_slab', count=2),
    type='minecraft:stonecutting',
)

DIORITE_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:diorite'},
    result=ItemStackOfComponent(id='minecraft:diorite_stairs', count=4),
    type='minecraft:crafting_shaped',
)

DIORITE_STAIRS_FROM_DIORITE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:diorite',
    result=ItemStackOfComponent(id='minecraft:diorite_stairs'),
    type='minecraft:stonecutting',
)

DIORITE_WALL = RecipeCraftingShaped(
    pattern=['###', '###'],
    key={'#': 'minecraft:diorite'},
    result=ItemStackOfComponent(id='minecraft:diorite_wall', count=6),
    type='minecraft:crafting_shaped',
)

DIORITE_WALL_FROM_DIORITE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:diorite',
    result=ItemStackOfComponent(id='minecraft:diorite_wall'),
    type='minecraft:stonecutting',
)

DISPENSER = RecipeCraftingShaped(
    category=CraftingBookCategory.REDSTONE,
    pattern=['###', '#X#', '#R#'],
    key={'#': 'minecraft:cobblestone', 'R': 'minecraft:redstone', 'X': 'minecraft:bow'},
    result=ItemStackOfComponent(id='minecraft:dispenser'),
    type='minecraft:crafting_shaped',
)

DRIED_GHAST = RecipeCraftingShaped(
    group='dry_ghast',
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:ghast_tear', 'X': 'minecraft:soul_sand'},
    result=ItemStackOfComponent(id='minecraft:dried_ghast'),
    type='minecraft:crafting_shaped',
)

DRIED_KELP = RecipeCraftingShapeless(
    ingredients=['minecraft:dried_kelp_block'],
    result=ItemStackOfComponent(id='minecraft:dried_kelp', count=9),
    type='minecraft:crafting_shapeless',
)

DRIED_KELP_BLOCK = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '###', '###'],
    key={'#': 'minecraft:dried_kelp'},
    result=ItemStackOfComponent(id='minecraft:dried_kelp_block'),
    type='minecraft:crafting_shaped',
)

DRIED_KELP_FROM_CAMPFIRE_COOKING = RecipeCampfireCooking(
    category=CookingBookCategory.FOOD,
    ingredient='minecraft:kelp',
    result=ItemStackOfComponent(id='minecraft:dried_kelp'),
    experience=0.1,
    cookingtime=600,
    type='minecraft:campfire_cooking',
)

DRIED_KELP_FROM_SMELTING = RecipeSmelting(
    category=CookingBookCategory.FOOD,
    ingredient='minecraft:kelp',
    result=ItemStackOfComponent(id='minecraft:dried_kelp'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

DRIED_KELP_FROM_SMOKING = RecipeSmoking(
    category=CookingBookCategory.FOOD,
    ingredient='minecraft:kelp',
    result=ItemStackOfComponent(id='minecraft:dried_kelp'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smoking',
)

DRIPSTONE_BLOCK = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:pointed_dripstone'},
    result=ItemStackOfComponent(id='minecraft:dripstone_block'),
    type='minecraft:crafting_shaped',
)

DROPPER = RecipeCraftingShaped(
    category=CraftingBookCategory.REDSTONE,
    pattern=['###', '# #', '#R#'],
    key={'#': 'minecraft:cobblestone', 'R': 'minecraft:redstone'},
    result=ItemStackOfComponent(id='minecraft:dropper'),
    type='minecraft:crafting_shaped',
)

DUNE_ARMOR_TRIM_SMITHING_TEMPLATE = RecipeCraftingShaped(
    pattern=['#S#', '#C#', '###'],
    key={'#': 'minecraft:diamond', 'C': 'minecraft:sandstone', 'S': 'minecraft:dune_armor_trim_smithing_template'},
    result=ItemStackOfComponent(id='minecraft:dune_armor_trim_smithing_template', count=2),
    type='minecraft:crafting_shaped',
)

DUNE_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = RecipeSmithingTrim(
    base='#minecraft:trimmable_armor',
    addition='#minecraft:trim_materials',
    template='minecraft:dune_armor_trim_smithing_template',
    pattern='minecraft:dune',
    type='minecraft:smithing_trim',
)

DYE_BLACK_BED = RecipeCraftingShapeless(
    group='bed_dye',
    ingredients=[
        'minecraft:black_dye',
        [
            'minecraft:white_bed',
            'minecraft:orange_bed',
            'minecraft:magenta_bed',
            'minecraft:light_blue_bed',
            'minecraft:yellow_bed',
            'minecraft:lime_bed',
            'minecraft:pink_bed',
            'minecraft:gray_bed',
            'minecraft:light_gray_bed',
            'minecraft:cyan_bed',
            'minecraft:purple_bed',
            'minecraft:blue_bed',
            'minecraft:brown_bed',
            'minecraft:green_bed',
            'minecraft:red_bed',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:black_bed'),
    type='minecraft:crafting_shapeless',
)

DYE_BLACK_CARPET = RecipeCraftingShapeless(
    group='carpet_dye',
    ingredients=[
        'minecraft:black_dye',
        [
            'minecraft:white_carpet',
            'minecraft:orange_carpet',
            'minecraft:magenta_carpet',
            'minecraft:light_blue_carpet',
            'minecraft:yellow_carpet',
            'minecraft:lime_carpet',
            'minecraft:pink_carpet',
            'minecraft:gray_carpet',
            'minecraft:light_gray_carpet',
            'minecraft:cyan_carpet',
            'minecraft:purple_carpet',
            'minecraft:blue_carpet',
            'minecraft:brown_carpet',
            'minecraft:green_carpet',
            'minecraft:red_carpet',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:black_carpet'),
    type='minecraft:crafting_shapeless',
)

DYE_BLACK_CUSHION = RecipeCraftingShapeless(
    group='cushion_dye',
    ingredients=[
        'minecraft:black_dye',
        [
            'minecraft:white_cushion',
            'minecraft:orange_cushion',
            'minecraft:magenta_cushion',
            'minecraft:light_blue_cushion',
            'minecraft:yellow_cushion',
            'minecraft:lime_cushion',
            'minecraft:pink_cushion',
            'minecraft:gray_cushion',
            'minecraft:light_gray_cushion',
            'minecraft:cyan_cushion',
            'minecraft:purple_cushion',
            'minecraft:blue_cushion',
            'minecraft:brown_cushion',
            'minecraft:green_cushion',
            'minecraft:red_cushion',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:black_cushion'),
    type='minecraft:crafting_shapeless',
)

DYE_BLACK_HARNESS = RecipeCraftingShapeless(
    group='harness_dye',
    category=CraftingBookCategory.EQUIPMENT,
    ingredients=[
        'minecraft:black_dye',
        [
            'minecraft:white_harness',
            'minecraft:orange_harness',
            'minecraft:magenta_harness',
            'minecraft:light_blue_harness',
            'minecraft:yellow_harness',
            'minecraft:lime_harness',
            'minecraft:pink_harness',
            'minecraft:gray_harness',
            'minecraft:light_gray_harness',
            'minecraft:cyan_harness',
            'minecraft:purple_harness',
            'minecraft:blue_harness',
            'minecraft:brown_harness',
            'minecraft:green_harness',
            'minecraft:red_harness',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:black_harness'),
    type='minecraft:crafting_shapeless',
)

DYE_BLACK_WOOL = RecipeCraftingShapeless(
    group='wool',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:black_dye',
        [
            'minecraft:white_wool',
            'minecraft:orange_wool',
            'minecraft:magenta_wool',
            'minecraft:light_blue_wool',
            'minecraft:yellow_wool',
            'minecraft:lime_wool',
            'minecraft:pink_wool',
            'minecraft:gray_wool',
            'minecraft:light_gray_wool',
            'minecraft:cyan_wool',
            'minecraft:purple_wool',
            'minecraft:blue_wool',
            'minecraft:brown_wool',
            'minecraft:green_wool',
            'minecraft:red_wool',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:black_wool'),
    type='minecraft:crafting_shapeless',
)

DYE_BLACK_WOOL_SLAB = RecipeCraftingShapeless(
    group='wool_slabs',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:black_dye',
        [
            'minecraft:white_wool_slab',
            'minecraft:orange_wool_slab',
            'minecraft:magenta_wool_slab',
            'minecraft:light_blue_wool_slab',
            'minecraft:yellow_wool_slab',
            'minecraft:lime_wool_slab',
            'minecraft:pink_wool_slab',
            'minecraft:gray_wool_slab',
            'minecraft:light_gray_wool_slab',
            'minecraft:cyan_wool_slab',
            'minecraft:purple_wool_slab',
            'minecraft:blue_wool_slab',
            'minecraft:brown_wool_slab',
            'minecraft:green_wool_slab',
            'minecraft:red_wool_slab',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:black_wool_slab'),
    type='minecraft:crafting_shapeless',
)

DYE_BLACK_WOOL_STAIRS = RecipeCraftingShapeless(
    group='wool_stairs',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:black_dye',
        [
            'minecraft:white_wool_stairs',
            'minecraft:orange_wool_stairs',
            'minecraft:magenta_wool_stairs',
            'minecraft:light_blue_wool_stairs',
            'minecraft:yellow_wool_stairs',
            'minecraft:lime_wool_stairs',
            'minecraft:pink_wool_stairs',
            'minecraft:gray_wool_stairs',
            'minecraft:light_gray_wool_stairs',
            'minecraft:cyan_wool_stairs',
            'minecraft:purple_wool_stairs',
            'minecraft:blue_wool_stairs',
            'minecraft:brown_wool_stairs',
            'minecraft:green_wool_stairs',
            'minecraft:red_wool_stairs',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:black_wool_stairs'),
    type='minecraft:crafting_shapeless',
)

DYE_BLUE_BED = RecipeCraftingShapeless(
    group='bed_dye',
    ingredients=[
        'minecraft:blue_dye',
        [
            'minecraft:white_bed',
            'minecraft:orange_bed',
            'minecraft:magenta_bed',
            'minecraft:light_blue_bed',
            'minecraft:yellow_bed',
            'minecraft:lime_bed',
            'minecraft:pink_bed',
            'minecraft:gray_bed',
            'minecraft:light_gray_bed',
            'minecraft:cyan_bed',
            'minecraft:purple_bed',
            'minecraft:brown_bed',
            'minecraft:green_bed',
            'minecraft:red_bed',
            'minecraft:black_bed',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:blue_bed'),
    type='minecraft:crafting_shapeless',
)

DYE_BLUE_CARPET = RecipeCraftingShapeless(
    group='carpet_dye',
    ingredients=[
        'minecraft:blue_dye',
        [
            'minecraft:white_carpet',
            'minecraft:orange_carpet',
            'minecraft:magenta_carpet',
            'minecraft:light_blue_carpet',
            'minecraft:yellow_carpet',
            'minecraft:lime_carpet',
            'minecraft:pink_carpet',
            'minecraft:gray_carpet',
            'minecraft:light_gray_carpet',
            'minecraft:cyan_carpet',
            'minecraft:purple_carpet',
            'minecraft:brown_carpet',
            'minecraft:green_carpet',
            'minecraft:red_carpet',
            'minecraft:black_carpet',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:blue_carpet'),
    type='minecraft:crafting_shapeless',
)

DYE_BLUE_CUSHION = RecipeCraftingShapeless(
    group='cushion_dye',
    ingredients=[
        'minecraft:blue_dye',
        [
            'minecraft:white_cushion',
            'minecraft:orange_cushion',
            'minecraft:magenta_cushion',
            'minecraft:light_blue_cushion',
            'minecraft:yellow_cushion',
            'minecraft:lime_cushion',
            'minecraft:pink_cushion',
            'minecraft:gray_cushion',
            'minecraft:light_gray_cushion',
            'minecraft:cyan_cushion',
            'minecraft:purple_cushion',
            'minecraft:brown_cushion',
            'minecraft:green_cushion',
            'minecraft:red_cushion',
            'minecraft:black_cushion',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:blue_cushion'),
    type='minecraft:crafting_shapeless',
)

DYE_BLUE_HARNESS = RecipeCraftingShapeless(
    group='harness_dye',
    category=CraftingBookCategory.EQUIPMENT,
    ingredients=[
        'minecraft:blue_dye',
        [
            'minecraft:white_harness',
            'minecraft:orange_harness',
            'minecraft:magenta_harness',
            'minecraft:light_blue_harness',
            'minecraft:yellow_harness',
            'minecraft:lime_harness',
            'minecraft:pink_harness',
            'minecraft:gray_harness',
            'minecraft:light_gray_harness',
            'minecraft:cyan_harness',
            'minecraft:purple_harness',
            'minecraft:brown_harness',
            'minecraft:green_harness',
            'minecraft:red_harness',
            'minecraft:black_harness',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:blue_harness'),
    type='minecraft:crafting_shapeless',
)

DYE_BLUE_WOOL = RecipeCraftingShapeless(
    group='wool',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:blue_dye',
        [
            'minecraft:white_wool',
            'minecraft:orange_wool',
            'minecraft:magenta_wool',
            'minecraft:light_blue_wool',
            'minecraft:yellow_wool',
            'minecraft:lime_wool',
            'minecraft:pink_wool',
            'minecraft:gray_wool',
            'minecraft:light_gray_wool',
            'minecraft:cyan_wool',
            'minecraft:purple_wool',
            'minecraft:brown_wool',
            'minecraft:green_wool',
            'minecraft:red_wool',
            'minecraft:black_wool',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:blue_wool'),
    type='minecraft:crafting_shapeless',
)

DYE_BLUE_WOOL_SLAB = RecipeCraftingShapeless(
    group='wool_slabs',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:blue_dye',
        [
            'minecraft:white_wool_slab',
            'minecraft:orange_wool_slab',
            'minecraft:magenta_wool_slab',
            'minecraft:light_blue_wool_slab',
            'minecraft:yellow_wool_slab',
            'minecraft:lime_wool_slab',
            'minecraft:pink_wool_slab',
            'minecraft:gray_wool_slab',
            'minecraft:light_gray_wool_slab',
            'minecraft:cyan_wool_slab',
            'minecraft:purple_wool_slab',
            'minecraft:brown_wool_slab',
            'minecraft:green_wool_slab',
            'minecraft:red_wool_slab',
            'minecraft:black_wool_slab',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:blue_wool_slab'),
    type='minecraft:crafting_shapeless',
)

DYE_BLUE_WOOL_STAIRS = RecipeCraftingShapeless(
    group='wool_stairs',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:blue_dye',
        [
            'minecraft:white_wool_stairs',
            'minecraft:orange_wool_stairs',
            'minecraft:magenta_wool_stairs',
            'minecraft:light_blue_wool_stairs',
            'minecraft:yellow_wool_stairs',
            'minecraft:lime_wool_stairs',
            'minecraft:pink_wool_stairs',
            'minecraft:gray_wool_stairs',
            'minecraft:light_gray_wool_stairs',
            'minecraft:cyan_wool_stairs',
            'minecraft:purple_wool_stairs',
            'minecraft:brown_wool_stairs',
            'minecraft:green_wool_stairs',
            'minecraft:red_wool_stairs',
            'minecraft:black_wool_stairs',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:blue_wool_stairs'),
    type='minecraft:crafting_shapeless',
)

DYE_BROWN_BED = RecipeCraftingShapeless(
    group='bed_dye',
    ingredients=[
        'minecraft:brown_dye',
        [
            'minecraft:white_bed',
            'minecraft:orange_bed',
            'minecraft:magenta_bed',
            'minecraft:light_blue_bed',
            'minecraft:yellow_bed',
            'minecraft:lime_bed',
            'minecraft:pink_bed',
            'minecraft:gray_bed',
            'minecraft:light_gray_bed',
            'minecraft:cyan_bed',
            'minecraft:purple_bed',
            'minecraft:blue_bed',
            'minecraft:green_bed',
            'minecraft:red_bed',
            'minecraft:black_bed',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:brown_bed'),
    type='minecraft:crafting_shapeless',
)

DYE_BROWN_CARPET = RecipeCraftingShapeless(
    group='carpet_dye',
    ingredients=[
        'minecraft:brown_dye',
        [
            'minecraft:white_carpet',
            'minecraft:orange_carpet',
            'minecraft:magenta_carpet',
            'minecraft:light_blue_carpet',
            'minecraft:yellow_carpet',
            'minecraft:lime_carpet',
            'minecraft:pink_carpet',
            'minecraft:gray_carpet',
            'minecraft:light_gray_carpet',
            'minecraft:cyan_carpet',
            'minecraft:purple_carpet',
            'minecraft:blue_carpet',
            'minecraft:green_carpet',
            'minecraft:red_carpet',
            'minecraft:black_carpet',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:brown_carpet'),
    type='minecraft:crafting_shapeless',
)

DYE_BROWN_CUSHION = RecipeCraftingShapeless(
    group='cushion_dye',
    ingredients=[
        'minecraft:brown_dye',
        [
            'minecraft:white_cushion',
            'minecraft:orange_cushion',
            'minecraft:magenta_cushion',
            'minecraft:light_blue_cushion',
            'minecraft:yellow_cushion',
            'minecraft:lime_cushion',
            'minecraft:pink_cushion',
            'minecraft:gray_cushion',
            'minecraft:light_gray_cushion',
            'minecraft:cyan_cushion',
            'minecraft:purple_cushion',
            'minecraft:blue_cushion',
            'minecraft:green_cushion',
            'minecraft:red_cushion',
            'minecraft:black_cushion',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:brown_cushion'),
    type='minecraft:crafting_shapeless',
)

DYE_BROWN_HARNESS = RecipeCraftingShapeless(
    group='harness_dye',
    category=CraftingBookCategory.EQUIPMENT,
    ingredients=[
        'minecraft:brown_dye',
        [
            'minecraft:white_harness',
            'minecraft:orange_harness',
            'minecraft:magenta_harness',
            'minecraft:light_blue_harness',
            'minecraft:yellow_harness',
            'minecraft:lime_harness',
            'minecraft:pink_harness',
            'minecraft:gray_harness',
            'minecraft:light_gray_harness',
            'minecraft:cyan_harness',
            'minecraft:purple_harness',
            'minecraft:blue_harness',
            'minecraft:green_harness',
            'minecraft:red_harness',
            'minecraft:black_harness',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:brown_harness'),
    type='minecraft:crafting_shapeless',
)

DYE_BROWN_WOOL = RecipeCraftingShapeless(
    group='wool',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:brown_dye',
        [
            'minecraft:white_wool',
            'minecraft:orange_wool',
            'minecraft:magenta_wool',
            'minecraft:light_blue_wool',
            'minecraft:yellow_wool',
            'minecraft:lime_wool',
            'minecraft:pink_wool',
            'minecraft:gray_wool',
            'minecraft:light_gray_wool',
            'minecraft:cyan_wool',
            'minecraft:purple_wool',
            'minecraft:blue_wool',
            'minecraft:green_wool',
            'minecraft:red_wool',
            'minecraft:black_wool',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:brown_wool'),
    type='minecraft:crafting_shapeless',
)

DYE_BROWN_WOOL_SLAB = RecipeCraftingShapeless(
    group='wool_slabs',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:brown_dye',
        [
            'minecraft:white_wool_slab',
            'minecraft:orange_wool_slab',
            'minecraft:magenta_wool_slab',
            'minecraft:light_blue_wool_slab',
            'minecraft:yellow_wool_slab',
            'minecraft:lime_wool_slab',
            'minecraft:pink_wool_slab',
            'minecraft:gray_wool_slab',
            'minecraft:light_gray_wool_slab',
            'minecraft:cyan_wool_slab',
            'minecraft:purple_wool_slab',
            'minecraft:blue_wool_slab',
            'minecraft:green_wool_slab',
            'minecraft:red_wool_slab',
            'minecraft:black_wool_slab',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:brown_wool_slab'),
    type='minecraft:crafting_shapeless',
)

DYE_BROWN_WOOL_STAIRS = RecipeCraftingShapeless(
    group='wool_stairs',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:brown_dye',
        [
            'minecraft:white_wool_stairs',
            'minecraft:orange_wool_stairs',
            'minecraft:magenta_wool_stairs',
            'minecraft:light_blue_wool_stairs',
            'minecraft:yellow_wool_stairs',
            'minecraft:lime_wool_stairs',
            'minecraft:pink_wool_stairs',
            'minecraft:gray_wool_stairs',
            'minecraft:light_gray_wool_stairs',
            'minecraft:cyan_wool_stairs',
            'minecraft:purple_wool_stairs',
            'minecraft:blue_wool_stairs',
            'minecraft:green_wool_stairs',
            'minecraft:red_wool_stairs',
            'minecraft:black_wool_stairs',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:brown_wool_stairs'),
    type='minecraft:crafting_shapeless',
)

DYE_CYAN_BED = RecipeCraftingShapeless(
    group='bed_dye',
    ingredients=[
        'minecraft:cyan_dye',
        [
            'minecraft:white_bed',
            'minecraft:orange_bed',
            'minecraft:magenta_bed',
            'minecraft:light_blue_bed',
            'minecraft:yellow_bed',
            'minecraft:lime_bed',
            'minecraft:pink_bed',
            'minecraft:gray_bed',
            'minecraft:light_gray_bed',
            'minecraft:purple_bed',
            'minecraft:blue_bed',
            'minecraft:brown_bed',
            'minecraft:green_bed',
            'minecraft:red_bed',
            'minecraft:black_bed',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:cyan_bed'),
    type='minecraft:crafting_shapeless',
)

DYE_CYAN_CARPET = RecipeCraftingShapeless(
    group='carpet_dye',
    ingredients=[
        'minecraft:cyan_dye',
        [
            'minecraft:white_carpet',
            'minecraft:orange_carpet',
            'minecraft:magenta_carpet',
            'minecraft:light_blue_carpet',
            'minecraft:yellow_carpet',
            'minecraft:lime_carpet',
            'minecraft:pink_carpet',
            'minecraft:gray_carpet',
            'minecraft:light_gray_carpet',
            'minecraft:purple_carpet',
            'minecraft:blue_carpet',
            'minecraft:brown_carpet',
            'minecraft:green_carpet',
            'minecraft:red_carpet',
            'minecraft:black_carpet',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:cyan_carpet'),
    type='minecraft:crafting_shapeless',
)

DYE_CYAN_CUSHION = RecipeCraftingShapeless(
    group='cushion_dye',
    ingredients=[
        'minecraft:cyan_dye',
        [
            'minecraft:white_cushion',
            'minecraft:orange_cushion',
            'minecraft:magenta_cushion',
            'minecraft:light_blue_cushion',
            'minecraft:yellow_cushion',
            'minecraft:lime_cushion',
            'minecraft:pink_cushion',
            'minecraft:gray_cushion',
            'minecraft:light_gray_cushion',
            'minecraft:purple_cushion',
            'minecraft:blue_cushion',
            'minecraft:brown_cushion',
            'minecraft:green_cushion',
            'minecraft:red_cushion',
            'minecraft:black_cushion',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:cyan_cushion'),
    type='minecraft:crafting_shapeless',
)

DYE_CYAN_HARNESS = RecipeCraftingShapeless(
    group='harness_dye',
    category=CraftingBookCategory.EQUIPMENT,
    ingredients=[
        'minecraft:cyan_dye',
        [
            'minecraft:white_harness',
            'minecraft:orange_harness',
            'minecraft:magenta_harness',
            'minecraft:light_blue_harness',
            'minecraft:yellow_harness',
            'minecraft:lime_harness',
            'minecraft:pink_harness',
            'minecraft:gray_harness',
            'minecraft:light_gray_harness',
            'minecraft:purple_harness',
            'minecraft:blue_harness',
            'minecraft:brown_harness',
            'minecraft:green_harness',
            'minecraft:red_harness',
            'minecraft:black_harness',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:cyan_harness'),
    type='minecraft:crafting_shapeless',
)

DYE_CYAN_WOOL = RecipeCraftingShapeless(
    group='wool',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:cyan_dye',
        [
            'minecraft:white_wool',
            'minecraft:orange_wool',
            'minecraft:magenta_wool',
            'minecraft:light_blue_wool',
            'minecraft:yellow_wool',
            'minecraft:lime_wool',
            'minecraft:pink_wool',
            'minecraft:gray_wool',
            'minecraft:light_gray_wool',
            'minecraft:purple_wool',
            'minecraft:blue_wool',
            'minecraft:brown_wool',
            'minecraft:green_wool',
            'minecraft:red_wool',
            'minecraft:black_wool',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:cyan_wool'),
    type='minecraft:crafting_shapeless',
)

DYE_CYAN_WOOL_SLAB = RecipeCraftingShapeless(
    group='wool_slabs',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:cyan_dye',
        [
            'minecraft:white_wool_slab',
            'minecraft:orange_wool_slab',
            'minecraft:magenta_wool_slab',
            'minecraft:light_blue_wool_slab',
            'minecraft:yellow_wool_slab',
            'minecraft:lime_wool_slab',
            'minecraft:pink_wool_slab',
            'minecraft:gray_wool_slab',
            'minecraft:light_gray_wool_slab',
            'minecraft:purple_wool_slab',
            'minecraft:blue_wool_slab',
            'minecraft:brown_wool_slab',
            'minecraft:green_wool_slab',
            'minecraft:red_wool_slab',
            'minecraft:black_wool_slab',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:cyan_wool_slab'),
    type='minecraft:crafting_shapeless',
)

DYE_CYAN_WOOL_STAIRS = RecipeCraftingShapeless(
    group='wool_stairs',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:cyan_dye',
        [
            'minecraft:white_wool_stairs',
            'minecraft:orange_wool_stairs',
            'minecraft:magenta_wool_stairs',
            'minecraft:light_blue_wool_stairs',
            'minecraft:yellow_wool_stairs',
            'minecraft:lime_wool_stairs',
            'minecraft:pink_wool_stairs',
            'minecraft:gray_wool_stairs',
            'minecraft:light_gray_wool_stairs',
            'minecraft:purple_wool_stairs',
            'minecraft:blue_wool_stairs',
            'minecraft:brown_wool_stairs',
            'minecraft:green_wool_stairs',
            'minecraft:red_wool_stairs',
            'minecraft:black_wool_stairs',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:cyan_wool_stairs'),
    type='minecraft:crafting_shapeless',
)

DYE_GRAY_BED = RecipeCraftingShapeless(
    group='bed_dye',
    ingredients=[
        'minecraft:gray_dye',
        [
            'minecraft:white_bed',
            'minecraft:orange_bed',
            'minecraft:magenta_bed',
            'minecraft:light_blue_bed',
            'minecraft:yellow_bed',
            'minecraft:lime_bed',
            'minecraft:pink_bed',
            'minecraft:light_gray_bed',
            'minecraft:cyan_bed',
            'minecraft:purple_bed',
            'minecraft:blue_bed',
            'minecraft:brown_bed',
            'minecraft:green_bed',
            'minecraft:red_bed',
            'minecraft:black_bed',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:gray_bed'),
    type='minecraft:crafting_shapeless',
)

DYE_GRAY_CARPET = RecipeCraftingShapeless(
    group='carpet_dye',
    ingredients=[
        'minecraft:gray_dye',
        [
            'minecraft:white_carpet',
            'minecraft:orange_carpet',
            'minecraft:magenta_carpet',
            'minecraft:light_blue_carpet',
            'minecraft:yellow_carpet',
            'minecraft:lime_carpet',
            'minecraft:pink_carpet',
            'minecraft:light_gray_carpet',
            'minecraft:cyan_carpet',
            'minecraft:purple_carpet',
            'minecraft:blue_carpet',
            'minecraft:brown_carpet',
            'minecraft:green_carpet',
            'minecraft:red_carpet',
            'minecraft:black_carpet',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:gray_carpet'),
    type='minecraft:crafting_shapeless',
)

DYE_GRAY_CUSHION = RecipeCraftingShapeless(
    group='cushion_dye',
    ingredients=[
        'minecraft:gray_dye',
        [
            'minecraft:white_cushion',
            'minecraft:orange_cushion',
            'minecraft:magenta_cushion',
            'minecraft:light_blue_cushion',
            'minecraft:yellow_cushion',
            'minecraft:lime_cushion',
            'minecraft:pink_cushion',
            'minecraft:light_gray_cushion',
            'minecraft:cyan_cushion',
            'minecraft:purple_cushion',
            'minecraft:blue_cushion',
            'minecraft:brown_cushion',
            'minecraft:green_cushion',
            'minecraft:red_cushion',
            'minecraft:black_cushion',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:gray_cushion'),
    type='minecraft:crafting_shapeless',
)

DYE_GRAY_HARNESS = RecipeCraftingShapeless(
    group='harness_dye',
    category=CraftingBookCategory.EQUIPMENT,
    ingredients=[
        'minecraft:gray_dye',
        [
            'minecraft:white_harness',
            'minecraft:orange_harness',
            'minecraft:magenta_harness',
            'minecraft:light_blue_harness',
            'minecraft:yellow_harness',
            'minecraft:lime_harness',
            'minecraft:pink_harness',
            'minecraft:light_gray_harness',
            'minecraft:cyan_harness',
            'minecraft:purple_harness',
            'minecraft:blue_harness',
            'minecraft:brown_harness',
            'minecraft:green_harness',
            'minecraft:red_harness',
            'minecraft:black_harness',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:gray_harness'),
    type='minecraft:crafting_shapeless',
)

DYE_GRAY_WOOL = RecipeCraftingShapeless(
    group='wool',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:gray_dye',
        [
            'minecraft:white_wool',
            'minecraft:orange_wool',
            'minecraft:magenta_wool',
            'minecraft:light_blue_wool',
            'minecraft:yellow_wool',
            'minecraft:lime_wool',
            'minecraft:pink_wool',
            'minecraft:light_gray_wool',
            'minecraft:cyan_wool',
            'minecraft:purple_wool',
            'minecraft:blue_wool',
            'minecraft:brown_wool',
            'minecraft:green_wool',
            'minecraft:red_wool',
            'minecraft:black_wool',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:gray_wool'),
    type='minecraft:crafting_shapeless',
)

DYE_GRAY_WOOL_SLAB = RecipeCraftingShapeless(
    group='wool_slabs',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:gray_dye',
        [
            'minecraft:white_wool_slab',
            'minecraft:orange_wool_slab',
            'minecraft:magenta_wool_slab',
            'minecraft:light_blue_wool_slab',
            'minecraft:yellow_wool_slab',
            'minecraft:lime_wool_slab',
            'minecraft:pink_wool_slab',
            'minecraft:light_gray_wool_slab',
            'minecraft:cyan_wool_slab',
            'minecraft:purple_wool_slab',
            'minecraft:blue_wool_slab',
            'minecraft:brown_wool_slab',
            'minecraft:green_wool_slab',
            'minecraft:red_wool_slab',
            'minecraft:black_wool_slab',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:gray_wool_slab'),
    type='minecraft:crafting_shapeless',
)

DYE_GRAY_WOOL_STAIRS = RecipeCraftingShapeless(
    group='wool_stairs',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:gray_dye',
        [
            'minecraft:white_wool_stairs',
            'minecraft:orange_wool_stairs',
            'minecraft:magenta_wool_stairs',
            'minecraft:light_blue_wool_stairs',
            'minecraft:yellow_wool_stairs',
            'minecraft:lime_wool_stairs',
            'minecraft:pink_wool_stairs',
            'minecraft:light_gray_wool_stairs',
            'minecraft:cyan_wool_stairs',
            'minecraft:purple_wool_stairs',
            'minecraft:blue_wool_stairs',
            'minecraft:brown_wool_stairs',
            'minecraft:green_wool_stairs',
            'minecraft:red_wool_stairs',
            'minecraft:black_wool_stairs',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:gray_wool_stairs'),
    type='minecraft:crafting_shapeless',
)

DYE_GREEN_BED = RecipeCraftingShapeless(
    group='bed_dye',
    ingredients=[
        'minecraft:green_dye',
        [
            'minecraft:white_bed',
            'minecraft:orange_bed',
            'minecraft:magenta_bed',
            'minecraft:light_blue_bed',
            'minecraft:yellow_bed',
            'minecraft:lime_bed',
            'minecraft:pink_bed',
            'minecraft:gray_bed',
            'minecraft:light_gray_bed',
            'minecraft:cyan_bed',
            'minecraft:purple_bed',
            'minecraft:blue_bed',
            'minecraft:brown_bed',
            'minecraft:red_bed',
            'minecraft:black_bed',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:green_bed'),
    type='minecraft:crafting_shapeless',
)

DYE_GREEN_CARPET = RecipeCraftingShapeless(
    group='carpet_dye',
    ingredients=[
        'minecraft:green_dye',
        [
            'minecraft:white_carpet',
            'minecraft:orange_carpet',
            'minecraft:magenta_carpet',
            'minecraft:light_blue_carpet',
            'minecraft:yellow_carpet',
            'minecraft:lime_carpet',
            'minecraft:pink_carpet',
            'minecraft:gray_carpet',
            'minecraft:light_gray_carpet',
            'minecraft:cyan_carpet',
            'minecraft:purple_carpet',
            'minecraft:blue_carpet',
            'minecraft:brown_carpet',
            'minecraft:red_carpet',
            'minecraft:black_carpet',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:green_carpet'),
    type='minecraft:crafting_shapeless',
)

DYE_GREEN_CUSHION = RecipeCraftingShapeless(
    group='cushion_dye',
    ingredients=[
        'minecraft:green_dye',
        [
            'minecraft:white_cushion',
            'minecraft:orange_cushion',
            'minecraft:magenta_cushion',
            'minecraft:light_blue_cushion',
            'minecraft:yellow_cushion',
            'minecraft:lime_cushion',
            'minecraft:pink_cushion',
            'minecraft:gray_cushion',
            'minecraft:light_gray_cushion',
            'minecraft:cyan_cushion',
            'minecraft:purple_cushion',
            'minecraft:blue_cushion',
            'minecraft:brown_cushion',
            'minecraft:red_cushion',
            'minecraft:black_cushion',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:green_cushion'),
    type='minecraft:crafting_shapeless',
)

DYE_GREEN_HARNESS = RecipeCraftingShapeless(
    group='harness_dye',
    category=CraftingBookCategory.EQUIPMENT,
    ingredients=[
        'minecraft:green_dye',
        [
            'minecraft:white_harness',
            'minecraft:orange_harness',
            'minecraft:magenta_harness',
            'minecraft:light_blue_harness',
            'minecraft:yellow_harness',
            'minecraft:lime_harness',
            'minecraft:pink_harness',
            'minecraft:gray_harness',
            'minecraft:light_gray_harness',
            'minecraft:cyan_harness',
            'minecraft:purple_harness',
            'minecraft:blue_harness',
            'minecraft:brown_harness',
            'minecraft:red_harness',
            'minecraft:black_harness',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:green_harness'),
    type='minecraft:crafting_shapeless',
)

DYE_GREEN_WOOL = RecipeCraftingShapeless(
    group='wool',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:green_dye',
        [
            'minecraft:white_wool',
            'minecraft:orange_wool',
            'minecraft:magenta_wool',
            'minecraft:light_blue_wool',
            'minecraft:yellow_wool',
            'minecraft:lime_wool',
            'minecraft:pink_wool',
            'minecraft:gray_wool',
            'minecraft:light_gray_wool',
            'minecraft:cyan_wool',
            'minecraft:purple_wool',
            'minecraft:blue_wool',
            'minecraft:brown_wool',
            'minecraft:red_wool',
            'minecraft:black_wool',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:green_wool'),
    type='minecraft:crafting_shapeless',
)

DYE_GREEN_WOOL_SLAB = RecipeCraftingShapeless(
    group='wool_slabs',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:green_dye',
        [
            'minecraft:white_wool_slab',
            'minecraft:orange_wool_slab',
            'minecraft:magenta_wool_slab',
            'minecraft:light_blue_wool_slab',
            'minecraft:yellow_wool_slab',
            'minecraft:lime_wool_slab',
            'minecraft:pink_wool_slab',
            'minecraft:gray_wool_slab',
            'minecraft:light_gray_wool_slab',
            'minecraft:cyan_wool_slab',
            'minecraft:purple_wool_slab',
            'minecraft:blue_wool_slab',
            'minecraft:brown_wool_slab',
            'minecraft:red_wool_slab',
            'minecraft:black_wool_slab',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:green_wool_slab'),
    type='minecraft:crafting_shapeless',
)

DYE_GREEN_WOOL_STAIRS = RecipeCraftingShapeless(
    group='wool_stairs',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:green_dye',
        [
            'minecraft:white_wool_stairs',
            'minecraft:orange_wool_stairs',
            'minecraft:magenta_wool_stairs',
            'minecraft:light_blue_wool_stairs',
            'minecraft:yellow_wool_stairs',
            'minecraft:lime_wool_stairs',
            'minecraft:pink_wool_stairs',
            'minecraft:gray_wool_stairs',
            'minecraft:light_gray_wool_stairs',
            'minecraft:cyan_wool_stairs',
            'minecraft:purple_wool_stairs',
            'minecraft:blue_wool_stairs',
            'minecraft:brown_wool_stairs',
            'minecraft:red_wool_stairs',
            'minecraft:black_wool_stairs',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:green_wool_stairs'),
    type='minecraft:crafting_shapeless',
)

DYE_LIGHT_BLUE_BED = RecipeCraftingShapeless(
    group='bed_dye',
    ingredients=[
        'minecraft:light_blue_dye',
        [
            'minecraft:white_bed',
            'minecraft:orange_bed',
            'minecraft:magenta_bed',
            'minecraft:yellow_bed',
            'minecraft:lime_bed',
            'minecraft:pink_bed',
            'minecraft:gray_bed',
            'minecraft:light_gray_bed',
            'minecraft:cyan_bed',
            'minecraft:purple_bed',
            'minecraft:blue_bed',
            'minecraft:brown_bed',
            'minecraft:green_bed',
            'minecraft:red_bed',
            'minecraft:black_bed',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:light_blue_bed'),
    type='minecraft:crafting_shapeless',
)

DYE_LIGHT_BLUE_CARPET = RecipeCraftingShapeless(
    group='carpet_dye',
    ingredients=[
        'minecraft:light_blue_dye',
        [
            'minecraft:white_carpet',
            'minecraft:orange_carpet',
            'minecraft:magenta_carpet',
            'minecraft:yellow_carpet',
            'minecraft:lime_carpet',
            'minecraft:pink_carpet',
            'minecraft:gray_carpet',
            'minecraft:light_gray_carpet',
            'minecraft:cyan_carpet',
            'minecraft:purple_carpet',
            'minecraft:blue_carpet',
            'minecraft:brown_carpet',
            'minecraft:green_carpet',
            'minecraft:red_carpet',
            'minecraft:black_carpet',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:light_blue_carpet'),
    type='minecraft:crafting_shapeless',
)

DYE_LIGHT_BLUE_CUSHION = RecipeCraftingShapeless(
    group='cushion_dye',
    ingredients=[
        'minecraft:light_blue_dye',
        [
            'minecraft:white_cushion',
            'minecraft:orange_cushion',
            'minecraft:magenta_cushion',
            'minecraft:yellow_cushion',
            'minecraft:lime_cushion',
            'minecraft:pink_cushion',
            'minecraft:gray_cushion',
            'minecraft:light_gray_cushion',
            'minecraft:cyan_cushion',
            'minecraft:purple_cushion',
            'minecraft:blue_cushion',
            'minecraft:brown_cushion',
            'minecraft:green_cushion',
            'minecraft:red_cushion',
            'minecraft:black_cushion',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:light_blue_cushion'),
    type='minecraft:crafting_shapeless',
)

DYE_LIGHT_BLUE_HARNESS = RecipeCraftingShapeless(
    group='harness_dye',
    category=CraftingBookCategory.EQUIPMENT,
    ingredients=[
        'minecraft:light_blue_dye',
        [
            'minecraft:white_harness',
            'minecraft:orange_harness',
            'minecraft:magenta_harness',
            'minecraft:yellow_harness',
            'minecraft:lime_harness',
            'minecraft:pink_harness',
            'minecraft:gray_harness',
            'minecraft:light_gray_harness',
            'minecraft:cyan_harness',
            'minecraft:purple_harness',
            'minecraft:blue_harness',
            'minecraft:brown_harness',
            'minecraft:green_harness',
            'minecraft:red_harness',
            'minecraft:black_harness',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:light_blue_harness'),
    type='minecraft:crafting_shapeless',
)

DYE_LIGHT_BLUE_WOOL = RecipeCraftingShapeless(
    group='wool',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:light_blue_dye',
        [
            'minecraft:white_wool',
            'minecraft:orange_wool',
            'minecraft:magenta_wool',
            'minecraft:yellow_wool',
            'minecraft:lime_wool',
            'minecraft:pink_wool',
            'minecraft:gray_wool',
            'minecraft:light_gray_wool',
            'minecraft:cyan_wool',
            'minecraft:purple_wool',
            'minecraft:blue_wool',
            'minecraft:brown_wool',
            'minecraft:green_wool',
            'minecraft:red_wool',
            'minecraft:black_wool',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:light_blue_wool'),
    type='minecraft:crafting_shapeless',
)

DYE_LIGHT_BLUE_WOOL_SLAB = RecipeCraftingShapeless(
    group='wool_slabs',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:light_blue_dye',
        [
            'minecraft:white_wool_slab',
            'minecraft:orange_wool_slab',
            'minecraft:magenta_wool_slab',
            'minecraft:yellow_wool_slab',
            'minecraft:lime_wool_slab',
            'minecraft:pink_wool_slab',
            'minecraft:gray_wool_slab',
            'minecraft:light_gray_wool_slab',
            'minecraft:cyan_wool_slab',
            'minecraft:purple_wool_slab',
            'minecraft:blue_wool_slab',
            'minecraft:brown_wool_slab',
            'minecraft:green_wool_slab',
            'minecraft:red_wool_slab',
            'minecraft:black_wool_slab',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:light_blue_wool_slab'),
    type='minecraft:crafting_shapeless',
)

DYE_LIGHT_BLUE_WOOL_STAIRS = RecipeCraftingShapeless(
    group='wool_stairs',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:light_blue_dye',
        [
            'minecraft:white_wool_stairs',
            'minecraft:orange_wool_stairs',
            'minecraft:magenta_wool_stairs',
            'minecraft:yellow_wool_stairs',
            'minecraft:lime_wool_stairs',
            'minecraft:pink_wool_stairs',
            'minecraft:gray_wool_stairs',
            'minecraft:light_gray_wool_stairs',
            'minecraft:cyan_wool_stairs',
            'minecraft:purple_wool_stairs',
            'minecraft:blue_wool_stairs',
            'minecraft:brown_wool_stairs',
            'minecraft:green_wool_stairs',
            'minecraft:red_wool_stairs',
            'minecraft:black_wool_stairs',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:light_blue_wool_stairs'),
    type='minecraft:crafting_shapeless',
)

DYE_LIGHT_GRAY_BED = RecipeCraftingShapeless(
    group='bed_dye',
    ingredients=[
        'minecraft:light_gray_dye',
        [
            'minecraft:white_bed',
            'minecraft:orange_bed',
            'minecraft:magenta_bed',
            'minecraft:light_blue_bed',
            'minecraft:yellow_bed',
            'minecraft:lime_bed',
            'minecraft:pink_bed',
            'minecraft:gray_bed',
            'minecraft:cyan_bed',
            'minecraft:purple_bed',
            'minecraft:blue_bed',
            'minecraft:brown_bed',
            'minecraft:green_bed',
            'minecraft:red_bed',
            'minecraft:black_bed',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:light_gray_bed'),
    type='minecraft:crafting_shapeless',
)

DYE_LIGHT_GRAY_CARPET = RecipeCraftingShapeless(
    group='carpet_dye',
    ingredients=[
        'minecraft:light_gray_dye',
        [
            'minecraft:white_carpet',
            'minecraft:orange_carpet',
            'minecraft:magenta_carpet',
            'minecraft:light_blue_carpet',
            'minecraft:yellow_carpet',
            'minecraft:lime_carpet',
            'minecraft:pink_carpet',
            'minecraft:gray_carpet',
            'minecraft:cyan_carpet',
            'minecraft:purple_carpet',
            'minecraft:blue_carpet',
            'minecraft:brown_carpet',
            'minecraft:green_carpet',
            'minecraft:red_carpet',
            'minecraft:black_carpet',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:light_gray_carpet'),
    type='minecraft:crafting_shapeless',
)

DYE_LIGHT_GRAY_CUSHION = RecipeCraftingShapeless(
    group='cushion_dye',
    ingredients=[
        'minecraft:light_gray_dye',
        [
            'minecraft:white_cushion',
            'minecraft:orange_cushion',
            'minecraft:magenta_cushion',
            'minecraft:light_blue_cushion',
            'minecraft:yellow_cushion',
            'minecraft:lime_cushion',
            'minecraft:pink_cushion',
            'minecraft:gray_cushion',
            'minecraft:cyan_cushion',
            'minecraft:purple_cushion',
            'minecraft:blue_cushion',
            'minecraft:brown_cushion',
            'minecraft:green_cushion',
            'minecraft:red_cushion',
            'minecraft:black_cushion',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:light_gray_cushion'),
    type='minecraft:crafting_shapeless',
)

DYE_LIGHT_GRAY_HARNESS = RecipeCraftingShapeless(
    group='harness_dye',
    category=CraftingBookCategory.EQUIPMENT,
    ingredients=[
        'minecraft:light_gray_dye',
        [
            'minecraft:white_harness',
            'minecraft:orange_harness',
            'minecraft:magenta_harness',
            'minecraft:light_blue_harness',
            'minecraft:yellow_harness',
            'minecraft:lime_harness',
            'minecraft:pink_harness',
            'minecraft:gray_harness',
            'minecraft:cyan_harness',
            'minecraft:purple_harness',
            'minecraft:blue_harness',
            'minecraft:brown_harness',
            'minecraft:green_harness',
            'minecraft:red_harness',
            'minecraft:black_harness',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:light_gray_harness'),
    type='minecraft:crafting_shapeless',
)

DYE_LIGHT_GRAY_WOOL = RecipeCraftingShapeless(
    group='wool',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:light_gray_dye',
        [
            'minecraft:white_wool',
            'minecraft:orange_wool',
            'minecraft:magenta_wool',
            'minecraft:light_blue_wool',
            'minecraft:yellow_wool',
            'minecraft:lime_wool',
            'minecraft:pink_wool',
            'minecraft:gray_wool',
            'minecraft:cyan_wool',
            'minecraft:purple_wool',
            'minecraft:blue_wool',
            'minecraft:brown_wool',
            'minecraft:green_wool',
            'minecraft:red_wool',
            'minecraft:black_wool',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:light_gray_wool'),
    type='minecraft:crafting_shapeless',
)

DYE_LIGHT_GRAY_WOOL_SLAB = RecipeCraftingShapeless(
    group='wool_slabs',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:light_gray_dye',
        [
            'minecraft:white_wool_slab',
            'minecraft:orange_wool_slab',
            'minecraft:magenta_wool_slab',
            'minecraft:light_blue_wool_slab',
            'minecraft:yellow_wool_slab',
            'minecraft:lime_wool_slab',
            'minecraft:pink_wool_slab',
            'minecraft:gray_wool_slab',
            'minecraft:cyan_wool_slab',
            'minecraft:purple_wool_slab',
            'minecraft:blue_wool_slab',
            'minecraft:brown_wool_slab',
            'minecraft:green_wool_slab',
            'minecraft:red_wool_slab',
            'minecraft:black_wool_slab',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:light_gray_wool_slab'),
    type='minecraft:crafting_shapeless',
)

DYE_LIGHT_GRAY_WOOL_STAIRS = RecipeCraftingShapeless(
    group='wool_stairs',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:light_gray_dye',
        [
            'minecraft:white_wool_stairs',
            'minecraft:orange_wool_stairs',
            'minecraft:magenta_wool_stairs',
            'minecraft:light_blue_wool_stairs',
            'minecraft:yellow_wool_stairs',
            'minecraft:lime_wool_stairs',
            'minecraft:pink_wool_stairs',
            'minecraft:gray_wool_stairs',
            'minecraft:cyan_wool_stairs',
            'minecraft:purple_wool_stairs',
            'minecraft:blue_wool_stairs',
            'minecraft:brown_wool_stairs',
            'minecraft:green_wool_stairs',
            'minecraft:red_wool_stairs',
            'minecraft:black_wool_stairs',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:light_gray_wool_stairs'),
    type='minecraft:crafting_shapeless',
)

DYE_LIME_BED = RecipeCraftingShapeless(
    group='bed_dye',
    ingredients=[
        'minecraft:lime_dye',
        [
            'minecraft:white_bed',
            'minecraft:orange_bed',
            'minecraft:magenta_bed',
            'minecraft:light_blue_bed',
            'minecraft:yellow_bed',
            'minecraft:pink_bed',
            'minecraft:gray_bed',
            'minecraft:light_gray_bed',
            'minecraft:cyan_bed',
            'minecraft:purple_bed',
            'minecraft:blue_bed',
            'minecraft:brown_bed',
            'minecraft:green_bed',
            'minecraft:red_bed',
            'minecraft:black_bed',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:lime_bed'),
    type='minecraft:crafting_shapeless',
)

DYE_LIME_CARPET = RecipeCraftingShapeless(
    group='carpet_dye',
    ingredients=[
        'minecraft:lime_dye',
        [
            'minecraft:white_carpet',
            'minecraft:orange_carpet',
            'minecraft:magenta_carpet',
            'minecraft:light_blue_carpet',
            'minecraft:yellow_carpet',
            'minecraft:pink_carpet',
            'minecraft:gray_carpet',
            'minecraft:light_gray_carpet',
            'minecraft:cyan_carpet',
            'minecraft:purple_carpet',
            'minecraft:blue_carpet',
            'minecraft:brown_carpet',
            'minecraft:green_carpet',
            'minecraft:red_carpet',
            'minecraft:black_carpet',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:lime_carpet'),
    type='minecraft:crafting_shapeless',
)

DYE_LIME_CUSHION = RecipeCraftingShapeless(
    group='cushion_dye',
    ingredients=[
        'minecraft:lime_dye',
        [
            'minecraft:white_cushion',
            'minecraft:orange_cushion',
            'minecraft:magenta_cushion',
            'minecraft:light_blue_cushion',
            'minecraft:yellow_cushion',
            'minecraft:pink_cushion',
            'minecraft:gray_cushion',
            'minecraft:light_gray_cushion',
            'minecraft:cyan_cushion',
            'minecraft:purple_cushion',
            'minecraft:blue_cushion',
            'minecraft:brown_cushion',
            'minecraft:green_cushion',
            'minecraft:red_cushion',
            'minecraft:black_cushion',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:lime_cushion'),
    type='minecraft:crafting_shapeless',
)

DYE_LIME_HARNESS = RecipeCraftingShapeless(
    group='harness_dye',
    category=CraftingBookCategory.EQUIPMENT,
    ingredients=[
        'minecraft:lime_dye',
        [
            'minecraft:white_harness',
            'minecraft:orange_harness',
            'minecraft:magenta_harness',
            'minecraft:light_blue_harness',
            'minecraft:yellow_harness',
            'minecraft:pink_harness',
            'minecraft:gray_harness',
            'minecraft:light_gray_harness',
            'minecraft:cyan_harness',
            'minecraft:purple_harness',
            'minecraft:blue_harness',
            'minecraft:brown_harness',
            'minecraft:green_harness',
            'minecraft:red_harness',
            'minecraft:black_harness',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:lime_harness'),
    type='minecraft:crafting_shapeless',
)

DYE_LIME_WOOL = RecipeCraftingShapeless(
    group='wool',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:lime_dye',
        [
            'minecraft:white_wool',
            'minecraft:orange_wool',
            'minecraft:magenta_wool',
            'minecraft:light_blue_wool',
            'minecraft:yellow_wool',
            'minecraft:pink_wool',
            'minecraft:gray_wool',
            'minecraft:light_gray_wool',
            'minecraft:cyan_wool',
            'minecraft:purple_wool',
            'minecraft:blue_wool',
            'minecraft:brown_wool',
            'minecraft:green_wool',
            'minecraft:red_wool',
            'minecraft:black_wool',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:lime_wool'),
    type='minecraft:crafting_shapeless',
)

DYE_LIME_WOOL_SLAB = RecipeCraftingShapeless(
    group='wool_slabs',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:lime_dye',
        [
            'minecraft:white_wool_slab',
            'minecraft:orange_wool_slab',
            'minecraft:magenta_wool_slab',
            'minecraft:light_blue_wool_slab',
            'minecraft:yellow_wool_slab',
            'minecraft:pink_wool_slab',
            'minecraft:gray_wool_slab',
            'minecraft:light_gray_wool_slab',
            'minecraft:cyan_wool_slab',
            'minecraft:purple_wool_slab',
            'minecraft:blue_wool_slab',
            'minecraft:brown_wool_slab',
            'minecraft:green_wool_slab',
            'minecraft:red_wool_slab',
            'minecraft:black_wool_slab',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:lime_wool_slab'),
    type='minecraft:crafting_shapeless',
)

DYE_LIME_WOOL_STAIRS = RecipeCraftingShapeless(
    group='wool_stairs',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:lime_dye',
        [
            'minecraft:white_wool_stairs',
            'minecraft:orange_wool_stairs',
            'minecraft:magenta_wool_stairs',
            'minecraft:light_blue_wool_stairs',
            'minecraft:yellow_wool_stairs',
            'minecraft:pink_wool_stairs',
            'minecraft:gray_wool_stairs',
            'minecraft:light_gray_wool_stairs',
            'minecraft:cyan_wool_stairs',
            'minecraft:purple_wool_stairs',
            'minecraft:blue_wool_stairs',
            'minecraft:brown_wool_stairs',
            'minecraft:green_wool_stairs',
            'minecraft:red_wool_stairs',
            'minecraft:black_wool_stairs',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:lime_wool_stairs'),
    type='minecraft:crafting_shapeless',
)

DYE_MAGENTA_BED = RecipeCraftingShapeless(
    group='bed_dye',
    ingredients=[
        'minecraft:magenta_dye',
        [
            'minecraft:white_bed',
            'minecraft:orange_bed',
            'minecraft:light_blue_bed',
            'minecraft:yellow_bed',
            'minecraft:lime_bed',
            'minecraft:pink_bed',
            'minecraft:gray_bed',
            'minecraft:light_gray_bed',
            'minecraft:cyan_bed',
            'minecraft:purple_bed',
            'minecraft:blue_bed',
            'minecraft:brown_bed',
            'minecraft:green_bed',
            'minecraft:red_bed',
            'minecraft:black_bed',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:magenta_bed'),
    type='minecraft:crafting_shapeless',
)

DYE_MAGENTA_CARPET = RecipeCraftingShapeless(
    group='carpet_dye',
    ingredients=[
        'minecraft:magenta_dye',
        [
            'minecraft:white_carpet',
            'minecraft:orange_carpet',
            'minecraft:light_blue_carpet',
            'minecraft:yellow_carpet',
            'minecraft:lime_carpet',
            'minecraft:pink_carpet',
            'minecraft:gray_carpet',
            'minecraft:light_gray_carpet',
            'minecraft:cyan_carpet',
            'minecraft:purple_carpet',
            'minecraft:blue_carpet',
            'minecraft:brown_carpet',
            'minecraft:green_carpet',
            'minecraft:red_carpet',
            'minecraft:black_carpet',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:magenta_carpet'),
    type='minecraft:crafting_shapeless',
)

DYE_MAGENTA_CUSHION = RecipeCraftingShapeless(
    group='cushion_dye',
    ingredients=[
        'minecraft:magenta_dye',
        [
            'minecraft:white_cushion',
            'minecraft:orange_cushion',
            'minecraft:light_blue_cushion',
            'minecraft:yellow_cushion',
            'minecraft:lime_cushion',
            'minecraft:pink_cushion',
            'minecraft:gray_cushion',
            'minecraft:light_gray_cushion',
            'minecraft:cyan_cushion',
            'minecraft:purple_cushion',
            'minecraft:blue_cushion',
            'minecraft:brown_cushion',
            'minecraft:green_cushion',
            'minecraft:red_cushion',
            'minecraft:black_cushion',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:magenta_cushion'),
    type='minecraft:crafting_shapeless',
)

DYE_MAGENTA_HARNESS = RecipeCraftingShapeless(
    group='harness_dye',
    category=CraftingBookCategory.EQUIPMENT,
    ingredients=[
        'minecraft:magenta_dye',
        [
            'minecraft:white_harness',
            'minecraft:orange_harness',
            'minecraft:light_blue_harness',
            'minecraft:yellow_harness',
            'minecraft:lime_harness',
            'minecraft:pink_harness',
            'minecraft:gray_harness',
            'minecraft:light_gray_harness',
            'minecraft:cyan_harness',
            'minecraft:purple_harness',
            'minecraft:blue_harness',
            'minecraft:brown_harness',
            'minecraft:green_harness',
            'minecraft:red_harness',
            'minecraft:black_harness',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:magenta_harness'),
    type='minecraft:crafting_shapeless',
)

DYE_MAGENTA_WOOL = RecipeCraftingShapeless(
    group='wool',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:magenta_dye',
        [
            'minecraft:white_wool',
            'minecraft:orange_wool',
            'minecraft:light_blue_wool',
            'minecraft:yellow_wool',
            'minecraft:lime_wool',
            'minecraft:pink_wool',
            'minecraft:gray_wool',
            'minecraft:light_gray_wool',
            'minecraft:cyan_wool',
            'minecraft:purple_wool',
            'minecraft:blue_wool',
            'minecraft:brown_wool',
            'minecraft:green_wool',
            'minecraft:red_wool',
            'minecraft:black_wool',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:magenta_wool'),
    type='minecraft:crafting_shapeless',
)

DYE_MAGENTA_WOOL_SLAB = RecipeCraftingShapeless(
    group='wool_slabs',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:magenta_dye',
        [
            'minecraft:white_wool_slab',
            'minecraft:orange_wool_slab',
            'minecraft:light_blue_wool_slab',
            'minecraft:yellow_wool_slab',
            'minecraft:lime_wool_slab',
            'minecraft:pink_wool_slab',
            'minecraft:gray_wool_slab',
            'minecraft:light_gray_wool_slab',
            'minecraft:cyan_wool_slab',
            'minecraft:purple_wool_slab',
            'minecraft:blue_wool_slab',
            'minecraft:brown_wool_slab',
            'minecraft:green_wool_slab',
            'minecraft:red_wool_slab',
            'minecraft:black_wool_slab',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:magenta_wool_slab'),
    type='minecraft:crafting_shapeless',
)

DYE_MAGENTA_WOOL_STAIRS = RecipeCraftingShapeless(
    group='wool_stairs',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:magenta_dye',
        [
            'minecraft:white_wool_stairs',
            'minecraft:orange_wool_stairs',
            'minecraft:light_blue_wool_stairs',
            'minecraft:yellow_wool_stairs',
            'minecraft:lime_wool_stairs',
            'minecraft:pink_wool_stairs',
            'minecraft:gray_wool_stairs',
            'minecraft:light_gray_wool_stairs',
            'minecraft:cyan_wool_stairs',
            'minecraft:purple_wool_stairs',
            'minecraft:blue_wool_stairs',
            'minecraft:brown_wool_stairs',
            'minecraft:green_wool_stairs',
            'minecraft:red_wool_stairs',
            'minecraft:black_wool_stairs',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:magenta_wool_stairs'),
    type='minecraft:crafting_shapeless',
)

DYE_ORANGE_BED = RecipeCraftingShapeless(
    group='bed_dye',
    ingredients=[
        'minecraft:orange_dye',
        [
            'minecraft:white_bed',
            'minecraft:magenta_bed',
            'minecraft:light_blue_bed',
            'minecraft:yellow_bed',
            'minecraft:lime_bed',
            'minecraft:pink_bed',
            'minecraft:gray_bed',
            'minecraft:light_gray_bed',
            'minecraft:cyan_bed',
            'minecraft:purple_bed',
            'minecraft:blue_bed',
            'minecraft:brown_bed',
            'minecraft:green_bed',
            'minecraft:red_bed',
            'minecraft:black_bed',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:orange_bed'),
    type='minecraft:crafting_shapeless',
)

DYE_ORANGE_CARPET = RecipeCraftingShapeless(
    group='carpet_dye',
    ingredients=[
        'minecraft:orange_dye',
        [
            'minecraft:white_carpet',
            'minecraft:magenta_carpet',
            'minecraft:light_blue_carpet',
            'minecraft:yellow_carpet',
            'minecraft:lime_carpet',
            'minecraft:pink_carpet',
            'minecraft:gray_carpet',
            'minecraft:light_gray_carpet',
            'minecraft:cyan_carpet',
            'minecraft:purple_carpet',
            'minecraft:blue_carpet',
            'minecraft:brown_carpet',
            'minecraft:green_carpet',
            'minecraft:red_carpet',
            'minecraft:black_carpet',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:orange_carpet'),
    type='minecraft:crafting_shapeless',
)

DYE_ORANGE_CUSHION = RecipeCraftingShapeless(
    group='cushion_dye',
    ingredients=[
        'minecraft:orange_dye',
        [
            'minecraft:white_cushion',
            'minecraft:magenta_cushion',
            'minecraft:light_blue_cushion',
            'minecraft:yellow_cushion',
            'minecraft:lime_cushion',
            'minecraft:pink_cushion',
            'minecraft:gray_cushion',
            'minecraft:light_gray_cushion',
            'minecraft:cyan_cushion',
            'minecraft:purple_cushion',
            'minecraft:blue_cushion',
            'minecraft:brown_cushion',
            'minecraft:green_cushion',
            'minecraft:red_cushion',
            'minecraft:black_cushion',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:orange_cushion'),
    type='minecraft:crafting_shapeless',
)

DYE_ORANGE_HARNESS = RecipeCraftingShapeless(
    group='harness_dye',
    category=CraftingBookCategory.EQUIPMENT,
    ingredients=[
        'minecraft:orange_dye',
        [
            'minecraft:white_harness',
            'minecraft:magenta_harness',
            'minecraft:light_blue_harness',
            'minecraft:yellow_harness',
            'minecraft:lime_harness',
            'minecraft:pink_harness',
            'minecraft:gray_harness',
            'minecraft:light_gray_harness',
            'minecraft:cyan_harness',
            'minecraft:purple_harness',
            'minecraft:blue_harness',
            'minecraft:brown_harness',
            'minecraft:green_harness',
            'minecraft:red_harness',
            'minecraft:black_harness',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:orange_harness'),
    type='minecraft:crafting_shapeless',
)

DYE_ORANGE_WOOL = RecipeCraftingShapeless(
    group='wool',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:orange_dye',
        [
            'minecraft:white_wool',
            'minecraft:magenta_wool',
            'minecraft:light_blue_wool',
            'minecraft:yellow_wool',
            'minecraft:lime_wool',
            'minecraft:pink_wool',
            'minecraft:gray_wool',
            'minecraft:light_gray_wool',
            'minecraft:cyan_wool',
            'minecraft:purple_wool',
            'minecraft:blue_wool',
            'minecraft:brown_wool',
            'minecraft:green_wool',
            'minecraft:red_wool',
            'minecraft:black_wool',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:orange_wool'),
    type='minecraft:crafting_shapeless',
)

DYE_ORANGE_WOOL_SLAB = RecipeCraftingShapeless(
    group='wool_slabs',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:orange_dye',
        [
            'minecraft:white_wool_slab',
            'minecraft:magenta_wool_slab',
            'minecraft:light_blue_wool_slab',
            'minecraft:yellow_wool_slab',
            'minecraft:lime_wool_slab',
            'minecraft:pink_wool_slab',
            'minecraft:gray_wool_slab',
            'minecraft:light_gray_wool_slab',
            'minecraft:cyan_wool_slab',
            'minecraft:purple_wool_slab',
            'minecraft:blue_wool_slab',
            'minecraft:brown_wool_slab',
            'minecraft:green_wool_slab',
            'minecraft:red_wool_slab',
            'minecraft:black_wool_slab',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:orange_wool_slab'),
    type='minecraft:crafting_shapeless',
)

DYE_ORANGE_WOOL_STAIRS = RecipeCraftingShapeless(
    group='wool_stairs',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:orange_dye',
        [
            'minecraft:white_wool_stairs',
            'minecraft:magenta_wool_stairs',
            'minecraft:light_blue_wool_stairs',
            'minecraft:yellow_wool_stairs',
            'minecraft:lime_wool_stairs',
            'minecraft:pink_wool_stairs',
            'minecraft:gray_wool_stairs',
            'minecraft:light_gray_wool_stairs',
            'minecraft:cyan_wool_stairs',
            'minecraft:purple_wool_stairs',
            'minecraft:blue_wool_stairs',
            'minecraft:brown_wool_stairs',
            'minecraft:green_wool_stairs',
            'minecraft:red_wool_stairs',
            'minecraft:black_wool_stairs',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:orange_wool_stairs'),
    type='minecraft:crafting_shapeless',
)

DYE_PINK_BED = RecipeCraftingShapeless(
    group='bed_dye',
    ingredients=[
        'minecraft:pink_dye',
        [
            'minecraft:white_bed',
            'minecraft:orange_bed',
            'minecraft:magenta_bed',
            'minecraft:light_blue_bed',
            'minecraft:yellow_bed',
            'minecraft:lime_bed',
            'minecraft:gray_bed',
            'minecraft:light_gray_bed',
            'minecraft:cyan_bed',
            'minecraft:purple_bed',
            'minecraft:blue_bed',
            'minecraft:brown_bed',
            'minecraft:green_bed',
            'minecraft:red_bed',
            'minecraft:black_bed',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:pink_bed'),
    type='minecraft:crafting_shapeless',
)

DYE_PINK_CARPET = RecipeCraftingShapeless(
    group='carpet_dye',
    ingredients=[
        'minecraft:pink_dye',
        [
            'minecraft:white_carpet',
            'minecraft:orange_carpet',
            'minecraft:magenta_carpet',
            'minecraft:light_blue_carpet',
            'minecraft:yellow_carpet',
            'minecraft:lime_carpet',
            'minecraft:gray_carpet',
            'minecraft:light_gray_carpet',
            'minecraft:cyan_carpet',
            'minecraft:purple_carpet',
            'minecraft:blue_carpet',
            'minecraft:brown_carpet',
            'minecraft:green_carpet',
            'minecraft:red_carpet',
            'minecraft:black_carpet',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:pink_carpet'),
    type='minecraft:crafting_shapeless',
)

DYE_PINK_CUSHION = RecipeCraftingShapeless(
    group='cushion_dye',
    ingredients=[
        'minecraft:pink_dye',
        [
            'minecraft:white_cushion',
            'minecraft:orange_cushion',
            'minecraft:magenta_cushion',
            'minecraft:light_blue_cushion',
            'minecraft:yellow_cushion',
            'minecraft:lime_cushion',
            'minecraft:gray_cushion',
            'minecraft:light_gray_cushion',
            'minecraft:cyan_cushion',
            'minecraft:purple_cushion',
            'minecraft:blue_cushion',
            'minecraft:brown_cushion',
            'minecraft:green_cushion',
            'minecraft:red_cushion',
            'minecraft:black_cushion',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:pink_cushion'),
    type='minecraft:crafting_shapeless',
)

DYE_PINK_HARNESS = RecipeCraftingShapeless(
    group='harness_dye',
    category=CraftingBookCategory.EQUIPMENT,
    ingredients=[
        'minecraft:pink_dye',
        [
            'minecraft:white_harness',
            'minecraft:orange_harness',
            'minecraft:magenta_harness',
            'minecraft:light_blue_harness',
            'minecraft:yellow_harness',
            'minecraft:lime_harness',
            'minecraft:gray_harness',
            'minecraft:light_gray_harness',
            'minecraft:cyan_harness',
            'minecraft:purple_harness',
            'minecraft:blue_harness',
            'minecraft:brown_harness',
            'minecraft:green_harness',
            'minecraft:red_harness',
            'minecraft:black_harness',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:pink_harness'),
    type='minecraft:crafting_shapeless',
)

DYE_PINK_WOOL = RecipeCraftingShapeless(
    group='wool',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:pink_dye',
        [
            'minecraft:white_wool',
            'minecraft:orange_wool',
            'minecraft:magenta_wool',
            'minecraft:light_blue_wool',
            'minecraft:yellow_wool',
            'minecraft:lime_wool',
            'minecraft:gray_wool',
            'minecraft:light_gray_wool',
            'minecraft:cyan_wool',
            'minecraft:purple_wool',
            'minecraft:blue_wool',
            'minecraft:brown_wool',
            'minecraft:green_wool',
            'minecraft:red_wool',
            'minecraft:black_wool',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:pink_wool'),
    type='minecraft:crafting_shapeless',
)

DYE_PINK_WOOL_SLAB = RecipeCraftingShapeless(
    group='wool_slabs',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:pink_dye',
        [
            'minecraft:white_wool_slab',
            'minecraft:orange_wool_slab',
            'minecraft:magenta_wool_slab',
            'minecraft:light_blue_wool_slab',
            'minecraft:yellow_wool_slab',
            'minecraft:lime_wool_slab',
            'minecraft:gray_wool_slab',
            'minecraft:light_gray_wool_slab',
            'minecraft:cyan_wool_slab',
            'minecraft:purple_wool_slab',
            'minecraft:blue_wool_slab',
            'minecraft:brown_wool_slab',
            'minecraft:green_wool_slab',
            'minecraft:red_wool_slab',
            'minecraft:black_wool_slab',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:pink_wool_slab'),
    type='minecraft:crafting_shapeless',
)

DYE_PINK_WOOL_STAIRS = RecipeCraftingShapeless(
    group='wool_stairs',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:pink_dye',
        [
            'minecraft:white_wool_stairs',
            'minecraft:orange_wool_stairs',
            'minecraft:magenta_wool_stairs',
            'minecraft:light_blue_wool_stairs',
            'minecraft:yellow_wool_stairs',
            'minecraft:lime_wool_stairs',
            'minecraft:gray_wool_stairs',
            'minecraft:light_gray_wool_stairs',
            'minecraft:cyan_wool_stairs',
            'minecraft:purple_wool_stairs',
            'minecraft:blue_wool_stairs',
            'minecraft:brown_wool_stairs',
            'minecraft:green_wool_stairs',
            'minecraft:red_wool_stairs',
            'minecraft:black_wool_stairs',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:pink_wool_stairs'),
    type='minecraft:crafting_shapeless',
)

DYE_PURPLE_BED = RecipeCraftingShapeless(
    group='bed_dye',
    ingredients=[
        'minecraft:purple_dye',
        [
            'minecraft:white_bed',
            'minecraft:orange_bed',
            'minecraft:magenta_bed',
            'minecraft:light_blue_bed',
            'minecraft:yellow_bed',
            'minecraft:lime_bed',
            'minecraft:pink_bed',
            'minecraft:gray_bed',
            'minecraft:light_gray_bed',
            'minecraft:cyan_bed',
            'minecraft:blue_bed',
            'minecraft:brown_bed',
            'minecraft:green_bed',
            'minecraft:red_bed',
            'minecraft:black_bed',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:purple_bed'),
    type='minecraft:crafting_shapeless',
)

DYE_PURPLE_CARPET = RecipeCraftingShapeless(
    group='carpet_dye',
    ingredients=[
        'minecraft:purple_dye',
        [
            'minecraft:white_carpet',
            'minecraft:orange_carpet',
            'minecraft:magenta_carpet',
            'minecraft:light_blue_carpet',
            'minecraft:yellow_carpet',
            'minecraft:lime_carpet',
            'minecraft:pink_carpet',
            'minecraft:gray_carpet',
            'minecraft:light_gray_carpet',
            'minecraft:cyan_carpet',
            'minecraft:blue_carpet',
            'minecraft:brown_carpet',
            'minecraft:green_carpet',
            'minecraft:red_carpet',
            'minecraft:black_carpet',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:purple_carpet'),
    type='minecraft:crafting_shapeless',
)

DYE_PURPLE_CUSHION = RecipeCraftingShapeless(
    group='cushion_dye',
    ingredients=[
        'minecraft:purple_dye',
        [
            'minecraft:white_cushion',
            'minecraft:orange_cushion',
            'minecraft:magenta_cushion',
            'minecraft:light_blue_cushion',
            'minecraft:yellow_cushion',
            'minecraft:lime_cushion',
            'minecraft:pink_cushion',
            'minecraft:gray_cushion',
            'minecraft:light_gray_cushion',
            'minecraft:cyan_cushion',
            'minecraft:blue_cushion',
            'minecraft:brown_cushion',
            'minecraft:green_cushion',
            'minecraft:red_cushion',
            'minecraft:black_cushion',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:purple_cushion'),
    type='minecraft:crafting_shapeless',
)

DYE_PURPLE_HARNESS = RecipeCraftingShapeless(
    group='harness_dye',
    category=CraftingBookCategory.EQUIPMENT,
    ingredients=[
        'minecraft:purple_dye',
        [
            'minecraft:white_harness',
            'minecraft:orange_harness',
            'minecraft:magenta_harness',
            'minecraft:light_blue_harness',
            'minecraft:yellow_harness',
            'minecraft:lime_harness',
            'minecraft:pink_harness',
            'minecraft:gray_harness',
            'minecraft:light_gray_harness',
            'minecraft:cyan_harness',
            'minecraft:blue_harness',
            'minecraft:brown_harness',
            'minecraft:green_harness',
            'minecraft:red_harness',
            'minecraft:black_harness',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:purple_harness'),
    type='minecraft:crafting_shapeless',
)

DYE_PURPLE_WOOL = RecipeCraftingShapeless(
    group='wool',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:purple_dye',
        [
            'minecraft:white_wool',
            'minecraft:orange_wool',
            'minecraft:magenta_wool',
            'minecraft:light_blue_wool',
            'minecraft:yellow_wool',
            'minecraft:lime_wool',
            'minecraft:pink_wool',
            'minecraft:gray_wool',
            'minecraft:light_gray_wool',
            'minecraft:cyan_wool',
            'minecraft:blue_wool',
            'minecraft:brown_wool',
            'minecraft:green_wool',
            'minecraft:red_wool',
            'minecraft:black_wool',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:purple_wool'),
    type='minecraft:crafting_shapeless',
)

DYE_PURPLE_WOOL_SLAB = RecipeCraftingShapeless(
    group='wool_slabs',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:purple_dye',
        [
            'minecraft:white_wool_slab',
            'minecraft:orange_wool_slab',
            'minecraft:magenta_wool_slab',
            'minecraft:light_blue_wool_slab',
            'minecraft:yellow_wool_slab',
            'minecraft:lime_wool_slab',
            'minecraft:pink_wool_slab',
            'minecraft:gray_wool_slab',
            'minecraft:light_gray_wool_slab',
            'minecraft:cyan_wool_slab',
            'minecraft:blue_wool_slab',
            'minecraft:brown_wool_slab',
            'minecraft:green_wool_slab',
            'minecraft:red_wool_slab',
            'minecraft:black_wool_slab',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:purple_wool_slab'),
    type='minecraft:crafting_shapeless',
)

DYE_PURPLE_WOOL_STAIRS = RecipeCraftingShapeless(
    group='wool_stairs',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:purple_dye',
        [
            'minecraft:white_wool_stairs',
            'minecraft:orange_wool_stairs',
            'minecraft:magenta_wool_stairs',
            'minecraft:light_blue_wool_stairs',
            'minecraft:yellow_wool_stairs',
            'minecraft:lime_wool_stairs',
            'minecraft:pink_wool_stairs',
            'minecraft:gray_wool_stairs',
            'minecraft:light_gray_wool_stairs',
            'minecraft:cyan_wool_stairs',
            'minecraft:blue_wool_stairs',
            'minecraft:brown_wool_stairs',
            'minecraft:green_wool_stairs',
            'minecraft:red_wool_stairs',
            'minecraft:black_wool_stairs',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:purple_wool_stairs'),
    type='minecraft:crafting_shapeless',
)

DYE_RED_BED = RecipeCraftingShapeless(
    group='bed_dye',
    ingredients=[
        'minecraft:red_dye',
        [
            'minecraft:white_bed',
            'minecraft:orange_bed',
            'minecraft:magenta_bed',
            'minecraft:light_blue_bed',
            'minecraft:yellow_bed',
            'minecraft:lime_bed',
            'minecraft:pink_bed',
            'minecraft:gray_bed',
            'minecraft:light_gray_bed',
            'minecraft:cyan_bed',
            'minecraft:purple_bed',
            'minecraft:blue_bed',
            'minecraft:brown_bed',
            'minecraft:green_bed',
            'minecraft:black_bed',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:red_bed'),
    type='minecraft:crafting_shapeless',
)

DYE_RED_CARPET = RecipeCraftingShapeless(
    group='carpet_dye',
    ingredients=[
        'minecraft:red_dye',
        [
            'minecraft:white_carpet',
            'minecraft:orange_carpet',
            'minecraft:magenta_carpet',
            'minecraft:light_blue_carpet',
            'minecraft:yellow_carpet',
            'minecraft:lime_carpet',
            'minecraft:pink_carpet',
            'minecraft:gray_carpet',
            'minecraft:light_gray_carpet',
            'minecraft:cyan_carpet',
            'minecraft:purple_carpet',
            'minecraft:blue_carpet',
            'minecraft:brown_carpet',
            'minecraft:green_carpet',
            'minecraft:black_carpet',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:red_carpet'),
    type='minecraft:crafting_shapeless',
)

DYE_RED_CUSHION = RecipeCraftingShapeless(
    group='cushion_dye',
    ingredients=[
        'minecraft:red_dye',
        [
            'minecraft:white_cushion',
            'minecraft:orange_cushion',
            'minecraft:magenta_cushion',
            'minecraft:light_blue_cushion',
            'minecraft:yellow_cushion',
            'minecraft:lime_cushion',
            'minecraft:pink_cushion',
            'minecraft:gray_cushion',
            'minecraft:light_gray_cushion',
            'minecraft:cyan_cushion',
            'minecraft:purple_cushion',
            'minecraft:blue_cushion',
            'minecraft:brown_cushion',
            'minecraft:green_cushion',
            'minecraft:black_cushion',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:red_cushion'),
    type='minecraft:crafting_shapeless',
)

DYE_RED_HARNESS = RecipeCraftingShapeless(
    group='harness_dye',
    category=CraftingBookCategory.EQUIPMENT,
    ingredients=[
        'minecraft:red_dye',
        [
            'minecraft:white_harness',
            'minecraft:orange_harness',
            'minecraft:magenta_harness',
            'minecraft:light_blue_harness',
            'minecraft:yellow_harness',
            'minecraft:lime_harness',
            'minecraft:pink_harness',
            'minecraft:gray_harness',
            'minecraft:light_gray_harness',
            'minecraft:cyan_harness',
            'minecraft:purple_harness',
            'minecraft:blue_harness',
            'minecraft:brown_harness',
            'minecraft:green_harness',
            'minecraft:black_harness',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:red_harness'),
    type='minecraft:crafting_shapeless',
)

DYE_RED_WOOL = RecipeCraftingShapeless(
    group='wool',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:red_dye',
        [
            'minecraft:white_wool',
            'minecraft:orange_wool',
            'minecraft:magenta_wool',
            'minecraft:light_blue_wool',
            'minecraft:yellow_wool',
            'minecraft:lime_wool',
            'minecraft:pink_wool',
            'minecraft:gray_wool',
            'minecraft:light_gray_wool',
            'minecraft:cyan_wool',
            'minecraft:purple_wool',
            'minecraft:blue_wool',
            'minecraft:brown_wool',
            'minecraft:green_wool',
            'minecraft:black_wool',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:red_wool'),
    type='minecraft:crafting_shapeless',
)

DYE_RED_WOOL_SLAB = RecipeCraftingShapeless(
    group='wool_slabs',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:red_dye',
        [
            'minecraft:white_wool_slab',
            'minecraft:orange_wool_slab',
            'minecraft:magenta_wool_slab',
            'minecraft:light_blue_wool_slab',
            'minecraft:yellow_wool_slab',
            'minecraft:lime_wool_slab',
            'minecraft:pink_wool_slab',
            'minecraft:gray_wool_slab',
            'minecraft:light_gray_wool_slab',
            'minecraft:cyan_wool_slab',
            'minecraft:purple_wool_slab',
            'minecraft:blue_wool_slab',
            'minecraft:brown_wool_slab',
            'minecraft:green_wool_slab',
            'minecraft:black_wool_slab',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:red_wool_slab'),
    type='minecraft:crafting_shapeless',
)

DYE_RED_WOOL_STAIRS = RecipeCraftingShapeless(
    group='wool_stairs',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:red_dye',
        [
            'minecraft:white_wool_stairs',
            'minecraft:orange_wool_stairs',
            'minecraft:magenta_wool_stairs',
            'minecraft:light_blue_wool_stairs',
            'minecraft:yellow_wool_stairs',
            'minecraft:lime_wool_stairs',
            'minecraft:pink_wool_stairs',
            'minecraft:gray_wool_stairs',
            'minecraft:light_gray_wool_stairs',
            'minecraft:cyan_wool_stairs',
            'minecraft:purple_wool_stairs',
            'minecraft:blue_wool_stairs',
            'minecraft:brown_wool_stairs',
            'minecraft:green_wool_stairs',
            'minecraft:black_wool_stairs',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:red_wool_stairs'),
    type='minecraft:crafting_shapeless',
)

DYE_WHITE_BED = RecipeCraftingShapeless(
    group='bed_dye',
    ingredients=[
        'minecraft:white_dye',
        [
            'minecraft:orange_bed',
            'minecraft:magenta_bed',
            'minecraft:light_blue_bed',
            'minecraft:yellow_bed',
            'minecraft:lime_bed',
            'minecraft:pink_bed',
            'minecraft:gray_bed',
            'minecraft:light_gray_bed',
            'minecraft:cyan_bed',
            'minecraft:purple_bed',
            'minecraft:blue_bed',
            'minecraft:brown_bed',
            'minecraft:green_bed',
            'minecraft:red_bed',
            'minecraft:black_bed',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:white_bed'),
    type='minecraft:crafting_shapeless',
)

DYE_WHITE_CARPET = RecipeCraftingShapeless(
    group='carpet_dye',
    ingredients=[
        'minecraft:white_dye',
        [
            'minecraft:orange_carpet',
            'minecraft:magenta_carpet',
            'minecraft:light_blue_carpet',
            'minecraft:yellow_carpet',
            'minecraft:lime_carpet',
            'minecraft:pink_carpet',
            'minecraft:gray_carpet',
            'minecraft:light_gray_carpet',
            'minecraft:cyan_carpet',
            'minecraft:purple_carpet',
            'minecraft:blue_carpet',
            'minecraft:brown_carpet',
            'minecraft:green_carpet',
            'minecraft:red_carpet',
            'minecraft:black_carpet',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:white_carpet'),
    type='minecraft:crafting_shapeless',
)

DYE_WHITE_CUSHION = RecipeCraftingShapeless(
    group='cushion_dye',
    ingredients=[
        'minecraft:white_dye',
        [
            'minecraft:orange_cushion',
            'minecraft:magenta_cushion',
            'minecraft:light_blue_cushion',
            'minecraft:yellow_cushion',
            'minecraft:lime_cushion',
            'minecraft:pink_cushion',
            'minecraft:gray_cushion',
            'minecraft:light_gray_cushion',
            'minecraft:cyan_cushion',
            'minecraft:purple_cushion',
            'minecraft:blue_cushion',
            'minecraft:brown_cushion',
            'minecraft:green_cushion',
            'minecraft:red_cushion',
            'minecraft:black_cushion',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:white_cushion'),
    type='minecraft:crafting_shapeless',
)

DYE_WHITE_HARNESS = RecipeCraftingShapeless(
    group='harness_dye',
    category=CraftingBookCategory.EQUIPMENT,
    ingredients=[
        'minecraft:white_dye',
        [
            'minecraft:orange_harness',
            'minecraft:magenta_harness',
            'minecraft:light_blue_harness',
            'minecraft:yellow_harness',
            'minecraft:lime_harness',
            'minecraft:pink_harness',
            'minecraft:gray_harness',
            'minecraft:light_gray_harness',
            'minecraft:cyan_harness',
            'minecraft:purple_harness',
            'minecraft:blue_harness',
            'minecraft:brown_harness',
            'minecraft:green_harness',
            'minecraft:red_harness',
            'minecraft:black_harness',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:white_harness'),
    type='minecraft:crafting_shapeless',
)

DYE_WHITE_WOOL = RecipeCraftingShapeless(
    group='wool',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:white_dye',
        [
            'minecraft:orange_wool',
            'minecraft:magenta_wool',
            'minecraft:light_blue_wool',
            'minecraft:yellow_wool',
            'minecraft:lime_wool',
            'minecraft:pink_wool',
            'minecraft:gray_wool',
            'minecraft:light_gray_wool',
            'minecraft:cyan_wool',
            'minecraft:purple_wool',
            'minecraft:blue_wool',
            'minecraft:brown_wool',
            'minecraft:green_wool',
            'minecraft:red_wool',
            'minecraft:black_wool',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:white_wool'),
    type='minecraft:crafting_shapeless',
)

DYE_WHITE_WOOL_SLAB = RecipeCraftingShapeless(
    group='wool_slabs',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:white_dye',
        [
            'minecraft:orange_wool_slab',
            'minecraft:magenta_wool_slab',
            'minecraft:light_blue_wool_slab',
            'minecraft:yellow_wool_slab',
            'minecraft:lime_wool_slab',
            'minecraft:pink_wool_slab',
            'minecraft:gray_wool_slab',
            'minecraft:light_gray_wool_slab',
            'minecraft:cyan_wool_slab',
            'minecraft:purple_wool_slab',
            'minecraft:blue_wool_slab',
            'minecraft:brown_wool_slab',
            'minecraft:green_wool_slab',
            'minecraft:red_wool_slab',
            'minecraft:black_wool_slab',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:white_wool_slab'),
    type='minecraft:crafting_shapeless',
)

DYE_WHITE_WOOL_STAIRS = RecipeCraftingShapeless(
    group='wool_stairs',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:white_dye',
        [
            'minecraft:orange_wool_stairs',
            'minecraft:magenta_wool_stairs',
            'minecraft:light_blue_wool_stairs',
            'minecraft:yellow_wool_stairs',
            'minecraft:lime_wool_stairs',
            'minecraft:pink_wool_stairs',
            'minecraft:gray_wool_stairs',
            'minecraft:light_gray_wool_stairs',
            'minecraft:cyan_wool_stairs',
            'minecraft:purple_wool_stairs',
            'minecraft:blue_wool_stairs',
            'minecraft:brown_wool_stairs',
            'minecraft:green_wool_stairs',
            'minecraft:red_wool_stairs',
            'minecraft:black_wool_stairs',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:white_wool_stairs'),
    type='minecraft:crafting_shapeless',
)

DYE_YELLOW_BED = RecipeCraftingShapeless(
    group='bed_dye',
    ingredients=[
        'minecraft:yellow_dye',
        [
            'minecraft:white_bed',
            'minecraft:orange_bed',
            'minecraft:magenta_bed',
            'minecraft:light_blue_bed',
            'minecraft:lime_bed',
            'minecraft:pink_bed',
            'minecraft:gray_bed',
            'minecraft:light_gray_bed',
            'minecraft:cyan_bed',
            'minecraft:purple_bed',
            'minecraft:blue_bed',
            'minecraft:brown_bed',
            'minecraft:green_bed',
            'minecraft:red_bed',
            'minecraft:black_bed',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:yellow_bed'),
    type='minecraft:crafting_shapeless',
)

DYE_YELLOW_CARPET = RecipeCraftingShapeless(
    group='carpet_dye',
    ingredients=[
        'minecraft:yellow_dye',
        [
            'minecraft:white_carpet',
            'minecraft:orange_carpet',
            'minecraft:magenta_carpet',
            'minecraft:light_blue_carpet',
            'minecraft:lime_carpet',
            'minecraft:pink_carpet',
            'minecraft:gray_carpet',
            'minecraft:light_gray_carpet',
            'minecraft:cyan_carpet',
            'minecraft:purple_carpet',
            'minecraft:blue_carpet',
            'minecraft:brown_carpet',
            'minecraft:green_carpet',
            'minecraft:red_carpet',
            'minecraft:black_carpet',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:yellow_carpet'),
    type='minecraft:crafting_shapeless',
)

DYE_YELLOW_CUSHION = RecipeCraftingShapeless(
    group='cushion_dye',
    ingredients=[
        'minecraft:yellow_dye',
        [
            'minecraft:white_cushion',
            'minecraft:orange_cushion',
            'minecraft:magenta_cushion',
            'minecraft:light_blue_cushion',
            'minecraft:lime_cushion',
            'minecraft:pink_cushion',
            'minecraft:gray_cushion',
            'minecraft:light_gray_cushion',
            'minecraft:cyan_cushion',
            'minecraft:purple_cushion',
            'minecraft:blue_cushion',
            'minecraft:brown_cushion',
            'minecraft:green_cushion',
            'minecraft:red_cushion',
            'minecraft:black_cushion',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:yellow_cushion'),
    type='minecraft:crafting_shapeless',
)

DYE_YELLOW_HARNESS = RecipeCraftingShapeless(
    group='harness_dye',
    category=CraftingBookCategory.EQUIPMENT,
    ingredients=[
        'minecraft:yellow_dye',
        [
            'minecraft:white_harness',
            'minecraft:orange_harness',
            'minecraft:magenta_harness',
            'minecraft:light_blue_harness',
            'minecraft:lime_harness',
            'minecraft:pink_harness',
            'minecraft:gray_harness',
            'minecraft:light_gray_harness',
            'minecraft:cyan_harness',
            'minecraft:purple_harness',
            'minecraft:blue_harness',
            'minecraft:brown_harness',
            'minecraft:green_harness',
            'minecraft:red_harness',
            'minecraft:black_harness',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:yellow_harness'),
    type='minecraft:crafting_shapeless',
)

DYE_YELLOW_WOOL = RecipeCraftingShapeless(
    group='wool',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:yellow_dye',
        [
            'minecraft:white_wool',
            'minecraft:orange_wool',
            'minecraft:magenta_wool',
            'minecraft:light_blue_wool',
            'minecraft:lime_wool',
            'minecraft:pink_wool',
            'minecraft:gray_wool',
            'minecraft:light_gray_wool',
            'minecraft:cyan_wool',
            'minecraft:purple_wool',
            'minecraft:blue_wool',
            'minecraft:brown_wool',
            'minecraft:green_wool',
            'minecraft:red_wool',
            'minecraft:black_wool',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:yellow_wool'),
    type='minecraft:crafting_shapeless',
)

DYE_YELLOW_WOOL_SLAB = RecipeCraftingShapeless(
    group='wool_slabs',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:yellow_dye',
        [
            'minecraft:white_wool_slab',
            'minecraft:orange_wool_slab',
            'minecraft:magenta_wool_slab',
            'minecraft:light_blue_wool_slab',
            'minecraft:lime_wool_slab',
            'minecraft:pink_wool_slab',
            'minecraft:gray_wool_slab',
            'minecraft:light_gray_wool_slab',
            'minecraft:cyan_wool_slab',
            'minecraft:purple_wool_slab',
            'minecraft:blue_wool_slab',
            'minecraft:brown_wool_slab',
            'minecraft:green_wool_slab',
            'minecraft:red_wool_slab',
            'minecraft:black_wool_slab',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:yellow_wool_slab'),
    type='minecraft:crafting_shapeless',
)

DYE_YELLOW_WOOL_STAIRS = RecipeCraftingShapeless(
    group='wool_stairs',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:yellow_dye',
        [
            'minecraft:white_wool_stairs',
            'minecraft:orange_wool_stairs',
            'minecraft:magenta_wool_stairs',
            'minecraft:light_blue_wool_stairs',
            'minecraft:lime_wool_stairs',
            'minecraft:pink_wool_stairs',
            'minecraft:gray_wool_stairs',
            'minecraft:light_gray_wool_stairs',
            'minecraft:cyan_wool_stairs',
            'minecraft:purple_wool_stairs',
            'minecraft:blue_wool_stairs',
            'minecraft:brown_wool_stairs',
            'minecraft:green_wool_stairs',
            'minecraft:red_wool_stairs',
            'minecraft:black_wool_stairs',
        ],
    ],
    result=ItemStackOfComponent(id='minecraft:yellow_wool_stairs'),
    type='minecraft:crafting_shapeless',
)

EMERALD = RecipeCraftingShapeless(
    ingredients=['minecraft:emerald_block'],
    result=ItemStackOfComponent(id='minecraft:emerald', count=9),
    type='minecraft:crafting_shapeless',
)

EMERALD_BLOCK = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '###', '###'],
    key={'#': 'minecraft:emerald'},
    result=ItemStackOfComponent(id='minecraft:emerald_block'),
    type='minecraft:crafting_shaped',
)

EMERALD_FROM_BLASTING_DEEPSLATE_EMERALD_ORE = RecipeBlasting(
    group='emerald',
    ingredient='minecraft:deepslate_emerald_ore',
    result=ItemStackOfComponent(id='minecraft:emerald'),
    experience=1.0,
    cookingtime=200,
    type='minecraft:blasting',
)

EMERALD_FROM_BLASTING_EMERALD_ORE = RecipeBlasting(
    group='emerald',
    ingredient='minecraft:emerald_ore',
    result=ItemStackOfComponent(id='minecraft:emerald'),
    experience=1.0,
    cookingtime=200,
    type='minecraft:blasting',
)

EMERALD_FROM_SMELTING_DEEPSLATE_EMERALD_ORE = RecipeSmelting(
    group='emerald',
    ingredient='minecraft:deepslate_emerald_ore',
    result=ItemStackOfComponent(id='minecraft:emerald'),
    experience=1.0,
    cookingtime=200,
    type='minecraft:smelting',
)

EMERALD_FROM_SMELTING_EMERALD_ORE = RecipeSmelting(
    group='emerald',
    ingredient='minecraft:emerald_ore',
    result=ItemStackOfComponent(id='minecraft:emerald'),
    experience=1.0,
    cookingtime=200,
    type='minecraft:smelting',
)

ENCHANTING_TABLE = RecipeCraftingShaped(
    pattern=[' B ', 'D#D', '###'],
    key={'#': 'minecraft:obsidian', 'B': 'minecraft:book', 'D': 'minecraft:diamond'},
    result=ItemStackOfComponent(id='minecraft:enchanting_table'),
    type='minecraft:crafting_shaped',
)

ENDER_CHEST = RecipeCraftingShaped(
    pattern=['###', '#E#', '###'],
    key={'#': 'minecraft:obsidian', 'E': 'minecraft:ender_eye'},
    result=ItemStackOfComponent(id='minecraft:ender_chest'),
    type='minecraft:crafting_shaped',
)

ENDER_EYE = RecipeCraftingShapeless(
    ingredients=['minecraft:ender_pearl', 'minecraft:blaze_powder'],
    result=ItemStackOfComponent(id='minecraft:ender_eye'),
    type='minecraft:crafting_shapeless',
)

END_CRYSTAL = RecipeCraftingShaped(
    pattern=['GGG', 'GEG', 'GTG'],
    key={'E': 'minecraft:ender_eye', 'G': 'minecraft:glass', 'T': 'minecraft:ghast_tear'},
    result=ItemStackOfComponent(id='minecraft:end_crystal'),
    type='minecraft:crafting_shaped',
)

END_ROD = RecipeCraftingShaped(
    pattern=['/', '#'],
    key={'#': 'minecraft:popped_chorus_fruit', '/': 'minecraft:blaze_rod'},
    result=ItemStackOfComponent(id='minecraft:end_rod', count=4),
    type='minecraft:crafting_shaped',
)

END_STONE_BRICKS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:end_stone'},
    result=ItemStackOfComponent(id='minecraft:end_stone_bricks', count=4),
    type='minecraft:crafting_shaped',
)

END_STONE_BRICKS_FROM_END_STONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:end_stone',
    result=ItemStackOfComponent(id='minecraft:end_stone_bricks'),
    type='minecraft:stonecutting',
)

END_STONE_BRICK_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:end_stone_bricks'},
    result=ItemStackOfComponent(id='minecraft:end_stone_brick_slab', count=6),
    type='minecraft:crafting_shaped',
)

END_STONE_BRICK_SLAB_FROM_END_STONE_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:end_stone_bricks',
    result=ItemStackOfComponent(id='minecraft:end_stone_brick_slab', count=2),
    type='minecraft:stonecutting',
)

END_STONE_BRICK_SLAB_FROM_END_STONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:end_stone',
    result=ItemStackOfComponent(id='minecraft:end_stone_brick_slab', count=2),
    type='minecraft:stonecutting',
)

END_STONE_BRICK_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:end_stone_bricks'},
    result=ItemStackOfComponent(id='minecraft:end_stone_brick_stairs', count=4),
    type='minecraft:crafting_shaped',
)

END_STONE_BRICK_STAIRS_FROM_END_STONE_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:end_stone_bricks',
    result=ItemStackOfComponent(id='minecraft:end_stone_brick_stairs'),
    type='minecraft:stonecutting',
)

END_STONE_BRICK_STAIRS_FROM_END_STONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:end_stone',
    result=ItemStackOfComponent(id='minecraft:end_stone_brick_stairs'),
    type='minecraft:stonecutting',
)

END_STONE_BRICK_WALL = RecipeCraftingShaped(
    pattern=['###', '###'],
    key={'#': 'minecraft:end_stone_bricks'},
    result=ItemStackOfComponent(id='minecraft:end_stone_brick_wall', count=6),
    type='minecraft:crafting_shaped',
)

END_STONE_BRICK_WALL_FROM_END_STONE_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:end_stone_bricks',
    result=ItemStackOfComponent(id='minecraft:end_stone_brick_wall'),
    type='minecraft:stonecutting',
)

END_STONE_BRICK_WALL_FROM_END_STONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:end_stone',
    result=ItemStackOfComponent(id='minecraft:end_stone_brick_wall'),
    type='minecraft:stonecutting',
)

EXPOSED_CHISELED_COPPER = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#', '#'],
    key={'#': 'minecraft:exposed_cut_copper_slab'},
    result=ItemStackOfComponent(id='minecraft:exposed_chiseled_copper'),
    type='minecraft:crafting_shaped',
)

EXPOSED_CHISELED_COPPER_FROM_EXPOSED_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:exposed_copper',
    result=ItemStackOfComponent(id='minecraft:exposed_chiseled_copper', count=4),
    type='minecraft:stonecutting',
)

EXPOSED_CHISELED_COPPER_FROM_EXPOSED_CUT_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:exposed_cut_copper',
    result=ItemStackOfComponent(id='minecraft:exposed_chiseled_copper'),
    type='minecraft:stonecutting',
)

EXPOSED_COPPER_BULB = RecipeCraftingShaped(
    group='exposed_copper_bulb',
    category=CraftingBookCategory.REDSTONE,
    pattern=[' C ', 'CBC', ' R '],
    key={'B': 'minecraft:blaze_rod', 'C': 'minecraft:exposed_copper', 'R': 'minecraft:redstone'},
    result=ItemStackOfComponent(id='minecraft:exposed_copper_bulb', count=4),
    type='minecraft:crafting_shaped',
)

EXPOSED_COPPER_GRATE = RecipeCraftingShaped(
    group='exposed_copper_grate',
    category=CraftingBookCategory.BUILDING,
    pattern=[' M ', 'M M', ' M '],
    key={'M': 'minecraft:exposed_copper'},
    result=ItemStackOfComponent(id='minecraft:exposed_copper_grate', count=4),
    type='minecraft:crafting_shaped',
)

EXPOSED_COPPER_GRATE_FROM_EXPOSED_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:exposed_copper',
    result=ItemStackOfComponent(id='minecraft:exposed_copper_grate', count=4),
    type='minecraft:stonecutting',
)

EXPOSED_CUT_COPPER = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:exposed_copper'},
    result=ItemStackOfComponent(id='minecraft:exposed_cut_copper', count=4),
    type='minecraft:crafting_shaped',
)

EXPOSED_CUT_COPPER_FROM_EXPOSED_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:exposed_copper',
    result=ItemStackOfComponent(id='minecraft:exposed_cut_copper', count=4),
    type='minecraft:stonecutting',
)

EXPOSED_CUT_COPPER_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:exposed_cut_copper'},
    result=ItemStackOfComponent(id='minecraft:exposed_cut_copper_slab', count=6),
    type='minecraft:crafting_shaped',
)

EXPOSED_CUT_COPPER_SLAB_FROM_EXPOSED_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:exposed_copper',
    result=ItemStackOfComponent(id='minecraft:exposed_cut_copper_slab', count=8),
    type='minecraft:stonecutting',
)

EXPOSED_CUT_COPPER_SLAB_FROM_EXPOSED_CUT_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:exposed_cut_copper',
    result=ItemStackOfComponent(id='minecraft:exposed_cut_copper_slab', count=2),
    type='minecraft:stonecutting',
)

EXPOSED_CUT_COPPER_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:exposed_cut_copper'},
    result=ItemStackOfComponent(id='minecraft:exposed_cut_copper_stairs', count=4),
    type='minecraft:crafting_shaped',
)

EXPOSED_CUT_COPPER_STAIRS_FROM_EXPOSED_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:exposed_copper',
    result=ItemStackOfComponent(id='minecraft:exposed_cut_copper_stairs', count=4),
    type='minecraft:stonecutting',
)

EXPOSED_CUT_COPPER_STAIRS_FROM_EXPOSED_CUT_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:exposed_cut_copper',
    result=ItemStackOfComponent(id='minecraft:exposed_cut_copper_stairs'),
    type='minecraft:stonecutting',
)

EYE_ARMOR_TRIM_SMITHING_TEMPLATE = RecipeCraftingShaped(
    pattern=['#S#', '#C#', '###'],
    key={'#': 'minecraft:diamond', 'C': 'minecraft:end_stone', 'S': 'minecraft:eye_armor_trim_smithing_template'},
    result=ItemStackOfComponent(id='minecraft:eye_armor_trim_smithing_template', count=2),
    type='minecraft:crafting_shaped',
)

EYE_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = RecipeSmithingTrim(
    base='#minecraft:trimmable_armor',
    addition='#minecraft:trim_materials',
    template='minecraft:eye_armor_trim_smithing_template',
    pattern='minecraft:eye',
    type='minecraft:smithing_trim',
)

FERMENTED_SPIDER_EYE = RecipeCraftingShapeless(
    ingredients=['minecraft:spider_eye', 'minecraft:brown_mushroom', 'minecraft:sugar'],
    result=ItemStackOfComponent(id='minecraft:fermented_spider_eye'),
    type='minecraft:crafting_shapeless',
)

FIELD_MASONED_BANNER_PATTERN = RecipeCraftingShapeless(
    ingredients=['minecraft:paper', 'minecraft:bricks'],
    result=ItemStackOfComponent(id='minecraft:field_masoned_banner_pattern'),
    type='minecraft:crafting_shapeless',
)

FIREWORK_ROCKET = RecipeCraftingSpecialFireworkRocket(
    type='minecraft:crafting_special_firework_rocket',
    **dict[str, Any]({
        'fuel': 'minecraft:gunpowder',
        'result': {'count': 3, 'id': 'minecraft:firework_rocket'},
        'shell': 'minecraft:paper',
        'star': 'minecraft:firework_star',
    }),
)

FIREWORK_ROCKET_SIMPLE = RecipeCraftingShapeless(
    ingredients=['minecraft:gunpowder', 'minecraft:paper'],
    result=ItemStackOfComponent(id='minecraft:firework_rocket', count=3),
    type='minecraft:crafting_shapeless',
)

FIREWORK_STAR = RecipeCraftingSpecialFireworkStar(
    type='minecraft:crafting_special_firework_star',
    **dict[str, Any]({
        'dye': '#minecraft:dyes',
        'fuel': 'minecraft:gunpowder',
        'result': {'id': 'minecraft:firework_star'},
        'shapes': {
            'burst': 'minecraft:feather',
            'creeper': '#minecraft:skulls',
            'large_ball': 'minecraft:fire_charge',
            'star': 'minecraft:gold_nugget',
        },
        'trail': 'minecraft:diamond',
        'twinkle': 'minecraft:glowstone_dust',
    }),
)

FIREWORK_STAR_FADE = RecipeCraftingSpecialFireworkStarFade(
    type='minecraft:crafting_special_firework_star_fade',
    **dict[str, Any]({'dye': '#minecraft:dyes', 'result': {'id': 'minecraft:firework_star'}, 'target': 'minecraft:firework_star'}),
)

FIRE_CHARGE = RecipeCraftingShapeless(
    ingredients=['minecraft:gunpowder', 'minecraft:blaze_powder', ['minecraft:coal', 'minecraft:charcoal']],
    result=ItemStackOfComponent(id='minecraft:fire_charge', count=3),
    type='minecraft:crafting_shapeless',
)

FISHING_ROD = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['  #', ' #X', '# X'],
    key={'#': 'minecraft:stick', 'X': 'minecraft:string'},
    result=ItemStackOfComponent(id='minecraft:fishing_rod'),
    type='minecraft:crafting_shaped',
)

FLETCHING_TABLE = RecipeCraftingShaped(
    pattern=['@@', '##', '##'],
    key={'#': '#minecraft:planks', '@': 'minecraft:flint'},
    result=ItemStackOfComponent(id='minecraft:fletching_table'),
    type='minecraft:crafting_shaped',
)

FLINT_AND_STEEL = RecipeCraftingShapeless(
    category=CraftingBookCategory.EQUIPMENT,
    ingredients=['minecraft:iron_ingot', 'minecraft:flint'],
    result=ItemStackOfComponent(id='minecraft:flint_and_steel'),
    type='minecraft:crafting_shapeless',
)

FLOWER_BANNER_PATTERN = RecipeCraftingShapeless(
    ingredients=['minecraft:paper', 'minecraft:oxeye_daisy'],
    result=ItemStackOfComponent(id='minecraft:flower_banner_pattern'),
    type='minecraft:crafting_shapeless',
)

FLOWER_POT = RecipeCraftingShaped(
    pattern=['# #', ' # '],
    key={'#': 'minecraft:brick'},
    result=ItemStackOfComponent(id='minecraft:flower_pot'),
    type='minecraft:crafting_shaped',
)

FLOW_ARMOR_TRIM_SMITHING_TEMPLATE = RecipeCraftingShaped(
    pattern=['#S#', '#C#', '###'],
    key={'#': 'minecraft:diamond', 'C': 'minecraft:breeze_rod', 'S': 'minecraft:flow_armor_trim_smithing_template'},
    result=ItemStackOfComponent(id='minecraft:flow_armor_trim_smithing_template', count=2),
    type='minecraft:crafting_shaped',
)

FLOW_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = RecipeSmithingTrim(
    base='#minecraft:trimmable_armor',
    addition='#minecraft:trim_materials',
    template='minecraft:flow_armor_trim_smithing_template',
    pattern='minecraft:flow',
    type='minecraft:smithing_trim',
)

FURNACE = RecipeCraftingShaped(
    pattern=['###', '# #', '###'],
    key={'#': '#minecraft:stone_crafting_materials'},
    result=ItemStackOfComponent(id='minecraft:furnace'),
    type='minecraft:crafting_shaped',
)

FURNACE_MINECART = RecipeCraftingShapeless(
    ingredients=['minecraft:furnace', 'minecraft:minecart'],
    result=ItemStackOfComponent(id='minecraft:furnace_minecart'),
    type='minecraft:crafting_shapeless',
)

GLASS = RecipeSmelting(
    category=CookingBookCategory.BLOCKS,
    ingredient='#minecraft:smelts_to_glass',
    result=ItemStackOfComponent(id='minecraft:glass'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

GLASS_BOTTLE = RecipeCraftingShaped(
    pattern=['# #', ' # '],
    key={'#': 'minecraft:glass'},
    result=ItemStackOfComponent(id='minecraft:glass_bottle', count=3),
    type='minecraft:crafting_shaped',
)

GLASS_PANE = RecipeCraftingShaped(
    pattern=['###', '###'],
    key={'#': 'minecraft:glass'},
    result=ItemStackOfComponent(id='minecraft:glass_pane', count=16),
    type='minecraft:crafting_shaped',
)

GLISTERING_MELON_SLICE = RecipeCraftingShaped(
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:gold_nugget', 'X': 'minecraft:melon_slice'},
    result=ItemStackOfComponent(id='minecraft:glistering_melon_slice'),
    type='minecraft:crafting_shaped',
)

GLOWSTONE = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:glowstone_dust'},
    result=ItemStackOfComponent(id='minecraft:glowstone'),
    type='minecraft:crafting_shaped',
)

GLOW_ITEM_FRAME = RecipeCraftingShapeless(
    ingredients=['minecraft:item_frame', 'minecraft:glow_ink_sac'],
    result=ItemStackOfComponent(id='minecraft:glow_item_frame'),
    type='minecraft:crafting_shapeless',
)

GOLDEN_APPLE = RecipeCraftingShaped(
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:gold_ingot', 'X': 'minecraft:apple'},
    result=ItemStackOfComponent(id='minecraft:golden_apple'),
    type='minecraft:crafting_shaped',
)

GOLDEN_AXE = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['XX', 'X#', ' #'],
    key={'#': 'minecraft:stick', 'X': '#minecraft:gold_tool_materials'},
    result=ItemStackOfComponent(id='minecraft:golden_axe'),
    type='minecraft:crafting_shaped',
)

GOLDEN_BOOTS = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['X X', 'X X'],
    key={'X': 'minecraft:gold_ingot'},
    result=ItemStackOfComponent(id='minecraft:golden_boots'),
    type='minecraft:crafting_shaped',
)

GOLDEN_CARROT = RecipeCraftingShaped(
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:gold_nugget', 'X': 'minecraft:carrot'},
    result=ItemStackOfComponent(id='minecraft:golden_carrot'),
    type='minecraft:crafting_shaped',
)

GOLDEN_CHESTPLATE = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['X X', 'XXX', 'XXX'],
    key={'X': 'minecraft:gold_ingot'},
    result=ItemStackOfComponent(id='minecraft:golden_chestplate'),
    type='minecraft:crafting_shaped',
)

GOLDEN_DANDELION = RecipeCraftingShaped(
    pattern=['###', '#I#', '###'],
    key={'#': 'minecraft:gold_nugget', 'I': 'minecraft:dandelion'},
    result=ItemStackOfComponent(id='minecraft:golden_dandelion'),
    type='minecraft:crafting_shaped',
)

GOLDEN_HELMET = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['XXX', 'X X'],
    key={'X': 'minecraft:gold_ingot'},
    result=ItemStackOfComponent(id='minecraft:golden_helmet'),
    type='minecraft:crafting_shaped',
)

GOLDEN_HOE = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['XX', ' #', ' #'],
    key={'#': 'minecraft:stick', 'X': '#minecraft:gold_tool_materials'},
    result=ItemStackOfComponent(id='minecraft:golden_hoe'),
    type='minecraft:crafting_shaped',
)

GOLDEN_LEGGINGS = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['XXX', 'X X', 'X X'],
    key={'X': 'minecraft:gold_ingot'},
    result=ItemStackOfComponent(id='minecraft:golden_leggings'),
    type='minecraft:crafting_shaped',
)

GOLDEN_PICKAXE = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['XXX', ' # ', ' # '],
    key={'#': 'minecraft:stick', 'X': '#minecraft:gold_tool_materials'},
    result=ItemStackOfComponent(id='minecraft:golden_pickaxe'),
    type='minecraft:crafting_shaped',
)

GOLDEN_SHOVEL = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['X', '#', '#'],
    key={'#': 'minecraft:stick', 'X': '#minecraft:gold_tool_materials'},
    result=ItemStackOfComponent(id='minecraft:golden_shovel'),
    type='minecraft:crafting_shaped',
)

GOLDEN_SPEAR = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['  X', ' # ', '#  '],
    key={'#': 'minecraft:stick', 'X': '#minecraft:gold_tool_materials'},
    result=ItemStackOfComponent(id='minecraft:golden_spear'),
    type='minecraft:crafting_shaped',
)

GOLDEN_SWORD = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['X', 'X', '#'],
    key={'#': 'minecraft:stick', 'X': '#minecraft:gold_tool_materials'},
    result=ItemStackOfComponent(id='minecraft:golden_sword'),
    type='minecraft:crafting_shaped',
)

GOLD_BLOCK = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '###', '###'],
    key={'#': 'minecraft:gold_ingot'},
    result=ItemStackOfComponent(id='minecraft:gold_block'),
    type='minecraft:crafting_shaped',
)

GOLD_INGOT_FROM_BLASTING_DEEPSLATE_GOLD_ORE = RecipeBlasting(
    group='gold_ingot',
    ingredient='minecraft:deepslate_gold_ore',
    result=ItemStackOfComponent(id='minecraft:gold_ingot'),
    experience=1.0,
    cookingtime=200,
    type='minecraft:blasting',
)

GOLD_INGOT_FROM_BLASTING_GOLD_ORE = RecipeBlasting(
    group='gold_ingot',
    ingredient='minecraft:gold_ore',
    result=ItemStackOfComponent(id='minecraft:gold_ingot'),
    experience=1.0,
    cookingtime=200,
    type='minecraft:blasting',
)

GOLD_INGOT_FROM_BLASTING_NETHER_GOLD_ORE = RecipeBlasting(
    group='gold_ingot',
    ingredient='minecraft:nether_gold_ore',
    result=ItemStackOfComponent(id='minecraft:gold_ingot'),
    experience=1.0,
    cookingtime=200,
    type='minecraft:blasting',
)

GOLD_INGOT_FROM_BLASTING_RAW_GOLD = RecipeBlasting(
    group='gold_ingot',
    ingredient='minecraft:raw_gold',
    result=ItemStackOfComponent(id='minecraft:gold_ingot'),
    experience=1.0,
    cookingtime=200,
    type='minecraft:blasting',
)

GOLD_INGOT_FROM_GOLD_BLOCK = RecipeCraftingShapeless(
    group='gold_ingot',
    ingredients=['minecraft:gold_block'],
    result=ItemStackOfComponent(id='minecraft:gold_ingot', count=9),
    type='minecraft:crafting_shapeless',
)

GOLD_INGOT_FROM_NUGGETS = RecipeCraftingShaped(
    group='gold_ingot',
    pattern=['###', '###', '###'],
    key={'#': 'minecraft:gold_nugget'},
    result=ItemStackOfComponent(id='minecraft:gold_ingot'),
    type='minecraft:crafting_shaped',
)

GOLD_INGOT_FROM_SMELTING_DEEPSLATE_GOLD_ORE = RecipeSmelting(
    group='gold_ingot',
    ingredient='minecraft:deepslate_gold_ore',
    result=ItemStackOfComponent(id='minecraft:gold_ingot'),
    experience=1.0,
    cookingtime=200,
    type='minecraft:smelting',
)

GOLD_INGOT_FROM_SMELTING_GOLD_ORE = RecipeSmelting(
    group='gold_ingot',
    ingredient='minecraft:gold_ore',
    result=ItemStackOfComponent(id='minecraft:gold_ingot'),
    experience=1.0,
    cookingtime=200,
    type='minecraft:smelting',
)

GOLD_INGOT_FROM_SMELTING_NETHER_GOLD_ORE = RecipeSmelting(
    group='gold_ingot',
    ingredient='minecraft:nether_gold_ore',
    result=ItemStackOfComponent(id='minecraft:gold_ingot'),
    experience=1.0,
    cookingtime=200,
    type='minecraft:smelting',
)

GOLD_INGOT_FROM_SMELTING_RAW_GOLD = RecipeSmelting(
    group='gold_ingot',
    ingredient='minecraft:raw_gold',
    result=ItemStackOfComponent(id='minecraft:gold_ingot'),
    experience=1.0,
    cookingtime=200,
    type='minecraft:smelting',
)

GOLD_NUGGET = RecipeCraftingShapeless(
    ingredients=['minecraft:gold_ingot'],
    result=ItemStackOfComponent(id='minecraft:gold_nugget', count=9),
    type='minecraft:crafting_shapeless',
)

GOLD_NUGGET_FROM_BLASTING = RecipeBlasting(
    ingredient=[
        'minecraft:golden_pickaxe',
        'minecraft:golden_shovel',
        'minecraft:golden_axe',
        'minecraft:golden_hoe',
        'minecraft:golden_sword',
        'minecraft:golden_spear',
        'minecraft:golden_helmet',
        'minecraft:golden_chestplate',
        'minecraft:golden_leggings',
        'minecraft:golden_boots',
        'minecraft:golden_horse_armor',
        'minecraft:golden_nautilus_armor',
    ],
    result=ItemStackOfComponent(id='minecraft:gold_nugget'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:blasting',
)

GOLD_NUGGET_FROM_SMELTING = RecipeSmelting(
    ingredient=[
        'minecraft:golden_pickaxe',
        'minecraft:golden_shovel',
        'minecraft:golden_axe',
        'minecraft:golden_hoe',
        'minecraft:golden_sword',
        'minecraft:golden_spear',
        'minecraft:golden_helmet',
        'minecraft:golden_chestplate',
        'minecraft:golden_leggings',
        'minecraft:golden_boots',
        'minecraft:golden_horse_armor',
        'minecraft:golden_nautilus_armor',
    ],
    result=ItemStackOfComponent(id='minecraft:gold_nugget'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

GRANITE = RecipeCraftingShapeless(
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:diorite', 'minecraft:quartz'],
    result=ItemStackOfComponent(id='minecraft:granite'),
    type='minecraft:crafting_shapeless',
)

GRANITE_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:granite'},
    result=ItemStackOfComponent(id='minecraft:granite_slab', count=6),
    type='minecraft:crafting_shaped',
)

GRANITE_SLAB_FROM_GRANITE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:granite',
    result=ItemStackOfComponent(id='minecraft:granite_slab', count=2),
    type='minecraft:stonecutting',
)

GRANITE_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:granite'},
    result=ItemStackOfComponent(id='minecraft:granite_stairs', count=4),
    type='minecraft:crafting_shaped',
)

GRANITE_STAIRS_FROM_GRANITE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:granite',
    result=ItemStackOfComponent(id='minecraft:granite_stairs'),
    type='minecraft:stonecutting',
)

GRANITE_WALL = RecipeCraftingShaped(
    pattern=['###', '###'],
    key={'#': 'minecraft:granite'},
    result=ItemStackOfComponent(id='minecraft:granite_wall', count=6),
    type='minecraft:crafting_shaped',
)

GRANITE_WALL_FROM_GRANITE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:granite',
    result=ItemStackOfComponent(id='minecraft:granite_wall'),
    type='minecraft:stonecutting',
)

GRAY_BANNER = RecipeCraftingShaped(
    group='banner',
    pattern=['###', '###', ' | '],
    key={'#': 'minecraft:gray_wool', '|': 'minecraft:stick'},
    result=ItemStackOfComponent(id='minecraft:gray_banner'),
    type='minecraft:crafting_shaped',
)

GRAY_BANNER_DUPLICATE = RecipeCraftingSpecialBannerduplicate(
    type='minecraft:crafting_special_bannerduplicate',
    **dict[str, Any]({'banner': 'minecraft:gray_banner', 'result': {'id': 'minecraft:gray_banner'}}),
)

GRAY_BED = RecipeCraftingShaped(
    group='bed',
    pattern=['###', 'XXX'],
    key={'#': 'minecraft:gray_wool', 'X': '#minecraft:planks'},
    result=ItemStackOfComponent(id='minecraft:gray_bed'),
    type='minecraft:crafting_shaped',
)

GRAY_BUNDLE = RecipeCraftingTransmute(
    group='bundle_dye',
    category=CraftingBookCategory.EQUIPMENT,
    input='#minecraft:bundles',
    material='minecraft:gray_dye',
    result=TransmuteResult(id='minecraft:gray_bundle'),
    type='minecraft:crafting_transmute',
)

GRAY_CANDLE = RecipeCraftingShapeless(
    group='dyed_candle',
    ingredients=['minecraft:candle', 'minecraft:gray_dye'],
    result=ItemStackOfComponent(id='minecraft:gray_candle'),
    type='minecraft:crafting_shapeless',
)

GRAY_CARPET = RecipeCraftingShaped(
    group='woolen_carpet',
    pattern=['##'],
    key={'#': 'minecraft:gray_wool'},
    result=ItemStackOfComponent(id='minecraft:gray_carpet', count=3),
    type='minecraft:crafting_shaped',
)

GRAY_CONCRETE_POWDER = RecipeCraftingShapeless(
    group='concrete_powder',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:gray_dye',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:gravel',
        'minecraft:gravel',
        'minecraft:gravel',
        'minecraft:gravel',
    ],
    result=ItemStackOfComponent(id='minecraft:gray_concrete_powder', count=8),
    type='minecraft:crafting_shapeless',
)

GRAY_CONCRETE_SLAB = RecipeCraftingShaped(
    group='concrete_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:gray_concrete'},
    result=ItemStackOfComponent(id='minecraft:gray_concrete_slab', count=6),
    type='minecraft:crafting_shaped',
)

GRAY_CONCRETE_SLAB_FROM_GRAY_CONCRETE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:gray_concrete',
    result=ItemStackOfComponent(id='minecraft:gray_concrete_slab', count=2),
    type='minecraft:stonecutting',
)

GRAY_CONCRETE_STAIRS = RecipeCraftingShaped(
    group='concrete_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:gray_concrete'},
    result=ItemStackOfComponent(id='minecraft:gray_concrete_stairs', count=4),
    type='minecraft:crafting_shaped',
)

GRAY_CONCRETE_STAIRS_FROM_GRAY_CONCRETE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:gray_concrete',
    result=ItemStackOfComponent(id='minecraft:gray_concrete_stairs'),
    type='minecraft:stonecutting',
)

GRAY_CUSHION = RecipeCraftingShaped(
    group='cushion',
    pattern=['###'],
    key={'#': 'minecraft:gray_wool_slab'},
    result=ItemStackOfComponent(id='minecraft:gray_cushion'),
    type='minecraft:crafting_shaped',
)

GRAY_DYE = RecipeCraftingShapeless(
    group='gray_dye',
    ingredients=['minecraft:black_dye', 'minecraft:white_dye'],
    result=ItemStackOfComponent(id='minecraft:gray_dye', count=2),
    type='minecraft:crafting_shapeless',
)

GRAY_DYE_FROM_CLOSED_EYEBLOSSOM = RecipeCraftingShapeless(
    group='gray_dye',
    ingredients=['minecraft:closed_eyeblossom'],
    result=ItemStackOfComponent(id='minecraft:gray_dye'),
    type='minecraft:crafting_shapeless',
)

GRAY_GLAZED_TERRACOTTA = RecipeSmelting(
    category=CookingBookCategory.BLOCKS,
    ingredient='minecraft:gray_terracotta',
    result=ItemStackOfComponent(id='minecraft:gray_glazed_terracotta'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

GRAY_HARNESS = RecipeCraftingShaped(
    group='harness',
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['LLL', 'G#G'],
    key={'#': 'minecraft:gray_wool', 'G': 'minecraft:glass', 'L': 'minecraft:leather'},
    result=ItemStackOfComponent(id='minecraft:gray_harness'),
    type='minecraft:crafting_shaped',
)

GRAY_SHULKER_BOX = RecipeCraftingTransmute(
    group='shulker_box_dye',
    input='#minecraft:shulker_boxes',
    material='minecraft:gray_dye',
    result=TransmuteResult(id='minecraft:gray_shulker_box'),
    type='minecraft:crafting_transmute',
)

GRAY_STAINED_GLASS = RecipeCraftingShaped(
    group='stained_glass',
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:glass', 'X': 'minecraft:gray_dye'},
    result=ItemStackOfComponent(id='minecraft:gray_stained_glass', count=8),
    type='minecraft:crafting_shaped',
)

GRAY_STAINED_GLASS_PANE = RecipeCraftingShaped(
    group='stained_glass_pane',
    pattern=['###', '###'],
    key={'#': 'minecraft:gray_stained_glass'},
    result=ItemStackOfComponent(id='minecraft:gray_stained_glass_pane', count=16),
    type='minecraft:crafting_shaped',
)

GRAY_STAINED_GLASS_PANE_FROM_GLASS_PANE = RecipeCraftingShaped(
    group='stained_glass_pane',
    pattern=['###', '#$#', '###'],
    key={'#': 'minecraft:glass_pane', '$': 'minecraft:gray_dye'},
    result=ItemStackOfComponent(id='minecraft:gray_stained_glass_pane', count=8),
    type='minecraft:crafting_shaped',
)

GRAY_TERRACOTTA = RecipeCraftingShaped(
    group='stained_terracotta',
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:terracotta', 'X': 'minecraft:gray_dye'},
    result=ItemStackOfComponent(id='minecraft:gray_terracotta', count=8),
    type='minecraft:crafting_shaped',
)

GRAY_WOOL_SLAB = RecipeCraftingShaped(
    group='woolen_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:gray_wool'},
    result=ItemStackOfComponent(id='minecraft:gray_wool_slab', count=6),
    type='minecraft:crafting_shaped',
)

GRAY_WOOL_STAIRS = RecipeCraftingShaped(
    group='woolen_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:gray_wool'},
    result=ItemStackOfComponent(id='minecraft:gray_wool_stairs', count=4),
    type='minecraft:crafting_shaped',
)

GREEN_BANNER = RecipeCraftingShaped(
    group='banner',
    pattern=['###', '###', ' | '],
    key={'#': 'minecraft:green_wool', '|': 'minecraft:stick'},
    result=ItemStackOfComponent(id='minecraft:green_banner'),
    type='minecraft:crafting_shaped',
)

GREEN_BANNER_DUPLICATE = RecipeCraftingSpecialBannerduplicate(
    type='minecraft:crafting_special_bannerduplicate',
    **dict[str, Any]({'banner': 'minecraft:green_banner', 'result': {'id': 'minecraft:green_banner'}}),
)

GREEN_BED = RecipeCraftingShaped(
    group='bed',
    pattern=['###', 'XXX'],
    key={'#': 'minecraft:green_wool', 'X': '#minecraft:planks'},
    result=ItemStackOfComponent(id='minecraft:green_bed'),
    type='minecraft:crafting_shaped',
)

GREEN_BUNDLE = RecipeCraftingTransmute(
    group='bundle_dye',
    category=CraftingBookCategory.EQUIPMENT,
    input='#minecraft:bundles',
    material='minecraft:green_dye',
    result=TransmuteResult(id='minecraft:green_bundle'),
    type='minecraft:crafting_transmute',
)

GREEN_CANDLE = RecipeCraftingShapeless(
    group='dyed_candle',
    ingredients=['minecraft:candle', 'minecraft:green_dye'],
    result=ItemStackOfComponent(id='minecraft:green_candle'),
    type='minecraft:crafting_shapeless',
)

GREEN_CARPET = RecipeCraftingShaped(
    group='woolen_carpet',
    pattern=['##'],
    key={'#': 'minecraft:green_wool'},
    result=ItemStackOfComponent(id='minecraft:green_carpet', count=3),
    type='minecraft:crafting_shaped',
)

GREEN_CONCRETE_POWDER = RecipeCraftingShapeless(
    group='concrete_powder',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:green_dye',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:gravel',
        'minecraft:gravel',
        'minecraft:gravel',
        'minecraft:gravel',
    ],
    result=ItemStackOfComponent(id='minecraft:green_concrete_powder', count=8),
    type='minecraft:crafting_shapeless',
)

GREEN_CONCRETE_SLAB = RecipeCraftingShaped(
    group='concrete_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:green_concrete'},
    result=ItemStackOfComponent(id='minecraft:green_concrete_slab', count=6),
    type='minecraft:crafting_shaped',
)

GREEN_CONCRETE_SLAB_FROM_GREEN_CONCRETE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:green_concrete',
    result=ItemStackOfComponent(id='minecraft:green_concrete_slab', count=2),
    type='minecraft:stonecutting',
)

GREEN_CONCRETE_STAIRS = RecipeCraftingShaped(
    group='concrete_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:green_concrete'},
    result=ItemStackOfComponent(id='minecraft:green_concrete_stairs', count=4),
    type='minecraft:crafting_shaped',
)

GREEN_CONCRETE_STAIRS_FROM_GREEN_CONCRETE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:green_concrete',
    result=ItemStackOfComponent(id='minecraft:green_concrete_stairs'),
    type='minecraft:stonecutting',
)

GREEN_CUSHION = RecipeCraftingShaped(
    group='cushion',
    pattern=['###'],
    key={'#': 'minecraft:green_wool_slab'},
    result=ItemStackOfComponent(id='minecraft:green_cushion'),
    type='minecraft:crafting_shaped',
)

GREEN_DYE = RecipeSmelting(
    ingredient='minecraft:cactus',
    result=ItemStackOfComponent(id='minecraft:green_dye'),
    experience=1.0,
    cookingtime=200,
    type='minecraft:smelting',
)

GREEN_GLAZED_TERRACOTTA = RecipeSmelting(
    category=CookingBookCategory.BLOCKS,
    ingredient='minecraft:green_terracotta',
    result=ItemStackOfComponent(id='minecraft:green_glazed_terracotta'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

GREEN_HARNESS = RecipeCraftingShaped(
    group='harness',
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['LLL', 'G#G'],
    key={'#': 'minecraft:green_wool', 'G': 'minecraft:glass', 'L': 'minecraft:leather'},
    result=ItemStackOfComponent(id='minecraft:green_harness'),
    type='minecraft:crafting_shaped',
)

GREEN_SHULKER_BOX = RecipeCraftingTransmute(
    group='shulker_box_dye',
    input='#minecraft:shulker_boxes',
    material='minecraft:green_dye',
    result=TransmuteResult(id='minecraft:green_shulker_box'),
    type='minecraft:crafting_transmute',
)

GREEN_STAINED_GLASS = RecipeCraftingShaped(
    group='stained_glass',
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:glass', 'X': 'minecraft:green_dye'},
    result=ItemStackOfComponent(id='minecraft:green_stained_glass', count=8),
    type='minecraft:crafting_shaped',
)

GREEN_STAINED_GLASS_PANE = RecipeCraftingShaped(
    group='stained_glass_pane',
    pattern=['###', '###'],
    key={'#': 'minecraft:green_stained_glass'},
    result=ItemStackOfComponent(id='minecraft:green_stained_glass_pane', count=16),
    type='minecraft:crafting_shaped',
)

GREEN_STAINED_GLASS_PANE_FROM_GLASS_PANE = RecipeCraftingShaped(
    group='stained_glass_pane',
    pattern=['###', '#$#', '###'],
    key={'#': 'minecraft:glass_pane', '$': 'minecraft:green_dye'},
    result=ItemStackOfComponent(id='minecraft:green_stained_glass_pane', count=8),
    type='minecraft:crafting_shaped',
)

GREEN_TERRACOTTA = RecipeCraftingShaped(
    group='stained_terracotta',
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:terracotta', 'X': 'minecraft:green_dye'},
    result=ItemStackOfComponent(id='minecraft:green_terracotta', count=8),
    type='minecraft:crafting_shaped',
)

GREEN_WOOL_SLAB = RecipeCraftingShaped(
    group='woolen_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:green_wool'},
    result=ItemStackOfComponent(id='minecraft:green_wool_slab', count=6),
    type='minecraft:crafting_shaped',
)

GREEN_WOOL_STAIRS = RecipeCraftingShaped(
    group='woolen_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:green_wool'},
    result=ItemStackOfComponent(id='minecraft:green_wool_stairs', count=4),
    type='minecraft:crafting_shaped',
)

GRINDSTONE = RecipeCraftingShaped(
    pattern=['I-I', '# #'],
    key={'#': '#minecraft:planks', '-': 'minecraft:stone_slab', 'I': 'minecraft:stick'},
    result=ItemStackOfComponent(id='minecraft:grindstone'),
    type='minecraft:crafting_shaped',
)

HAY_BLOCK = RecipeCraftingShapeless(
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:wheat',
        'minecraft:wheat',
        'minecraft:wheat',
        'minecraft:wheat',
        'minecraft:wheat',
        'minecraft:wheat',
        'minecraft:wheat',
        'minecraft:wheat',
        'minecraft:wheat',
    ],
    result=ItemStackOfComponent(id='minecraft:hay_block'),
    type='minecraft:crafting_shapeless',
)

HEAVY_WEIGHTED_PRESSURE_PLATE = RecipeCraftingShaped(
    category=CraftingBookCategory.REDSTONE,
    pattern=['##'],
    key={'#': 'minecraft:iron_ingot'},
    result=ItemStackOfComponent(id='minecraft:heavy_weighted_pressure_plate'),
    type='minecraft:crafting_shaped',
)

HONEYCOMB_BLOCK = RecipeCraftingShaped(
    pattern=['##', '##'],
    key={'#': 'minecraft:honeycomb'},
    result=ItemStackOfComponent(id='minecraft:honeycomb_block'),
    type='minecraft:crafting_shaped',
)

HONEY_BLOCK = RecipeCraftingShaped(
    category=CraftingBookCategory.REDSTONE,
    pattern=['##', '##'],
    key={'#': 'minecraft:honey_bottle'},
    result=ItemStackOfComponent(id='minecraft:honey_block'),
    type='minecraft:crafting_shaped',
)

HONEY_BOTTLE = RecipeCraftingShapeless(
    ingredients=[
        'minecraft:honey_block',
        'minecraft:glass_bottle',
        'minecraft:glass_bottle',
        'minecraft:glass_bottle',
        'minecraft:glass_bottle',
    ],
    result=ItemStackOfComponent(id='minecraft:honey_bottle', count=4),
    type='minecraft:crafting_shapeless',
)

HOPPER = RecipeCraftingShaped(
    category=CraftingBookCategory.REDSTONE,
    pattern=['I I', 'ICI', ' I '],
    key={'C': 'minecraft:chest', 'I': 'minecraft:iron_ingot'},
    result=ItemStackOfComponent(id='minecraft:hopper'),
    type='minecraft:crafting_shaped',
)

HOPPER_MINECART = RecipeCraftingShapeless(
    ingredients=['minecraft:hopper', 'minecraft:minecart'],
    result=ItemStackOfComponent(id='minecraft:hopper_minecart'),
    type='minecraft:crafting_shapeless',
)

HOST_ARMOR_TRIM_SMITHING_TEMPLATE = RecipeCraftingShaped(
    pattern=['#S#', '#C#', '###'],
    key={'#': 'minecraft:diamond', 'C': 'minecraft:terracotta', 'S': 'minecraft:host_armor_trim_smithing_template'},
    result=ItemStackOfComponent(id='minecraft:host_armor_trim_smithing_template', count=2),
    type='minecraft:crafting_shaped',
)

HOST_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = RecipeSmithingTrim(
    base='#minecraft:trimmable_armor',
    addition='#minecraft:trim_materials',
    template='minecraft:host_armor_trim_smithing_template',
    pattern='minecraft:host',
    type='minecraft:smithing_trim',
)

IRON_AXE = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['XX', 'X#', ' #'],
    key={'#': 'minecraft:stick', 'X': '#minecraft:iron_tool_materials'},
    result=ItemStackOfComponent(id='minecraft:iron_axe'),
    type='minecraft:crafting_shaped',
)

IRON_BARS = RecipeCraftingShaped(
    pattern=['###', '###'],
    key={'#': 'minecraft:iron_ingot'},
    result=ItemStackOfComponent(id='minecraft:iron_bars', count=16),
    type='minecraft:crafting_shaped',
)

IRON_BLOCK = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '###', '###'],
    key={'#': 'minecraft:iron_ingot'},
    result=ItemStackOfComponent(id='minecraft:iron_block'),
    type='minecraft:crafting_shaped',
)

IRON_BOOTS = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['X X', 'X X'],
    key={'X': 'minecraft:iron_ingot'},
    result=ItemStackOfComponent(id='minecraft:iron_boots'),
    type='minecraft:crafting_shaped',
)

IRON_CHAIN = RecipeCraftingShaped(
    pattern=['N', 'I', 'N'],
    key={'I': 'minecraft:iron_ingot', 'N': 'minecraft:iron_nugget'},
    result=ItemStackOfComponent(id='minecraft:iron_chain'),
    type='minecraft:crafting_shaped',
)

IRON_CHESTPLATE = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['X X', 'XXX', 'XXX'],
    key={'X': 'minecraft:iron_ingot'},
    result=ItemStackOfComponent(id='minecraft:iron_chestplate'),
    type='minecraft:crafting_shaped',
)

IRON_DOOR = RecipeCraftingShaped(
    category=CraftingBookCategory.REDSTONE,
    pattern=['##', '##', '##'],
    key={'#': 'minecraft:iron_ingot'},
    result=ItemStackOfComponent(id='minecraft:iron_door', count=3),
    type='minecraft:crafting_shaped',
)

IRON_HELMET = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['XXX', 'X X'],
    key={'X': 'minecraft:iron_ingot'},
    result=ItemStackOfComponent(id='minecraft:iron_helmet'),
    type='minecraft:crafting_shaped',
)

IRON_HOE = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['XX', ' #', ' #'],
    key={'#': 'minecraft:stick', 'X': '#minecraft:iron_tool_materials'},
    result=ItemStackOfComponent(id='minecraft:iron_hoe'),
    type='minecraft:crafting_shaped',
)

IRON_INGOT_FROM_BLASTING_DEEPSLATE_IRON_ORE = RecipeBlasting(
    group='iron_ingot',
    ingredient='minecraft:deepslate_iron_ore',
    result=ItemStackOfComponent(id='minecraft:iron_ingot'),
    experience=0.7,
    cookingtime=200,
    type='minecraft:blasting',
)

IRON_INGOT_FROM_BLASTING_IRON_ORE = RecipeBlasting(
    group='iron_ingot',
    ingredient='minecraft:iron_ore',
    result=ItemStackOfComponent(id='minecraft:iron_ingot'),
    experience=0.7,
    cookingtime=200,
    type='minecraft:blasting',
)

IRON_INGOT_FROM_BLASTING_RAW_IRON = RecipeBlasting(
    group='iron_ingot',
    ingredient='minecraft:raw_iron',
    result=ItemStackOfComponent(id='minecraft:iron_ingot'),
    experience=0.7,
    cookingtime=200,
    type='minecraft:blasting',
)

IRON_INGOT_FROM_IRON_BLOCK = RecipeCraftingShapeless(
    group='iron_ingot',
    ingredients=['minecraft:iron_block'],
    result=ItemStackOfComponent(id='minecraft:iron_ingot', count=9),
    type='minecraft:crafting_shapeless',
)

IRON_INGOT_FROM_NUGGETS = RecipeCraftingShaped(
    group='iron_ingot',
    pattern=['###', '###', '###'],
    key={'#': 'minecraft:iron_nugget'},
    result=ItemStackOfComponent(id='minecraft:iron_ingot'),
    type='minecraft:crafting_shaped',
)

IRON_INGOT_FROM_SMELTING_DEEPSLATE_IRON_ORE = RecipeSmelting(
    group='iron_ingot',
    ingredient='minecraft:deepslate_iron_ore',
    result=ItemStackOfComponent(id='minecraft:iron_ingot'),
    experience=0.7,
    cookingtime=200,
    type='minecraft:smelting',
)

IRON_INGOT_FROM_SMELTING_IRON_ORE = RecipeSmelting(
    group='iron_ingot',
    ingredient='minecraft:iron_ore',
    result=ItemStackOfComponent(id='minecraft:iron_ingot'),
    experience=0.7,
    cookingtime=200,
    type='minecraft:smelting',
)

IRON_INGOT_FROM_SMELTING_RAW_IRON = RecipeSmelting(
    group='iron_ingot',
    ingredient='minecraft:raw_iron',
    result=ItemStackOfComponent(id='minecraft:iron_ingot'),
    experience=0.7,
    cookingtime=200,
    type='minecraft:smelting',
)

IRON_LEGGINGS = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['XXX', 'X X', 'X X'],
    key={'X': 'minecraft:iron_ingot'},
    result=ItemStackOfComponent(id='minecraft:iron_leggings'),
    type='minecraft:crafting_shaped',
)

IRON_NUGGET = RecipeCraftingShapeless(
    ingredients=['minecraft:iron_ingot'],
    result=ItemStackOfComponent(id='minecraft:iron_nugget', count=9),
    type='minecraft:crafting_shapeless',
)

IRON_NUGGET_FROM_BLASTING = RecipeBlasting(
    ingredient=[
        'minecraft:iron_pickaxe',
        'minecraft:iron_shovel',
        'minecraft:iron_axe',
        'minecraft:iron_hoe',
        'minecraft:iron_sword',
        'minecraft:iron_spear',
        'minecraft:iron_helmet',
        'minecraft:iron_chestplate',
        'minecraft:iron_leggings',
        'minecraft:iron_boots',
        'minecraft:iron_horse_armor',
        'minecraft:iron_nautilus_armor',
        'minecraft:chainmail_helmet',
        'minecraft:chainmail_chestplate',
        'minecraft:chainmail_leggings',
        'minecraft:chainmail_boots',
    ],
    result=ItemStackOfComponent(id='minecraft:iron_nugget'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:blasting',
)

IRON_NUGGET_FROM_SMELTING = RecipeSmelting(
    ingredient=[
        'minecraft:iron_pickaxe',
        'minecraft:iron_shovel',
        'minecraft:iron_axe',
        'minecraft:iron_hoe',
        'minecraft:iron_sword',
        'minecraft:iron_spear',
        'minecraft:iron_helmet',
        'minecraft:iron_chestplate',
        'minecraft:iron_leggings',
        'minecraft:iron_boots',
        'minecraft:iron_horse_armor',
        'minecraft:chainmail_helmet',
        'minecraft:chainmail_chestplate',
        'minecraft:chainmail_leggings',
        'minecraft:chainmail_boots',
        'minecraft:iron_nautilus_armor',
    ],
    result=ItemStackOfComponent(id='minecraft:iron_nugget'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

IRON_PICKAXE = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['XXX', ' # ', ' # '],
    key={'#': 'minecraft:stick', 'X': '#minecraft:iron_tool_materials'},
    result=ItemStackOfComponent(id='minecraft:iron_pickaxe'),
    type='minecraft:crafting_shaped',
)

IRON_SHOVEL = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['X', '#', '#'],
    key={'#': 'minecraft:stick', 'X': '#minecraft:iron_tool_materials'},
    result=ItemStackOfComponent(id='minecraft:iron_shovel'),
    type='minecraft:crafting_shaped',
)

IRON_SPEAR = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['  X', ' # ', '#  '],
    key={'#': 'minecraft:stick', 'X': '#minecraft:iron_tool_materials'},
    result=ItemStackOfComponent(id='minecraft:iron_spear'),
    type='minecraft:crafting_shaped',
)

IRON_SWORD = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['X', 'X', '#'],
    key={'#': 'minecraft:stick', 'X': '#minecraft:iron_tool_materials'},
    result=ItemStackOfComponent(id='minecraft:iron_sword'),
    type='minecraft:crafting_shaped',
)

IRON_TRAPDOOR = RecipeCraftingShaped(
    category=CraftingBookCategory.REDSTONE,
    pattern=['##', '##'],
    key={'#': 'minecraft:iron_ingot'},
    result=ItemStackOfComponent(id='minecraft:iron_trapdoor'),
    type='minecraft:crafting_shaped',
)

ITEM_FRAME = RecipeCraftingShaped(
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:stick', 'X': 'minecraft:leather'},
    result=ItemStackOfComponent(id='minecraft:item_frame'),
    type='minecraft:crafting_shaped',
)

JACK_O_LANTERN = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['A', 'B'],
    key={'A': 'minecraft:carved_pumpkin', 'B': 'minecraft:torch'},
    result=ItemStackOfComponent(id='minecraft:jack_o_lantern'),
    type='minecraft:crafting_shaped',
)

JUKEBOX = RecipeCraftingShaped(
    pattern=['###', '#X#', '###'],
    key={'#': '#minecraft:planks', 'X': 'minecraft:diamond'},
    result=ItemStackOfComponent(id='minecraft:jukebox'),
    type='minecraft:crafting_shaped',
)

JUNGLE_BOAT = RecipeCraftingShaped(
    group='boat',
    pattern=['# #', '###'],
    key={'#': 'minecraft:jungle_planks'},
    result=ItemStackOfComponent(id='minecraft:jungle_boat'),
    type='minecraft:crafting_shaped',
)

JUNGLE_BUTTON = RecipeCraftingShapeless(
    group='wooden_button',
    category=CraftingBookCategory.REDSTONE,
    ingredients=['minecraft:jungle_planks'],
    result=ItemStackOfComponent(id='minecraft:jungle_button'),
    type='minecraft:crafting_shapeless',
)

JUNGLE_CHEST_BOAT = RecipeCraftingShapeless(
    group='chest_boat',
    ingredients=['minecraft:chest', 'minecraft:jungle_boat'],
    result=ItemStackOfComponent(id='minecraft:jungle_chest_boat'),
    type='minecraft:crafting_shapeless',
)

JUNGLE_DOOR = RecipeCraftingShaped(
    group='wooden_door',
    category=CraftingBookCategory.REDSTONE,
    pattern=['##', '##', '##'],
    key={'#': 'minecraft:jungle_planks'},
    result=ItemStackOfComponent(id='minecraft:jungle_door', count=3),
    type='minecraft:crafting_shaped',
)

JUNGLE_FENCE = RecipeCraftingShaped(
    group='wooden_fence',
    pattern=['W#W', 'W#W'],
    key={'#': 'minecraft:stick', 'W': 'minecraft:jungle_planks'},
    result=ItemStackOfComponent(id='minecraft:jungle_fence', count=3),
    type='minecraft:crafting_shaped',
)

JUNGLE_FENCE_GATE = RecipeCraftingShaped(
    group='wooden_fence_gate',
    category=CraftingBookCategory.REDSTONE,
    pattern=['#W#', '#W#'],
    key={'#': 'minecraft:stick', 'W': 'minecraft:jungle_planks'},
    result=ItemStackOfComponent(id='minecraft:jungle_fence_gate'),
    type='minecraft:crafting_shaped',
)

JUNGLE_HANGING_SIGN = RecipeCraftingShaped(
    group='wooden_hanging_sign',
    pattern=['X X', '###', '###'],
    key={'#': 'minecraft:stripped_jungle_log', 'X': 'minecraft:iron_chain'},
    result=ItemStackOfComponent(id='minecraft:jungle_hanging_sign', count=6),
    type='minecraft:crafting_shaped',
)

JUNGLE_PLANKS = RecipeCraftingShapeless(
    group='planks',
    category=CraftingBookCategory.BUILDING,
    ingredients=['#minecraft:jungle_logs'],
    result=ItemStackOfComponent(id='minecraft:jungle_planks', count=4),
    type='minecraft:crafting_shapeless',
)

JUNGLE_PRESSURE_PLATE = RecipeCraftingShaped(
    group='wooden_pressure_plate',
    category=CraftingBookCategory.REDSTONE,
    pattern=['##'],
    key={'#': 'minecraft:jungle_planks'},
    result=ItemStackOfComponent(id='minecraft:jungle_pressure_plate'),
    type='minecraft:crafting_shaped',
)

JUNGLE_SHELF = RecipeCraftingShaped(
    group='shelf',
    pattern=['###', '   ', '###'],
    key={'#': 'minecraft:stripped_jungle_log'},
    result=ItemStackOfComponent(id='minecraft:jungle_shelf', count=6),
    type='minecraft:crafting_shaped',
)

JUNGLE_SIGN = RecipeCraftingShaped(
    group='wooden_sign',
    pattern=['###', '###', ' X '],
    key={'#': 'minecraft:jungle_planks', 'X': 'minecraft:stick'},
    result=ItemStackOfComponent(id='minecraft:jungle_sign', count=3),
    type='minecraft:crafting_shaped',
)

JUNGLE_SLAB = RecipeCraftingShaped(
    group='wooden_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:jungle_planks'},
    result=ItemStackOfComponent(id='minecraft:jungle_slab', count=6),
    type='minecraft:crafting_shaped',
)

JUNGLE_STAIRS = RecipeCraftingShaped(
    group='wooden_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:jungle_planks'},
    result=ItemStackOfComponent(id='minecraft:jungle_stairs', count=4),
    type='minecraft:crafting_shaped',
)

JUNGLE_TRAPDOOR = RecipeCraftingShaped(
    group='wooden_trapdoor',
    category=CraftingBookCategory.REDSTONE,
    pattern=['###', '###'],
    key={'#': 'minecraft:jungle_planks'},
    result=ItemStackOfComponent(id='minecraft:jungle_trapdoor', count=2),
    type='minecraft:crafting_shaped',
)

JUNGLE_WOOD = RecipeCraftingShaped(
    group='bark',
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:jungle_log'},
    result=ItemStackOfComponent(id='minecraft:jungle_wood', count=3),
    type='minecraft:crafting_shaped',
)

LADDER = RecipeCraftingShaped(
    pattern=['# #', '###', '# #'],
    key={'#': 'minecraft:stick'},
    result=ItemStackOfComponent(id='minecraft:ladder', count=3),
    type='minecraft:crafting_shaped',
)

LANTERN = RecipeCraftingShaped(
    pattern=['XXX', 'X#X', 'XXX'],
    key={'#': 'minecraft:torch', 'X': 'minecraft:iron_nugget'},
    result=ItemStackOfComponent(id='minecraft:lantern'),
    type='minecraft:crafting_shaped',
)

LAPIS_BLOCK = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '###', '###'],
    key={'#': 'minecraft:lapis_lazuli'},
    result=ItemStackOfComponent(id='minecraft:lapis_block'),
    type='minecraft:crafting_shaped',
)

LAPIS_LAZULI = RecipeCraftingShapeless(
    ingredients=['minecraft:lapis_block'],
    result=ItemStackOfComponent(id='minecraft:lapis_lazuli', count=9),
    type='minecraft:crafting_shapeless',
)

LAPIS_LAZULI_FROM_BLASTING_DEEPSLATE_LAPIS_ORE = RecipeBlasting(
    group='lapis_lazuli',
    ingredient='minecraft:deepslate_lapis_ore',
    result=ItemStackOfComponent(id='minecraft:lapis_lazuli'),
    experience=0.2,
    cookingtime=200,
    type='minecraft:blasting',
)

LAPIS_LAZULI_FROM_BLASTING_LAPIS_ORE = RecipeBlasting(
    group='lapis_lazuli',
    ingredient='minecraft:lapis_ore',
    result=ItemStackOfComponent(id='minecraft:lapis_lazuli'),
    experience=0.2,
    cookingtime=200,
    type='minecraft:blasting',
)

LAPIS_LAZULI_FROM_SMELTING_DEEPSLATE_LAPIS_ORE = RecipeSmelting(
    group='lapis_lazuli',
    ingredient='minecraft:deepslate_lapis_ore',
    result=ItemStackOfComponent(id='minecraft:lapis_lazuli'),
    experience=0.2,
    cookingtime=200,
    type='minecraft:smelting',
)

LAPIS_LAZULI_FROM_SMELTING_LAPIS_ORE = RecipeSmelting(
    group='lapis_lazuli',
    ingredient='minecraft:lapis_ore',
    result=ItemStackOfComponent(id='minecraft:lapis_lazuli'),
    experience=0.2,
    cookingtime=200,
    type='minecraft:smelting',
)

LEAD = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['~~ ', '~~ ', '  ~'],
    key={'~': 'minecraft:string'},
    result=ItemStackOfComponent(id='minecraft:lead', count=2),
    type='minecraft:crafting_shaped',
)

LEAF_LITTER = RecipeSmelting(
    category=CookingBookCategory.BLOCKS,
    ingredient='#minecraft:leaves',
    result=ItemStackOfComponent(id='minecraft:leaf_litter'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

LEATHER = RecipeCraftingShaped(
    pattern=['##', '##'],
    key={'#': 'minecraft:rabbit_hide'},
    result=ItemStackOfComponent(id='minecraft:leather'),
    type='minecraft:crafting_shaped',
)

LEATHER_BOOTS = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['X X', 'X X'],
    key={'X': 'minecraft:leather'},
    result=ItemStackOfComponent(id='minecraft:leather_boots'),
    type='minecraft:crafting_shaped',
)

LEATHER_BOOTS_DYED = RecipeCraftingDye(
    group='dyed_armor',
    target='minecraft:leather_boots',
    dye='#minecraft:dyes',
    result=ItemStackOfComponent(id='minecraft:leather_boots'),
    type='minecraft:crafting_dye',
)

LEATHER_CHESTPLATE = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['X X', 'XXX', 'XXX'],
    key={'X': 'minecraft:leather'},
    result=ItemStackOfComponent(id='minecraft:leather_chestplate'),
    type='minecraft:crafting_shaped',
)

LEATHER_CHESTPLATE_DYED = RecipeCraftingDye(
    group='dyed_armor',
    target='minecraft:leather_chestplate',
    dye='#minecraft:dyes',
    result=ItemStackOfComponent(id='minecraft:leather_chestplate'),
    type='minecraft:crafting_dye',
)

LEATHER_HELMET = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['XXX', 'X X'],
    key={'X': 'minecraft:leather'},
    result=ItemStackOfComponent(id='minecraft:leather_helmet'),
    type='minecraft:crafting_shaped',
)

LEATHER_HELMET_DYED = RecipeCraftingDye(
    group='dyed_armor',
    target='minecraft:leather_helmet',
    dye='#minecraft:dyes',
    result=ItemStackOfComponent(id='minecraft:leather_helmet'),
    type='minecraft:crafting_dye',
)

LEATHER_HORSE_ARMOR = RecipeCraftingShaped(
    pattern=['X X', 'XXX', 'X X'],
    key={'X': 'minecraft:leather'},
    result=ItemStackOfComponent(id='minecraft:leather_horse_armor'),
    type='minecraft:crafting_shaped',
)

LEATHER_HORSE_ARMOR_DYED = RecipeCraftingDye(
    group='dyed_armor',
    target='minecraft:leather_horse_armor',
    dye='#minecraft:dyes',
    result=ItemStackOfComponent(id='minecraft:leather_horse_armor'),
    type='minecraft:crafting_dye',
)

LEATHER_LEGGINGS = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['XXX', 'X X', 'X X'],
    key={'X': 'minecraft:leather'},
    result=ItemStackOfComponent(id='minecraft:leather_leggings'),
    type='minecraft:crafting_shaped',
)

LEATHER_LEGGINGS_DYED = RecipeCraftingDye(
    group='dyed_armor',
    target='minecraft:leather_leggings',
    dye='#minecraft:dyes',
    result=ItemStackOfComponent(id='minecraft:leather_leggings'),
    type='minecraft:crafting_dye',
)

LECTERN = RecipeCraftingShaped(
    category=CraftingBookCategory.REDSTONE,
    pattern=['SSS', ' B ', ' S '],
    key={'B': 'minecraft:bookshelf', 'S': '#minecraft:wooden_slabs'},
    result=ItemStackOfComponent(id='minecraft:lectern'),
    type='minecraft:crafting_shaped',
)

LEVER = RecipeCraftingShaped(
    category=CraftingBookCategory.REDSTONE,
    pattern=['X', '#'],
    key={'#': 'minecraft:cobblestone', 'X': 'minecraft:stick'},
    result=ItemStackOfComponent(id='minecraft:lever'),
    type='minecraft:crafting_shaped',
)

LIGHTNING_ROD = RecipeCraftingShaped(
    category=CraftingBookCategory.REDSTONE,
    pattern=['#', '#', '#'],
    key={'#': 'minecraft:copper_ingot'},
    result=ItemStackOfComponent(id='minecraft:lightning_rod'),
    type='minecraft:crafting_shaped',
)

LIGHT_BLUE_BANNER = RecipeCraftingShaped(
    group='banner',
    pattern=['###', '###', ' | '],
    key={'#': 'minecraft:light_blue_wool', '|': 'minecraft:stick'},
    result=ItemStackOfComponent(id='minecraft:light_blue_banner'),
    type='minecraft:crafting_shaped',
)

LIGHT_BLUE_BANNER_DUPLICATE = RecipeCraftingSpecialBannerduplicate(
    type='minecraft:crafting_special_bannerduplicate',
    **dict[str, Any]({'banner': 'minecraft:light_blue_banner', 'result': {'id': 'minecraft:light_blue_banner'}}),
)

LIGHT_BLUE_BED = RecipeCraftingShaped(
    group='bed',
    pattern=['###', 'XXX'],
    key={'#': 'minecraft:light_blue_wool', 'X': '#minecraft:planks'},
    result=ItemStackOfComponent(id='minecraft:light_blue_bed'),
    type='minecraft:crafting_shaped',
)

LIGHT_BLUE_BUNDLE = RecipeCraftingTransmute(
    group='bundle_dye',
    category=CraftingBookCategory.EQUIPMENT,
    input='#minecraft:bundles',
    material='minecraft:light_blue_dye',
    result=TransmuteResult(id='minecraft:light_blue_bundle'),
    type='minecraft:crafting_transmute',
)

LIGHT_BLUE_CANDLE = RecipeCraftingShapeless(
    group='dyed_candle',
    ingredients=['minecraft:candle', 'minecraft:light_blue_dye'],
    result=ItemStackOfComponent(id='minecraft:light_blue_candle'),
    type='minecraft:crafting_shapeless',
)

LIGHT_BLUE_CARPET = RecipeCraftingShaped(
    group='woolen_carpet',
    pattern=['##'],
    key={'#': 'minecraft:light_blue_wool'},
    result=ItemStackOfComponent(id='minecraft:light_blue_carpet', count=3),
    type='minecraft:crafting_shaped',
)

LIGHT_BLUE_CONCRETE_POWDER = RecipeCraftingShapeless(
    group='concrete_powder',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:light_blue_dye',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:gravel',
        'minecraft:gravel',
        'minecraft:gravel',
        'minecraft:gravel',
    ],
    result=ItemStackOfComponent(id='minecraft:light_blue_concrete_powder', count=8),
    type='minecraft:crafting_shapeless',
)

LIGHT_BLUE_CONCRETE_SLAB = RecipeCraftingShaped(
    group='concrete_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:light_blue_concrete'},
    result=ItemStackOfComponent(id='minecraft:light_blue_concrete_slab', count=6),
    type='minecraft:crafting_shaped',
)

LIGHT_BLUE_CONCRETE_SLAB_FROM_LIGHT_BLUE_CONCRETE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:light_blue_concrete',
    result=ItemStackOfComponent(id='minecraft:light_blue_concrete_slab', count=2),
    type='minecraft:stonecutting',
)

LIGHT_BLUE_CONCRETE_STAIRS = RecipeCraftingShaped(
    group='concrete_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:light_blue_concrete'},
    result=ItemStackOfComponent(id='minecraft:light_blue_concrete_stairs', count=4),
    type='minecraft:crafting_shaped',
)

LIGHT_BLUE_CONCRETE_STAIRS_FROM_LIGHT_BLUE_CONCRETE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:light_blue_concrete',
    result=ItemStackOfComponent(id='minecraft:light_blue_concrete_stairs'),
    type='minecraft:stonecutting',
)

LIGHT_BLUE_CUSHION = RecipeCraftingShaped(
    group='cushion',
    pattern=['###'],
    key={'#': 'minecraft:light_blue_wool_slab'},
    result=ItemStackOfComponent(id='minecraft:light_blue_cushion'),
    type='minecraft:crafting_shaped',
)

LIGHT_BLUE_DYE_FROM_BLUE_ORCHID = RecipeCraftingShapeless(
    group='light_blue_dye',
    ingredients=['minecraft:blue_orchid'],
    result=ItemStackOfComponent(id='minecraft:light_blue_dye'),
    type='minecraft:crafting_shapeless',
)

LIGHT_BLUE_DYE_FROM_BLUE_WHITE_DYE = RecipeCraftingShapeless(
    group='light_blue_dye',
    ingredients=['minecraft:blue_dye', 'minecraft:white_dye'],
    result=ItemStackOfComponent(id='minecraft:light_blue_dye', count=2),
    type='minecraft:crafting_shapeless',
)

LIGHT_BLUE_GLAZED_TERRACOTTA = RecipeSmelting(
    category=CookingBookCategory.BLOCKS,
    ingredient='minecraft:light_blue_terracotta',
    result=ItemStackOfComponent(id='minecraft:light_blue_glazed_terracotta'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

LIGHT_BLUE_HARNESS = RecipeCraftingShaped(
    group='harness',
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['LLL', 'G#G'],
    key={'#': 'minecraft:light_blue_wool', 'G': 'minecraft:glass', 'L': 'minecraft:leather'},
    result=ItemStackOfComponent(id='minecraft:light_blue_harness'),
    type='minecraft:crafting_shaped',
)

LIGHT_BLUE_SHULKER_BOX = RecipeCraftingTransmute(
    group='shulker_box_dye',
    input='#minecraft:shulker_boxes',
    material='minecraft:light_blue_dye',
    result=TransmuteResult(id='minecraft:light_blue_shulker_box'),
    type='minecraft:crafting_transmute',
)

LIGHT_BLUE_STAINED_GLASS = RecipeCraftingShaped(
    group='stained_glass',
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:glass', 'X': 'minecraft:light_blue_dye'},
    result=ItemStackOfComponent(id='minecraft:light_blue_stained_glass', count=8),
    type='minecraft:crafting_shaped',
)

LIGHT_BLUE_STAINED_GLASS_PANE = RecipeCraftingShaped(
    group='stained_glass_pane',
    pattern=['###', '###'],
    key={'#': 'minecraft:light_blue_stained_glass'},
    result=ItemStackOfComponent(id='minecraft:light_blue_stained_glass_pane', count=16),
    type='minecraft:crafting_shaped',
)

LIGHT_BLUE_STAINED_GLASS_PANE_FROM_GLASS_PANE = RecipeCraftingShaped(
    group='stained_glass_pane',
    pattern=['###', '#$#', '###'],
    key={'#': 'minecraft:glass_pane', '$': 'minecraft:light_blue_dye'},
    result=ItemStackOfComponent(id='minecraft:light_blue_stained_glass_pane', count=8),
    type='minecraft:crafting_shaped',
)

LIGHT_BLUE_TERRACOTTA = RecipeCraftingShaped(
    group='stained_terracotta',
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:terracotta', 'X': 'minecraft:light_blue_dye'},
    result=ItemStackOfComponent(id='minecraft:light_blue_terracotta', count=8),
    type='minecraft:crafting_shaped',
)

LIGHT_BLUE_WOOL_SLAB = RecipeCraftingShaped(
    group='woolen_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:light_blue_wool'},
    result=ItemStackOfComponent(id='minecraft:light_blue_wool_slab', count=6),
    type='minecraft:crafting_shaped',
)

LIGHT_BLUE_WOOL_STAIRS = RecipeCraftingShaped(
    group='woolen_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:light_blue_wool'},
    result=ItemStackOfComponent(id='minecraft:light_blue_wool_stairs', count=4),
    type='minecraft:crafting_shaped',
)

LIGHT_GRAY_BANNER = RecipeCraftingShaped(
    group='banner',
    pattern=['###', '###', ' | '],
    key={'#': 'minecraft:light_gray_wool', '|': 'minecraft:stick'},
    result=ItemStackOfComponent(id='minecraft:light_gray_banner'),
    type='minecraft:crafting_shaped',
)

LIGHT_GRAY_BANNER_DUPLICATE = RecipeCraftingSpecialBannerduplicate(
    type='minecraft:crafting_special_bannerduplicate',
    **dict[str, Any]({'banner': 'minecraft:light_gray_banner', 'result': {'id': 'minecraft:light_gray_banner'}}),
)

LIGHT_GRAY_BED = RecipeCraftingShaped(
    group='bed',
    pattern=['###', 'XXX'],
    key={'#': 'minecraft:light_gray_wool', 'X': '#minecraft:planks'},
    result=ItemStackOfComponent(id='minecraft:light_gray_bed'),
    type='minecraft:crafting_shaped',
)

LIGHT_GRAY_BUNDLE = RecipeCraftingTransmute(
    group='bundle_dye',
    category=CraftingBookCategory.EQUIPMENT,
    input='#minecraft:bundles',
    material='minecraft:light_gray_dye',
    result=TransmuteResult(id='minecraft:light_gray_bundle'),
    type='minecraft:crafting_transmute',
)

LIGHT_GRAY_CANDLE = RecipeCraftingShapeless(
    group='dyed_candle',
    ingredients=['minecraft:candle', 'minecraft:light_gray_dye'],
    result=ItemStackOfComponent(id='minecraft:light_gray_candle'),
    type='minecraft:crafting_shapeless',
)

LIGHT_GRAY_CARPET = RecipeCraftingShaped(
    group='woolen_carpet',
    pattern=['##'],
    key={'#': 'minecraft:light_gray_wool'},
    result=ItemStackOfComponent(id='minecraft:light_gray_carpet', count=3),
    type='minecraft:crafting_shaped',
)

LIGHT_GRAY_CONCRETE_POWDER = RecipeCraftingShapeless(
    group='concrete_powder',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:light_gray_dye',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:gravel',
        'minecraft:gravel',
        'minecraft:gravel',
        'minecraft:gravel',
    ],
    result=ItemStackOfComponent(id='minecraft:light_gray_concrete_powder', count=8),
    type='minecraft:crafting_shapeless',
)

LIGHT_GRAY_CONCRETE_SLAB = RecipeCraftingShaped(
    group='concrete_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:light_gray_concrete'},
    result=ItemStackOfComponent(id='minecraft:light_gray_concrete_slab', count=6),
    type='minecraft:crafting_shaped',
)

LIGHT_GRAY_CONCRETE_SLAB_FROM_LIGHT_GRAY_CONCRETE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:light_gray_concrete',
    result=ItemStackOfComponent(id='minecraft:light_gray_concrete_slab', count=2),
    type='minecraft:stonecutting',
)

LIGHT_GRAY_CONCRETE_STAIRS = RecipeCraftingShaped(
    group='concrete_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:light_gray_concrete'},
    result=ItemStackOfComponent(id='minecraft:light_gray_concrete_stairs', count=4),
    type='minecraft:crafting_shaped',
)

LIGHT_GRAY_CONCRETE_STAIRS_FROM_LIGHT_GRAY_CONCRETE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:light_gray_concrete',
    result=ItemStackOfComponent(id='minecraft:light_gray_concrete_stairs'),
    type='minecraft:stonecutting',
)

LIGHT_GRAY_CUSHION = RecipeCraftingShaped(
    group='cushion',
    pattern=['###'],
    key={'#': 'minecraft:light_gray_wool_slab'},
    result=ItemStackOfComponent(id='minecraft:light_gray_cushion'),
    type='minecraft:crafting_shaped',
)

LIGHT_GRAY_DYE_FROM_AZURE_BLUET = RecipeCraftingShapeless(
    group='light_gray_dye',
    ingredients=['minecraft:azure_bluet'],
    result=ItemStackOfComponent(id='minecraft:light_gray_dye'),
    type='minecraft:crafting_shapeless',
)

LIGHT_GRAY_DYE_FROM_BLACK_WHITE_DYE = RecipeCraftingShapeless(
    group='light_gray_dye',
    ingredients=['minecraft:black_dye', 'minecraft:white_dye', 'minecraft:white_dye'],
    result=ItemStackOfComponent(id='minecraft:light_gray_dye', count=3),
    type='minecraft:crafting_shapeless',
)

LIGHT_GRAY_DYE_FROM_GRAY_WHITE_DYE = RecipeCraftingShapeless(
    group='light_gray_dye',
    ingredients=['minecraft:gray_dye', 'minecraft:white_dye'],
    result=ItemStackOfComponent(id='minecraft:light_gray_dye', count=2),
    type='minecraft:crafting_shapeless',
)

LIGHT_GRAY_DYE_FROM_OXEYE_DAISY = RecipeCraftingShapeless(
    group='light_gray_dye',
    ingredients=['minecraft:oxeye_daisy'],
    result=ItemStackOfComponent(id='minecraft:light_gray_dye'),
    type='minecraft:crafting_shapeless',
)

LIGHT_GRAY_DYE_FROM_WHITE_TULIP = RecipeCraftingShapeless(
    group='light_gray_dye',
    ingredients=['minecraft:white_tulip'],
    result=ItemStackOfComponent(id='minecraft:light_gray_dye'),
    type='minecraft:crafting_shapeless',
)

LIGHT_GRAY_GLAZED_TERRACOTTA = RecipeSmelting(
    category=CookingBookCategory.BLOCKS,
    ingredient='minecraft:light_gray_terracotta',
    result=ItemStackOfComponent(id='minecraft:light_gray_glazed_terracotta'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

LIGHT_GRAY_HARNESS = RecipeCraftingShaped(
    group='harness',
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['LLL', 'G#G'],
    key={'#': 'minecraft:light_gray_wool', 'G': 'minecraft:glass', 'L': 'minecraft:leather'},
    result=ItemStackOfComponent(id='minecraft:light_gray_harness'),
    type='minecraft:crafting_shaped',
)

LIGHT_GRAY_SHULKER_BOX = RecipeCraftingTransmute(
    group='shulker_box_dye',
    input='#minecraft:shulker_boxes',
    material='minecraft:light_gray_dye',
    result=TransmuteResult(id='minecraft:light_gray_shulker_box'),
    type='minecraft:crafting_transmute',
)

LIGHT_GRAY_STAINED_GLASS = RecipeCraftingShaped(
    group='stained_glass',
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:glass', 'X': 'minecraft:light_gray_dye'},
    result=ItemStackOfComponent(id='minecraft:light_gray_stained_glass', count=8),
    type='minecraft:crafting_shaped',
)

LIGHT_GRAY_STAINED_GLASS_PANE = RecipeCraftingShaped(
    group='stained_glass_pane',
    pattern=['###', '###'],
    key={'#': 'minecraft:light_gray_stained_glass'},
    result=ItemStackOfComponent(id='minecraft:light_gray_stained_glass_pane', count=16),
    type='minecraft:crafting_shaped',
)

LIGHT_GRAY_STAINED_GLASS_PANE_FROM_GLASS_PANE = RecipeCraftingShaped(
    group='stained_glass_pane',
    pattern=['###', '#$#', '###'],
    key={'#': 'minecraft:glass_pane', '$': 'minecraft:light_gray_dye'},
    result=ItemStackOfComponent(id='minecraft:light_gray_stained_glass_pane', count=8),
    type='minecraft:crafting_shaped',
)

LIGHT_GRAY_TERRACOTTA = RecipeCraftingShaped(
    group='stained_terracotta',
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:terracotta', 'X': 'minecraft:light_gray_dye'},
    result=ItemStackOfComponent(id='minecraft:light_gray_terracotta', count=8),
    type='minecraft:crafting_shaped',
)

LIGHT_GRAY_WOOL_SLAB = RecipeCraftingShaped(
    group='woolen_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:light_gray_wool'},
    result=ItemStackOfComponent(id='minecraft:light_gray_wool_slab', count=6),
    type='minecraft:crafting_shaped',
)

LIGHT_GRAY_WOOL_STAIRS = RecipeCraftingShaped(
    group='woolen_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:light_gray_wool'},
    result=ItemStackOfComponent(id='minecraft:light_gray_wool_stairs', count=4),
    type='minecraft:crafting_shaped',
)

LIGHT_WEIGHTED_PRESSURE_PLATE = RecipeCraftingShaped(
    category=CraftingBookCategory.REDSTONE,
    pattern=['##'],
    key={'#': 'minecraft:gold_ingot'},
    result=ItemStackOfComponent(id='minecraft:light_weighted_pressure_plate'),
    type='minecraft:crafting_shaped',
)

LIME_BANNER = RecipeCraftingShaped(
    group='banner',
    pattern=['###', '###', ' | '],
    key={'#': 'minecraft:lime_wool', '|': 'minecraft:stick'},
    result=ItemStackOfComponent(id='minecraft:lime_banner'),
    type='minecraft:crafting_shaped',
)

LIME_BANNER_DUPLICATE = RecipeCraftingSpecialBannerduplicate(
    type='minecraft:crafting_special_bannerduplicate',
    **dict[str, Any]({'banner': 'minecraft:lime_banner', 'result': {'id': 'minecraft:lime_banner'}}),
)

LIME_BED = RecipeCraftingShaped(
    group='bed',
    pattern=['###', 'XXX'],
    key={'#': 'minecraft:lime_wool', 'X': '#minecraft:planks'},
    result=ItemStackOfComponent(id='minecraft:lime_bed'),
    type='minecraft:crafting_shaped',
)

LIME_BUNDLE = RecipeCraftingTransmute(
    group='bundle_dye',
    category=CraftingBookCategory.EQUIPMENT,
    input='#minecraft:bundles',
    material='minecraft:lime_dye',
    result=TransmuteResult(id='minecraft:lime_bundle'),
    type='minecraft:crafting_transmute',
)

LIME_CANDLE = RecipeCraftingShapeless(
    group='dyed_candle',
    ingredients=['minecraft:candle', 'minecraft:lime_dye'],
    result=ItemStackOfComponent(id='minecraft:lime_candle'),
    type='minecraft:crafting_shapeless',
)

LIME_CARPET = RecipeCraftingShaped(
    group='woolen_carpet',
    pattern=['##'],
    key={'#': 'minecraft:lime_wool'},
    result=ItemStackOfComponent(id='minecraft:lime_carpet', count=3),
    type='minecraft:crafting_shaped',
)

LIME_CONCRETE_POWDER = RecipeCraftingShapeless(
    group='concrete_powder',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:lime_dye',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:gravel',
        'minecraft:gravel',
        'minecraft:gravel',
        'minecraft:gravel',
    ],
    result=ItemStackOfComponent(id='minecraft:lime_concrete_powder', count=8),
    type='minecraft:crafting_shapeless',
)

LIME_CONCRETE_SLAB = RecipeCraftingShaped(
    group='concrete_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:lime_concrete'},
    result=ItemStackOfComponent(id='minecraft:lime_concrete_slab', count=6),
    type='minecraft:crafting_shaped',
)

LIME_CONCRETE_SLAB_FROM_LIME_CONCRETE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:lime_concrete',
    result=ItemStackOfComponent(id='minecraft:lime_concrete_slab', count=2),
    type='minecraft:stonecutting',
)

LIME_CONCRETE_STAIRS = RecipeCraftingShaped(
    group='concrete_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:lime_concrete'},
    result=ItemStackOfComponent(id='minecraft:lime_concrete_stairs', count=4),
    type='minecraft:crafting_shaped',
)

LIME_CONCRETE_STAIRS_FROM_LIME_CONCRETE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:lime_concrete',
    result=ItemStackOfComponent(id='minecraft:lime_concrete_stairs'),
    type='minecraft:stonecutting',
)

LIME_CUSHION = RecipeCraftingShaped(
    group='cushion',
    pattern=['###'],
    key={'#': 'minecraft:lime_wool_slab'},
    result=ItemStackOfComponent(id='minecraft:lime_cushion'),
    type='minecraft:crafting_shaped',
)

LIME_DYE = RecipeCraftingShapeless(
    ingredients=['minecraft:green_dye', 'minecraft:white_dye'],
    result=ItemStackOfComponent(id='minecraft:lime_dye', count=2),
    type='minecraft:crafting_shapeless',
)

LIME_DYE_FROM_SMELTING = RecipeSmelting(
    ingredient='minecraft:sea_pickle',
    result=ItemStackOfComponent(id='minecraft:lime_dye'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

LIME_GLAZED_TERRACOTTA = RecipeSmelting(
    category=CookingBookCategory.BLOCKS,
    ingredient='minecraft:lime_terracotta',
    result=ItemStackOfComponent(id='minecraft:lime_glazed_terracotta'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

LIME_HARNESS = RecipeCraftingShaped(
    group='harness',
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['LLL', 'G#G'],
    key={'#': 'minecraft:lime_wool', 'G': 'minecraft:glass', 'L': 'minecraft:leather'},
    result=ItemStackOfComponent(id='minecraft:lime_harness'),
    type='minecraft:crafting_shaped',
)

LIME_SHULKER_BOX = RecipeCraftingTransmute(
    group='shulker_box_dye',
    input='#minecraft:shulker_boxes',
    material='minecraft:lime_dye',
    result=TransmuteResult(id='minecraft:lime_shulker_box'),
    type='minecraft:crafting_transmute',
)

LIME_STAINED_GLASS = RecipeCraftingShaped(
    group='stained_glass',
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:glass', 'X': 'minecraft:lime_dye'},
    result=ItemStackOfComponent(id='minecraft:lime_stained_glass', count=8),
    type='minecraft:crafting_shaped',
)

LIME_STAINED_GLASS_PANE = RecipeCraftingShaped(
    group='stained_glass_pane',
    pattern=['###', '###'],
    key={'#': 'minecraft:lime_stained_glass'},
    result=ItemStackOfComponent(id='minecraft:lime_stained_glass_pane', count=16),
    type='minecraft:crafting_shaped',
)

LIME_STAINED_GLASS_PANE_FROM_GLASS_PANE = RecipeCraftingShaped(
    group='stained_glass_pane',
    pattern=['###', '#$#', '###'],
    key={'#': 'minecraft:glass_pane', '$': 'minecraft:lime_dye'},
    result=ItemStackOfComponent(id='minecraft:lime_stained_glass_pane', count=8),
    type='minecraft:crafting_shaped',
)

LIME_TERRACOTTA = RecipeCraftingShaped(
    group='stained_terracotta',
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:terracotta', 'X': 'minecraft:lime_dye'},
    result=ItemStackOfComponent(id='minecraft:lime_terracotta', count=8),
    type='minecraft:crafting_shaped',
)

LIME_WOOL_SLAB = RecipeCraftingShaped(
    group='woolen_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:lime_wool'},
    result=ItemStackOfComponent(id='minecraft:lime_wool_slab', count=6),
    type='minecraft:crafting_shaped',
)

LIME_WOOL_STAIRS = RecipeCraftingShaped(
    group='woolen_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:lime_wool'},
    result=ItemStackOfComponent(id='minecraft:lime_wool_stairs', count=4),
    type='minecraft:crafting_shaped',
)

LODESTONE = RecipeCraftingShaped(
    pattern=['SSS', 'S#S', 'SSS'],
    key={'#': 'minecraft:iron_ingot', 'S': 'minecraft:chiseled_stone_bricks'},
    result=ItemStackOfComponent(id='minecraft:lodestone'),
    type='minecraft:crafting_shaped',
)

LOOM = RecipeCraftingShaped(
    pattern=['@@', '##'],
    key={'#': '#minecraft:planks', '@': 'minecraft:string'},
    result=ItemStackOfComponent(id='minecraft:loom'),
    type='minecraft:crafting_shaped',
)

MACE = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=[' # ', ' I '],
    key={'#': 'minecraft:heavy_core', 'I': 'minecraft:breeze_rod'},
    result=ItemStackOfComponent(id='minecraft:mace'),
    type='minecraft:crafting_shaped',
)

MAGENTA_BANNER = RecipeCraftingShaped(
    group='banner',
    pattern=['###', '###', ' | '],
    key={'#': 'minecraft:magenta_wool', '|': 'minecraft:stick'},
    result=ItemStackOfComponent(id='minecraft:magenta_banner'),
    type='minecraft:crafting_shaped',
)

MAGENTA_BANNER_DUPLICATE = RecipeCraftingSpecialBannerduplicate(
    type='minecraft:crafting_special_bannerduplicate',
    **dict[str, Any]({'banner': 'minecraft:magenta_banner', 'result': {'id': 'minecraft:magenta_banner'}}),
)

MAGENTA_BED = RecipeCraftingShaped(
    group='bed',
    pattern=['###', 'XXX'],
    key={'#': 'minecraft:magenta_wool', 'X': '#minecraft:planks'},
    result=ItemStackOfComponent(id='minecraft:magenta_bed'),
    type='minecraft:crafting_shaped',
)

MAGENTA_BUNDLE = RecipeCraftingTransmute(
    group='bundle_dye',
    category=CraftingBookCategory.EQUIPMENT,
    input='#minecraft:bundles',
    material='minecraft:magenta_dye',
    result=TransmuteResult(id='minecraft:magenta_bundle'),
    type='minecraft:crafting_transmute',
)

MAGENTA_CANDLE = RecipeCraftingShapeless(
    group='dyed_candle',
    ingredients=['minecraft:candle', 'minecraft:magenta_dye'],
    result=ItemStackOfComponent(id='minecraft:magenta_candle'),
    type='minecraft:crafting_shapeless',
)

MAGENTA_CARPET = RecipeCraftingShaped(
    group='woolen_carpet',
    pattern=['##'],
    key={'#': 'minecraft:magenta_wool'},
    result=ItemStackOfComponent(id='minecraft:magenta_carpet', count=3),
    type='minecraft:crafting_shaped',
)

MAGENTA_CONCRETE_POWDER = RecipeCraftingShapeless(
    group='concrete_powder',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:magenta_dye',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:gravel',
        'minecraft:gravel',
        'minecraft:gravel',
        'minecraft:gravel',
    ],
    result=ItemStackOfComponent(id='minecraft:magenta_concrete_powder', count=8),
    type='minecraft:crafting_shapeless',
)

MAGENTA_CONCRETE_SLAB = RecipeCraftingShaped(
    group='concrete_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:magenta_concrete'},
    result=ItemStackOfComponent(id='minecraft:magenta_concrete_slab', count=6),
    type='minecraft:crafting_shaped',
)

MAGENTA_CONCRETE_SLAB_FROM_MAGENTA_CONCRETE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:magenta_concrete',
    result=ItemStackOfComponent(id='minecraft:magenta_concrete_slab', count=2),
    type='minecraft:stonecutting',
)

MAGENTA_CONCRETE_STAIRS = RecipeCraftingShaped(
    group='concrete_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:magenta_concrete'},
    result=ItemStackOfComponent(id='minecraft:magenta_concrete_stairs', count=4),
    type='minecraft:crafting_shaped',
)

MAGENTA_CONCRETE_STAIRS_FROM_MAGENTA_CONCRETE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:magenta_concrete',
    result=ItemStackOfComponent(id='minecraft:magenta_concrete_stairs'),
    type='minecraft:stonecutting',
)

MAGENTA_CUSHION = RecipeCraftingShaped(
    group='cushion',
    pattern=['###'],
    key={'#': 'minecraft:magenta_wool_slab'},
    result=ItemStackOfComponent(id='minecraft:magenta_cushion'),
    type='minecraft:crafting_shaped',
)

MAGENTA_DYE_FROM_ALLIUM = RecipeCraftingShapeless(
    group='magenta_dye',
    ingredients=['minecraft:allium'],
    result=ItemStackOfComponent(id='minecraft:magenta_dye'),
    type='minecraft:crafting_shapeless',
)

MAGENTA_DYE_FROM_BLUE_RED_PINK = RecipeCraftingShapeless(
    group='magenta_dye',
    ingredients=['minecraft:blue_dye', 'minecraft:red_dye', 'minecraft:pink_dye'],
    result=ItemStackOfComponent(id='minecraft:magenta_dye', count=3),
    type='minecraft:crafting_shapeless',
)

MAGENTA_DYE_FROM_BLUE_RED_WHITE_DYE = RecipeCraftingShapeless(
    group='magenta_dye',
    ingredients=['minecraft:blue_dye', 'minecraft:red_dye', 'minecraft:red_dye', 'minecraft:white_dye'],
    result=ItemStackOfComponent(id='minecraft:magenta_dye', count=4),
    type='minecraft:crafting_shapeless',
)

MAGENTA_DYE_FROM_LILAC = RecipeCraftingShapeless(
    group='magenta_dye',
    ingredients=['minecraft:lilac'],
    result=ItemStackOfComponent(id='minecraft:magenta_dye', count=2),
    type='minecraft:crafting_shapeless',
)

MAGENTA_DYE_FROM_PURPLE_AND_PINK = RecipeCraftingShapeless(
    group='magenta_dye',
    ingredients=['minecraft:purple_dye', 'minecraft:pink_dye'],
    result=ItemStackOfComponent(id='minecraft:magenta_dye', count=2),
    type='minecraft:crafting_shapeless',
)

MAGENTA_GLAZED_TERRACOTTA = RecipeSmelting(
    category=CookingBookCategory.BLOCKS,
    ingredient='minecraft:magenta_terracotta',
    result=ItemStackOfComponent(id='minecraft:magenta_glazed_terracotta'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

MAGENTA_HARNESS = RecipeCraftingShaped(
    group='harness',
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['LLL', 'G#G'],
    key={'#': 'minecraft:magenta_wool', 'G': 'minecraft:glass', 'L': 'minecraft:leather'},
    result=ItemStackOfComponent(id='minecraft:magenta_harness'),
    type='minecraft:crafting_shaped',
)

MAGENTA_SHULKER_BOX = RecipeCraftingTransmute(
    group='shulker_box_dye',
    input='#minecraft:shulker_boxes',
    material='minecraft:magenta_dye',
    result=TransmuteResult(id='minecraft:magenta_shulker_box'),
    type='minecraft:crafting_transmute',
)

MAGENTA_STAINED_GLASS = RecipeCraftingShaped(
    group='stained_glass',
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:glass', 'X': 'minecraft:magenta_dye'},
    result=ItemStackOfComponent(id='minecraft:magenta_stained_glass', count=8),
    type='minecraft:crafting_shaped',
)

MAGENTA_STAINED_GLASS_PANE = RecipeCraftingShaped(
    group='stained_glass_pane',
    pattern=['###', '###'],
    key={'#': 'minecraft:magenta_stained_glass'},
    result=ItemStackOfComponent(id='minecraft:magenta_stained_glass_pane', count=16),
    type='minecraft:crafting_shaped',
)

MAGENTA_STAINED_GLASS_PANE_FROM_GLASS_PANE = RecipeCraftingShaped(
    group='stained_glass_pane',
    pattern=['###', '#$#', '###'],
    key={'#': 'minecraft:glass_pane', '$': 'minecraft:magenta_dye'},
    result=ItemStackOfComponent(id='minecraft:magenta_stained_glass_pane', count=8),
    type='minecraft:crafting_shaped',
)

MAGENTA_TERRACOTTA = RecipeCraftingShaped(
    group='stained_terracotta',
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:terracotta', 'X': 'minecraft:magenta_dye'},
    result=ItemStackOfComponent(id='minecraft:magenta_terracotta', count=8),
    type='minecraft:crafting_shaped',
)

MAGENTA_WOOL_SLAB = RecipeCraftingShaped(
    group='woolen_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:magenta_wool'},
    result=ItemStackOfComponent(id='minecraft:magenta_wool_slab', count=6),
    type='minecraft:crafting_shaped',
)

MAGENTA_WOOL_STAIRS = RecipeCraftingShaped(
    group='woolen_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:magenta_wool'},
    result=ItemStackOfComponent(id='minecraft:magenta_wool_stairs', count=4),
    type='minecraft:crafting_shaped',
)

MAGMA_BLOCK = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:magma_cream'},
    result=ItemStackOfComponent(id='minecraft:magma_block'),
    type='minecraft:crafting_shaped',
)

MAGMA_CREAM = RecipeCraftingShapeless(
    ingredients=['minecraft:blaze_powder', 'minecraft:slime_ball'],
    result=ItemStackOfComponent(id='minecraft:magma_cream'),
    type='minecraft:crafting_shapeless',
)

MANGROVE_BOAT = RecipeCraftingShaped(
    group='boat',
    pattern=['# #', '###'],
    key={'#': 'minecraft:mangrove_planks'},
    result=ItemStackOfComponent(id='minecraft:mangrove_boat'),
    type='minecraft:crafting_shaped',
)

MANGROVE_BUTTON = RecipeCraftingShapeless(
    group='wooden_button',
    category=CraftingBookCategory.REDSTONE,
    ingredients=['minecraft:mangrove_planks'],
    result=ItemStackOfComponent(id='minecraft:mangrove_button'),
    type='minecraft:crafting_shapeless',
)

MANGROVE_CHEST_BOAT = RecipeCraftingShapeless(
    group='chest_boat',
    ingredients=['minecraft:chest', 'minecraft:mangrove_boat'],
    result=ItemStackOfComponent(id='minecraft:mangrove_chest_boat'),
    type='minecraft:crafting_shapeless',
)

MANGROVE_DOOR = RecipeCraftingShaped(
    group='wooden_door',
    category=CraftingBookCategory.REDSTONE,
    pattern=['##', '##', '##'],
    key={'#': 'minecraft:mangrove_planks'},
    result=ItemStackOfComponent(id='minecraft:mangrove_door', count=3),
    type='minecraft:crafting_shaped',
)

MANGROVE_FENCE = RecipeCraftingShaped(
    group='wooden_fence',
    pattern=['W#W', 'W#W'],
    key={'#': 'minecraft:stick', 'W': 'minecraft:mangrove_planks'},
    result=ItemStackOfComponent(id='minecraft:mangrove_fence', count=3),
    type='minecraft:crafting_shaped',
)

MANGROVE_FENCE_GATE = RecipeCraftingShaped(
    group='wooden_fence_gate',
    category=CraftingBookCategory.REDSTONE,
    pattern=['#W#', '#W#'],
    key={'#': 'minecraft:stick', 'W': 'minecraft:mangrove_planks'},
    result=ItemStackOfComponent(id='minecraft:mangrove_fence_gate'),
    type='minecraft:crafting_shaped',
)

MANGROVE_HANGING_SIGN = RecipeCraftingShaped(
    group='wooden_hanging_sign',
    pattern=['X X', '###', '###'],
    key={'#': 'minecraft:stripped_mangrove_log', 'X': 'minecraft:iron_chain'},
    result=ItemStackOfComponent(id='minecraft:mangrove_hanging_sign', count=6),
    type='minecraft:crafting_shaped',
)

MANGROVE_PLANKS = RecipeCraftingShapeless(
    group='planks',
    category=CraftingBookCategory.BUILDING,
    ingredients=['#minecraft:mangrove_logs'],
    result=ItemStackOfComponent(id='minecraft:mangrove_planks', count=4),
    type='minecraft:crafting_shapeless',
)

MANGROVE_PRESSURE_PLATE = RecipeCraftingShaped(
    group='wooden_pressure_plate',
    category=CraftingBookCategory.REDSTONE,
    pattern=['##'],
    key={'#': 'minecraft:mangrove_planks'},
    result=ItemStackOfComponent(id='minecraft:mangrove_pressure_plate'),
    type='minecraft:crafting_shaped',
)

MANGROVE_SHELF = RecipeCraftingShaped(
    group='shelf',
    pattern=['###', '   ', '###'],
    key={'#': 'minecraft:stripped_mangrove_log'},
    result=ItemStackOfComponent(id='minecraft:mangrove_shelf', count=6),
    type='minecraft:crafting_shaped',
)

MANGROVE_SIGN = RecipeCraftingShaped(
    group='wooden_sign',
    pattern=['###', '###', ' X '],
    key={'#': 'minecraft:mangrove_planks', 'X': 'minecraft:stick'},
    result=ItemStackOfComponent(id='minecraft:mangrove_sign', count=3),
    type='minecraft:crafting_shaped',
)

MANGROVE_SLAB = RecipeCraftingShaped(
    group='wooden_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:mangrove_planks'},
    result=ItemStackOfComponent(id='minecraft:mangrove_slab', count=6),
    type='minecraft:crafting_shaped',
)

MANGROVE_STAIRS = RecipeCraftingShaped(
    group='wooden_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:mangrove_planks'},
    result=ItemStackOfComponent(id='minecraft:mangrove_stairs', count=4),
    type='minecraft:crafting_shaped',
)

MANGROVE_TRAPDOOR = RecipeCraftingShaped(
    group='wooden_trapdoor',
    category=CraftingBookCategory.REDSTONE,
    pattern=['###', '###'],
    key={'#': 'minecraft:mangrove_planks'},
    result=ItemStackOfComponent(id='minecraft:mangrove_trapdoor', count=2),
    type='minecraft:crafting_shaped',
)

MANGROVE_WOOD = RecipeCraftingShaped(
    group='bark',
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:mangrove_log'},
    result=ItemStackOfComponent(id='minecraft:mangrove_wood', count=3),
    type='minecraft:crafting_shaped',
)

MAP = RecipeCraftingShaped(
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:paper', 'X': 'minecraft:compass'},
    result=ItemStackOfComponent(id='minecraft:map'),
    type='minecraft:crafting_shaped',
)

MAP_CLONING = RecipeCraftingTransmute(
    group='map_cloning',
    input='#minecraft:clonable_maps',
    material='minecraft:map',
    material_count=MinMaxBounds(min=1, max=8),
    add_material_count_to_result=True,
    result=TransmuteResult(),
    type='minecraft:crafting_transmute',
)

MAP_EXTENDING = RecipeCraftingSpecialMapextending(
    type='minecraft:crafting_special_mapextending',
    **dict[str, Any]({'map': '#minecraft:extendable_maps', 'material': 'minecraft:paper', 'result': {}}),
)

MELON = RecipeCraftingShapeless(
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:melon_slice',
        'minecraft:melon_slice',
        'minecraft:melon_slice',
        'minecraft:melon_slice',
        'minecraft:melon_slice',
        'minecraft:melon_slice',
        'minecraft:melon_slice',
        'minecraft:melon_slice',
        'minecraft:melon_slice',
    ],
    result=ItemStackOfComponent(id='minecraft:melon'),
    type='minecraft:crafting_shapeless',
)

MELON_SEEDS = RecipeCraftingShapeless(
    ingredients=['minecraft:melon_slice'],
    result=ItemStackOfComponent(id='minecraft:melon_seeds'),
    type='minecraft:crafting_shapeless',
)

MINECART = RecipeCraftingShaped(
    pattern=['# #', '###'],
    key={'#': 'minecraft:iron_ingot'},
    result=ItemStackOfComponent(id='minecraft:minecart'),
    type='minecraft:crafting_shaped',
)

MOJANG_BANNER_PATTERN = RecipeCraftingShapeless(
    ingredients=['minecraft:paper', 'minecraft:enchanted_golden_apple'],
    result=ItemStackOfComponent(id='minecraft:mojang_banner_pattern'),
    type='minecraft:crafting_shapeless',
)

MOSSY_COBBLESTONE_FROM_MOSS_BLOCK = RecipeCraftingShapeless(
    group='mossy_cobblestone',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:cobblestone', 'minecraft:moss_block'],
    result=ItemStackOfComponent(id='minecraft:mossy_cobblestone'),
    type='minecraft:crafting_shapeless',
)

MOSSY_COBBLESTONE_FROM_VINE = RecipeCraftingShapeless(
    group='mossy_cobblestone',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:cobblestone', 'minecraft:vine'],
    result=ItemStackOfComponent(id='minecraft:mossy_cobblestone'),
    type='minecraft:crafting_shapeless',
)

MOSSY_COBBLESTONE_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:mossy_cobblestone'},
    result=ItemStackOfComponent(id='minecraft:mossy_cobblestone_slab', count=6),
    type='minecraft:crafting_shaped',
)

MOSSY_COBBLESTONE_SLAB_FROM_MOSSY_COBBLESTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:mossy_cobblestone',
    result=ItemStackOfComponent(id='minecraft:mossy_cobblestone_slab', count=2),
    type='minecraft:stonecutting',
)

MOSSY_COBBLESTONE_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:mossy_cobblestone'},
    result=ItemStackOfComponent(id='minecraft:mossy_cobblestone_stairs', count=4),
    type='minecraft:crafting_shaped',
)

MOSSY_COBBLESTONE_STAIRS_FROM_MOSSY_COBBLESTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:mossy_cobblestone',
    result=ItemStackOfComponent(id='minecraft:mossy_cobblestone_stairs'),
    type='minecraft:stonecutting',
)

MOSSY_COBBLESTONE_WALL = RecipeCraftingShaped(
    pattern=['###', '###'],
    key={'#': 'minecraft:mossy_cobblestone'},
    result=ItemStackOfComponent(id='minecraft:mossy_cobblestone_wall', count=6),
    type='minecraft:crafting_shaped',
)

MOSSY_COBBLESTONE_WALL_FROM_MOSSY_COBBLESTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:mossy_cobblestone',
    result=ItemStackOfComponent(id='minecraft:mossy_cobblestone_wall'),
    type='minecraft:stonecutting',
)

MOSSY_STONE_BRICKS_FROM_MOSS_BLOCK = RecipeCraftingShapeless(
    group='mossy_stone_bricks',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:stone_bricks', 'minecraft:moss_block'],
    result=ItemStackOfComponent(id='minecraft:mossy_stone_bricks'),
    type='minecraft:crafting_shapeless',
)

MOSSY_STONE_BRICKS_FROM_VINE = RecipeCraftingShapeless(
    group='mossy_stone_bricks',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:stone_bricks', 'minecraft:vine'],
    result=ItemStackOfComponent(id='minecraft:mossy_stone_bricks'),
    type='minecraft:crafting_shapeless',
)

MOSSY_STONE_BRICK_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:mossy_stone_bricks'},
    result=ItemStackOfComponent(id='minecraft:mossy_stone_brick_slab', count=6),
    type='minecraft:crafting_shaped',
)

MOSSY_STONE_BRICK_SLAB_FROM_MOSSY_STONE_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:mossy_stone_bricks',
    result=ItemStackOfComponent(id='minecraft:mossy_stone_brick_slab', count=2),
    type='minecraft:stonecutting',
)

MOSSY_STONE_BRICK_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:mossy_stone_bricks'},
    result=ItemStackOfComponent(id='minecraft:mossy_stone_brick_stairs', count=4),
    type='minecraft:crafting_shaped',
)

MOSSY_STONE_BRICK_STAIRS_FROM_MOSSY_STONE_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:mossy_stone_bricks',
    result=ItemStackOfComponent(id='minecraft:mossy_stone_brick_stairs'),
    type='minecraft:stonecutting',
)

MOSSY_STONE_BRICK_WALL = RecipeCraftingShaped(
    pattern=['###', '###'],
    key={'#': 'minecraft:mossy_stone_bricks'},
    result=ItemStackOfComponent(id='minecraft:mossy_stone_brick_wall', count=6),
    type='minecraft:crafting_shaped',
)

MOSSY_STONE_BRICK_WALL_FROM_MOSSY_STONE_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:mossy_stone_bricks',
    result=ItemStackOfComponent(id='minecraft:mossy_stone_brick_wall'),
    type='minecraft:stonecutting',
)

MOSS_CARPET = RecipeCraftingShaped(
    group='carpet',
    pattern=['##'],
    key={'#': 'minecraft:moss_block'},
    result=ItemStackOfComponent(id='minecraft:moss_carpet', count=3),
    type='minecraft:crafting_shaped',
)

MUDDY_MANGROVE_ROOTS = RecipeCraftingShapeless(
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:mud', 'minecraft:mangrove_roots'],
    result=ItemStackOfComponent(id='minecraft:muddy_mangrove_roots'),
    type='minecraft:crafting_shapeless',
)

MUD_BRICKS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:packed_mud'},
    result=ItemStackOfComponent(id='minecraft:mud_bricks', count=4),
    type='minecraft:crafting_shaped',
)

MUD_BRICK_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:mud_bricks'},
    result=ItemStackOfComponent(id='minecraft:mud_brick_slab', count=6),
    type='minecraft:crafting_shaped',
)

MUD_BRICK_SLAB_FROM_MUD_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:mud_bricks',
    result=ItemStackOfComponent(id='minecraft:mud_brick_slab', count=2),
    type='minecraft:stonecutting',
)

MUD_BRICK_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:mud_bricks'},
    result=ItemStackOfComponent(id='minecraft:mud_brick_stairs', count=4),
    type='minecraft:crafting_shaped',
)

MUD_BRICK_STAIRS_FROM_MUD_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:mud_bricks',
    result=ItemStackOfComponent(id='minecraft:mud_brick_stairs'),
    type='minecraft:stonecutting',
)

MUD_BRICK_WALL = RecipeCraftingShaped(
    pattern=['###', '###'],
    key={'#': 'minecraft:mud_bricks'},
    result=ItemStackOfComponent(id='minecraft:mud_brick_wall', count=6),
    type='minecraft:crafting_shaped',
)

MUD_BRICK_WALL_FROM_MUD_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:mud_bricks',
    result=ItemStackOfComponent(id='minecraft:mud_brick_wall'),
    type='minecraft:stonecutting',
)

MUSHROOM_STEW = RecipeCraftingShapeless(
    group='mushroom_stew',
    ingredients=['#minecraft:mushrooms', '#minecraft:mushrooms', 'minecraft:bowl'],
    result=ItemStackOfComponent(id='minecraft:mushroom_stew'),
    type='minecraft:crafting_shapeless',
)

MUSIC_DISC_5 = RecipeCraftingShapeless(
    ingredients=[
        'minecraft:disc_fragment_5',
        'minecraft:disc_fragment_5',
        'minecraft:disc_fragment_5',
        'minecraft:disc_fragment_5',
        'minecraft:disc_fragment_5',
        'minecraft:disc_fragment_5',
        'minecraft:disc_fragment_5',
        'minecraft:disc_fragment_5',
        'minecraft:disc_fragment_5',
    ],
    result=ItemStackOfComponent(id='minecraft:music_disc_5'),
    type='minecraft:crafting_shapeless',
)

NAME_TAG = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=[' X', '# '],
    key={'#': 'minecraft:paper', 'X': '#minecraft:metal_nuggets'},
    result=ItemStackOfComponent(id='minecraft:name_tag'),
    type='minecraft:crafting_shaped',
)

NETHERITE_AXE_SMITHING = RecipeSmithingTransform(
    base='minecraft:diamond_axe',
    addition='#minecraft:netherite_tool_materials',
    template='minecraft:netherite_upgrade_smithing_template',
    result=ItemStackOfComponent(id='minecraft:netherite_axe'),
    type='minecraft:smithing_transform',
)

NETHERITE_BLOCK = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '###', '###'],
    key={'#': 'minecraft:netherite_ingot'},
    result=ItemStackOfComponent(id='minecraft:netherite_block'),
    type='minecraft:crafting_shaped',
)

NETHERITE_BOOTS_SMITHING = RecipeSmithingTransform(
    base='minecraft:diamond_boots',
    addition='#minecraft:netherite_tool_materials',
    template='minecraft:netherite_upgrade_smithing_template',
    result=ItemStackOfComponent(id='minecraft:netherite_boots'),
    type='minecraft:smithing_transform',
)

NETHERITE_CHESTPLATE_SMITHING = RecipeSmithingTransform(
    base='minecraft:diamond_chestplate',
    addition='#minecraft:netherite_tool_materials',
    template='minecraft:netherite_upgrade_smithing_template',
    result=ItemStackOfComponent(id='minecraft:netherite_chestplate'),
    type='minecraft:smithing_transform',
)

NETHERITE_HELMET_SMITHING = RecipeSmithingTransform(
    base='minecraft:diamond_helmet',
    addition='#minecraft:netherite_tool_materials',
    template='minecraft:netherite_upgrade_smithing_template',
    result=ItemStackOfComponent(id='minecraft:netherite_helmet'),
    type='minecraft:smithing_transform',
)

NETHERITE_HOE_SMITHING = RecipeSmithingTransform(
    base='minecraft:diamond_hoe',
    addition='#minecraft:netherite_tool_materials',
    template='minecraft:netherite_upgrade_smithing_template',
    result=ItemStackOfComponent(id='minecraft:netherite_hoe'),
    type='minecraft:smithing_transform',
)

NETHERITE_HORSE_ARMOR_SMITHING = RecipeSmithingTransform(
    base='minecraft:diamond_horse_armor',
    addition='#minecraft:netherite_tool_materials',
    template='minecraft:netherite_upgrade_smithing_template',
    result=ItemStackOfComponent(id='minecraft:netherite_horse_armor'),
    type='minecraft:smithing_transform',
)

NETHERITE_INGOT = RecipeCraftingShapeless(
    group='netherite_ingot',
    ingredients=[
        'minecraft:netherite_scrap',
        'minecraft:netherite_scrap',
        'minecraft:netherite_scrap',
        'minecraft:netherite_scrap',
        'minecraft:gold_ingot',
        'minecraft:gold_ingot',
        'minecraft:gold_ingot',
        'minecraft:gold_ingot',
    ],
    result=ItemStackOfComponent(id='minecraft:netherite_ingot'),
    type='minecraft:crafting_shapeless',
)

NETHERITE_INGOT_FROM_NETHERITE_BLOCK = RecipeCraftingShapeless(
    group='netherite_ingot',
    ingredients=['minecraft:netherite_block'],
    result=ItemStackOfComponent(id='minecraft:netherite_ingot', count=9),
    type='minecraft:crafting_shapeless',
)

NETHERITE_LEGGINGS_SMITHING = RecipeSmithingTransform(
    base='minecraft:diamond_leggings',
    addition='#minecraft:netherite_tool_materials',
    template='minecraft:netherite_upgrade_smithing_template',
    result=ItemStackOfComponent(id='minecraft:netherite_leggings'),
    type='minecraft:smithing_transform',
)

NETHERITE_NAUTILUS_ARMOR_SMITHING = RecipeSmithingTransform(
    base='minecraft:diamond_nautilus_armor',
    addition='#minecraft:netherite_tool_materials',
    template='minecraft:netherite_upgrade_smithing_template',
    result=ItemStackOfComponent(id='minecraft:netherite_nautilus_armor'),
    type='minecraft:smithing_transform',
)

NETHERITE_PICKAXE_SMITHING = RecipeSmithingTransform(
    base='minecraft:diamond_pickaxe',
    addition='#minecraft:netherite_tool_materials',
    template='minecraft:netherite_upgrade_smithing_template',
    result=ItemStackOfComponent(id='minecraft:netherite_pickaxe'),
    type='minecraft:smithing_transform',
)

NETHERITE_SCRAP = RecipeSmelting(
    ingredient='minecraft:ancient_debris',
    result=ItemStackOfComponent(id='minecraft:netherite_scrap'),
    experience=2.0,
    cookingtime=200,
    type='minecraft:smelting',
)

NETHERITE_SCRAP_FROM_BLASTING = RecipeBlasting(
    ingredient='minecraft:ancient_debris',
    result=ItemStackOfComponent(id='minecraft:netherite_scrap'),
    experience=2.0,
    cookingtime=200,
    type='minecraft:blasting',
)

NETHERITE_SHOVEL_SMITHING = RecipeSmithingTransform(
    base='minecraft:diamond_shovel',
    addition='#minecraft:netherite_tool_materials',
    template='minecraft:netherite_upgrade_smithing_template',
    result=ItemStackOfComponent(id='minecraft:netherite_shovel'),
    type='minecraft:smithing_transform',
)

NETHERITE_SPEAR_SMITHING = RecipeSmithingTransform(
    base='minecraft:diamond_spear',
    addition='#minecraft:netherite_tool_materials',
    template='minecraft:netherite_upgrade_smithing_template',
    result=ItemStackOfComponent(id='minecraft:netherite_spear'),
    type='minecraft:smithing_transform',
)

NETHERITE_SWORD_SMITHING = RecipeSmithingTransform(
    base='minecraft:diamond_sword',
    addition='#minecraft:netherite_tool_materials',
    template='minecraft:netherite_upgrade_smithing_template',
    result=ItemStackOfComponent(id='minecraft:netherite_sword'),
    type='minecraft:smithing_transform',
)

NETHERITE_UPGRADE_SMITHING_TEMPLATE = RecipeCraftingShaped(
    pattern=['#S#', '#C#', '###'],
    key={'#': 'minecraft:diamond', 'C': 'minecraft:netherrack', 'S': 'minecraft:netherite_upgrade_smithing_template'},
    result=ItemStackOfComponent(id='minecraft:netherite_upgrade_smithing_template', count=2),
    type='minecraft:crafting_shaped',
)

NETHER_BRICK = RecipeSmelting(
    ingredient='minecraft:netherrack',
    result=ItemStackOfComponent(id='minecraft:nether_brick'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

NETHER_BRICKS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:nether_brick'},
    result=ItemStackOfComponent(id='minecraft:nether_bricks'),
    type='minecraft:crafting_shaped',
)

NETHER_BRICK_FENCE = RecipeCraftingShaped(
    pattern=['W#W', 'W#W'],
    key={'#': 'minecraft:nether_brick', 'W': 'minecraft:nether_bricks'},
    result=ItemStackOfComponent(id='minecraft:nether_brick_fence', count=6),
    type='minecraft:crafting_shaped',
)

NETHER_BRICK_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:nether_bricks'},
    result=ItemStackOfComponent(id='minecraft:nether_brick_slab', count=6),
    type='minecraft:crafting_shaped',
)

NETHER_BRICK_SLAB_FROM_NETHER_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:nether_bricks',
    result=ItemStackOfComponent(id='minecraft:nether_brick_slab', count=2),
    type='minecraft:stonecutting',
)

NETHER_BRICK_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:nether_bricks'},
    result=ItemStackOfComponent(id='minecraft:nether_brick_stairs', count=4),
    type='minecraft:crafting_shaped',
)

NETHER_BRICK_STAIRS_FROM_NETHER_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:nether_bricks',
    result=ItemStackOfComponent(id='minecraft:nether_brick_stairs'),
    type='minecraft:stonecutting',
)

NETHER_BRICK_WALL = RecipeCraftingShaped(
    pattern=['###', '###'],
    key={'#': 'minecraft:nether_bricks'},
    result=ItemStackOfComponent(id='minecraft:nether_brick_wall', count=6),
    type='minecraft:crafting_shaped',
)

NETHER_BRICK_WALL_FROM_NETHER_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:nether_bricks',
    result=ItemStackOfComponent(id='minecraft:nether_brick_wall'),
    type='minecraft:stonecutting',
)

NETHER_WART_BLOCK = RecipeCraftingShapeless(
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:nether_wart',
        'minecraft:nether_wart',
        'minecraft:nether_wart',
        'minecraft:nether_wart',
        'minecraft:nether_wart',
        'minecraft:nether_wart',
        'minecraft:nether_wart',
        'minecraft:nether_wart',
        'minecraft:nether_wart',
    ],
    result=ItemStackOfComponent(id='minecraft:nether_wart_block'),
    type='minecraft:crafting_shapeless',
)

NOTE_BLOCK = RecipeCraftingShaped(
    category=CraftingBookCategory.REDSTONE,
    pattern=['###', '#X#', '###'],
    key={'#': '#minecraft:planks', 'X': 'minecraft:redstone'},
    result=ItemStackOfComponent(id='minecraft:note_block'),
    type='minecraft:crafting_shaped',
)

OAK_BOAT = RecipeCraftingShaped(
    group='boat',
    pattern=['# #', '###'],
    key={'#': 'minecraft:oak_planks'},
    result=ItemStackOfComponent(id='minecraft:oak_boat'),
    type='minecraft:crafting_shaped',
)

OAK_BUTTON = RecipeCraftingShapeless(
    group='wooden_button',
    category=CraftingBookCategory.REDSTONE,
    ingredients=['minecraft:oak_planks'],
    result=ItemStackOfComponent(id='minecraft:oak_button'),
    type='minecraft:crafting_shapeless',
)

OAK_CHEST_BOAT = RecipeCraftingShapeless(
    group='chest_boat',
    ingredients=['minecraft:chest', 'minecraft:oak_boat'],
    result=ItemStackOfComponent(id='minecraft:oak_chest_boat'),
    type='minecraft:crafting_shapeless',
)

OAK_DOOR = RecipeCraftingShaped(
    group='wooden_door',
    category=CraftingBookCategory.REDSTONE,
    pattern=['##', '##', '##'],
    key={'#': 'minecraft:oak_planks'},
    result=ItemStackOfComponent(id='minecraft:oak_door', count=3),
    type='minecraft:crafting_shaped',
)

OAK_FENCE = RecipeCraftingShaped(
    group='wooden_fence',
    pattern=['W#W', 'W#W'],
    key={'#': 'minecraft:stick', 'W': 'minecraft:oak_planks'},
    result=ItemStackOfComponent(id='minecraft:oak_fence', count=3),
    type='minecraft:crafting_shaped',
)

OAK_FENCE_GATE = RecipeCraftingShaped(
    group='wooden_fence_gate',
    category=CraftingBookCategory.REDSTONE,
    pattern=['#W#', '#W#'],
    key={'#': 'minecraft:stick', 'W': 'minecraft:oak_planks'},
    result=ItemStackOfComponent(id='minecraft:oak_fence_gate'),
    type='minecraft:crafting_shaped',
)

OAK_HANGING_SIGN = RecipeCraftingShaped(
    group='wooden_hanging_sign',
    pattern=['X X', '###', '###'],
    key={'#': 'minecraft:stripped_oak_log', 'X': 'minecraft:iron_chain'},
    result=ItemStackOfComponent(id='minecraft:oak_hanging_sign', count=6),
    type='minecraft:crafting_shaped',
)

OAK_PLANKS = RecipeCraftingShapeless(
    group='planks',
    category=CraftingBookCategory.BUILDING,
    ingredients=['#minecraft:oak_logs'],
    result=ItemStackOfComponent(id='minecraft:oak_planks', count=4),
    type='minecraft:crafting_shapeless',
)

OAK_PRESSURE_PLATE = RecipeCraftingShaped(
    group='wooden_pressure_plate',
    category=CraftingBookCategory.REDSTONE,
    pattern=['##'],
    key={'#': 'minecraft:oak_planks'},
    result=ItemStackOfComponent(id='minecraft:oak_pressure_plate'),
    type='minecraft:crafting_shaped',
)

OAK_SHELF = RecipeCraftingShaped(
    group='shelf',
    pattern=['###', '   ', '###'],
    key={'#': 'minecraft:stripped_oak_log'},
    result=ItemStackOfComponent(id='minecraft:oak_shelf', count=6),
    type='minecraft:crafting_shaped',
)

OAK_SIGN = RecipeCraftingShaped(
    group='wooden_sign',
    pattern=['###', '###', ' X '],
    key={'#': 'minecraft:oak_planks', 'X': 'minecraft:stick'},
    result=ItemStackOfComponent(id='minecraft:oak_sign', count=3),
    type='minecraft:crafting_shaped',
)

OAK_SLAB = RecipeCraftingShaped(
    group='wooden_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:oak_planks'},
    result=ItemStackOfComponent(id='minecraft:oak_slab', count=6),
    type='minecraft:crafting_shaped',
)

OAK_STAIRS = RecipeCraftingShaped(
    group='wooden_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:oak_planks'},
    result=ItemStackOfComponent(id='minecraft:oak_stairs', count=4),
    type='minecraft:crafting_shaped',
)

OAK_TRAPDOOR = RecipeCraftingShaped(
    group='wooden_trapdoor',
    category=CraftingBookCategory.REDSTONE,
    pattern=['###', '###'],
    key={'#': 'minecraft:oak_planks'},
    result=ItemStackOfComponent(id='minecraft:oak_trapdoor', count=2),
    type='minecraft:crafting_shaped',
)

OAK_WOOD = RecipeCraftingShaped(
    group='bark',
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:oak_log'},
    result=ItemStackOfComponent(id='minecraft:oak_wood', count=3),
    type='minecraft:crafting_shaped',
)

OBSERVER = RecipeCraftingShaped(
    category=CraftingBookCategory.REDSTONE,
    pattern=['###', 'RRQ', '###'],
    key={'#': 'minecraft:cobblestone', 'Q': 'minecraft:quartz', 'R': 'minecraft:redstone'},
    result=ItemStackOfComponent(id='minecraft:observer'),
    type='minecraft:crafting_shaped',
)

ORANGE_BANNER = RecipeCraftingShaped(
    group='banner',
    pattern=['###', '###', ' | '],
    key={'#': 'minecraft:orange_wool', '|': 'minecraft:stick'},
    result=ItemStackOfComponent(id='minecraft:orange_banner'),
    type='minecraft:crafting_shaped',
)

ORANGE_BANNER_DUPLICATE = RecipeCraftingSpecialBannerduplicate(
    type='minecraft:crafting_special_bannerduplicate',
    **dict[str, Any]({'banner': 'minecraft:orange_banner', 'result': {'id': 'minecraft:orange_banner'}}),
)

ORANGE_BED = RecipeCraftingShaped(
    group='bed',
    pattern=['###', 'XXX'],
    key={'#': 'minecraft:orange_wool', 'X': '#minecraft:planks'},
    result=ItemStackOfComponent(id='minecraft:orange_bed'),
    type='minecraft:crafting_shaped',
)

ORANGE_BUNDLE = RecipeCraftingTransmute(
    group='bundle_dye',
    category=CraftingBookCategory.EQUIPMENT,
    input='#minecraft:bundles',
    material='minecraft:orange_dye',
    result=TransmuteResult(id='minecraft:orange_bundle'),
    type='minecraft:crafting_transmute',
)

ORANGE_CANDLE = RecipeCraftingShapeless(
    group='dyed_candle',
    ingredients=['minecraft:candle', 'minecraft:orange_dye'],
    result=ItemStackOfComponent(id='minecraft:orange_candle'),
    type='minecraft:crafting_shapeless',
)

ORANGE_CARPET = RecipeCraftingShaped(
    group='woolen_carpet',
    pattern=['##'],
    key={'#': 'minecraft:orange_wool'},
    result=ItemStackOfComponent(id='minecraft:orange_carpet', count=3),
    type='minecraft:crafting_shaped',
)

ORANGE_CONCRETE_POWDER = RecipeCraftingShapeless(
    group='concrete_powder',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:orange_dye',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:gravel',
        'minecraft:gravel',
        'minecraft:gravel',
        'minecraft:gravel',
    ],
    result=ItemStackOfComponent(id='minecraft:orange_concrete_powder', count=8),
    type='minecraft:crafting_shapeless',
)

ORANGE_CONCRETE_SLAB = RecipeCraftingShaped(
    group='concrete_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:orange_concrete'},
    result=ItemStackOfComponent(id='minecraft:orange_concrete_slab', count=6),
    type='minecraft:crafting_shaped',
)

ORANGE_CONCRETE_SLAB_FROM_ORANGE_CONCRETE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:orange_concrete',
    result=ItemStackOfComponent(id='minecraft:orange_concrete_slab', count=2),
    type='minecraft:stonecutting',
)

ORANGE_CONCRETE_STAIRS = RecipeCraftingShaped(
    group='concrete_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:orange_concrete'},
    result=ItemStackOfComponent(id='minecraft:orange_concrete_stairs', count=4),
    type='minecraft:crafting_shaped',
)

ORANGE_CONCRETE_STAIRS_FROM_ORANGE_CONCRETE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:orange_concrete',
    result=ItemStackOfComponent(id='minecraft:orange_concrete_stairs'),
    type='minecraft:stonecutting',
)

ORANGE_CUSHION = RecipeCraftingShaped(
    group='cushion',
    pattern=['###'],
    key={'#': 'minecraft:orange_wool_slab'},
    result=ItemStackOfComponent(id='minecraft:orange_cushion'),
    type='minecraft:crafting_shaped',
)

ORANGE_DYE_FROM_OPEN_EYEBLOSSOM = RecipeCraftingShapeless(
    group='orange_dye',
    ingredients=['minecraft:open_eyeblossom'],
    result=ItemStackOfComponent(id='minecraft:orange_dye'),
    type='minecraft:crafting_shapeless',
)

ORANGE_DYE_FROM_ORANGE_TULIP = RecipeCraftingShapeless(
    group='orange_dye',
    ingredients=['minecraft:orange_tulip'],
    result=ItemStackOfComponent(id='minecraft:orange_dye'),
    type='minecraft:crafting_shapeless',
)

ORANGE_DYE_FROM_RED_YELLOW = RecipeCraftingShapeless(
    group='orange_dye',
    ingredients=['minecraft:red_dye', 'minecraft:yellow_dye'],
    result=ItemStackOfComponent(id='minecraft:orange_dye', count=2),
    type='minecraft:crafting_shapeless',
)

ORANGE_DYE_FROM_TORCHFLOWER = RecipeCraftingShapeless(
    group='orange_dye',
    ingredients=['minecraft:torchflower'],
    result=ItemStackOfComponent(id='minecraft:orange_dye'),
    type='minecraft:crafting_shapeless',
)

ORANGE_GLAZED_TERRACOTTA = RecipeSmelting(
    category=CookingBookCategory.BLOCKS,
    ingredient='minecraft:orange_terracotta',
    result=ItemStackOfComponent(id='minecraft:orange_glazed_terracotta'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

ORANGE_HARNESS = RecipeCraftingShaped(
    group='harness',
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['LLL', 'G#G'],
    key={'#': 'minecraft:orange_wool', 'G': 'minecraft:glass', 'L': 'minecraft:leather'},
    result=ItemStackOfComponent(id='minecraft:orange_harness'),
    type='minecraft:crafting_shaped',
)

ORANGE_SHULKER_BOX = RecipeCraftingTransmute(
    group='shulker_box_dye',
    input='#minecraft:shulker_boxes',
    material='minecraft:orange_dye',
    result=TransmuteResult(id='minecraft:orange_shulker_box'),
    type='minecraft:crafting_transmute',
)

ORANGE_STAINED_GLASS = RecipeCraftingShaped(
    group='stained_glass',
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:glass', 'X': 'minecraft:orange_dye'},
    result=ItemStackOfComponent(id='minecraft:orange_stained_glass', count=8),
    type='minecraft:crafting_shaped',
)

ORANGE_STAINED_GLASS_PANE = RecipeCraftingShaped(
    group='stained_glass_pane',
    pattern=['###', '###'],
    key={'#': 'minecraft:orange_stained_glass'},
    result=ItemStackOfComponent(id='minecraft:orange_stained_glass_pane', count=16),
    type='minecraft:crafting_shaped',
)

ORANGE_STAINED_GLASS_PANE_FROM_GLASS_PANE = RecipeCraftingShaped(
    group='stained_glass_pane',
    pattern=['###', '#$#', '###'],
    key={'#': 'minecraft:glass_pane', '$': 'minecraft:orange_dye'},
    result=ItemStackOfComponent(id='minecraft:orange_stained_glass_pane', count=8),
    type='minecraft:crafting_shaped',
)

ORANGE_TERRACOTTA = RecipeCraftingShaped(
    group='stained_terracotta',
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:terracotta', 'X': 'minecraft:orange_dye'},
    result=ItemStackOfComponent(id='minecraft:orange_terracotta', count=8),
    type='minecraft:crafting_shaped',
)

ORANGE_WOOL_SLAB = RecipeCraftingShaped(
    group='woolen_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:orange_wool'},
    result=ItemStackOfComponent(id='minecraft:orange_wool_slab', count=6),
    type='minecraft:crafting_shaped',
)

ORANGE_WOOL_STAIRS = RecipeCraftingShaped(
    group='woolen_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:orange_wool'},
    result=ItemStackOfComponent(id='minecraft:orange_wool_stairs', count=4),
    type='minecraft:crafting_shaped',
)

OXIDIZED_CHISELED_COPPER = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#', '#'],
    key={'#': 'minecraft:oxidized_cut_copper_slab'},
    result=ItemStackOfComponent(id='minecraft:oxidized_chiseled_copper'),
    type='minecraft:crafting_shaped',
)

OXIDIZED_CHISELED_COPPER_FROM_OXIDIZED_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:oxidized_copper',
    result=ItemStackOfComponent(id='minecraft:oxidized_chiseled_copper', count=4),
    type='minecraft:stonecutting',
)

OXIDIZED_CHISELED_COPPER_FROM_OXIDIZED_CUT_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:oxidized_cut_copper',
    result=ItemStackOfComponent(id='minecraft:oxidized_chiseled_copper'),
    type='minecraft:stonecutting',
)

OXIDIZED_COPPER_BULB = RecipeCraftingShaped(
    group='oxidized_copper_bulb',
    category=CraftingBookCategory.REDSTONE,
    pattern=[' C ', 'CBC', ' R '],
    key={'B': 'minecraft:blaze_rod', 'C': 'minecraft:oxidized_copper', 'R': 'minecraft:redstone'},
    result=ItemStackOfComponent(id='minecraft:oxidized_copper_bulb', count=4),
    type='minecraft:crafting_shaped',
)

OXIDIZED_COPPER_GRATE = RecipeCraftingShaped(
    group='oxidized_copper_grate',
    category=CraftingBookCategory.BUILDING,
    pattern=[' M ', 'M M', ' M '],
    key={'M': 'minecraft:oxidized_copper'},
    result=ItemStackOfComponent(id='minecraft:oxidized_copper_grate', count=4),
    type='minecraft:crafting_shaped',
)

OXIDIZED_COPPER_GRATE_FROM_OXIDIZED_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:oxidized_copper',
    result=ItemStackOfComponent(id='minecraft:oxidized_copper_grate', count=4),
    type='minecraft:stonecutting',
)

OXIDIZED_CUT_COPPER = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:oxidized_copper'},
    result=ItemStackOfComponent(id='minecraft:oxidized_cut_copper', count=4),
    type='minecraft:crafting_shaped',
)

OXIDIZED_CUT_COPPER_FROM_OXIDIZED_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:oxidized_copper',
    result=ItemStackOfComponent(id='minecraft:oxidized_cut_copper', count=4),
    type='minecraft:stonecutting',
)

OXIDIZED_CUT_COPPER_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:oxidized_cut_copper'},
    result=ItemStackOfComponent(id='minecraft:oxidized_cut_copper_slab', count=6),
    type='minecraft:crafting_shaped',
)

OXIDIZED_CUT_COPPER_SLAB_FROM_OXIDIZED_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:oxidized_copper',
    result=ItemStackOfComponent(id='minecraft:oxidized_cut_copper_slab', count=8),
    type='minecraft:stonecutting',
)

OXIDIZED_CUT_COPPER_SLAB_FROM_OXIDIZED_CUT_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:oxidized_cut_copper',
    result=ItemStackOfComponent(id='minecraft:oxidized_cut_copper_slab', count=2),
    type='minecraft:stonecutting',
)

OXIDIZED_CUT_COPPER_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:oxidized_cut_copper'},
    result=ItemStackOfComponent(id='minecraft:oxidized_cut_copper_stairs', count=4),
    type='minecraft:crafting_shaped',
)

OXIDIZED_CUT_COPPER_STAIRS_FROM_OXIDIZED_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:oxidized_copper',
    result=ItemStackOfComponent(id='minecraft:oxidized_cut_copper_stairs', count=4),
    type='minecraft:stonecutting',
)

OXIDIZED_CUT_COPPER_STAIRS_FROM_OXIDIZED_CUT_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:oxidized_cut_copper',
    result=ItemStackOfComponent(id='minecraft:oxidized_cut_copper_stairs'),
    type='minecraft:stonecutting',
)

PACKED_ICE = RecipeCraftingShapeless(
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:ice',
        'minecraft:ice',
        'minecraft:ice',
        'minecraft:ice',
        'minecraft:ice',
        'minecraft:ice',
        'minecraft:ice',
        'minecraft:ice',
        'minecraft:ice',
    ],
    result=ItemStackOfComponent(id='minecraft:packed_ice'),
    type='minecraft:crafting_shapeless',
)

PACKED_MUD = RecipeCraftingShapeless(
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:mud', 'minecraft:wheat'],
    result=ItemStackOfComponent(id='minecraft:packed_mud'),
    type='minecraft:crafting_shapeless',
)

PAINTING = RecipeCraftingShaped(
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:stick', 'X': '#minecraft:wool'},
    result=ItemStackOfComponent(id='minecraft:painting'),
    type='minecraft:crafting_shaped',
)

PALE_MOSS_CARPET = RecipeCraftingShaped(
    group='carpet',
    pattern=['##'],
    key={'#': 'minecraft:pale_moss_block'},
    result=ItemStackOfComponent(id='minecraft:pale_moss_carpet', count=3),
    type='minecraft:crafting_shaped',
)

PALE_OAK_BOAT = RecipeCraftingShaped(
    group='boat',
    pattern=['# #', '###'],
    key={'#': 'minecraft:pale_oak_planks'},
    result=ItemStackOfComponent(id='minecraft:pale_oak_boat'),
    type='minecraft:crafting_shaped',
)

PALE_OAK_BUTTON = RecipeCraftingShapeless(
    group='wooden_button',
    category=CraftingBookCategory.REDSTONE,
    ingredients=['minecraft:pale_oak_planks'],
    result=ItemStackOfComponent(id='minecraft:pale_oak_button'),
    type='minecraft:crafting_shapeless',
)

PALE_OAK_CHEST_BOAT = RecipeCraftingShapeless(
    group='chest_boat',
    ingredients=['minecraft:chest', 'minecraft:pale_oak_boat'],
    result=ItemStackOfComponent(id='minecraft:pale_oak_chest_boat'),
    type='minecraft:crafting_shapeless',
)

PALE_OAK_DOOR = RecipeCraftingShaped(
    group='wooden_door',
    category=CraftingBookCategory.REDSTONE,
    pattern=['##', '##', '##'],
    key={'#': 'minecraft:pale_oak_planks'},
    result=ItemStackOfComponent(id='minecraft:pale_oak_door', count=3),
    type='minecraft:crafting_shaped',
)

PALE_OAK_FENCE = RecipeCraftingShaped(
    group='wooden_fence',
    pattern=['W#W', 'W#W'],
    key={'#': 'minecraft:stick', 'W': 'minecraft:pale_oak_planks'},
    result=ItemStackOfComponent(id='minecraft:pale_oak_fence', count=3),
    type='minecraft:crafting_shaped',
)

PALE_OAK_FENCE_GATE = RecipeCraftingShaped(
    group='wooden_fence_gate',
    category=CraftingBookCategory.REDSTONE,
    pattern=['#W#', '#W#'],
    key={'#': 'minecraft:stick', 'W': 'minecraft:pale_oak_planks'},
    result=ItemStackOfComponent(id='minecraft:pale_oak_fence_gate'),
    type='minecraft:crafting_shaped',
)

PALE_OAK_HANGING_SIGN = RecipeCraftingShaped(
    group='wooden_hanging_sign',
    pattern=['X X', '###', '###'],
    key={'#': 'minecraft:stripped_pale_oak_log', 'X': 'minecraft:iron_chain'},
    result=ItemStackOfComponent(id='minecraft:pale_oak_hanging_sign', count=6),
    type='minecraft:crafting_shaped',
)

PALE_OAK_PLANKS = RecipeCraftingShapeless(
    group='planks',
    category=CraftingBookCategory.BUILDING,
    ingredients=['#minecraft:pale_oak_logs'],
    result=ItemStackOfComponent(id='minecraft:pale_oak_planks', count=4),
    type='minecraft:crafting_shapeless',
)

PALE_OAK_PRESSURE_PLATE = RecipeCraftingShaped(
    group='wooden_pressure_plate',
    category=CraftingBookCategory.REDSTONE,
    pattern=['##'],
    key={'#': 'minecraft:pale_oak_planks'},
    result=ItemStackOfComponent(id='minecraft:pale_oak_pressure_plate'),
    type='minecraft:crafting_shaped',
)

PALE_OAK_SHELF = RecipeCraftingShaped(
    group='shelf',
    pattern=['###', '   ', '###'],
    key={'#': 'minecraft:stripped_pale_oak_log'},
    result=ItemStackOfComponent(id='minecraft:pale_oak_shelf', count=6),
    type='minecraft:crafting_shaped',
)

PALE_OAK_SIGN = RecipeCraftingShaped(
    group='wooden_sign',
    pattern=['###', '###', ' X '],
    key={'#': 'minecraft:pale_oak_planks', 'X': 'minecraft:stick'},
    result=ItemStackOfComponent(id='minecraft:pale_oak_sign', count=3),
    type='minecraft:crafting_shaped',
)

PALE_OAK_SLAB = RecipeCraftingShaped(
    group='wooden_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:pale_oak_planks'},
    result=ItemStackOfComponent(id='minecraft:pale_oak_slab', count=6),
    type='minecraft:crafting_shaped',
)

PALE_OAK_STAIRS = RecipeCraftingShaped(
    group='wooden_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:pale_oak_planks'},
    result=ItemStackOfComponent(id='minecraft:pale_oak_stairs', count=4),
    type='minecraft:crafting_shaped',
)

PALE_OAK_TRAPDOOR = RecipeCraftingShaped(
    group='wooden_trapdoor',
    category=CraftingBookCategory.REDSTONE,
    pattern=['###', '###'],
    key={'#': 'minecraft:pale_oak_planks'},
    result=ItemStackOfComponent(id='minecraft:pale_oak_trapdoor', count=2),
    type='minecraft:crafting_shaped',
)

PALE_OAK_WOOD = RecipeCraftingShaped(
    group='bark',
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:pale_oak_log'},
    result=ItemStackOfComponent(id='minecraft:pale_oak_wood', count=3),
    type='minecraft:crafting_shaped',
)

PAPER = RecipeCraftingShaped(
    pattern=['###'],
    key={'#': 'minecraft:sugar_cane'},
    result=ItemStackOfComponent(id='minecraft:paper', count=3),
    type='minecraft:crafting_shaped',
)

PINK_BANNER = RecipeCraftingShaped(
    group='banner',
    pattern=['###', '###', ' | '],
    key={'#': 'minecraft:pink_wool', '|': 'minecraft:stick'},
    result=ItemStackOfComponent(id='minecraft:pink_banner'),
    type='minecraft:crafting_shaped',
)

PINK_BANNER_DUPLICATE = RecipeCraftingSpecialBannerduplicate(
    type='minecraft:crafting_special_bannerduplicate',
    **dict[str, Any]({'banner': 'minecraft:pink_banner', 'result': {'id': 'minecraft:pink_banner'}}),
)

PINK_BED = RecipeCraftingShaped(
    group='bed',
    pattern=['###', 'XXX'],
    key={'#': 'minecraft:pink_wool', 'X': '#minecraft:planks'},
    result=ItemStackOfComponent(id='minecraft:pink_bed'),
    type='minecraft:crafting_shaped',
)

PINK_BUNDLE = RecipeCraftingTransmute(
    group='bundle_dye',
    category=CraftingBookCategory.EQUIPMENT,
    input='#minecraft:bundles',
    material='minecraft:pink_dye',
    result=TransmuteResult(id='minecraft:pink_bundle'),
    type='minecraft:crafting_transmute',
)

PINK_CANDLE = RecipeCraftingShapeless(
    group='dyed_candle',
    ingredients=['minecraft:candle', 'minecraft:pink_dye'],
    result=ItemStackOfComponent(id='minecraft:pink_candle'),
    type='minecraft:crafting_shapeless',
)

PINK_CARPET = RecipeCraftingShaped(
    group='woolen_carpet',
    pattern=['##'],
    key={'#': 'minecraft:pink_wool'},
    result=ItemStackOfComponent(id='minecraft:pink_carpet', count=3),
    type='minecraft:crafting_shaped',
)

PINK_CONCRETE_POWDER = RecipeCraftingShapeless(
    group='concrete_powder',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:pink_dye',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:gravel',
        'minecraft:gravel',
        'minecraft:gravel',
        'minecraft:gravel',
    ],
    result=ItemStackOfComponent(id='minecraft:pink_concrete_powder', count=8),
    type='minecraft:crafting_shapeless',
)

PINK_CONCRETE_SLAB = RecipeCraftingShaped(
    group='concrete_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:pink_concrete'},
    result=ItemStackOfComponent(id='minecraft:pink_concrete_slab', count=6),
    type='minecraft:crafting_shaped',
)

PINK_CONCRETE_SLAB_FROM_PINK_CONCRETE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:pink_concrete',
    result=ItemStackOfComponent(id='minecraft:pink_concrete_slab', count=2),
    type='minecraft:stonecutting',
)

PINK_CONCRETE_STAIRS = RecipeCraftingShaped(
    group='concrete_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:pink_concrete'},
    result=ItemStackOfComponent(id='minecraft:pink_concrete_stairs', count=4),
    type='minecraft:crafting_shaped',
)

PINK_CONCRETE_STAIRS_FROM_PINK_CONCRETE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:pink_concrete',
    result=ItemStackOfComponent(id='minecraft:pink_concrete_stairs'),
    type='minecraft:stonecutting',
)

PINK_CUSHION = RecipeCraftingShaped(
    group='cushion',
    pattern=['###'],
    key={'#': 'minecraft:pink_wool_slab'},
    result=ItemStackOfComponent(id='minecraft:pink_cushion'),
    type='minecraft:crafting_shaped',
)

PINK_DYE_FROM_CACTUS_FLOWER = RecipeCraftingShapeless(
    group='pink_dye',
    ingredients=['minecraft:cactus_flower'],
    result=ItemStackOfComponent(id='minecraft:pink_dye'),
    type='minecraft:crafting_shapeless',
)

PINK_DYE_FROM_PEONY = RecipeCraftingShapeless(
    group='pink_dye',
    ingredients=['minecraft:peony'],
    result=ItemStackOfComponent(id='minecraft:pink_dye', count=2),
    type='minecraft:crafting_shapeless',
)

PINK_DYE_FROM_PINK_PETALS = RecipeCraftingShapeless(
    group='pink_dye',
    ingredients=['minecraft:pink_petals'],
    result=ItemStackOfComponent(id='minecraft:pink_dye'),
    type='minecraft:crafting_shapeless',
)

PINK_DYE_FROM_PINK_TULIP = RecipeCraftingShapeless(
    group='pink_dye',
    ingredients=['minecraft:pink_tulip'],
    result=ItemStackOfComponent(id='minecraft:pink_dye'),
    type='minecraft:crafting_shapeless',
)

PINK_DYE_FROM_RED_WHITE_DYE = RecipeCraftingShapeless(
    group='pink_dye',
    ingredients=['minecraft:red_dye', 'minecraft:white_dye'],
    result=ItemStackOfComponent(id='minecraft:pink_dye', count=2),
    type='minecraft:crafting_shapeless',
)

PINK_GLAZED_TERRACOTTA = RecipeSmelting(
    category=CookingBookCategory.BLOCKS,
    ingredient='minecraft:pink_terracotta',
    result=ItemStackOfComponent(id='minecraft:pink_glazed_terracotta'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

PINK_HARNESS = RecipeCraftingShaped(
    group='harness',
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['LLL', 'G#G'],
    key={'#': 'minecraft:pink_wool', 'G': 'minecraft:glass', 'L': 'minecraft:leather'},
    result=ItemStackOfComponent(id='minecraft:pink_harness'),
    type='minecraft:crafting_shaped',
)

PINK_SHULKER_BOX = RecipeCraftingTransmute(
    group='shulker_box_dye',
    input='#minecraft:shulker_boxes',
    material='minecraft:pink_dye',
    result=TransmuteResult(id='minecraft:pink_shulker_box'),
    type='minecraft:crafting_transmute',
)

PINK_STAINED_GLASS = RecipeCraftingShaped(
    group='stained_glass',
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:glass', 'X': 'minecraft:pink_dye'},
    result=ItemStackOfComponent(id='minecraft:pink_stained_glass', count=8),
    type='minecraft:crafting_shaped',
)

PINK_STAINED_GLASS_PANE = RecipeCraftingShaped(
    group='stained_glass_pane',
    pattern=['###', '###'],
    key={'#': 'minecraft:pink_stained_glass'},
    result=ItemStackOfComponent(id='minecraft:pink_stained_glass_pane', count=16),
    type='minecraft:crafting_shaped',
)

PINK_STAINED_GLASS_PANE_FROM_GLASS_PANE = RecipeCraftingShaped(
    group='stained_glass_pane',
    pattern=['###', '#$#', '###'],
    key={'#': 'minecraft:glass_pane', '$': 'minecraft:pink_dye'},
    result=ItemStackOfComponent(id='minecraft:pink_stained_glass_pane', count=8),
    type='minecraft:crafting_shaped',
)

PINK_TERRACOTTA = RecipeCraftingShaped(
    group='stained_terracotta',
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:terracotta', 'X': 'minecraft:pink_dye'},
    result=ItemStackOfComponent(id='minecraft:pink_terracotta', count=8),
    type='minecraft:crafting_shaped',
)

PINK_WOOL_SLAB = RecipeCraftingShaped(
    group='woolen_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:pink_wool'},
    result=ItemStackOfComponent(id='minecraft:pink_wool_slab', count=6),
    type='minecraft:crafting_shaped',
)

PINK_WOOL_STAIRS = RecipeCraftingShaped(
    group='woolen_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:pink_wool'},
    result=ItemStackOfComponent(id='minecraft:pink_wool_stairs', count=4),
    type='minecraft:crafting_shaped',
)

PISTON = RecipeCraftingShaped(
    category=CraftingBookCategory.REDSTONE,
    pattern=['TTT', '#X#', '#R#'],
    key={'#': 'minecraft:cobblestone', 'R': 'minecraft:redstone', 'T': '#minecraft:planks', 'X': 'minecraft:iron_ingot'},
    result=ItemStackOfComponent(id='minecraft:piston'),
    type='minecraft:crafting_shaped',
)

POLISHED_ANDESITE = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['SS', 'SS'],
    key={'S': 'minecraft:andesite'},
    result=ItemStackOfComponent(id='minecraft:polished_andesite', count=4),
    type='minecraft:crafting_shaped',
)

POLISHED_ANDESITE_FROM_ANDESITE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:andesite',
    result=ItemStackOfComponent(id='minecraft:polished_andesite'),
    type='minecraft:stonecutting',
)

POLISHED_ANDESITE_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:polished_andesite'},
    result=ItemStackOfComponent(id='minecraft:polished_andesite_slab', count=6),
    type='minecraft:crafting_shaped',
)

POLISHED_ANDESITE_SLAB_FROM_ANDESITE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:andesite',
    result=ItemStackOfComponent(id='minecraft:polished_andesite_slab', count=2),
    type='minecraft:stonecutting',
)

POLISHED_ANDESITE_SLAB_FROM_POLISHED_ANDESITE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_andesite',
    result=ItemStackOfComponent(id='minecraft:polished_andesite_slab', count=2),
    type='minecraft:stonecutting',
)

POLISHED_ANDESITE_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:polished_andesite'},
    result=ItemStackOfComponent(id='minecraft:polished_andesite_stairs', count=4),
    type='minecraft:crafting_shaped',
)

POLISHED_ANDESITE_STAIRS_FROM_ANDESITE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:andesite',
    result=ItemStackOfComponent(id='minecraft:polished_andesite_stairs'),
    type='minecraft:stonecutting',
)

POLISHED_ANDESITE_STAIRS_FROM_POLISHED_ANDESITE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_andesite',
    result=ItemStackOfComponent(id='minecraft:polished_andesite_stairs'),
    type='minecraft:stonecutting',
)

POLISHED_BASALT = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['SS', 'SS'],
    key={'S': 'minecraft:basalt'},
    result=ItemStackOfComponent(id='minecraft:polished_basalt', count=4),
    type='minecraft:crafting_shaped',
)

POLISHED_BASALT_FROM_BASALT_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:basalt',
    result=ItemStackOfComponent(id='minecraft:polished_basalt'),
    type='minecraft:stonecutting',
)

POLISHED_BLACKSTONE = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['SS', 'SS'],
    key={'S': 'minecraft:blackstone'},
    result=ItemStackOfComponent(id='minecraft:polished_blackstone', count=4),
    type='minecraft:crafting_shaped',
)

POLISHED_BLACKSTONE_BRICKS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:polished_blackstone'},
    result=ItemStackOfComponent(id='minecraft:polished_blackstone_bricks', count=4),
    type='minecraft:crafting_shaped',
)

POLISHED_BLACKSTONE_BRICKS_FROM_BLACKSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:blackstone',
    result=ItemStackOfComponent(id='minecraft:polished_blackstone_bricks'),
    type='minecraft:stonecutting',
)

POLISHED_BLACKSTONE_BRICKS_FROM_POLISHED_BLACKSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_blackstone',
    result=ItemStackOfComponent(id='minecraft:polished_blackstone_bricks'),
    type='minecraft:stonecutting',
)

POLISHED_BLACKSTONE_BRICK_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:polished_blackstone_bricks'},
    result=ItemStackOfComponent(id='minecraft:polished_blackstone_brick_slab', count=6),
    type='minecraft:crafting_shaped',
)

POLISHED_BLACKSTONE_BRICK_SLAB_FROM_BLACKSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:blackstone',
    result=ItemStackOfComponent(id='minecraft:polished_blackstone_brick_slab', count=2),
    type='minecraft:stonecutting',
)

POLISHED_BLACKSTONE_BRICK_SLAB_FROM_POLISHED_BLACKSTONE_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_blackstone_bricks',
    result=ItemStackOfComponent(id='minecraft:polished_blackstone_brick_slab', count=2),
    type='minecraft:stonecutting',
)

POLISHED_BLACKSTONE_BRICK_SLAB_FROM_POLISHED_BLACKSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_blackstone',
    result=ItemStackOfComponent(id='minecraft:polished_blackstone_brick_slab', count=2),
    type='minecraft:stonecutting',
)

POLISHED_BLACKSTONE_BRICK_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:polished_blackstone_bricks'},
    result=ItemStackOfComponent(id='minecraft:polished_blackstone_brick_stairs', count=4),
    type='minecraft:crafting_shaped',
)

POLISHED_BLACKSTONE_BRICK_STAIRS_FROM_BLACKSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:blackstone',
    result=ItemStackOfComponent(id='minecraft:polished_blackstone_brick_stairs'),
    type='minecraft:stonecutting',
)

POLISHED_BLACKSTONE_BRICK_STAIRS_FROM_POLISHED_BLACKSTONE_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_blackstone_bricks',
    result=ItemStackOfComponent(id='minecraft:polished_blackstone_brick_stairs'),
    type='minecraft:stonecutting',
)

POLISHED_BLACKSTONE_BRICK_STAIRS_FROM_POLISHED_BLACKSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_blackstone',
    result=ItemStackOfComponent(id='minecraft:polished_blackstone_brick_stairs'),
    type='minecraft:stonecutting',
)

POLISHED_BLACKSTONE_BRICK_WALL = RecipeCraftingShaped(
    pattern=['###', '###'],
    key={'#': 'minecraft:polished_blackstone_bricks'},
    result=ItemStackOfComponent(id='minecraft:polished_blackstone_brick_wall', count=6),
    type='minecraft:crafting_shaped',
)

POLISHED_BLACKSTONE_BRICK_WALL_FROM_BLACKSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:blackstone',
    result=ItemStackOfComponent(id='minecraft:polished_blackstone_brick_wall'),
    type='minecraft:stonecutting',
)

POLISHED_BLACKSTONE_BRICK_WALL_FROM_POLISHED_BLACKSTONE_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_blackstone_bricks',
    result=ItemStackOfComponent(id='minecraft:polished_blackstone_brick_wall'),
    type='minecraft:stonecutting',
)

POLISHED_BLACKSTONE_BRICK_WALL_FROM_POLISHED_BLACKSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_blackstone',
    result=ItemStackOfComponent(id='minecraft:polished_blackstone_brick_wall'),
    type='minecraft:stonecutting',
)

POLISHED_BLACKSTONE_BUTTON = RecipeCraftingShapeless(
    category=CraftingBookCategory.REDSTONE,
    ingredients=['minecraft:polished_blackstone'],
    result=ItemStackOfComponent(id='minecraft:polished_blackstone_button'),
    type='minecraft:crafting_shapeless',
)

POLISHED_BLACKSTONE_FROM_BLACKSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:blackstone',
    result=ItemStackOfComponent(id='minecraft:polished_blackstone'),
    type='minecraft:stonecutting',
)

POLISHED_BLACKSTONE_PRESSURE_PLATE = RecipeCraftingShaped(
    category=CraftingBookCategory.REDSTONE,
    pattern=['##'],
    key={'#': 'minecraft:polished_blackstone'},
    result=ItemStackOfComponent(id='minecraft:polished_blackstone_pressure_plate'),
    type='minecraft:crafting_shaped',
)

POLISHED_BLACKSTONE_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:polished_blackstone'},
    result=ItemStackOfComponent(id='minecraft:polished_blackstone_slab', count=6),
    type='minecraft:crafting_shaped',
)

POLISHED_BLACKSTONE_SLAB_FROM_BLACKSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:blackstone',
    result=ItemStackOfComponent(id='minecraft:polished_blackstone_slab', count=2),
    type='minecraft:stonecutting',
)

POLISHED_BLACKSTONE_SLAB_FROM_POLISHED_BLACKSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_blackstone',
    result=ItemStackOfComponent(id='minecraft:polished_blackstone_slab', count=2),
    type='minecraft:stonecutting',
)

POLISHED_BLACKSTONE_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:polished_blackstone'},
    result=ItemStackOfComponent(id='minecraft:polished_blackstone_stairs', count=4),
    type='minecraft:crafting_shaped',
)

POLISHED_BLACKSTONE_STAIRS_FROM_BLACKSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:blackstone',
    result=ItemStackOfComponent(id='minecraft:polished_blackstone_stairs'),
    type='minecraft:stonecutting',
)

POLISHED_BLACKSTONE_STAIRS_FROM_POLISHED_BLACKSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_blackstone',
    result=ItemStackOfComponent(id='minecraft:polished_blackstone_stairs'),
    type='minecraft:stonecutting',
)

POLISHED_BLACKSTONE_WALL = RecipeCraftingShaped(
    pattern=['###', '###'],
    key={'#': 'minecraft:polished_blackstone'},
    result=ItemStackOfComponent(id='minecraft:polished_blackstone_wall', count=6),
    type='minecraft:crafting_shaped',
)

POLISHED_BLACKSTONE_WALL_FROM_BLACKSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:blackstone',
    result=ItemStackOfComponent(id='minecraft:polished_blackstone_wall'),
    type='minecraft:stonecutting',
)

POLISHED_BLACKSTONE_WALL_FROM_POLISHED_BLACKSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_blackstone',
    result=ItemStackOfComponent(id='minecraft:polished_blackstone_wall'),
    type='minecraft:stonecutting',
)

POLISHED_CINNABAR = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['SS', 'SS'],
    key={'S': 'minecraft:cinnabar'},
    result=ItemStackOfComponent(id='minecraft:polished_cinnabar', count=4),
    type='minecraft:crafting_shaped',
)

POLISHED_CINNABAR_FROM_CINNABAR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cinnabar',
    result=ItemStackOfComponent(id='minecraft:polished_cinnabar'),
    type='minecraft:stonecutting',
)

POLISHED_CINNABAR_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:polished_cinnabar'},
    result=ItemStackOfComponent(id='minecraft:polished_cinnabar_slab', count=6),
    type='minecraft:crafting_shaped',
)

POLISHED_CINNABAR_SLAB_FROM_CINNABAR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cinnabar',
    result=ItemStackOfComponent(id='minecraft:polished_cinnabar_slab', count=2),
    type='minecraft:stonecutting',
)

POLISHED_CINNABAR_SLAB_FROM_POLISHED_CINNABAR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_cinnabar',
    result=ItemStackOfComponent(id='minecraft:polished_cinnabar_slab', count=2),
    type='minecraft:stonecutting',
)

POLISHED_CINNABAR_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:polished_cinnabar'},
    result=ItemStackOfComponent(id='minecraft:polished_cinnabar_stairs', count=4),
    type='minecraft:crafting_shaped',
)

POLISHED_CINNABAR_STAIRS_FROM_CINNABAR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cinnabar',
    result=ItemStackOfComponent(id='minecraft:polished_cinnabar_stairs'),
    type='minecraft:stonecutting',
)

POLISHED_CINNABAR_STAIRS_FROM_POLISHED_CINNABAR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_cinnabar',
    result=ItemStackOfComponent(id='minecraft:polished_cinnabar_stairs'),
    type='minecraft:stonecutting',
)

POLISHED_CINNABAR_WALL = RecipeCraftingShaped(
    pattern=['###', '###'],
    key={'#': 'minecraft:polished_cinnabar'},
    result=ItemStackOfComponent(id='minecraft:polished_cinnabar_wall', count=6),
    type='minecraft:crafting_shaped',
)

POLISHED_CINNABAR_WALL_FROM_CINNABAR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cinnabar',
    result=ItemStackOfComponent(id='minecraft:polished_cinnabar_wall'),
    type='minecraft:stonecutting',
)

POLISHED_CINNABAR_WALL_FROM_POLISHED_CINNABAR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_cinnabar',
    result=ItemStackOfComponent(id='minecraft:polished_cinnabar_wall'),
    type='minecraft:stonecutting',
)

POLISHED_DEEPSLATE = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['SS', 'SS'],
    key={'S': 'minecraft:cobbled_deepslate'},
    result=ItemStackOfComponent(id='minecraft:polished_deepslate', count=4),
    type='minecraft:crafting_shaped',
)

POLISHED_DEEPSLATE_FROM_COBBLED_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cobbled_deepslate',
    result=ItemStackOfComponent(id='minecraft:polished_deepslate'),
    type='minecraft:stonecutting',
)

POLISHED_DEEPSLATE_FROM_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:deepslate',
    result=ItemStackOfComponent(id='minecraft:polished_deepslate'),
    type='minecraft:stonecutting',
)

POLISHED_DEEPSLATE_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:polished_deepslate'},
    result=ItemStackOfComponent(id='minecraft:polished_deepslate_slab', count=6),
    type='minecraft:crafting_shaped',
)

POLISHED_DEEPSLATE_SLAB_FROM_COBBLED_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cobbled_deepslate',
    result=ItemStackOfComponent(id='minecraft:polished_deepslate_slab', count=2),
    type='minecraft:stonecutting',
)

POLISHED_DEEPSLATE_SLAB_FROM_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:deepslate',
    result=ItemStackOfComponent(id='minecraft:polished_deepslate_slab', count=2),
    type='minecraft:stonecutting',
)

POLISHED_DEEPSLATE_SLAB_FROM_POLISHED_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_deepslate',
    result=ItemStackOfComponent(id='minecraft:polished_deepslate_slab', count=2),
    type='minecraft:stonecutting',
)

POLISHED_DEEPSLATE_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:polished_deepslate'},
    result=ItemStackOfComponent(id='minecraft:polished_deepslate_stairs', count=4),
    type='minecraft:crafting_shaped',
)

POLISHED_DEEPSLATE_STAIRS_FROM_COBBLED_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cobbled_deepslate',
    result=ItemStackOfComponent(id='minecraft:polished_deepslate_stairs'),
    type='minecraft:stonecutting',
)

POLISHED_DEEPSLATE_STAIRS_FROM_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:deepslate',
    result=ItemStackOfComponent(id='minecraft:polished_deepslate_stairs'),
    type='minecraft:stonecutting',
)

POLISHED_DEEPSLATE_STAIRS_FROM_POLISHED_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_deepslate',
    result=ItemStackOfComponent(id='minecraft:polished_deepslate_stairs'),
    type='minecraft:stonecutting',
)

POLISHED_DEEPSLATE_WALL = RecipeCraftingShaped(
    pattern=['###', '###'],
    key={'#': 'minecraft:polished_deepslate'},
    result=ItemStackOfComponent(id='minecraft:polished_deepslate_wall', count=6),
    type='minecraft:crafting_shaped',
)

POLISHED_DEEPSLATE_WALL_FROM_COBBLED_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:cobbled_deepslate',
    result=ItemStackOfComponent(id='minecraft:polished_deepslate_wall'),
    type='minecraft:stonecutting',
)

POLISHED_DEEPSLATE_WALL_FROM_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:deepslate',
    result=ItemStackOfComponent(id='minecraft:polished_deepslate_wall'),
    type='minecraft:stonecutting',
)

POLISHED_DEEPSLATE_WALL_FROM_POLISHED_DEEPSLATE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_deepslate',
    result=ItemStackOfComponent(id='minecraft:polished_deepslate_wall'),
    type='minecraft:stonecutting',
)

POLISHED_DIORITE = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['SS', 'SS'],
    key={'S': 'minecraft:diorite'},
    result=ItemStackOfComponent(id='minecraft:polished_diorite', count=4),
    type='minecraft:crafting_shaped',
)

POLISHED_DIORITE_FROM_DIORITE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:diorite',
    result=ItemStackOfComponent(id='minecraft:polished_diorite'),
    type='minecraft:stonecutting',
)

POLISHED_DIORITE_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:polished_diorite'},
    result=ItemStackOfComponent(id='minecraft:polished_diorite_slab', count=6),
    type='minecraft:crafting_shaped',
)

POLISHED_DIORITE_SLAB_FROM_DIORITE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:diorite',
    result=ItemStackOfComponent(id='minecraft:polished_diorite_slab', count=2),
    type='minecraft:stonecutting',
)

POLISHED_DIORITE_SLAB_FROM_POLISHED_DIORITE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_diorite',
    result=ItemStackOfComponent(id='minecraft:polished_diorite_slab', count=2),
    type='minecraft:stonecutting',
)

POLISHED_DIORITE_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:polished_diorite'},
    result=ItemStackOfComponent(id='minecraft:polished_diorite_stairs', count=4),
    type='minecraft:crafting_shaped',
)

POLISHED_DIORITE_STAIRS_FROM_DIORITE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:diorite',
    result=ItemStackOfComponent(id='minecraft:polished_diorite_stairs'),
    type='minecraft:stonecutting',
)

POLISHED_DIORITE_STAIRS_FROM_POLISHED_DIORITE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_diorite',
    result=ItemStackOfComponent(id='minecraft:polished_diorite_stairs'),
    type='minecraft:stonecutting',
)

POLISHED_GRANITE = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['SS', 'SS'],
    key={'S': 'minecraft:granite'},
    result=ItemStackOfComponent(id='minecraft:polished_granite', count=4),
    type='minecraft:crafting_shaped',
)

POLISHED_GRANITE_FROM_GRANITE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:granite',
    result=ItemStackOfComponent(id='minecraft:polished_granite'),
    type='minecraft:stonecutting',
)

POLISHED_GRANITE_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:polished_granite'},
    result=ItemStackOfComponent(id='minecraft:polished_granite_slab', count=6),
    type='minecraft:crafting_shaped',
)

POLISHED_GRANITE_SLAB_FROM_GRANITE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:granite',
    result=ItemStackOfComponent(id='minecraft:polished_granite_slab', count=2),
    type='minecraft:stonecutting',
)

POLISHED_GRANITE_SLAB_FROM_POLISHED_GRANITE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_granite',
    result=ItemStackOfComponent(id='minecraft:polished_granite_slab', count=2),
    type='minecraft:stonecutting',
)

POLISHED_GRANITE_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:polished_granite'},
    result=ItemStackOfComponent(id='minecraft:polished_granite_stairs', count=4),
    type='minecraft:crafting_shaped',
)

POLISHED_GRANITE_STAIRS_FROM_GRANITE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:granite',
    result=ItemStackOfComponent(id='minecraft:polished_granite_stairs'),
    type='minecraft:stonecutting',
)

POLISHED_GRANITE_STAIRS_FROM_POLISHED_GRANITE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_granite',
    result=ItemStackOfComponent(id='minecraft:polished_granite_stairs'),
    type='minecraft:stonecutting',
)

POLISHED_SULFUR = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['SS', 'SS'],
    key={'S': 'minecraft:sulfur'},
    result=ItemStackOfComponent(id='minecraft:polished_sulfur', count=4),
    type='minecraft:crafting_shaped',
)

POLISHED_SULFUR_FROM_SULFUR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:sulfur',
    result=ItemStackOfComponent(id='minecraft:polished_sulfur'),
    type='minecraft:stonecutting',
)

POLISHED_SULFUR_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:polished_sulfur'},
    result=ItemStackOfComponent(id='minecraft:polished_sulfur_slab', count=6),
    type='minecraft:crafting_shaped',
)

POLISHED_SULFUR_SLAB_FROM_POLISHED_SULFUR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_sulfur',
    result=ItemStackOfComponent(id='minecraft:polished_sulfur_slab', count=2),
    type='minecraft:stonecutting',
)

POLISHED_SULFUR_SLAB_FROM_SULFUR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:sulfur',
    result=ItemStackOfComponent(id='minecraft:polished_sulfur_slab', count=2),
    type='minecraft:stonecutting',
)

POLISHED_SULFUR_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:polished_sulfur'},
    result=ItemStackOfComponent(id='minecraft:polished_sulfur_stairs', count=4),
    type='minecraft:crafting_shaped',
)

POLISHED_SULFUR_STAIRS_FROM_POLISHED_SULFUR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_sulfur',
    result=ItemStackOfComponent(id='minecraft:polished_sulfur_stairs'),
    type='minecraft:stonecutting',
)

POLISHED_SULFUR_STAIRS_FROM_SULFUR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:sulfur',
    result=ItemStackOfComponent(id='minecraft:polished_sulfur_stairs'),
    type='minecraft:stonecutting',
)

POLISHED_SULFUR_WALL = RecipeCraftingShaped(
    pattern=['###', '###'],
    key={'#': 'minecraft:polished_sulfur'},
    result=ItemStackOfComponent(id='minecraft:polished_sulfur_wall', count=6),
    type='minecraft:crafting_shaped',
)

POLISHED_SULFUR_WALL_FROM_POLISHED_SULFUR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_sulfur',
    result=ItemStackOfComponent(id='minecraft:polished_sulfur_wall'),
    type='minecraft:stonecutting',
)

POLISHED_SULFUR_WALL_FROM_SULFUR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:sulfur',
    result=ItemStackOfComponent(id='minecraft:polished_sulfur_wall'),
    type='minecraft:stonecutting',
)

POLISHED_TUFF = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['SS', 'SS'],
    key={'S': 'minecraft:tuff'},
    result=ItemStackOfComponent(id='minecraft:polished_tuff', count=4),
    type='minecraft:crafting_shaped',
)

POLISHED_TUFF_FROM_TUFF_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:tuff',
    result=ItemStackOfComponent(id='minecraft:polished_tuff'),
    type='minecraft:stonecutting',
)

POLISHED_TUFF_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:polished_tuff'},
    result=ItemStackOfComponent(id='minecraft:polished_tuff_slab', count=6),
    type='minecraft:crafting_shaped',
)

POLISHED_TUFF_SLAB_FROM_POLISHED_TUFF_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_tuff',
    result=ItemStackOfComponent(id='minecraft:polished_tuff_slab', count=2),
    type='minecraft:stonecutting',
)

POLISHED_TUFF_SLAB_FROM_TUFF_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:tuff',
    result=ItemStackOfComponent(id='minecraft:polished_tuff_slab', count=2),
    type='minecraft:stonecutting',
)

POLISHED_TUFF_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:polished_tuff'},
    result=ItemStackOfComponent(id='minecraft:polished_tuff_stairs', count=4),
    type='minecraft:crafting_shaped',
)

POLISHED_TUFF_STAIRS_FROM_POLISHED_TUFF_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_tuff',
    result=ItemStackOfComponent(id='minecraft:polished_tuff_stairs'),
    type='minecraft:stonecutting',
)

POLISHED_TUFF_STAIRS_FROM_TUFF_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:tuff',
    result=ItemStackOfComponent(id='minecraft:polished_tuff_stairs'),
    type='minecraft:stonecutting',
)

POLISHED_TUFF_WALL = RecipeCraftingShaped(
    pattern=['###', '###'],
    key={'#': 'minecraft:polished_tuff'},
    result=ItemStackOfComponent(id='minecraft:polished_tuff_wall', count=6),
    type='minecraft:crafting_shaped',
)

POLISHED_TUFF_WALL_FROM_POLISHED_TUFF_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_tuff',
    result=ItemStackOfComponent(id='minecraft:polished_tuff_wall'),
    type='minecraft:stonecutting',
)

POLISHED_TUFF_WALL_FROM_TUFF_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:tuff',
    result=ItemStackOfComponent(id='minecraft:polished_tuff_wall'),
    type='minecraft:stonecutting',
)

POPLAR_BOAT = RecipeCraftingShaped(
    group='boat',
    pattern=['# #', '###'],
    key={'#': 'minecraft:poplar_planks'},
    result=ItemStackOfComponent(id='minecraft:poplar_boat'),
    type='minecraft:crafting_shaped',
)

POPLAR_BUTTON = RecipeCraftingShapeless(
    group='wooden_button',
    category=CraftingBookCategory.REDSTONE,
    ingredients=['minecraft:poplar_planks'],
    result=ItemStackOfComponent(id='minecraft:poplar_button'),
    type='minecraft:crafting_shapeless',
)

POPLAR_CHEST_BOAT = RecipeCraftingShapeless(
    group='chest_boat',
    ingredients=['minecraft:chest', 'minecraft:poplar_boat'],
    result=ItemStackOfComponent(id='minecraft:poplar_chest_boat'),
    type='minecraft:crafting_shapeless',
)

POPLAR_DOOR = RecipeCraftingShaped(
    group='wooden_door',
    category=CraftingBookCategory.REDSTONE,
    pattern=['##', '##', '##'],
    key={'#': 'minecraft:poplar_planks'},
    result=ItemStackOfComponent(id='minecraft:poplar_door', count=3),
    type='minecraft:crafting_shaped',
)

POPLAR_FENCE = RecipeCraftingShaped(
    group='wooden_fence',
    pattern=['W#W', 'W#W'],
    key={'#': 'minecraft:stick', 'W': 'minecraft:poplar_planks'},
    result=ItemStackOfComponent(id='minecraft:poplar_fence', count=3),
    type='minecraft:crafting_shaped',
)

POPLAR_FENCE_GATE = RecipeCraftingShaped(
    group='wooden_fence_gate',
    category=CraftingBookCategory.REDSTONE,
    pattern=['#W#', '#W#'],
    key={'#': 'minecraft:stick', 'W': 'minecraft:poplar_planks'},
    result=ItemStackOfComponent(id='minecraft:poplar_fence_gate'),
    type='minecraft:crafting_shaped',
)

POPLAR_HANGING_SIGN = RecipeCraftingShaped(
    group='wooden_hanging_sign',
    pattern=['X X', '###', '###'],
    key={'#': 'minecraft:stripped_poplar_log', 'X': 'minecraft:iron_chain'},
    result=ItemStackOfComponent(id='minecraft:poplar_hanging_sign', count=6),
    type='minecraft:crafting_shaped',
)

POPLAR_PLANKS = RecipeCraftingShapeless(
    group='planks',
    category=CraftingBookCategory.BUILDING,
    ingredients=['#minecraft:poplar_logs'],
    result=ItemStackOfComponent(id='minecraft:poplar_planks', count=4),
    type='minecraft:crafting_shapeless',
)

POPLAR_PRESSURE_PLATE = RecipeCraftingShaped(
    group='wooden_pressure_plate',
    category=CraftingBookCategory.REDSTONE,
    pattern=['##'],
    key={'#': 'minecraft:poplar_planks'},
    result=ItemStackOfComponent(id='minecraft:poplar_pressure_plate'),
    type='minecraft:crafting_shaped',
)

POPLAR_SHELF = RecipeCraftingShaped(
    group='shelf',
    pattern=['###', '   ', '###'],
    key={'#': 'minecraft:stripped_poplar_log'},
    result=ItemStackOfComponent(id='minecraft:poplar_shelf', count=6),
    type='minecraft:crafting_shaped',
)

POPLAR_SIGN = RecipeCraftingShaped(
    group='wooden_sign',
    pattern=['###', '###', ' X '],
    key={'#': 'minecraft:poplar_planks', 'X': 'minecraft:stick'},
    result=ItemStackOfComponent(id='minecraft:poplar_sign', count=3),
    type='minecraft:crafting_shaped',
)

POPLAR_SLAB = RecipeCraftingShaped(
    group='wooden_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:poplar_planks'},
    result=ItemStackOfComponent(id='minecraft:poplar_slab', count=6),
    type='minecraft:crafting_shaped',
)

POPLAR_STAIRS = RecipeCraftingShaped(
    group='wooden_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:poplar_planks'},
    result=ItemStackOfComponent(id='minecraft:poplar_stairs', count=4),
    type='minecraft:crafting_shaped',
)

POPLAR_TRAPDOOR = RecipeCraftingShaped(
    group='wooden_trapdoor',
    category=CraftingBookCategory.REDSTONE,
    pattern=['###', '###'],
    key={'#': 'minecraft:poplar_planks'},
    result=ItemStackOfComponent(id='minecraft:poplar_trapdoor', count=2),
    type='minecraft:crafting_shaped',
)

POPLAR_WOOD = RecipeCraftingShaped(
    group='bark',
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:poplar_log'},
    result=ItemStackOfComponent(id='minecraft:poplar_wood', count=3),
    type='minecraft:crafting_shaped',
)

POPPED_CHORUS_FRUIT = RecipeSmelting(
    ingredient='minecraft:chorus_fruit',
    result=ItemStackOfComponent(id='minecraft:popped_chorus_fruit'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

POTENT_SULFUR = RecipeCraftingShapeless(
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:sulfur',
        'minecraft:sulfur',
        'minecraft:sulfur',
        'minecraft:sulfur',
        'minecraft:sulfur',
        'minecraft:sulfur',
        'minecraft:sulfur',
        'minecraft:sulfur',
        'minecraft:sulfur',
    ],
    result=ItemStackOfComponent(id='minecraft:potent_sulfur'),
    type='minecraft:crafting_shapeless',
)

POWERED_RAIL = RecipeCraftingShaped(
    pattern=['X X', 'X#X', 'XRX'],
    key={'#': 'minecraft:stick', 'R': 'minecraft:redstone', 'X': 'minecraft:gold_ingot'},
    result=ItemStackOfComponent(id='minecraft:powered_rail', count=6),
    type='minecraft:crafting_shaped',
)

PRISMARINE = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:prismarine_shard'},
    result=ItemStackOfComponent(id='minecraft:prismarine'),
    type='minecraft:crafting_shaped',
)

PRISMARINE_BRICKS = RecipeCraftingShapeless(
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:prismarine_shard',
        'minecraft:prismarine_shard',
        'minecraft:prismarine_shard',
        'minecraft:prismarine_shard',
        'minecraft:prismarine_shard',
        'minecraft:prismarine_shard',
        'minecraft:prismarine_shard',
        'minecraft:prismarine_shard',
        'minecraft:prismarine_shard',
    ],
    result=ItemStackOfComponent(id='minecraft:prismarine_bricks'),
    type='minecraft:crafting_shapeless',
)

PRISMARINE_BRICK_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:prismarine_bricks'},
    result=ItemStackOfComponent(id='minecraft:prismarine_brick_slab', count=6),
    type='minecraft:crafting_shaped',
)

PRISMARINE_BRICK_SLAB_FROM_PRISMARINE_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:prismarine_bricks',
    result=ItemStackOfComponent(id='minecraft:prismarine_brick_slab', count=2),
    type='minecraft:stonecutting',
)

PRISMARINE_BRICK_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:prismarine_bricks'},
    result=ItemStackOfComponent(id='minecraft:prismarine_brick_stairs', count=4),
    type='minecraft:crafting_shaped',
)

PRISMARINE_BRICK_STAIRS_FROM_PRISMARINE_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:prismarine_bricks',
    result=ItemStackOfComponent(id='minecraft:prismarine_brick_stairs'),
    type='minecraft:stonecutting',
)

PRISMARINE_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:prismarine'},
    result=ItemStackOfComponent(id='minecraft:prismarine_slab', count=6),
    type='minecraft:crafting_shaped',
)

PRISMARINE_SLAB_FROM_PRISMARINE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:prismarine',
    result=ItemStackOfComponent(id='minecraft:prismarine_slab', count=2),
    type='minecraft:stonecutting',
)

PRISMARINE_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:prismarine'},
    result=ItemStackOfComponent(id='minecraft:prismarine_stairs', count=4),
    type='minecraft:crafting_shaped',
)

PRISMARINE_STAIRS_FROM_PRISMARINE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:prismarine',
    result=ItemStackOfComponent(id='minecraft:prismarine_stairs'),
    type='minecraft:stonecutting',
)

PRISMARINE_WALL = RecipeCraftingShaped(
    pattern=['###', '###'],
    key={'#': 'minecraft:prismarine'},
    result=ItemStackOfComponent(id='minecraft:prismarine_wall', count=6),
    type='minecraft:crafting_shaped',
)

PRISMARINE_WALL_FROM_PRISMARINE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:prismarine',
    result=ItemStackOfComponent(id='minecraft:prismarine_wall'),
    type='minecraft:stonecutting',
)

PUMPKIN_PIE = RecipeCraftingShapeless(
    ingredients=['minecraft:pumpkin', 'minecraft:sugar', '#minecraft:eggs'],
    result=ItemStackOfComponent(id='minecraft:pumpkin_pie'),
    type='minecraft:crafting_shapeless',
)

PUMPKIN_SEEDS = RecipeCraftingShapeless(
    ingredients=['minecraft:pumpkin'],
    result=ItemStackOfComponent(id='minecraft:pumpkin_seeds', count=4),
    type='minecraft:crafting_shapeless',
)

PURPLE_BANNER = RecipeCraftingShaped(
    group='banner',
    pattern=['###', '###', ' | '],
    key={'#': 'minecraft:purple_wool', '|': 'minecraft:stick'},
    result=ItemStackOfComponent(id='minecraft:purple_banner'),
    type='minecraft:crafting_shaped',
)

PURPLE_BANNER_DUPLICATE = RecipeCraftingSpecialBannerduplicate(
    type='minecraft:crafting_special_bannerduplicate',
    **dict[str, Any]({'banner': 'minecraft:purple_banner', 'result': {'id': 'minecraft:purple_banner'}}),
)

PURPLE_BED = RecipeCraftingShaped(
    group='bed',
    pattern=['###', 'XXX'],
    key={'#': 'minecraft:purple_wool', 'X': '#minecraft:planks'},
    result=ItemStackOfComponent(id='minecraft:purple_bed'),
    type='minecraft:crafting_shaped',
)

PURPLE_BUNDLE = RecipeCraftingTransmute(
    group='bundle_dye',
    category=CraftingBookCategory.EQUIPMENT,
    input='#minecraft:bundles',
    material='minecraft:purple_dye',
    result=TransmuteResult(id='minecraft:purple_bundle'),
    type='minecraft:crafting_transmute',
)

PURPLE_CANDLE = RecipeCraftingShapeless(
    group='dyed_candle',
    ingredients=['minecraft:candle', 'minecraft:purple_dye'],
    result=ItemStackOfComponent(id='minecraft:purple_candle'),
    type='minecraft:crafting_shapeless',
)

PURPLE_CARPET = RecipeCraftingShaped(
    group='woolen_carpet',
    pattern=['##'],
    key={'#': 'minecraft:purple_wool'},
    result=ItemStackOfComponent(id='minecraft:purple_carpet', count=3),
    type='minecraft:crafting_shaped',
)

PURPLE_CONCRETE_POWDER = RecipeCraftingShapeless(
    group='concrete_powder',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:purple_dye',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:gravel',
        'minecraft:gravel',
        'minecraft:gravel',
        'minecraft:gravel',
    ],
    result=ItemStackOfComponent(id='minecraft:purple_concrete_powder', count=8),
    type='minecraft:crafting_shapeless',
)

PURPLE_CONCRETE_SLAB = RecipeCraftingShaped(
    group='concrete_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:purple_concrete'},
    result=ItemStackOfComponent(id='minecraft:purple_concrete_slab', count=6),
    type='minecraft:crafting_shaped',
)

PURPLE_CONCRETE_SLAB_FROM_PURPLE_CONCRETE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:purple_concrete',
    result=ItemStackOfComponent(id='minecraft:purple_concrete_slab', count=2),
    type='minecraft:stonecutting',
)

PURPLE_CONCRETE_STAIRS = RecipeCraftingShaped(
    group='concrete_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:purple_concrete'},
    result=ItemStackOfComponent(id='minecraft:purple_concrete_stairs', count=4),
    type='minecraft:crafting_shaped',
)

PURPLE_CONCRETE_STAIRS_FROM_PURPLE_CONCRETE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:purple_concrete',
    result=ItemStackOfComponent(id='minecraft:purple_concrete_stairs'),
    type='minecraft:stonecutting',
)

PURPLE_CUSHION = RecipeCraftingShaped(
    group='cushion',
    pattern=['###'],
    key={'#': 'minecraft:purple_wool_slab'},
    result=ItemStackOfComponent(id='minecraft:purple_cushion'),
    type='minecraft:crafting_shaped',
)

PURPLE_DYE = RecipeCraftingShapeless(
    ingredients=['minecraft:blue_dye', 'minecraft:red_dye'],
    result=ItemStackOfComponent(id='minecraft:purple_dye', count=2),
    type='minecraft:crafting_shapeless',
)

PURPLE_GLAZED_TERRACOTTA = RecipeSmelting(
    category=CookingBookCategory.BLOCKS,
    ingredient='minecraft:purple_terracotta',
    result=ItemStackOfComponent(id='minecraft:purple_glazed_terracotta'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

PURPLE_HARNESS = RecipeCraftingShaped(
    group='harness',
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['LLL', 'G#G'],
    key={'#': 'minecraft:purple_wool', 'G': 'minecraft:glass', 'L': 'minecraft:leather'},
    result=ItemStackOfComponent(id='minecraft:purple_harness'),
    type='minecraft:crafting_shaped',
)

PURPLE_SHULKER_BOX = RecipeCraftingTransmute(
    group='shulker_box_dye',
    input='#minecraft:shulker_boxes',
    material='minecraft:purple_dye',
    result=TransmuteResult(id='minecraft:purple_shulker_box'),
    type='minecraft:crafting_transmute',
)

PURPLE_STAINED_GLASS = RecipeCraftingShaped(
    group='stained_glass',
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:glass', 'X': 'minecraft:purple_dye'},
    result=ItemStackOfComponent(id='minecraft:purple_stained_glass', count=8),
    type='minecraft:crafting_shaped',
)

PURPLE_STAINED_GLASS_PANE = RecipeCraftingShaped(
    group='stained_glass_pane',
    pattern=['###', '###'],
    key={'#': 'minecraft:purple_stained_glass'},
    result=ItemStackOfComponent(id='minecraft:purple_stained_glass_pane', count=16),
    type='minecraft:crafting_shaped',
)

PURPLE_STAINED_GLASS_PANE_FROM_GLASS_PANE = RecipeCraftingShaped(
    group='stained_glass_pane',
    pattern=['###', '#$#', '###'],
    key={'#': 'minecraft:glass_pane', '$': 'minecraft:purple_dye'},
    result=ItemStackOfComponent(id='minecraft:purple_stained_glass_pane', count=8),
    type='minecraft:crafting_shaped',
)

PURPLE_TERRACOTTA = RecipeCraftingShaped(
    group='stained_terracotta',
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:terracotta', 'X': 'minecraft:purple_dye'},
    result=ItemStackOfComponent(id='minecraft:purple_terracotta', count=8),
    type='minecraft:crafting_shaped',
)

PURPLE_WOOL_SLAB = RecipeCraftingShaped(
    group='woolen_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:purple_wool'},
    result=ItemStackOfComponent(id='minecraft:purple_wool_slab', count=6),
    type='minecraft:crafting_shaped',
)

PURPLE_WOOL_STAIRS = RecipeCraftingShaped(
    group='woolen_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:purple_wool'},
    result=ItemStackOfComponent(id='minecraft:purple_wool_stairs', count=4),
    type='minecraft:crafting_shaped',
)

PURPUR_BLOCK = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['FF', 'FF'],
    key={'F': 'minecraft:popped_chorus_fruit'},
    result=ItemStackOfComponent(id='minecraft:purpur_block', count=4),
    type='minecraft:crafting_shaped',
)

PURPUR_PILLAR = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#', '#'],
    key={'#': 'minecraft:purpur_slab'},
    result=ItemStackOfComponent(id='minecraft:purpur_pillar'),
    type='minecraft:crafting_shaped',
)

PURPUR_PILLAR_FROM_PURPUR_BLOCK_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:purpur_block',
    result=ItemStackOfComponent(id='minecraft:purpur_pillar'),
    type='minecraft:stonecutting',
)

PURPUR_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': ['minecraft:purpur_block', 'minecraft:purpur_pillar']},
    result=ItemStackOfComponent(id='minecraft:purpur_slab', count=6),
    type='minecraft:crafting_shaped',
)

PURPUR_SLAB_FROM_PURPUR_BLOCK_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:purpur_block',
    result=ItemStackOfComponent(id='minecraft:purpur_slab', count=2),
    type='minecraft:stonecutting',
)

PURPUR_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': ['minecraft:purpur_block', 'minecraft:purpur_pillar']},
    result=ItemStackOfComponent(id='minecraft:purpur_stairs', count=4),
    type='minecraft:crafting_shaped',
)

PURPUR_STAIRS_FROM_PURPUR_BLOCK_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:purpur_block',
    result=ItemStackOfComponent(id='minecraft:purpur_stairs'),
    type='minecraft:stonecutting',
)

QUARTZ = RecipeSmelting(
    ingredient='minecraft:nether_quartz_ore',
    result=ItemStackOfComponent(id='minecraft:quartz'),
    experience=0.2,
    cookingtime=200,
    type='minecraft:smelting',
)

QUARTZ_BLOCK = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:quartz'},
    result=ItemStackOfComponent(id='minecraft:quartz_block'),
    type='minecraft:crafting_shaped',
)

QUARTZ_BRICKS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:quartz_block'},
    result=ItemStackOfComponent(id='minecraft:quartz_bricks', count=4),
    type='minecraft:crafting_shaped',
)

QUARTZ_BRICKS_FROM_QUARTZ_BLOCK_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:quartz_block',
    result=ItemStackOfComponent(id='minecraft:quartz_bricks'),
    type='minecraft:stonecutting',
)

QUARTZ_FROM_BLASTING = RecipeBlasting(
    ingredient='minecraft:nether_quartz_ore',
    result=ItemStackOfComponent(id='minecraft:quartz'),
    experience=0.2,
    cookingtime=200,
    type='minecraft:blasting',
)

QUARTZ_PILLAR = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#', '#'],
    key={'#': 'minecraft:quartz_block'},
    result=ItemStackOfComponent(id='minecraft:quartz_pillar', count=2),
    type='minecraft:crafting_shaped',
)

QUARTZ_PILLAR_FROM_QUARTZ_BLOCK_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:quartz_block',
    result=ItemStackOfComponent(id='minecraft:quartz_pillar'),
    type='minecraft:stonecutting',
)

QUARTZ_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': ['minecraft:chiseled_quartz_block', 'minecraft:quartz_block', 'minecraft:quartz_pillar']},
    result=ItemStackOfComponent(id='minecraft:quartz_slab', count=6),
    type='minecraft:crafting_shaped',
)

QUARTZ_SLAB_FROM_QUARTZ_BLOCK_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:quartz_block',
    result=ItemStackOfComponent(id='minecraft:quartz_slab', count=2),
    type='minecraft:stonecutting',
)

QUARTZ_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': ['minecraft:chiseled_quartz_block', 'minecraft:quartz_block', 'minecraft:quartz_pillar']},
    result=ItemStackOfComponent(id='minecraft:quartz_stairs', count=4),
    type='minecraft:crafting_shaped',
)

QUARTZ_STAIRS_FROM_QUARTZ_BLOCK_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:quartz_block',
    result=ItemStackOfComponent(id='minecraft:quartz_stairs'),
    type='minecraft:stonecutting',
)

RABBIT_STEW_FROM_BROWN_MUSHROOM = RecipeCraftingShapeless(
    group='rabbit_stew',
    ingredients=[
        'minecraft:baked_potato',
        'minecraft:cooked_rabbit',
        'minecraft:bowl',
        'minecraft:carrot',
        'minecraft:brown_mushroom',
    ],
    result=ItemStackOfComponent(id='minecraft:rabbit_stew'),
    type='minecraft:crafting_shapeless',
)

RABBIT_STEW_FROM_RED_MUSHROOM = RecipeCraftingShapeless(
    group='rabbit_stew',
    ingredients=[
        'minecraft:baked_potato',
        'minecraft:cooked_rabbit',
        'minecraft:bowl',
        'minecraft:carrot',
        'minecraft:red_mushroom',
    ],
    result=ItemStackOfComponent(id='minecraft:rabbit_stew'),
    type='minecraft:crafting_shapeless',
)

RABBIT_STEW_FROM_SHELF_MUSHROOM = RecipeCraftingShapeless(
    group='rabbit_stew',
    ingredients=[
        'minecraft:baked_potato',
        'minecraft:cooked_rabbit',
        'minecraft:bowl',
        'minecraft:carrot',
        'minecraft:shelf_mushroom',
    ],
    result=ItemStackOfComponent(id='minecraft:rabbit_stew'),
    type='minecraft:crafting_shapeless',
)

RAIL = RecipeCraftingShaped(
    pattern=['X X', 'X#X', 'X X'],
    key={'#': 'minecraft:stick', 'X': 'minecraft:iron_ingot'},
    result=ItemStackOfComponent(id='minecraft:rail', count=16),
    type='minecraft:crafting_shaped',
)

RAISER_ARMOR_TRIM_SMITHING_TEMPLATE = RecipeCraftingShaped(
    pattern=['#S#', '#C#', '###'],
    key={'#': 'minecraft:diamond', 'C': 'minecraft:terracotta', 'S': 'minecraft:raiser_armor_trim_smithing_template'},
    result=ItemStackOfComponent(id='minecraft:raiser_armor_trim_smithing_template', count=2),
    type='minecraft:crafting_shaped',
)

RAISER_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = RecipeSmithingTrim(
    base='#minecraft:trimmable_armor',
    addition='#minecraft:trim_materials',
    template='minecraft:raiser_armor_trim_smithing_template',
    pattern='minecraft:raiser',
    type='minecraft:smithing_trim',
)

RAW_COPPER = RecipeCraftingShapeless(
    ingredients=['minecraft:raw_copper_block'],
    result=ItemStackOfComponent(id='minecraft:raw_copper', count=9),
    type='minecraft:crafting_shapeless',
)

RAW_COPPER_BLOCK = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '###', '###'],
    key={'#': 'minecraft:raw_copper'},
    result=ItemStackOfComponent(id='minecraft:raw_copper_block'),
    type='minecraft:crafting_shaped',
)

RAW_GOLD = RecipeCraftingShapeless(
    ingredients=['minecraft:raw_gold_block'],
    result=ItemStackOfComponent(id='minecraft:raw_gold', count=9),
    type='minecraft:crafting_shapeless',
)

RAW_GOLD_BLOCK = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '###', '###'],
    key={'#': 'minecraft:raw_gold'},
    result=ItemStackOfComponent(id='minecraft:raw_gold_block'),
    type='minecraft:crafting_shaped',
)

RAW_IRON = RecipeCraftingShapeless(
    ingredients=['minecraft:raw_iron_block'],
    result=ItemStackOfComponent(id='minecraft:raw_iron', count=9),
    type='minecraft:crafting_shapeless',
)

RAW_IRON_BLOCK = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '###', '###'],
    key={'#': 'minecraft:raw_iron'},
    result=ItemStackOfComponent(id='minecraft:raw_iron_block'),
    type='minecraft:crafting_shaped',
)

RECOVERY_COMPASS = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['SSS', 'SCS', 'SSS'],
    key={'C': 'minecraft:compass', 'S': 'minecraft:echo_shard'},
    result=ItemStackOfComponent(id='minecraft:recovery_compass'),
    type='minecraft:crafting_shaped',
)

REDSTONE = RecipeCraftingShapeless(
    category=CraftingBookCategory.REDSTONE,
    ingredients=['minecraft:redstone_block'],
    result=ItemStackOfComponent(id='minecraft:redstone', count=9),
    type='minecraft:crafting_shapeless',
)

REDSTONE_BLOCK = RecipeCraftingShaped(
    category=CraftingBookCategory.REDSTONE,
    pattern=['###', '###', '###'],
    key={'#': 'minecraft:redstone'},
    result=ItemStackOfComponent(id='minecraft:redstone_block'),
    type='minecraft:crafting_shaped',
)

REDSTONE_FROM_BLASTING_DEEPSLATE_REDSTONE_ORE = RecipeBlasting(
    group='redstone',
    category=CookingBookCategory.BLOCKS,
    ingredient='minecraft:deepslate_redstone_ore',
    result=ItemStackOfComponent(id='minecraft:redstone'),
    experience=0.7,
    cookingtime=200,
    type='minecraft:blasting',
)

REDSTONE_FROM_BLASTING_REDSTONE_ORE = RecipeBlasting(
    group='redstone',
    category=CookingBookCategory.BLOCKS,
    ingredient='minecraft:redstone_ore',
    result=ItemStackOfComponent(id='minecraft:redstone'),
    experience=0.7,
    cookingtime=200,
    type='minecraft:blasting',
)

REDSTONE_FROM_SMELTING_DEEPSLATE_REDSTONE_ORE = RecipeSmelting(
    group='redstone',
    category=CookingBookCategory.BLOCKS,
    ingredient='minecraft:deepslate_redstone_ore',
    result=ItemStackOfComponent(id='minecraft:redstone'),
    experience=0.7,
    cookingtime=200,
    type='minecraft:smelting',
)

REDSTONE_FROM_SMELTING_REDSTONE_ORE = RecipeSmelting(
    group='redstone',
    category=CookingBookCategory.BLOCKS,
    ingredient='minecraft:redstone_ore',
    result=ItemStackOfComponent(id='minecraft:redstone'),
    experience=0.7,
    cookingtime=200,
    type='minecraft:smelting',
)

REDSTONE_LAMP = RecipeCraftingShaped(
    category=CraftingBookCategory.REDSTONE,
    pattern=[' R ', 'RGR', ' R '],
    key={'G': 'minecraft:glowstone', 'R': 'minecraft:redstone'},
    result=ItemStackOfComponent(id='minecraft:redstone_lamp'),
    type='minecraft:crafting_shaped',
)

REDSTONE_TORCH = RecipeCraftingShaped(
    category=CraftingBookCategory.REDSTONE,
    pattern=['X', '#'],
    key={'#': 'minecraft:stick', 'X': 'minecraft:redstone'},
    result=ItemStackOfComponent(id='minecraft:redstone_torch'),
    type='minecraft:crafting_shaped',
)

RED_BANNER = RecipeCraftingShaped(
    group='banner',
    pattern=['###', '###', ' | '],
    key={'#': 'minecraft:red_wool', '|': 'minecraft:stick'},
    result=ItemStackOfComponent(id='minecraft:red_banner'),
    type='minecraft:crafting_shaped',
)

RED_BANNER_DUPLICATE = RecipeCraftingSpecialBannerduplicate(
    type='minecraft:crafting_special_bannerduplicate',
    **dict[str, Any]({'banner': 'minecraft:red_banner', 'result': {'id': 'minecraft:red_banner'}}),
)

RED_BED = RecipeCraftingShaped(
    group='bed',
    pattern=['###', 'XXX'],
    key={'#': 'minecraft:red_wool', 'X': '#minecraft:planks'},
    result=ItemStackOfComponent(id='minecraft:red_bed'),
    type='minecraft:crafting_shaped',
)

RED_BUNDLE = RecipeCraftingTransmute(
    group='bundle_dye',
    category=CraftingBookCategory.EQUIPMENT,
    input='#minecraft:bundles',
    material='minecraft:red_dye',
    result=TransmuteResult(id='minecraft:red_bundle'),
    type='minecraft:crafting_transmute',
)

RED_CANDLE = RecipeCraftingShapeless(
    group='dyed_candle',
    ingredients=['minecraft:candle', 'minecraft:red_dye'],
    result=ItemStackOfComponent(id='minecraft:red_candle'),
    type='minecraft:crafting_shapeless',
)

RED_CARPET = RecipeCraftingShaped(
    group='woolen_carpet',
    pattern=['##'],
    key={'#': 'minecraft:red_wool'},
    result=ItemStackOfComponent(id='minecraft:red_carpet', count=3),
    type='minecraft:crafting_shaped',
)

RED_CONCRETE_POWDER = RecipeCraftingShapeless(
    group='concrete_powder',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:red_dye',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:gravel',
        'minecraft:gravel',
        'minecraft:gravel',
        'minecraft:gravel',
    ],
    result=ItemStackOfComponent(id='minecraft:red_concrete_powder', count=8),
    type='minecraft:crafting_shapeless',
)

RED_CONCRETE_SLAB = RecipeCraftingShaped(
    group='concrete_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:red_concrete'},
    result=ItemStackOfComponent(id='minecraft:red_concrete_slab', count=6),
    type='minecraft:crafting_shaped',
)

RED_CONCRETE_SLAB_FROM_RED_CONCRETE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:red_concrete',
    result=ItemStackOfComponent(id='minecraft:red_concrete_slab', count=2),
    type='minecraft:stonecutting',
)

RED_CONCRETE_STAIRS = RecipeCraftingShaped(
    group='concrete_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:red_concrete'},
    result=ItemStackOfComponent(id='minecraft:red_concrete_stairs', count=4),
    type='minecraft:crafting_shaped',
)

RED_CONCRETE_STAIRS_FROM_RED_CONCRETE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:red_concrete',
    result=ItemStackOfComponent(id='minecraft:red_concrete_stairs'),
    type='minecraft:stonecutting',
)

RED_CUSHION = RecipeCraftingShaped(
    group='cushion',
    pattern=['###'],
    key={'#': 'minecraft:red_wool_slab'},
    result=ItemStackOfComponent(id='minecraft:red_cushion'),
    type='minecraft:crafting_shaped',
)

RED_DYE_FROM_BEETROOT = RecipeCraftingShapeless(
    group='red_dye',
    ingredients=['minecraft:beetroot'],
    result=ItemStackOfComponent(id='minecraft:red_dye'),
    type='minecraft:crafting_shapeless',
)

RED_DYE_FROM_POPPY = RecipeCraftingShapeless(
    group='red_dye',
    ingredients=['minecraft:poppy'],
    result=ItemStackOfComponent(id='minecraft:red_dye'),
    type='minecraft:crafting_shapeless',
)

RED_DYE_FROM_ROSE_BUSH = RecipeCraftingShapeless(
    group='red_dye',
    ingredients=['minecraft:rose_bush'],
    result=ItemStackOfComponent(id='minecraft:red_dye', count=2),
    type='minecraft:crafting_shapeless',
)

RED_DYE_FROM_TULIP = RecipeCraftingShapeless(
    group='red_dye',
    ingredients=['minecraft:red_tulip'],
    result=ItemStackOfComponent(id='minecraft:red_dye'),
    type='minecraft:crafting_shapeless',
)

RED_GLAZED_TERRACOTTA = RecipeSmelting(
    category=CookingBookCategory.BLOCKS,
    ingredient='minecraft:red_terracotta',
    result=ItemStackOfComponent(id='minecraft:red_glazed_terracotta'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

RED_HARNESS = RecipeCraftingShaped(
    group='harness',
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['LLL', 'G#G'],
    key={'#': 'minecraft:red_wool', 'G': 'minecraft:glass', 'L': 'minecraft:leather'},
    result=ItemStackOfComponent(id='minecraft:red_harness'),
    type='minecraft:crafting_shaped',
)

RED_NETHER_BRICKS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['NW', 'WN'],
    key={'N': 'minecraft:nether_brick', 'W': 'minecraft:nether_wart'},
    result=ItemStackOfComponent(id='minecraft:red_nether_bricks'),
    type='minecraft:crafting_shaped',
)

RED_NETHER_BRICK_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:red_nether_bricks'},
    result=ItemStackOfComponent(id='minecraft:red_nether_brick_slab', count=6),
    type='minecraft:crafting_shaped',
)

RED_NETHER_BRICK_SLAB_FROM_RED_NETHER_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:red_nether_bricks',
    result=ItemStackOfComponent(id='minecraft:red_nether_brick_slab', count=2),
    type='minecraft:stonecutting',
)

RED_NETHER_BRICK_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:red_nether_bricks'},
    result=ItemStackOfComponent(id='minecraft:red_nether_brick_stairs', count=4),
    type='minecraft:crafting_shaped',
)

RED_NETHER_BRICK_STAIRS_FROM_RED_NETHER_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:red_nether_bricks',
    result=ItemStackOfComponent(id='minecraft:red_nether_brick_stairs'),
    type='minecraft:stonecutting',
)

RED_NETHER_BRICK_WALL = RecipeCraftingShaped(
    pattern=['###', '###'],
    key={'#': 'minecraft:red_nether_bricks'},
    result=ItemStackOfComponent(id='minecraft:red_nether_brick_wall', count=6),
    type='minecraft:crafting_shaped',
)

RED_NETHER_BRICK_WALL_FROM_RED_NETHER_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:red_nether_bricks',
    result=ItemStackOfComponent(id='minecraft:red_nether_brick_wall'),
    type='minecraft:stonecutting',
)

RED_SANDSTONE = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:red_sand'},
    result=ItemStackOfComponent(id='minecraft:red_sandstone'),
    type='minecraft:crafting_shaped',
)

RED_SANDSTONE_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': ['minecraft:red_sandstone', 'minecraft:chiseled_red_sandstone']},
    result=ItemStackOfComponent(id='minecraft:red_sandstone_slab', count=6),
    type='minecraft:crafting_shaped',
)

RED_SANDSTONE_SLAB_FROM_RED_SANDSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:red_sandstone',
    result=ItemStackOfComponent(id='minecraft:red_sandstone_slab', count=2),
    type='minecraft:stonecutting',
)

RED_SANDSTONE_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': ['minecraft:red_sandstone', 'minecraft:chiseled_red_sandstone', 'minecraft:cut_red_sandstone']},
    result=ItemStackOfComponent(id='minecraft:red_sandstone_stairs', count=4),
    type='minecraft:crafting_shaped',
)

RED_SANDSTONE_STAIRS_FROM_RED_SANDSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:red_sandstone',
    result=ItemStackOfComponent(id='minecraft:red_sandstone_stairs'),
    type='minecraft:stonecutting',
)

RED_SANDSTONE_WALL = RecipeCraftingShaped(
    pattern=['###', '###'],
    key={'#': 'minecraft:red_sandstone'},
    result=ItemStackOfComponent(id='minecraft:red_sandstone_wall', count=6),
    type='minecraft:crafting_shaped',
)

RED_SANDSTONE_WALL_FROM_RED_SANDSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:red_sandstone',
    result=ItemStackOfComponent(id='minecraft:red_sandstone_wall'),
    type='minecraft:stonecutting',
)

RED_SHULKER_BOX = RecipeCraftingTransmute(
    group='shulker_box_dye',
    input='#minecraft:shulker_boxes',
    material='minecraft:red_dye',
    result=TransmuteResult(id='minecraft:red_shulker_box'),
    type='minecraft:crafting_transmute',
)

RED_STAINED_GLASS = RecipeCraftingShaped(
    group='stained_glass',
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:glass', 'X': 'minecraft:red_dye'},
    result=ItemStackOfComponent(id='minecraft:red_stained_glass', count=8),
    type='minecraft:crafting_shaped',
)

RED_STAINED_GLASS_PANE = RecipeCraftingShaped(
    group='stained_glass_pane',
    pattern=['###', '###'],
    key={'#': 'minecraft:red_stained_glass'},
    result=ItemStackOfComponent(id='minecraft:red_stained_glass_pane', count=16),
    type='minecraft:crafting_shaped',
)

RED_STAINED_GLASS_PANE_FROM_GLASS_PANE = RecipeCraftingShaped(
    group='stained_glass_pane',
    pattern=['###', '#$#', '###'],
    key={'#': 'minecraft:glass_pane', '$': 'minecraft:red_dye'},
    result=ItemStackOfComponent(id='minecraft:red_stained_glass_pane', count=8),
    type='minecraft:crafting_shaped',
)

RED_TERRACOTTA = RecipeCraftingShaped(
    group='stained_terracotta',
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:terracotta', 'X': 'minecraft:red_dye'},
    result=ItemStackOfComponent(id='minecraft:red_terracotta', count=8),
    type='minecraft:crafting_shaped',
)

RED_WOOL_SLAB = RecipeCraftingShaped(
    group='woolen_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:red_wool'},
    result=ItemStackOfComponent(id='minecraft:red_wool_slab', count=6),
    type='minecraft:crafting_shaped',
)

RED_WOOL_STAIRS = RecipeCraftingShaped(
    group='woolen_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:red_wool'},
    result=ItemStackOfComponent(id='minecraft:red_wool_stairs', count=4),
    type='minecraft:crafting_shaped',
)

REPAIR_ITEM = RecipeCraftingSpecialRepairitem(type='minecraft:crafting_special_repairitem')

REPEATER = RecipeCraftingShaped(
    category=CraftingBookCategory.REDSTONE,
    pattern=['#X#', 'III'],
    key={'#': 'minecraft:redstone_torch', 'I': 'minecraft:stone', 'X': 'minecraft:redstone'},
    result=ItemStackOfComponent(id='minecraft:repeater'),
    type='minecraft:crafting_shaped',
)

RESIN_BLOCK = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '###', '###'],
    key={'#': 'minecraft:resin_clump'},
    result=ItemStackOfComponent(id='minecraft:resin_block'),
    type='minecraft:crafting_shaped',
)

RESIN_BRICK = RecipeSmelting(
    ingredient='minecraft:resin_clump',
    result=ItemStackOfComponent(id='minecraft:resin_brick'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

RESIN_BRICKS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:resin_brick'},
    result=ItemStackOfComponent(id='minecraft:resin_bricks'),
    type='minecraft:crafting_shaped',
)

RESIN_BRICK_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:resin_bricks'},
    result=ItemStackOfComponent(id='minecraft:resin_brick_slab', count=6),
    type='minecraft:crafting_shaped',
)

RESIN_BRICK_SLAB_FROM_RESIN_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:resin_bricks',
    result=ItemStackOfComponent(id='minecraft:resin_brick_slab', count=2),
    type='minecraft:stonecutting',
)

RESIN_BRICK_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:resin_bricks'},
    result=ItemStackOfComponent(id='minecraft:resin_brick_stairs', count=4),
    type='minecraft:crafting_shaped',
)

RESIN_BRICK_STAIRS_FROM_RESIN_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:resin_bricks',
    result=ItemStackOfComponent(id='minecraft:resin_brick_stairs'),
    type='minecraft:stonecutting',
)

RESIN_BRICK_WALL = RecipeCraftingShaped(
    pattern=['###', '###'],
    key={'#': 'minecraft:resin_bricks'},
    result=ItemStackOfComponent(id='minecraft:resin_brick_wall', count=6),
    type='minecraft:crafting_shaped',
)

RESIN_BRICK_WALL_FROM_RESIN_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:resin_bricks',
    result=ItemStackOfComponent(id='minecraft:resin_brick_wall'),
    type='minecraft:stonecutting',
)

RESIN_CLUMP = RecipeCraftingShapeless(
    ingredients=['minecraft:resin_block'],
    result=ItemStackOfComponent(id='minecraft:resin_clump', count=9),
    type='minecraft:crafting_shapeless',
)

RESPAWN_ANCHOR = RecipeCraftingShaped(
    pattern=['OOO', 'GGG', 'OOO'],
    key={'G': 'minecraft:glowstone', 'O': 'minecraft:crying_obsidian'},
    result=ItemStackOfComponent(id='minecraft:respawn_anchor'),
    type='minecraft:crafting_shaped',
)

RIB_ARMOR_TRIM_SMITHING_TEMPLATE = RecipeCraftingShaped(
    pattern=['#S#', '#C#', '###'],
    key={'#': 'minecraft:diamond', 'C': 'minecraft:netherrack', 'S': 'minecraft:rib_armor_trim_smithing_template'},
    result=ItemStackOfComponent(id='minecraft:rib_armor_trim_smithing_template', count=2),
    type='minecraft:crafting_shaped',
)

RIB_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = RecipeSmithingTrim(
    base='#minecraft:trimmable_armor',
    addition='#minecraft:trim_materials',
    template='minecraft:rib_armor_trim_smithing_template',
    pattern='minecraft:rib',
    type='minecraft:smithing_trim',
)

SADDLE = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=[' X ', 'X#X'],
    key={'#': 'minecraft:iron_ingot', 'X': 'minecraft:leather'},
    result=ItemStackOfComponent(id='minecraft:saddle'),
    type='minecraft:crafting_shaped',
)

SANDSTONE = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:sand'},
    result=ItemStackOfComponent(id='minecraft:sandstone'),
    type='minecraft:crafting_shaped',
)

SANDSTONE_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': ['minecraft:sandstone', 'minecraft:chiseled_sandstone']},
    result=ItemStackOfComponent(id='minecraft:sandstone_slab', count=6),
    type='minecraft:crafting_shaped',
)

SANDSTONE_SLAB_FROM_SANDSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:sandstone',
    result=ItemStackOfComponent(id='minecraft:sandstone_slab', count=2),
    type='minecraft:stonecutting',
)

SANDSTONE_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': ['minecraft:sandstone', 'minecraft:chiseled_sandstone', 'minecraft:cut_sandstone']},
    result=ItemStackOfComponent(id='minecraft:sandstone_stairs', count=4),
    type='minecraft:crafting_shaped',
)

SANDSTONE_STAIRS_FROM_SANDSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:sandstone',
    result=ItemStackOfComponent(id='minecraft:sandstone_stairs'),
    type='minecraft:stonecutting',
)

SANDSTONE_WALL = RecipeCraftingShaped(
    pattern=['###', '###'],
    key={'#': 'minecraft:sandstone'},
    result=ItemStackOfComponent(id='minecraft:sandstone_wall', count=6),
    type='minecraft:crafting_shaped',
)

SANDSTONE_WALL_FROM_SANDSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:sandstone',
    result=ItemStackOfComponent(id='minecraft:sandstone_wall'),
    type='minecraft:stonecutting',
)

SCAFFOLDING = RecipeCraftingShaped(
    pattern=['I~I', 'I I', 'I I'],
    key={'I': 'minecraft:bamboo', '~': 'minecraft:string'},
    result=ItemStackOfComponent(id='minecraft:scaffolding', count=6),
    type='minecraft:crafting_shaped',
)

SEA_LANTERN = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['SCS', 'CCC', 'SCS'],
    key={'C': 'minecraft:prismarine_crystals', 'S': 'minecraft:prismarine_shard'},
    result=ItemStackOfComponent(id='minecraft:sea_lantern'),
    type='minecraft:crafting_shaped',
)

SENTRY_ARMOR_TRIM_SMITHING_TEMPLATE = RecipeCraftingShaped(
    pattern=['#S#', '#C#', '###'],
    key={'#': 'minecraft:diamond', 'C': 'minecraft:cobblestone', 'S': 'minecraft:sentry_armor_trim_smithing_template'},
    result=ItemStackOfComponent(id='minecraft:sentry_armor_trim_smithing_template', count=2),
    type='minecraft:crafting_shaped',
)

SENTRY_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = RecipeSmithingTrim(
    base='#minecraft:trimmable_armor',
    addition='#minecraft:trim_materials',
    template='minecraft:sentry_armor_trim_smithing_template',
    pattern='minecraft:sentry',
    type='minecraft:smithing_trim',
)

SHAPER_ARMOR_TRIM_SMITHING_TEMPLATE = RecipeCraftingShaped(
    pattern=['#S#', '#C#', '###'],
    key={'#': 'minecraft:diamond', 'C': 'minecraft:terracotta', 'S': 'minecraft:shaper_armor_trim_smithing_template'},
    result=ItemStackOfComponent(id='minecraft:shaper_armor_trim_smithing_template', count=2),
    type='minecraft:crafting_shaped',
)

SHAPER_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = RecipeSmithingTrim(
    base='#minecraft:trimmable_armor',
    addition='#minecraft:trim_materials',
    template='minecraft:shaper_armor_trim_smithing_template',
    pattern='minecraft:shaper',
    type='minecraft:smithing_trim',
)

SHEARS = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=[' #', '# '],
    key={'#': 'minecraft:iron_ingot'},
    result=ItemStackOfComponent(id='minecraft:shears'),
    type='minecraft:crafting_shaped',
)

SHIELD = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['WoW', 'WWW', ' W '],
    key={'W': '#minecraft:wooden_tool_materials', 'o': 'minecraft:iron_ingot'},
    result=ItemStackOfComponent(id='minecraft:shield'),
    type='minecraft:crafting_shaped',
)

SHIELD_DECORATION = RecipeCraftingSpecialShielddecoration(
    type='minecraft:crafting_special_shielddecoration',
    **dict[str, Any]({'banner': '#minecraft:banners', 'result': {'id': 'minecraft:shield'}, 'target': 'minecraft:shield'}),
)

SHULKER_BOX = RecipeCraftingShaped(
    pattern=['-', '#', '-'],
    key={'#': 'minecraft:chest', '-': 'minecraft:shulker_shell'},
    result=ItemStackOfComponent(id='minecraft:shulker_box'),
    type='minecraft:crafting_shaped',
)

SILENCE_ARMOR_TRIM_SMITHING_TEMPLATE = RecipeCraftingShaped(
    pattern=['#S#', '#C#', '###'],
    key={
        '#': 'minecraft:diamond',
        'C': 'minecraft:cobbled_deepslate',
        'S': 'minecraft:silence_armor_trim_smithing_template',
    },
    result=ItemStackOfComponent(id='minecraft:silence_armor_trim_smithing_template', count=2),
    type='minecraft:crafting_shaped',
)

SILENCE_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = RecipeSmithingTrim(
    base='#minecraft:trimmable_armor',
    addition='#minecraft:trim_materials',
    template='minecraft:silence_armor_trim_smithing_template',
    pattern='minecraft:silence',
    type='minecraft:smithing_trim',
)

SKULL_BANNER_PATTERN = RecipeCraftingShapeless(
    ingredients=['minecraft:paper', 'minecraft:wither_skeleton_skull'],
    result=ItemStackOfComponent(id='minecraft:skull_banner_pattern'),
    type='minecraft:crafting_shapeless',
)

SLIME_BALL = RecipeCraftingShapeless(
    ingredients=['minecraft:slime_block'],
    result=ItemStackOfComponent(id='minecraft:slime_ball', count=9),
    type='minecraft:crafting_shapeless',
)

SLIME_BLOCK = RecipeCraftingShaped(
    category=CraftingBookCategory.REDSTONE,
    pattern=['###', '###', '###'],
    key={'#': 'minecraft:slime_ball'},
    result=ItemStackOfComponent(id='minecraft:slime_block'),
    type='minecraft:crafting_shaped',
)

SMITHING_TABLE = RecipeCraftingShaped(
    pattern=['@@', '##', '##'],
    key={'#': '#minecraft:planks', '@': 'minecraft:iron_ingot'},
    result=ItemStackOfComponent(id='minecraft:smithing_table'),
    type='minecraft:crafting_shaped',
)

SMOKER = RecipeCraftingShaped(
    pattern=[' # ', '#X#', ' # '],
    key={'#': '#minecraft:logs', 'X': 'minecraft:furnace'},
    result=ItemStackOfComponent(id='minecraft:smoker'),
    type='minecraft:crafting_shaped',
)

SMOOTH_BASALT = RecipeSmelting(
    category=CookingBookCategory.BLOCKS,
    ingredient='minecraft:basalt',
    result=ItemStackOfComponent(id='minecraft:smooth_basalt'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

SMOOTH_QUARTZ = RecipeSmelting(
    category=CookingBookCategory.BLOCKS,
    ingredient='minecraft:quartz_block',
    result=ItemStackOfComponent(id='minecraft:smooth_quartz'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

SMOOTH_QUARTZ_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:smooth_quartz'},
    result=ItemStackOfComponent(id='minecraft:smooth_quartz_slab', count=6),
    type='minecraft:crafting_shaped',
)

SMOOTH_QUARTZ_SLAB_FROM_SMOOTH_QUARTZ_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:smooth_quartz',
    result=ItemStackOfComponent(id='minecraft:smooth_quartz_slab', count=2),
    type='minecraft:stonecutting',
)

SMOOTH_QUARTZ_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:smooth_quartz'},
    result=ItemStackOfComponent(id='minecraft:smooth_quartz_stairs', count=4),
    type='minecraft:crafting_shaped',
)

SMOOTH_QUARTZ_STAIRS_FROM_SMOOTH_QUARTZ_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:smooth_quartz',
    result=ItemStackOfComponent(id='minecraft:smooth_quartz_stairs'),
    type='minecraft:stonecutting',
)

SMOOTH_RED_SANDSTONE = RecipeSmelting(
    category=CookingBookCategory.BLOCKS,
    ingredient='minecraft:red_sandstone',
    result=ItemStackOfComponent(id='minecraft:smooth_red_sandstone'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

SMOOTH_RED_SANDSTONE_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:smooth_red_sandstone'},
    result=ItemStackOfComponent(id='minecraft:smooth_red_sandstone_slab', count=6),
    type='minecraft:crafting_shaped',
)

SMOOTH_RED_SANDSTONE_SLAB_FROM_SMOOTH_RED_SANDSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:smooth_red_sandstone',
    result=ItemStackOfComponent(id='minecraft:smooth_red_sandstone_slab', count=2),
    type='minecraft:stonecutting',
)

SMOOTH_RED_SANDSTONE_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:smooth_red_sandstone'},
    result=ItemStackOfComponent(id='minecraft:smooth_red_sandstone_stairs', count=4),
    type='minecraft:crafting_shaped',
)

SMOOTH_RED_SANDSTONE_STAIRS_FROM_SMOOTH_RED_SANDSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:smooth_red_sandstone',
    result=ItemStackOfComponent(id='minecraft:smooth_red_sandstone_stairs'),
    type='minecraft:stonecutting',
)

SMOOTH_SANDSTONE = RecipeSmelting(
    category=CookingBookCategory.BLOCKS,
    ingredient='minecraft:sandstone',
    result=ItemStackOfComponent(id='minecraft:smooth_sandstone'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

SMOOTH_SANDSTONE_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:smooth_sandstone'},
    result=ItemStackOfComponent(id='minecraft:smooth_sandstone_slab', count=6),
    type='minecraft:crafting_shaped',
)

SMOOTH_SANDSTONE_SLAB_FROM_SMOOTH_SANDSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:smooth_sandstone',
    result=ItemStackOfComponent(id='minecraft:smooth_sandstone_slab', count=2),
    type='minecraft:stonecutting',
)

SMOOTH_SANDSTONE_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:smooth_sandstone'},
    result=ItemStackOfComponent(id='minecraft:smooth_sandstone_stairs', count=4),
    type='minecraft:crafting_shaped',
)

SMOOTH_SANDSTONE_STAIRS_FROM_SMOOTH_SANDSTONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:smooth_sandstone',
    result=ItemStackOfComponent(id='minecraft:smooth_sandstone_stairs'),
    type='minecraft:stonecutting',
)

SMOOTH_STONE = RecipeSmelting(
    category=CookingBookCategory.BLOCKS,
    ingredient='minecraft:stone',
    result=ItemStackOfComponent(id='minecraft:smooth_stone'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

SMOOTH_STONE_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:smooth_stone'},
    result=ItemStackOfComponent(id='minecraft:smooth_stone_slab', count=6),
    type='minecraft:crafting_shaped',
)

SMOOTH_STONE_SLAB_FROM_SMOOTH_STONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:smooth_stone',
    result=ItemStackOfComponent(id='minecraft:smooth_stone_slab', count=2),
    type='minecraft:stonecutting',
)

SNOUT_ARMOR_TRIM_SMITHING_TEMPLATE = RecipeCraftingShaped(
    pattern=['#S#', '#C#', '###'],
    key={'#': 'minecraft:diamond', 'C': 'minecraft:blackstone', 'S': 'minecraft:snout_armor_trim_smithing_template'},
    result=ItemStackOfComponent(id='minecraft:snout_armor_trim_smithing_template', count=2),
    type='minecraft:crafting_shaped',
)

SNOUT_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = RecipeSmithingTrim(
    base='#minecraft:trimmable_armor',
    addition='#minecraft:trim_materials',
    template='minecraft:snout_armor_trim_smithing_template',
    pattern='minecraft:snout',
    type='minecraft:smithing_trim',
)

SNOW = RecipeCraftingShaped(
    pattern=['###'],
    key={'#': 'minecraft:snow_block'},
    result=ItemStackOfComponent(id='minecraft:snow', count=6),
    type='minecraft:crafting_shaped',
)

SNOW_BLOCK = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:snowball'},
    result=ItemStackOfComponent(id='minecraft:snow_block'),
    type='minecraft:crafting_shaped',
)

SOUL_CAMPFIRE = RecipeCraftingShaped(
    pattern=[' S ', 'S#S', 'LLL'],
    key={'#': '#minecraft:soul_fire_base_blocks', 'L': '#minecraft:logs', 'S': 'minecraft:stick'},
    result=ItemStackOfComponent(id='minecraft:soul_campfire'),
    type='minecraft:crafting_shaped',
)

SOUL_LANTERN = RecipeCraftingShaped(
    pattern=['XXX', 'X#X', 'XXX'],
    key={'#': 'minecraft:soul_torch', 'X': 'minecraft:iron_nugget'},
    result=ItemStackOfComponent(id='minecraft:soul_lantern'),
    type='minecraft:crafting_shaped',
)

SOUL_TORCH = RecipeCraftingShaped(
    pattern=['X', '#', 'S'],
    key={'#': 'minecraft:stick', 'S': '#minecraft:soul_fire_base_blocks', 'X': ['minecraft:coal', 'minecraft:charcoal']},
    result=ItemStackOfComponent(id='minecraft:soul_torch', count=4),
    type='minecraft:crafting_shaped',
)

SPECTRAL_ARROW = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=[' # ', '#X#', ' # '],
    key={'#': 'minecraft:glowstone_dust', 'X': 'minecraft:arrow'},
    result=ItemStackOfComponent(id='minecraft:spectral_arrow', count=2),
    type='minecraft:crafting_shaped',
)

SPIRE_ARMOR_TRIM_SMITHING_TEMPLATE = RecipeCraftingShaped(
    pattern=['#S#', '#C#', '###'],
    key={'#': 'minecraft:diamond', 'C': 'minecraft:purpur_block', 'S': 'minecraft:spire_armor_trim_smithing_template'},
    result=ItemStackOfComponent(id='minecraft:spire_armor_trim_smithing_template', count=2),
    type='minecraft:crafting_shaped',
)

SPIRE_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = RecipeSmithingTrim(
    base='#minecraft:trimmable_armor',
    addition='#minecraft:trim_materials',
    template='minecraft:spire_armor_trim_smithing_template',
    pattern='minecraft:spire',
    type='minecraft:smithing_trim',
)

SPONGE = RecipeSmelting(
    category=CookingBookCategory.BLOCKS,
    ingredient='minecraft:wet_sponge',
    result=ItemStackOfComponent(id='minecraft:sponge'),
    experience=0.15,
    cookingtime=200,
    type='minecraft:smelting',
)

SPRUCE_BOAT = RecipeCraftingShaped(
    group='boat',
    pattern=['# #', '###'],
    key={'#': 'minecraft:spruce_planks'},
    result=ItemStackOfComponent(id='minecraft:spruce_boat'),
    type='minecraft:crafting_shaped',
)

SPRUCE_BUTTON = RecipeCraftingShapeless(
    group='wooden_button',
    category=CraftingBookCategory.REDSTONE,
    ingredients=['minecraft:spruce_planks'],
    result=ItemStackOfComponent(id='minecraft:spruce_button'),
    type='minecraft:crafting_shapeless',
)

SPRUCE_CHEST_BOAT = RecipeCraftingShapeless(
    group='chest_boat',
    ingredients=['minecraft:chest', 'minecraft:spruce_boat'],
    result=ItemStackOfComponent(id='minecraft:spruce_chest_boat'),
    type='minecraft:crafting_shapeless',
)

SPRUCE_DOOR = RecipeCraftingShaped(
    group='wooden_door',
    category=CraftingBookCategory.REDSTONE,
    pattern=['##', '##', '##'],
    key={'#': 'minecraft:spruce_planks'},
    result=ItemStackOfComponent(id='minecraft:spruce_door', count=3),
    type='minecraft:crafting_shaped',
)

SPRUCE_FENCE = RecipeCraftingShaped(
    group='wooden_fence',
    pattern=['W#W', 'W#W'],
    key={'#': 'minecraft:stick', 'W': 'minecraft:spruce_planks'},
    result=ItemStackOfComponent(id='minecraft:spruce_fence', count=3),
    type='minecraft:crafting_shaped',
)

SPRUCE_FENCE_GATE = RecipeCraftingShaped(
    group='wooden_fence_gate',
    category=CraftingBookCategory.REDSTONE,
    pattern=['#W#', '#W#'],
    key={'#': 'minecraft:stick', 'W': 'minecraft:spruce_planks'},
    result=ItemStackOfComponent(id='minecraft:spruce_fence_gate'),
    type='minecraft:crafting_shaped',
)

SPRUCE_HANGING_SIGN = RecipeCraftingShaped(
    group='wooden_hanging_sign',
    pattern=['X X', '###', '###'],
    key={'#': 'minecraft:stripped_spruce_log', 'X': 'minecraft:iron_chain'},
    result=ItemStackOfComponent(id='minecraft:spruce_hanging_sign', count=6),
    type='minecraft:crafting_shaped',
)

SPRUCE_PLANKS = RecipeCraftingShapeless(
    group='planks',
    category=CraftingBookCategory.BUILDING,
    ingredients=['#minecraft:spruce_logs'],
    result=ItemStackOfComponent(id='minecraft:spruce_planks', count=4),
    type='minecraft:crafting_shapeless',
)

SPRUCE_PRESSURE_PLATE = RecipeCraftingShaped(
    group='wooden_pressure_plate',
    category=CraftingBookCategory.REDSTONE,
    pattern=['##'],
    key={'#': 'minecraft:spruce_planks'},
    result=ItemStackOfComponent(id='minecraft:spruce_pressure_plate'),
    type='minecraft:crafting_shaped',
)

SPRUCE_SHELF = RecipeCraftingShaped(
    group='shelf',
    pattern=['###', '   ', '###'],
    key={'#': 'minecraft:stripped_spruce_log'},
    result=ItemStackOfComponent(id='minecraft:spruce_shelf', count=6),
    type='minecraft:crafting_shaped',
)

SPRUCE_SIGN = RecipeCraftingShaped(
    group='wooden_sign',
    pattern=['###', '###', ' X '],
    key={'#': 'minecraft:spruce_planks', 'X': 'minecraft:stick'},
    result=ItemStackOfComponent(id='minecraft:spruce_sign', count=3),
    type='minecraft:crafting_shaped',
)

SPRUCE_SLAB = RecipeCraftingShaped(
    group='wooden_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:spruce_planks'},
    result=ItemStackOfComponent(id='minecraft:spruce_slab', count=6),
    type='minecraft:crafting_shaped',
)

SPRUCE_STAIRS = RecipeCraftingShaped(
    group='wooden_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:spruce_planks'},
    result=ItemStackOfComponent(id='minecraft:spruce_stairs', count=4),
    type='minecraft:crafting_shaped',
)

SPRUCE_TRAPDOOR = RecipeCraftingShaped(
    group='wooden_trapdoor',
    category=CraftingBookCategory.REDSTONE,
    pattern=['###', '###'],
    key={'#': 'minecraft:spruce_planks'},
    result=ItemStackOfComponent(id='minecraft:spruce_trapdoor', count=2),
    type='minecraft:crafting_shaped',
)

SPRUCE_WOOD = RecipeCraftingShaped(
    group='bark',
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:spruce_log'},
    result=ItemStackOfComponent(id='minecraft:spruce_wood', count=3),
    type='minecraft:crafting_shaped',
)

SPYGLASS = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=[' # ', ' X ', ' X '],
    key={'#': 'minecraft:amethyst_shard', 'X': 'minecraft:copper_ingot'},
    result=ItemStackOfComponent(id='minecraft:spyglass'),
    type='minecraft:crafting_shaped',
)

STICK = RecipeCraftingShaped(
    group='sticks',
    pattern=['#', '#'],
    key={'#': '#minecraft:planks'},
    result=ItemStackOfComponent(id='minecraft:stick', count=4),
    type='minecraft:crafting_shaped',
)

STICKY_PISTON = RecipeCraftingShaped(
    category=CraftingBookCategory.REDSTONE,
    pattern=['S', 'P'],
    key={'P': 'minecraft:piston', 'S': 'minecraft:slime_ball'},
    result=ItemStackOfComponent(id='minecraft:sticky_piston'),
    type='minecraft:crafting_shaped',
)

STICK_FROM_BAMBOO_ITEM = RecipeCraftingShaped(
    group='sticks',
    pattern=['#', '#'],
    key={'#': 'minecraft:bamboo'},
    result=ItemStackOfComponent(id='minecraft:stick'),
    type='minecraft:crafting_shaped',
)

STONE = RecipeSmelting(
    category=CookingBookCategory.BLOCKS,
    ingredient='minecraft:cobblestone',
    result=ItemStackOfComponent(id='minecraft:stone'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

STONECUTTER = RecipeCraftingShaped(
    pattern=[' I ', '###'],
    key={'#': 'minecraft:stone', 'I': 'minecraft:iron_ingot'},
    result=ItemStackOfComponent(id='minecraft:stonecutter'),
    type='minecraft:crafting_shaped',
)

STONE_AXE = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['XX', 'X#', ' #'],
    key={'#': 'minecraft:stick', 'X': '#minecraft:stone_tool_materials'},
    result=ItemStackOfComponent(id='minecraft:stone_axe'),
    type='minecraft:crafting_shaped',
)

STONE_BRICKS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:stone'},
    result=ItemStackOfComponent(id='minecraft:stone_bricks', count=4),
    type='minecraft:crafting_shaped',
)

STONE_BRICKS_FROM_STONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:stone',
    result=ItemStackOfComponent(id='minecraft:stone_bricks'),
    type='minecraft:stonecutting',
)

STONE_BRICK_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:stone_bricks'},
    result=ItemStackOfComponent(id='minecraft:stone_brick_slab', count=6),
    type='minecraft:crafting_shaped',
)

STONE_BRICK_SLAB_FROM_STONE_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:stone_bricks',
    result=ItemStackOfComponent(id='minecraft:stone_brick_slab', count=2),
    type='minecraft:stonecutting',
)

STONE_BRICK_SLAB_FROM_STONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:stone',
    result=ItemStackOfComponent(id='minecraft:stone_brick_slab', count=2),
    type='minecraft:stonecutting',
)

STONE_BRICK_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:stone_bricks'},
    result=ItemStackOfComponent(id='minecraft:stone_brick_stairs', count=4),
    type='minecraft:crafting_shaped',
)

STONE_BRICK_STAIRS_FROM_STONE_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:stone_bricks',
    result=ItemStackOfComponent(id='minecraft:stone_brick_stairs'),
    type='minecraft:stonecutting',
)

STONE_BRICK_STAIRS_FROM_STONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:stone',
    result=ItemStackOfComponent(id='minecraft:stone_brick_stairs'),
    type='minecraft:stonecutting',
)

STONE_BRICK_WALL = RecipeCraftingShaped(
    pattern=['###', '###'],
    key={'#': 'minecraft:stone_bricks'},
    result=ItemStackOfComponent(id='minecraft:stone_brick_wall', count=6),
    type='minecraft:crafting_shaped',
)

STONE_BRICK_WALL_FROM_STONE_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:stone_bricks',
    result=ItemStackOfComponent(id='minecraft:stone_brick_wall'),
    type='minecraft:stonecutting',
)

STONE_BRICK_WALL_FROM_STONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:stone',
    result=ItemStackOfComponent(id='minecraft:stone_brick_wall'),
    type='minecraft:stonecutting',
)

STONE_BUTTON = RecipeCraftingShapeless(
    category=CraftingBookCategory.REDSTONE,
    ingredients=['minecraft:stone'],
    result=ItemStackOfComponent(id='minecraft:stone_button'),
    type='minecraft:crafting_shapeless',
)

STONE_HOE = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['XX', ' #', ' #'],
    key={'#': 'minecraft:stick', 'X': '#minecraft:stone_tool_materials'},
    result=ItemStackOfComponent(id='minecraft:stone_hoe'),
    type='minecraft:crafting_shaped',
)

STONE_PICKAXE = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['XXX', ' # ', ' # '],
    key={'#': 'minecraft:stick', 'X': '#minecraft:stone_tool_materials'},
    result=ItemStackOfComponent(id='minecraft:stone_pickaxe'),
    type='minecraft:crafting_shaped',
)

STONE_PRESSURE_PLATE = RecipeCraftingShaped(
    category=CraftingBookCategory.REDSTONE,
    pattern=['##'],
    key={'#': 'minecraft:stone'},
    result=ItemStackOfComponent(id='minecraft:stone_pressure_plate'),
    type='minecraft:crafting_shaped',
)

STONE_SHOVEL = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['X', '#', '#'],
    key={'#': 'minecraft:stick', 'X': '#minecraft:stone_tool_materials'},
    result=ItemStackOfComponent(id='minecraft:stone_shovel'),
    type='minecraft:crafting_shaped',
)

STONE_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:stone'},
    result=ItemStackOfComponent(id='minecraft:stone_slab', count=6),
    type='minecraft:crafting_shaped',
)

STONE_SLAB_FROM_STONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:stone',
    result=ItemStackOfComponent(id='minecraft:stone_slab', count=2),
    type='minecraft:stonecutting',
)

STONE_SPEAR = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['  X', ' # ', '#  '],
    key={'#': 'minecraft:stick', 'X': '#minecraft:stone_tool_materials'},
    result=ItemStackOfComponent(id='minecraft:stone_spear'),
    type='minecraft:crafting_shaped',
)

STONE_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:stone'},
    result=ItemStackOfComponent(id='minecraft:stone_stairs', count=4),
    type='minecraft:crafting_shaped',
)

STONE_STAIRS_FROM_STONE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:stone',
    result=ItemStackOfComponent(id='minecraft:stone_stairs'),
    type='minecraft:stonecutting',
)

STONE_SWORD = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['X', 'X', '#'],
    key={'#': 'minecraft:stick', 'X': '#minecraft:stone_tool_materials'},
    result=ItemStackOfComponent(id='minecraft:stone_sword'),
    type='minecraft:crafting_shaped',
)

STRAW_BED = RecipeCraftingShaped(
    pattern=['XXX'],
    key={'X': 'minecraft:hay_block'},
    result=ItemStackOfComponent(id='minecraft:straw_bed', count=4),
    type='minecraft:crafting_shaped',
)

STRIPPED_ACACIA_WOOD = RecipeCraftingShaped(
    group='bark',
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:stripped_acacia_log'},
    result=ItemStackOfComponent(id='minecraft:stripped_acacia_wood', count=3),
    type='minecraft:crafting_shaped',
)

STRIPPED_BIRCH_WOOD = RecipeCraftingShaped(
    group='bark',
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:stripped_birch_log'},
    result=ItemStackOfComponent(id='minecraft:stripped_birch_wood', count=3),
    type='minecraft:crafting_shaped',
)

STRIPPED_CHERRY_WOOD = RecipeCraftingShaped(
    group='bark',
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:stripped_cherry_log'},
    result=ItemStackOfComponent(id='minecraft:stripped_cherry_wood', count=3),
    type='minecraft:crafting_shaped',
)

STRIPPED_CRIMSON_HYPHAE = RecipeCraftingShaped(
    group='bark',
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:stripped_crimson_stem'},
    result=ItemStackOfComponent(id='minecraft:stripped_crimson_hyphae', count=3),
    type='minecraft:crafting_shaped',
)

STRIPPED_DARK_OAK_WOOD = RecipeCraftingShaped(
    group='bark',
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:stripped_dark_oak_log'},
    result=ItemStackOfComponent(id='minecraft:stripped_dark_oak_wood', count=3),
    type='minecraft:crafting_shaped',
)

STRIPPED_JUNGLE_WOOD = RecipeCraftingShaped(
    group='bark',
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:stripped_jungle_log'},
    result=ItemStackOfComponent(id='minecraft:stripped_jungle_wood', count=3),
    type='minecraft:crafting_shaped',
)

STRIPPED_MANGROVE_WOOD = RecipeCraftingShaped(
    group='bark',
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:stripped_mangrove_log'},
    result=ItemStackOfComponent(id='minecraft:stripped_mangrove_wood', count=3),
    type='minecraft:crafting_shaped',
)

STRIPPED_OAK_WOOD = RecipeCraftingShaped(
    group='bark',
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:stripped_oak_log'},
    result=ItemStackOfComponent(id='minecraft:stripped_oak_wood', count=3),
    type='minecraft:crafting_shaped',
)

STRIPPED_PALE_OAK_WOOD = RecipeCraftingShaped(
    group='bark',
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:stripped_pale_oak_log'},
    result=ItemStackOfComponent(id='minecraft:stripped_pale_oak_wood', count=3),
    type='minecraft:crafting_shaped',
)

STRIPPED_POPLAR_WOOD = RecipeCraftingShaped(
    group='bark',
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:stripped_poplar_log'},
    result=ItemStackOfComponent(id='minecraft:stripped_poplar_wood', count=3),
    type='minecraft:crafting_shaped',
)

STRIPPED_SPRUCE_WOOD = RecipeCraftingShaped(
    group='bark',
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:stripped_spruce_log'},
    result=ItemStackOfComponent(id='minecraft:stripped_spruce_wood', count=3),
    type='minecraft:crafting_shaped',
)

STRIPPED_WARPED_HYPHAE = RecipeCraftingShaped(
    group='bark',
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:stripped_warped_stem'},
    result=ItemStackOfComponent(id='minecraft:stripped_warped_hyphae', count=3),
    type='minecraft:crafting_shaped',
)

SUGAR_FROM_HONEY_BOTTLE = RecipeCraftingShapeless(
    group='sugar',
    ingredients=['minecraft:honey_bottle'],
    result=ItemStackOfComponent(id='minecraft:sugar', count=3),
    type='minecraft:crafting_shapeless',
)

SUGAR_FROM_SUGAR_CANE = RecipeCraftingShapeless(
    group='sugar',
    ingredients=['minecraft:sugar_cane'],
    result=ItemStackOfComponent(id='minecraft:sugar'),
    type='minecraft:crafting_shapeless',
)

SULFUR_BRICKS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:polished_sulfur'},
    result=ItemStackOfComponent(id='minecraft:sulfur_bricks', count=4),
    type='minecraft:crafting_shaped',
)

SULFUR_BRICKS_FROM_POLISHED_SULFUR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_sulfur',
    result=ItemStackOfComponent(id='minecraft:sulfur_bricks'),
    type='minecraft:stonecutting',
)

SULFUR_BRICKS_FROM_SULFUR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:sulfur',
    result=ItemStackOfComponent(id='minecraft:sulfur_bricks'),
    type='minecraft:stonecutting',
)

SULFUR_BRICK_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:sulfur_bricks'},
    result=ItemStackOfComponent(id='minecraft:sulfur_brick_slab', count=6),
    type='minecraft:crafting_shaped',
)

SULFUR_BRICK_SLAB_FROM_POLISHED_SULFUR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_sulfur',
    result=ItemStackOfComponent(id='minecraft:sulfur_brick_slab', count=2),
    type='minecraft:stonecutting',
)

SULFUR_BRICK_SLAB_FROM_SULFUR_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:sulfur_bricks',
    result=ItemStackOfComponent(id='minecraft:sulfur_brick_slab', count=2),
    type='minecraft:stonecutting',
)

SULFUR_BRICK_SLAB_FROM_SULFUR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:sulfur',
    result=ItemStackOfComponent(id='minecraft:sulfur_brick_slab', count=2),
    type='minecraft:stonecutting',
)

SULFUR_BRICK_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:sulfur_bricks'},
    result=ItemStackOfComponent(id='minecraft:sulfur_brick_stairs', count=4),
    type='minecraft:crafting_shaped',
)

SULFUR_BRICK_STAIRS_FROM_POLISHED_SULFUR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_sulfur',
    result=ItemStackOfComponent(id='minecraft:sulfur_brick_stairs'),
    type='minecraft:stonecutting',
)

SULFUR_BRICK_STAIRS_FROM_SULFUR_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:sulfur_bricks',
    result=ItemStackOfComponent(id='minecraft:sulfur_brick_stairs'),
    type='minecraft:stonecutting',
)

SULFUR_BRICK_STAIRS_FROM_SULFUR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:sulfur',
    result=ItemStackOfComponent(id='minecraft:sulfur_brick_stairs'),
    type='minecraft:stonecutting',
)

SULFUR_BRICK_WALL = RecipeCraftingShaped(
    pattern=['###', '###'],
    key={'#': 'minecraft:sulfur_bricks'},
    result=ItemStackOfComponent(id='minecraft:sulfur_brick_wall', count=6),
    type='minecraft:crafting_shaped',
)

SULFUR_BRICK_WALL_FROM_POLISHED_SULFUR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_sulfur',
    result=ItemStackOfComponent(id='minecraft:sulfur_brick_wall'),
    type='minecraft:stonecutting',
)

SULFUR_BRICK_WALL_FROM_SULFUR_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:sulfur_bricks',
    result=ItemStackOfComponent(id='minecraft:sulfur_brick_wall'),
    type='minecraft:stonecutting',
)

SULFUR_BRICK_WALL_FROM_SULFUR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:sulfur',
    result=ItemStackOfComponent(id='minecraft:sulfur_brick_wall'),
    type='minecraft:stonecutting',
)

SULFUR_FROM_SULFUR_SPIKES = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:sulfur_spike'},
    result=ItemStackOfComponent(id='minecraft:sulfur'),
    type='minecraft:crafting_shaped',
)

SULFUR_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:sulfur'},
    result=ItemStackOfComponent(id='minecraft:sulfur_slab', count=6),
    type='minecraft:crafting_shaped',
)

SULFUR_SLAB_FROM_SULFUR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:sulfur',
    result=ItemStackOfComponent(id='minecraft:sulfur_slab', count=2),
    type='minecraft:stonecutting',
)

SULFUR_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:sulfur'},
    result=ItemStackOfComponent(id='minecraft:sulfur_stairs', count=4),
    type='minecraft:crafting_shaped',
)

SULFUR_STAIRS_FROM_SULFUR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:sulfur',
    result=ItemStackOfComponent(id='minecraft:sulfur_stairs'),
    type='minecraft:stonecutting',
)

SULFUR_WALL = RecipeCraftingShaped(
    pattern=['###', '###'],
    key={'#': 'minecraft:sulfur'},
    result=ItemStackOfComponent(id='minecraft:sulfur_wall', count=6),
    type='minecraft:crafting_shaped',
)

SULFUR_WALL_FROM_SULFUR_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:sulfur',
    result=ItemStackOfComponent(id='minecraft:sulfur_wall'),
    type='minecraft:stonecutting',
)

SUSPICIOUS_STEW_FROM_ALLIUM = RecipeCraftingShapeless(
    group='suspicious_stew',
    ingredients=['minecraft:bowl', '#minecraft:mushrooms', '#minecraft:mushrooms', 'minecraft:allium'],
    result=ItemStackOfComponent(
        id='minecraft:suspicious_stew',
        components=DataComponentPatch(suspicious_stew_effects=[SuspiciousStewEffect(id='minecraft:fire_resistance', duration=60)]),
    ),
    type='minecraft:crafting_shapeless',
)

SUSPICIOUS_STEW_FROM_AZURE_BLUET = RecipeCraftingShapeless(
    group='suspicious_stew',
    ingredients=['minecraft:bowl', '#minecraft:mushrooms', '#minecraft:mushrooms', 'minecraft:azure_bluet'],
    result=ItemStackOfComponent(
        id='minecraft:suspicious_stew',
        components=DataComponentPatch(suspicious_stew_effects=[SuspiciousStewEffect(id='minecraft:blindness', duration=220)]),
    ),
    type='minecraft:crafting_shapeless',
)

SUSPICIOUS_STEW_FROM_BLUE_ORCHID = RecipeCraftingShapeless(
    group='suspicious_stew',
    ingredients=['minecraft:bowl', '#minecraft:mushrooms', '#minecraft:mushrooms', 'minecraft:blue_orchid'],
    result=ItemStackOfComponent(
        id='minecraft:suspicious_stew',
        components=DataComponentPatch(suspicious_stew_effects=[SuspiciousStewEffect(id='minecraft:saturation', duration=7)]),
    ),
    type='minecraft:crafting_shapeless',
)

SUSPICIOUS_STEW_FROM_CLOSED_EYEBLOSSOM = RecipeCraftingShapeless(
    group='suspicious_stew',
    ingredients=['minecraft:bowl', '#minecraft:mushrooms', '#minecraft:mushrooms', 'minecraft:closed_eyeblossom'],
    result=ItemStackOfComponent(
        id='minecraft:suspicious_stew',
        components=DataComponentPatch(suspicious_stew_effects=[SuspiciousStewEffect(id='minecraft:nausea', duration=140)]),
    ),
    type='minecraft:crafting_shapeless',
)

SUSPICIOUS_STEW_FROM_CORNFLOWER = RecipeCraftingShapeless(
    group='suspicious_stew',
    ingredients=['minecraft:bowl', '#minecraft:mushrooms', '#minecraft:mushrooms', 'minecraft:cornflower'],
    result=ItemStackOfComponent(
        id='minecraft:suspicious_stew',
        components=DataComponentPatch(suspicious_stew_effects=[SuspiciousStewEffect(id='minecraft:jump_boost', duration=100)]),
    ),
    type='minecraft:crafting_shapeless',
)

SUSPICIOUS_STEW_FROM_DANDELION = RecipeCraftingShapeless(
    group='suspicious_stew',
    ingredients=['minecraft:bowl', '#minecraft:mushrooms', '#minecraft:mushrooms', 'minecraft:dandelion'],
    result=ItemStackOfComponent(
        id='minecraft:suspicious_stew',
        components=DataComponentPatch(suspicious_stew_effects=[SuspiciousStewEffect(id='minecraft:saturation', duration=7)]),
    ),
    type='minecraft:crafting_shapeless',
)

SUSPICIOUS_STEW_FROM_GOLDEN_DANDELION = RecipeCraftingShapeless(
    group='suspicious_stew',
    ingredients=['minecraft:bowl', '#minecraft:mushrooms', '#minecraft:mushrooms', 'minecraft:golden_dandelion'],
    result=ItemStackOfComponent(
        id='minecraft:suspicious_stew',
        components=DataComponentPatch(suspicious_stew_effects=[SuspiciousStewEffect(id='minecraft:saturation', duration=7)]),
    ),
    type='minecraft:crafting_shapeless',
)

SUSPICIOUS_STEW_FROM_LILY_OF_THE_VALLEY = RecipeCraftingShapeless(
    group='suspicious_stew',
    ingredients=['minecraft:bowl', '#minecraft:mushrooms', '#minecraft:mushrooms', 'minecraft:lily_of_the_valley'],
    result=ItemStackOfComponent(
        id='minecraft:suspicious_stew',
        components=DataComponentPatch(suspicious_stew_effects=[SuspiciousStewEffect(id='minecraft:poison', duration=220)]),
    ),
    type='minecraft:crafting_shapeless',
)

SUSPICIOUS_STEW_FROM_OPEN_EYEBLOSSOM = RecipeCraftingShapeless(
    group='suspicious_stew',
    ingredients=['minecraft:bowl', '#minecraft:mushrooms', '#minecraft:mushrooms', 'minecraft:open_eyeblossom'],
    result=ItemStackOfComponent(
        id='minecraft:suspicious_stew',
        components=DataComponentPatch(suspicious_stew_effects=[SuspiciousStewEffect(id='minecraft:blindness', duration=220)]),
    ),
    type='minecraft:crafting_shapeless',
)

SUSPICIOUS_STEW_FROM_ORANGE_TULIP = RecipeCraftingShapeless(
    group='suspicious_stew',
    ingredients=['minecraft:bowl', '#minecraft:mushrooms', '#minecraft:mushrooms', 'minecraft:orange_tulip'],
    result=ItemStackOfComponent(
        id='minecraft:suspicious_stew',
        components=DataComponentPatch(suspicious_stew_effects=[SuspiciousStewEffect(id='minecraft:weakness', duration=140)]),
    ),
    type='minecraft:crafting_shapeless',
)

SUSPICIOUS_STEW_FROM_OXEYE_DAISY = RecipeCraftingShapeless(
    group='suspicious_stew',
    ingredients=['minecraft:bowl', '#minecraft:mushrooms', '#minecraft:mushrooms', 'minecraft:oxeye_daisy'],
    result=ItemStackOfComponent(
        id='minecraft:suspicious_stew',
        components=DataComponentPatch(suspicious_stew_effects=[SuspiciousStewEffect(id='minecraft:regeneration', duration=140)]),
    ),
    type='minecraft:crafting_shapeless',
)

SUSPICIOUS_STEW_FROM_PINK_TULIP = RecipeCraftingShapeless(
    group='suspicious_stew',
    ingredients=['minecraft:bowl', '#minecraft:mushrooms', '#minecraft:mushrooms', 'minecraft:pink_tulip'],
    result=ItemStackOfComponent(
        id='minecraft:suspicious_stew',
        components=DataComponentPatch(suspicious_stew_effects=[SuspiciousStewEffect(id='minecraft:weakness', duration=140)]),
    ),
    type='minecraft:crafting_shapeless',
)

SUSPICIOUS_STEW_FROM_POPPY = RecipeCraftingShapeless(
    group='suspicious_stew',
    ingredients=['minecraft:bowl', '#minecraft:mushrooms', '#minecraft:mushrooms', 'minecraft:poppy'],
    result=ItemStackOfComponent(
        id='minecraft:suspicious_stew',
        components=DataComponentPatch(suspicious_stew_effects=[SuspiciousStewEffect(id='minecraft:night_vision', duration=100)]),
    ),
    type='minecraft:crafting_shapeless',
)

SUSPICIOUS_STEW_FROM_RED_TULIP = RecipeCraftingShapeless(
    group='suspicious_stew',
    ingredients=['minecraft:bowl', '#minecraft:mushrooms', '#minecraft:mushrooms', 'minecraft:red_tulip'],
    result=ItemStackOfComponent(
        id='minecraft:suspicious_stew',
        components=DataComponentPatch(suspicious_stew_effects=[SuspiciousStewEffect(id='minecraft:weakness', duration=140)]),
    ),
    type='minecraft:crafting_shapeless',
)

SUSPICIOUS_STEW_FROM_TORCHFLOWER = RecipeCraftingShapeless(
    group='suspicious_stew',
    ingredients=['minecraft:bowl', '#minecraft:mushrooms', '#minecraft:mushrooms', 'minecraft:torchflower'],
    result=ItemStackOfComponent(
        id='minecraft:suspicious_stew',
        components=DataComponentPatch(suspicious_stew_effects=[SuspiciousStewEffect(id='minecraft:night_vision', duration=100)]),
    ),
    type='minecraft:crafting_shapeless',
)

SUSPICIOUS_STEW_FROM_WHITE_TULIP = RecipeCraftingShapeless(
    group='suspicious_stew',
    ingredients=['minecraft:bowl', '#minecraft:mushrooms', '#minecraft:mushrooms', 'minecraft:white_tulip'],
    result=ItemStackOfComponent(
        id='minecraft:suspicious_stew',
        components=DataComponentPatch(suspicious_stew_effects=[SuspiciousStewEffect(id='minecraft:weakness', duration=140)]),
    ),
    type='minecraft:crafting_shapeless',
)

SUSPICIOUS_STEW_FROM_WITHER_ROSE = RecipeCraftingShapeless(
    group='suspicious_stew',
    ingredients=['minecraft:bowl', '#minecraft:mushrooms', '#minecraft:mushrooms', 'minecraft:wither_rose'],
    result=ItemStackOfComponent(
        id='minecraft:suspicious_stew',
        components=DataComponentPatch(suspicious_stew_effects=[SuspiciousStewEffect(id='minecraft:wither', duration=140)]),
    ),
    type='minecraft:crafting_shapeless',
)

TARGET = RecipeCraftingShaped(
    category=CraftingBookCategory.REDSTONE,
    pattern=[' R ', 'RHR', ' R '],
    key={'H': 'minecraft:hay_block', 'R': 'minecraft:redstone'},
    result=ItemStackOfComponent(id='minecraft:target'),
    type='minecraft:crafting_shaped',
)

TERRACOTTA = RecipeSmelting(
    category=CookingBookCategory.BLOCKS,
    ingredient='minecraft:clay',
    result=ItemStackOfComponent(id='minecraft:terracotta'),
    experience=0.35,
    cookingtime=200,
    type='minecraft:smelting',
)

TIDE_ARMOR_TRIM_SMITHING_TEMPLATE = RecipeCraftingShaped(
    pattern=['#S#', '#C#', '###'],
    key={'#': 'minecraft:diamond', 'C': 'minecraft:prismarine', 'S': 'minecraft:tide_armor_trim_smithing_template'},
    result=ItemStackOfComponent(id='minecraft:tide_armor_trim_smithing_template', count=2),
    type='minecraft:crafting_shaped',
)

TIDE_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = RecipeSmithingTrim(
    base='#minecraft:trimmable_armor',
    addition='#minecraft:trim_materials',
    template='minecraft:tide_armor_trim_smithing_template',
    pattern='minecraft:tide',
    type='minecraft:smithing_trim',
)

TINTED_GLASS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=[' S ', 'SGS', ' S '],
    key={'G': 'minecraft:glass', 'S': 'minecraft:amethyst_shard'},
    result=ItemStackOfComponent(id='minecraft:tinted_glass', count=2),
    type='minecraft:crafting_shaped',
)

TIPPED_ARROW = RecipeCraftingImbue(
    source='minecraft:lingering_potion',
    material='minecraft:arrow',
    result=ItemStackOfComponent(id='minecraft:tipped_arrow', count=8),
    type='minecraft:crafting_imbue',
)

TNT = RecipeCraftingShaped(
    category=CraftingBookCategory.REDSTONE,
    pattern=['X#X', '#X#', 'X#X'],
    key={'#': ['minecraft:sand', 'minecraft:red_sand'], 'X': 'minecraft:gunpowder'},
    result=ItemStackOfComponent(id='minecraft:tnt'),
    type='minecraft:crafting_shaped',
)

TNT_MINECART = RecipeCraftingShapeless(
    ingredients=['minecraft:tnt', 'minecraft:minecart'],
    result=ItemStackOfComponent(id='minecraft:tnt_minecart'),
    type='minecraft:crafting_shapeless',
)

TORCH = RecipeCraftingShaped(
    pattern=['X', '#'],
    key={'#': 'minecraft:stick', 'X': ['minecraft:coal', 'minecraft:charcoal']},
    result=ItemStackOfComponent(id='minecraft:torch', count=4),
    type='minecraft:crafting_shaped',
)

TRAPPED_CHEST = RecipeCraftingShapeless(
    category=CraftingBookCategory.REDSTONE,
    ingredients=['minecraft:chest', 'minecraft:tripwire_hook'],
    result=ItemStackOfComponent(id='minecraft:trapped_chest'),
    type='minecraft:crafting_shapeless',
)

TRIPWIRE_HOOK = RecipeCraftingShaped(
    category=CraftingBookCategory.REDSTONE,
    pattern=['I', 'S', '#'],
    key={'#': '#minecraft:planks', 'I': 'minecraft:iron_ingot', 'S': 'minecraft:stick'},
    result=ItemStackOfComponent(id='minecraft:tripwire_hook', count=2),
    type='minecraft:crafting_shaped',
)

TUFF_BRICKS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:polished_tuff'},
    result=ItemStackOfComponent(id='minecraft:tuff_bricks', count=4),
    type='minecraft:crafting_shaped',
)

TUFF_BRICKS_FROM_POLISHED_TUFF_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_tuff',
    result=ItemStackOfComponent(id='minecraft:tuff_bricks'),
    type='minecraft:stonecutting',
)

TUFF_BRICKS_FROM_TUFF_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:tuff',
    result=ItemStackOfComponent(id='minecraft:tuff_bricks'),
    type='minecraft:stonecutting',
)

TUFF_BRICK_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:tuff_bricks'},
    result=ItemStackOfComponent(id='minecraft:tuff_brick_slab', count=6),
    type='minecraft:crafting_shaped',
)

TUFF_BRICK_SLAB_FROM_POLISHED_TUFF_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_tuff',
    result=ItemStackOfComponent(id='minecraft:tuff_brick_slab', count=2),
    type='minecraft:stonecutting',
)

TUFF_BRICK_SLAB_FROM_TUFF_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:tuff_bricks',
    result=ItemStackOfComponent(id='minecraft:tuff_brick_slab', count=2),
    type='minecraft:stonecutting',
)

TUFF_BRICK_SLAB_FROM_TUFF_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:tuff',
    result=ItemStackOfComponent(id='minecraft:tuff_brick_slab', count=2),
    type='minecraft:stonecutting',
)

TUFF_BRICK_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:tuff_bricks'},
    result=ItemStackOfComponent(id='minecraft:tuff_brick_stairs', count=4),
    type='minecraft:crafting_shaped',
)

TUFF_BRICK_STAIRS_FROM_POLISHED_TUFF_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_tuff',
    result=ItemStackOfComponent(id='minecraft:tuff_brick_stairs'),
    type='minecraft:stonecutting',
)

TUFF_BRICK_STAIRS_FROM_TUFF_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:tuff_bricks',
    result=ItemStackOfComponent(id='minecraft:tuff_brick_stairs'),
    type='minecraft:stonecutting',
)

TUFF_BRICK_STAIRS_FROM_TUFF_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:tuff',
    result=ItemStackOfComponent(id='minecraft:tuff_brick_stairs'),
    type='minecraft:stonecutting',
)

TUFF_BRICK_WALL = RecipeCraftingShaped(
    pattern=['###', '###'],
    key={'#': 'minecraft:tuff_bricks'},
    result=ItemStackOfComponent(id='minecraft:tuff_brick_wall', count=6),
    type='minecraft:crafting_shaped',
)

TUFF_BRICK_WALL_FROM_POLISHED_TUFF_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:polished_tuff',
    result=ItemStackOfComponent(id='minecraft:tuff_brick_wall'),
    type='minecraft:stonecutting',
)

TUFF_BRICK_WALL_FROM_TUFF_BRICKS_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:tuff_bricks',
    result=ItemStackOfComponent(id='minecraft:tuff_brick_wall'),
    type='minecraft:stonecutting',
)

TUFF_BRICK_WALL_FROM_TUFF_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:tuff',
    result=ItemStackOfComponent(id='minecraft:tuff_brick_wall'),
    type='minecraft:stonecutting',
)

TUFF_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:tuff'},
    result=ItemStackOfComponent(id='minecraft:tuff_slab', count=6),
    type='minecraft:crafting_shaped',
)

TUFF_SLAB_FROM_TUFF_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:tuff',
    result=ItemStackOfComponent(id='minecraft:tuff_slab', count=2),
    type='minecraft:stonecutting',
)

TUFF_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:tuff'},
    result=ItemStackOfComponent(id='minecraft:tuff_stairs', count=4),
    type='minecraft:crafting_shaped',
)

TUFF_STAIRS_FROM_TUFF_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:tuff',
    result=ItemStackOfComponent(id='minecraft:tuff_stairs'),
    type='minecraft:stonecutting',
)

TUFF_WALL = RecipeCraftingShaped(
    pattern=['###', '###'],
    key={'#': 'minecraft:tuff'},
    result=ItemStackOfComponent(id='minecraft:tuff_wall', count=6),
    type='minecraft:crafting_shaped',
)

TUFF_WALL_FROM_TUFF_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:tuff',
    result=ItemStackOfComponent(id='minecraft:tuff_wall'),
    type='minecraft:stonecutting',
)

TURTLE_HELMET = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['XXX', 'X X'],
    key={'X': 'minecraft:turtle_scute'},
    result=ItemStackOfComponent(id='minecraft:turtle_helmet'),
    type='minecraft:crafting_shaped',
)

VEX_ARMOR_TRIM_SMITHING_TEMPLATE = RecipeCraftingShaped(
    pattern=['#S#', '#C#', '###'],
    key={'#': 'minecraft:diamond', 'C': 'minecraft:cobblestone', 'S': 'minecraft:vex_armor_trim_smithing_template'},
    result=ItemStackOfComponent(id='minecraft:vex_armor_trim_smithing_template', count=2),
    type='minecraft:crafting_shaped',
)

VEX_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = RecipeSmithingTrim(
    base='#minecraft:trimmable_armor',
    addition='#minecraft:trim_materials',
    template='minecraft:vex_armor_trim_smithing_template',
    pattern='minecraft:vex',
    type='minecraft:smithing_trim',
)

WARD_ARMOR_TRIM_SMITHING_TEMPLATE = RecipeCraftingShaped(
    pattern=['#S#', '#C#', '###'],
    key={'#': 'minecraft:diamond', 'C': 'minecraft:cobbled_deepslate', 'S': 'minecraft:ward_armor_trim_smithing_template'},
    result=ItemStackOfComponent(id='minecraft:ward_armor_trim_smithing_template', count=2),
    type='minecraft:crafting_shaped',
)

WARD_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = RecipeSmithingTrim(
    base='#minecraft:trimmable_armor',
    addition='#minecraft:trim_materials',
    template='minecraft:ward_armor_trim_smithing_template',
    pattern='minecraft:ward',
    type='minecraft:smithing_trim',
)

WARPED_BUTTON = RecipeCraftingShapeless(
    group='wooden_button',
    category=CraftingBookCategory.REDSTONE,
    ingredients=['minecraft:warped_planks'],
    result=ItemStackOfComponent(id='minecraft:warped_button'),
    type='minecraft:crafting_shapeless',
)

WARPED_DOOR = RecipeCraftingShaped(
    group='wooden_door',
    category=CraftingBookCategory.REDSTONE,
    pattern=['##', '##', '##'],
    key={'#': 'minecraft:warped_planks'},
    result=ItemStackOfComponent(id='minecraft:warped_door', count=3),
    type='minecraft:crafting_shaped',
)

WARPED_FENCE = RecipeCraftingShaped(
    group='wooden_fence',
    pattern=['W#W', 'W#W'],
    key={'#': 'minecraft:stick', 'W': 'minecraft:warped_planks'},
    result=ItemStackOfComponent(id='minecraft:warped_fence', count=3),
    type='minecraft:crafting_shaped',
)

WARPED_FENCE_GATE = RecipeCraftingShaped(
    group='wooden_fence_gate',
    category=CraftingBookCategory.REDSTONE,
    pattern=['#W#', '#W#'],
    key={'#': 'minecraft:stick', 'W': 'minecraft:warped_planks'},
    result=ItemStackOfComponent(id='minecraft:warped_fence_gate'),
    type='minecraft:crafting_shaped',
)

WARPED_FUNGUS_ON_A_STICK = RecipeCraftingShaped(
    pattern=['# ', ' X'],
    key={'#': 'minecraft:fishing_rod', 'X': 'minecraft:warped_fungus'},
    result=ItemStackOfComponent(id='minecraft:warped_fungus_on_a_stick'),
    type='minecraft:crafting_shaped',
)

WARPED_HANGING_SIGN = RecipeCraftingShaped(
    group='wooden_hanging_sign',
    pattern=['X X', '###', '###'],
    key={'#': 'minecraft:stripped_warped_stem', 'X': 'minecraft:iron_chain'},
    result=ItemStackOfComponent(id='minecraft:warped_hanging_sign', count=6),
    type='minecraft:crafting_shaped',
)

WARPED_HYPHAE = RecipeCraftingShaped(
    group='bark',
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:warped_stem'},
    result=ItemStackOfComponent(id='minecraft:warped_hyphae', count=3),
    type='minecraft:crafting_shaped',
)

WARPED_PLANKS = RecipeCraftingShapeless(
    group='planks',
    category=CraftingBookCategory.BUILDING,
    ingredients=['#minecraft:warped_stems'],
    result=ItemStackOfComponent(id='minecraft:warped_planks', count=4),
    type='minecraft:crafting_shapeless',
)

WARPED_PRESSURE_PLATE = RecipeCraftingShaped(
    group='wooden_pressure_plate',
    category=CraftingBookCategory.REDSTONE,
    pattern=['##'],
    key={'#': 'minecraft:warped_planks'},
    result=ItemStackOfComponent(id='minecraft:warped_pressure_plate'),
    type='minecraft:crafting_shaped',
)

WARPED_SHELF = RecipeCraftingShaped(
    group='shelf',
    pattern=['###', '   ', '###'],
    key={'#': 'minecraft:stripped_warped_stem'},
    result=ItemStackOfComponent(id='minecraft:warped_shelf', count=6),
    type='minecraft:crafting_shaped',
)

WARPED_SIGN = RecipeCraftingShaped(
    group='wooden_sign',
    pattern=['###', '###', ' X '],
    key={'#': 'minecraft:warped_planks', 'X': 'minecraft:stick'},
    result=ItemStackOfComponent(id='minecraft:warped_sign', count=3),
    type='minecraft:crafting_shaped',
)

WARPED_SLAB = RecipeCraftingShaped(
    group='wooden_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:warped_planks'},
    result=ItemStackOfComponent(id='minecraft:warped_slab', count=6),
    type='minecraft:crafting_shaped',
)

WARPED_STAIRS = RecipeCraftingShaped(
    group='wooden_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:warped_planks'},
    result=ItemStackOfComponent(id='minecraft:warped_stairs', count=4),
    type='minecraft:crafting_shaped',
)

WARPED_TRAPDOOR = RecipeCraftingShaped(
    group='wooden_trapdoor',
    category=CraftingBookCategory.REDSTONE,
    pattern=['###', '###'],
    key={'#': 'minecraft:warped_planks'},
    result=ItemStackOfComponent(id='minecraft:warped_trapdoor', count=2),
    type='minecraft:crafting_shaped',
)

WAXED_CHISELED_COPPER = RecipeCraftingShaped(
    group='waxed_chiseled_copper',
    category=CraftingBookCategory.BUILDING,
    pattern=[' M ', ' M '],
    key={'M': 'minecraft:waxed_cut_copper_slab'},
    result=ItemStackOfComponent(id='minecraft:waxed_chiseled_copper'),
    type='minecraft:crafting_shaped',
)

WAXED_CHISELED_COPPER_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_chiseled_copper',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:chiseled_copper', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_chiseled_copper'),
    type='minecraft:crafting_shapeless',
)

WAXED_CHISELED_COPPER_FROM_WAXED_COPPER_BLOCK_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:waxed_copper_block',
    result=ItemStackOfComponent(id='minecraft:waxed_chiseled_copper', count=4),
    type='minecraft:stonecutting',
)

WAXED_CHISELED_COPPER_FROM_WAXED_CUT_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:waxed_cut_copper',
    result=ItemStackOfComponent(id='minecraft:waxed_chiseled_copper'),
    type='minecraft:stonecutting',
)

WAXED_COPPER_BARS_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_copper_bar',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:copper_bars', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_copper_bars'),
    type='minecraft:crafting_shapeless',
)

WAXED_COPPER_BLOCK_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_copper_block',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:copper_block', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_copper_block'),
    type='minecraft:crafting_shapeless',
)

WAXED_COPPER_BULB = RecipeCraftingShaped(
    group='waxed_copper_bulb',
    category=CraftingBookCategory.REDSTONE,
    pattern=[' C ', 'CBC', ' R '],
    key={'B': 'minecraft:blaze_rod', 'C': 'minecraft:waxed_copper_block', 'R': 'minecraft:redstone'},
    result=ItemStackOfComponent(id='minecraft:waxed_copper_bulb', count=4),
    type='minecraft:crafting_shaped',
)

WAXED_COPPER_BULB_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_copper_bulb',
    category=CraftingBookCategory.REDSTONE,
    ingredients=['minecraft:copper_bulb', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_copper_bulb'),
    type='minecraft:crafting_shapeless',
)

WAXED_COPPER_CHAIN_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_copper_chain',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:copper_chain', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_copper_chain'),
    type='minecraft:crafting_shapeless',
)

WAXED_COPPER_CHEST_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_copper_chest',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:copper_chest', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_copper_chest'),
    type='minecraft:crafting_shapeless',
)

WAXED_COPPER_DOOR_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_copper_door',
    category=CraftingBookCategory.REDSTONE,
    ingredients=['minecraft:copper_door', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_copper_door'),
    type='minecraft:crafting_shapeless',
)

WAXED_COPPER_GOLEM_STATUE_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_copper_golem_statue',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:copper_golem_statue', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_copper_golem_statue'),
    type='minecraft:crafting_shapeless',
)

WAXED_COPPER_GRATE = RecipeCraftingShaped(
    group='waxed_copper_grate',
    category=CraftingBookCategory.BUILDING,
    pattern=[' M ', 'M M', ' M '],
    key={'M': 'minecraft:waxed_copper_block'},
    result=ItemStackOfComponent(id='minecraft:waxed_copper_grate', count=4),
    type='minecraft:crafting_shaped',
)

WAXED_COPPER_GRATE_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_copper_grate',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:copper_grate', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_copper_grate'),
    type='minecraft:crafting_shapeless',
)

WAXED_COPPER_GRATE_FROM_WAXED_COPPER_BLOCK_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:waxed_copper_block',
    result=ItemStackOfComponent(id='minecraft:waxed_copper_grate', count=4),
    type='minecraft:stonecutting',
)

WAXED_COPPER_LANTERN_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_copper_lantern',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:copper_lantern', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_copper_lantern'),
    type='minecraft:crafting_shapeless',
)

WAXED_COPPER_TRAPDOOR_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_copper_trapdoor',
    category=CraftingBookCategory.REDSTONE,
    ingredients=['minecraft:copper_trapdoor', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_copper_trapdoor'),
    type='minecraft:crafting_shapeless',
)

WAXED_CUT_COPPER = RecipeCraftingShaped(
    group='waxed_cut_copper',
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:waxed_copper_block'},
    result=ItemStackOfComponent(id='minecraft:waxed_cut_copper', count=4),
    type='minecraft:crafting_shaped',
)

WAXED_CUT_COPPER_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_cut_copper',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:cut_copper', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_cut_copper'),
    type='minecraft:crafting_shapeless',
)

WAXED_CUT_COPPER_FROM_WAXED_COPPER_BLOCK_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:waxed_copper_block',
    result=ItemStackOfComponent(id='minecraft:waxed_cut_copper', count=4),
    type='minecraft:stonecutting',
)

WAXED_CUT_COPPER_SLAB = RecipeCraftingShaped(
    group='waxed_cut_copper_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:waxed_cut_copper'},
    result=ItemStackOfComponent(id='minecraft:waxed_cut_copper_slab', count=6),
    type='minecraft:crafting_shaped',
)

WAXED_CUT_COPPER_SLAB_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_cut_copper_slab',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:cut_copper_slab', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_cut_copper_slab'),
    type='minecraft:crafting_shapeless',
)

WAXED_CUT_COPPER_SLAB_FROM_WAXED_COPPER_BLOCK_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:waxed_copper_block',
    result=ItemStackOfComponent(id='minecraft:waxed_cut_copper_slab', count=8),
    type='minecraft:stonecutting',
)

WAXED_CUT_COPPER_SLAB_FROM_WAXED_CUT_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:waxed_cut_copper',
    result=ItemStackOfComponent(id='minecraft:waxed_cut_copper_slab', count=2),
    type='minecraft:stonecutting',
)

WAXED_CUT_COPPER_STAIRS = RecipeCraftingShaped(
    group='waxed_cut_copper_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:waxed_cut_copper'},
    result=ItemStackOfComponent(id='minecraft:waxed_cut_copper_stairs', count=4),
    type='minecraft:crafting_shaped',
)

WAXED_CUT_COPPER_STAIRS_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_cut_copper_stairs',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:cut_copper_stairs', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_cut_copper_stairs'),
    type='minecraft:crafting_shapeless',
)

WAXED_CUT_COPPER_STAIRS_FROM_WAXED_COPPER_BLOCK_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:waxed_copper_block',
    result=ItemStackOfComponent(id='minecraft:waxed_cut_copper_stairs', count=4),
    type='minecraft:stonecutting',
)

WAXED_CUT_COPPER_STAIRS_FROM_WAXED_CUT_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:waxed_cut_copper',
    result=ItemStackOfComponent(id='minecraft:waxed_cut_copper_stairs'),
    type='minecraft:stonecutting',
)

WAXED_EXPOSED_CHISELED_COPPER = RecipeCraftingShaped(
    group='waxed_exposed_chiseled_copper',
    category=CraftingBookCategory.BUILDING,
    pattern=[' M ', ' M '],
    key={'M': 'minecraft:waxed_exposed_cut_copper_slab'},
    result=ItemStackOfComponent(id='minecraft:waxed_exposed_chiseled_copper'),
    type='minecraft:crafting_shaped',
)

WAXED_EXPOSED_CHISELED_COPPER_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_exposed_chiseled_copper',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:exposed_chiseled_copper', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_exposed_chiseled_copper'),
    type='minecraft:crafting_shapeless',
)

WAXED_EXPOSED_CHISELED_COPPER_FROM_WAXED_EXPOSED_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:waxed_exposed_copper',
    result=ItemStackOfComponent(id='minecraft:waxed_exposed_chiseled_copper', count=4),
    type='minecraft:stonecutting',
)

WAXED_EXPOSED_CHISELED_COPPER_FROM_WAXED_EXPOSED_CUT_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:waxed_exposed_cut_copper',
    result=ItemStackOfComponent(id='minecraft:waxed_exposed_chiseled_copper'),
    type='minecraft:stonecutting',
)

WAXED_EXPOSED_COPPER_BARS_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_copper_bar',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:exposed_copper_bars', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_exposed_copper_bars'),
    type='minecraft:crafting_shapeless',
)

WAXED_EXPOSED_COPPER_BULB = RecipeCraftingShaped(
    group='waxed_exposed_copper_bulb',
    category=CraftingBookCategory.REDSTONE,
    pattern=[' C ', 'CBC', ' R '],
    key={'B': 'minecraft:blaze_rod', 'C': 'minecraft:waxed_exposed_copper', 'R': 'minecraft:redstone'},
    result=ItemStackOfComponent(id='minecraft:waxed_exposed_copper_bulb', count=4),
    type='minecraft:crafting_shaped',
)

WAXED_EXPOSED_COPPER_BULB_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_exposed_copper_bulb',
    category=CraftingBookCategory.REDSTONE,
    ingredients=['minecraft:exposed_copper_bulb', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_exposed_copper_bulb'),
    type='minecraft:crafting_shapeless',
)

WAXED_EXPOSED_COPPER_CHAIN_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_copper_chain',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:exposed_copper_chain', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_exposed_copper_chain'),
    type='minecraft:crafting_shapeless',
)

WAXED_EXPOSED_COPPER_CHEST_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_copper_chest',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:exposed_copper_chest', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_exposed_copper_chest'),
    type='minecraft:crafting_shapeless',
)

WAXED_EXPOSED_COPPER_DOOR_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_copper_door',
    category=CraftingBookCategory.REDSTONE,
    ingredients=['minecraft:exposed_copper_door', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_exposed_copper_door'),
    type='minecraft:crafting_shapeless',
)

WAXED_EXPOSED_COPPER_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_copper_block',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:exposed_copper', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_exposed_copper'),
    type='minecraft:crafting_shapeless',
)

WAXED_EXPOSED_COPPER_GOLEM_STATUE_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_copper_golem_statue',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:exposed_copper_golem_statue', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_exposed_copper_golem_statue'),
    type='minecraft:crafting_shapeless',
)

WAXED_EXPOSED_COPPER_GRATE = RecipeCraftingShaped(
    group='waxed_exposed_copper_grate',
    category=CraftingBookCategory.BUILDING,
    pattern=[' M ', 'M M', ' M '],
    key={'M': 'minecraft:waxed_exposed_copper'},
    result=ItemStackOfComponent(id='minecraft:waxed_exposed_copper_grate', count=4),
    type='minecraft:crafting_shaped',
)

WAXED_EXPOSED_COPPER_GRATE_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_exposed_copper_grate',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:exposed_copper_grate', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_exposed_copper_grate'),
    type='minecraft:crafting_shapeless',
)

WAXED_EXPOSED_COPPER_GRATE_FROM_WAXED_EXPOSED_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:waxed_exposed_copper',
    result=ItemStackOfComponent(id='minecraft:waxed_exposed_copper_grate', count=4),
    type='minecraft:stonecutting',
)

WAXED_EXPOSED_COPPER_LANTERN_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_copper_lantern',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:exposed_copper_lantern', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_exposed_copper_lantern'),
    type='minecraft:crafting_shapeless',
)

WAXED_EXPOSED_COPPER_TRAPDOOR_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_copper_trapdoor',
    category=CraftingBookCategory.REDSTONE,
    ingredients=['minecraft:exposed_copper_trapdoor', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_exposed_copper_trapdoor'),
    type='minecraft:crafting_shapeless',
)

WAXED_EXPOSED_CUT_COPPER = RecipeCraftingShaped(
    group='waxed_exposed_cut_copper',
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:waxed_exposed_copper'},
    result=ItemStackOfComponent(id='minecraft:waxed_exposed_cut_copper', count=4),
    type='minecraft:crafting_shaped',
)

WAXED_EXPOSED_CUT_COPPER_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_exposed_cut_copper',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:exposed_cut_copper', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_exposed_cut_copper'),
    type='minecraft:crafting_shapeless',
)

WAXED_EXPOSED_CUT_COPPER_FROM_WAXED_EXPOSED_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:waxed_exposed_copper',
    result=ItemStackOfComponent(id='minecraft:waxed_exposed_cut_copper', count=4),
    type='minecraft:stonecutting',
)

WAXED_EXPOSED_CUT_COPPER_SLAB = RecipeCraftingShaped(
    group='waxed_exposed_cut_copper_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:waxed_exposed_cut_copper'},
    result=ItemStackOfComponent(id='minecraft:waxed_exposed_cut_copper_slab', count=6),
    type='minecraft:crafting_shaped',
)

WAXED_EXPOSED_CUT_COPPER_SLAB_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_exposed_cut_copper_slab',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:exposed_cut_copper_slab', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_exposed_cut_copper_slab'),
    type='minecraft:crafting_shapeless',
)

WAXED_EXPOSED_CUT_COPPER_SLAB_FROM_WAXED_EXPOSED_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:waxed_exposed_copper',
    result=ItemStackOfComponent(id='minecraft:waxed_exposed_cut_copper_slab', count=8),
    type='minecraft:stonecutting',
)

WAXED_EXPOSED_CUT_COPPER_SLAB_FROM_WAXED_EXPOSED_CUT_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:waxed_exposed_cut_copper',
    result=ItemStackOfComponent(id='minecraft:waxed_exposed_cut_copper_slab', count=2),
    type='minecraft:stonecutting',
)

WAXED_EXPOSED_CUT_COPPER_STAIRS = RecipeCraftingShaped(
    group='waxed_exposed_cut_copper_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:waxed_exposed_cut_copper'},
    result=ItemStackOfComponent(id='minecraft:waxed_exposed_cut_copper_stairs', count=4),
    type='minecraft:crafting_shaped',
)

WAXED_EXPOSED_CUT_COPPER_STAIRS_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_exposed_cut_copper_stairs',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:exposed_cut_copper_stairs', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_exposed_cut_copper_stairs'),
    type='minecraft:crafting_shapeless',
)

WAXED_EXPOSED_CUT_COPPER_STAIRS_FROM_WAXED_EXPOSED_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:waxed_exposed_copper',
    result=ItemStackOfComponent(id='minecraft:waxed_exposed_cut_copper_stairs', count=4),
    type='minecraft:stonecutting',
)

WAXED_EXPOSED_CUT_COPPER_STAIRS_FROM_WAXED_EXPOSED_CUT_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:waxed_exposed_cut_copper',
    result=ItemStackOfComponent(id='minecraft:waxed_exposed_cut_copper_stairs'),
    type='minecraft:stonecutting',
)

WAXED_EXPOSED_LIGHTNING_ROD_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_lightning_rod',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:exposed_lightning_rod', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_exposed_lightning_rod'),
    type='minecraft:crafting_shapeless',
)

WAXED_LIGHTNING_ROD_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_lightning_rod',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:lightning_rod', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_lightning_rod'),
    type='minecraft:crafting_shapeless',
)

WAXED_OXIDIZED_CHISELED_COPPER = RecipeCraftingShaped(
    group='waxed_oxidized_chiseled_copper',
    category=CraftingBookCategory.BUILDING,
    pattern=[' M ', ' M '],
    key={'M': 'minecraft:waxed_oxidized_cut_copper_slab'},
    result=ItemStackOfComponent(id='minecraft:waxed_oxidized_chiseled_copper'),
    type='minecraft:crafting_shaped',
)

WAXED_OXIDIZED_CHISELED_COPPER_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_oxidized_chiseled_copper',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:oxidized_chiseled_copper', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_oxidized_chiseled_copper'),
    type='minecraft:crafting_shapeless',
)

WAXED_OXIDIZED_CHISELED_COPPER_FROM_WAXED_OXIDIZED_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:waxed_oxidized_copper',
    result=ItemStackOfComponent(id='minecraft:waxed_oxidized_chiseled_copper', count=4),
    type='minecraft:stonecutting',
)

WAXED_OXIDIZED_CHISELED_COPPER_FROM_WAXED_OXIDIZED_CUT_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:waxed_oxidized_cut_copper',
    result=ItemStackOfComponent(id='minecraft:waxed_oxidized_chiseled_copper'),
    type='minecraft:stonecutting',
)

WAXED_OXIDIZED_COPPER_BARS_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_copper_bar',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:oxidized_copper_bars', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_oxidized_copper_bars'),
    type='minecraft:crafting_shapeless',
)

WAXED_OXIDIZED_COPPER_BULB = RecipeCraftingShaped(
    group='waxed_oxidized_copper_bulb',
    category=CraftingBookCategory.REDSTONE,
    pattern=[' C ', 'CBC', ' R '],
    key={'B': 'minecraft:blaze_rod', 'C': 'minecraft:waxed_oxidized_copper', 'R': 'minecraft:redstone'},
    result=ItemStackOfComponent(id='minecraft:waxed_oxidized_copper_bulb', count=4),
    type='minecraft:crafting_shaped',
)

WAXED_OXIDIZED_COPPER_BULB_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_oxidized_copper_bulb',
    category=CraftingBookCategory.REDSTONE,
    ingredients=['minecraft:oxidized_copper_bulb', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_oxidized_copper_bulb'),
    type='minecraft:crafting_shapeless',
)

WAXED_OXIDIZED_COPPER_CHAIN_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_copper_chain',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:oxidized_copper_chain', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_oxidized_copper_chain'),
    type='minecraft:crafting_shapeless',
)

WAXED_OXIDIZED_COPPER_CHEST_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_copper_chest',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:oxidized_copper_chest', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_oxidized_copper_chest'),
    type='minecraft:crafting_shapeless',
)

WAXED_OXIDIZED_COPPER_DOOR_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_copper_door',
    category=CraftingBookCategory.REDSTONE,
    ingredients=['minecraft:oxidized_copper_door', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_oxidized_copper_door'),
    type='minecraft:crafting_shapeless',
)

WAXED_OXIDIZED_COPPER_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_copper_block',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:oxidized_copper', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_oxidized_copper'),
    type='minecraft:crafting_shapeless',
)

WAXED_OXIDIZED_COPPER_GOLEM_STATUE_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_copper_golem_statue',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:oxidized_copper_golem_statue', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_oxidized_copper_golem_statue'),
    type='minecraft:crafting_shapeless',
)

WAXED_OXIDIZED_COPPER_GRATE = RecipeCraftingShaped(
    group='waxed_oxidized_copper_grate',
    category=CraftingBookCategory.BUILDING,
    pattern=[' M ', 'M M', ' M '],
    key={'M': 'minecraft:waxed_oxidized_copper'},
    result=ItemStackOfComponent(id='minecraft:waxed_oxidized_copper_grate', count=4),
    type='minecraft:crafting_shaped',
)

WAXED_OXIDIZED_COPPER_GRATE_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_oxidized_copper_grate',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:oxidized_copper_grate', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_oxidized_copper_grate'),
    type='minecraft:crafting_shapeless',
)

WAXED_OXIDIZED_COPPER_GRATE_FROM_WAXED_OXIDIZED_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:waxed_oxidized_copper',
    result=ItemStackOfComponent(id='minecraft:waxed_oxidized_copper_grate', count=4),
    type='minecraft:stonecutting',
)

WAXED_OXIDIZED_COPPER_LANTERN_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_copper_lantern',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:oxidized_copper_lantern', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_oxidized_copper_lantern'),
    type='minecraft:crafting_shapeless',
)

WAXED_OXIDIZED_COPPER_TRAPDOOR_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_copper_trapdoor',
    category=CraftingBookCategory.REDSTONE,
    ingredients=['minecraft:oxidized_copper_trapdoor', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_oxidized_copper_trapdoor'),
    type='minecraft:crafting_shapeless',
)

WAXED_OXIDIZED_CUT_COPPER = RecipeCraftingShaped(
    group='waxed_oxidized_cut_copper',
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:waxed_oxidized_copper'},
    result=ItemStackOfComponent(id='minecraft:waxed_oxidized_cut_copper', count=4),
    type='minecraft:crafting_shaped',
)

WAXED_OXIDIZED_CUT_COPPER_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_oxidized_cut_copper',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:oxidized_cut_copper', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_oxidized_cut_copper'),
    type='minecraft:crafting_shapeless',
)

WAXED_OXIDIZED_CUT_COPPER_FROM_WAXED_OXIDIZED_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:waxed_oxidized_copper',
    result=ItemStackOfComponent(id='minecraft:waxed_oxidized_cut_copper', count=4),
    type='minecraft:stonecutting',
)

WAXED_OXIDIZED_CUT_COPPER_SLAB = RecipeCraftingShaped(
    group='waxed_oxidized_cut_copper_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:waxed_oxidized_cut_copper'},
    result=ItemStackOfComponent(id='minecraft:waxed_oxidized_cut_copper_slab', count=6),
    type='minecraft:crafting_shaped',
)

WAXED_OXIDIZED_CUT_COPPER_SLAB_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_oxidized_cut_copper_slab',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:oxidized_cut_copper_slab', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_oxidized_cut_copper_slab'),
    type='minecraft:crafting_shapeless',
)

WAXED_OXIDIZED_CUT_COPPER_SLAB_FROM_WAXED_OXIDIZED_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:waxed_oxidized_copper',
    result=ItemStackOfComponent(id='minecraft:waxed_oxidized_cut_copper_slab', count=8),
    type='minecraft:stonecutting',
)

WAXED_OXIDIZED_CUT_COPPER_SLAB_FROM_WAXED_OXIDIZED_CUT_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:waxed_oxidized_cut_copper',
    result=ItemStackOfComponent(id='minecraft:waxed_oxidized_cut_copper_slab', count=2),
    type='minecraft:stonecutting',
)

WAXED_OXIDIZED_CUT_COPPER_STAIRS = RecipeCraftingShaped(
    group='waxed_oxidized_cut_copper_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:waxed_oxidized_cut_copper'},
    result=ItemStackOfComponent(id='minecraft:waxed_oxidized_cut_copper_stairs', count=4),
    type='minecraft:crafting_shaped',
)

WAXED_OXIDIZED_CUT_COPPER_STAIRS_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_oxidized_cut_copper_stairs',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:oxidized_cut_copper_stairs', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_oxidized_cut_copper_stairs'),
    type='minecraft:crafting_shapeless',
)

WAXED_OXIDIZED_CUT_COPPER_STAIRS_FROM_WAXED_OXIDIZED_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:waxed_oxidized_copper',
    result=ItemStackOfComponent(id='minecraft:waxed_oxidized_cut_copper_stairs', count=4),
    type='minecraft:stonecutting',
)

WAXED_OXIDIZED_CUT_COPPER_STAIRS_FROM_WAXED_OXIDIZED_CUT_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:waxed_oxidized_cut_copper',
    result=ItemStackOfComponent(id='minecraft:waxed_oxidized_cut_copper_stairs'),
    type='minecraft:stonecutting',
)

WAXED_OXIDIZED_LIGHTNING_ROD_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_lightning_rod',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:oxidized_lightning_rod', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_oxidized_lightning_rod'),
    type='minecraft:crafting_shapeless',
)

WAXED_WEATHERED_CHISELED_COPPER = RecipeCraftingShaped(
    group='waxed_weathered_chiseled_copper',
    category=CraftingBookCategory.BUILDING,
    pattern=[' M ', ' M '],
    key={'M': 'minecraft:waxed_weathered_cut_copper_slab'},
    result=ItemStackOfComponent(id='minecraft:waxed_weathered_chiseled_copper'),
    type='minecraft:crafting_shaped',
)

WAXED_WEATHERED_CHISELED_COPPER_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_weathered_chiseled_copper',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:weathered_chiseled_copper', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_weathered_chiseled_copper'),
    type='minecraft:crafting_shapeless',
)

WAXED_WEATHERED_CHISELED_COPPER_FROM_WAXED_WEATHERED_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:waxed_weathered_copper',
    result=ItemStackOfComponent(id='minecraft:waxed_weathered_chiseled_copper', count=4),
    type='minecraft:stonecutting',
)

WAXED_WEATHERED_CHISELED_COPPER_FROM_WAXED_WEATHERED_CUT_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:waxed_weathered_cut_copper',
    result=ItemStackOfComponent(id='minecraft:waxed_weathered_chiseled_copper'),
    type='minecraft:stonecutting',
)

WAXED_WEATHERED_COPPER_BARS_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_copper_bar',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:weathered_copper_bars', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_weathered_copper_bars'),
    type='minecraft:crafting_shapeless',
)

WAXED_WEATHERED_COPPER_BULB = RecipeCraftingShaped(
    group='waxed_weathered_copper_bulb',
    category=CraftingBookCategory.REDSTONE,
    pattern=[' C ', 'CBC', ' R '],
    key={'B': 'minecraft:blaze_rod', 'C': 'minecraft:waxed_weathered_copper', 'R': 'minecraft:redstone'},
    result=ItemStackOfComponent(id='minecraft:waxed_weathered_copper_bulb', count=4),
    type='minecraft:crafting_shaped',
)

WAXED_WEATHERED_COPPER_BULB_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_weathered_copper_bulb',
    category=CraftingBookCategory.REDSTONE,
    ingredients=['minecraft:weathered_copper_bulb', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_weathered_copper_bulb'),
    type='minecraft:crafting_shapeless',
)

WAXED_WEATHERED_COPPER_CHAIN_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_copper_chain',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:weathered_copper_chain', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_weathered_copper_chain'),
    type='minecraft:crafting_shapeless',
)

WAXED_WEATHERED_COPPER_CHEST_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_copper_chest',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:weathered_copper_chest', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_weathered_copper_chest'),
    type='minecraft:crafting_shapeless',
)

WAXED_WEATHERED_COPPER_DOOR_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_copper_door',
    category=CraftingBookCategory.REDSTONE,
    ingredients=['minecraft:weathered_copper_door', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_weathered_copper_door'),
    type='minecraft:crafting_shapeless',
)

WAXED_WEATHERED_COPPER_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_copper_block',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:weathered_copper', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_weathered_copper'),
    type='minecraft:crafting_shapeless',
)

WAXED_WEATHERED_COPPER_GOLEM_STATUE_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_copper_golem_statue',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:weathered_copper_golem_statue', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_weathered_copper_golem_statue'),
    type='minecraft:crafting_shapeless',
)

WAXED_WEATHERED_COPPER_GRATE = RecipeCraftingShaped(
    group='waxed_weathered_copper_grate',
    category=CraftingBookCategory.BUILDING,
    pattern=[' M ', 'M M', ' M '],
    key={'M': 'minecraft:waxed_weathered_copper'},
    result=ItemStackOfComponent(id='minecraft:waxed_weathered_copper_grate', count=4),
    type='minecraft:crafting_shaped',
)

WAXED_WEATHERED_COPPER_GRATE_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_weathered_copper_grate',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:weathered_copper_grate', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_weathered_copper_grate'),
    type='minecraft:crafting_shapeless',
)

WAXED_WEATHERED_COPPER_GRATE_FROM_WAXED_WEATHERED_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:waxed_weathered_copper',
    result=ItemStackOfComponent(id='minecraft:waxed_weathered_copper_grate', count=4),
    type='minecraft:stonecutting',
)

WAXED_WEATHERED_COPPER_LANTERN_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_copper_lantern',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:weathered_copper_lantern', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_weathered_copper_lantern'),
    type='minecraft:crafting_shapeless',
)

WAXED_WEATHERED_COPPER_TRAPDOOR_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_copper_trapdoor',
    category=CraftingBookCategory.REDSTONE,
    ingredients=['minecraft:weathered_copper_trapdoor', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_weathered_copper_trapdoor'),
    type='minecraft:crafting_shapeless',
)

WAXED_WEATHERED_CUT_COPPER = RecipeCraftingShaped(
    group='waxed_weathered_cut_copper',
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:waxed_weathered_copper'},
    result=ItemStackOfComponent(id='minecraft:waxed_weathered_cut_copper', count=4),
    type='minecraft:crafting_shaped',
)

WAXED_WEATHERED_CUT_COPPER_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_weathered_cut_copper',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:weathered_cut_copper', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_weathered_cut_copper'),
    type='minecraft:crafting_shapeless',
)

WAXED_WEATHERED_CUT_COPPER_FROM_WAXED_WEATHERED_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:waxed_weathered_copper',
    result=ItemStackOfComponent(id='minecraft:waxed_weathered_cut_copper', count=4),
    type='minecraft:stonecutting',
)

WAXED_WEATHERED_CUT_COPPER_SLAB = RecipeCraftingShaped(
    group='waxed_weathered_cut_copper_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:waxed_weathered_cut_copper'},
    result=ItemStackOfComponent(id='minecraft:waxed_weathered_cut_copper_slab', count=6),
    type='minecraft:crafting_shaped',
)

WAXED_WEATHERED_CUT_COPPER_SLAB_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_weathered_cut_copper_slab',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:weathered_cut_copper_slab', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_weathered_cut_copper_slab'),
    type='minecraft:crafting_shapeless',
)

WAXED_WEATHERED_CUT_COPPER_SLAB_FROM_WAXED_WEATHERED_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:waxed_weathered_copper',
    result=ItemStackOfComponent(id='minecraft:waxed_weathered_cut_copper_slab', count=8),
    type='minecraft:stonecutting',
)

WAXED_WEATHERED_CUT_COPPER_SLAB_FROM_WAXED_WEATHERED_CUT_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:waxed_weathered_cut_copper',
    result=ItemStackOfComponent(id='minecraft:waxed_weathered_cut_copper_slab', count=2),
    type='minecraft:stonecutting',
)

WAXED_WEATHERED_CUT_COPPER_STAIRS = RecipeCraftingShaped(
    group='waxed_weathered_cut_copper_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:waxed_weathered_cut_copper'},
    result=ItemStackOfComponent(id='minecraft:waxed_weathered_cut_copper_stairs', count=4),
    type='minecraft:crafting_shaped',
)

WAXED_WEATHERED_CUT_COPPER_STAIRS_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_weathered_cut_copper_stairs',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:weathered_cut_copper_stairs', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_weathered_cut_copper_stairs'),
    type='minecraft:crafting_shapeless',
)

WAXED_WEATHERED_CUT_COPPER_STAIRS_FROM_WAXED_WEATHERED_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:waxed_weathered_copper',
    result=ItemStackOfComponent(id='minecraft:waxed_weathered_cut_copper_stairs', count=4),
    type='minecraft:stonecutting',
)

WAXED_WEATHERED_CUT_COPPER_STAIRS_FROM_WAXED_WEATHERED_CUT_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:waxed_weathered_cut_copper',
    result=ItemStackOfComponent(id='minecraft:waxed_weathered_cut_copper_stairs'),
    type='minecraft:stonecutting',
)

WAXED_WEATHERED_LIGHTNING_ROD_FROM_HONEYCOMB = RecipeCraftingShapeless(
    group='waxed_lightning_rod',
    category=CraftingBookCategory.BUILDING,
    ingredients=['minecraft:weathered_lightning_rod', 'minecraft:honeycomb'],
    result=ItemStackOfComponent(id='minecraft:waxed_weathered_lightning_rod'),
    type='minecraft:crafting_shapeless',
)

WAYFINDER_ARMOR_TRIM_SMITHING_TEMPLATE = RecipeCraftingShaped(
    pattern=['#S#', '#C#', '###'],
    key={'#': 'minecraft:diamond', 'C': 'minecraft:terracotta', 'S': 'minecraft:wayfinder_armor_trim_smithing_template'},
    result=ItemStackOfComponent(id='minecraft:wayfinder_armor_trim_smithing_template', count=2),
    type='minecraft:crafting_shaped',
)

WAYFINDER_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = RecipeSmithingTrim(
    base='#minecraft:trimmable_armor',
    addition='#minecraft:trim_materials',
    template='minecraft:wayfinder_armor_trim_smithing_template',
    pattern='minecraft:wayfinder',
    type='minecraft:smithing_trim',
)

WEATHERED_CHISELED_COPPER = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#', '#'],
    key={'#': 'minecraft:weathered_cut_copper_slab'},
    result=ItemStackOfComponent(id='minecraft:weathered_chiseled_copper'),
    type='minecraft:crafting_shaped',
)

WEATHERED_CHISELED_COPPER_FROM_WEATHERED_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:weathered_copper',
    result=ItemStackOfComponent(id='minecraft:weathered_chiseled_copper', count=4),
    type='minecraft:stonecutting',
)

WEATHERED_CHISELED_COPPER_FROM_WEATHERED_CUT_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:weathered_cut_copper',
    result=ItemStackOfComponent(id='minecraft:weathered_chiseled_copper'),
    type='minecraft:stonecutting',
)

WEATHERED_COPPER_BULB = RecipeCraftingShaped(
    group='weathered_copper_bulb',
    category=CraftingBookCategory.REDSTONE,
    pattern=[' C ', 'CBC', ' R '],
    key={'B': 'minecraft:blaze_rod', 'C': 'minecraft:weathered_copper', 'R': 'minecraft:redstone'},
    result=ItemStackOfComponent(id='minecraft:weathered_copper_bulb', count=4),
    type='minecraft:crafting_shaped',
)

WEATHERED_COPPER_GRATE = RecipeCraftingShaped(
    group='weathered_copper_grate',
    category=CraftingBookCategory.BUILDING,
    pattern=[' M ', 'M M', ' M '],
    key={'M': 'minecraft:weathered_copper'},
    result=ItemStackOfComponent(id='minecraft:weathered_copper_grate', count=4),
    type='minecraft:crafting_shaped',
)

WEATHERED_COPPER_GRATE_FROM_WEATHERED_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:weathered_copper',
    result=ItemStackOfComponent(id='minecraft:weathered_copper_grate', count=4),
    type='minecraft:stonecutting',
)

WEATHERED_CUT_COPPER = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:weathered_copper'},
    result=ItemStackOfComponent(id='minecraft:weathered_cut_copper', count=4),
    type='minecraft:crafting_shaped',
)

WEATHERED_CUT_COPPER_FROM_WEATHERED_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:weathered_copper',
    result=ItemStackOfComponent(id='minecraft:weathered_cut_copper', count=4),
    type='minecraft:stonecutting',
)

WEATHERED_CUT_COPPER_SLAB = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:weathered_cut_copper'},
    result=ItemStackOfComponent(id='minecraft:weathered_cut_copper_slab', count=6),
    type='minecraft:crafting_shaped',
)

WEATHERED_CUT_COPPER_SLAB_FROM_WEATHERED_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:weathered_copper',
    result=ItemStackOfComponent(id='minecraft:weathered_cut_copper_slab', count=8),
    type='minecraft:stonecutting',
)

WEATHERED_CUT_COPPER_SLAB_FROM_WEATHERED_CUT_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:weathered_cut_copper',
    result=ItemStackOfComponent(id='minecraft:weathered_cut_copper_slab', count=2),
    type='minecraft:stonecutting',
)

WEATHERED_CUT_COPPER_STAIRS = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:weathered_cut_copper'},
    result=ItemStackOfComponent(id='minecraft:weathered_cut_copper_stairs', count=4),
    type='minecraft:crafting_shaped',
)

WEATHERED_CUT_COPPER_STAIRS_FROM_WEATHERED_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:weathered_copper',
    result=ItemStackOfComponent(id='minecraft:weathered_cut_copper_stairs', count=4),
    type='minecraft:stonecutting',
)

WEATHERED_CUT_COPPER_STAIRS_FROM_WEATHERED_CUT_COPPER_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:weathered_cut_copper',
    result=ItemStackOfComponent(id='minecraft:weathered_cut_copper_stairs'),
    type='minecraft:stonecutting',
)

WHEAT = RecipeCraftingShapeless(
    ingredients=['minecraft:hay_block'],
    result=ItemStackOfComponent(id='minecraft:wheat', count=9),
    type='minecraft:crafting_shapeless',
)

WHITE_BANNER = RecipeCraftingShaped(
    group='banner',
    pattern=['###', '###', ' | '],
    key={'#': 'minecraft:white_wool', '|': 'minecraft:stick'},
    result=ItemStackOfComponent(id='minecraft:white_banner'),
    type='minecraft:crafting_shaped',
)

WHITE_BANNER_DUPLICATE = RecipeCraftingSpecialBannerduplicate(
    type='minecraft:crafting_special_bannerduplicate',
    **dict[str, Any]({'banner': 'minecraft:white_banner', 'result': {'id': 'minecraft:white_banner'}}),
)

WHITE_BED = RecipeCraftingShaped(
    group='bed',
    pattern=['###', 'XXX'],
    key={'#': 'minecraft:white_wool', 'X': '#minecraft:planks'},
    result=ItemStackOfComponent(id='minecraft:white_bed'),
    type='minecraft:crafting_shaped',
)

WHITE_BUNDLE = RecipeCraftingTransmute(
    group='bundle_dye',
    category=CraftingBookCategory.EQUIPMENT,
    input='#minecraft:bundles',
    material='minecraft:white_dye',
    result=TransmuteResult(id='minecraft:white_bundle'),
    type='minecraft:crafting_transmute',
)

WHITE_CANDLE = RecipeCraftingShapeless(
    group='dyed_candle',
    ingredients=['minecraft:candle', 'minecraft:white_dye'],
    result=ItemStackOfComponent(id='minecraft:white_candle'),
    type='minecraft:crafting_shapeless',
)

WHITE_CARPET = RecipeCraftingShaped(
    group='woolen_carpet',
    pattern=['##'],
    key={'#': 'minecraft:white_wool'},
    result=ItemStackOfComponent(id='minecraft:white_carpet', count=3),
    type='minecraft:crafting_shaped',
)

WHITE_CONCRETE_POWDER = RecipeCraftingShapeless(
    group='concrete_powder',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:white_dye',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:gravel',
        'minecraft:gravel',
        'minecraft:gravel',
        'minecraft:gravel',
    ],
    result=ItemStackOfComponent(id='minecraft:white_concrete_powder', count=8),
    type='minecraft:crafting_shapeless',
)

WHITE_CONCRETE_SLAB = RecipeCraftingShaped(
    group='concrete_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:white_concrete'},
    result=ItemStackOfComponent(id='minecraft:white_concrete_slab', count=6),
    type='minecraft:crafting_shaped',
)

WHITE_CONCRETE_SLAB_FROM_WHITE_CONCRETE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:white_concrete',
    result=ItemStackOfComponent(id='minecraft:white_concrete_slab', count=2),
    type='minecraft:stonecutting',
)

WHITE_CONCRETE_STAIRS = RecipeCraftingShaped(
    group='concrete_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:white_concrete'},
    result=ItemStackOfComponent(id='minecraft:white_concrete_stairs', count=4),
    type='minecraft:crafting_shaped',
)

WHITE_CONCRETE_STAIRS_FROM_WHITE_CONCRETE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:white_concrete',
    result=ItemStackOfComponent(id='minecraft:white_concrete_stairs'),
    type='minecraft:stonecutting',
)

WHITE_CUSHION = RecipeCraftingShaped(
    group='cushion',
    pattern=['###'],
    key={'#': 'minecraft:white_wool_slab'},
    result=ItemStackOfComponent(id='minecraft:white_cushion'),
    type='minecraft:crafting_shaped',
)

WHITE_DYE = RecipeCraftingShapeless(
    group='white_dye',
    ingredients=['minecraft:bone_meal'],
    result=ItemStackOfComponent(id='minecraft:white_dye'),
    type='minecraft:crafting_shapeless',
)

WHITE_DYE_FROM_LILY_OF_THE_VALLEY = RecipeCraftingShapeless(
    group='white_dye',
    ingredients=['minecraft:lily_of_the_valley'],
    result=ItemStackOfComponent(id='minecraft:white_dye'),
    type='minecraft:crafting_shapeless',
)

WHITE_GLAZED_TERRACOTTA = RecipeSmelting(
    category=CookingBookCategory.BLOCKS,
    ingredient='minecraft:white_terracotta',
    result=ItemStackOfComponent(id='minecraft:white_glazed_terracotta'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

WHITE_HARNESS = RecipeCraftingShaped(
    group='harness',
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['LLL', 'G#G'],
    key={'#': 'minecraft:white_wool', 'G': 'minecraft:glass', 'L': 'minecraft:leather'},
    result=ItemStackOfComponent(id='minecraft:white_harness'),
    type='minecraft:crafting_shaped',
)

WHITE_SHULKER_BOX = RecipeCraftingTransmute(
    group='shulker_box_dye',
    input='#minecraft:shulker_boxes',
    material='minecraft:white_dye',
    result=TransmuteResult(id='minecraft:white_shulker_box'),
    type='minecraft:crafting_transmute',
)

WHITE_STAINED_GLASS = RecipeCraftingShaped(
    group='stained_glass',
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:glass', 'X': 'minecraft:white_dye'},
    result=ItemStackOfComponent(id='minecraft:white_stained_glass', count=8),
    type='minecraft:crafting_shaped',
)

WHITE_STAINED_GLASS_PANE = RecipeCraftingShaped(
    group='stained_glass_pane',
    pattern=['###', '###'],
    key={'#': 'minecraft:white_stained_glass'},
    result=ItemStackOfComponent(id='minecraft:white_stained_glass_pane', count=16),
    type='minecraft:crafting_shaped',
)

WHITE_STAINED_GLASS_PANE_FROM_GLASS_PANE = RecipeCraftingShaped(
    group='stained_glass_pane',
    pattern=['###', '#$#', '###'],
    key={'#': 'minecraft:glass_pane', '$': 'minecraft:white_dye'},
    result=ItemStackOfComponent(id='minecraft:white_stained_glass_pane', count=8),
    type='minecraft:crafting_shaped',
)

WHITE_TERRACOTTA = RecipeCraftingShaped(
    group='stained_terracotta',
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:terracotta', 'X': 'minecraft:white_dye'},
    result=ItemStackOfComponent(id='minecraft:white_terracotta', count=8),
    type='minecraft:crafting_shaped',
)

WHITE_WOOL_FROM_STRING = RecipeCraftingShaped(
    category=CraftingBookCategory.BUILDING,
    pattern=['##', '##'],
    key={'#': 'minecraft:string'},
    result=ItemStackOfComponent(id='minecraft:white_wool'),
    type='minecraft:crafting_shaped',
)

WHITE_WOOL_SLAB = RecipeCraftingShaped(
    group='woolen_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:white_wool'},
    result=ItemStackOfComponent(id='minecraft:white_wool_slab', count=6),
    type='minecraft:crafting_shaped',
)

WHITE_WOOL_STAIRS = RecipeCraftingShaped(
    group='woolen_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:white_wool'},
    result=ItemStackOfComponent(id='minecraft:white_wool_stairs', count=4),
    type='minecraft:crafting_shaped',
)

WILD_ARMOR_TRIM_SMITHING_TEMPLATE = RecipeCraftingShaped(
    pattern=['#S#', '#C#', '###'],
    key={'#': 'minecraft:diamond', 'C': 'minecraft:mossy_cobblestone', 'S': 'minecraft:wild_armor_trim_smithing_template'},
    result=ItemStackOfComponent(id='minecraft:wild_armor_trim_smithing_template', count=2),
    type='minecraft:crafting_shaped',
)

WILD_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = RecipeSmithingTrim(
    base='#minecraft:trimmable_armor',
    addition='#minecraft:trim_materials',
    template='minecraft:wild_armor_trim_smithing_template',
    pattern='minecraft:wild',
    type='minecraft:smithing_trim',
)

WIND_CHARGE = RecipeCraftingShapeless(
    ingredients=['minecraft:breeze_rod'],
    result=ItemStackOfComponent(id='minecraft:wind_charge', count=4),
    type='minecraft:crafting_shapeless',
)

WOLF_ARMOR = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['X  ', 'XXX', 'X X'],
    key={'X': 'minecraft:armadillo_scute'},
    result=ItemStackOfComponent(id='minecraft:wolf_armor'),
    type='minecraft:crafting_shaped',
)

WOLF_ARMOR_DYED = RecipeCraftingDye(
    group='dyed_armor',
    target='minecraft:wolf_armor',
    dye='#minecraft:dyes',
    result=ItemStackOfComponent(id='minecraft:wolf_armor'),
    type='minecraft:crafting_dye',
)

WOODEN_AXE = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['XX', 'X#', ' #'],
    key={'#': 'minecraft:stick', 'X': '#minecraft:wooden_tool_materials'},
    result=ItemStackOfComponent(id='minecraft:wooden_axe'),
    type='minecraft:crafting_shaped',
)

WOODEN_HOE = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['XX', ' #', ' #'],
    key={'#': 'minecraft:stick', 'X': '#minecraft:wooden_tool_materials'},
    result=ItemStackOfComponent(id='minecraft:wooden_hoe'),
    type='minecraft:crafting_shaped',
)

WOODEN_PICKAXE = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['XXX', ' # ', ' # '],
    key={'#': 'minecraft:stick', 'X': '#minecraft:wooden_tool_materials'},
    result=ItemStackOfComponent(id='minecraft:wooden_pickaxe'),
    type='minecraft:crafting_shaped',
)

WOODEN_SHOVEL = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['X', '#', '#'],
    key={'#': 'minecraft:stick', 'X': '#minecraft:wooden_tool_materials'},
    result=ItemStackOfComponent(id='minecraft:wooden_shovel'),
    type='minecraft:crafting_shaped',
)

WOODEN_SPEAR = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['  X', ' # ', '#  '],
    key={'#': 'minecraft:stick', 'X': '#minecraft:wooden_tool_materials'},
    result=ItemStackOfComponent(id='minecraft:wooden_spear'),
    type='minecraft:crafting_shaped',
)

WOODEN_SWORD = RecipeCraftingShaped(
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['X', 'X', '#'],
    key={'#': 'minecraft:stick', 'X': '#minecraft:wooden_tool_materials'},
    result=ItemStackOfComponent(id='minecraft:wooden_sword'),
    type='minecraft:crafting_shaped',
)

WRITABLE_BOOK = RecipeCraftingShapeless(
    ingredients=['minecraft:book', 'minecraft:ink_sac', 'minecraft:feather'],
    result=ItemStackOfComponent(id='minecraft:writable_book'),
    type='minecraft:crafting_shapeless',
)

YELLOW_BANNER = RecipeCraftingShaped(
    group='banner',
    pattern=['###', '###', ' | '],
    key={'#': 'minecraft:yellow_wool', '|': 'minecraft:stick'},
    result=ItemStackOfComponent(id='minecraft:yellow_banner'),
    type='minecraft:crafting_shaped',
)

YELLOW_BANNER_DUPLICATE = RecipeCraftingSpecialBannerduplicate(
    type='minecraft:crafting_special_bannerduplicate',
    **dict[str, Any]({'banner': 'minecraft:yellow_banner', 'result': {'id': 'minecraft:yellow_banner'}}),
)

YELLOW_BED = RecipeCraftingShaped(
    group='bed',
    pattern=['###', 'XXX'],
    key={'#': 'minecraft:yellow_wool', 'X': '#minecraft:planks'},
    result=ItemStackOfComponent(id='minecraft:yellow_bed'),
    type='minecraft:crafting_shaped',
)

YELLOW_BUNDLE = RecipeCraftingTransmute(
    group='bundle_dye',
    category=CraftingBookCategory.EQUIPMENT,
    input='#minecraft:bundles',
    material='minecraft:yellow_dye',
    result=TransmuteResult(id='minecraft:yellow_bundle'),
    type='minecraft:crafting_transmute',
)

YELLOW_CANDLE = RecipeCraftingShapeless(
    group='dyed_candle',
    ingredients=['minecraft:candle', 'minecraft:yellow_dye'],
    result=ItemStackOfComponent(id='minecraft:yellow_candle'),
    type='minecraft:crafting_shapeless',
)

YELLOW_CARPET = RecipeCraftingShaped(
    group='woolen_carpet',
    pattern=['##'],
    key={'#': 'minecraft:yellow_wool'},
    result=ItemStackOfComponent(id='minecraft:yellow_carpet', count=3),
    type='minecraft:crafting_shaped',
)

YELLOW_CONCRETE_POWDER = RecipeCraftingShapeless(
    group='concrete_powder',
    category=CraftingBookCategory.BUILDING,
    ingredients=[
        'minecraft:yellow_dye',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:sand',
        'minecraft:gravel',
        'minecraft:gravel',
        'minecraft:gravel',
        'minecraft:gravel',
    ],
    result=ItemStackOfComponent(id='minecraft:yellow_concrete_powder', count=8),
    type='minecraft:crafting_shapeless',
)

YELLOW_CONCRETE_SLAB = RecipeCraftingShaped(
    group='concrete_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:yellow_concrete'},
    result=ItemStackOfComponent(id='minecraft:yellow_concrete_slab', count=6),
    type='minecraft:crafting_shaped',
)

YELLOW_CONCRETE_SLAB_FROM_YELLOW_CONCRETE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:yellow_concrete',
    result=ItemStackOfComponent(id='minecraft:yellow_concrete_slab', count=2),
    type='minecraft:stonecutting',
)

YELLOW_CONCRETE_STAIRS = RecipeCraftingShaped(
    group='concrete_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:yellow_concrete'},
    result=ItemStackOfComponent(id='minecraft:yellow_concrete_stairs', count=4),
    type='minecraft:crafting_shaped',
)

YELLOW_CONCRETE_STAIRS_FROM_YELLOW_CONCRETE_STONECUTTING = RecipeStonecutting(
    ingredient='minecraft:yellow_concrete',
    result=ItemStackOfComponent(id='minecraft:yellow_concrete_stairs'),
    type='minecraft:stonecutting',
)

YELLOW_CUSHION = RecipeCraftingShaped(
    group='cushion',
    pattern=['###'],
    key={'#': 'minecraft:yellow_wool_slab'},
    result=ItemStackOfComponent(id='minecraft:yellow_cushion'),
    type='minecraft:crafting_shaped',
)

YELLOW_DYE_FROM_DANDELION = RecipeCraftingShapeless(
    group='yellow_dye',
    ingredients=['minecraft:dandelion'],
    result=ItemStackOfComponent(id='minecraft:yellow_dye'),
    type='minecraft:crafting_shapeless',
)

YELLOW_DYE_FROM_GOLDEN_DANDELION = RecipeCraftingShapeless(
    group='yellow_dye',
    ingredients=['minecraft:golden_dandelion'],
    result=ItemStackOfComponent(id='minecraft:yellow_dye'),
    type='minecraft:crafting_shapeless',
)

YELLOW_DYE_FROM_SUNFLOWER = RecipeCraftingShapeless(
    group='yellow_dye',
    ingredients=['minecraft:sunflower'],
    result=ItemStackOfComponent(id='minecraft:yellow_dye', count=2),
    type='minecraft:crafting_shapeless',
)

YELLOW_DYE_FROM_WILDFLOWERS = RecipeCraftingShapeless(
    group='yellow_dye',
    ingredients=['minecraft:wildflowers'],
    result=ItemStackOfComponent(id='minecraft:yellow_dye'),
    type='minecraft:crafting_shapeless',
)

YELLOW_GLAZED_TERRACOTTA = RecipeSmelting(
    category=CookingBookCategory.BLOCKS,
    ingredient='minecraft:yellow_terracotta',
    result=ItemStackOfComponent(id='minecraft:yellow_glazed_terracotta'),
    experience=0.1,
    cookingtime=200,
    type='minecraft:smelting',
)

YELLOW_HARNESS = RecipeCraftingShaped(
    group='harness',
    category=CraftingBookCategory.EQUIPMENT,
    pattern=['LLL', 'G#G'],
    key={'#': 'minecraft:yellow_wool', 'G': 'minecraft:glass', 'L': 'minecraft:leather'},
    result=ItemStackOfComponent(id='minecraft:yellow_harness'),
    type='minecraft:crafting_shaped',
)

YELLOW_SHULKER_BOX = RecipeCraftingTransmute(
    group='shulker_box_dye',
    input='#minecraft:shulker_boxes',
    material='minecraft:yellow_dye',
    result=TransmuteResult(id='minecraft:yellow_shulker_box'),
    type='minecraft:crafting_transmute',
)

YELLOW_STAINED_GLASS = RecipeCraftingShaped(
    group='stained_glass',
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:glass', 'X': 'minecraft:yellow_dye'},
    result=ItemStackOfComponent(id='minecraft:yellow_stained_glass', count=8),
    type='minecraft:crafting_shaped',
)

YELLOW_STAINED_GLASS_PANE = RecipeCraftingShaped(
    group='stained_glass_pane',
    pattern=['###', '###'],
    key={'#': 'minecraft:yellow_stained_glass'},
    result=ItemStackOfComponent(id='minecraft:yellow_stained_glass_pane', count=16),
    type='minecraft:crafting_shaped',
)

YELLOW_STAINED_GLASS_PANE_FROM_GLASS_PANE = RecipeCraftingShaped(
    group='stained_glass_pane',
    pattern=['###', '#$#', '###'],
    key={'#': 'minecraft:glass_pane', '$': 'minecraft:yellow_dye'},
    result=ItemStackOfComponent(id='minecraft:yellow_stained_glass_pane', count=8),
    type='minecraft:crafting_shaped',
)

YELLOW_TERRACOTTA = RecipeCraftingShaped(
    group='stained_terracotta',
    category=CraftingBookCategory.BUILDING,
    pattern=['###', '#X#', '###'],
    key={'#': 'minecraft:terracotta', 'X': 'minecraft:yellow_dye'},
    result=ItemStackOfComponent(id='minecraft:yellow_terracotta', count=8),
    type='minecraft:crafting_shaped',
)

YELLOW_WOOL_SLAB = RecipeCraftingShaped(
    group='woolen_slab',
    category=CraftingBookCategory.BUILDING,
    pattern=['###'],
    key={'#': 'minecraft:yellow_wool'},
    result=ItemStackOfComponent(id='minecraft:yellow_wool_slab', count=6),
    type='minecraft:crafting_shaped',
)

YELLOW_WOOL_STAIRS = RecipeCraftingShaped(
    group='woolen_stairs',
    category=CraftingBookCategory.BUILDING,
    pattern=['#  ', '## ', '###'],
    key={'#': 'minecraft:yellow_wool'},
    result=ItemStackOfComponent(id='minecraft:yellow_wool_stairs', count=4),
    type='minecraft:crafting_shaped',
)
