"""
Generated from symbols.json for ::java::data::number_provider::NumberProvider
Local link to file: generated_symbols/data/number_provider/NumberProvider.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.LevelBasedValue import LevelBasedValue
    from generated_symbols.data.number_provider.NumberProviderListRef import NumberProviderListRef
    from generated_symbols.data.number_provider.NumberProviderRef import NumberProviderRef
    from generated_symbols.data.predicate.PredicateRef import PredicateRef
    from generated_symbols.data.util.ScoreProvider import ScoreProvider
    from generated_symbols.data.worldgen.attribute.NumericalEnvironmentAttribute import NumericalEnvironmentAttribute
    from generated_symbols.util.NonEmptyWeightedList import NonEmptyWeightedList


@dataclass(kw_only=True)
class CasesStruct:
    condition: PredicateRef
    number_provider: NumberProviderRef


@dataclass(kw_only=True)
class NumberProviderStructNone:
    type: Annotated[str, IdSpec(registry='loot_number_provider_type')]
    min: NumberProviderRef | None = None
    max: NumberProviderRef | None = None


@dataclass(kw_only=True)
class NumberProviderStructBinomial:
    type: Literal['minecraft:binomial']
    n: NumberProviderRef
    p: NumberProviderRef


@dataclass(kw_only=True)
class NumberProviderStructConditional:
    type: Literal['minecraft:conditional']
    condition: PredicateRef
    on_true: NumberProviderRef
    on_false: NumberProviderRef | None = None  # Defaults to constant 0.


@dataclass(kw_only=True)
class NumberProviderStructConstant:
    type: Literal['minecraft:constant']
    value: float


@dataclass(kw_only=True)
class NumberProviderStructEnchantmentLevel:
    type: Literal['minecraft:enchantment_level']
    amount: LevelBasedValue


@dataclass(kw_only=True)
class NumberProviderStructEnvironmentAttribute:
    type: Literal['minecraft:environment_attribute']
    attribute: NumericalEnvironmentAttribute


@dataclass(kw_only=True)
class NumberProviderStructNumberDispatcher:
    type: Literal['minecraft:number_dispatcher']
    cases: list[CasesStruct]
    default: NumberProviderRef | None = None  # Defaults to constant 0.


@dataclass(kw_only=True)
class NumberProviderStructScore:
    type: Literal['minecraft:score']
    target: ScoreProvider
    score: str
    scale: float | None = None


@dataclass(kw_only=True)
class NumberProviderStructStorage:
    type: Literal['minecraft:storage']
    storage: Annotated[str, IdSpec(registry='storage')]
    path: str


@dataclass(kw_only=True)
class NumberProviderStructSum:
    type: Literal['minecraft:sum']
    summands: NumberProviderListRef


@dataclass(kw_only=True)
class NumberProviderStructUniform:
    type: Literal['minecraft:uniform']
    min: NumberProviderRef | None = None
    max: NumberProviderRef | None = None


@dataclass(kw_only=True)
class NumberProviderStructWeightedList:
    type: Literal['minecraft:weighted_list']
    distribution: NonEmptyWeightedList[NumberProviderRef]


type NumberProviderStruct = NumberProviderStructNone | NumberProviderStructBinomial | NumberProviderStructConditional | NumberProviderStructConstant | NumberProviderStructEnchantmentLevel | NumberProviderStructEnvironmentAttribute | NumberProviderStructNumberDispatcher | NumberProviderStructScore | NumberProviderStructStorage | NumberProviderStructSum | NumberProviderStructUniform | NumberProviderStructWeightedList

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

