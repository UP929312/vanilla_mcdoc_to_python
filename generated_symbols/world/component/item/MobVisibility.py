# Generated from symbols.json for ::java::world::component::item::MobVisibility
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class MobVisibility:
    targeting_entity_types: str | list[str]  # Entities to match.
    visibility: Annotated[float, 'Range | `0`-`10` | both inclusive']  # Visibility factor, with `0.0` reducing the range at which mobs detects the entity to `2`, while `10.0` increases the detection range tenfold. While multiple items with this component stack, the maximum vision will still never exceed `10.0`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::MobVisibility": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Entities to match.",
                "key": "targeting_entity_types",
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
                                                    "value": "entity_type"
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
                                                "value": "entity_type"
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
                "desc": "Visibility factor, with `0.0` reducing the range at which mobs detects the entity to `2`, while `10.0` increases the detection range tenfold.\nWhile multiple items with this component stack, the maximum vision will still never exceed `10.0`.",
                "key": "visibility",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 10
                    }
                }
            }
        ]
    }
}

