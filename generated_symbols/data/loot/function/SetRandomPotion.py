# Generated from symbols.json for ::java::data::loot::function::SetRandomPotion
from dataclasses import dataclass
from generated_symbols.data.loot.function.Conditions import Conditions


@dataclass(kw_only=True)
class SetRandomPotion(Conditions):
    options: str | None = None  # Possible potions to select from. Defaults to all potions.


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

