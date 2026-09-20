# ~~~ WHAT ARE WE TESTING ~~~

# Nested structs generated inside templates must retain their type arguments at use sites.

# ~~~ FILE CONTENT ~~~
"""
Generated from symbols.json for ::java::data::worldgen::attribute::MergeableAttribute
Local link to file: generated_symbols/data/worldgen/attribute/MergeableAttribute.py
"""
# ~~~ CODE ~~~
from pydantic import BaseModel
from typing import TYPE_CHECKING, Annotated, Generic, TypeVar

from generated_symbols.data.timeline.AttributeTrackBase import AttributeTrackBase

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.attribute.modifier.MergeableModifier import MergeableModifier
    from generated_symbols.data.worldgen.attribute.modifier.MergeableModifierType import MergeableModifierType


T = TypeVar('T')

class KeyframesStruct(BaseModel, Generic[T]):
    ticks: Annotated[int, 'Range | `0` and above | inclusive']
    value: T


class AttributeTrackStruct(AttributeTrackBase, Generic[T]):
    modifier: MergeableModifierType | None = None
    keyframes: Annotated[list[KeyframesStruct[T]], 'Length = 1 (inclusive) and above']


class MergeableAttribute(BaseModel, Generic[T]):
    value: T
    modifier: MergeableModifier[T]
    attribute_track: AttributeTrackStruct[T]


