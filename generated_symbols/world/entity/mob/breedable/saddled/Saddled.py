# Generated from symbols.json for ::java::world::entity::mob::breedable::saddled::Saddled
from dataclasses import dataclass
from generated_symbols.world.entity.mob.breedable.Breedable import Breedable


@dataclass(kw_only=True)
class Saddled(Breedable):
    pass


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::saddled::Saddled": {
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
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "desc": "Whether there is a saddle on it.",
                "key": "Saddle",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

