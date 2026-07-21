# Generated from symbols.json for ::java::data::worldgen::feature::BlockPileConfig
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.block_state_provider.BlockStateProvider import BlockStateProvider


@dataclass(kw_only=True)
class BlockPileConfig:
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

