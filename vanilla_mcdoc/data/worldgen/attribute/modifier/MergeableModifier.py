"""
Generated from symbols.json for ::java::data::worldgen::attribute::modifier::MergeableModifier
Local link to file: vanilla_mcdoc/data/worldgen/attribute/modifier/MergeableModifier.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Any, Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.attribute.modifier.MergeableModifierType import MergeableModifierType


T = TypeVar('T', default=Any)


class MergeableModifier(GeneratedModel, Generic[T]):
    modifier: MergeableModifierType
    argument: T
