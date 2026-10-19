"""
Generated from symbols.json for ::java::data::worldgen::UniformIntProvider
Local link to file: vanilla_mcdoc/data/worldgen/UniformIntProvider.py
"""
# ~~~ CODE ~~~
from typing import Any, Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel


T = TypeVar('T', default=Any)


class UniformIntProvider(GeneratedModel, Generic[T]):
    min_inclusive: T
    max_inclusive: T
