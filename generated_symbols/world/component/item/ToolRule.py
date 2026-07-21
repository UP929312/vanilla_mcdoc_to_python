# Generated from symbols.json for ::java::world::component::item::ToolRule
from dataclasses import dataclass


@dataclass(kw_only=True)
class ToolRule:
    blocks: str | list[str]
    speed: float | None = None  # Overrides the default mining speed.
    correct_for_drops: bool | None = None  # Overrides whether or not this tool is considered correct to mine at its most efficient speed, and to drop items if the block's loot table requires it.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::ToolRule": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "blocks",
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
                                                    "value": "block"
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
                                                "value": "block"
                                            }
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "Overrides the default mining speed.",
                "key": "speed",
                "type": {
                    "kind": "float"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Overrides whether or not this tool is considered correct to mine at its most efficient speed, and to drop items if the block's loot table requires it.",
                "key": "correct_for_drops",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

