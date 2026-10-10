"""
Generated from symbols.json for ::java::world::item::suspicious_stew::SuspiciousStew
Local link to file: vanilla_mcdoc/world/item/suspicious_stew/SuspiciousStew.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.item.ItemBase import ItemBase

if TYPE_CHECKING:
    from vanilla_mcdoc.world.item.suspicious_stew.Effect import Effect


class SuspiciousStew(ItemBase):
    Effects: list[Effect] | None = None  # Effects this stew will give.
