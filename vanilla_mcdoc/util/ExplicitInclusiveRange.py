"""
Generated from symbols.json for ::java::util::ExplicitInclusiveRange
Local link to file: vanilla_mcdoc/util/ExplicitInclusiveRange.py
"""
# ~~~ CODE ~~~
from typing import Any, Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel


T = TypeVar('T', default=Any)


class ExplicitInclusiveRange(GeneratedModel, Generic[T]):
    min_inclusive: T
    max_inclusive: T
