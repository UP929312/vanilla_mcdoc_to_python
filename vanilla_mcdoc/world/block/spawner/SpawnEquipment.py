"""
Generated from symbols.json for ::java::world::block::spawner::SpawnEquipment
Local link to file: vanilla_mcdoc/world/block/spawner/SpawnEquipment.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.util.slot.EquipmentSlot import EquipmentSlot


class SpawnEquipment(GeneratedModel):
    loot_table: Annotated[str, IdSpec(registry='loot_table')]  # Generates the equipment.
    slot_drop_chances: Annotated[float, Field(ge=0, le=1)] | dict[EquipmentSlot, Annotated[float, Field(ge=0, le=1)]]  # Chance the mob will drop the equipment on death.
