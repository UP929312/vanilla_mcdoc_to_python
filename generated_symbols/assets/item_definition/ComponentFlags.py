# Generated from symbols.json for ::java::assets::item_definition::ComponentFlags
from dataclasses import dataclass
from typing import Any


@dataclass(kw_only=True)
class ComponentFlags:
    predicate: str  # The component predicate to check.
    value: Any  # The predicate-specific value.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::ComponentFlags": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The component predicate to check.",
                "key": "predicate",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21.5"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "item_sub_predicate_type"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21.5"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "data_component_predicate_type"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "The predicate-specific value.",
                "key": "value",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "predicate"
                            ]
                        }
                    ],
                    "registry": "minecraft:data_component_predicate"
                }
            }
        ]
    }
}

