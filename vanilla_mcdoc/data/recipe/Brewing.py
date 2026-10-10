"""
Generated from symbols.json for ::java::data::recipe::Brewing
Local link to file: vanilla_mcdoc/data/recipe/Brewing.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.recipe.PotionIngredient import PotionIngredient
    from vanilla_mcdoc.world.item.ItemStackTemplate import ItemStackTemplate


class Brewing(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'recipe'

    input: PotionIngredient  # The original potion.
    reagent: PotionIngredient  # The ingredient.
    output: ItemStackTemplate
