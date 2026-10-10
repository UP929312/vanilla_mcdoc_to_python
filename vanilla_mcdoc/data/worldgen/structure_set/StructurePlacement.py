"""
Generated from symbols.json for ::java::data::worldgen::structure_set::StructurePlacement
Local link to file: vanilla_mcdoc/data/worldgen/structure_set/StructurePlacement.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.data.worldgen.structure_set.ConcentricRingsPlacement import ConcentricRingsPlacement
from vanilla_mcdoc.data.worldgen.structure_set.RandomSpreadPlacement import RandomSpreadPlacement
from vanilla_mcdoc.minecraft_types import IdSpec


class StructurePlacementUnknown(GeneratedModel):
    type: Annotated[str, IdSpec(registry='worldgen/structure_placement')]


class StructurePlacementConcentricRings(ConcentricRingsPlacement):
    type: Literal['minecraft:concentric_rings', 'concentric_rings'] = 'minecraft:concentric_rings'


class StructurePlacementRandomSpread(RandomSpreadPlacement):
    type: Literal['minecraft:random_spread', 'random_spread'] = 'minecraft:random_spread'


type StructurePlacement = StructurePlacementUnknown | StructurePlacementConcentricRings | StructurePlacementRandomSpread
