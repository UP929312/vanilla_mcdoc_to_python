# Generated from symbols.json for ::java::data::recipe::IngredientItem
from dataclasses import dataclass


@dataclass(kw_only=True)
class IngredientItem:
    item: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::recipe::IngredientItem": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "item",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "item"
                                }
                            }
                        }
                    ]
                }
            }
        ]
    }
}

