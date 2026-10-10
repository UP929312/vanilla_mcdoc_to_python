"""
Generated from symbols.json for ::java::data::recipe::PotionIngredient
Local link to file: vanilla_mcdoc/data/recipe/PotionIngredient.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.recipe.Ingredient import Ingredient
    from vanilla_mcdoc.world.component.predicate.PotionsPredicate import PotionsPredicate


class PotionIngredient(GeneratedModel):
    item: Ingredient
    potion_contents: PotionsPredicate | None = None
