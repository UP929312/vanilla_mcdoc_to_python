"""
Generated from symbols.json for ::java::data::enchantment::effect::ValueEffect
Local link to file: generated_symbols/data/enchantment/effect/ValueEffect.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Literal

from generated_symbols.data.enchantment.effect.AddEffectValue import AddEffectValue
from generated_symbols.data.enchantment.effect.AllOfEffectValue import AllOfEffectValue
from generated_symbols.data.enchantment.effect.ExponentialEffectValue import ExponentialEffectValue
from generated_symbols.data.enchantment.effect.MultiplyEffectValue import MultiplyEffectValue
from generated_symbols.data.enchantment.effect.ReduceBinomialEffectValue import ReduceBinomialEffectValue
from generated_symbols.data.enchantment.effect.SetEffectValue import SetEffectValue


@dataclass(kw_only=True)
class ValueEffectAdd(AddEffectValue):
    type: Literal['minecraft:add'] = 'minecraft:add'


@dataclass(kw_only=True)
class ValueEffectAllOf(AllOfEffectValue):
    type: Literal['minecraft:all_of'] = 'minecraft:all_of'


@dataclass(kw_only=True)
class ValueEffectExponential(ExponentialEffectValue):
    type: Literal['minecraft:exponential'] = 'minecraft:exponential'


@dataclass(kw_only=True)
class ValueEffectMultiply(MultiplyEffectValue):
    type: Literal['minecraft:multiply'] = 'minecraft:multiply'


@dataclass(kw_only=True)
class ValueEffectRemoveBinomial(ReduceBinomialEffectValue):
    type: Literal['minecraft:remove_binomial'] = 'minecraft:remove_binomial'


@dataclass(kw_only=True)
class ValueEffectSet(SetEffectValue):
    type: Literal['minecraft:set'] = 'minecraft:set'


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

