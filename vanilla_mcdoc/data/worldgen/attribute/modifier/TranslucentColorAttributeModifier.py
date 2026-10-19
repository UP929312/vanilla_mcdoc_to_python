"""
Generated from symbols.json for ::java::data::worldgen::attribute::modifier::TranslucentColorAttributeModifier
Local link to file: vanilla_mcdoc/data/worldgen/attribute/modifier/TranslucentColorAttributeModifier.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Literal

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.attribute.modifier.BlendToGray import BlendToGray
    from vanilla_mcdoc.data.worldgen.attribute.modifier.ColorModifierType import ColorModifierType
    from vanilla_mcdoc.data.worldgen.attribute.modifier.LenientStringARGB import LenientStringARGB
    from vanilla_mcdoc.util.color.StringRGB import StringRGB


class TranslucentColorAttributeModifierDefault(GeneratedModel):
    modifier: ColorModifierType
    argument: LenientStringARGB


class TranslucentColorAttributeModifierAdd(GeneratedModel):
    modifier: Literal['minecraft:add', 'add'] = 'minecraft:add'
    argument: StringRGB


class TranslucentColorAttributeModifierAlphaBlend(GeneratedModel):
    modifier: Literal['minecraft:alpha_blend', 'alpha_blend'] = 'minecraft:alpha_blend'
    argument: LenientStringARGB


class TranslucentColorAttributeModifierBlendToGray(GeneratedModel):
    modifier: Literal['minecraft:blend_to_gray', 'blend_to_gray'] = 'minecraft:blend_to_gray'
    argument: BlendToGray


class TranslucentColorAttributeModifierMultiply(GeneratedModel):
    modifier: Literal['minecraft:multiply', 'multiply'] = 'minecraft:multiply'
    argument: LenientStringARGB


class TranslucentColorAttributeModifierOverride(GeneratedModel):
    modifier: Literal['minecraft:override', 'override'] = 'minecraft:override'
    argument: LenientStringARGB


class TranslucentColorAttributeModifierSubtract(GeneratedModel):
    modifier: Literal['minecraft:subtract', 'subtract'] = 'minecraft:subtract'
    argument: StringRGB


type TranslucentColorAttributeModifier = TranslucentColorAttributeModifierDefault | TranslucentColorAttributeModifierAdd | TranslucentColorAttributeModifierAlphaBlend | TranslucentColorAttributeModifierBlendToGray | TranslucentColorAttributeModifierMultiply | TranslucentColorAttributeModifierOverride | TranslucentColorAttributeModifierSubtract
