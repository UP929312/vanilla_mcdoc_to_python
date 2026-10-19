"""
Generated from symbols.json for ::java::data::worldgen::material_condition::MaterialCondition
Local link to file: vanilla_mcdoc/data/worldgen/material_condition/MaterialCondition.py
"""
# ~~~ CODE ~~~
from typing import Annotated, ClassVar, Literal

from pydantic import Discriminator, Tag

from vanilla_mcdoc.base import GeneratedModel, tag_of
from vanilla_mcdoc.data.worldgen.material_condition.BiomeCondition import BiomeCondition
from vanilla_mcdoc.data.worldgen.material_condition.NoiseThresholdCondition import NoiseThresholdCondition
from vanilla_mcdoc.data.worldgen.material_condition.NotCondition import NotCondition
from vanilla_mcdoc.data.worldgen.material_condition.StoneDepthCondition import StoneDepthCondition
from vanilla_mcdoc.data.worldgen.material_condition.VerticalGradientCondition import VerticalGradientCondition
from vanilla_mcdoc.data.worldgen.material_condition.WaterCondition import WaterCondition
from vanilla_mcdoc.data.worldgen.material_condition.YAboveCondition import YAboveCondition


class MaterialConditionBiome(BiomeCondition):
    __resource_dir__: ClassVar[str] = 'worldgen/material_condition'

    type: Literal['minecraft:biome', 'biome'] = 'minecraft:biome'


class MaterialConditionNoiseThreshold(NoiseThresholdCondition):
    __resource_dir__: ClassVar[str] = 'worldgen/material_condition'

    type: Literal['minecraft:noise_threshold', 'noise_threshold'] = 'minecraft:noise_threshold'


class MaterialConditionNot(NotCondition):
    __resource_dir__: ClassVar[str] = 'worldgen/material_condition'

    type: Literal['minecraft:not', 'not'] = 'minecraft:not'


class MaterialConditionStoneDepth(StoneDepthCondition):
    __resource_dir__: ClassVar[str] = 'worldgen/material_condition'

    type: Literal['minecraft:stone_depth', 'stone_depth'] = 'minecraft:stone_depth'


class MaterialConditionVerticalGradient(VerticalGradientCondition):
    __resource_dir__: ClassVar[str] = 'worldgen/material_condition'

    type: Literal['minecraft:vertical_gradient', 'vertical_gradient'] = 'minecraft:vertical_gradient'


class MaterialConditionWater(WaterCondition):
    __resource_dir__: ClassVar[str] = 'worldgen/material_condition'

    type: Literal['minecraft:water', 'water'] = 'minecraft:water'


class MaterialConditionYAbove(YAboveCondition):
    __resource_dir__: ClassVar[str] = 'worldgen/material_condition'

    type: Literal['minecraft:y_above', 'y_above'] = 'minecraft:y_above'


class MaterialConditionAbovePreliminarySurface(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/material_condition'

    type: Literal['minecraft:above_preliminary_surface', 'above_preliminary_surface'] = 'minecraft:above_preliminary_surface'


class MaterialConditionHole(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/material_condition'

    type: Literal['minecraft:hole', 'hole'] = 'minecraft:hole'


class MaterialConditionSteep(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/material_condition'

    type: Literal['minecraft:steep', 'steep'] = 'minecraft:steep'


class MaterialConditionTemperature(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/material_condition'

    type: Literal['minecraft:temperature', 'temperature'] = 'minecraft:temperature'


type MaterialCondition = Annotated[
    Annotated[MaterialConditionBiome, Tag('minecraft:biome')]
    | Annotated[MaterialConditionNoiseThreshold, Tag('minecraft:noise_threshold')]
    | Annotated[MaterialConditionNot, Tag('minecraft:not')]
    | Annotated[MaterialConditionStoneDepth, Tag('minecraft:stone_depth')]
    | Annotated[MaterialConditionVerticalGradient, Tag('minecraft:vertical_gradient')]
    | Annotated[MaterialConditionWater, Tag('minecraft:water')]
    | Annotated[MaterialConditionYAbove, Tag('minecraft:y_above')]
    | Annotated[MaterialConditionAbovePreliminarySurface, Tag('minecraft:above_preliminary_surface')]
    | Annotated[MaterialConditionHole, Tag('minecraft:hole')]
    | Annotated[MaterialConditionSteep, Tag('minecraft:steep')]
    | Annotated[MaterialConditionTemperature, Tag('minecraft:temperature')],
    Discriminator(tag_of('type')),
]
