"""
Generated from symbols.json for ::java::data::enchantment::effect::ParticleVelocity
Local link to file: vanilla_mcdoc/data/enchantment/effect/ParticleVelocity.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class ParticleVelocity(GeneratedModel):
    base: float | None = None  # Defaults to 0.
    movement_scale: float | None = None  # Scale factor applied to the given axis (`1` adds the velocity of the entity to the spawned particles). Defaults to 0.
