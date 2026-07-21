# Generated from symbols.json for ::java::world::entity::mob::endermite::Endermite
from dataclasses import dataclass
from generated_symbols.world.entity.mob.MobBase import MobBase


@dataclass(kw_only=True)
class Endermite(MobBase):
    Lifetime: int | None = None  # How long it has existed.
    PlayerSpawned: bool | None = None  # Whether enderman should attack it.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::endermite::Endermite": {
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
                "desc": "How long it has existed.",
                "key": "Lifetime",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether enderman should attack it.",
                "key": "PlayerSpawned",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

