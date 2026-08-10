"""
Generated from symbols.json for ::java::assets::block_state_definition::BlockStateDefinitionMultipart
Local link to file: generated_symbols/assets/block_state_definition/BlockStateDefinitionMultipart.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.block_state_definition.ModelVariant import ModelVariant
    from generated_symbols.assets.block_state_definition.MultiPartCondition import MultiPartCondition


@dataclass(kw_only=True)
class MultipartStruct:
    apply: ModelVariant
    when: MultiPartCondition | None = None  # One condition or an array where at least one condition must apply.


@dataclass(kw_only=True)
class BlockStateDefinitionMultipart:
    multipart: list[MultipartStruct]


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

