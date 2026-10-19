"""
Generated from symbols.json for ::java::data::worldgen::structure_set::StructurePlacement
Local link to file: vanilla_mcdoc/data/worldgen/structure_set/StructurePlacement.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Discriminator, Tag

from vanilla_mcdoc.base import GeneratedModel, tag_of
from vanilla_mcdoc.data.worldgen.structure_set.ConcentricRingsPlacement import ConcentricRingsPlacement
from vanilla_mcdoc.data.worldgen.structure_set.RandomSpreadPlacement import RandomSpreadPlacement


class StructurePlacementConcentricRings(ConcentricRingsPlacement):
    type: Literal['minecraft:concentric_rings', 'concentric_rings'] = 'minecraft:concentric_rings'


class StructurePlacementRandomSpread(RandomSpreadPlacement):
    type: Literal['minecraft:random_spread', 'random_spread'] = 'minecraft:random_spread'


class StructurePlacementDimensionOrigin(GeneratedModel):
    type: Literal['minecraft:dimension_origin', 'dimension_origin'] = 'minecraft:dimension_origin'


type StructurePlacement = Annotated[
    Annotated[StructurePlacementConcentricRings, Tag('minecraft:concentric_rings')]
    | Annotated[StructurePlacementRandomSpread, Tag('minecraft:random_spread')]
    | Annotated[StructurePlacementDimensionOrigin, Tag('minecraft:dimension_origin')],
    Discriminator(tag_of('type')),
]
