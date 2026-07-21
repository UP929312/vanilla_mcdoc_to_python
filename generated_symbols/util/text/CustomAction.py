# Generated from symbols.json for ::java::util::text::CustomAction
from dataclasses import dataclass
from typing import Any


@dataclass(kw_only=True)
class CustomAction:
    id: str  # ID of a custom action. Has no functionality on vanilla servers.
    payload: Any | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::CustomAction": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "ID of a custom action.\nHas no functionality on vanilla servers.",
                "key": "id",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id"
                        },
                        {
                            "name": "dispatcher_key",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "mcdoc:custom_event"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "payload",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "id"
                            ]
                        }
                    ],
                    "registry": "mcdoc:custom_event"
                },
                "optional": True
            }
        ]
    }
}

