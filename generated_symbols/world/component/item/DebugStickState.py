"""
Generated from symbols.json for ::java::world::component::item::DebugStickState
Local link to file: generated_symbols/world/component/item/DebugStickState.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from runtime_metadata import IdSpec


type DebugStickState = dict[Annotated[str, IdSpec(registry='block')], str]


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

