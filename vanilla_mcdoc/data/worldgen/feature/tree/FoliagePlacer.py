"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::FoliagePlacer
Local link to file: vanilla_mcdoc/data/worldgen/feature/tree/FoliagePlacer.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from pydantic import Discriminator, Field, Tag

from vanilla_mcdoc.base import GeneratedModel, tag_of
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


class FoliagePlacerAcaciaFoliagePlacer(GeneratedModel):
    type: Literal['minecraft:acacia_foliage_placer', 'acacia_foliage_placer'] = 'minecraft:acacia_foliage_placer'
    radius: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]
    offset: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]


class FoliagePlacerDarkOakFoliagePlacer(GeneratedModel):
    type: Literal['minecraft:dark_oak_foliage_placer', 'dark_oak_foliage_placer'] = 'minecraft:dark_oak_foliage_placer'
    radius: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]
    offset: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]


type FoliagePlacer = Annotated[
    Annotated[FoliagePlacerBlobFoliagePlacer, Tag('minecraft:blob_foliage_placer')]
    | Annotated[FoliagePlacerBushFoliagePlacer, Tag('minecraft:bush_foliage_placer')]
    | Annotated[FoliagePlacerCherryFoliagePlacer, Tag('minecraft:cherry_foliage_placer')]
    | Annotated[FoliagePlacerFancyFoliagePlacer, Tag('minecraft:fancy_foliage_placer')]
    | Annotated[FoliagePlacerJungleFoliagePlacer, Tag('minecraft:jungle_foliage_placer')]
    | Annotated[FoliagePlacerMegaPineFoliagePlacer, Tag('minecraft:mega_pine_foliage_placer')]
    | Annotated[FoliagePlacerPineFoliagePlacer, Tag('minecraft:pine_foliage_placer')]
    | Annotated[FoliagePlacerPoplarFoliagePlacer, Tag('minecraft:poplar_foliage_placer')]
    | Annotated[FoliagePlacerRandomSpreadFoliagePlacer, Tag('minecraft:random_spread_foliage_placer')]
    | Annotated[FoliagePlacerSpruceFoliagePlacer, Tag('minecraft:spruce_foliage_placer')]
    | Annotated[FoliagePlacerAcaciaFoliagePlacer, Tag('minecraft:acacia_foliage_placer')]
    | Annotated[FoliagePlacerDarkOakFoliagePlacer, Tag('minecraft:dark_oak_foliage_placer')],
    Discriminator(tag_of('type')),
]
