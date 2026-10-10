"""
Generated from symbols.json for ::java::world::entity::mob::Attribute
Local link to file: vanilla_mcdoc/world/entity/mob/Attribute.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.world.entity.mob.AttributeModifier import AttributeModifier


class Attribute(GeneratedModel):
    id: Annotated[str, IdSpec(registry='attribute')] | None = None
    base: float | None = None
    modifiers: list[AttributeModifier] | None = None
