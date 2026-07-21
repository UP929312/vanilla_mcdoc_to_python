# Generated from symbols.json for ::java::data::recipe::FireworkShapeIngredients
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.recipe.Ingredient import Ingredient
    from generated_symbols.world.component.item.FireworkShape import FireworkShape


type FireworkShapeIngredients = dict[FireworkShape, Ingredient]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::recipe::FireworkShapeIngredients": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
                    "kind": "reference",
                    "path": "::java::world::component::item::FireworkShape"
                },
                "type": {
                    "kind": "reference",
                    "path": "::java::data::recipe::Ingredient"
                }
            }
        ]
    }
}

