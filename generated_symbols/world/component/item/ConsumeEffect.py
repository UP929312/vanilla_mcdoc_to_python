# Generated from symbols.json for ::java::world::component::item::ConsumeEffect
from dataclasses import dataclass


@dataclass(kw_only=True)
class ConsumeEffect:
    type: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::ConsumeEffect": {
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
                                    "value": "consume_effect_type"
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
                    "registry": "minecraft:consume_effect"
                }
            }
        ]
    }
}

