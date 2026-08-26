"""
Generated from symbols.json for ::java::data::util::RandomIntGenerator
Local link to file: generated_symbols/data/util/RandomIntGenerator.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

if TYPE_CHECKING:
    from generated_symbols.data.util.RandomIntGeneratorType import RandomIntGeneratorType


@dataclass(kw_only=True)
class RandomIntGeneratorStructNone:
    type: RandomIntGeneratorType | None = None
    min: int | None = None
    max: int | None = None


@dataclass(kw_only=True)
class RandomIntGeneratorStructBinomial:
    type: Literal['minecraft:binomial'] | None = None
    n: Annotated[int, 'Range | `0` and above | inclusive']
    p: Annotated[float, 'Range | `0`-`1` | both inclusive']


@dataclass(kw_only=True)
class RandomIntGeneratorStructConstant:
    type: Literal['minecraft:constant'] | None = None
    value: int


@dataclass(kw_only=True)
class RandomIntGeneratorStructUniform:
    type: Literal['minecraft:uniform'] | None = None
    min: int | None = None
    max: int | None = None


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

