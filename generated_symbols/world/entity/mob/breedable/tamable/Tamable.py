# Generated from symbols.json for ::java::world::entity::mob::breedable::tamable::Tamable
from dataclasses import dataclass
from generated_symbols.world.entity.mob.breedable.Breedable import Breedable


@dataclass(kw_only=True)
class Tamable(Breedable):
    Owner: tuple[int, int, int, int] | None = None
    Sitting: bool | None = None  # Whether the mob is sitting.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::tamable::Tamable": {
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
                "desc": "Whether the mob is sitting.",
                "key": "Sitting",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

