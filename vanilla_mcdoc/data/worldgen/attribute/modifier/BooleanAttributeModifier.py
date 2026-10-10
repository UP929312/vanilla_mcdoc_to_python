"""
Generated from symbols.json for ::java::data::worldgen::attribute::modifier::BooleanAttributeModifier
Local link to file: vanilla_mcdoc/data/worldgen/attribute/modifier/BooleanAttributeModifier.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.attribute.modifier.BooleanModifierType import BooleanModifierType


class BooleanAttributeModifier(GeneratedModel):
    modifier: BooleanModifierType
    argument: bool
