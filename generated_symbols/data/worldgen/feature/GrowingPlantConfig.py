"""
Generated from symbols.json for ::java::data::worldgen::feature::GrowingPlantConfig
Local link to file: generated_symbols/data/worldgen/feature/GrowingPlantConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.IntProvider import IntProvider
    from generated_symbols.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef
    from generated_symbols.util.WeightedList import WeightedList
    from generated_symbols.util.direction.Direction import Direction


class GrowingPlantConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    direction: Direction
    allow_water: bool
    height_distribution: WeightedList[IntProvider[int] | int]
    body_provider: BlockStateProviderRef
    head_provider: BlockStateProviderRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::GrowingPlantConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "direction",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::direction::Direction"
                }
            },
            {
                "kind": "pair",
                "key": "allow_water",
                "type": {
                    "kind": "boolean"
                }
            },
            {
                "kind": "pair",
                "key": "height_distribution",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::util::WeightedList"
                    },
                    "typeArgs": [
                        {
                            "kind": "concrete",
                            "child": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::IntProvider"
                            },
                            "typeArgs": [
                                {
                                    "kind": "int"
                                }
                            ]
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "body_provider",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProviderRef"
                }
            },
            {
                "kind": "pair",
                "key": "head_provider",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProviderRef"
                }
            }
        ]
    }
}
