"""
Generated from symbols.json for ::java::data::number_provider::ConditionalProvider
Local link to file: vanilla_mcdoc/data/number_provider/ConditionalProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.predicate.PredicateRef import PredicateRef


T = TypeVar('T')


class ConditionalProvider(GeneratedModel, Generic[T]):
    condition: PredicateRef
    on_true: T
    on_false: T | None = None  # Defaults to constant 0.
