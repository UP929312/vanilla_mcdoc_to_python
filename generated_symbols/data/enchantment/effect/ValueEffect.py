"""
Generated from symbols.json for ::java::data::enchantment::effect::ValueEffect
Local link to file: generated_symbols/data/enchantment/effect/ValueEffect.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from generated_symbols.data.enchantment.effect.AddEffectValue import AddEffectValue
from generated_symbols.data.enchantment.effect.AllOfEffectValue import AllOfEffectValue
from generated_symbols.data.enchantment.effect.ExponentialEffectValue import ExponentialEffectValue
from generated_symbols.data.enchantment.effect.MultiplyEffectValue import MultiplyEffectValue
from generated_symbols.data.enchantment.effect.ReduceBinomialEffectValue import ReduceBinomialEffectValue
from generated_symbols.data.enchantment.effect.SetEffectValue import SetEffectValue


class ValueEffectAdd(AddEffectValue):
    type: Literal['minecraft:add', 'add'] = 'minecraft:add'


class ValueEffectAllOf(AllOfEffectValue):
    type: Literal['minecraft:all_of', 'all_of'] = 'minecraft:all_of'


class ValueEffectExponential(ExponentialEffectValue):
    type: Literal['minecraft:exponential', 'exponential'] = 'minecraft:exponential'


class ValueEffectMultiply(MultiplyEffectValue):
    type: Literal['minecraft:multiply', 'multiply'] = 'minecraft:multiply'


class ValueEffectRemoveBinomial(ReduceBinomialEffectValue):
    type: Literal['minecraft:remove_binomial', 'remove_binomial'] = 'minecraft:remove_binomial'


class ValueEffectSet(SetEffectValue):
    type: Literal['minecraft:set', 'set'] = 'minecraft:set'


type ValueEffect = Annotated[
    ValueEffectAdd | ValueEffectAllOf | ValueEffectExponential | ValueEffectMultiply | ValueEffectRemoveBinomial | ValueEffectSet,
    Field(discriminator='type'),
]


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

