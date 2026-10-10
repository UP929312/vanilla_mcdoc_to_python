"""
Generated from symbols.json for ::java::data::tag::ExplicitTagEntry
Local link to file: vanilla_mcdoc/data/tag/ExplicitTagEntry.py
"""
# ~~~ CODE ~~~
from typing import Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel


E = TypeVar('E')


class ExplicitTagEntry(GeneratedModel, Generic[E]):
    id: E
    required: bool | None = None
