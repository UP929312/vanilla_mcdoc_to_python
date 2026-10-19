"""
Generated from symbols.json for ::java::data::worldgen::attribute::modifier::ColorAttributeModifier
Local link to file: vanilla_mcdoc/data/worldgen/attribute/modifier/ColorAttributeModifier.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Literal

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.attribute.modifier.BlendToGray import BlendToGray
    from vanilla_mcdoc.data.worldgen.attribute.modifier.ColorModifierType import ColorModifierType
    from vanilla_mcdoc.data.worldgen.attribute.modifier.LenientStringARGB import LenientStringARGB
    from vanilla_mcdoc.util.color.StringRGB import StringRGB


class ColorAttributeModifierDefault(GeneratedModel):
    modifier: ColorModifierType
    argument: StringRGB


class ColorAttributeModifierUnknown(GeneratedModel):
    modifier: ColorModifierType
    argument: StringRGB


class ColorAttributeModifierAlphaBlend(GeneratedModel):
    modifier: Literal['minecraft:alpha_blend', 'alpha_blend'] = 'minecraft:alpha_blend'
    argument: LenientStringARGB


class ColorAttributeModifierBlendToGray(GeneratedModel):
    modifier: Literal['minecraft:blend_to_gray', 'blend_to_gray'] = 'minecraft:blend_to_gray'
    argument: BlendToGray


class ColorAttributeModifierOverride(GeneratedModel):
    modifier: Literal['minecraft:override', 'override'] = 'minecraft:override'
    argument: StringRGB


type ColorAttributeModifier = ColorAttributeModifierDefault | ColorAttributeModifierUnknown | ColorAttributeModifierAlphaBlend | ColorAttributeModifierBlendToGray | ColorAttributeModifierOverride
