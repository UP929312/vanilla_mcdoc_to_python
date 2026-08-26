"""
Generated from symbols.json for ::java::data::recipe::Recipe
Local link to file: generated_symbols/data/recipe/Recipe.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, ClassVar, Literal

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


@dataclass(kw_only=True)
class RecipeUnknown:
    __resource_dir__: ClassVar[str] = 'recipe'

    type: Annotated[str, IdSpec(registry='recipe_serializer')] | KnownRecipeSerializerId


@dataclass(kw_only=True)
class RecipeBlasting(Smelting):
    type: Literal['minecraft:blasting']


@dataclass(kw_only=True)
class RecipeBrewing(Brewing):
    type: Literal['minecraft:brewing']


@dataclass(kw_only=True)
class RecipeCampfireCooking(Smelting):
    type: Literal['minecraft:campfire_cooking']


@dataclass(kw_only=True)
class RecipeCraftingDecoratedPot:
    type: Literal['minecraft:crafting_decorated_pot']


@dataclass(kw_only=True)
class RecipeCraftingDye(CraftingDye):
    type: Literal['minecraft:crafting_dye']


@dataclass(kw_only=True)
class RecipeCraftingImbue(CraftingImbue):
    type: Literal['minecraft:crafting_imbue']


@dataclass(kw_only=True)
class RecipeCraftingShaped(CraftingShaped):
    type: Literal['minecraft:crafting_shaped']


@dataclass(kw_only=True)
class RecipeCraftingShapeless(CraftingShapeless):
    type: Literal['minecraft:crafting_shapeless']


@dataclass(kw_only=True)
class RecipeCraftingSpecialBannerduplicate:
    type: Literal['minecraft:crafting_special_bannerduplicate']


@dataclass(kw_only=True)
class RecipeCraftingSpecialBookcloning:
    type: Literal['minecraft:crafting_special_bookcloning']


@dataclass(kw_only=True)
class RecipeCraftingSpecialFireworkRocket:
    type: Literal['minecraft:crafting_special_firework_rocket']


@dataclass(kw_only=True)
class RecipeCraftingSpecialFireworkStar:
    type: Literal['minecraft:crafting_special_firework_star']


@dataclass(kw_only=True)
class RecipeCraftingSpecialFireworkStarFade:
    type: Literal['minecraft:crafting_special_firework_star_fade']


@dataclass(kw_only=True)
class RecipeCraftingSpecialMapextending:
    type: Literal['minecraft:crafting_special_mapextending']


@dataclass(kw_only=True)
class RecipeCraftingSpecialShielddecoration:
    type: Literal['minecraft:crafting_special_shielddecoration']


@dataclass(kw_only=True)
class RecipeCraftingTransmute(CraftingTransmute):
    type: Literal['minecraft:crafting_transmute']


@dataclass(kw_only=True)
class RecipeSmelting(Smelting):
    type: Literal['minecraft:smelting']


@dataclass(kw_only=True)
class RecipeSmithingTransform(SmithingTransform):
    type: Literal['minecraft:smithing_transform']


@dataclass(kw_only=True)
class RecipeSmithingTrim(SmithingTrim):
    type: Literal['minecraft:smithing_trim']


@dataclass(kw_only=True)
class RecipeSmoking(Smelting):
    type: Literal['minecraft:smoking']


@dataclass(kw_only=True)
class RecipeStonecutting(Stonecutting):
    type: Literal['minecraft:stonecutting']


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

