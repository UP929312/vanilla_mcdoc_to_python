# Generated from symbols.json for ::java::world::entity::mob::player::RecipeBook
from dataclasses import dataclass


@dataclass(kw_only=True)
class RecipeBook:
    recipes: list[str] | None = None  # Recipes the player has acquired.
    toBeDisplayed: list[str] | None = None  # Recipes that should pulse in the crafting book.
    isFilteringCraftable: bool | None = None  # Whether the player has filtered crafting on in the crafting table.
    isGuiOpen: bool | None = None  # Whether the player has the crafting book open in the crafting table.
    isFurnaceFilteringCraftable: bool | None = None  # Whether the player has filtered crafting on in the furnace.
    isFurnaceGuiOpen: bool | None = None  # Whether the player has the crafting book open in the furnace.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::player::RecipeBook": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Recipes the player has acquired.",
                "key": "recipes",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "string",
                        "attributes": [
                            {
                                "name": "id",
                                "value": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "recipe"
                                    }
                                }
                            }
                        ]
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Recipes that should pulse in the crafting book.",
                "key": "toBeDisplayed",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "string",
                        "attributes": [
                            {
                                "name": "id",
                                "value": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "recipe"
                                    }
                                }
                            }
                        ]
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the player has filtered crafting on in the crafting table.",
                "key": "isFilteringCraftable",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the player has the crafting book open in the crafting table.",
                "key": "isGuiOpen",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the player has filtered crafting on in the furnace.",
                "key": "isFurnaceFilteringCraftable",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the player has the crafting book open in the furnace.",
                "key": "isFurnaceGuiOpen",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

