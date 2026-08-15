"""
Generated from symbols.json for ::java::data::advancement::trigger::RecipeUnlockedTrigger
Local link to file: generated_symbols/data/advancement/trigger/RecipeUnlockedTrigger.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass

from generated_symbols.data.advancement.trigger.ParitalRequired import ParitalRequired
from generated_symbols.data.advancement.trigger.PlayerConditions import PlayerConditions
from generated_symbols.data.recipe.RecipeListRef import RecipeListRef


@dataclass(kw_only=True)
class RecipeUnlockedTriggerTypeArg(PlayerConditions):
    recipes: RecipeListRef


RecipeUnlockedTrigger = ParitalRequired[RecipeUnlockedTriggerTypeArg]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::RecipeUnlockedTrigger": {
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
                        "key": "recipe",
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
                    }
                ]
            }
        ]
    }
}

