"""
Generated from symbols.json for ::java::data::loot::condition::Reference
Local link to file: generated_symbols/data/loot/condition/Reference.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from runtime_metadata import IdSpec


@dataclass(kw_only=True)
class Reference:
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

