# Generated from symbols.json for ::java::data::dialog::input::InputControl
from dataclasses import dataclass
from typing import Annotated, Any


@dataclass(kw_only=True)
class InputControl:
    type: str
    key: Annotated[str, 'Length = 1 (inclusive) and above'] | Any  # The input key, which is used to build macro command and generate custom action payload.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::dialog::input::InputControl": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "input_control_type"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "The input key, which is used to build macro command and generate custom action payload.",
                "key": "key",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "union",
                            "members": [
                                {
                                    "kind": "string",
                                    "lengthRange": {
                                        "kind": 0,
                                        "min": 1
                                    },
                                    "attributes": [
                                        {
                                            "name": "match_regex",
                                            "value": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "^[A-Za-z0-9_]*$"
                                                }
                                            }
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "kind": "dispatcher",
                            "parallelIndices": [
                                {
                                    "kind": "static",
                                    "value": "%fallback"
                                }
                            ],
                            "registry": "mcdoc:custom_dynamic_event_keys"
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:input_control"
                }
            }
        ]
    }
}

