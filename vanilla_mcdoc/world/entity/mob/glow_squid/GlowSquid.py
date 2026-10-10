"""
Generated from symbols.json for ::java::world::entity::mob::glow_squid::GlowSquid
Local link to file: vanilla_mcdoc/world/entity/mob/glow_squid/GlowSquid.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.entity.mob.AgeableMob import AgeableMob
from vanilla_mcdoc.world.entity.mob.MobBase import MobBase


class GlowSquid(AgeableMob, MobBase):
    DarkTicksRemaining: int | None = None  # Ticks that it will wait before glowing.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::glow_squid::GlowSquid": {
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
                "kind": "spread",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.2"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::AgeableMob"
                }
            },
            {
                "kind": "pair",
                "desc": "Ticks that it will wait before glowing.",
                "key": "DarkTicksRemaining",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}
