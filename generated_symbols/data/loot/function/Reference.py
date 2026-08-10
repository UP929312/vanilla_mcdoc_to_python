"""
Generated from symbols.json for ::java::data::loot::function::Reference
Local link to file: generated_symbols/data/loot/function/Reference.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from generated_symbols.data.loot.function.Conditions import Conditions
from runtime_metadata import IdSpec


@dataclass(kw_only=True)
class Reference(Conditions):
    name: Annotated[str, IdSpec(registry='item_modifier')]  # Item modifier to reference.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::Reference": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Item modifier to reference.",
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
                                    "value": "item_modifier"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::function::Conditions"
                }
            }
        ]
    }
}

