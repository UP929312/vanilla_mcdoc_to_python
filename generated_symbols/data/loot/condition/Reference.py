"""
Generated from symbols.json for ::java::data::loot::condition::Reference
Local link to file: generated_symbols/data/loot/condition/Reference.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from generated_symbols.base import GeneratedModel
from minecraft_registry import IdSpec


class Reference(GeneratedModel):
    name: Annotated[str, IdSpec(registry='predicate')]  # A cyclic reference causes a parsing failure.


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

