"""
Generated from symbols.json for ::java::data::recipe::RecipeListRef
Local link to file: generated_symbols/data/recipe/RecipeListRef.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from runtime_metadata import IdSpec


type RecipeListRef = Annotated[str, IdSpec(registry='recipe', tags='allowed')] | list[Annotated[str, IdSpec(registry='recipe')]]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::recipe::RecipeListRef": {
        "kind": "union",
        "members": [
            {
                "kind": "string",
                "attributes": [
                    {
                        "name": "id",
                        "value": {
                            "kind": "tree",
                            "values": {
                                "registry": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "recipe"
                                    }
                                },
                                "tags": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "allowed"
                                    }
                                }
                            }
                        }
                    }
                ]
            },
            {
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
            }
        ]
    }
}

