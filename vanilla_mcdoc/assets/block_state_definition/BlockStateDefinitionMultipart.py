"""
Generated from symbols.json for ::java::assets::block_state_definition::BlockStateDefinitionMultipart
Local link to file: vanilla_mcdoc/assets/block_state_definition/BlockStateDefinitionMultipart.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.block_state_definition.ModelVariant import ModelVariant
    from vanilla_mcdoc.assets.block_state_definition.MultiPartCondition import MultiPartCondition


class MultipartStruct(GeneratedModel):
    when: MultiPartCondition | None = None  # One condition or an array where at least one condition must apply.
    apply: ModelVariant


class BlockStateDefinitionMultipart(GeneratedModel):
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
