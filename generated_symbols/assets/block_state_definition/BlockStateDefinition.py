"""
Generated from symbols.json for ::java::assets::block_state_definition::BlockStateDefinition
Local link to file: generated_symbols/assets/block_state_definition/BlockStateDefinition.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.assets.block_state_definition.ModelVariant import ModelVariant
    from generated_symbols.assets.block_state_definition.MultiPartCondition import MultiPartCondition


class MultipartStruct(GeneratedModel):
    when: MultiPartCondition | None = None  # One condition or an array where at least one condition must apply.
    apply: ModelVariant


class BlockStateDefinitionStruct1(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'block_definition'

    variants: dict[str, ModelVariant]


class BlockStateDefinitionStruct2(GeneratedModel):
    multipart: list[MultipartStruct]


type BlockStateDefinition = BlockStateDefinitionStruct1 | BlockStateDefinitionStruct2


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::block_state_definition::BlockStateDefinition": {
        "kind": "union",
        "members": [
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "key": "variants",
                        "type": {
                            "kind": "struct",
                            "fields": [
                                {
                                    "kind": "pair",
                                    "key": {
                                        "kind": "string"
                                    },
                                    "type": {
                                        "kind": "reference",
                                        "path": "::java::assets::block_state_definition::ModelVariant"
                                    }
                                }
                            ]
                        }
                    }
                ]
            },
            {
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
        ]
    }
}

