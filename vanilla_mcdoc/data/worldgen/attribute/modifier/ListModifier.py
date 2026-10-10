"""
Generated from symbols.json for ::java::data::worldgen::attribute::modifier::ListModifier
Local link to file: vanilla_mcdoc/data/worldgen/attribute/modifier/ListModifier.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.attribute.modifier.ListModifierType import ListModifierType


E = TypeVar('E')


class ListModifier(GeneratedModel, Generic[E]):
    modifier: ListModifierType
    argument: list[E]
