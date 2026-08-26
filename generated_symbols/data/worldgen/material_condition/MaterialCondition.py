"""
Generated from symbols.json for ::java::data::worldgen::material_condition::MaterialCondition
Local link to file: generated_symbols/data/worldgen/material_condition/MaterialCondition.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import ClassVar, Literal

from generated_symbols.data.worldgen.material_condition.BiomeCondition import BiomeCondition
from generated_symbols.data.worldgen.material_condition.NoiseThresholdCondition import NoiseThresholdCondition
from generated_symbols.data.worldgen.material_condition.NotCondition import NotCondition
from generated_symbols.data.worldgen.material_condition.StoneDepthCondition import StoneDepthCondition
from generated_symbols.data.worldgen.material_condition.VerticalGradientCondition import VerticalGradientCondition
from generated_symbols.data.worldgen.material_condition.WaterCondition import WaterCondition
from generated_symbols.data.worldgen.material_condition.YAboveCondition import YAboveCondition


@dataclass(kw_only=True)
class MaterialConditionBiome(BiomeCondition):
    __resource_dir__: ClassVar[str] = 'worldgen/material_condition'

    type: Literal['minecraft:biome']


@dataclass(kw_only=True)
class MaterialConditionNoiseThreshold(NoiseThresholdCondition):
    type: Literal['minecraft:noise_threshold']


@dataclass(kw_only=True)
class MaterialConditionNot(NotCondition):
    type: Literal['minecraft:not']


@dataclass(kw_only=True)
class MaterialConditionStoneDepth(StoneDepthCondition):
    type: Literal['minecraft:stone_depth']


@dataclass(kw_only=True)
class MaterialConditionVerticalGradient(VerticalGradientCondition):
    type: Literal['minecraft:vertical_gradient']


@dataclass(kw_only=True)
class MaterialConditionWater(WaterCondition):
    type: Literal['minecraft:water']


@dataclass(kw_only=True)
class MaterialConditionYAbove(YAboveCondition):
    type: Literal['minecraft:y_above']


type MaterialCondition = MaterialConditionBiome | MaterialConditionNoiseThreshold | MaterialConditionNot | MaterialConditionStoneDepth | MaterialConditionVerticalGradient | MaterialConditionWater | MaterialConditionYAbove


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::material_condition::MaterialCondition": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "26.3"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "worldgen/material_condition"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "26.3"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "worldgen/material_condition_type"
                                        }
                                    }
                                }
                            ]
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
                    "registry": "minecraft:material_condition"
                }
            }
        ]
    }
}

