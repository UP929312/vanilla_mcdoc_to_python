# Generated from symbols.json for ::java::data::enchantment::effect::SpawnParticlesEntityEffect
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.effect.ParticlePosition import ParticlePosition
    from generated_symbols.data.enchantment.effect.ParticleVelocity import ParticleVelocity
    from generated_symbols.util.particle.Particle import Particle


@dataclass(kw_only=True)
class SpawnParticlesEntityEffect:
    particle: Particle
    horizontal_position: ParticlePosition
    vertical_position: ParticlePosition
    horizontal_velocity: ParticleVelocity
    vertical_velocity: ParticleVelocity
    speed: float | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect::SpawnParticlesEntityEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "particle",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::particle::Particle"
                }
            },
            {
                "kind": "pair",
                "key": "horizontal_position",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::effect::ParticlePosition"
                }
            },
            {
                "kind": "pair",
                "key": "vertical_position",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::effect::ParticlePosition"
                }
            },
            {
                "kind": "pair",
                "key": "horizontal_velocity",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::effect::ParticleVelocity"
                }
            },
            {
                "kind": "pair",
                "key": "vertical_velocity",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::effect::ParticleVelocity"
                }
            },
            {
                "kind": "pair",
                "key": "speed",
                "type": {
                    "kind": "float"
                },
                "optional": True
            }
        ]
    }
}

