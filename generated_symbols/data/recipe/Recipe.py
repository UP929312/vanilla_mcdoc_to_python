# Generated from symbols.json for ::java::data::recipe::Recipe
from dataclasses import dataclass


@dataclass(kw_only=True)
class Recipe:
    type: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::recipe::Recipe": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "recipe_serializer"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:recipe_serializer"
                }
            }
        ]
    }
}

