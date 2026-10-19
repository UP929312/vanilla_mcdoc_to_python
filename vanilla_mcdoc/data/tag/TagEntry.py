"""
Generated from symbols.json for ::java::data::tag::TagEntry
Local link to file: vanilla_mcdoc/data/tag/TagEntry.py
"""
# ~~~ CODE ~~~
from typing import Any, Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel


E = TypeVar('E', default=Any)


class TagEntry(GeneratedModel, Generic[E]):
    id: E
    required: bool | None = None
