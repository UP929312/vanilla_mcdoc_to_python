"""
Generated from symbols.json for ::java::world::component::item::Explosion
Local link to file: vanilla_mcdoc/world/component/item/Explosion.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.component.item.FireworkShape import FireworkShape


class Explosion(GeneratedModel):
    shape: FireworkShape  # The shape of the explosion.
    colors: list[int] | None = None  # Colors of the initial particles of the explosion, randomly selected from. Calculated as `RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive.
    fade_colors: list[int] | None = None  # Colors of the fading particles of the explosion
    has_trail: bool | None = None  # Added to a firework star via Diamond.
    has_twinkle: bool | None = None  # Added to a firework star via Glowstone Dust.
