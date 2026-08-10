"""
Generated from symbols.json for ::java::data::loot::function::SetPotion
Local link to file: generated_symbols/data/loot/function/SetPotion.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from generated_symbols.data.loot.function.Conditions import Conditions
from runtime_metadata import IdSpec


@dataclass(kw_only=True)
class SetPotion(Conditions):
    id: Annotated[str, IdSpec(registry='potion')]  # The potion identifier.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::SetPotion": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The potion identifier.",
                "key": "id",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "potion"
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

