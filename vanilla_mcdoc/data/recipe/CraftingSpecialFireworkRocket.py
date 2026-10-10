"""
Generated from symbols.json for ::java::data::recipe::CraftingSpecialFireworkRocket
Local link to file: vanilla_mcdoc/data/recipe/CraftingSpecialFireworkRocket.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.recipe.Ingredient import Ingredient
    from vanilla_mcdoc.world.item.ItemStackTemplate import ItemStackTemplate


class CraftingSpecialFireworkRocket(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'recipe'

    shell: Ingredient  # Additional ingredient.  Exactly 1 additional ingredient is required.
    fuel: Ingredient  # The fuel ingredient.  The count of fuel ingredients controls the `flight_duration` field.  Only 1 ~ 3 fuels are allowed.
    star: Ingredient  # The firework star ingredient.  Provides explosion data by the `firework_explosion` component.  Any count of stars (including 0) are allowed.
    result: ItemStackTemplate  # The `fireworks` component is controlled by `fuel` and `star`.
