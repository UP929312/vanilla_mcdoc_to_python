"""
Generated from symbols.json for ::java::data::worldgen::attribute::ARGBColorAttribute
Local link to file: vanilla_mcdoc/data/worldgen/attribute/ARGBColorAttribute.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.data.timeline.AttributeTrackBase import AttributeTrackBase

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.attribute.modifier.BlendToGray import BlendToGray
    from vanilla_mcdoc.data.worldgen.attribute.modifier.ColorModifierType import ColorModifierType
    from vanilla_mcdoc.data.worldgen.attribute.modifier.TranslucentColorAttributeModifier import TranslucentColorAttributeModifier
    from vanilla_mcdoc.util.color.StringARGB import StringARGB
    from vanilla_mcdoc.util.color.StringRGB import StringRGB


class KeyframesStruct(GeneratedModel):
    ticks: Annotated[int, Field(ge=0)]
    value: StringARGB | StringRGB | BlendToGray | StringRGB | StringARGB


class AttributeTrackStruct(AttributeTrackBase):
    modifier: ColorModifierType | None = None
    keyframes: Annotated[list[KeyframesStruct], Field(min_length=1)]


class ARGBColorAttribute(GeneratedModel):
    value: StringARGB
    modifier: TranslucentColorAttributeModifier
    attribute_track: AttributeTrackStruct
