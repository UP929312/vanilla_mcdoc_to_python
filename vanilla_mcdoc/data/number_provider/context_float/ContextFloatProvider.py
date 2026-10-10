"""
Generated from symbols.json for ::java::data::number_provider::context_float::ContextFloatProvider
Local link to file: vanilla_mcdoc/data/number_provider/context_float/ContextFloatProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar, Literal

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.data.number_provider.context_float.AggregateProvider import AggregateProvider
from vanilla_mcdoc.data.number_provider.context_float.BinaryProvider import BinaryProvider
from vanilla_mcdoc.data.number_provider.context_float.EnchantmentLevelProvider import EnchantmentLevelProvider
from vanilla_mcdoc.data.number_provider.context_float.SingleProvider import SingleProvider
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.number_provider.context_float.FloatRef import FloatRef
    from vanilla_mcdoc.data.number_provider.context_int.IntRef import IntRef
    from vanilla_mcdoc.data.predicate.PredicateRef import PredicateRef
    from vanilla_mcdoc.data.worldgen.attribute.NumericalEnvironmentAttribute import NumericalEnvironmentAttribute
    from vanilla_mcdoc.util.NonEmptyWeightedList import NonEmptyWeightedList


class CasesStruct(GeneratedModel):
    condition: PredicateRef
    value: FloatRef


class ContextFloatProviderStructDefault(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'context_float_provider'

    type: Annotated[str, IdSpec(registry='context_float_provider_type')]


class ContextFloatProviderStructAbs(SingleProvider):
    __resource_dir__: ClassVar[str] = 'context_float_provider'

    type: Literal['minecraft:abs', 'abs'] = 'minecraft:abs'


class ContextFloatProviderStructAdd(AggregateProvider):
    __resource_dir__: ClassVar[str] = 'context_float_provider'

    type: Literal['minecraft:add', 'add'] = 'minecraft:add'


class ContextFloatProviderStructAvg(AggregateProvider):
    __resource_dir__: ClassVar[str] = 'context_float_provider'

    type: Literal['minecraft:avg', 'avg'] = 'minecraft:avg'


class ContextFloatProviderStructCeil(SingleProvider):
    __resource_dir__: ClassVar[str] = 'context_float_provider'

    type: Literal['minecraft:ceil', 'ceil'] = 'minecraft:ceil'


class ContextFloatProviderStructConditional(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'context_float_provider'

    type: Literal['minecraft:conditional', 'conditional'] = 'minecraft:conditional'
    condition: PredicateRef
    on_true: FloatRef
    on_false: FloatRef | None = None  # Defaults to constant 0.


class ContextFloatProviderStructConstant(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'context_float_provider'

    type: Literal['minecraft:constant', 'constant'] = 'minecraft:constant'
    value: float


class ContextFloatProviderStructCos(SingleProvider):
    __resource_dir__: ClassVar[str] = 'context_float_provider'

    type: Literal['minecraft:cos', 'cos'] = 'minecraft:cos'


class ContextFloatProviderStructDiv(BinaryProvider):
    __resource_dir__: ClassVar[str] = 'context_float_provider'

    type: Literal['minecraft:div', 'div'] = 'minecraft:div'


class ContextFloatProviderStructEnchantmentLevel(EnchantmentLevelProvider):
    __resource_dir__: ClassVar[str] = 'context_float_provider'

    type: Literal['minecraft:enchantment_level', 'enchantment_level'] = 'minecraft:enchantment_level'


class ContextFloatProviderStructEnvironmentAttribute(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'context_float_provider'

    type: Literal['minecraft:environment_attribute', 'environment_attribute'] = 'minecraft:environment_attribute'
    attribute: NumericalEnvironmentAttribute


class ContextFloatProviderStructFloor(SingleProvider):
    __resource_dir__: ClassVar[str] = 'context_float_provider'

    type: Literal['minecraft:floor', 'floor'] = 'minecraft:floor'


class ContextFloatProviderStructFromInt(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'context_float_provider'

    type: Literal['minecraft:from_int', 'from_int'] = 'minecraft:from_int'
    input: IntRef


class ContextFloatProviderStructLength(AggregateProvider):
    __resource_dir__: ClassVar[str] = 'context_float_provider'

    type: Literal['minecraft:length', 'length'] = 'minecraft:length'


class ContextFloatProviderStructMax(AggregateProvider):
    __resource_dir__: ClassVar[str] = 'context_float_provider'

    type: Literal['minecraft:max', 'max'] = 'minecraft:max'


class ContextFloatProviderStructMin(AggregateProvider):
    __resource_dir__: ClassVar[str] = 'context_float_provider'

    type: Literal['minecraft:min', 'min'] = 'minecraft:min'


class ContextFloatProviderStructMod(BinaryProvider):
    __resource_dir__: ClassVar[str] = 'context_float_provider'

    type: Literal['minecraft:mod', 'mod'] = 'minecraft:mod'


class ContextFloatProviderStructMul(AggregateProvider):
    __resource_dir__: ClassVar[str] = 'context_float_provider'

    type: Literal['minecraft:mul', 'mul'] = 'minecraft:mul'


class ContextFloatProviderStructNegate(SingleProvider):
    __resource_dir__: ClassVar[str] = 'context_float_provider'

    type: Literal['minecraft:negate', 'negate'] = 'minecraft:negate'


class ContextFloatProviderStructNumberDispatcher(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'context_float_provider'

    type: Literal['minecraft:number_dispatcher', 'number_dispatcher'] = 'minecraft:number_dispatcher'
    cases: list[CasesStruct]  # Each condition is tested in order, the first in the list that passes is used.
    default: FloatRef | None = None  # Defaults to constant 0.


class ContextFloatProviderStructPow(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'context_float_provider'

    type: Literal['minecraft:pow', 'pow'] = 'minecraft:pow'
    base: FloatRef
    exponent: FloatRef


class ContextFloatProviderStructRound(SingleProvider):
    __resource_dir__: ClassVar[str] = 'context_float_provider'

    type: Literal['minecraft:round', 'round'] = 'minecraft:round'


class ContextFloatProviderStructSin(SingleProvider):
    __resource_dir__: ClassVar[str] = 'context_float_provider'

    type: Literal['minecraft:sin', 'sin'] = 'minecraft:sin'


class ContextFloatProviderStructSqrt(SingleProvider):
    __resource_dir__: ClassVar[str] = 'context_float_provider'

    type: Literal['minecraft:sqrt', 'sqrt'] = 'minecraft:sqrt'


class ContextFloatProviderStructStorage(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'context_float_provider'

    type: Literal['minecraft:storage', 'storage'] = 'minecraft:storage'
    storage: Annotated[str, IdSpec(registry='storage')]
    path: str
    fallback: FloatRef | None = None  # Defaults to constant 0.


class ContextFloatProviderStructSub(BinaryProvider):
    __resource_dir__: ClassVar[str] = 'context_float_provider'

    type: Literal['minecraft:sub', 'sub'] = 'minecraft:sub'


class ContextFloatProviderStructTruncate(SingleProvider):
    __resource_dir__: ClassVar[str] = 'context_float_provider'

    type: Literal['minecraft:truncate', 'truncate'] = 'minecraft:truncate'


class ContextFloatProviderStructUniform(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'context_float_provider'

    type: Literal['minecraft:uniform', 'uniform'] = 'minecraft:uniform'
    min: FloatRef
    max: FloatRef


class ContextFloatProviderStructWeightedList(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'context_float_provider'

    type: Literal['minecraft:weighted_list', 'weighted_list'] = 'minecraft:weighted_list'
    distribution: NonEmptyWeightedList[FloatRef]


type ContextFloatProviderStruct = ContextFloatProviderStructDefault | ContextFloatProviderStructAbs | ContextFloatProviderStructAdd | ContextFloatProviderStructAvg | ContextFloatProviderStructCeil | ContextFloatProviderStructConditional | ContextFloatProviderStructConstant | ContextFloatProviderStructCos | ContextFloatProviderStructDiv | ContextFloatProviderStructEnchantmentLevel | ContextFloatProviderStructEnvironmentAttribute | ContextFloatProviderStructFloor | ContextFloatProviderStructFromInt | ContextFloatProviderStructLength | ContextFloatProviderStructMax | ContextFloatProviderStructMin | ContextFloatProviderStructMod | ContextFloatProviderStructMul | ContextFloatProviderStructNegate | ContextFloatProviderStructNumberDispatcher | ContextFloatProviderStructPow | ContextFloatProviderStructRound | ContextFloatProviderStructSin | ContextFloatProviderStructSqrt | ContextFloatProviderStructStorage | ContextFloatProviderStructSub | ContextFloatProviderStructTruncate | ContextFloatProviderStructUniform | ContextFloatProviderStructWeightedList


type ContextFloatProvider = float | ContextFloatProviderStruct
