"""
Generated from symbols.json for ::java::data::worldgen::ConstantIntProvider
Local link to file: vanilla_mcdoc/data/worldgen/ConstantIntProvider.py
"""
# ~~~ CODE ~~~
from typing import Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel


T = TypeVar('T')


class ConstantIntProvider(GeneratedModel, Generic[T]):
    value: T
