"""
Generated from symbols.json for ::java::world::item::head::PlayerHead
Local link to file: vanilla_mcdoc/world/item/head/PlayerHead.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from pydantic import Field

from vanilla_mcdoc.world.item.ItemBase import ItemBase

if TYPE_CHECKING:
    from vanilla_mcdoc.world.block.head.SkullOwner import SkullOwner


class PlayerHead(ItemBase):
    SkullOwner_: SkullOwner | str | None = Field(default=None, alias='SkullOwner')
