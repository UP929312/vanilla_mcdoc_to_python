# Generated from symbols.json for ::java::data::advancement::AdvancementRewards
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.loot.LootTableListRef import LootTableListRef


@dataclass(kw_only=True)
class AdvancementRewards:
    experience: int | None = None  # XP to add.
    loot: LootTableListRef | None = None  # Loot tables to give.
    recipes: list[str] | None = None  # Recipes to unlock.
    function: str | None = None  # Function to run as and at the player. Function tags are not allowed.


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
                    "kind": "reference",
                    "path": "::java::data::loot::LootTableListRef"
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

