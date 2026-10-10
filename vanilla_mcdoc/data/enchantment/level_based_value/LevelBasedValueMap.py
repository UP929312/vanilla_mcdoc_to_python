"""
Generated from symbols.json for ::java::data::enchantment::level_based_value::LevelBasedValueMap
Local link to file: generated_symbols/data/enchantment/level_based_value/LevelBasedValueMap.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from generated_symbols.data.enchantment.level_based_value.ClampedLevelValue import ClampedLevelValue
from generated_symbols.data.enchantment.level_based_value.ExponentLevelValue import ExponentLevelValue
from generated_symbols.data.enchantment.level_based_value.FractionLevelValue import FractionLevelValue
from generated_symbols.data.enchantment.level_based_value.LinearLevelValue import LinearLevelValue
from generated_symbols.data.enchantment.level_based_value.LookupLevelValue import LookupLevelValue
from generated_symbols.data.enchantment.level_based_value.SquaredLevelValue import SquaredLevelValue


class LevelBasedValueMapClamped(ClampedLevelValue):
    type: Literal['minecraft:clamped', 'clamped'] = 'minecraft:clamped'


class LevelBasedValueMapExponent(ExponentLevelValue):
    type: Literal['minecraft:exponent', 'exponent'] = 'minecraft:exponent'


class LevelBasedValueMapFraction(FractionLevelValue):
    type: Literal['minecraft:fraction', 'fraction'] = 'minecraft:fraction'


class LevelBasedValueMapLevelsSquared(SquaredLevelValue):
    type: Literal['minecraft:levels_squared', 'levels_squared'] = 'minecraft:levels_squared'


class LevelBasedValueMapLinear(LinearLevelValue):
    type: Literal['minecraft:linear', 'linear'] = 'minecraft:linear'


class LevelBasedValueMapLookup(LookupLevelValue):
    type: Literal['minecraft:lookup', 'lookup'] = 'minecraft:lookup'


type LevelBasedValueMap = Annotated[
    LevelBasedValueMapClamped | LevelBasedValueMapExponent | LevelBasedValueMapFraction | LevelBasedValueMapLevelsSquared | LevelBasedValueMapLinear | LevelBasedValueMapLookup,
    Field(discriminator='type'),
]


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
