"""
Generated from symbols.json for ::java::world::block::furnace::Furnace
Local link to file: vanilla_mcdoc/world/block/furnace/Furnace.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.minecraft_types import IdSpec
from vanilla_mcdoc.world.block.BlockEntity import BlockEntity
from vanilla_mcdoc.world.block.Lockable import Lockable
from vanilla_mcdoc.world.block.Nameable import Nameable

if TYPE_CHECKING:
    from vanilla_mcdoc.util.slot.SlottedItem import SlottedItem


class Furnace(BlockEntity, Lockable, Nameable):
    Items: Annotated[list[SlottedItem[Annotated[int, Field(ge=0, le=2)]]], Field(min_length=0, max_length=3)] | None = None  # The items in this furnace, with slots: * 0: Item being smelted * 1: Fuel * 2: Output
    cooking_total_time: int | None = None  # The total amount of time the current cooking process will take. Defaults to `0`.
    cooking_time_spent: int | None = None  # The amount of time that the current cooking process has taken so far. Defaults to `0`.
    lit_time_remaining: int | None = None  # The amount of burn time remaining. Defaults to `0`.
    lit_total_time: int | None = None  # The total amount of burn time that was added in the last refuel. Defaults to `0`.
    speed_multiplier: float | None = None  # Used to speed up or slow down the next cooking process. Defaults to `1`.
    RecipesUsed: dict[Annotated[str, IdSpec(registry='recipe')], int] | None = None  # Recipes that have been used since the last time a result item was removed from the GUI. Used to calculate the experience to give to the player.
