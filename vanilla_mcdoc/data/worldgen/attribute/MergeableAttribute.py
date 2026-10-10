"""
Generated from symbols.json for ::java::data::worldgen::attribute::MergeableAttribute
Local link to file: vanilla_mcdoc/data/worldgen/attribute/MergeableAttribute.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Generic, TypeVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.data.timeline.AttributeTrackBase import AttributeTrackBase

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.attribute.modifier.MergeableModifier import MergeableModifier
    from vanilla_mcdoc.data.worldgen.attribute.modifier.MergeableModifierType import MergeableModifierType


T = TypeVar('T')


class KeyframesStruct(GeneratedModel, Generic[T]):
    ticks: Annotated[int, Field(ge=0)]
    value: T


class AttributeTrackStruct(AttributeTrackBase, Generic[T]):
    modifier: MergeableModifierType | None = None
    keyframes: Annotated[list[KeyframesStruct[T]], Field(min_length=1)]


class MergeableAttribute(GeneratedModel, Generic[T]):
    value: T
    modifier: MergeableModifier[T]
    attribute_track: AttributeTrackStruct[T]
