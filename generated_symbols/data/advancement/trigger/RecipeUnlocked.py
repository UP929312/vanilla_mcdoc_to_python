# Generated from symbols.json for ::java::data::advancement::trigger::RecipeUnlocked
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.advancement.trigger.TriggerBase import TriggerBase

if TYPE_CHECKING:
    from generated_symbols.data.recipe.RecipeListRef import RecipeListRef


@dataclass(kw_only=True)
class RecipeUnlocked(TriggerBase):
    recipes: RecipeListRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::RecipeUnlocked": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::trigger::TriggerBase"
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
}

