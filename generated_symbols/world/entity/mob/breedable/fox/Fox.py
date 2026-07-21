# Generated from symbols.json for ::java::world::entity::mob::breedable::fox::Fox
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.entity.mob.breedable.Breedable import Breedable

if TYPE_CHECKING:
    from generated_symbols.world.component.entity.FoxType import FoxType


@dataclass(kw_only=True)
class Fox(Breedable):
    Trusted: list[tuple[int, int, int, int]] | None = None  # List of trusted players.
    Sleeping: bool | None = None  # Whether it is sleeping.
    Type: FoxType | None = None  # The type of fox.
    Sitting: bool | None = None  # Whether it is sitting.
    Crouching: bool | None = None  # Whether it is crouching.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::fox::Fox": {
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
                "desc": "List of trusted players.",
                "key": "TrustedUUIDs",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::world::entity::mob::breedable::fox::TrustedUUID",
                        "attributes": [
                            {
                                "name": "uuid"
                            }
                        ]
                    }
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
                "desc": "List of trusted players.",
                "key": "Trusted",
                "type": {
                    "kind": "list",
                    "item": {
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
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether it is sleeping.",
                "key": "Sleeping",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The type of fox.",
                "key": "Type",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::entity::FoxType"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether it is sitting.",
                "key": "Sitting",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether it is crouching.",
                "key": "Crouching",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

