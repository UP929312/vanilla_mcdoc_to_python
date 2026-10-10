"""
Generated from symbols.json for ::java::data::recipe::Smithing
Local link to file: generated_symbols/data/recipe/Smithing.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.recipe.IngredientValue import IngredientValue
    from generated_symbols.data.recipe.ItemResult import ItemResult


class Smithing(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'recipe'

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
