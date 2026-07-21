# Generated from symbols.json for ::java::data::variants::SpawnCondition
from dataclasses import dataclass


@dataclass(kw_only=True)
class SpawnCondition:
    type: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::variants::SpawnCondition": {
        "kind": "struct",
        "fields": [
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
                                    "value": "spawn_condition_type"
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
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:spawn_condition"
                }
            }
        ]
    }
}

