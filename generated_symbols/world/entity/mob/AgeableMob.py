# Generated from symbols.json for ::java::world::entity::mob::AgeableMob
from dataclasses import dataclass


@dataclass(kw_only=True)
class AgeableMob:
    Age: int | None = None  # The age of the mob in ticks. When negative, the mob is a baby. When 0 or above, the mob is an adult. If this mob is breedable, when 0 or above, represents the number of ticks before it can breed again.
    ForcedAge: int | None = None  # A value of age assigned to this mob when it grows up. Incremented when a baby mob is fed.
    AgeLocked: bool | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::AgeableMob": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The age of the mob in ticks. When negative, the mob is a baby. When 0 or above, the mob is an adult.\nIf this mob is breedable, when 0 or above, represents the number of ticks before it can breed again.",
                "key": "Age",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "A value of age assigned to this mob when it grows up.\nIncremented when a baby mob is fed.",
                "key": "ForcedAge",
                "type": {
                    "kind": "int"
                },
                "optional": True
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
                                "value": "26.1"
                            }
                        }
                    }
                ],
                "key": "AgeLocked",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

