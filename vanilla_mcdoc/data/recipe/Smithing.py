"""
Generated from symbols.json for ::java::data::recipe::Smithing
Local link to file: vanilla_mcdoc/data/recipe/Smithing.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.recipe.IngredientValue import IngredientValue
    from vanilla_mcdoc.data.recipe.ItemResult import ItemResult


class Smithing(GeneratedModel):
    base: IngredientValue
    addition: IngredientValue
    result: ItemResult


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::recipe::Smithing": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "base",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::recipe::IngredientValue"
                }
            },
            {
                "kind": "pair",
                "key": "addition",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::recipe::IngredientValue"
                }
            },
            {
                "kind": "pair",
                "key": "result",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::recipe::ItemResult"
                }
            }
        ]
    }
}
