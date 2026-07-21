# Generated from symbols.json for ::java::assets::block_state_definition::BlockStateDefinition
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from generated_symbols.assets.block_state_definition.ModelVariant import ModelVariant


@dataclass(kw_only=True)
class BlockStateDefinitionStruct1:
    variants: dict[str, ModelVariant]

@dataclass(kw_only=True)
class BlockStateDefinitionStruct2:
    multipart: list[Any]

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

