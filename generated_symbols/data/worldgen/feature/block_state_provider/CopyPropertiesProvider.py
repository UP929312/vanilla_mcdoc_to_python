"""
Generated from symbols.json for ::java::data::worldgen::feature::block_state_provider::CopyPropertiesProvider
Local link to file: generated_symbols/data/worldgen/feature/block_state_provider/CopyPropertiesProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.block_state_provider.BlockStateProvider import BlockStateProvider


class CopyPropertiesProvider(GeneratedModel):
    source: BlockStateProvider


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::block_state_provider::CopyPropertiesProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "source",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProvider"
                }
            }
        ]
    }
}

