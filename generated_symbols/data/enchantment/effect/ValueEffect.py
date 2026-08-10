"""
Generated from symbols.json for ::java::data::enchantment::effect::ValueEffect
Local link to file: generated_symbols/data/enchantment/effect/ValueEffect.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.LevelBasedValue import LevelBasedValue


@dataclass(kw_only=True)
class ValueEffectAdd:
    type: Literal['minecraft:add']
    value: LevelBasedValue


@dataclass(kw_only=True)
class ValueEffectAllOf:
    type: Literal['minecraft:all_of']
    effects: Annotated[list[ValueEffect], 'Length = 1 (inclusive) and above']


@dataclass(kw_only=True)
class ValueEffectExponential:
    type: Literal['minecraft:exponential']
    base: LevelBasedValue
    exponent: LevelBasedValue


@dataclass(kw_only=True)
class ValueEffectMultiply:
    type: Literal['minecraft:multiply']
    factor: LevelBasedValue  # Level-Based Value determining the factor to multiply in


@dataclass(kw_only=True)
class ValueEffectRemoveBinomial:
    type: Literal['minecraft:remove_binomial']
    chance: LevelBasedValue  # Chance that an input value is dropped by 1.  The span is 0 to 1, with 0 being no chance to drop an input value and 1 dropping all input values.


@dataclass(kw_only=True)
class ValueEffectSet:
    type: Literal['minecraft:set']
    value: LevelBasedValue


type ValueEffect = ValueEffectAdd | ValueEffectAllOf | ValueEffectExponential | ValueEffectMultiply | ValueEffectRemoveBinomial | ValueEffectSet


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect::ValueEffect": {
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
                                    "value": "enchantment_value_effect_type"
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
                    "registry": "minecraft:value_effect"
                }
            }
        ]
    }
}

