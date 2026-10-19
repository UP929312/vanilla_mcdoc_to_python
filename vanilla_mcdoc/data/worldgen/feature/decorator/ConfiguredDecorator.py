"""
Generated from symbols.json for ::java::data::worldgen::feature::decorator::ConfiguredDecorator
Local link to file: vanilla_mcdoc/data/worldgen/feature/decorator/ConfiguredDecorator.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from pydantic import Discriminator, Tag

from vanilla_mcdoc.base import GeneratedModel, tag_of

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.decorator.CarvingMaskConfig import CarvingMaskConfig
    from vanilla_mcdoc.data.worldgen.feature.decorator.CaveSurface import CaveSurface
    from vanilla_mcdoc.data.worldgen.feature.decorator.ChanceConfig import ChanceConfig
    from vanilla_mcdoc.data.worldgen.feature.decorator.CountConfig import CountConfig
    from vanilla_mcdoc.data.worldgen.feature.decorator.CountExtraConfig import CountExtraConfig
    from vanilla_mcdoc.data.worldgen.feature.decorator.CountNoiseBiasedConfig import CountNoiseBiasedConfig
    from vanilla_mcdoc.data.worldgen.feature.decorator.CountNoiseConfig import CountNoiseConfig
    from vanilla_mcdoc.data.worldgen.feature.decorator.DecoratedConfig import DecoratedConfig
    from vanilla_mcdoc.data.worldgen.feature.decorator.HeightmapConfig import HeightmapConfig
    from vanilla_mcdoc.data.worldgen.feature.decorator.RangeConfig import RangeConfig
    from vanilla_mcdoc.data.worldgen.feature.decorator.WaterDepthThresholdConfig import WaterDepthThresholdConfig


class ConfigStruct(GeneratedModel):
    pass


class ConfiguredDecoratorCarvingMask(GeneratedModel):
    type: Literal['minecraft:carving_mask', 'carving_mask'] = 'minecraft:carving_mask'
    config: CarvingMaskConfig


class ConfiguredDecoratorCaveSurface(GeneratedModel):
    type: Literal['minecraft:cave_surface', 'cave_surface'] = 'minecraft:cave_surface'
    config: CaveSurface


class ConfiguredDecoratorChance(GeneratedModel):
    type: Literal['minecraft:chance', 'chance'] = 'minecraft:chance'
    config: ChanceConfig


class ConfiguredDecoratorCount(GeneratedModel):
    type: Literal['minecraft:count', 'count'] = 'minecraft:count'
    config: CountConfig


class ConfiguredDecoratorCountExtra(GeneratedModel):
    type: Literal['minecraft:count_extra', 'count_extra'] = 'minecraft:count_extra'
    config: CountExtraConfig


class ConfiguredDecoratorCountMultilayer(GeneratedModel):
    type: Literal['minecraft:count_multilayer', 'count_multilayer'] = 'minecraft:count_multilayer'
    config: CountConfig


class ConfiguredDecoratorCountNoise(GeneratedModel):
    type: Literal['minecraft:count_noise', 'count_noise'] = 'minecraft:count_noise'
    config: CountNoiseConfig


class ConfiguredDecoratorCountNoiseBiased(GeneratedModel):
    type: Literal['minecraft:count_noise_biased', 'count_noise_biased'] = 'minecraft:count_noise_biased'
    config: CountNoiseBiasedConfig


class ConfiguredDecoratorDarkOakTree(GeneratedModel):
    type: Literal['minecraft:dark_oak_tree', 'dark_oak_tree'] = 'minecraft:dark_oak_tree'
    config: ConfigStruct


class ConfiguredDecoratorDecorated(GeneratedModel):
    type: Literal['minecraft:decorated', 'decorated'] = 'minecraft:decorated'
    config: DecoratedConfig


class ConfiguredDecoratorEndGateway(GeneratedModel):
    type: Literal['minecraft:end_gateway', 'end_gateway'] = 'minecraft:end_gateway'
    config: ConfigStruct


class ConfiguredDecoratorFire(GeneratedModel):
    type: Literal['minecraft:fire', 'fire'] = 'minecraft:fire'
    config: CountConfig


class ConfiguredDecoratorGlowstone(GeneratedModel):
    type: Literal['minecraft:glowstone', 'glowstone'] = 'minecraft:glowstone'
    config: CountConfig


class ConfiguredDecoratorHeightmap(GeneratedModel):
    type: Literal['minecraft:heightmap', 'heightmap'] = 'minecraft:heightmap'
    config: HeightmapConfig


class ConfiguredDecoratorHeightmapSpreadDouble(GeneratedModel):
    type: Literal['minecraft:heightmap_spread_double', 'heightmap_spread_double'] = 'minecraft:heightmap_spread_double'
    config: HeightmapConfig


class ConfiguredDecoratorIceberg(GeneratedModel):
    type: Literal['minecraft:iceberg', 'iceberg'] = 'minecraft:iceberg'
    config: ConfigStruct


class ConfiguredDecoratorLavaLake(GeneratedModel):
    type: Literal['minecraft:lava_lake', 'lava_lake'] = 'minecraft:lava_lake'
    config: ChanceConfig


class ConfiguredDecoratorNope(GeneratedModel):
    type: Literal['minecraft:nope', 'nope'] = 'minecraft:nope'
    config: ConfigStruct


class ConfiguredDecoratorRange(GeneratedModel):
    type: Literal['minecraft:range', 'range'] = 'minecraft:range'
    config: RangeConfig


class ConfiguredDecoratorSpread32Above(GeneratedModel):
    type: Literal['minecraft:spread_32_above', 'spread_32_above'] = 'minecraft:spread_32_above'
    config: ConfigStruct


class ConfiguredDecoratorSquare(GeneratedModel):
    type: Literal['minecraft:square', 'square'] = 'minecraft:square'
    config: ConfigStruct


class ConfiguredDecoratorWaterDepthThreshold(GeneratedModel):
    type: Literal['minecraft:water_depth_threshold', 'water_depth_threshold'] = 'minecraft:water_depth_threshold'
    config: WaterDepthThresholdConfig


type ConfiguredDecorator = Annotated[
    Annotated[ConfiguredDecoratorCarvingMask, Tag('minecraft:carving_mask')]
    | Annotated[ConfiguredDecoratorCaveSurface, Tag('minecraft:cave_surface')]
    | Annotated[ConfiguredDecoratorChance, Tag('minecraft:chance')]
    | Annotated[ConfiguredDecoratorCount, Tag('minecraft:count')]
    | Annotated[ConfiguredDecoratorCountExtra, Tag('minecraft:count_extra')]
    | Annotated[ConfiguredDecoratorCountMultilayer, Tag('minecraft:count_multilayer')]
    | Annotated[ConfiguredDecoratorCountNoise, Tag('minecraft:count_noise')]
    | Annotated[ConfiguredDecoratorCountNoiseBiased, Tag('minecraft:count_noise_biased')]
    | Annotated[ConfiguredDecoratorDarkOakTree, Tag('minecraft:dark_oak_tree')]
    | Annotated[ConfiguredDecoratorDecorated, Tag('minecraft:decorated')]
    | Annotated[ConfiguredDecoratorEndGateway, Tag('minecraft:end_gateway')]
    | Annotated[ConfiguredDecoratorFire, Tag('minecraft:fire')]
    | Annotated[ConfiguredDecoratorGlowstone, Tag('minecraft:glowstone')]
    | Annotated[ConfiguredDecoratorHeightmap, Tag('minecraft:heightmap')]
    | Annotated[ConfiguredDecoratorHeightmapSpreadDouble, Tag('minecraft:heightmap_spread_double')]
    | Annotated[ConfiguredDecoratorIceberg, Tag('minecraft:iceberg')]
    | Annotated[ConfiguredDecoratorLavaLake, Tag('minecraft:lava_lake')]
    | Annotated[ConfiguredDecoratorNope, Tag('minecraft:nope')]
    | Annotated[ConfiguredDecoratorRange, Tag('minecraft:range')]
    | Annotated[ConfiguredDecoratorSpread32Above, Tag('minecraft:spread_32_above')]
    | Annotated[ConfiguredDecoratorSquare, Tag('minecraft:square')]
    | Annotated[ConfiguredDecoratorWaterDepthThreshold, Tag('minecraft:water_depth_threshold')],
    Discriminator(tag_of('type')),
]
