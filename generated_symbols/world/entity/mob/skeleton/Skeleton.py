# Generated from symbols.json for ::java::world::entity::mob::skeleton::Skeleton
from dataclasses import dataclass
from generated_symbols.world.entity.mob.MobBase import MobBase


@dataclass(kw_only=True)
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

