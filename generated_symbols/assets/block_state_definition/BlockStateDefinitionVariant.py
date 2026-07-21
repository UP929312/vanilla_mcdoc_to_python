# Generated from symbols.json for ::java::assets::block_state_definition::BlockStateDefinitionVariant
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.block_state_definition.ModelVariant import ModelVariant


@dataclass(kw_only=True)
class BlockStateDefinitionVariant:
    variants: dict[str, ModelVariant]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::block_state_definition::BlockStateDefinitionVariant": {
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
    }
}

