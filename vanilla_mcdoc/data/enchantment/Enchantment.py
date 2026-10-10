"""
Generated from symbols.json for ::java::data::enchantment::Enchantment
Local link to file: vanilla_mcdoc/data/enchantment/Enchantment.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.EnchantmentCost import EnchantmentCost
    from vanilla_mcdoc.data.enchantment.effect_component.EnchantmentEffectComponentMap import EnchantmentEffectComponentMap
    from vanilla_mcdoc.registry.KnownItemId import KnownItemId
    from vanilla_mcdoc.util.slot.EquipmentSlotGroup import EquipmentSlotGroup
    from vanilla_mcdoc.util.text.Text import Text


class Enchantment(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'enchantment'

    description: Text
    exclusive_set: Annotated[str, IdSpec(registry='enchantment', tags='allowed')] | list[Annotated[str, IdSpec(registry='enchantment')]] | None = None
    supported_items: Annotated[str, IdSpec(registry='item', tags='allowed')] | KnownItemId | list[Annotated[str, IdSpec(registry='item')] | KnownItemId]
    primary_items: Annotated[str, IdSpec(registry='item', tags='allowed')] | KnownItemId | list[Annotated[str, IdSpec(registry='item')] | KnownItemId] | None = None  # Item types for which this Enchantment shows up in Enchanting Tables and on traded equipment.  Must be a subset of `supported_items`.
    weight: Annotated[int, Field(ge=1, le=1024)]  # How commonly the Enchantment appears, compared to the total combined `weight` of all available Enchantments.
    max_level: Annotated[int, Field(ge=1, le=255)]  # Maximum level of the enchantment.
    min_cost: EnchantmentCost  # Minimum experience cost.
    max_cost: EnchantmentCost  # Maximum experience cost.
    anvil_cost: Annotated[int, Field(ge=0)]  # Halved when an Enchantment is added to a book. The effective fee is multiplied by the level of the Enchantment.
    slots: list[EquipmentSlotGroup]
    effects: EnchantmentEffectComponentMap | None = None
