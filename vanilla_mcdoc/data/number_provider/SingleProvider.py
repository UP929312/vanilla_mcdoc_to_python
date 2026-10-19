"""
Generated from symbols.json for ::java::data::number_provider::SingleProvider
Local link to file: vanilla_mcdoc/data/number_provider/SingleProvider.py
"""
# ~~~ CODE ~~~
from typing import Any, Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel


T = TypeVar('T', default=Any)


class SingleProvider(GeneratedModel, Generic[T]):
    input: T
