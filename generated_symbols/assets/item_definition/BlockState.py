# Generated from symbols.json for ::java::assets::item_definition::BlockState
from dataclasses import dataclass
from typing import Any
from generated_symbols.assets.item_definition.SelectCases import SelectCases


@dataclass(kw_only=True)
class BlockState(SelectCases[str]):
    block_state_property: Any


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::BlockState": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "block_state_property",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "static",
                            "value": "%fallback"
                        }
                    ],
                    "registry": "mcdoc:block_state_keys"
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::assets::item_definition::SelectCases"
                    },
                    "typeArgs": [
                        {
                            "kind": "string"
                        }
                    ]
                }
            }
        ]
    }
}

