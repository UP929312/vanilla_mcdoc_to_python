# Generated from symbols.json for ::java::data::recipe::CraftingIngredients
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.recipe.Ingredient import Ingredient


type CraftingIngredients = dict[str, Ingredient]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::recipe::CraftingIngredients": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "crafting_ingredient"
                        }
                    ]
                },
                "type": {
                    "kind": "reference",
                    "path": "::java::data::recipe::Ingredient"
                }
            }
        ]
    }
}

