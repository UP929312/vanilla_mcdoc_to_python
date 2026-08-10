# ~~~ WHAT ARE WE TESTING ~~~

# FlatWeightedList, a type with type `T`, equating to a list with another type with type.

# ~~~ FILE CONTENT ~~~
"""
Generated from symbols.json for ::java::util::FlatWeightedList
Local link to file: generated_symbols/util/FlatWeightedList.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    from generated_symbols.util.FlatWeightedEntry import FlatWeightedEntry


T = TypeVar('T')

type FlatWeightedList[T] = list[FlatWeightedEntry[T]]
