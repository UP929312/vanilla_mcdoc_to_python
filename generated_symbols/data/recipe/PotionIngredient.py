"""
Generated from symbols.json for ::java::data::recipe::PotionIngredient
Local link to file: generated_symbols/data/recipe/PotionIngredient.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.recipe.Ingredient import Ingredient
    from generated_symbols.world.component.predicate.PotionsPredicate import PotionsPredicate


class PotionIngredient(GeneratedModel):
    item: Ingredient
    potion_contents: PotionsPredicate | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::recipe::PotionIngredient": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "item",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::recipe::Ingredient"
                }
            },
            {
                "kind": "pair",
                "key": "potion_contents",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::predicate::PotionsPredicate"
                },
                "optional": True
            }
        ]
    }
}

