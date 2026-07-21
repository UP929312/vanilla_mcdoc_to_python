# Generated from symbols.json for ::java::data::enchantment::effect::ParticleVelocity
from dataclasses import dataclass


@dataclass(kw_only=True)
class ParticleVelocity:
    base: float | None = None  # Defaults to 0.
    movement_scale: float | None = None  # Scale factor applied to the given axis (`1` adds the velocity of the entity to the spawned particles). Defaults to 0.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect::ParticleVelocity": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Defaults to 0.",
                "key": "base",
                "type": {
                    "kind": "float"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Scale factor applied to the given axis (`1` adds the velocity of the entity to the spawned particles). Defaults to 0.",
                "key": "movement_scale",
                "type": {
                    "kind": "float"
                },
                "optional": True
            }
        ]
    }
}

