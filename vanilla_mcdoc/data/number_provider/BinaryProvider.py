"""
Generated from symbols.json for ::java::data::number_provider::BinaryProvider
Local link to file: vanilla_mcdoc/data/number_provider/BinaryProvider.py
"""
# ~~~ CODE ~~~
from typing import Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel


T = TypeVar('T')


class BinaryProvider(GeneratedModel, Generic[T]):
    left: T
    right: T
