"""
Generated from symbols.json for ::java::world::component::predicate::CollectionCountPredicate
Local link to file: vanilla_mcdoc/world/component/predicate/CollectionCountPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds


P = TypeVar('P')


class CollectionCountPredicate(GeneratedModel, Generic[P]):
    test: P  # The contents an entry's text must match exactly.
    count: MinMaxBounds[int] | int  # The number of entries that must match the test.
