"""
Generated from symbols.json for ::java::data::advancement::trigger::RecipeUnlockedTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/RecipeUnlockedTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.trigger.ParitalRequired import ParitalRequired
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions
from vanilla_mcdoc.data.recipe.RecipeListRef import RecipeListRef


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
