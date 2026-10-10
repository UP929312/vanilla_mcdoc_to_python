"""
Generated from symbols.json for ::java::data::recipe::CraftingSpecialMapExtending
Local link to file: vanilla_mcdoc/data/recipe/CraftingSpecialMapExtending.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.recipe.Ingredient import Ingredient
    from vanilla_mcdoc.world.item.ItemStackTemplate import ItemStackTemplate


class CraftingSpecialMapExtending(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'recipe'

    map: Ingredient  # The map item.  The `map_id` component is used to determine the resulting item.  The other components are copied.  This item is placed at the center grid.   The source map will be kept in the crafting grid.
    material: Ingredient  # Additional ingredients.  8 `material` items are required to surroud the `map` item.
    result: ItemStackTemplate  # The previewing result will have `map_post_processing` transient component.  The crafted result will have a new `map_id` component, which shows the extended version of the original map.
