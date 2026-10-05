# ~~~ WHAT ARE WE TESTING ~~~

# Nested structs generated inside templates must retain their type arguments at use sites.

# ~~~ FILE CONTENT ~~~
"""
Generated from symbols.json for ::java::data::worldgen::attribute::MergeableAttribute
Local link to file: generated_symbols/data/worldgen/attribute/MergeableAttribute.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Generic, TypeVar

from generated_symbols.base import GeneratedModel
from generated_symbols.data.timeline.AttributeTrackBase import AttributeTrackBase
from pydantic import Field

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.attribute.modifier.MergeableModifier import MergeableModifier
    from generated_symbols.data.worldgen.attribute.modifier.MergeableModifierType import MergeableModifierType


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
