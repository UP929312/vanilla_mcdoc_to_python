# Generated from symbols.json for ::java::assets::block_state_definition::BlockStateDefinitionVariantMap
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.block_state_definition.ModelVariant import ModelVariant


type BlockStateDefinitionVariantMap = dict[str, ModelVariant]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::block_state_definition::BlockStateDefinitionVariantMap": {
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

