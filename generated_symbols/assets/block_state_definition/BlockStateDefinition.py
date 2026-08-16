"""
Generated from symbols.json for ::java::assets::block_state_definition::BlockStateDefinition
Local link to file: generated_symbols/assets/block_state_definition/BlockStateDefinition.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from generated_symbols.assets.block_state_definition.ModelVariant import ModelVariant
    from generated_symbols.assets.block_state_definition.MultiPartCondition import MultiPartCondition


@dataclass(kw_only=True)
class MultipartStruct:
    when: MultiPartCondition | None = None  # One condition or an array where at least one condition must apply.
    apply: ModelVariant


@dataclass(kw_only=True)
class BlockStateDefinitionStruct1:
    __resource_dir__: ClassVar[str] = 'block_definition'

    variants: dict[str, ModelVariant]


@dataclass(kw_only=True)
class BlockStateDefinitionStruct2:
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

