"""
Generated from symbols.json for ::java::data::util::MinMaxBounds
Local link to file: vanilla_mcdoc/data/util/MinMaxBounds.py
"""
# ~~~ CODE ~~~
from typing import Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel


T = TypeVar('T')


class MinMaxBounds(GeneratedModel, Generic[T]):
    min: T | None = None
    max: T | None = None
