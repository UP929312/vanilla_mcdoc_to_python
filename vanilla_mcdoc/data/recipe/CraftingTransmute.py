"""
Generated from symbols.json for ::java::data::recipe::CraftingTransmute
Local link to file: vanilla_mcdoc/data/recipe/CraftingTransmute.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.data.recipe.CraftingBookInfo import CraftingBookInfo
from vanilla_mcdoc.data.recipe.NotificationInfo import NotificationInfo
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.recipe.Ingredient import Ingredient
    from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds
    from vanilla_mcdoc.world.item.ItemStack import ItemStack


class CraftingTransmute(CraftingBookInfo, NotificationInfo):
    __resource_dir__: ClassVar[str] = 'recipe'

    input: Ingredient  # The ingredient that will transfer its data components to the result item.
    material: Ingredient  # An additional ingredient.
    material_count: MinMaxBounds[Annotated[int, Field(ge=1, le=8)]] | Annotated[int, Field(ge=1, le=8)] | None = None  # The allowed count of material. Defaults to `1`.
    add_material_count_to_result: bool | None = None  # When true, the number of materials will be added to the result count.  Defaults to `false`.
    result: ItemStack | Annotated[str, IdSpec(registry='item', exclude=('air',))]  # The result item that will be merged with the input ingredient.
