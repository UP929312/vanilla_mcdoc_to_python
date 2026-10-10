"""
Generated from symbols.json for ::java::world::item::AttributeModifier
Local link to file: vanilla_mcdoc/world/item/AttributeModifier.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec, MinecraftUUID

if TYPE_CHECKING:
    from vanilla_mcdoc.util.attribute.LegacyOperation import LegacyOperation
    from vanilla_mcdoc.util.slot.EquipmentSlotGroup import EquipmentSlotGroup


class AttributeModifier(GeneratedModel):
    AttributeName: Annotated[str, IdSpec(registry='attribute')] | None = None
    Name: str | None = None  # Identifying name of the modifier, has no real effect.
    Slot: EquipmentSlotGroup | None = None  # Slot that the modifier is active in.
    Operation: LegacyOperation | None = None
    Amount: float | None = None  # Change in the attribute.
    UUID: MinecraftUUID | None = None
