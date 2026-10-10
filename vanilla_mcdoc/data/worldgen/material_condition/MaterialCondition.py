"""
Generated from symbols.json for ::java::data::worldgen::material_condition::MaterialCondition
Local link to file: vanilla_mcdoc/data/worldgen/material_condition/MaterialCondition.py
"""
# ~~~ CODE ~~~
from typing import Annotated, ClassVar, Literal

from pydantic import Field

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


type MaterialCondition = Annotated[
    MaterialConditionBiome | MaterialConditionNoiseThreshold | MaterialConditionNot | MaterialConditionStoneDepth | MaterialConditionVerticalGradient | MaterialConditionWater | MaterialConditionYAbove,
    Field(discriminator='type'),
]
