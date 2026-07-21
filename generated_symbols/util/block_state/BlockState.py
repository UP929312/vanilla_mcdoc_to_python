# Generated from symbols.json for ::java::util::block_state::BlockState
from dataclasses import dataclass
from typing import Any


@dataclass(kw_only=True)
class BlockState:
    Name: str
    Properties: Any | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::block_state::BlockState": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "Name",
                "type": {
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
            },
            {
                "kind": "pair",
                "key": "Properties",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "Name"
                            ]
                        }
                    ],
                    "registry": "mcdoc:block_states"
                },
                "optional": True
            }
        ]
    }
}

