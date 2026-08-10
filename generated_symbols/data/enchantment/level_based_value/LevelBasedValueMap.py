"""
Generated from symbols.json for ::java::data::enchantment::level_based_value::LevelBasedValueMap
Local link to file: generated_symbols/data/enchantment/level_based_value/LevelBasedValueMap.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.level_based_value.LevelBasedValue import LevelBasedValue


@dataclass(kw_only=True)
class LevelBasedValueMapClamped:
    type: Literal['minecraft:clamped']
    value: LevelBasedValue
    min: float
    max: float


@dataclass(kw_only=True)
class LevelBasedValueMapExponent:
    type: Literal['minecraft:exponent']
    base: LevelBasedValue
    power: LevelBasedValue


@dataclass(kw_only=True)
class LevelBasedValueMapFraction:
    type: Literal['minecraft:fraction']
    numerator: LevelBasedValue
    denominator: LevelBasedValue


@dataclass(kw_only=True)
class LevelBasedValueMapLevelsSquared:
    type: Literal['minecraft:levels_squared']
    added: float  # Added to the result so that the result becomes `square(level) + added`.


@dataclass(kw_only=True)
class LevelBasedValueMapLinear:
    type: Literal['minecraft:linear']
    base: float  # Base value at level 1.
    per_level_above_first: float  # Value increase per level above 1.


@dataclass(kw_only=True)
class LevelBasedValueMapLookup:
    type: Literal['minecraft:lookup']
    values: Annotated[list[LevelBasedValue], 'Length = 1 (inclusive) and above']  # Indexed by `level - 1` to apply, if present
    fallback: LevelBasedValue  # Applied if the level is greater than the size of `values`.


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

