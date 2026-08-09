# Generated from symbols.json for ::java::data::advancement::predicate::PlayerRecipes
from typing import Annotated

from runtime_metadata import IdSpec


type PlayerRecipes = dict[Annotated[str, IdSpec(registry='recipe')], bool]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::PlayerRecipes": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
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
                    "kind": "boolean"
                }
            }
        ]
    }
}

