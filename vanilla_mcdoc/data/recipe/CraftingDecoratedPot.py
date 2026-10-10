"""
Generated from symbols.json for ::java::data::recipe::CraftingDecoratedPot
Local link to file: vanilla_mcdoc/data/recipe/CraftingDecoratedPot.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.recipe.Ingredient import Ingredient
    from vanilla_mcdoc.world.item.ItemStackTemplate import ItemStackTemplate


class CraftingDecoratedPot(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'recipe'

    back: Ingredient
    left: Ingredient
    right: Ingredient
    front: Ingredient
    result: ItemStackTemplate  # The `pot_decorations` component will store the 4 ingredients.
