# Generated from symbols.json for ::java::world::entity::AnyEntity
from dataclasses import dataclass


@dataclass(kw_only=True)
class AnyEntity:
    id: str  # The ID of this entity. Not present on player entities.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::AnyEntity": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The ID of this entity. Not present on player entities.",
                "key": "id",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "entity_type"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "id"
                            ]
                        }
                    ],
                    "registry": "minecraft:entity"
                }
            }
        ]
    }
}

