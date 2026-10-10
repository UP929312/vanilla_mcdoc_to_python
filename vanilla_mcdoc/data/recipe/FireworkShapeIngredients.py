"""
Generated from symbols.json for ::java::data::recipe::FireworkShapeIngredients
Local link to file: vanilla_mcdoc/data/recipe/FireworkShapeIngredients.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vanilla_mcdoc.data.recipe.Ingredient import Ingredient
    from vanilla_mcdoc.world.component.item.FireworkShape import FireworkShape


type FireworkShapeIngredients = dict[FireworkShape, Ingredient]
