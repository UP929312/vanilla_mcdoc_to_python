"""
Generated from symbols.json for ::java::data::number_provider::NumberProvider
Local link to file: generated_symbols/data/number_provider/NumberProvider.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import ClassVar, Literal

from generated_symbols.data.number_provider.AggregateNumberProvider import AggregateNumberProvider
from generated_symbols.data.number_provider.BinomialNumberProvider import BinomialNumberProvider
from generated_symbols.data.number_provider.ConditionalNumberProvider import ConditionalNumberProvider
from generated_symbols.data.number_provider.ConstantNumberProvider import ConstantNumberProvider
from generated_symbols.data.number_provider.EnchantmentLevelProvider import EnchantmentLevelProvider
from generated_symbols.data.number_provider.EnvironmentAttributeNumberProvider import EnvironmentAttributeNumberProvider
from generated_symbols.data.number_provider.NumberDispatcher import NumberDispatcher
from generated_symbols.data.number_provider.ScoreNumberProvider import ScoreNumberProvider
from generated_symbols.data.number_provider.StorageNumberProvider import StorageNumberProvider
from generated_symbols.data.number_provider.UniformNumberProvider import UniformNumberProvider
from generated_symbols.data.number_provider.WeightedNumberProvider import WeightedNumberProvider


@dataclass(kw_only=True)
class NumberProviderStructAverage(AggregateNumberProvider):
    __resource_dir__: ClassVar[str] = 'number_provider'

    type: Literal['minecraft:average']


@dataclass(kw_only=True)
class NumberProviderStructBinomial(BinomialNumberProvider):
    type: Literal['minecraft:binomial']


@dataclass(kw_only=True)
class NumberProviderStructConditional(ConditionalNumberProvider):
    type: Literal['minecraft:conditional']


@dataclass(kw_only=True)
class NumberProviderStructConstant(ConstantNumberProvider):
    type: Literal['minecraft:constant']


@dataclass(kw_only=True)
class NumberProviderStructEnchantmentLevel(EnchantmentLevelProvider):
    type: Literal['minecraft:enchantment_level']


@dataclass(kw_only=True)
class NumberProviderStructEnvironmentAttribute(EnvironmentAttributeNumberProvider):
    type: Literal['minecraft:environment_attribute']


@dataclass(kw_only=True)
class NumberProviderStructMaximum(AggregateNumberProvider):
    type: Literal['minecraft:maximum']


@dataclass(kw_only=True)
class NumberProviderStructMinimum(AggregateNumberProvider):
    type: Literal['minecraft:minimum']


@dataclass(kw_only=True)
class NumberProviderStructNumberDispatcher(NumberDispatcher):
    type: Literal['minecraft:number_dispatcher']


@dataclass(kw_only=True)
class NumberProviderStructProduct(AggregateNumberProvider):
    type: Literal['minecraft:product']


@dataclass(kw_only=True)
class NumberProviderStructScore(ScoreNumberProvider):
    type: Literal['minecraft:score']


@dataclass(kw_only=True)
class NumberProviderStructStorage(StorageNumberProvider):
    type: Literal['minecraft:storage']


@dataclass(kw_only=True)
class NumberProviderStructSum(AggregateNumberProvider):
    type: Literal['minecraft:sum']


@dataclass(kw_only=True)
class NumberProviderStructUniform(UniformNumberProvider):
    type: Literal['minecraft:uniform']


@dataclass(kw_only=True)
class NumberProviderStructWeightedList(WeightedNumberProvider):
    type: Literal['minecraft:weighted_list']


type NumberProviderStruct = NumberProviderStructAverage | NumberProviderStructBinomial | NumberProviderStructConditional | NumberProviderStructConstant | NumberProviderStructEnchantmentLevel | NumberProviderStructEnvironmentAttribute | NumberProviderStructMaximum | NumberProviderStructMinimum | NumberProviderStructNumberDispatcher | NumberProviderStructProduct | NumberProviderStructScore | NumberProviderStructStorage | NumberProviderStructSum | NumberProviderStructUniform | NumberProviderStructWeightedList

type NumberProvider = float | NumberProviderStruct


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::NumberProvider": {
        "kind": "union",
        "members": [
            {
                "kind": "float"
            },
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "desc": "Defaults to `minecraft:uniform`.",
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
                                            "value": "loot_number_provider_type"
                                        }
                                    }
                                }
                            ]
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
                            "registry": "minecraft:number_provider"
                        }
                    }
                ],
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ]
            },
            {
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
                                            "value": "loot_number_provider_type"
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
                            "registry": "minecraft:number_provider"
                        }
                    }
                ],
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ]
            }
        ]
    }
}

