"""
Generated from symbols.json for ::java::data::recipe::CraftingSpecialFireworkStarFade
Local link to file: vanilla_mcdoc/data/recipe/CraftingSpecialFireworkStarFade.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.recipe.Ingredient import Ingredient
    from vanilla_mcdoc.world.item.ItemStackTemplate import ItemStackTemplate


class CraftingSpecialFireworkStarFade(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'recipe'

    target: Ingredient  # The firework star item.  The fade effect of its `firework_explosion` will be changed.  The other components are copied.
    dye: Ingredient  # The items to provide fade color.  Colors are provided by the `dye` component.  Multiple dyes can be used at the same time.
    result: ItemStackTemplate
