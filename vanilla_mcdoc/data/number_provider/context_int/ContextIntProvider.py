"""
Generated from symbols.json for ::java::data::number_provider::context_int::ContextIntProvider
Local link to file: generated_symbols/data/number_provider/context_int/ContextIntProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar, Literal

from generated_symbols.base import GeneratedModel
from generated_symbols.data.number_provider.context_int.AggregateProvider import AggregateProvider
from generated_symbols.data.number_provider.context_int.BinaryProvider import BinaryProvider
from generated_symbols.data.number_provider.context_int.BinomialDistributionGenerator import BinomialDistributionGenerator
from generated_symbols.data.number_provider.context_int.ScoreboardValue import ScoreboardValue
from generated_symbols.data.number_provider.context_int.SingleProvider import SingleProvider
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.context_float.FloatRef import FloatRef
    from generated_symbols.data.number_provider.context_int.IntRef import IntRef
    from generated_symbols.data.predicate.PredicateRef import PredicateRef
    from generated_symbols.data.worldgen.attribute.IntegerEnvironmentAttribute import IntegerEnvironmentAttribute
    from generated_symbols.util.NonEmptyWeightedList import NonEmptyWeightedList


class CasesStruct(GeneratedModel):
    condition: PredicateRef
    value: IntRef


class ContextIntProviderStructNone(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'context_int_provider'

    type: Annotated[str, IdSpec(registry='context_int_provider_type')]


class ContextIntProviderStructAbs(SingleProvider):
    __resource_dir__: ClassVar[str] = 'context_int_provider'

    type: Literal['minecraft:abs', 'abs'] = 'minecraft:abs'


class ContextIntProviderStructAdd(AggregateProvider):
    __resource_dir__: ClassVar[str] = 'context_int_provider'

    type: Literal['minecraft:add', 'add'] = 'minecraft:add'


class ContextIntProviderStructAvg(AggregateProvider):
    __resource_dir__: ClassVar[str] = 'context_int_provider'

    type: Literal['minecraft:avg', 'avg'] = 'minecraft:avg'


class ContextIntProviderStructBinomial(BinomialDistributionGenerator):
    __resource_dir__: ClassVar[str] = 'context_int_provider'

    type: Literal['minecraft:binomial', 'binomial'] = 'minecraft:binomial'


class ContextIntProviderStructConditional(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'context_int_provider'

    type: Literal['minecraft:conditional', 'conditional'] = 'minecraft:conditional'
    condition: PredicateRef
    on_true: IntRef
    on_false: IntRef | None = None  # Defaults to constant 0.


class ContextIntProviderStructConstant(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'context_int_provider'

    type: Literal['minecraft:constant', 'constant'] = 'minecraft:constant'
    value: int


class ContextIntProviderStructDiv(BinaryProvider):
    __resource_dir__: ClassVar[str] = 'context_int_provider'

    type: Literal['minecraft:div', 'div'] = 'minecraft:div'


class ContextIntProviderStructEnvironmentAttribute(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'context_int_provider'

    type: Literal['minecraft:environment_attribute', 'environment_attribute'] = 'minecraft:environment_attribute'
    attribute: IntegerEnvironmentAttribute


class ContextIntProviderStructFloorDiv(BinaryProvider):
    __resource_dir__: ClassVar[str] = 'context_int_provider'

    type: Literal['minecraft:floor_div', 'floor_div'] = 'minecraft:floor_div'


class ContextIntProviderStructFloorMod(BinaryProvider):
    __resource_dir__: ClassVar[str] = 'context_int_provider'

    type: Literal['minecraft:floor_mod', 'floor_mod'] = 'minecraft:floor_mod'


class ContextIntProviderStructFromFloat(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'context_int_provider'

    type: Literal['minecraft:from_float', 'from_float'] = 'minecraft:from_float'
    input: FloatRef


class ContextIntProviderStructMax(AggregateProvider):
    __resource_dir__: ClassVar[str] = 'context_int_provider'

    type: Literal['minecraft:max', 'max'] = 'minecraft:max'


class ContextIntProviderStructMin(AggregateProvider):
    __resource_dir__: ClassVar[str] = 'context_int_provider'

    type: Literal['minecraft:min', 'min'] = 'minecraft:min'


class ContextIntProviderStructMod(BinaryProvider):
    __resource_dir__: ClassVar[str] = 'context_int_provider'

    type: Literal['minecraft:mod', 'mod'] = 'minecraft:mod'


class ContextIntProviderStructMul(AggregateProvider):
    __resource_dir__: ClassVar[str] = 'context_int_provider'

    type: Literal['minecraft:mul', 'mul'] = 'minecraft:mul'


class ContextIntProviderStructNegate(SingleProvider):
    __resource_dir__: ClassVar[str] = 'context_int_provider'

    type: Literal['minecraft:negate', 'negate'] = 'minecraft:negate'


class ContextIntProviderStructNumberDispatcher(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'context_int_provider'

    type: Literal['minecraft:number_dispatcher', 'number_dispatcher'] = 'minecraft:number_dispatcher'
    cases: list[CasesStruct]  # Each condition is tested in order, the first in the list that passes is used.
    default: IntRef | None = None  # Defaults to constant 0.


class ContextIntProviderStructPow(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'context_int_provider'

    type: Literal['minecraft:pow', 'pow'] = 'minecraft:pow'
    base: IntRef
    exponent: IntRef


class ContextIntProviderStructScore(ScoreboardValue):
    __resource_dir__: ClassVar[str] = 'context_int_provider'

    type: Literal['minecraft:score', 'score'] = 'minecraft:score'


class ContextIntProviderStructStorage(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'context_int_provider'

    type: Literal['minecraft:storage', 'storage'] = 'minecraft:storage'
    storage: Annotated[str, IdSpec(registry='storage')]
    path: str
    fallback: IntRef | None = None  # Defaults to constant 0.


class ContextIntProviderStructSub(BinaryProvider):
    __resource_dir__: ClassVar[str] = 'context_int_provider'

    type: Literal['minecraft:sub', 'sub'] = 'minecraft:sub'


class ContextIntProviderStructUniform(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'context_int_provider'

    type: Literal['minecraft:uniform', 'uniform'] = 'minecraft:uniform'
    min: IntRef
    max: IntRef


class ContextIntProviderStructWeightedList(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'context_int_provider'

    type: Literal['minecraft:weighted_list', 'weighted_list'] = 'minecraft:weighted_list'
    distribution: NonEmptyWeightedList[IntRef]


type ContextIntProviderStruct = ContextIntProviderStructNone | ContextIntProviderStructAbs | ContextIntProviderStructAdd | ContextIntProviderStructAvg | ContextIntProviderStructBinomial | ContextIntProviderStructConditional | ContextIntProviderStructConstant | ContextIntProviderStructDiv | ContextIntProviderStructEnvironmentAttribute | ContextIntProviderStructFloorDiv | ContextIntProviderStructFloorMod | ContextIntProviderStructFromFloat | ContextIntProviderStructMax | ContextIntProviderStructMin | ContextIntProviderStructMod | ContextIntProviderStructMul | ContextIntProviderStructNegate | ContextIntProviderStructNumberDispatcher | ContextIntProviderStructPow | ContextIntProviderStructScore | ContextIntProviderStructStorage | ContextIntProviderStructSub | ContextIntProviderStructUniform | ContextIntProviderStructWeightedList


type ContextIntProvider = int | ContextIntProviderStruct


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::context_int::ContextIntProvider": {
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
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "context_int_provider_type"
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
                            "registry": "minecraft:context_int_provider"
                        }
                    }
                ]
            }
        ]
    }
}
