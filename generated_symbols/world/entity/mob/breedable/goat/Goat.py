# Generated from symbols.json for ::java::world::entity::mob::breedable::goat::Goat
from dataclasses import dataclass
from generated_symbols.world.entity.mob.breedable.Breedable import Breedable


@dataclass(kw_only=True)
class Goat(Breedable):
    HasLeftHorn: bool | None = None  # Whether it has its left horn.
    HasRightHorn: bool | None = None  # Whether it has its right horn.
    IsScreamingGoat: bool | None = None  # Whether it is a screaming goat.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::goat::Goat": {
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
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "desc": "Whether it has its left horn.",
                "key": "HasLeftHorn",
                "type": {
                    "kind": "boolean"
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
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "desc": "Whether it has its right horn.",
                "key": "HasRightHorn",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether it is a screaming goat.",
                "key": "IsScreamingGoat",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

