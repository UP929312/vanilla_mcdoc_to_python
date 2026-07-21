# Generated from symbols.json for ::java::data::worldgen::feature::block_state_provider::NoiseProvider
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.worldgen.feature.block_state_provider.BaseNoiseProvider import BaseNoiseProvider

if TYPE_CHECKING:
    from generated_symbols.util.block_state.BlockState import BlockState


@dataclass(kw_only=True)
class NoiseProvider(BaseNoiseProvider):
    states: list[BlockState]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::block_state_provider::NoiseProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_state_provider::BaseNoiseProvider"
                }
            },
            {
                "kind": "pair",
                "key": "states",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::util::block_state::BlockState"
                    }
                }
            }
        ]
    }
}

