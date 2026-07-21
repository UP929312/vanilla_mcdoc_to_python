# Generated from symbols.json for ::java::assets::block_state_definition::BlockStateDefinitionMultipart
from dataclasses import dataclass
from typing import Any


@dataclass(kw_only=True)
class BlockStateDefinitionMultipart:
    multipart: list[Any]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::block_state_definition::BlockStateDefinitionMultipart": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "multipart",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "struct",
                        "fields": [
                            {
                                "kind": "pair",
                                "desc": "One condition or an array where at least one condition must apply.",
                                "key": "when",
                                "type": {
                                    "kind": "reference",
                                    "path": "::java::assets::block_state_definition::MultiPartCondition"
                                },
                                "optional": True
                            },
                            {
                                "kind": "pair",
                                "key": "apply",
                                "type": {
                                    "kind": "reference",
                                    "path": "::java::assets::block_state_definition::ModelVariant"
                                }
                            }
                        ]
                    }
                }
            }
        ]
    }
}

