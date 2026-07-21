# Generated from symbols.json for ::java::world::component::item::DebugStickState
from typing import Any


type DebugStickState = dict[str, Any]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::DebugStickState": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
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
                },
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                {
                                    "keyword": "key"
                                }
                            ]
                        }
                    ],
                    "registry": "mcdoc:block_state_keys"
                }
            }
        ]
    }
}

