"""Vanilla's data/recipe/brewing/ files"""
from vanilla_mcdoc.data.recipe.PotionIngredient import PotionIngredient
from vanilla_mcdoc.data.recipe.Recipe import RecipeBrewing
from vanilla_mcdoc.world.component.DataComponentPatch import DataComponentPatch
from vanilla_mcdoc.world.component.item.PotionContents import PotionContents
from vanilla_mcdoc.world.component.predicate.PotionsPredicate import PotionsPredicate
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

LINGERING_POTION_AWKWARD_BLAZE_POWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:blaze_powder'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strength')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_AWKWARD_BREEZE_ROD = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:breeze_rod'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:wind_charged')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_AWKWARD_COBWEB = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:cobweb'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:weaving')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_AWKWARD_GHAST_TEAR = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:ghast_tear'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:regeneration')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_AWKWARD_GLISTERING_MELON_SLICE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:glistering_melon_slice'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:healing')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_AWKWARD_GOLDEN_CARROT = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:golden_carrot'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:night_vision')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_AWKWARD_ICE_BALL = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:ice_ball'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:freezing')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_AWKWARD_MAGMA_CREAM = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:magma_cream'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:fire_resistance')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_AWKWARD_PHANTOM_MEMBRANE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:phantom_membrane'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:slow_falling')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_AWKWARD_PUFFERFISH = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:pufferfish'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:water_breathing')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_AWKWARD_RABBIT_FOOT = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:rabbit_foot'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:leaping')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_AWKWARD_SLIME_BLOCK = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:slime_block'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:oozing')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_AWKWARD_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:poison')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_AWKWARD_STONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:stone'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:infested')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_AWKWARD_SUGAR = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:sugar'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:swiftness')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_AWKWARD_TURTLE_HELMET = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:turtle_helmet'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:turtle_master')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_FIRE_RESISTANCE_REDSTONE = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:lingering_potion',
        potion_contents=PotionsPredicate(potions='minecraft:fire_resistance'),
    ),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_fire_resistance')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_FREEZING_REDSTONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:freezing')),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_freezing')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_HARMING_GLOWSTONE_DUST = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:harming')),
    reagent=PotionIngredient(item='minecraft:glowstone_dust'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_harming')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_HEALING_FERMENTED_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:healing')),
    reagent=PotionIngredient(item='minecraft:fermented_spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:harming')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_HEALING_GLOWSTONE_DUST = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:healing')),
    reagent=PotionIngredient(item='minecraft:glowstone_dust'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_healing')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_INVISIBILITY_REDSTONE = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:lingering_potion',
        potion_contents=PotionsPredicate(potions='minecraft:invisibility'),
    ),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_invisibility')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_LEAPING_FERMENTED_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:leaping')),
    reagent=PotionIngredient(item='minecraft:fermented_spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:slowness')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_LEAPING_GLOWSTONE_DUST = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:leaping')),
    reagent=PotionIngredient(item='minecraft:glowstone_dust'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_leaping')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_LEAPING_REDSTONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:leaping')),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_leaping')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_LONG_LEAPING_FERMENTED_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:lingering_potion',
        potion_contents=PotionsPredicate(potions='minecraft:long_leaping'),
    ),
    reagent=PotionIngredient(item='minecraft:fermented_spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_slowness')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_LONG_NIGHT_VISION_FERMENTED_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:lingering_potion',
        potion_contents=PotionsPredicate(potions='minecraft:long_night_vision'),
    ),
    reagent=PotionIngredient(item='minecraft:fermented_spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_invisibility')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_LONG_POISON_FERMENTED_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:lingering_potion',
        potion_contents=PotionsPredicate(potions='minecraft:long_poison'),
    ),
    reagent=PotionIngredient(item='minecraft:fermented_spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:harming')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_LONG_SWIFTNESS_FERMENTED_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:lingering_potion',
        potion_contents=PotionsPredicate(potions='minecraft:long_swiftness'),
    ),
    reagent=PotionIngredient(item='minecraft:fermented_spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_slowness')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_NIGHT_VISION_FERMENTED_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:lingering_potion',
        potion_contents=PotionsPredicate(potions='minecraft:night_vision'),
    ),
    reagent=PotionIngredient(item='minecraft:fermented_spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:invisibility')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_NIGHT_VISION_REDSTONE = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:lingering_potion',
        potion_contents=PotionsPredicate(potions='minecraft:night_vision'),
    ),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_night_vision')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_POISON_FERMENTED_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:poison')),
    reagent=PotionIngredient(item='minecraft:fermented_spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:harming')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_POISON_GLOWSTONE_DUST = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:poison')),
    reagent=PotionIngredient(item='minecraft:glowstone_dust'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_poison')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_POISON_REDSTONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:poison')),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_poison')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_REGENERATION_GLOWSTONE_DUST = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:lingering_potion',
        potion_contents=PotionsPredicate(potions='minecraft:regeneration'),
    ),
    reagent=PotionIngredient(item='minecraft:glowstone_dust'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_regeneration')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_REGENERATION_REDSTONE = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:lingering_potion',
        potion_contents=PotionsPredicate(potions='minecraft:regeneration'),
    ),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_regeneration')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_SLOWNESS_GLOWSTONE_DUST = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:slowness')),
    reagent=PotionIngredient(item='minecraft:glowstone_dust'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_slowness')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_SLOWNESS_REDSTONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:slowness')),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_slowness')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_SLOW_FALLING_REDSTONE = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:lingering_potion',
        potion_contents=PotionsPredicate(potions='minecraft:slow_falling'),
    ),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_slow_falling')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_STRENGTH_GLOWSTONE_DUST = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:strength')),
    reagent=PotionIngredient(item='minecraft:glowstone_dust'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_strength')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_STRENGTH_REDSTONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:strength')),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_strength')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_STRONG_HEALING_FERMENTED_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:lingering_potion',
        potion_contents=PotionsPredicate(potions='minecraft:strong_healing'),
    ),
    reagent=PotionIngredient(item='minecraft:fermented_spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_harming')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_STRONG_POISON_FERMENTED_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:lingering_potion',
        potion_contents=PotionsPredicate(potions='minecraft:strong_poison'),
    ),
    reagent=PotionIngredient(item='minecraft:fermented_spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_harming')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_SWIFTNESS_FERMENTED_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:swiftness')),
    reagent=PotionIngredient(item='minecraft:fermented_spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:slowness')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_SWIFTNESS_GLOWSTONE_DUST = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:swiftness')),
    reagent=PotionIngredient(item='minecraft:glowstone_dust'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_swiftness')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_SWIFTNESS_REDSTONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:swiftness')),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_swiftness')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_TURTLE_MASTER_GLOWSTONE_DUST = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:lingering_potion',
        potion_contents=PotionsPredicate(potions='minecraft:turtle_master'),
    ),
    reagent=PotionIngredient(item='minecraft:glowstone_dust'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_turtle_master')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_TURTLE_MASTER_REDSTONE = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:lingering_potion',
        potion_contents=PotionsPredicate(potions='minecraft:turtle_master'),
    ),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_turtle_master')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_WATER_BLAZE_POWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:blaze_powder'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_WATER_BREATHING_REDSTONE = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:lingering_potion',
        potion_contents=PotionsPredicate(potions='minecraft:water_breathing'),
    ),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_water_breathing')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_WATER_BREEZE_ROD = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:breeze_rod'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_WATER_COBWEB = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:cobweb'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_WATER_FERMENTED_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:fermented_spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:weakness')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_WATER_GHAST_TEAR = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:ghast_tear'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_WATER_GLISTERING_MELON_SLICE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:glistering_melon_slice'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_WATER_GLOWSTONE_DUST = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:glowstone_dust'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:thick')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_WATER_ICE_BALL = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:ice_ball'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_WATER_MAGMA_CREAM = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:magma_cream'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_WATER_NETHER_WART = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:nether_wart'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:awkward')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_WATER_RABBIT_FOOT = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:rabbit_foot'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_WATER_REDSTONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_WATER_SLIME_BLOCK = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:slime_block'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_WATER_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_WATER_STONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:stone'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_WATER_SUGAR = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:sugar'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

LINGERING_POTION_WEAKNESS_REDSTONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:lingering_potion', potion_contents=PotionsPredicate(potions='minecraft:weakness')),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_weakness')),
    ),
    type='minecraft:brewing',
)

POTION_AWKWARD_BLAZE_POWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:blaze_powder'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strength')),
    ),
    type='minecraft:brewing',
)

POTION_AWKWARD_BREEZE_ROD = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:breeze_rod'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:wind_charged')),
    ),
    type='minecraft:brewing',
)

POTION_AWKWARD_COBWEB = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:cobweb'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:weaving')),
    ),
    type='minecraft:brewing',
)

POTION_AWKWARD_GHAST_TEAR = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:ghast_tear'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:regeneration')),
    ),
    type='minecraft:brewing',
)

POTION_AWKWARD_GLISTERING_MELON_SLICE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:glistering_melon_slice'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:healing')),
    ),
    type='minecraft:brewing',
)

POTION_AWKWARD_GOLDEN_CARROT = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:golden_carrot'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:night_vision')),
    ),
    type='minecraft:brewing',
)

POTION_AWKWARD_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:awkward')),
    ),
    type='minecraft:brewing',
)

POTION_AWKWARD_ICE_BALL = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:ice_ball'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:freezing')),
    ),
    type='minecraft:brewing',
)

POTION_AWKWARD_MAGMA_CREAM = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:magma_cream'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:fire_resistance')),
    ),
    type='minecraft:brewing',
)

POTION_AWKWARD_PHANTOM_MEMBRANE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:phantom_membrane'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:slow_falling')),
    ),
    type='minecraft:brewing',
)

POTION_AWKWARD_PUFFERFISH = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:pufferfish'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:water_breathing')),
    ),
    type='minecraft:brewing',
)

POTION_AWKWARD_RABBIT_FOOT = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:rabbit_foot'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:leaping')),
    ),
    type='minecraft:brewing',
)

POTION_AWKWARD_SLIME_BLOCK = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:slime_block'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:oozing')),
    ),
    type='minecraft:brewing',
)

POTION_AWKWARD_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:poison')),
    ),
    type='minecraft:brewing',
)

POTION_AWKWARD_STONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:stone'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:infested')),
    ),
    type='minecraft:brewing',
)

POTION_AWKWARD_SUGAR = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:sugar'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:swiftness')),
    ),
    type='minecraft:brewing',
)

POTION_AWKWARD_TURTLE_HELMET = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:turtle_helmet'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:turtle_master')),
    ),
    type='minecraft:brewing',
)

POTION_FIRE_RESISTANCE_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:fire_resistance')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:fire_resistance')),
    ),
    type='minecraft:brewing',
)

POTION_FIRE_RESISTANCE_REDSTONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:fire_resistance')),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_fire_resistance')),
    ),
    type='minecraft:brewing',
)

POTION_FREEZING_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:freezing')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:freezing')),
    ),
    type='minecraft:brewing',
)

POTION_FREEZING_REDSTONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:freezing')),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_freezing')),
    ),
    type='minecraft:brewing',
)

POTION_HARMING_GLOWSTONE_DUST = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:harming')),
    reagent=PotionIngredient(item='minecraft:glowstone_dust'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_harming')),
    ),
    type='minecraft:brewing',
)

POTION_HARMING_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:harming')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:harming')),
    ),
    type='minecraft:brewing',
)

POTION_HEALING_FERMENTED_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:healing')),
    reagent=PotionIngredient(item='minecraft:fermented_spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:harming')),
    ),
    type='minecraft:brewing',
)

POTION_HEALING_GLOWSTONE_DUST = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:healing')),
    reagent=PotionIngredient(item='minecraft:glowstone_dust'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_healing')),
    ),
    type='minecraft:brewing',
)

POTION_HEALING_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:healing')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:healing')),
    ),
    type='minecraft:brewing',
)

POTION_INFESTED_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:infested')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:infested')),
    ),
    type='minecraft:brewing',
)

POTION_INVISIBILITY_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:invisibility')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:invisibility')),
    ),
    type='minecraft:brewing',
)

POTION_INVISIBILITY_REDSTONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:invisibility')),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_invisibility')),
    ),
    type='minecraft:brewing',
)

POTION_LEAPING_FERMENTED_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:leaping')),
    reagent=PotionIngredient(item='minecraft:fermented_spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:slowness')),
    ),
    type='minecraft:brewing',
)

POTION_LEAPING_GLOWSTONE_DUST = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:leaping')),
    reagent=PotionIngredient(item='minecraft:glowstone_dust'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_leaping')),
    ),
    type='minecraft:brewing',
)

POTION_LEAPING_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:leaping')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:leaping')),
    ),
    type='minecraft:brewing',
)

POTION_LEAPING_REDSTONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:leaping')),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_leaping')),
    ),
    type='minecraft:brewing',
)

POTION_LONG_FIRE_RESISTANCE_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:potion',
        potion_contents=PotionsPredicate(potions='minecraft:long_fire_resistance'),
    ),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_fire_resistance')),
    ),
    type='minecraft:brewing',
)

POTION_LONG_FREEZING_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:long_freezing')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_freezing')),
    ),
    type='minecraft:brewing',
)

POTION_LONG_INVISIBILITY_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:long_invisibility')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_invisibility')),
    ),
    type='minecraft:brewing',
)

POTION_LONG_LEAPING_FERMENTED_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:long_leaping')),
    reagent=PotionIngredient(item='minecraft:fermented_spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_slowness')),
    ),
    type='minecraft:brewing',
)

POTION_LONG_LEAPING_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:long_leaping')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_leaping')),
    ),
    type='minecraft:brewing',
)

POTION_LONG_NIGHT_VISION_FERMENTED_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:long_night_vision')),
    reagent=PotionIngredient(item='minecraft:fermented_spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_invisibility')),
    ),
    type='minecraft:brewing',
)

POTION_LONG_NIGHT_VISION_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:long_night_vision')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_night_vision')),
    ),
    type='minecraft:brewing',
)

POTION_LONG_POISON_FERMENTED_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:long_poison')),
    reagent=PotionIngredient(item='minecraft:fermented_spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:harming')),
    ),
    type='minecraft:brewing',
)

POTION_LONG_POISON_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:long_poison')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_poison')),
    ),
    type='minecraft:brewing',
)

POTION_LONG_REGENERATION_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:long_regeneration')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_regeneration')),
    ),
    type='minecraft:brewing',
)

POTION_LONG_SLOWNESS_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:long_slowness')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_slowness')),
    ),
    type='minecraft:brewing',
)

POTION_LONG_SLOW_FALLING_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:long_slow_falling')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_slow_falling')),
    ),
    type='minecraft:brewing',
)

POTION_LONG_STRENGTH_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:long_strength')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_strength')),
    ),
    type='minecraft:brewing',
)

POTION_LONG_SWIFTNESS_FERMENTED_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:long_swiftness')),
    reagent=PotionIngredient(item='minecraft:fermented_spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_slowness')),
    ),
    type='minecraft:brewing',
)

POTION_LONG_SWIFTNESS_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:long_swiftness')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_swiftness')),
    ),
    type='minecraft:brewing',
)

POTION_LONG_TURTLE_MASTER_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:long_turtle_master')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_turtle_master')),
    ),
    type='minecraft:brewing',
)

POTION_LONG_WATER_BREATHING_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:potion',
        potion_contents=PotionsPredicate(potions='minecraft:long_water_breathing'),
    ),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_water_breathing')),
    ),
    type='minecraft:brewing',
)

POTION_LONG_WEAKNESS_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:long_weakness')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_weakness')),
    ),
    type='minecraft:brewing',
)

POTION_MUNDANE_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:mundane')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

POTION_NIGHT_VISION_FERMENTED_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:night_vision')),
    reagent=PotionIngredient(item='minecraft:fermented_spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:invisibility')),
    ),
    type='minecraft:brewing',
)

POTION_NIGHT_VISION_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:night_vision')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:night_vision')),
    ),
    type='minecraft:brewing',
)

POTION_NIGHT_VISION_REDSTONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:night_vision')),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_night_vision')),
    ),
    type='minecraft:brewing',
)

POTION_OOZING_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:oozing')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:oozing')),
    ),
    type='minecraft:brewing',
)

POTION_POISON_FERMENTED_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:poison')),
    reagent=PotionIngredient(item='minecraft:fermented_spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:harming')),
    ),
    type='minecraft:brewing',
)

POTION_POISON_GLOWSTONE_DUST = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:poison')),
    reagent=PotionIngredient(item='minecraft:glowstone_dust'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_poison')),
    ),
    type='minecraft:brewing',
)

POTION_POISON_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:poison')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:poison')),
    ),
    type='minecraft:brewing',
)

POTION_POISON_REDSTONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:poison')),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_poison')),
    ),
    type='minecraft:brewing',
)

POTION_REGENERATION_GLOWSTONE_DUST = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:regeneration')),
    reagent=PotionIngredient(item='minecraft:glowstone_dust'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_regeneration')),
    ),
    type='minecraft:brewing',
)

POTION_REGENERATION_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:regeneration')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:regeneration')),
    ),
    type='minecraft:brewing',
)

POTION_REGENERATION_REDSTONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:regeneration')),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_regeneration')),
    ),
    type='minecraft:brewing',
)

POTION_SLOWNESS_GLOWSTONE_DUST = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:slowness')),
    reagent=PotionIngredient(item='minecraft:glowstone_dust'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_slowness')),
    ),
    type='minecraft:brewing',
)

POTION_SLOWNESS_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:slowness')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:slowness')),
    ),
    type='minecraft:brewing',
)

POTION_SLOWNESS_REDSTONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:slowness')),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_slowness')),
    ),
    type='minecraft:brewing',
)

POTION_SLOW_FALLING_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:slow_falling')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:slow_falling')),
    ),
    type='minecraft:brewing',
)

POTION_SLOW_FALLING_REDSTONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:slow_falling')),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_slow_falling')),
    ),
    type='minecraft:brewing',
)

POTION_STRENGTH_GLOWSTONE_DUST = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:strength')),
    reagent=PotionIngredient(item='minecraft:glowstone_dust'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_strength')),
    ),
    type='minecraft:brewing',
)

POTION_STRENGTH_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:strength')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strength')),
    ),
    type='minecraft:brewing',
)

POTION_STRENGTH_REDSTONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:strength')),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_strength')),
    ),
    type='minecraft:brewing',
)

POTION_STRONG_HARMING_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:strong_harming')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_harming')),
    ),
    type='minecraft:brewing',
)

POTION_STRONG_HEALING_FERMENTED_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:strong_healing')),
    reagent=PotionIngredient(item='minecraft:fermented_spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_harming')),
    ),
    type='minecraft:brewing',
)

POTION_STRONG_HEALING_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:strong_healing')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_healing')),
    ),
    type='minecraft:brewing',
)

POTION_STRONG_LEAPING_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:strong_leaping')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_leaping')),
    ),
    type='minecraft:brewing',
)

POTION_STRONG_POISON_FERMENTED_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:strong_poison')),
    reagent=PotionIngredient(item='minecraft:fermented_spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_harming')),
    ),
    type='minecraft:brewing',
)

POTION_STRONG_POISON_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:strong_poison')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_poison')),
    ),
    type='minecraft:brewing',
)

POTION_STRONG_REGENERATION_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:strong_regeneration')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_regeneration')),
    ),
    type='minecraft:brewing',
)

POTION_STRONG_SLOWNESS_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:strong_slowness')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_slowness')),
    ),
    type='minecraft:brewing',
)

POTION_STRONG_STRENGTH_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:strong_strength')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_strength')),
    ),
    type='minecraft:brewing',
)

POTION_STRONG_SWIFTNESS_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:strong_swiftness')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_swiftness')),
    ),
    type='minecraft:brewing',
)

POTION_STRONG_TURTLE_MASTER_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:potion',
        potion_contents=PotionsPredicate(potions='minecraft:strong_turtle_master'),
    ),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_turtle_master')),
    ),
    type='minecraft:brewing',
)

POTION_SWIFTNESS_FERMENTED_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:swiftness')),
    reagent=PotionIngredient(item='minecraft:fermented_spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:slowness')),
    ),
    type='minecraft:brewing',
)

POTION_SWIFTNESS_GLOWSTONE_DUST = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:swiftness')),
    reagent=PotionIngredient(item='minecraft:glowstone_dust'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_swiftness')),
    ),
    type='minecraft:brewing',
)

POTION_SWIFTNESS_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:swiftness')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:swiftness')),
    ),
    type='minecraft:brewing',
)

POTION_SWIFTNESS_REDSTONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:swiftness')),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_swiftness')),
    ),
    type='minecraft:brewing',
)

POTION_THICK_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:thick')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:thick')),
    ),
    type='minecraft:brewing',
)

POTION_TURTLE_MASTER_GLOWSTONE_DUST = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:turtle_master')),
    reagent=PotionIngredient(item='minecraft:glowstone_dust'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_turtle_master')),
    ),
    type='minecraft:brewing',
)

POTION_TURTLE_MASTER_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:turtle_master')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:turtle_master')),
    ),
    type='minecraft:brewing',
)

POTION_TURTLE_MASTER_REDSTONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:turtle_master')),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_turtle_master')),
    ),
    type='minecraft:brewing',
)

POTION_WATER_BLAZE_POWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:blaze_powder'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

POTION_WATER_BREATHING_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:water_breathing')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:water_breathing')),
    ),
    type='minecraft:brewing',
)

POTION_WATER_BREATHING_REDSTONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:water_breathing')),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_water_breathing')),
    ),
    type='minecraft:brewing',
)

POTION_WATER_BREEZE_ROD = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:breeze_rod'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

POTION_WATER_COBWEB = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:cobweb'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

POTION_WATER_FERMENTED_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:fermented_spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:weakness')),
    ),
    type='minecraft:brewing',
)

POTION_WATER_GHAST_TEAR = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:ghast_tear'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

POTION_WATER_GLISTERING_MELON_SLICE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:glistering_melon_slice'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

POTION_WATER_GLOWSTONE_DUST = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:glowstone_dust'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:thick')),
    ),
    type='minecraft:brewing',
)

POTION_WATER_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:water')),
    ),
    type='minecraft:brewing',
)

POTION_WATER_ICE_BALL = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:ice_ball'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

POTION_WATER_MAGMA_CREAM = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:magma_cream'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

POTION_WATER_NETHER_WART = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:nether_wart'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:awkward')),
    ),
    type='minecraft:brewing',
)

POTION_WATER_RABBIT_FOOT = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:rabbit_foot'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

POTION_WATER_REDSTONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

POTION_WATER_SLIME_BLOCK = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:slime_block'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

POTION_WATER_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

POTION_WATER_STONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:stone'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

POTION_WATER_SUGAR = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:sugar'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

POTION_WEAKNESS_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:weakness')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:weakness')),
    ),
    type='minecraft:brewing',
)

POTION_WEAKNESS_REDSTONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:weakness')),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_weakness')),
    ),
    type='minecraft:brewing',
)

POTION_WEAVING_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:weaving')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:weaving')),
    ),
    type='minecraft:brewing',
)

POTION_WIND_CHARGED_GUNPOWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:potion', potion_contents=PotionsPredicate(potions='minecraft:wind_charged')),
    reagent=PotionIngredient(item='minecraft:gunpowder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:wind_charged')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_AWKWARD_BLAZE_POWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:blaze_powder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strength')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_AWKWARD_BREEZE_ROD = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:breeze_rod'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:wind_charged')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_AWKWARD_COBWEB = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:cobweb'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:weaving')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_AWKWARD_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:awkward')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_AWKWARD_GHAST_TEAR = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:ghast_tear'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:regeneration')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_AWKWARD_GLISTERING_MELON_SLICE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:glistering_melon_slice'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:healing')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_AWKWARD_GOLDEN_CARROT = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:golden_carrot'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:night_vision')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_AWKWARD_ICE_BALL = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:ice_ball'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:freezing')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_AWKWARD_MAGMA_CREAM = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:magma_cream'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:fire_resistance')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_AWKWARD_PHANTOM_MEMBRANE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:phantom_membrane'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:slow_falling')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_AWKWARD_PUFFERFISH = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:pufferfish'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:water_breathing')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_AWKWARD_RABBIT_FOOT = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:rabbit_foot'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:leaping')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_AWKWARD_SLIME_BLOCK = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:slime_block'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:oozing')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_AWKWARD_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:poison')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_AWKWARD_STONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:stone'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:infested')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_AWKWARD_SUGAR = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:sugar'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:swiftness')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_AWKWARD_TURTLE_HELMET = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:awkward')),
    reagent=PotionIngredient(item='minecraft:turtle_helmet'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:turtle_master')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_FIRE_RESISTANCE_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:splash_potion',
        potion_contents=PotionsPredicate(potions='minecraft:fire_resistance'),
    ),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:fire_resistance')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_FIRE_RESISTANCE_REDSTONE = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:splash_potion',
        potion_contents=PotionsPredicate(potions='minecraft:fire_resistance'),
    ),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_fire_resistance')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_FREEZING_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:freezing')),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:freezing')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_FREEZING_REDSTONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:freezing')),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_freezing')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_HARMING_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:harming')),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:harming')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_HARMING_GLOWSTONE_DUST = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:harming')),
    reagent=PotionIngredient(item='minecraft:glowstone_dust'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_harming')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_HEALING_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:healing')),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:healing')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_HEALING_FERMENTED_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:healing')),
    reagent=PotionIngredient(item='minecraft:fermented_spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:harming')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_HEALING_GLOWSTONE_DUST = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:healing')),
    reagent=PotionIngredient(item='minecraft:glowstone_dust'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_healing')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_INFESTED_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:infested')),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:infested')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_INVISIBILITY_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:invisibility')),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:invisibility')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_INVISIBILITY_REDSTONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:invisibility')),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_invisibility')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_LEAPING_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:leaping')),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:leaping')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_LEAPING_FERMENTED_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:leaping')),
    reagent=PotionIngredient(item='minecraft:fermented_spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:slowness')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_LEAPING_GLOWSTONE_DUST = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:leaping')),
    reagent=PotionIngredient(item='minecraft:glowstone_dust'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_leaping')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_LEAPING_REDSTONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:leaping')),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_leaping')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_LONG_FIRE_RESISTANCE_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:splash_potion',
        potion_contents=PotionsPredicate(potions='minecraft:long_fire_resistance'),
    ),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_fire_resistance')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_LONG_FREEZING_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:splash_potion',
        potion_contents=PotionsPredicate(potions='minecraft:long_freezing'),
    ),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_freezing')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_LONG_INVISIBILITY_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:splash_potion',
        potion_contents=PotionsPredicate(potions='minecraft:long_invisibility'),
    ),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_invisibility')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_LONG_LEAPING_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:long_leaping')),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_leaping')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_LONG_LEAPING_FERMENTED_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:long_leaping')),
    reagent=PotionIngredient(item='minecraft:fermented_spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_slowness')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_LONG_NIGHT_VISION_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:splash_potion',
        potion_contents=PotionsPredicate(potions='minecraft:long_night_vision'),
    ),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_night_vision')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_LONG_NIGHT_VISION_FERMENTED_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:splash_potion',
        potion_contents=PotionsPredicate(potions='minecraft:long_night_vision'),
    ),
    reagent=PotionIngredient(item='minecraft:fermented_spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_invisibility')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_LONG_POISON_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:long_poison')),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_poison')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_LONG_POISON_FERMENTED_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:long_poison')),
    reagent=PotionIngredient(item='minecraft:fermented_spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:harming')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_LONG_REGENERATION_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:splash_potion',
        potion_contents=PotionsPredicate(potions='minecraft:long_regeneration'),
    ),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_regeneration')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_LONG_SLOWNESS_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:splash_potion',
        potion_contents=PotionsPredicate(potions='minecraft:long_slowness'),
    ),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_slowness')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_LONG_SLOW_FALLING_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:splash_potion',
        potion_contents=PotionsPredicate(potions='minecraft:long_slow_falling'),
    ),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_slow_falling')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_LONG_STRENGTH_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:splash_potion',
        potion_contents=PotionsPredicate(potions='minecraft:long_strength'),
    ),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_strength')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_LONG_SWIFTNESS_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:splash_potion',
        potion_contents=PotionsPredicate(potions='minecraft:long_swiftness'),
    ),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_swiftness')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_LONG_SWIFTNESS_FERMENTED_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:splash_potion',
        potion_contents=PotionsPredicate(potions='minecraft:long_swiftness'),
    ),
    reagent=PotionIngredient(item='minecraft:fermented_spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_slowness')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_LONG_TURTLE_MASTER_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:splash_potion',
        potion_contents=PotionsPredicate(potions='minecraft:long_turtle_master'),
    ),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_turtle_master')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_LONG_WATER_BREATHING_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:splash_potion',
        potion_contents=PotionsPredicate(potions='minecraft:long_water_breathing'),
    ),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_water_breathing')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_LONG_WEAKNESS_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:splash_potion',
        potion_contents=PotionsPredicate(potions='minecraft:long_weakness'),
    ),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_weakness')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_MUNDANE_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:mundane')),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_NIGHT_VISION_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:night_vision')),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:night_vision')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_NIGHT_VISION_FERMENTED_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:night_vision')),
    reagent=PotionIngredient(item='minecraft:fermented_spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:invisibility')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_NIGHT_VISION_REDSTONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:night_vision')),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_night_vision')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_OOZING_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:oozing')),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:oozing')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_POISON_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:poison')),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:poison')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_POISON_FERMENTED_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:poison')),
    reagent=PotionIngredient(item='minecraft:fermented_spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:harming')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_POISON_GLOWSTONE_DUST = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:poison')),
    reagent=PotionIngredient(item='minecraft:glowstone_dust'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_poison')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_POISON_REDSTONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:poison')),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_poison')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_REGENERATION_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:regeneration')),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:regeneration')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_REGENERATION_GLOWSTONE_DUST = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:regeneration')),
    reagent=PotionIngredient(item='minecraft:glowstone_dust'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_regeneration')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_REGENERATION_REDSTONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:regeneration')),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_regeneration')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_SLOWNESS_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:slowness')),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:slowness')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_SLOWNESS_GLOWSTONE_DUST = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:slowness')),
    reagent=PotionIngredient(item='minecraft:glowstone_dust'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_slowness')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_SLOWNESS_REDSTONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:slowness')),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_slowness')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_SLOW_FALLING_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:slow_falling')),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:slow_falling')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_SLOW_FALLING_REDSTONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:slow_falling')),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_slow_falling')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_STRENGTH_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:strength')),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strength')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_STRENGTH_GLOWSTONE_DUST = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:strength')),
    reagent=PotionIngredient(item='minecraft:glowstone_dust'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_strength')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_STRENGTH_REDSTONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:strength')),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_strength')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_STRONG_HARMING_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:splash_potion',
        potion_contents=PotionsPredicate(potions='minecraft:strong_harming'),
    ),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_harming')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_STRONG_HEALING_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:splash_potion',
        potion_contents=PotionsPredicate(potions='minecraft:strong_healing'),
    ),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_healing')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_STRONG_HEALING_FERMENTED_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:splash_potion',
        potion_contents=PotionsPredicate(potions='minecraft:strong_healing'),
    ),
    reagent=PotionIngredient(item='minecraft:fermented_spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_harming')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_STRONG_LEAPING_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:splash_potion',
        potion_contents=PotionsPredicate(potions='minecraft:strong_leaping'),
    ),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_leaping')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_STRONG_POISON_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:splash_potion',
        potion_contents=PotionsPredicate(potions='minecraft:strong_poison'),
    ),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_poison')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_STRONG_POISON_FERMENTED_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:splash_potion',
        potion_contents=PotionsPredicate(potions='minecraft:strong_poison'),
    ),
    reagent=PotionIngredient(item='minecraft:fermented_spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_harming')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_STRONG_REGENERATION_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:splash_potion',
        potion_contents=PotionsPredicate(potions='minecraft:strong_regeneration'),
    ),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_regeneration')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_STRONG_SLOWNESS_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:splash_potion',
        potion_contents=PotionsPredicate(potions='minecraft:strong_slowness'),
    ),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_slowness')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_STRONG_STRENGTH_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:splash_potion',
        potion_contents=PotionsPredicate(potions='minecraft:strong_strength'),
    ),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_strength')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_STRONG_SWIFTNESS_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:splash_potion',
        potion_contents=PotionsPredicate(potions='minecraft:strong_swiftness'),
    ),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_swiftness')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_STRONG_TURTLE_MASTER_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:splash_potion',
        potion_contents=PotionsPredicate(potions='minecraft:strong_turtle_master'),
    ),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_turtle_master')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_SWIFTNESS_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:swiftness')),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:swiftness')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_SWIFTNESS_FERMENTED_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:swiftness')),
    reagent=PotionIngredient(item='minecraft:fermented_spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:slowness')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_SWIFTNESS_GLOWSTONE_DUST = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:swiftness')),
    reagent=PotionIngredient(item='minecraft:glowstone_dust'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_swiftness')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_SWIFTNESS_REDSTONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:swiftness')),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_swiftness')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_THICK_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:thick')),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:thick')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_TURTLE_MASTER_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:splash_potion',
        potion_contents=PotionsPredicate(potions='minecraft:turtle_master'),
    ),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:turtle_master')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_TURTLE_MASTER_GLOWSTONE_DUST = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:splash_potion',
        potion_contents=PotionsPredicate(potions='minecraft:turtle_master'),
    ),
    reagent=PotionIngredient(item='minecraft:glowstone_dust'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:strong_turtle_master')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_TURTLE_MASTER_REDSTONE = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:splash_potion',
        potion_contents=PotionsPredicate(potions='minecraft:turtle_master'),
    ),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_turtle_master')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_WATER_BLAZE_POWDER = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:blaze_powder'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_WATER_BREATHING_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:splash_potion',
        potion_contents=PotionsPredicate(potions='minecraft:water_breathing'),
    ),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:water_breathing')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_WATER_BREATHING_REDSTONE = RecipeBrewing(
    input=PotionIngredient(
        item='minecraft:splash_potion',
        potion_contents=PotionsPredicate(potions='minecraft:water_breathing'),
    ),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_water_breathing')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_WATER_BREEZE_ROD = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:breeze_rod'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_WATER_COBWEB = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:cobweb'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_WATER_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:water')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_WATER_FERMENTED_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:fermented_spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:weakness')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_WATER_GHAST_TEAR = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:ghast_tear'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_WATER_GLISTERING_MELON_SLICE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:glistering_melon_slice'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_WATER_GLOWSTONE_DUST = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:glowstone_dust'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:thick')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_WATER_ICE_BALL = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:ice_ball'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_WATER_MAGMA_CREAM = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:magma_cream'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_WATER_NETHER_WART = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:nether_wart'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:awkward')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_WATER_RABBIT_FOOT = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:rabbit_foot'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_WATER_REDSTONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_WATER_SLIME_BLOCK = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:slime_block'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_WATER_SPIDER_EYE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:spider_eye'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_WATER_STONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:stone'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_WATER_SUGAR = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:water')),
    reagent=PotionIngredient(item='minecraft:sugar'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:mundane')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_WEAKNESS_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:weakness')),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:weakness')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_WEAKNESS_REDSTONE = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:weakness')),
    reagent=PotionIngredient(item='minecraft:redstone'),
    output=ItemStackOfComponent(
        id='minecraft:splash_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:long_weakness')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_WEAVING_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:weaving')),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:weaving')),
    ),
    type='minecraft:brewing',
)

SPLASH_POTION_WIND_CHARGED_DRAGON_BREATH = RecipeBrewing(
    input=PotionIngredient(item='minecraft:splash_potion', potion_contents=PotionsPredicate(potions='minecraft:wind_charged')),
    reagent=PotionIngredient(item='minecraft:dragon_breath'),
    output=ItemStackOfComponent(
        id='minecraft:lingering_potion',
        components=DataComponentPatch(potion_contents=PotionContents(potion='minecraft:wind_charged')),
    ),
    type='minecraft:brewing',
)
