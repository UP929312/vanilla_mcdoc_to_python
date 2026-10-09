"""
Generated from symbols.json for ::java::data::recipe::Recipe
Local link to file: generated_symbols/data/recipe/Recipe.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar, Literal

from generated_symbols.base import GeneratedModel
from generated_symbols.data.recipe.Brewing import Brewing
from generated_symbols.data.recipe.CraftingDye import CraftingDye
from generated_symbols.data.recipe.CraftingImbue import CraftingImbue
from generated_symbols.data.recipe.CraftingShaped import CraftingShaped
from generated_symbols.data.recipe.CraftingShapeless import CraftingShapeless
from generated_symbols.data.recipe.CraftingTransmute import CraftingTransmute
from generated_symbols.data.recipe.Smelting import Smelting
from generated_symbols.data.recipe.SmithingTransform import SmithingTransform
from generated_symbols.data.recipe.SmithingTrim import SmithingTrim
from generated_symbols.data.recipe.Stonecutting import Stonecutting
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.registry.KnownRecipeSerializerId import KnownRecipeSerializerId


class RecipeUnknown(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'recipe'

    type: Annotated[str, IdSpec(registry='recipe_serializer')] | KnownRecipeSerializerId


class RecipeBlasting(Smelting):
    type: Literal['minecraft:blasting', 'blasting'] = 'minecraft:blasting'


class RecipeBrewing(Brewing):
    type: Literal['minecraft:brewing', 'brewing'] = 'minecraft:brewing'


class RecipeCampfireCooking(Smelting):
    type: Literal['minecraft:campfire_cooking', 'campfire_cooking'] = 'minecraft:campfire_cooking'


class RecipeCraftingDecoratedPot(GeneratedModel):
    type: Literal['minecraft:crafting_decorated_pot', 'crafting_decorated_pot'] = 'minecraft:crafting_decorated_pot'


class RecipeCraftingDye(CraftingDye):
    type: Literal['minecraft:crafting_dye', 'crafting_dye'] = 'minecraft:crafting_dye'


class RecipeCraftingImbue(CraftingImbue):
    type: Literal['minecraft:crafting_imbue', 'crafting_imbue'] = 'minecraft:crafting_imbue'


class RecipeCraftingShaped(CraftingShaped):
    type: Literal['minecraft:crafting_shaped', 'crafting_shaped'] = 'minecraft:crafting_shaped'


class RecipeCraftingShapeless(CraftingShapeless):
    type: Literal['minecraft:crafting_shapeless', 'crafting_shapeless'] = 'minecraft:crafting_shapeless'


class RecipeCraftingSpecialBannerduplicate(GeneratedModel):
    type: Literal['minecraft:crafting_special_bannerduplicate', 'crafting_special_bannerduplicate'] = 'minecraft:crafting_special_bannerduplicate'


class RecipeCraftingSpecialBookcloning(GeneratedModel):
    type: Literal['minecraft:crafting_special_bookcloning', 'crafting_special_bookcloning'] = 'minecraft:crafting_special_bookcloning'


class RecipeCraftingSpecialFireworkRocket(GeneratedModel):
    type: Literal['minecraft:crafting_special_firework_rocket', 'crafting_special_firework_rocket'] = 'minecraft:crafting_special_firework_rocket'


class RecipeCraftingSpecialFireworkStar(GeneratedModel):
    type: Literal['minecraft:crafting_special_firework_star', 'crafting_special_firework_star'] = 'minecraft:crafting_special_firework_star'


class RecipeCraftingSpecialFireworkStarFade(GeneratedModel):
    type: Literal['minecraft:crafting_special_firework_star_fade', 'crafting_special_firework_star_fade'] = 'minecraft:crafting_special_firework_star_fade'


class RecipeCraftingSpecialMapextending(GeneratedModel):
    type: Literal['minecraft:crafting_special_mapextending', 'crafting_special_mapextending'] = 'minecraft:crafting_special_mapextending'


class RecipeCraftingSpecialShielddecoration(GeneratedModel):
    type: Literal['minecraft:crafting_special_shielddecoration', 'crafting_special_shielddecoration'] = 'minecraft:crafting_special_shielddecoration'


class RecipeCraftingTransmute(CraftingTransmute):
    type: Literal['minecraft:crafting_transmute', 'crafting_transmute'] = 'minecraft:crafting_transmute'


class RecipeSmelting(Smelting):
    type: Literal['minecraft:smelting', 'smelting'] = 'minecraft:smelting'


class RecipeSmithingTransform(SmithingTransform):
    type: Literal['minecraft:smithing_transform', 'smithing_transform'] = 'minecraft:smithing_transform'


class RecipeSmithingTrim(SmithingTrim):
    type: Literal['minecraft:smithing_trim', 'smithing_trim'] = 'minecraft:smithing_trim'


class RecipeSmoking(Smelting):
    type: Literal['minecraft:smoking', 'smoking'] = 'minecraft:smoking'


class RecipeStonecutting(Stonecutting):
    type: Literal['minecraft:stonecutting', 'stonecutting'] = 'minecraft:stonecutting'


type Recipe = RecipeUnknown | RecipeBlasting | RecipeBrewing | RecipeCampfireCooking | RecipeCraftingDecoratedPot | RecipeCraftingDye | RecipeCraftingImbue | RecipeCraftingShaped | RecipeCraftingShapeless | RecipeCraftingSpecialBannerduplicate | RecipeCraftingSpecialBookcloning | RecipeCraftingSpecialFireworkRocket | RecipeCraftingSpecialFireworkStar | RecipeCraftingSpecialFireworkStarFade | RecipeCraftingSpecialMapextending | RecipeCraftingSpecialShielddecoration | RecipeCraftingTransmute | RecipeSmelting | RecipeSmithingTransform | RecipeSmithingTrim | RecipeSmoking | RecipeStonecutting


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::recipe::Recipe": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "recipe_serializer"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:recipe_serializer"
                }
            }
        ]
    }
}

