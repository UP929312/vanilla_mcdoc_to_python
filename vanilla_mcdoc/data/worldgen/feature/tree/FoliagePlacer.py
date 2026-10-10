"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::FoliagePlacer
Local link to file: vanilla_mcdoc/data/worldgen/feature/tree/FoliagePlacer.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.data.worldgen.feature.tree.CherryFoliagePlacer import CherryFoliagePlacer
from vanilla_mcdoc.data.worldgen.feature.tree.HeightFoliagePlacer import HeightFoliagePlacer
from vanilla_mcdoc.data.worldgen.feature.tree.MegaPineFoliagePlacer import MegaPineFoliagePlacer
from vanilla_mcdoc.data.worldgen.feature.tree.PineFoliagePlacer import PineFoliagePlacer
from vanilla_mcdoc.data.worldgen.feature.tree.PoplarFoliagePlacer import PoplarFoliagePlacer
from vanilla_mcdoc.data.worldgen.feature.tree.RandomSpreadFoliagePlacer import RandomSpreadFoliagePlacer
from vanilla_mcdoc.data.worldgen.feature.tree.SprucePineFoliagePlacer import SprucePineFoliagePlacer

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider


class FoliagePlacerBlobFoliagePlacer(HeightFoliagePlacer):
    type: Literal['minecraft:blob_foliage_placer', 'blob_foliage_placer'] = 'minecraft:blob_foliage_placer'
    radius: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]
    offset: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]


class FoliagePlacerBushFoliagePlacer(HeightFoliagePlacer):
    type: Literal['minecraft:bush_foliage_placer', 'bush_foliage_placer'] = 'minecraft:bush_foliage_placer'
    radius: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]
    offset: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]


class FoliagePlacerCherryFoliagePlacer(CherryFoliagePlacer):
    type: Literal['minecraft:cherry_foliage_placer', 'cherry_foliage_placer'] = 'minecraft:cherry_foliage_placer'
    radius: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]
    offset: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]


class FoliagePlacerFancyFoliagePlacer(HeightFoliagePlacer):
    type: Literal['minecraft:fancy_foliage_placer', 'fancy_foliage_placer'] = 'minecraft:fancy_foliage_placer'
    radius: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]
    offset: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]


class FoliagePlacerJungleFoliagePlacer(HeightFoliagePlacer):
    type: Literal['minecraft:jungle_foliage_placer', 'jungle_foliage_placer'] = 'minecraft:jungle_foliage_placer'
    radius: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]
    offset: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]


class FoliagePlacerMegaPineFoliagePlacer(MegaPineFoliagePlacer):
    type: Literal['minecraft:mega_pine_foliage_placer', 'mega_pine_foliage_placer'] = 'minecraft:mega_pine_foliage_placer'
    radius: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]
    offset: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]


class FoliagePlacerPineFoliagePlacer(PineFoliagePlacer):
    type: Literal['minecraft:pine_foliage_placer', 'pine_foliage_placer'] = 'minecraft:pine_foliage_placer'
    radius: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]
    offset: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]


class FoliagePlacerPoplarFoliagePlacer(PoplarFoliagePlacer):
    type: Literal['minecraft:poplar_foliage_placer', 'poplar_foliage_placer'] = 'minecraft:poplar_foliage_placer'
    radius: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]
    offset: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]


class FoliagePlacerRandomSpreadFoliagePlacer(RandomSpreadFoliagePlacer):
    type: Literal['minecraft:random_spread_foliage_placer', 'random_spread_foliage_placer'] = 'minecraft:random_spread_foliage_placer'
    radius: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]
    offset: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]


class FoliagePlacerSpruceFoliagePlacer(SprucePineFoliagePlacer):
    type: Literal['minecraft:spruce_foliage_placer', 'spruce_foliage_placer'] = 'minecraft:spruce_foliage_placer'
    radius: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]
    offset: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]


type FoliagePlacer = Annotated[
    FoliagePlacerBlobFoliagePlacer | FoliagePlacerBushFoliagePlacer | FoliagePlacerCherryFoliagePlacer | FoliagePlacerFancyFoliagePlacer | FoliagePlacerJungleFoliagePlacer | FoliagePlacerMegaPineFoliagePlacer | FoliagePlacerPineFoliagePlacer | FoliagePlacerPoplarFoliagePlacer | FoliagePlacerRandomSpreadFoliagePlacer | FoliagePlacerSpruceFoliagePlacer,
    Field(discriminator='type'),
]
