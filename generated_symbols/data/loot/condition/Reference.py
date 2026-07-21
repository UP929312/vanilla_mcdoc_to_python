# Generated from symbols.json for ::java::data::loot::condition::Reference
from dataclasses import dataclass


@dataclass(kw_only=True)
class Reference:
    name: str  # A cyclic reference causes a parsing failure.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::condition::Reference": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "A cyclic reference causes a parsing failure.",
                "key": "name",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "predicate"
                                }
                            }
                        }
                    ]
                }
            }
        ]
    }
}

