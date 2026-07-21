# Generated from symbols.json for ::java::data::loot::function::CopyState
from dataclasses import dataclass
from typing import Any
from generated_symbols.data.loot.function.Conditions import Conditions


@dataclass(kw_only=True)
class CopyState(Conditions):
    block: str
    properties: list[Any]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::CopyState": {
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
                    "kind": "list",
                    "item": {
                        "kind": "dispatcher",
                        "parallelIndices": [
                            {
                                "kind": "dynamic",
                                "accessor": [
                                    {
                                        "keyword": "parent"
                                    },
                                    "block"
                                ]
                            }
                        ],
                        "registry": "mcdoc:block_state_keys"
                    }
                }
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

