# Generated from symbols.json for ::java::world::component::item::RemoveEffectsConsumeEffect
from dataclasses import dataclass


@dataclass(kw_only=True)
class RemoveEffectsConsumeEffect:
    effects: str | list[str]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::RemoveEffectsConsumeEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "effects",
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
                                                    "value": "mob_effect"
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
                                                "value": "mob_effect"
                                            }
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
        ]
    }
}

