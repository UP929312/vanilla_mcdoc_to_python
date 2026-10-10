"""
Generated from symbols.json for ::java::world::entity::minecart::ChestMinecart
Local link to file: vanilla_mcdoc/world/entity/minecart/ChestMinecart.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.world.entity.minecart.ContainerMinecart import ContainerMinecart
from vanilla_mcdoc.world.entity.minecart.Minecart import Minecart

if TYPE_CHECKING:
    from vanilla_mcdoc.util.slot.SlottedItem import SlottedItem


class ChestMinecart(ContainerMinecart, Minecart):
    Items: Annotated[list[SlottedItem[Annotated[int, Field(ge=0, le=26)]]], Field(min_length=0, max_length=27)] | None = None  # Slots from 0 to 26.
