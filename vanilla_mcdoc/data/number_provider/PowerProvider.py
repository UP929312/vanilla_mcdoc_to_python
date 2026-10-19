"""
Generated from symbols.json for ::java::data::number_provider::PowerProvider
Local link to file: vanilla_mcdoc/data/number_provider/PowerProvider.py
"""
# ~~~ CODE ~~~
from typing import Any, Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel


T = TypeVar('T', default=Any)


class PowerProvider(GeneratedModel, Generic[T]):
    base: T
    exponent: T
