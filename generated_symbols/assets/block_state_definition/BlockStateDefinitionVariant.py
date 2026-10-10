"""
Generated from symbols.json for ::java::assets::block_state_definition::BlockStateDefinitionVariant
Local link to file: generated_symbols/assets/block_state_definition/BlockStateDefinitionVariant.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.assets.block_state_definition.ModelVariant import ModelVariant


class BlockStateDefinitionVariant(GeneratedModel):
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
