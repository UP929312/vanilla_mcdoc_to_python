"""
Generated from symbols.json for ::java::util::FlatWeightedEntry
Local link to file: vanilla_mcdoc/util/FlatWeightedEntry.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Generic, TypeVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


T = TypeVar('T')


class FlatWeightedEntry(GeneratedModel, Generic[T]):
    weight: Annotated[int, Field(ge=0)]
