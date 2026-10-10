"""
Generated from symbols.json for ::java::data::worldgen::attribute::DiscreteAttribute
Local link to file: vanilla_mcdoc/data/worldgen/attribute/DiscreteAttribute.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Generic, Literal, TypeVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.data.timeline.AttributeTrackBase import AttributeTrackBase

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.attribute.modifier.OverrideModifier import OverrideModifier


T = TypeVar('T')


class KeyframesStruct(GeneratedModel, Generic[T]):
    ticks: Annotated[int, Field(ge=0)]
    value: T


class AttributeTrackStruct(AttributeTrackBase, Generic[T]):
    modifier: Literal['override'] | None = 'override'
    keyframes: Annotated[list[KeyframesStruct[T]], Field(min_length=1)]


class DiscreteAttribute(GeneratedModel, Generic[T]):
    value: T
    modifier: OverrideModifier[T]
    attribute_track: AttributeTrackStruct[T]
