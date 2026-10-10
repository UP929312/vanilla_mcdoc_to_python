"""
Generated from symbols.json for ::java::data::worldgen::attribute::modifier::FloatAttributeModifier
Local link to file: vanilla_mcdoc/data/worldgen/attribute/modifier/FloatAttributeModifier.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.attribute.modifier.FloatModifierType import FloatModifierType
    from vanilla_mcdoc.data.worldgen.attribute.modifier.FloatWithAlpha import FloatWithAlpha


T = TypeVar('T')


class FloatAttributeModifier(GeneratedModel, Generic[T]):
    modifier: FloatModifierType
    argument: T | float | FloatWithAlpha
