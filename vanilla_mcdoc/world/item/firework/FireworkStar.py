"""
Generated from symbols.json for ::java::world::item::firework::FireworkStar
Local link to file: vanilla_mcdoc/world/item/firework/FireworkStar.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from pydantic import Field

from vanilla_mcdoc.world.item.ItemBase import ItemBase

if TYPE_CHECKING:
    from vanilla_mcdoc.world.item.firework.Explosion import Explosion


class FireworkStar(ItemBase):
    Explosion_: Explosion | None = Field(default=None, alias='Explosion')
