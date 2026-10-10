"""
Generated from symbols.json for ::java::world::component::predicate::AttributeModifiersPredicateEntry
Local link to file: vanilla_mcdoc/world/component/predicate/AttributeModifiersPredicateEntry.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds
    from vanilla_mcdoc.util.attribute.AttributeOperation import AttributeOperation
    from vanilla_mcdoc.util.slot.EquipmentSlotGroup import EquipmentSlotGroup


class AttributeModifiersPredicateEntry(GeneratedModel):
    attribute: Annotated[str, IdSpec(registry='attribute', tags='allowed')] | list[Annotated[str, IdSpec(registry='attribute')]] | None = None
    id: Annotated[str, IdSpec(registry='attribute_modifier')] | None = None
    amount: MinMaxBounds[float] | float | None = None
    operation: AttributeOperation | None = None
    slot: EquipmentSlotGroup | None = None
