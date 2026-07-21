# Generated from symbols.json for ::java::util::game_event::PositionSource
from dataclasses import dataclass


@dataclass(kw_only=True)
class PositionSource:
    type: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::game_event::PositionSource": {
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
                                    "value": "position_source_type"
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
                    "registry": "minecraft:position_source"
                }
            }
        ]
    }
}

