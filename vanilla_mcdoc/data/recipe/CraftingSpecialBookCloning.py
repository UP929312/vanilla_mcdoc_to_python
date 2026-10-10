"""
Generated from symbols.json for ::java::data::recipe::CraftingSpecialBookCloning
Local link to file: vanilla_mcdoc/data/recipe/CraftingSpecialBookCloning.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.recipe.Ingredient import Ingredient
    from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds
    from vanilla_mcdoc.world.item.ItemStackTemplate import ItemStackTemplate


class CraftingSpecialBookCloning(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'recipe'

    source: Ingredient  # The book item.  Its `written_book_contents` component will be copied, with `generation` value increased by 1.  The other components are copied as-is.   The book will be kept in the crafting grid.
    material: Ingredient  # Additional ingredients.  Multiple materials can be used at the same time.  The number of materials beyond the first one will be added to the result count.
    allowed_generations: MinMaxBounds[Annotated[int, Field(ge=0, le=2)]] | Annotated[int, Field(ge=0, le=2)] | None = None  # Limits the generation of the `source` item that can be copied. Defaults to allow generation 0 and 1 (original and first copy).
    result: ItemStackTemplate
