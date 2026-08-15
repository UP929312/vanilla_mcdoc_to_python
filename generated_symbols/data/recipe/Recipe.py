"""
Generated from symbols.json for ::java::data::recipe::Recipe
Local link to file: generated_symbols/data/recipe/Recipe.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from generated_symbols.data.recipe.CookingBookInfo import CookingBookInfo
from generated_symbols.data.recipe.CraftingBookInfo import CraftingBookInfo
from generated_symbols.data.recipe.NotificationInfo import NotificationInfo
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.recipe.Ingredient import Ingredient
    from generated_symbols.data.recipe.IngredientValue import IngredientValue
    from generated_symbols.data.recipe.ItemResult import ItemResult
    from generated_symbols.data.recipe.PotionIngredient import PotionIngredient
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds
    from generated_symbols.registry.KnownRecipeSerializerId import KnownRecipeSerializerId
    from generated_symbols.world.item.ItemStack import ItemStack
    from generated_symbols.world.item.ItemStackTemplate import ItemStackTemplate


@dataclass(kw_only=True)
class RecipeUnknown:
    type: Annotated[str, IdSpec(registry='recipe_serializer')] | KnownRecipeSerializerId


@dataclass(kw_only=True)
class RecipeBlasting(CookingBookInfo, NotificationInfo):
    type: Literal['minecraft:blasting']
    ingredient: Ingredient
    result: ItemStackTemplate
    experience: float | None = None
    cookingtime: int | None = None


@dataclass(kw_only=True)
class RecipeBrewing:
    type: Literal['minecraft:brewing']
    input: PotionIngredient  # The original potion.
    reagent: PotionIngredient  # The ingredient.
    output: ItemStackTemplate


@dataclass(kw_only=True)
class RecipeCampfireCooking(CookingBookInfo, NotificationInfo):
    type: Literal['minecraft:campfire_cooking']
    ingredient: Ingredient
    result: ItemStackTemplate
    experience: float | None = None
    cookingtime: int | None = None


@dataclass(kw_only=True)
class RecipeCraftingDecoratedPot:
    type: Literal['minecraft:crafting_decorated_pot']


@dataclass(kw_only=True)
class RecipeCraftingDye(CraftingBookInfo, NotificationInfo):
    type: Literal['minecraft:crafting_dye']
    target: Ingredient  # The item to be dyed.  Its `dyed_color` component will be dyed. The other components are copied.
    dye: Ingredient  # The items to provide dye color.  Colors are provided by the `dye` component.  Multiple dyes can be used at the same time.
    result: ItemStackTemplate


@dataclass(kw_only=True)
class RecipeCraftingImbue(CraftingBookInfo, NotificationInfo):
    type: Literal['minecraft:crafting_imbue']
    source: Ingredient  # The item to provide potion effect.  Its `potion_contents` component will be copied.  This item is placed at the center grid.
    material: Ingredient  # Additional ingredients.  8 `material` items are required to surroud the `source` item.
    result: ItemStackTemplate


@dataclass(kw_only=True)
class RecipeCraftingShaped(CraftingBookInfo, NotificationInfo):
    type: Literal['minecraft:crafting_shaped']
    pattern: Annotated[list[Annotated[str, 'Length = 1-3 (both inclusive)']], 'Length = 1-3 (both inclusive)']
    key: dict[str, Ingredient]
    result: ItemStackTemplate


@dataclass(kw_only=True)
class RecipeCraftingShapeless(CraftingBookInfo, NotificationInfo):
    type: Literal['minecraft:crafting_shapeless']
    ingredients: Annotated[list[Ingredient], 'Length = 1-9 (both inclusive)']
    result: ItemStackTemplate


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
class RecipeCraftingTransmute(CraftingBookInfo, NotificationInfo):
    type: Literal['minecraft:crafting_transmute']
    input: Ingredient  # The ingredient that will transfer its data components to the result item.
    material: Ingredient  # An additional ingredient.
    result: ItemStack | Annotated[str, IdSpec(registry='item', exclude=('air',))]  # The result item that will be merged with the input ingredient.
    material_count: MinMaxBounds[Annotated[int, 'Range | `1`-`8` | both inclusive']] | Annotated[int, 'Range | `1`-`8` | both inclusive'] | None = None  # The allowed count of material. Defaults to `1`.
    add_material_count_to_result: bool | None = None  # When true, the number of materials will be added to the result count.  Defaults to `false`.


@dataclass(kw_only=True)
class RecipeSmelting(CookingBookInfo, NotificationInfo):
    type: Literal['minecraft:smelting']
    ingredient: Ingredient
    result: ItemStackTemplate
    experience: float | None = None
    cookingtime: int | None = None


@dataclass(kw_only=True)
class RecipeSmithing:
    type: Literal['minecraft:smithing']
    base: IngredientValue
    addition: IngredientValue
    result: ItemResult


@dataclass(kw_only=True)
class RecipeSmithingTransform(NotificationInfo):
    type: Literal['minecraft:smithing_transform']
    base: Ingredient  # Ingredient specifying an item to be transformed.
    result: ItemStackTemplate  # Resulting transformed item.
    addition: Ingredient | None = None  # Material that will be used.
    template: Ingredient | None = None  # Template item that will be used for the pattern.


@dataclass(kw_only=True)
class RecipeSmithingTrim(NotificationInfo):
    type: Literal['minecraft:smithing_trim']
    base: Ingredient  # Ingredient specifying an item to be trimmed.
    addition: Ingredient  # Material that will be used.
    template: Ingredient  # Template item that will be used for the pattern.
    pattern: Annotated[str, IdSpec(registry='trim_pattern')]  # The trim pattern to apply to the result item.


@dataclass(kw_only=True)
class RecipeSmoking(CookingBookInfo, NotificationInfo):
    type: Literal['minecraft:smoking']
    ingredient: Ingredient
    result: ItemStackTemplate
    experience: float | None = None
    cookingtime: int | None = None


@dataclass(kw_only=True)
class RecipeStonecutting(NotificationInfo):
    type: Literal['minecraft:stonecutting']
    ingredient: Ingredient
    result: ItemStackTemplate


type Recipe = RecipeUnknown | RecipeBlasting | RecipeBrewing | RecipeCampfireCooking | RecipeCraftingDecoratedPot | RecipeCraftingDye | RecipeCraftingImbue | RecipeCraftingShaped | RecipeCraftingShapeless | RecipeCraftingSpecialBannerduplicate | RecipeCraftingSpecialBookcloning | RecipeCraftingSpecialFireworkRocket | RecipeCraftingSpecialFireworkStar | RecipeCraftingSpecialFireworkStarFade | RecipeCraftingSpecialMapextending | RecipeCraftingSpecialShielddecoration | RecipeCraftingTransmute | RecipeSmelting | RecipeSmithing | RecipeSmithingTransform | RecipeSmithingTrim | RecipeSmoking | RecipeStonecutting


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

