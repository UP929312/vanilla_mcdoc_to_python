"""
Generated from symbols.json for ::java::world::entity::mob::DropChances
Local link to file: vanilla_mcdoc/world/entity/mob/DropChances.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

if TYPE_CHECKING:
    from vanilla_mcdoc.util.slot.EquipmentSlot import EquipmentSlot


type DropChances = dict[EquipmentSlot, Annotated[float, Field(ge=0)]]
