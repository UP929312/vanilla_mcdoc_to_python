"""
Generated from symbols.json for ::java::data::enchantment::effect::AttributeEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect/AttributeEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.LevelBasedValue import LevelBasedValue
    from vanilla_mcdoc.util.attribute.AttributeOperation import AttributeOperation


class AttributeEffect(GeneratedModel):
    attribute: Annotated[str, IdSpec(registry='attribute')]
    id: Annotated[str, IdSpec(registry='attribute_modifier')]  # Used when equipping and unequipping the item to identify which modifier to add or remove from the entity.  Postfixed with the slot name when the enchanted item is equipped.
    amount: LevelBasedValue  # Change in the attribute.
    operation: AttributeOperation  # The attribute operation to use.
