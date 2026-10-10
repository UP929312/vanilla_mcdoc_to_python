"""
Generated from symbols.json for ::java::util::NonEmptyFlatWeightedList
Local link to file: vanilla_mcdoc/util/NonEmptyFlatWeightedList.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, TypeVar

from pydantic import Field

if TYPE_CHECKING:
    from vanilla_mcdoc.util.FlatWeightedEntry import FlatWeightedEntry


T = TypeVar('T')


type NonEmptyFlatWeightedList[T] = Annotated[list[FlatWeightedEntry[T]], Field(min_length=1)]
