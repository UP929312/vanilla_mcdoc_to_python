"""
Generated from symbols.json for ::java::util::FilteredText
Local link to file: vanilla_mcdoc/util/FilteredText.py
"""
# ~~~ CODE ~~~
from typing import Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel


T = TypeVar('T')


class FilteredText(GeneratedModel, Generic[T]):
    raw: T
    filtered: T | None = None  # Shown only to players with chat filtering enabled.
