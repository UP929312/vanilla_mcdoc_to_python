# Generated from symbols.json for ::java::world::entity::experience_orb::ExperienceOrb
from dataclasses import dataclass
from generated_symbols.world.entity.EntityBase import EntityBase


@dataclass(kw_only=True)
class ExperienceOrb(EntityBase):
    Age: int | None = None  # Ticks that it has existed.
    Health: int | None = None
    Value: int | None = None  # Amount of experience it will give.
    Count: int | None = None  # Remaining number of times that the orb can be picked up. When the orb is picked up, the value decreases by 1. When multiple orbs are merged, their values are added up to result orb. When the value reaches 0, the orb is depleted.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::experience_orb::ExperienceOrb": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::EntityBase"
                }
            },
            {
                "kind": "pair",
                "desc": "Ticks that it has existed.",
                "key": "Age",
                "type": {
                    "kind": "short"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "Health",
                "type": {
                    "kind": "short"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Amount of experience it will give.",
                "key": "Value",
                "type": {
                    "kind": "short"
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
                                "value": "1.17"
                            }
                        }
                    }
                ],
                "desc": "Remaining number of times that the orb can be picked up.\nWhen the orb is picked up, the value decreases by 1.\nWhen multiple orbs are merged, their values are added up to result orb.\nWhen the value reaches 0, the orb is depleted.",
                "key": "Count",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}

