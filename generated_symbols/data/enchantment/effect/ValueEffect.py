# Generated from symbols.json for ::java::data::enchantment::effect::ValueEffect
from dataclasses import dataclass


@dataclass(kw_only=True)
class ValueEffect:
    type: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect::ValueEffect": {
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
                                    "value": "enchantment_value_effect_type"
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
                    "registry": "minecraft:value_effect"
                }
            }
        ]
    }
}

