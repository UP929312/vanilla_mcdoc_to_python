"""
Generated from symbols.json for ::java::data::advancement::AdvancementRewards
Local link to file: generated_symbols/data/advancement/AdvancementRewards.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.loot.LootTableListRef import LootTableListRef


@dataclass(kw_only=True)
class AdvancementRewards:
    experience: int | None = None  # XP to add.
    loot: LootTableListRef | None = None  # Loot tables to give.
    recipes: list[Annotated[str, IdSpec(registry='recipe')]] | None = None  # Recipes to unlock.
    function: Annotated[str, IdSpec(registry='function')] | None = None  # Function to run as and at the player. Function tags are not allowed.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::AdvancementRewards": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "XP to add.",
                "key": "experience",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Loot tables to give.",
                "key": "loot",
                "type": {
                    "kind": "union",
                    "members": [
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
                                                "value": "loot_table"
                                            }
                                        }
                                    }
                                ]
                            },
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "26.3"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "reference",
                            "path": "::java::data::loot::LootTableListRef",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "26.3"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Recipes to unlock.",
                "key": "recipes",
                "type": {
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
                                        "value": "recipe"
                                    }
                                }
                            }
                        ]
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Function to run as and at the player. Function tags are not allowed.",
                "key": "function",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "function"
                                }
                            }
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

