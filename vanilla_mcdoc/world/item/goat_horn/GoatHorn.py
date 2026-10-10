"""
Generated from symbols.json for ::java::world::item::goat_horn::GoatHorn
Local link to file: vanilla_mcdoc/world/item/goat_horn/GoatHorn.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.minecraft_types import IdSpec
from vanilla_mcdoc.world.item.ItemBase import ItemBase


class GoatHorn(ItemBase):
    instrument: Annotated[str, IdSpec(registry='instrument')] | None = None
