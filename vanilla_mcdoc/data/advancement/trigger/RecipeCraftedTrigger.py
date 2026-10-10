"""
Generated from symbols.json for ::java::data::advancement::trigger::RecipeCraftedTrigger
Local link to file: generated_symbols/data/advancement/trigger/RecipeCraftedTrigger.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from generated_symbols.data.advancement.predicate.ItemPredicate import ItemPredicate
from generated_symbols.data.advancement.trigger.ParitalRequired import ParitalRequired
from generated_symbols.data.advancement.trigger.PlayerConditions import PlayerConditions
from generated_symbols.data.recipe.RecipeListRef import RecipeListRef


class RecipeCraftedTriggerTypeArg(PlayerConditions):
    recipes: RecipeListRef
    ingredients: Annotated[list[ItemPredicate], Field(min_length=1, max_length=9)] | None = None


RecipeCraftedTrigger = ParitalRequired[RecipeCraftedTriggerTypeArg]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::RecipeCraftedTrigger": {
        "kind": "concrete",
        "child": {
            "kind": "reference",
            "path": "::java::data::advancement::trigger::ParitalRequired"
        },
        "typeArgs": [
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "spread",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::advancement::trigger::PlayerConditions"
                        }
                    },
                    {
                        "kind": "pair",
                        "attributes": [
                            {
                                "name": "until",
                                "value": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "26.3"
                                    }
                                }
                            }
                        ],
                        "key": "recipe_id",
                        "type": {
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
                    {
                        "kind": "pair",
                        "attributes": [
                            {
                                "name": "since",
                                "value": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "26.3"
                                    }
                                }
                            }
                        ],
                        "key": "recipes",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::recipe::RecipeListRef"
                        }
                    },
                    {
                        "kind": "pair",
                        "key": "ingredients",
                        "type": {
                            "kind": "list",
                            "item": {
                                "kind": "reference",
                                "path": "::java::data::advancement::predicate::ItemPredicate"
                            },
                            "lengthRange": {
                                "kind": 0,
                                "min": 1,
                                "max": 9
                            }
                        },
                        "optional": True
                    }
                ]
            }
        ]
    }
}
