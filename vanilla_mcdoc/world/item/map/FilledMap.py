"""
Generated from symbols.json for ::java::world::item::map::FilledMap
Local link to file: vanilla_mcdoc/world/item/map/FilledMap.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.world.item.Display import Display
from vanilla_mcdoc.world.item.ItemBase import ItemBase
from vanilla_mcdoc.world.item.map.Decoration import Decoration


class DecorationsStruct(Decoration):
    id: str  # An arbitrary unique string identifying the decoration.


class DisplayStruct(Display):
    MapColor: int | None = None  # Calculated as `RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive.


class FilledMap(ItemBase):
    map: int | None = None  # Map number, representing the shared state holding map contents and markers.
    map_scale_direction: Annotated[int, Field(ge=1)] | None = None  # Amount to increase the current map scale by when crafting.
    map_to_lock: bool | None = None  # Whether the map should be locked after being taken out of the cartography table.
    Decorations: list[DecorationsStruct] | None = None  # Decorations on the map.
    display: DisplayStruct | None = None  # Display for the item.
