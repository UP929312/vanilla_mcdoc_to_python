"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::RootPlacer
Local link to file: generated_symbols/data/worldgen/feature/tree/RootPlacer.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.IntProvider import IntProvider
    from generated_symbols.data.worldgen.feature.block_state_provider.BlockStateProvider import BlockStateProvider
    from generated_symbols.data.worldgen.feature.tree.AboveRootPlacement import AboveRootPlacement
    from generated_symbols.data.worldgen.feature.tree.MangroveRootPlacement import MangroveRootPlacement


@dataclass(kw_only=True)
class RootPlacerMangroveRootPlacer:
    type: Literal['minecraft:mangrove_root_placer']
    root_provider: BlockStateProvider
    trunk_offset_y: IntProvider[int] | int
    mangrove_root_placement: MangroveRootPlacement
    above_root_placement: AboveRootPlacement | None = None


type RootPlacer = RootPlacerMangroveRootPlacer


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::RootPlacer": {
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
                                    "value": "worldgen/root_placer_type"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "root_provider",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProvider"
                }
            },
            {
                "kind": "pair",
                "key": "trunk_offset_y",
                "type": {
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
            },
            {
                "kind": "pair",
                "key": "above_root_placement",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::tree::AboveRootPlacement"
                },
                "optional": True
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
                    "registry": "minecraft:root_placer"
                }
            }
        ]
    }
}

