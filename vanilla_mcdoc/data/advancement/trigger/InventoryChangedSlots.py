"""
Generated from symbols.json for ::java::data::advancement::trigger::InventoryChangedSlots
Local link to file: vanilla_mcdoc/data/advancement/trigger/InventoryChangedSlots.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds


class InventoryChangedSlots(GeneratedModel):
    empty: MinMaxBounds[int] | int | None = None  # Amount of empty slots.
    occupied: MinMaxBounds[int] | int | None = None  # Amount of occupied slots.
    full: MinMaxBounds[int] | int | None = None  # Amount of slots that are a full stack.
