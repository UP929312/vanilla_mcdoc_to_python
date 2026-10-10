"""
Generated from symbols.json for ::java::data::enchantment::effect::ExplosionParticleInfo
Local link to file: vanilla_mcdoc/data/enchantment/effect/ExplosionParticleInfo.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.particle.Particle import Particle


class ExplosionParticleInfo(GeneratedModel):
    particle: Particle
    scaling: float | None = None  # Defaults to 1.0. Scaling of the distance between the center of the explosion and the block
    speed: float | None = None  # Defaults to 1.0. Scaling of the speed of the particle
