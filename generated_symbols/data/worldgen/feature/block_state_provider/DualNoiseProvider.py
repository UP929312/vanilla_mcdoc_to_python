# Generated from symbols.json for ::java::data::worldgen::feature::block_state_provider::DualNoiseProvider
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated
from generated_symbols.data.worldgen.feature.block_state_provider.BaseNoiseProvider import BaseNoiseProvider

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.dimension.biome_source.NoiseParameters import NoiseParameters
    from generated_symbols.util.InclusiveRange import InclusiveRange
    from generated_symbols.util.block_state.BlockState import BlockState


@dataclass(kw_only=True)
class DualNoiseProvider(BaseNoiseProvider):
    variety: InclusiveRange[Annotated[int, 'Range | `1`-`64` | both inclusive']] | Annotated[int, 'Range | `1`-`64` | both inclusive']
    slow_noise: NoiseParameters
    slow_scale: Annotated[float, 'Range | Min `0` and above | inclusive']
    states: list[BlockState]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::block_state_provider::DualNoiseProvider": {
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
                "key": "variety",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::util::InclusiveRange"
                    },
                    "typeArgs": [
                        {
                            "kind": "int",
                            "valueRange": {
                                "kind": 0,
                                "min": 1,
                                "max": 64
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "slow_noise",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::dimension::biome_source::NoiseParameters"
                }
            },
            {
                "kind": "pair",
                "key": "slow_scale",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
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

