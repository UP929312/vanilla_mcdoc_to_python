"""
Generated from symbols.json for ::java::world::component::predicate::CollectionPredicate
Local link to file: vanilla_mcdoc/world/component/predicate/CollectionPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds


P = TypeVar('P')


class CountStruct(GeneratedModel, Generic[P]):
    test: P  # The contents an entry's text must match exactly.
    count: MinMaxBounds[int] | int  # The number of entries that must match the test.


class CollectionPredicate(GeneratedModel, Generic[P]):
    contains: list[P] | None = None  # A list of tests. For each test, there must be at least one entry whose contents match exactly.
    count: list[CountStruct[P]] | None = None
    size: MinMaxBounds[int] | int | None = None  # When set, total number of entries in the this collection.
