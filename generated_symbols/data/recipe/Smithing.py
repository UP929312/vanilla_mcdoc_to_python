# Generated from symbols.json for ::java::data::recipe::Smithing
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.recipe.IngredientValue import IngredientValue
    from generated_symbols.data.recipe.ItemResult import ItemResult


@dataclass(kw_only=True)
class Smithing:
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

