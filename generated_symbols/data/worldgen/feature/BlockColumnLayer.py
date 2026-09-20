"""
Generated from symbols.json for ::java::data::worldgen::feature::BlockColumnLayer
Local link to file: generated_symbols/data/worldgen/feature/BlockColumnLayer.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from generated_symbols.base import GeneratedModel
from pydantic import Field

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.IntProvider import IntProvider
    from generated_symbols.data.worldgen.feature.block_state_provider.BlockStateProvider import BlockStateProvider


class BlockColumnLayer(GeneratedModel):
    height: IntProvider[Annotated[int, Field(ge=0)]] | Annotated[int, Field(ge=0)]
    provider: BlockStateProvider


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::BlockColumnLayer": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "height",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::IntProvider"
                    },
                    "typeArgs": [
                        {
                            "kind": "int",
                            "valueRange": {
                                "kind": 0,
                                "min": 0
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "provider",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProvider"
                }
            }
        ]
    }
}

