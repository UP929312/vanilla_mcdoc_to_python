"""
Generated from symbols.json for ::java::world::item::firework::Fireworks
Local link to file: vanilla_mcdoc/world/item/firework/Fireworks.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.item.firework.Explosion import Explosion


class Fireworks(GeneratedModel):
    Flight: int | None = None  # Duration of flight.
    Explosions: list[Explosion] | None = None
