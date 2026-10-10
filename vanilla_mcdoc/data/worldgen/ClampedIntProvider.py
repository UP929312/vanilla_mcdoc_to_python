"""
Generated from symbols.json for ::java::data::worldgen::ClampedIntProvider
Local link to file: vanilla_mcdoc/data/worldgen/ClampedIntProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider


T = TypeVar('T')


class ClampedIntProvider(GeneratedModel, Generic[T]):
    min_inclusive: T
    max_inclusive: T
    source: IntProvider[int] | int
