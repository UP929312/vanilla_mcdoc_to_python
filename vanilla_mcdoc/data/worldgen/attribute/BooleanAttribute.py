"""
Generated from symbols.json for ::java::data::worldgen::attribute::BooleanAttribute
Local link to file: vanilla_mcdoc/data/worldgen/attribute/BooleanAttribute.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.data.timeline.AttributeTrackBase import AttributeTrackBase

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.attribute.modifier.BooleanAttributeModifier import BooleanAttributeModifier
    from vanilla_mcdoc.data.worldgen.attribute.modifier.BooleanModifierType import BooleanModifierType


class KeyframesStruct(GeneratedModel):
    ticks: Annotated[int, Field(ge=0)]
    value: bool


class AttributeTrackStruct(AttributeTrackBase):
    modifier: BooleanModifierType | None = None
    keyframes: Annotated[list[KeyframesStruct], Field(min_length=1)]


class BooleanAttribute(GeneratedModel):
    value: bool
    modifier: BooleanAttributeModifier
    attribute_track: AttributeTrackStruct
