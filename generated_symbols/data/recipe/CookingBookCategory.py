"""
Generated from symbols.json for ::java::data::recipe::CookingBookCategory
Local link to file: generated_symbols/data/recipe/CookingBookCategory.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class CookingBookCategory(StrEnum):
    FOOD = "food"
    BLOCKS = "blocks"
    MISC = "misc"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::recipe::CookingBookCategory": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "identifier": "Food",
                "value": "food"
            },
            {
                "identifier": "Blocks",
                "value": "blocks"
            },
            {
                "identifier": "Misc",
                "value": "misc"
            }
        ]
    }
}

