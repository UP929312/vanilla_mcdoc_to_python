# Generated from symbols.json for ::java::world::entity::mob::creeper::Creeper
from dataclasses import dataclass
from generated_symbols.world.entity.mob.MobBase import MobBase


@dataclass(kw_only=True)
class Creeper(MobBase):
    powered: bool | None = None  # Whether it is being struck by lightning.
    ExplosionRadius: int | None = None  # Radius of the explosion.
    Fuse: int | None = None  # Ticks until it explodes.
    ignited: bool | None = None  # Whether it was lit with flint and steel.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::creeper::Creeper": {
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
                "desc": "Whether it is being struck by lightning.",
                "key": "powered",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Radius of the explosion.",
                "key": "ExplosionRadius",
                "type": {
                    "kind": "byte"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Ticks until it explodes.",
                "key": "Fuse",
                "type": {
                    "kind": "short"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether it was lit with flint and steel.",
                "key": "ignited",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

