"""
Generated from symbols.json for ::java::data::loot::function::SetRandomPotion
Local link to file: generated_symbols/data/loot/function/SetRandomPotion.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from generated_symbols.data.loot.function.Conditions import Conditions
from minecraft_registry import IdSpec


@dataclass(kw_only=True)
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

