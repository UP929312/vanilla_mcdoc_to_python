# Generated from symbols.json for ::java::data::advancement::trigger::RecipeCrafted
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated
from generated_symbols.data.advancement.trigger.TriggerBase import TriggerBase

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.ItemPredicate import ItemPredicate
    from generated_symbols.data.recipe.RecipeListRef import RecipeListRef


@dataclass(kw_only=True)
class RecipeCrafted(TriggerBase):
    recipes: RecipeListRef
    ingredients: Annotated[list[ItemPredicate], 'Length = 1-9 (both inclusive)'] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::RecipeCrafted": {
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
}

