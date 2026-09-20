"""
Generated from symbols.json for ::java::data::number_provider::NumberProvider
Local link to file: generated_symbols/data/number_provider/NumberProvider.py
"""
# ~~~ CODE ~~~
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


class NumberProviderStructAverage(AggregateNumberProvider):
    __resource_dir__: ClassVar[str] = 'number_provider'

    type: Literal['minecraft:average'] = 'minecraft:average'


class NumberProviderStructBinomial(BinomialNumberProvider):
    type: Literal['minecraft:binomial'] = 'minecraft:binomial'


class NumberProviderStructConditional(ConditionalNumberProvider):
    type: Literal['minecraft:conditional'] = 'minecraft:conditional'


class NumberProviderStructConstant(ConstantNumberProvider):
    type: Literal['minecraft:constant'] = 'minecraft:constant'


class NumberProviderStructEnchantmentLevel(EnchantmentLevelProvider):
    type: Literal['minecraft:enchantment_level'] = 'minecraft:enchantment_level'


class NumberProviderStructEnvironmentAttribute(EnvironmentAttributeNumberProvider):
    type: Literal['minecraft:environment_attribute'] = 'minecraft:environment_attribute'


class NumberProviderStructMaximum(AggregateNumberProvider):
    type: Literal['minecraft:maximum'] = 'minecraft:maximum'


class NumberProviderStructMinimum(AggregateNumberProvider):
    type: Literal['minecraft:minimum'] = 'minecraft:minimum'


class NumberProviderStructNumberDispatcher(NumberDispatcher):
    type: Literal['minecraft:number_dispatcher'] = 'minecraft:number_dispatcher'


class NumberProviderStructProduct(AggregateNumberProvider):
    type: Literal['minecraft:product'] = 'minecraft:product'


class NumberProviderStructScore(ScoreNumberProvider):
    type: Literal['minecraft:score'] = 'minecraft:score'


class NumberProviderStructStorage(StorageNumberProvider):
    type: Literal['minecraft:storage'] = 'minecraft:storage'


class NumberProviderStructSum(AggregateNumberProvider):
    type: Literal['minecraft:sum'] = 'minecraft:sum'


class NumberProviderStructUniform(UniformNumberProvider):
    type: Literal['minecraft:uniform'] = 'minecraft:uniform'


class NumberProviderStructWeightedList(WeightedNumberProvider):
    type: Literal['minecraft:weighted_list'] = 'minecraft:weighted_list'


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

