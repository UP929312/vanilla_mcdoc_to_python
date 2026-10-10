"""
Generated from symbols.json for ::java::data::worldgen::feature::block_state_provider::CopyPropertiesProvider
Local link to file: vanilla_mcdoc/data/worldgen/feature/block_state_provider/CopyPropertiesProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef


class CopyPropertiesProvider(GeneratedModel):
    source: BlockStateProviderRef


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
                    "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProviderRef"
                }
            }
        ]
    }
}
