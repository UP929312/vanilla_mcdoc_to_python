"""
Generated from symbols.json for ::java::data::recipe::CraftingBookCategory
Local link to file: generated_symbols/data/recipe/CraftingBookCategory.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class CraftingBookCategory(StrEnum):
    BUILDING = "building"
    REDSTONE = "redstone"
    EQUIPMENT = "equipment"
    MISC = "misc"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::recipe::CraftingBookCategory": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "identifier": "Building",
                "value": "building"
            },
            {
                "identifier": "Redstone",
                "value": "redstone"
            },
            {
                "identifier": "Equipment",
                "value": "equipment"
            },
            {
                "identifier": "Misc",
                "value": "misc"
            }
        ]
    }
}

