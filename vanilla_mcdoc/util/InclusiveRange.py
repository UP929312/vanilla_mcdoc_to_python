"""
Generated from symbols.json for ::java::util::InclusiveRange
Local link to file: vanilla_mcdoc/util/InclusiveRange.py
"""
# ~~~ CODE ~~~
from typing import Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel


T = TypeVar('T')


class InclusiveRange(GeneratedModel, Generic[T]):
    min_inclusive: T
    max_inclusive: T
