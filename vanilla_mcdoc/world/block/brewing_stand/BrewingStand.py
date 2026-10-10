"""
Generated from symbols.json for ::java::world::block::brewing_stand::BrewingStand
Local link to file: vanilla_mcdoc/world/block/brewing_stand/BrewingStand.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.world.block.BlockEntity import BlockEntity
from vanilla_mcdoc.world.block.Lockable import Lockable
from vanilla_mcdoc.world.block.Nameable import Nameable

if TYPE_CHECKING:
    from vanilla_mcdoc.util.slot.SlottedItem import SlottedItem


class BrewingStand(BlockEntity, Lockable, Nameable):
    Items: Annotated[list[SlottedItem[Annotated[int, Field(ge=0, le=4)]]], Field(min_length=0, max_length=5)] | None = None  # * 0: left brewing slot * 1: middle brewing slot * 2: right brewing slot * 3: ingredient slot * 4: fuel slot
    BrewTime: int | None = None  # Number of ticks until the brewing is complete.
    Fuel: int | None = None  # Amount of fuel the brewing stand has left.
    total_brew_time: int | None = None  # The total amount of time the current brewing process will take. Defaults to `400`.
    total_fuel: int | None = None  # The amount of fuel that was added in the last refuel. Defaults to `20`.
    speed_multiplier: float | None = None  # Used to speed up or slow down the next brewing process. Defaults to `1`.
