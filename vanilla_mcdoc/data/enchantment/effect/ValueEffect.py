"""
Generated from symbols.json for ::java::data::enchantment::effect::ValueEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect/ValueEffect.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Discriminator, Tag

from vanilla_mcdoc.base import tag_of
from vanilla_mcdoc.data.enchantment.effect.AddEffectValue import AddEffectValue
from vanilla_mcdoc.data.enchantment.effect.AllOfEffectValue import AllOfEffectValue
from vanilla_mcdoc.data.enchantment.effect.ExponentialEffectValue import ExponentialEffectValue
from vanilla_mcdoc.data.enchantment.effect.MultiplyEffectValue import MultiplyEffectValue
from vanilla_mcdoc.data.enchantment.effect.ReduceBinomialEffectValue import ReduceBinomialEffectValue
from vanilla_mcdoc.data.enchantment.effect.SetEffectValue import SetEffectValue


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
    Annotated[ValueEffectAdd, Tag('minecraft:add')]
    | Annotated[ValueEffectAllOf, Tag('minecraft:all_of')]
    | Annotated[ValueEffectExponential, Tag('minecraft:exponential')]
    | Annotated[ValueEffectMultiply, Tag('minecraft:multiply')]
    | Annotated[ValueEffectRemoveBinomial, Tag('minecraft:remove_binomial')]
    | Annotated[ValueEffectSet, Tag('minecraft:set')],
    Discriminator(tag_of('type')),
]
