"""
Generated from symbols.json for ::java::data::worldgen::attribute::modifier::TranslucentColorAttributeModifier
Local link to file: vanilla_mcdoc/data/worldgen/attribute/modifier/TranslucentColorAttributeModifier.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.attribute.modifier.BlendToGray import BlendToGray
    from vanilla_mcdoc.data.worldgen.attribute.modifier.ColorModifierType import ColorModifierType
    from vanilla_mcdoc.util.color.StringARGB import StringARGB
    from vanilla_mcdoc.util.color.StringRGB import StringRGB


class TranslucentColorAttributeModifier(GeneratedModel):
    modifier: ColorModifierType
    argument: StringARGB | StringRGB | BlendToGray | StringRGB | StringARGB
