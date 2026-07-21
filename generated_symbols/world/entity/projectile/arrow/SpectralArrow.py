# Generated from symbols.json for ::java::world::entity::projectile::arrow::SpectralArrow
from dataclasses import dataclass
from generated_symbols.world.entity.projectile.arrow.ArrowBase import ArrowBase


@dataclass(kw_only=True)
class SpectralArrow(ArrowBase):
    Duration: int | None = None  # Ticks the glowing effect lasts.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::projectile::arrow::SpectralArrow": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::projectile::arrow::ArrowBase"
                }
            },
            {
                "kind": "pair",
                "desc": "Ticks the glowing effect lasts.",
                "key": "Duration",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}

