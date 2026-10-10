"""
Generated from symbols.json for ::java::data::recipe::CraftingBookInfo
Local link to file: generated_symbols/data/recipe/CraftingBookInfo.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.recipe.CraftingBookCategory import CraftingBookCategory


class CraftingBookInfo(GeneratedModel):
    group: str | None = None  # Identifier to group multiple recipes in the recipe book.
    category: CraftingBookCategory | None = None  # Identifier for the category this goes in the recipe book.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::recipe::CraftingBookInfo": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Identifier to group multiple recipes in the recipe book.",
                "key": "group",
                "type": {
                    "kind": "string"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Identifier for the category this goes in the recipe book.",
                "key": "category",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::recipe::CraftingBookCategory"
                },
                "optional": True
            }
        ]
    }
}
