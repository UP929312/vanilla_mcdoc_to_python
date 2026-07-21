# Generated from symbols.json for ::java::world::entity::mob::raider::Vindicator
from dataclasses import dataclass
from generated_symbols.world.entity.mob.raider.RaiderBase import RaiderBase


@dataclass(kw_only=True)
class Vindicator(RaiderBase):
    Johnny: bool | None = None  # Whether it should try to attack most other mobs.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::raider::Vindicator": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::raider::RaiderBase"
                }
            },
            {
                "kind": "pair",
                "desc": "Whether it should try to attack most other mobs.",
                "key": "Johnny",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

