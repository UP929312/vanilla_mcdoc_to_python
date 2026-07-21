# Generated from symbols.json for ::java::world::entity::mob::wither::Wither
from dataclasses import dataclass
from generated_symbols.world.entity.mob.MobBase import MobBase


@dataclass(kw_only=True)
class Wither(MobBase):
    Invul: int | None = None  # Ticks it is invulnerable for.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::wither::Wither": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::MobBase"
                }
            },
            {
                "kind": "pair",
                "desc": "Ticks it is invulnerable for.",
                "key": "Invul",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}

