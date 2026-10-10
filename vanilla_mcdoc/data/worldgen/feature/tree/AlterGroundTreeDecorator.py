"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::AlterGroundTreeDecorator
Local link to file: vanilla_mcdoc/data/worldgen/feature/tree/AlterGroundTreeDecorator.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef


class AlterGroundTreeDecorator(GeneratedModel):
    provider: BlockStateProviderRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::AlterGroundTreeDecorator": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "provider",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProviderRef"
                }
            }
        ]
    }
}
