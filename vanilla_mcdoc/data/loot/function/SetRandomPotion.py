"""
Generated from symbols.json for ::java::data::loot::function::SetRandomPotion
Local link to file: vanilla_mcdoc/data/loot/function/SetRandomPotion.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.data.loot.function.Conditions import Conditions
from vanilla_mcdoc.minecraft_types import IdSpec


class SetRandomPotion(Conditions):
    options: Annotated[str, IdSpec(registry='potion', tags='allowed')] | list[Annotated[str, IdSpec(registry='potion')]] | None = None  # Possible potions to select from. Defaults to all potions.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::SetRandomPotion": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Possible potions to select from.\nDefaults to all potions.",
                "key": "options",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "tree",
                                        "values": {
                                            "registry": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "potion"
                                                }
                                            },
                                            "tags": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "allowed"
                                                }
                                            }
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "list",
                            "item": {
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
                        }
                    ]
                },
                "optional": True
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
