"""
Generated from symbols.json for ::java::world::block::furnace::RecipesUsed
Local link to file: generated_symbols/world/block/furnace/RecipesUsed.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from runtime_metadata import IdSpec


type RecipesUsed = dict[Annotated[str, IdSpec(registry='recipe')], int]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::furnace::RecipesUsed": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "How many times this recipe has been used.",
                "key": {
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
                },
                "type": {
                    "kind": "int"
                }
            }
        ]
    }
}

