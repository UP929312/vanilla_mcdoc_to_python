"""
Generated from symbols.json for ::java::world::item::debug_stick::DebugStick
Local link to file: vanilla_mcdoc/world/item/debug_stick/DebugStick.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.item.ItemBase import ItemBase

if TYPE_CHECKING:
    from vanilla_mcdoc.world.component.item.DebugStickState import DebugStickState


class DebugStick(ItemBase):
    DebugProperty: DebugStickState | None = None
