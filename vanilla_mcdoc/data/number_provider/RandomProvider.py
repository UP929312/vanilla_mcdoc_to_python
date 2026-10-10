"""
Generated from symbols.json for ::java::data::number_provider::RandomProvider
Local link to file: vanilla_mcdoc/data/number_provider/RandomProvider.py
"""
# ~~~ CODE ~~~
from typing import Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel


T = TypeVar('T')


class RandomProvider(GeneratedModel, Generic[T]):
    min: T
    max: T
