"""
Generated from symbols.json for ::java::data::worldgen::feature::GrowingPlantConfig
Local link to file: generated_symbols/data/worldgen/feature/GrowingPlantConfig.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.GrowingPlantHeight import GrowingPlantHeight
    from generated_symbols.data.worldgen.feature.block_state_provider.BlockStateProvider import BlockStateProvider
    from generated_symbols.util.direction.Direction import Direction


@dataclass(kw_only=True)
class GrowingPlantConfig:
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    direction: Direction
    allow_water: bool
    height_distribution: list[GrowingPlantHeight]
    body_provider: BlockStateProvider
    head_provider: BlockStateProvider


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
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::feature::GrowingPlantHeight"
                    }
                }
            },
            {
                "kind": "pair",
                "key": "body_provider",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProvider"
                }
            },
            {
                "kind": "pair",
                "key": "head_provider",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProvider"
                }
            }
        ]
    }
}

