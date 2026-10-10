"""
Generated from symbols.json for ::java::world::entity::mob::raider::Vindicator
Local link to file: generated_symbols/world/entity/mob/raider/Vindicator.py
"""
# ~~~ CODE ~~~
from generated_symbols.world.entity.mob.raider.RaiderBase import RaiderBase


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
