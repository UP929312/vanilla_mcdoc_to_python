"""
Generated from symbols.json for ::java::world::item::firework::Explosion
Local link to file: vanilla_mcdoc/world/item/firework/Explosion.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.item.firework.ExplosionType import ExplosionType


class Explosion(GeneratedModel):
    Flicker: bool | None = None  # Whether the explosion should flicker.
    Trail: bool | None = None  # Whether the explosion should have a trail.
    Type: ExplosionType | None = None
    Colors: list[int] | None = None  # Colors of the explosion. Calculated as `RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive.
    FadeColors: list[int] | None = None  # Colors of the explosion fade. Calculated as `RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive.
