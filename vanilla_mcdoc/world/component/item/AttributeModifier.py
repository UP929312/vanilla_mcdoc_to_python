"""
Generated from symbols.json for ::java::world::component::item::AttributeModifier
Local link to file: vanilla_mcdoc/world/component/item/AttributeModifier.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.util.attribute.AttributeOperation import AttributeOperation
    from vanilla_mcdoc.util.slot.EquipmentSlotGroup import EquipmentSlotGroup
    from vanilla_mcdoc.world.component.item.AttributeDisplay import AttributeDisplay


class AttributeModifier(GeneratedModel):
    type: Annotated[str, IdSpec(registry='attribute')]
    id: Annotated[str, IdSpec(registry='attribute_modifier')]  # Used when equipping and unequipping the item to identify which modifier to add or remove from the entity.
    amount: float  # Change in the attribute.
    operation: AttributeOperation
    slot: EquipmentSlotGroup | None = None  # Slot or slot type the item must be in for the modifier to take effect. Defaults to `any`.
    display: AttributeDisplay | None = None  # Controls how this modifier is shown in the item tooltip.
