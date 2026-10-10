"""
Generated from symbols.json for ::java::data::tag::Tag
Local link to file: vanilla_mcdoc/data/tag/Tag.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.tag.TagEntry import TagEntry


E = TypeVar('E')


class Tag(GeneratedModel, Generic[E]):
    replace: bool | None = None
    values: list[TagEntry[E]]
