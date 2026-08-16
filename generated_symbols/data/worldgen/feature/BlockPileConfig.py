"""
Generated from symbols.json for ::java::data::worldgen::feature::BlockPileConfig
Local link to file: generated_symbols/data/worldgen/feature/BlockPileConfig.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.block_state_provider.BlockStateProvider import BlockStateProvider


@dataclass(kw_only=True)
class BlockPileConfig:
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    state_provider: BlockStateProvider


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::BlockPileConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "state_provider",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProvider"
                }
            }
        ]
    }
}

