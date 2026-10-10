"""
Generated from symbols.json for ::java::data::util::RandomIntGenerator
Local link to file: vanilla_mcdoc/data/util/RandomIntGenerator.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Literal

from vanilla_mcdoc.data.util.BinomialIntGenerator import BinomialIntGenerator
from vanilla_mcdoc.data.util.ConstantIntGenerator import ConstantIntGenerator
from vanilla_mcdoc.data.util.UniformIntGenerator import UniformIntGenerator

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.RandomIntGeneratorType import RandomIntGeneratorType


class RandomIntGeneratorStructDefault(UniformIntGenerator):
    type: RandomIntGeneratorType | None = None


class RandomIntGeneratorStructBinomial(BinomialIntGenerator):
    type: Literal['minecraft:binomial', 'binomial'] | None = 'minecraft:binomial'


class RandomIntGeneratorStructConstant(ConstantIntGenerator):
    type: Literal['minecraft:constant', 'constant'] | None = 'minecraft:constant'


class RandomIntGeneratorStructUniform(UniformIntGenerator):
    type: Literal['minecraft:uniform', 'uniform'] | None = 'minecraft:uniform'


type RandomIntGeneratorStruct = RandomIntGeneratorStructDefault | RandomIntGeneratorStructBinomial | RandomIntGeneratorStructConstant | RandomIntGeneratorStructUniform


type RandomIntGenerator = int | RandomIntGeneratorStruct
