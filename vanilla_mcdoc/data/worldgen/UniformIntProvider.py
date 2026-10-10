"""
Generated from symbols.json for ::java::data::worldgen::UniformIntProvider
Local link to file: vanilla_mcdoc/data/worldgen/UniformIntProvider.py
"""
# ~~~ CODE ~~~
from typing import Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel


T = TypeVar('T')


class UniformIntProvider(GeneratedModel, Generic[T]):
    min_inclusive: T
    max_inclusive: T
