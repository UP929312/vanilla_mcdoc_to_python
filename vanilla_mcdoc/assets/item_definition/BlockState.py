"""
Generated from symbols.json for ::java::assets::item_definition::BlockState
Local link to file: vanilla_mcdoc/assets/item_definition/BlockState.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.assets.item_definition.SelectCases import SelectCases


class BlockState(SelectCases[str]):
    block_state_property: str


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
