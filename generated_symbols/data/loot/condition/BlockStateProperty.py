# Generated from symbols.json for ::java::data::loot::condition::BlockStateProperty
from dataclasses import dataclass
from typing import Any


@dataclass(kw_only=True)
class BlockStateProperty:
    block: str
    properties: Any | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::condition::BlockStateProperty": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "block",
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
                "key": "properties",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "block"
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

