"""
Generated from symbols.json for ::java::world::entity::minecart::HopperMinecart
Local link to file: vanilla_mcdoc/world/entity/minecart/HopperMinecart.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.world.entity.minecart.ContainerMinecart import ContainerMinecart
from vanilla_mcdoc.world.entity.minecart.Minecart import Minecart

if TYPE_CHECKING:
    from vanilla_mcdoc.util.slot.SlottedItem import SlottedItem


class HopperMinecart(ContainerMinecart, Minecart):
    Items: Annotated[list[SlottedItem[Annotated[int, Field(ge=0, le=4)]]], Field(min_length=0, max_length=5)] | None = None  # Slots from 0 to 4.
    TransferCooldown: int | None = None  # Ticks until an item can be transferred.
    Enabled: bool | None = None  # Whether it should pick up items.
