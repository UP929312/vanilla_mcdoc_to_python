"""
Generated from symbols.json for ::java::data::loot::function::Reference
Local link to file: vanilla_mcdoc/data/loot/function/Reference.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.data.loot.function.Conditions import Conditions
from vanilla_mcdoc.minecraft_types import IdSpec


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
