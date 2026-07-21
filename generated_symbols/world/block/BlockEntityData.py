# Generated from symbols.json for ::java::world::block::BlockEntityData
from dataclasses import dataclass


@dataclass(kw_only=True)
class BlockEntityData:
    id: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::BlockEntityData": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
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
                                    "value": "block_entity_type"
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
                    "registry": "minecraft:block_entity"
                }
            }
        ]
    }
}

