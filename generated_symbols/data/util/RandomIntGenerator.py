"""
Generated from symbols.json for ::java::data::util::RandomIntGenerator
Local link to file: generated_symbols/data/util/RandomIntGenerator.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from generated_symbols.data.util.BinomialIntGenerator import BinomialIntGenerator
from generated_symbols.data.util.ConstantIntGenerator import ConstantIntGenerator
from generated_symbols.data.util.UniformIntGenerator import UniformIntGenerator

if TYPE_CHECKING:
    from generated_symbols.data.util.RandomIntGeneratorType import RandomIntGeneratorType


@dataclass(kw_only=True)
class RandomIntGeneratorStructNone(UniformIntGenerator):
    type: RandomIntGeneratorType | None = None


@dataclass(kw_only=True)
class RandomIntGeneratorStructBinomial(BinomialIntGenerator):
    type: Literal['minecraft:binomial'] = 'minecraft:binomial'


@dataclass(kw_only=True)
class RandomIntGeneratorStructConstant(ConstantIntGenerator):
    type: Literal['minecraft:constant'] = 'minecraft:constant'


@dataclass(kw_only=True)
class RandomIntGeneratorStructUniform(UniformIntGenerator):
    type: Literal['minecraft:uniform'] = 'minecraft:uniform'


type RandomIntGeneratorStruct = RandomIntGeneratorStructNone | RandomIntGeneratorStructBinomial | RandomIntGeneratorStructConstant | RandomIntGeneratorStructUniform

type RandomIntGenerator = int | RandomIntGeneratorStruct


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::util::RandomIntGenerator": {
        "kind": "union",
        "members": [
            {
                "kind": "int"
            },
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "key": "type",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::util::RandomIntGeneratorType"
                        },
                        "optional": True
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
                            "registry": "minecraft:random_int_generator"
                        }
                    }
                ]
            }
        ]
    }
}

