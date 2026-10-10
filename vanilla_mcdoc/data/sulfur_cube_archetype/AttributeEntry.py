"""
Generated from symbols.json for ::java::data::sulfur_cube_archetype::AttributeEntry
Local link to file: vanilla_mcdoc/data/sulfur_cube_archetype/AttributeEntry.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.minecraft_types import IdSpec
from vanilla_mcdoc.world.entity.mob.ModernAttributeModifier import ModernAttributeModifier


class AttributeEntry(ModernAttributeModifier):
    attribute: Annotated[str, IdSpec(registry='attribute')]  # Attribute type to modify.
