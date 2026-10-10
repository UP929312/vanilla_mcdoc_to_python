"""
Generated from symbols.json for ::java::data::loot::function::AttributeModifier
Local link to file: vanilla_mcdoc/data/loot/function/AttributeModifier.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.number_provider.FloatNumberProviderRef import FloatNumberProviderRef
    from vanilla_mcdoc.util.attribute.AttributeOperation import AttributeOperation
    from vanilla_mcdoc.util.slot.EquipmentSlotGroup import EquipmentSlotGroup


class AttributeModifier(GeneratedModel):
    attribute: Annotated[str, IdSpec(registry='attribute')]  # Attribute type to modify.
    id: Annotated[str, IdSpec(registry='attribute_modifier')]  # The unique identifier of this attribute modifier.
    amount: FloatNumberProviderRef
    operation: AttributeOperation  # The operation used for this modifier.
    slot: EquipmentSlotGroup | list[EquipmentSlotGroup]  # If a list, one of the listed slots will be chosen randomly.
