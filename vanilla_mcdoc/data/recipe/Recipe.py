"""
Generated from symbols.json for ::java::data::recipe::Recipe
Local link to file: vanilla_mcdoc/data/recipe/Recipe.py
"""
# ~~~ CODE ~~~
from typing import Annotated, ClassVar, Literal

from pydantic import Discriminator, Tag

from vanilla_mcdoc.base import GeneratedModel, tag_of
from vanilla_mcdoc.data.recipe.Brewing import Brewing
from vanilla_mcdoc.data.recipe.CraftingDye import CraftingDye
from vanilla_mcdoc.data.recipe.CraftingImbue import CraftingImbue
from vanilla_mcdoc.data.recipe.CraftingShaped import CraftingShaped
from vanilla_mcdoc.data.recipe.CraftingShapeless import CraftingShapeless
from vanilla_mcdoc.data.recipe.CraftingTransmute import CraftingTransmute
from vanilla_mcdoc.data.recipe.Smelting import Smelting
from vanilla_mcdoc.data.recipe.SmithingTransform import SmithingTransform
from vanilla_mcdoc.data.recipe.SmithingTrim import SmithingTrim
from vanilla_mcdoc.data.recipe.Stonecutting import Stonecutting


class RecipeBlasting(Smelting):
    __resource_dir__: ClassVar[str] = 'recipe'

    type: Literal['minecraft:blasting', 'blasting'] = 'minecraft:blasting'


class RecipeBrewing(Brewing):
    __resource_dir__: ClassVar[str] = 'recipe'

    type: Literal['minecraft:brewing', 'brewing'] = 'minecraft:brewing'


class RecipeCampfireCooking(Smelting):
    __resource_dir__: ClassVar[str] = 'recipe'

    type: Literal['minecraft:campfire_cooking', 'campfire_cooking'] = 'minecraft:campfire_cooking'


class RecipeCraftingDecoratedPot(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'recipe'

    type: Literal['minecraft:crafting_decorated_pot', 'crafting_decorated_pot'] = 'minecraft:crafting_decorated_pot'


class RecipeCraftingDye(CraftingDye):
    __resource_dir__: ClassVar[str] = 'recipe'

    type: Literal['minecraft:crafting_dye', 'crafting_dye'] = 'minecraft:crafting_dye'


class RecipeCraftingImbue(CraftingImbue):
    __resource_dir__: ClassVar[str] = 'recipe'

    type: Literal['minecraft:crafting_imbue', 'crafting_imbue'] = 'minecraft:crafting_imbue'


class RecipeCraftingShaped(CraftingShaped):
    __resource_dir__: ClassVar[str] = 'recipe'

    type: Literal['minecraft:crafting_shaped', 'crafting_shaped'] = 'minecraft:crafting_shaped'


class RecipeCraftingShapeless(CraftingShapeless):
    __resource_dir__: ClassVar[str] = 'recipe'

    type: Literal['minecraft:crafting_shapeless', 'crafting_shapeless'] = 'minecraft:crafting_shapeless'


class RecipeCraftingSpecialBannerduplicate(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'recipe'

    type: Literal['minecraft:crafting_special_bannerduplicate', 'crafting_special_bannerduplicate'] = 'minecraft:crafting_special_bannerduplicate'


class RecipeCraftingSpecialBookcloning(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'recipe'

    type: Literal['minecraft:crafting_special_bookcloning', 'crafting_special_bookcloning'] = 'minecraft:crafting_special_bookcloning'


class RecipeCraftingSpecialFireworkRocket(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'recipe'

    type: Literal['minecraft:crafting_special_firework_rocket', 'crafting_special_firework_rocket'] = 'minecraft:crafting_special_firework_rocket'


class RecipeCraftingSpecialFireworkStar(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'recipe'

    type: Literal['minecraft:crafting_special_firework_star', 'crafting_special_firework_star'] = 'minecraft:crafting_special_firework_star'


class RecipeCraftingSpecialFireworkStarFade(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'recipe'

    type: Literal['minecraft:crafting_special_firework_star_fade', 'crafting_special_firework_star_fade'] = 'minecraft:crafting_special_firework_star_fade'


class RecipeCraftingSpecialMapextending(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'recipe'

    type: Literal['minecraft:crafting_special_mapextending', 'crafting_special_mapextending'] = 'minecraft:crafting_special_mapextending'


class RecipeCraftingSpecialShielddecoration(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'recipe'

    type: Literal['minecraft:crafting_special_shielddecoration', 'crafting_special_shielddecoration'] = 'minecraft:crafting_special_shielddecoration'


class RecipeCraftingTransmute(CraftingTransmute):
    __resource_dir__: ClassVar[str] = 'recipe'

    type: Literal['minecraft:crafting_transmute', 'crafting_transmute'] = 'minecraft:crafting_transmute'


class RecipeSmelting(Smelting):
    __resource_dir__: ClassVar[str] = 'recipe'

    type: Literal['minecraft:smelting', 'smelting'] = 'minecraft:smelting'


class RecipeSmithingTransform(SmithingTransform):
    __resource_dir__: ClassVar[str] = 'recipe'

    type: Literal['minecraft:smithing_transform', 'smithing_transform'] = 'minecraft:smithing_transform'


class RecipeSmithingTrim(SmithingTrim):
    __resource_dir__: ClassVar[str] = 'recipe'

    type: Literal['minecraft:smithing_trim', 'smithing_trim'] = 'minecraft:smithing_trim'


class RecipeSmoking(Smelting):
    __resource_dir__: ClassVar[str] = 'recipe'

    type: Literal['minecraft:smoking', 'smoking'] = 'minecraft:smoking'


class RecipeStonecutting(Stonecutting):
    __resource_dir__: ClassVar[str] = 'recipe'

    type: Literal['minecraft:stonecutting', 'stonecutting'] = 'minecraft:stonecutting'


class RecipeCraftingSpecialRepairitem(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'recipe'

    type: Literal['minecraft:crafting_special_repairitem', 'crafting_special_repairitem'] = 'minecraft:crafting_special_repairitem'


type Recipe = Annotated[
    Annotated[RecipeBlasting, Tag('minecraft:blasting')]
    | Annotated[RecipeBrewing, Tag('minecraft:brewing')]
    | Annotated[RecipeCampfireCooking, Tag('minecraft:campfire_cooking')]
    | Annotated[RecipeCraftingDecoratedPot, Tag('minecraft:crafting_decorated_pot')]
    | Annotated[RecipeCraftingDye, Tag('minecraft:crafting_dye')]
    | Annotated[RecipeCraftingImbue, Tag('minecraft:crafting_imbue')]
    | Annotated[RecipeCraftingShaped, Tag('minecraft:crafting_shaped')]
    | Annotated[RecipeCraftingShapeless, Tag('minecraft:crafting_shapeless')]
    | Annotated[RecipeCraftingSpecialBannerduplicate, Tag('minecraft:crafting_special_bannerduplicate')]
    | Annotated[RecipeCraftingSpecialBookcloning, Tag('minecraft:crafting_special_bookcloning')]
    | Annotated[RecipeCraftingSpecialFireworkRocket, Tag('minecraft:crafting_special_firework_rocket')]
    | Annotated[RecipeCraftingSpecialFireworkStar, Tag('minecraft:crafting_special_firework_star')]
    | Annotated[RecipeCraftingSpecialFireworkStarFade, Tag('minecraft:crafting_special_firework_star_fade')]
    | Annotated[RecipeCraftingSpecialMapextending, Tag('minecraft:crafting_special_mapextending')]
    | Annotated[RecipeCraftingSpecialShielddecoration, Tag('minecraft:crafting_special_shielddecoration')]
    | Annotated[RecipeCraftingTransmute, Tag('minecraft:crafting_transmute')]
    | Annotated[RecipeSmelting, Tag('minecraft:smelting')]
    | Annotated[RecipeSmithingTransform, Tag('minecraft:smithing_transform')]
    | Annotated[RecipeSmithingTrim, Tag('minecraft:smithing_trim')]
    | Annotated[RecipeSmoking, Tag('minecraft:smoking')]
    | Annotated[RecipeStonecutting, Tag('minecraft:stonecutting')]
    | Annotated[RecipeCraftingSpecialRepairitem, Tag('minecraft:crafting_special_repairitem')],
    Discriminator(tag_of('type')),
]
