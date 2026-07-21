# Generated from symbols.json for ::java::data::worldgen::feature::block_state_provider::NoiseThresholdProvider
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated
from generated_symbols.data.worldgen.feature.block_state_provider.BaseNoiseProvider import BaseNoiseProvider

if TYPE_CHECKING:
    from generated_symbols.util.block_state.BlockState import BlockState


@dataclass(kw_only=True)
class NoiseThresholdProvider(BaseNoiseProvider):
    threshold: Annotated[float, 'Range | `-1`-`1` | both inclusive']
    high_chance: Annotated[float, 'Range | `0`-`1` | both inclusive']
    default_state: BlockState
    low_states: list[BlockState]
    high_states: list[BlockState]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::block_state_provider::NoiseThresholdProvider": {
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
                "key": "threshold",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": -1,
                        "max": 1
                    }
                }
            },
            {
                "kind": "pair",
                "key": "high_chance",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                }
            },
            {
                "kind": "pair",
                "key": "default_state",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::block_state::BlockState"
                }
            },
            {
                "kind": "pair",
                "key": "low_states",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::util::block_state::BlockState"
                    }
                }
            },
            {
                "kind": "pair",
                "key": "high_states",
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

