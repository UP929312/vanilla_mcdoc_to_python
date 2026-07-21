# Generated from symbols.json for ::java::world::entity::mob::breedable::villager::VillagerData
from dataclasses import dataclass


@dataclass(kw_only=True)
class VillagerData:
    level: int | None = None  # Used for trading and badge rendering.
    profession: str | None = None
    type: str | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::villager::VillagerData": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Used for trading and badge rendering.",
                "key": "level",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "profession",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "villager_profession"
                                }
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "villager_type"
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

