"""
Generated from symbols.json for ::java::util::WeightedList
Local link to file: vanilla_mcdoc/util/WeightedList.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    from vanilla_mcdoc.util.WeightedEntry import WeightedEntry


T = TypeVar('T')


type WeightedList[T] = list[WeightedEntry[T]]
