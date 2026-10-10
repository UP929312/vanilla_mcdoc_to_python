"""
Generated from symbols.json for ::java::data::enchantment::effect::SpawnParticlesEntityEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect/SpawnParticlesEntityEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.effect.ParticlePosition import ParticlePosition
    from vanilla_mcdoc.data.enchantment.effect.ParticleVelocity import ParticleVelocity
    from vanilla_mcdoc.util.particle.Particle import Particle


class SpawnParticlesEntityEffect(GeneratedModel):
    particle: Particle
    horizontal_position: ParticlePosition
    vertical_position: ParticlePosition
    horizontal_velocity: ParticleVelocity
    vertical_velocity: ParticleVelocity
    speed: float | None = None
