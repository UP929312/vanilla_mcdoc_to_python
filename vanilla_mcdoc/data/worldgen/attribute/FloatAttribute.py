"""
Generated from symbols.json for ::java::data::worldgen::attribute::FloatAttribute
Local link to file: vanilla_mcdoc/data/worldgen/attribute/FloatAttribute.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Generic, TypeVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.data.timeline.AttributeTrackBase import AttributeTrackBase

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.attribute.modifier.FloatAttributeModifier import FloatAttributeModifier
    from vanilla_mcdoc.data.worldgen.attribute.modifier.FloatModifierType import FloatModifierType
    from vanilla_mcdoc.data.worldgen.attribute.modifier.FloatWithAlpha import FloatWithAlpha


T = TypeVar('T')


class KeyframesStruct(GeneratedModel, Generic[T]):
    ticks: Annotated[int, Field(ge=0)]
    value: T | float | FloatWithAlpha


class AttributeTrackStruct(AttributeTrackBase, Generic[T]):
    modifier: FloatModifierType | None = None
    keyframes: Annotated[list[KeyframesStruct[T]], Field(min_length=1)]


class FloatAttribute(GeneratedModel, Generic[T]):
    value: T
    modifier: FloatAttributeModifier[T]
    attribute_track: AttributeTrackStruct[T]
