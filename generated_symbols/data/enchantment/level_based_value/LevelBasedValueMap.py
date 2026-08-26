"""
Generated from symbols.json for ::java::data::enchantment::level_based_value::LevelBasedValueMap
Local link to file: generated_symbols/data/enchantment/level_based_value/LevelBasedValueMap.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Literal

from generated_symbols.data.enchantment.level_based_value.ClampedLevelValue import ClampedLevelValue
from generated_symbols.data.enchantment.level_based_value.ExponentLevelValue import ExponentLevelValue
from generated_symbols.data.enchantment.level_based_value.FractionLevelValue import FractionLevelValue
from generated_symbols.data.enchantment.level_based_value.LinearLevelValue import LinearLevelValue
from generated_symbols.data.enchantment.level_based_value.LookupLevelValue import LookupLevelValue
from generated_symbols.data.enchantment.level_based_value.SquaredLevelValue import SquaredLevelValue


@dataclass(kw_only=True)
class LevelBasedValueMapClamped(ClampedLevelValue):
    type: Literal['minecraft:clamped'] = 'minecraft:clamped'


@dataclass(kw_only=True)
class LevelBasedValueMapExponent(ExponentLevelValue):
    type: Literal['minecraft:exponent'] = 'minecraft:exponent'


@dataclass(kw_only=True)
class LevelBasedValueMapFraction(FractionLevelValue):
    type: Literal['minecraft:fraction'] = 'minecraft:fraction'


@dataclass(kw_only=True)
class LevelBasedValueMapLevelsSquared(SquaredLevelValue):
    type: Literal['minecraft:levels_squared'] = 'minecraft:levels_squared'


@dataclass(kw_only=True)
class LevelBasedValueMapLinear(LinearLevelValue):
    type: Literal['minecraft:linear'] = 'minecraft:linear'


@dataclass(kw_only=True)
class LevelBasedValueMapLookup(LookupLevelValue):
    type: Literal['minecraft:lookup'] = 'minecraft:lookup'


type LevelBasedValueMap = LevelBasedValueMapClamped | LevelBasedValueMapExponent | LevelBasedValueMapFraction | LevelBasedValueMapLevelsSquared | LevelBasedValueMapLinear | LevelBasedValueMapLookup


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::level_based_value::LevelBasedValueMap": {
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
                                    "value": "enchantment_level_based_value_type"
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
                    "registry": "minecraft:level_based_value"
                }
            }
        ]
    }
}

