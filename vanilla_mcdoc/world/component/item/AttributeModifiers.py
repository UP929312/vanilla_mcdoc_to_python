"""
Generated from symbols.json for ::java::world::component::item::AttributeModifiers
Local link to file: vanilla_mcdoc/world/component/item/AttributeModifiers.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.component.item.AttributeModifier import AttributeModifier


class AttributeModifiers(GeneratedModel):
    modifiers: list[AttributeModifier]
    show_in_tooltip: bool | None = None
