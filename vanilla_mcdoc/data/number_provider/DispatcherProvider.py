"""
Generated from symbols.json for ::java::data::number_provider::DispatcherProvider
Local link to file: vanilla_mcdoc/data/number_provider/DispatcherProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.predicate.PredicateRef import PredicateRef


T = TypeVar('T')


class CasesStruct(GeneratedModel, Generic[T]):
    condition: PredicateRef
    value: T


class DispatcherProvider(GeneratedModel, Generic[T]):
    cases: list[CasesStruct[T]]  # Each condition is tested in order, the first in the list that passes is used.
    default: T | None = None  # Defaults to constant 0.
