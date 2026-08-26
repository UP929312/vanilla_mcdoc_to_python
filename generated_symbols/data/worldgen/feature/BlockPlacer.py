"""
Generated from symbols.json for ::java::data::worldgen::feature::BlockPlacer
Local link to file: generated_symbols/data/worldgen/feature/BlockPlacer.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Literal

from generated_symbols.data.worldgen.feature.ColumnPlacer import ColumnPlacer


@dataclass(kw_only=True)
class BlockPlacerColumnPlacer(ColumnPlacer):
    type: Literal['minecraft:column_placer']


@dataclass(kw_only=True)
class BlockPlacerDoublePlantPlacer:
    type: Literal['minecraft:double_plant_placer']


@dataclass(kw_only=True)
class BlockPlacerSimpleBlockPlacer:
    type: Literal['minecraft:simple_block_placer']


type BlockPlacer = BlockPlacerColumnPlacer | BlockPlacerDoublePlantPlacer | BlockPlacerSimpleBlockPlacer


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::BlockPlacer": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "worldgen/block_placer_type"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:block_placer"
                }
            }
        ]
    }
}

