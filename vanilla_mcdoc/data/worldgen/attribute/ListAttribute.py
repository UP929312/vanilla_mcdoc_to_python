"""
Generated from symbols.json for ::java::data::worldgen::attribute::ListAttribute
Local link to file: vanilla_mcdoc/data/worldgen/attribute/ListAttribute.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Generic, TypeVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.data.timeline.AttributeTrackBase import AttributeTrackBase

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.attribute.modifier.ListModifier import ListModifier
    from vanilla_mcdoc.data.worldgen.attribute.modifier.ListModifierType import ListModifierType


E = TypeVar('E')


class KeyframesStruct(GeneratedModel, Generic[E]):
    ticks: Annotated[int, Field(ge=0)]
    value: list[E]


class AttributeTrackStruct(AttributeTrackBase, Generic[E]):
    modifier: ListModifierType | None = None
    keyframes: Annotated[list[KeyframesStruct[E]], Field(min_length=1)]


class ListAttribute(GeneratedModel, Generic[E]):
    value: list[E]
    modifier: ListModifier[E]
    attribute_track: AttributeTrackStruct[E]
