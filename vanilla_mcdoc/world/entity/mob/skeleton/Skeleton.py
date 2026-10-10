"""
Generated from symbols.json for ::java::world::entity::mob::skeleton::Skeleton
Local link to file: vanilla_mcdoc/world/entity/mob/skeleton/Skeleton.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.entity.mob.MobBase import MobBase


class Skeleton(MobBase):
    StrayConversionTime: int | None = None  # Time until it converts to a stray.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::skeleton::Skeleton": {
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
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.17"
                            }
                        }
                    }
                ],
                "desc": "Time until it converts to a stray.",
                "key": "StrayConversionTime",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}
