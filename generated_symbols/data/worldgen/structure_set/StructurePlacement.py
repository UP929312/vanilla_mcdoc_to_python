"""
Generated from symbols.json for ::java::data::worldgen::structure_set::StructurePlacement
Local link to file: generated_symbols/data/worldgen/structure_set/StructurePlacement.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from generated_symbols.base import GeneratedModel
from generated_symbols.data.worldgen.structure_set.ConcentricRingsPlacement import ConcentricRingsPlacement
from generated_symbols.data.worldgen.structure_set.RandomSpreadPlacement import RandomSpreadPlacement
from minecraft_registry import IdSpec


class StructurePlacementUnknown(GeneratedModel):
    type: Annotated[str, IdSpec(registry='worldgen/structure_placement')]


class StructurePlacementConcentricRings(ConcentricRingsPlacement):
    type: Literal['minecraft:concentric_rings'] = 'minecraft:concentric_rings'


class StructurePlacementRandomSpread(RandomSpreadPlacement):
    type: Literal['minecraft:random_spread'] = 'minecraft:random_spread'


type StructurePlacement = StructurePlacementUnknown | StructurePlacementConcentricRings | StructurePlacementRandomSpread


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::structure_set::StructurePlacement": {
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
                                    "value": "worldgen/structure_placement"
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
                    "registry": "minecraft:structure_placement"
                }
            }
        ]
    }
}

