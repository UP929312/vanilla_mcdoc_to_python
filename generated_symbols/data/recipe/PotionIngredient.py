# Generated from symbols.json for ::java::data::recipe::PotionIngredient
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.recipe.Ingredient import Ingredient
    from generated_symbols.world.component.predicate.PotionsPredicate import PotionsPredicate


@dataclass(kw_only=True)
class PotionIngredient:
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

