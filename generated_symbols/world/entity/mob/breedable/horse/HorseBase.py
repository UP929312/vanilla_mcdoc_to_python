# Generated from symbols.json for ::java::world::entity::mob::breedable::horse::HorseBase
from dataclasses import dataclass
from typing import Annotated
from generated_symbols.world.entity.mob.breedable.Breedable import Breedable


@dataclass(kw_only=True)
class HorseBase(Breedable):
    Bred: bool | None = None  # Unknown use. Remains `0` even if it was bred.
    EatingHaystack: bool | None = None  # Whether it is eating a haystack.
    Tame: bool | None = None  # Whether it has been tamed.
    Temper: Annotated[int, 'Range | `0`-`100` | both inclusive'] | None = None  # Higher values make it easier to tame. Increases with feeding.
    Owner: tuple[int, int, int, int] | None = None  # Player who tamed it.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::horse::HorseBase": {
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
                "desc": "Unknown use.\nRemains `0` even if it was bred.",
                "key": "Bred",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether it is eating a haystack.",
                "key": "EatingHaystack",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether it has been tamed.",
                "key": "Tame",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Higher values make it easier to tame. Increases with feeding.",
                "key": "Temper",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 100
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "desc": "Player who tamed it.",
                "key": "OwnerUUID",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "uuid"
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
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "desc": "Player who tamed it.",
                "key": "Owner",
                "type": {
                    "kind": "int_array",
                    "lengthRange": {
                        "kind": 0,
                        "min": 4,
                        "max": 4
                    },
                    "attributes": [
                        {
                            "name": "uuid"
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "key": "SaddleItem",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::ItemStack"
                },
                "optional": True
            }
        ]
    }
}

