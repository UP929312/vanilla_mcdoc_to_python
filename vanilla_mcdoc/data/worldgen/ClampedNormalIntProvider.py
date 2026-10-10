"""
Generated from symbols.json for ::java::data::worldgen::ClampedNormalIntProvider
Local link to file: vanilla_mcdoc/data/worldgen/ClampedNormalIntProvider.py
"""
# ~~~ CODE ~~~
from typing import Generic, TypeVar

from vanilla_mcdoc.data.worldgen.UniformIntProvider import UniformIntProvider


T = TypeVar('T')


class ClampedNormalIntProvider(UniformIntProvider[T], Generic[T]):
    mean: float
    deviation: float
