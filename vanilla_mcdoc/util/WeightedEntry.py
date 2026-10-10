"""
Generated from symbols.json for ::java::util::WeightedEntry
Local link to file: vanilla_mcdoc/util/WeightedEntry.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Generic, TypeVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


T = TypeVar('T')


class WeightedEntry(GeneratedModel, Generic[T]):
    weight: Annotated[int, Field(ge=0)]
    data: T
