"""
Generated from symbols.json for ::java::util::WeightedList
Local link to file: vanilla_mcdoc/util/WeightedList.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Any, TypeVar

if TYPE_CHECKING:
    from vanilla_mcdoc.util.WeightedEntry import WeightedEntry


T = TypeVar('T', default=Any)


type WeightedList[T] = list[WeightedEntry[T]]
