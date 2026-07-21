# Generated from symbols.json for ::java::data::slot_source::TypedSlotSource
from dataclasses import dataclass


@dataclass(kw_only=True)
class TypedSlotSource:
    type: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::slot_source::TypedSlotSource": {
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
                                    "value": "slot_source_type"
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
                    "registry": "minecraft:slot_source"
                }
            }
        ]
    }
}

