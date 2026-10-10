"""
Generated from symbols.json for ::java::data::worldgen::feature::block_state_provider::DualNoiseProvider
Local link to file: vanilla_mcdoc/data/worldgen/feature/block_state_provider/DualNoiseProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.data.worldgen.feature.block_state_provider.BaseNoiseProvider import BaseNoiseProvider

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.dimension.biome_source.NoiseParameters import NoiseParameters
    from vanilla_mcdoc.util.InclusiveRange import InclusiveRange
    from vanilla_mcdoc.util.block_state.BlockState import BlockState


class DualNoiseProvider(BaseNoiseProvider):
    variety: InclusiveRange[Annotated[int, Field(ge=1, le=64)]] | Annotated[int, Field(ge=1, le=64)]
    slow_noise: NoiseParameters
    slow_scale: Annotated[float, Field(ge=0)]
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
