# Generated from symbols.json for ::java::world::entity::mob::breedable::chicken::Chicken
from dataclasses import dataclass
from generated_symbols.world.entity.mob.breedable.Breedable import Breedable


@dataclass(kw_only=True)
class Chicken(Breedable):
    IsChickenJockey: bool | None = None  # Whether it is from a chicken jockey. If true it will despawn and will drop more experience.
    EggLayTime: int | None = None  # Time until it lays another egg.
    variant: str | None = None
    sound_variant: str | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::chicken::Chicken": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::breedable::Breedable"
                }
            },
            {
                "kind": "pair",
                "desc": "Whether it is from a chicken jockey.\nIf True it will despawn and will drop more experience.",
                "key": "IsChickenJockey",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Time until it lays another egg.",
                "key": "EggLayTime",
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
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "key": "variant",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "chicken_variant"
                                }
                            }
                        }
                    ]
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
                "key": "sound_variant",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "chicken_sound_variant"
                                }
                            }
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

