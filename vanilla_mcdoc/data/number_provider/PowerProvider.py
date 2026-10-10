"""
Generated from symbols.json for ::java::data::number_provider::PowerProvider
Local link to file: vanilla_mcdoc/data/number_provider/PowerProvider.py
"""
# ~~~ CODE ~~~
from typing import Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel


T = TypeVar('T')


class PowerProvider(GeneratedModel, Generic[T]):
    base: T
    exponent: T
