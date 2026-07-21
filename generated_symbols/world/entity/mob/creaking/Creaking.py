# Generated from symbols.json for ::java::world::entity::mob::creaking::Creaking
from dataclasses import dataclass
from generated_symbols.world.entity.mob.MobBase import MobBase


@dataclass(kw_only=True)
class Creaking(MobBase):
    home_pos: tuple[int, int, int] | None = None  # The creaking heart block that this is linked to.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::creaking::Creaking": {
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
                                "value": "1.21.4"
                            }
                        }
                    }
                ],
                "desc": "The creaking heart block that this is linked to.",
                "key": "home_pos",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "int"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
                    }
                },
                "optional": True
            }
        ]
    }
}

