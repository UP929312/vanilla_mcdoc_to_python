"""
Generated from symbols.json for ::java::data::recipe::CookingBookInfo
Local link to file: vanilla_mcdoc/data/recipe/CookingBookInfo.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.recipe.CookingBookCategory import CookingBookCategory


class CookingBookInfo(GeneratedModel):
    group: str | None = None  # Identifier to group multiple recipes in the recipe book.
    category: CookingBookCategory | None = None  # Identifier for the category this goes in the recipe book.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::recipe::CookingBookInfo": {
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
                    "path": "::java::data::recipe::CookingBookCategory"
                },
                "optional": True
            }
        ]
    }
}
